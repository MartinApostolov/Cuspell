from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
import re
from typing import Iterable

from .language import Entry, Language
from .model import CheckResult, Diagnostic, Node
from .surface import split_fields, split_phrases, split_phrases_with_spans, split_top_level, strip_sentence_source
from .validator import validate_execution_closure, validate_semantics


_INFER_BINDER_TYPE = "__UnresolvedNativeBinder__"


@dataclass(frozen=True)
class Context:
    variables: tuple[tuple[str, str], ...] = ()
    in_event: bool = False
    old_name_stack: tuple[str, ...] = ()

    def variable_map(self) -> dict[str, str]:
        return dict(self.variables)

    def with_variable(self, name: str, typ: str) -> "Context":
        data = self.variable_map()
        data[name] = typ
        return replace(self, variables=tuple(sorted(data.items())))

    def with_event(self) -> "Context":
        return replace(self, in_event=True)

    def with_old_name(self, old_name_id: str) -> "Context":
        return replace(self, old_name_stack=self.old_name_stack + (old_name_id,))


@dataclass(frozen=True)
class Candidate:
    node: Node
    next_index: int


class Parser:
    def __init__(self, language: Language):
        self.language = language
        self._diagnostics: list[Diagnostic] = []
        self._fields: list[str] = []
        self._field_spans: list[tuple[int, int]] = []

    def check(self, source: str) -> CheckResult:
        self._diagnostics = []
        try:
            mood, body, body_start = strip_sentence_source(source)
        except ValueError as exc:
            return CheckResult(
                valid=False,
                source=source,
                mood="unknown",
                phrases=[],
                diagnostics=[Diagnostic("SyntaxError", str(exc))],
                mana=self.mana_cost(source),
            )

        body_pieces = split_phrases_with_spans(body)
        phrases = [piece.text for piece in body_pieces]
        mana = self.mana_cost(source)

        expected = {
            "command": "EventSpec",
            "assertion": "Proposition",
            "question": "Proposition",
        }[mood]

        parse_context = Context()
        open_binders: list[Node] = []
        parse_body = body
        parse_offset = body_start
        if mood == "question":
            consumed = 0
            for piece in body_pieces:
                token = piece.text
                if not self._is_binder_token(token):
                    break
                binder = self.parse_phrase(
                    body[piece.start:piece.end],
                    expected_type="Binder",
                    source_offset=body_start + piece.start,
                )
                if isinstance(binder, Diagnostic):
                    return CheckResult(
                        valid=False,
                        source=source,
                        mood=mood,
                        phrases=phrases,
                        diagnostics=[binder],
                        mana=mana,
                    )
                if binder.meta_dict().get("rune_native") and (
                    binder.name in parse_context.variable_map()
                ):
                    return CheckResult(
                        valid=False, source=source, mood=mood, phrases=phrases,
                        diagnostics=[Diagnostic(
                            "DuplicateBinder",
                            f"Rune label {binder.name} is already bound in this scope.",
                            field=token, source_start=body_start + piece.start,
                            source_end=body_start + piece.end,
                        )], mana=mana,
                    )
                open_binders.append(binder)
                binder_type = binder.meta_dict().get("bound_type", "Entity")
                if binder.meta_dict().get("rune_native") and binder_type == "Any":
                    binder_type = _INFER_BINDER_TYPE
                parse_context = parse_context.with_variable(binder.name or "?", binder_type)
                consumed += 1
            if open_binders:
                if consumed >= len(body_pieces):
                    end = body_start + len(body)
                    return CheckResult(
                        valid=False,
                        source=source,
                        mood=mood,
                        phrases=phrases,
                        diagnostics=[Diagnostic(
                            "SyntaxError",
                            "Open question binder has no query expression.",
                            source_start=end,
                            source_end=end,
                        )],
                        mana=mana,
                    )
                remainder_start = body_pieces[consumed].start
                parse_body = body[remainder_start:]
                parse_offset = body_start + remainder_start

        parse = self.parse_phrase(
            parse_body,
            expected_type=expected,
            context=parse_context,
            source_offset=parse_offset,
            resolve_external_binders=bool(open_binders),
        )
        if isinstance(parse, Diagnostic):
            return CheckResult(
                valid=False,
                source=source,
                mood=mood,
                phrases=phrases,
                diagnostics=[parse],
                mana=mana,
            )
        if open_binders:
            # The query has now committed the types of initially untyped
            # leading binders. Include these in its structured AST.
            resolved_names: dict[str, str] = {}
            def collect_resolved_variables(node: Node) -> None:
                if node.kind == "Variable" and node.meta_dict().get("inferred_type"):
                    resolved_names[node.name[1:]] = node.type
                for child in node.children:
                    collect_resolved_variables(child)
            collect_resolved_variables(parse)
            open_binders = [
                replace(
                    binder, value=f"inferred:{resolved_names[binder.name]}",
                    meta=(("bound_type", resolved_names[binder.name]),
                          ("rune_native", True), ("inferred_type", True)),
                ) if (
                    binder.meta_dict().get("rune_native")
                    and binder.meta_dict().get("bound_type") == "Any"
                    and binder.name in resolved_names
                ) else binder
                for binder in open_binders
            ]
            span_starts = [
                node.source_start for node in (*open_binders, parse)
                if node.source_start is not None
            ]
            span_ends = [
                node.source_end for node in (*open_binders, parse)
                if node.source_end is not None
            ]
            parse = Node(
                kind="OpenQuestion",
                type="QuestionContent",
                name="OpenQuestion",
                children=tuple(open_binders) + (parse,),
                roles=tuple(["binder"] * len(open_binders) + ["query"]),
                source_start=min(span_starts) if span_starts else None,
                source_end=max(span_ends) if span_ends else None,
            )
        semantic_diagnostics = validate_semantics(parse)
        if semantic_diagnostics:
            return CheckResult(
                valid=False,
                source=source,
                mood=mood,
                phrases=phrases,
                diagnostics=semantic_diagnostics,
                mana=mana,
            )
        if mood == "command":
            closure_diagnostics = validate_execution_closure(parse)
            if closure_diagnostics:
                return CheckResult(
                    valid=False,
                    source=source,
                    mood=mood,
                    phrases=phrases,
                    diagnostics=closure_diagnostics,
                    mana=mana,
                )
        ast = Node(
            kind=mood.capitalize(),
            type={"command":"Command","assertion":"Assertion","question":"Question"}[mood],
            name=mood.capitalize(),
            children=(parse,),
            source_start=parse.source_start,
            source_end=parse.source_end,
        )
        return CheckResult(
            valid=True,
            source=source,
            mood=mood,
            phrases=phrases,
            ast=ast,
            diagnostics=[],
            mana=mana,
        )

    def parse_phrase(
        self,
        phrase: str,
        expected_type: str = "SemanticValue",
        context: Context | None = None,
        source_offset: int = 0,
        resolve_external_binders: bool = False,
    ) -> Node | Diagnostic:
        self._diagnostics = []
        pieces = split_phrases_with_spans(phrase)
        self._fields = [piece.text for piece in pieces]
        self._field_spans = [
            (source_offset + piece.start, source_offset + piece.end)
            for piece in pieces
        ]
        ctx = context or Context()
        if not self._fields:
            return Diagnostic(
                "SyntaxError",
                "Empty expression.",
                source_start=source_offset,
                source_end=source_offset,
            )
        candidates = self._parse_expr(0, expected_type, ctx, outer_head=True)
        full = [c for c in candidates if c.next_index == len(self._fields)]
        if resolve_external_binders:
            external = tuple(
                name for name, typ in ctx.variables if typ == _INFER_BINDER_TYPE
            )
            if external:
                resolved_full = []
                for candidate in full:
                    resolved = self._resolve_inferred_binders(
                        candidate.node, external, 0
                    )
                    if resolved is not None:
                        resolved_full.append(Candidate(resolved, candidate.next_index))
                full = resolved_full
        if not full:
            if self._diagnostics:
                return self._attach_source_span(self._best_diagnostic())
            return Diagnostic(
                "SyntaxError",
                "No legal parse consumed every token in the expression.",
            )
        unique: dict[str, Node] = {c.node.canonical(): c.node for c in full}
        if len(unique) > 1:
            meanings = "; ".join(sorted(unique))
            return Diagnostic(
                "AmbiguousPhrase",
                f"More than one distinct typed parse is legal: {meanings}",
                source_start=self._field_spans[0][0] if self._field_spans else None,
                source_end=self._field_spans[-1][1] if self._field_spans else None,
            )
        return next(iter(unique.values()))

    def _attach_source_span(self, diagnostic: Diagnostic) -> Diagnostic:
        if diagnostic.source_start is not None or diagnostic.source_end is not None:
            return diagnostic
        if diagnostic.field_index is None:
            return diagnostic
        if diagnostic.field_index < 0 or diagnostic.field_index >= len(self._field_spans):
            return diagnostic
        start, end = self._field_spans[diagnostic.field_index]
        return replace(diagnostic, source_start=start, source_end=end)

    def _parse_bound_group(
        self,
        field: str,
        index: int,
        expected_type: str,
        context: Context,
    ) -> list[Candidate]:
        """Parse a maximal pipe-connected token group as one hard-bound expression."""
        parts = split_fields(field)
        if len(parts) < 2:
            return []
        nested = Parser(self.language)
        nested._fields = parts
        candidates = nested._parse_expr(0, expected_type, context, outer_head=True)
        full = [candidate for candidate in candidates if candidate.next_index == len(parts)]
        if not full:
            diagnostic = nested._best_diagnostic() if nested._diagnostics else Diagnostic(
                "BoundGroupError",
                f"Pipe-bound group {field} does not form one complete {expected_type} expression.",
            )
            self._diagnostics.append(replace(
                diagnostic, field_index=index, field=field, progress_index=index
            ))
            return []
        unique = {candidate.node.canonical(): candidate.node for candidate in full}
        if len(unique) > 1:
            meanings = "; ".join(sorted(unique))
            self._diagnostics.append(Diagnostic(
                "AmbiguousBoundGroup",
                f"Pipe-bound group {field} has multiple meanings: {meanings}",
                field_index=index,
                field=field,
            ))
            return []
        return [Candidate(next(iter(unique.values())), index + 1)]

    def _parse_tight_group(
        self,
        field: str,
        index: int,
        expected_type: str,
        context: Context,
    ) -> list[Candidate]:
        """Parse concatenated registered roots as one tightly bound local expression."""
        meanings: dict[str, Node] = {}
        for segmentation in self.language.known_segmentations(field):
            nested = Parser(self.language)
            nested._fields = list(segmentation)
            candidates = nested._parse_expr(0, expected_type, context, outer_head=True)
            for candidate in candidates:
                if candidate.next_index != len(segmentation):
                    continue
                node = self._clear_source_spans(candidate.node)
                meanings[node.canonical()] = node
        if not meanings:
            return []
        if len(meanings) > 1:
            rendered = "; ".join(sorted(meanings))
            self._diagnostics.append(Diagnostic(
                "AmbiguousTightGroup",
                f"Tightly joined token {field} has multiple typed meanings: {rendered}",
                field_index=index,
                field=field,
                progress_index=index,
            ))
            return []
        return [Candidate(next(iter(meanings.values())), index + 1)]

    @staticmethod
    def _is_binder_token(field: str) -> bool:
        # Canonical rune-native label, optionally typed by a *Cuspell* witness.
        # The prefixed colon keeps the declaration distinct from an ordinary
        # quoted Sign and from a variable reference $«...».
        if re.fullmatch(r":«[A-Za-z]+»(?::(?:[A-Za-z][A-Za-z0-9_]*|«.+»))?", field):
            return True
        # Legacy named binders remain compatible with older corpus snapshots.
        return bool(
            re.fullmatch(
                r"(?:\[)?[A-Za-z][A-Za-z0-9_]*:(?:[A-Za-z][A-Za-z0-9_:]*|«.+»)(?:\])?",
                field,
            )
            and (not field.startswith("[") or field.endswith("]"))
        )

    def _parse_flat_event_group(
        self,
        index: int,
        context: Context,
        operator: str,
        end_marker: str,
    ) -> list[Candidate]:
        """Parse a flat variadic EventSpec group.

        Sequence and Concurrent use the same language-like surface rule:
        the sentence boundary closes the group automatically, while a
        zero-mana explicit end marker is required when later material follows.
        """
        results: list[Candidate] = []
        frame_ctx = context.with_event()

        def build(events: tuple[Node, ...], next_index: int) -> None:
            collection = Node(
                kind="Collection",
                type="Collection:EventSpec",
                children=events,
            )
            node = Node(
                kind="OperatorApply",
                type="EventSpec",
                name=operator,
                children=(collection,),
                roles=("events",),
            )
            results.append(Candidate(node, next_index))

        def recurse(pos: int, events: tuple[Node, ...]) -> None:
            if pos < len(self._fields) and self._fields[pos] in {end_marker, f"{operator}End"}:
                if events:
                    build(events, pos + 1)
                return
            if pos >= len(self._fields):
                if events:
                    build(events, pos)
                return

            child_candidates = self._parse_expr(
                pos,
                "EventSpec",
                frame_ctx,
                outer_head=False,
            )
            for child in child_candidates:
                if child.next_index <= pos:
                    continue
                recurse(child.next_index, events + (child.node,))

        recurse(index + 1, ())
        return results

    def _best_diagnostic(self) -> Diagnostic:
        with_index = [d for d in self._diagnostics if d.field_index is not None]
        if not with_index:
            return self._diagnostics[-1]
        furthest = max(
            d.progress_index if d.progress_index is not None else (d.field_index or 0)
            for d in with_index
        )
        best = [
            d for d in with_index
            if (d.progress_index if d.progress_index is not None else (d.field_index or 0)) == furthest
        ]
        for code in ("DimensionMismatch", "ValueDomainMismatch", "SemanticallyIncomplete", "TypeMismatch", "AmbiguousTightGroup", "IllegalCompound", "FreeVariable", "UnknownRoot", "MissingRequiredRole", "InvalidRole"):
            for diag in best:
                if diag.code == code:
                    return diag
        return best[-1]

    def _parse_expr(
        self,
        index: int,
        expected_type: str,
        context: Context,
        outer_head: bool = False,
    ) -> list[Candidate]:
        base = self._parse_expr_unspanned(index, expected_type, context, outer_head)
        candidates = [
            Candidate(
                self._with_source_span(candidate.node, index, candidate.next_index),
                candidate.next_index,
            )
            for candidate in base
        ]

        # Canonical surface conjunction/disjunction is infix:
        # A And B / A Or B. Prefix collection forms remain parser-compatible.
        # Mixed And/Or without explicit grouping is intentionally rejected so
        # logical scope never depends on an implicit precedence convention.
        combined: list[Candidate] = list(candidates)
        for operator in ("And", "Or"):
            for left in candidates:
                if (
                    left.next_index >= len(self._fields)
                    or self._fields[left.next_index] != operator
                ):
                    continue
                if (
                    operator == "And"
                    and self.language.is_assignable(left.node.type, "EventSpec")
                ):
                    operand_type = "EventSpec"
                elif self.language.is_assignable(left.node.type, "Proposition"):
                    operand_type = "Proposition"
                else:
                    continue
                if not self.language.is_assignable(operand_type, expected_type):
                    continue

                right_index = left.next_index + 1
                rights = self._parse_expr(
                    right_index,
                    operand_type,
                    context,
                    outer_head=False,
                )
                for right in rights:
                    right_is_explicitly_grouped = (
                        right_index < len(self._fields)
                        and self._fields[right_index].startswith("(")
                    )
                    if (
                        right.node.name in {"And", "Or"}
                        and right.node.name != operator
                        and not right_is_explicitly_grouped
                    ):
                        continue

                    items: list[Node] = []
                    for operand in (left.node, right.node):
                        if (
                            operand.name == operator
                            and operand.children
                            and operand.children[0].kind == "Collection"
                        ):
                            items.extend(operand.children[0].children)
                        else:
                            items.append(operand)
                    collection = Node(
                        kind="Collection",
                        type=f"Collection:{operand_type}",
                        children=tuple(items),
                    )
                    node = Node(
                        kind="OperatorApply",
                        type=operand_type,
                        name=operator,
                        children=(collection,),
                        roles=("items",),
                    )
                    combined.append(Candidate(
                        self._with_source_span(node, index, right.next_index),
                        right.next_index,
                    ))
        return combined

    def _with_source_span(self, node: Node, start_index: int, next_index: int) -> Node:
        if (
            not self._field_spans
            or start_index < 0
            or next_index <= start_index
            or start_index >= len(self._field_spans)
            or next_index - 1 >= len(self._field_spans)
        ):
            return node
        start = self._field_spans[start_index][0]
        end = self._field_spans[next_index - 1][1]
        return replace(node, source_start=start, source_end=end)

    def _clear_source_spans(self, node: Node) -> Node:
        return replace(
            node,
            source_start=None,
            source_end=None,
            children=tuple(self._clear_source_spans(child) for child in node.children),
        )

    def _quantity_from_unit_definition(
        self,
        definition: dict,
        amount: Node,
        source_unit: str,
    ) -> Node:
        scale_data = definition.get("scale", {"numerator": 1, "denominator": 1})
        scale = Fraction(
            int(scale_data.get("numerator", 1)),
            int(scale_data.get("denominator", 1)),
        )
        static_amount = self._static_number_value(amount)
        if static_amount is not None:
            normalized_amount = Node(
                kind="Number",
                type="Quantity:Number",
                value=static_amount * scale,
                name=str(static_amount * scale),
            )
        elif scale == 1:
            normalized_amount = amount
        else:
            scale_node = Node(
                kind="Number",
                type="Quantity:Number",
                value=scale,
                name=str(scale),
            )
            normalized_amount = Node(
                kind="OperatorApply",
                type="Quantity:Number",
                name="Multiply",
                children=(scale_node, amount),
                roles=("factor", "value"),
            )
        dimension = str(definition["dimension"])
        return Node(
            kind="QuantityValue",
            type=f"Quantity:{dimension}",
            name=f"{dimension}Quantity",
            children=(normalized_amount,),
            roles=("amount",),
            meta=(
                ("source_unit", source_unit),
                ("unit_old_name_id", definition.get("old_name_id")),
                ("scale_numerator", scale.numerator),
                ("scale_denominator", scale.denominator),
            ),
        )

    def _substitute_old_name_parameters(
        self,
        node: Node,
        arguments: dict[str, Node],
    ) -> Node:
        if node.kind == "Variable" and node.name and node.name.startswith("$"):
            replacement = arguments.get(node.name[1:])
            if replacement is not None:
                return replacement
        return replace(
            node,
            children=tuple(
                self._substitute_old_name_parameters(child, arguments)
                for child in node.children
            ),
        )

    def _parse_parameterized_old_name(
        self,
        old_name: dict,
        content: str,
        index: int,
        expected_type: str,
        context: Context,
    ) -> list[Candidate]:
        old_id = str(old_name.get("id", content))
        meaning = old_name.get("meaning") or {}
        declared_type = meaning.get("type")
        parameters = meaning.get("parameters")
        source = meaning.get("source")

        if not isinstance(declared_type, str):
            return []
        if not self.language.is_assignable(declared_type, expected_type):
            return []
        if old_id in context.old_name_stack:
            self._diagnostics.append(Diagnostic(
                "RecursiveOldName",
                f"Old Name «{content}» recursively expands itself.",
                field_index=index,
                field=f"«{content}»",
                progress_index=index,
            ))
            return []
        if not isinstance(parameters, list) or not parameters:
            return []
        if not isinstance(source, str) or not source.strip():
            self._diagnostics.append(Diagnostic(
                "InvalidOldName",
                f"Old Name «{content}» lacks a frozen semantic expression.",
                field_index=index,
                field=f"«{content}»",
                progress_index=index,
            ))
            return []

        # Frozen expression templates are lexically scoped. They can refer only
        # to their declared parameters, not to caller binders that happen to
        # have the same variable names.
        template_context = Context(
            old_name_stack=context.old_name_stack,
        ).with_old_name(old_id)
        parameter_names: list[str] = []
        for parameter in parameters:
            if not isinstance(parameter, dict):
                return []
            name = parameter.get("name")
            typ = parameter.get("type")
            if not isinstance(name, str) or not isinstance(typ, str):
                return []
            parameter_names.append(name)
            template_context = template_context.with_variable(name, typ)

        nested = Parser(self.language).parse_phrase(
            source,
            expected_type=declared_type,
            context=template_context,
        )
        if isinstance(nested, Diagnostic):
            self._diagnostics.append(replace(
                nested,
                code="InvalidOldName",
                message=(
                    f"Old Name «{content}» has an invalid frozen template: "
                    f"{nested.message}"
                ),
                field_index=index,
                field=f"«{content}»",
                progress_index=index,
            ))
            return []

        template_node = self._clear_source_spans(nested)
        results: list[Candidate] = []

        def recurse(
            parameter_index: int,
            pos: int,
            args: tuple[Node, ...],
        ) -> None:
            if parameter_index >= len(parameters):
                mapping = {
                    name: arg
                    for name, arg in zip(parameter_names, args)
                }
                instantiated = self._substitute_old_name_parameters(
                    template_node,
                    mapping,
                )
                instantiated = replace(
                    instantiated,
                    meta=instantiated.meta + (
                        ("old_name_id", old_id),
                        ("old_name_sign", content),
                        ("old_name_expansion", True),
                        ("old_name_parameterized", True),
                    ),
                )
                results.append(Candidate(instantiated, pos))
                return

            parameter = parameters[parameter_index]
            typ = str(parameter["type"])
            if pos >= len(self._fields):
                self._diagnostics.append(Diagnostic(
                    "MissingRequiredRole",
                    (
                        f"Old Name «{content}» needs parameter "
                        f"{parameter['name']}:{typ}."
                    ),
                    field_index=max(index, pos - 1),
                    field=f"«{content}»",
                    expected=typ,
                    actual="missing",
                    progress_index=max(index, pos - 1),
                ))
                return

            if self._fields[pos] == "_":
                self._diagnostics.append(Diagnostic(
                    "InvalidOmission",
                    (
                        f"Parameterized Old Name «{content}» has no optional "
                        f"parameters; {parameter['name']} cannot be omitted."
                    ),
                    field_index=pos,
                    field="_",
                    expected=typ,
                    actual="omitted",
                    progress_index=pos,
                ))
                return

            children = self._parse_expr(
                pos,
                typ,
                context,
                outer_head=False,
            )
            for child in children:
                recurse(
                    parameter_index + 1,
                    child.next_index,
                    args + (child.node,),
                )

        recurse(0, index + 1, ())
        return results

    def _parse_quoted_name(
        self,
        field: str,
        index: int,
        expected_type: str,
        context: Context,
    ) -> list[Candidate]:
        """Parse an exact quoted Sign and any registered Old Name meaning.

        Every «... » remains available as a Sign. Only historically registered
        Old Names gain a second, typed semantic reading. New Names remain
        ordinary Name/reference data and never expand here.

        Unit-valued Old Names may also head a numeric quantity construction:
        «LengthUnit» @@.
        """
        content = field[1:-1]
        results: list[Candidate] = []

        sign_node = Node(kind="SignLiteral", type="Sign", name="Quote", value=content)
        if self.language.is_assignable("Sign", expected_type):
            results.append(Candidate(sign_node, index + 1))

        registered_old_names = self.language.old_name_entries(content)
        for old_name in registered_old_names:
            old_id = str(old_name.get("id", content))
            meaning = old_name.get("meaning") or {}
            meaning_kind = meaning.get("kind")
            declared_type = meaning.get("type")

            if not isinstance(declared_type, str):
                self._diagnostics.append(Diagnostic(
                    "InvalidOldName",
                    f"Old Name {field} lacks a declared semantic type.",
                    field_index=index,
                    field=field,
                    progress_index=index,
                ))
                continue

            semantic_node: Node | None = None
            unit_definition: dict | None = None
            if meaning_kind == "concept":
                concept_id = meaning.get("concept_id")
                concept = (
                    self.language.world_concept(str(concept_id))
                    if concept_id is not None
                    else None
                )
                if concept is None:
                    self._diagnostics.append(Diagnostic(
                        "InvalidOldName",
                        f"Old Name {field} references unknown world concept {concept_id!r}.",
                        field_index=index,
                        field=field,
                        progress_index=index,
                    ))
                    continue
                semantic_node = Node(
                    kind="WorldConcept",
                    type=declared_type,
                    name=str(concept_id),
                    value=content,
                    meta=(
                        ("old_name_id", old_id),
                        ("old_name_sign", content),
                    ),
                )
            elif meaning_kind == "expression":
                parameters = meaning.get("parameters")
                if parameters:
                    results.extend(
                        self._parse_parameterized_old_name(
                            old_name,
                            content,
                            index,
                            expected_type,
                            context,
                        )
                    )
                    continue
                if old_id in context.old_name_stack:
                    self._diagnostics.append(Diagnostic(
                        "RecursiveOldName",
                        f"Old Name {field} recursively expands itself.",
                        field_index=index,
                        field=field,
                        progress_index=index,
                    ))
                    continue
                source = meaning.get("source")
                if not isinstance(source, str) or not source.strip():
                    self._diagnostics.append(Diagnostic(
                        "InvalidOldName",
                        f"Old Name {field} lacks a frozen semantic expression.",
                        field_index=index,
                        field=field,
                        progress_index=index,
                    ))
                    continue

                # Closed frozen expressions are also lexically scoped: they may
                # not capture a caller's binder variables.
                frozen_context = Context(
                    old_name_stack=context.old_name_stack,
                ).with_old_name(old_id)
                nested = Parser(self.language).parse_phrase(
                    source,
                    expected_type=declared_type,
                    context=frozen_context,
                )
                if isinstance(nested, Diagnostic):
                    self._diagnostics.append(replace(
                        nested,
                        code="InvalidOldName",
                        message=(
                            f"Old Name {field} has an invalid frozen meaning: "
                            f"{nested.message}"
                        ),
                        field_index=index,
                        field=field,
                        progress_index=index,
                    ))
                    continue
                cleared = self._clear_source_spans(nested)
                semantic_node = replace(
                    cleared,
                    meta=cleared.meta + (
                        ("old_name_id", old_id),
                        ("old_name_sign", content),
                        ("old_name_expansion", True),
                    ),
                )
            elif meaning_kind == "unit":
                unit_definition = self.language.unit_definition_for_old_name(old_id)
                if unit_definition is None:
                    self._diagnostics.append(Diagnostic(
                        "InvalidOldName",
                        f"Old Name {field} has no registered typed Unit definition.",
                        field_index=index,
                        field=field,
                        progress_index=index,
                    ))
                    continue
                if str(meaning.get("unit_id")) != str(unit_definition.get("id")):
                    self._diagnostics.append(Diagnostic(
                        "InvalidOldName",
                        f"Old Name {field} does not match its registered Unit definition.",
                        field_index=index,
                        field=field,
                        progress_index=index,
                    ))
                    continue
                semantic_node = Node(
                    kind="UnitValue",
                    type=declared_type,
                    name=str(unit_definition["id"]),
                    value=content,
                    meta=(
                        ("old_name_id", old_id),
                        ("old_name_sign", content),
                        ("dimension", str(unit_definition["dimension"])),
                    ),
                )
            else:
                self._diagnostics.append(Diagnostic(
                    "InvalidOldName",
                    f"Old Name {field} uses unsupported meaning kind {meaning_kind!r}.",
                    field_index=index,
                    field=field,
                    progress_index=index,
                ))
                continue

            if semantic_node is None:
                continue

            if self.language.is_assignable(semantic_node.type, expected_type):
                results.append(Candidate(semantic_node, index + 1))

            if unit_definition is not None and index + 1 < len(self._fields):
                quantity_type = f"Quantity:{unit_definition['dimension']}"
                if self.language.is_assignable(quantity_type, expected_type):
                    amounts = self._parse_expr(
                        index + 1,
                        "Quantity:Number",
                        context,
                        outer_head=False,
                    )
                    for amount in amounts:
                        results.append(Candidate(
                            self._quantity_from_unit_definition(
                                unit_definition,
                                amount.node,
                                content,
                            ),
                            amount.next_index,
                        ))
                elif expected_type.startswith("Quantity"):
                    self._record_type_mismatch(
                        index,
                        field,
                        expected_type,
                        quantity_type,
                        progress_index=index + 1,
                    )

            # A Kind-valued Old Name can behave as a typed world
            # classifier. Existing concepts default to Entity classification;
            # world concepts may opt into other explicit target types such as
            # Event/EventSpec or Information.
            if (
                semantic_node.type == "Kind"
                and self.language.is_assignable("Proposition", expected_type)
                and index + 1 < len(self._fields)
            ):
                classify_types = self.language.world_kind_classifies_types(
                    str(semantic_node.name)
                )
                for classify_type in classify_types:
                    subjects = self._parse_expr(
                        index + 1,
                        str(classify_type),
                        context,
                        outer_head=False,
                    )
                    for subject in subjects:
                        proposition = Node(
                            kind="RelationApply",
                            type="Proposition",
                            name="InstanceOf",
                            children=(subject.node, semantic_node),
                            roles=("subject", "kind"),
                            meta=(("classified_type", str(classify_type)),),
                        )
                        results.append(Candidate(proposition, subject.next_index))

        if results:
            return results

        # If a registered Old Name was found but its frozen meaning itself is
        # invalid/recursive, preserve that diagnostic instead of masking it as
        # a generic Sign type mismatch.
        if registered_old_names and any(
            diagnostic.field_index == index
            and diagnostic.code in {"InvalidOldName", "RecursiveOldName"}
            for diagnostic in self._diagnostics
        ):
            return []

        # An unregistered/new quoted name is still a Sign; it simply is not a
        # magical semantic abbreviation.
        self._record_type_mismatch(index, field, expected_type, "Sign")
        return []

    def _parse_expr_unspanned(
        self,
        index: int,
        expected_type: str,
        context: Context,
        outer_head: bool = False,
    ) -> list[Candidate]:
        if index >= len(self._fields):
            return []
        field = self._fields[index]

        if len(split_fields(field)) > 1:
            return self._parse_bound_group(field, index, expected_type, context)

        if field.startswith("(") and field.endswith(")"):
            inner = field[1:-1].strip()
            nested = Parser(self.language).parse_phrase(inner, expected_type, context)
            if isinstance(nested, Diagnostic):
                self._diagnostics.append(replace(
                    nested, field_index=index, field=field, progress_index=index
                ))
                return []
            return [Candidate(self._clear_source_spans(nested), index + 1)]

        if field.startswith("«") and field.endswith("»"):
            return self._parse_quoted_name(
                field,
                index,
                expected_type,
                context,
            )

        if field.startswith("{") and field.endswith("}"):
            return self._parse_collection(field, index, expected_type, context)

        if self._is_binder_token(field):
            return self._parse_binder(field, index, expected_type)

        if field == ":":
            self._diagnostics.append(Diagnostic(
                "UnexpectedGroupClose",
                "':' closes a flat Sequence/Concurrent; no such group is open here.",
                field_index=index, field=field,
            ))
            return []

        if field in {"SequenceEnd", "ConcurrentEnd"}:
            operator = "Sequence" if field == "SequenceEnd" else "Concurrent"
            self._diagnostics.append(Diagnostic(
                f"Unexpected{field}",
                f"{field} appeared without a {operator} waiting to be closed.",
                field_index=index,
                field=field,
            ))
            return []

        if field in {"Sequence", "Concurrent"} and expected_type == "EventSpec":
            flat_group = self._parse_flat_event_group(
                index,
                context,
                operator=field,
                end_marker=":",
            )
            if flat_group:
                return flat_group

        if field.startswith("$"):
            return self._parse_variable(field, index, expected_type, context)

        if re.fullmatch(r"@+", field):
            node = Node(kind="Number", type="Quantity:Number", value=len(field), name=field)
            if self.language.is_assignable(node.type, expected_type):
                return [Candidate(node, index + 1)]
            self._record_type_mismatch(index, field, expected_type, node.type)
            return []

        if field == "_":
            self._diagnostics.append(Diagnostic(
                "InvalidOmission",
                "The omission marker '_' is only valid while advancing over an optional frame slot.",
                field_index=index,
                field=field,
            ))
            return []

        if field.startswith(":"):
            self._diagnostics.append(Diagnostic(
                "InvalidRole",
                "Named role markers are not current Cuspell. "
                "Write arguments in frame order and use '_' only to omit an optional slot.",
                field_index=index,
                field=field,
            ))
            return []

        entries = self.language.resolve_entries(field)
        if not entries:
            if self.language.has_known_segmentation(field):
                tight = self._parse_tight_group(field, index, expected_type, context)
                if tight:
                    return tight
                if any(
                    diagnostic.code == "AmbiguousTightGroup"
                    and diagnostic.field_index == index
                    for diagnostic in self._diagnostics
                ):
                    return []
                segmentations = [" + ".join(parts) for parts in self.language.known_segmentations(field)]
                self._diagnostics.append(Diagnostic(
                    "IllegalCompound",
                    f"Known roots can segment {field}, but they form neither a registered lexical compound nor one complete typed tight expression: " + "; ".join(segmentations),
                    field_index=index,
                    field=field,
                ))
            else:
                self._diagnostics.append(Diagnostic(
                    "UnknownRoot",
                    f"Unknown root or unregistered compound: {field}",
                    field_index=index,
                    field=field,
                ))
            return []

        candidates: list[Candidate] = []
        for entry in entries:
            candidates.extend(self._parse_entry(entry, index, expected_type, context))
        return candidates

    def _parse_entry(
        self,
        entry: Entry,
        index: int,
        expected_type: str,
        context: Context,
    ) -> list[Candidate]:
        candidates: list[Candidate] = []
        atom_type = entry.atom_type
        if (
            atom_type
            and entry.data.get("literal_number") == 0
            and expected_type.startswith("Quantity:")
        ):
            atom_type = expected_type
        if atom_type and self.language.is_assignable(atom_type, expected_type):
            meta: list[tuple[str, object]] = []
            if entry.data.get("descriptor_value_type"):
                meta.append(("descriptor_value_type", entry.data["descriptor_value_type"]))
            if entry.data.get("property_expr"):
                meta.append(("property_expr", entry.data["property_expr"]))
            if entry.data.get("family"):
                meta.append(("family", entry.data["family"]))
            if entry.data.get("family_value"):
                meta.append(("family_value", entry.data["family_value"]))
            if entry.data.get("value_domain"):
                meta.append(("value_domain", entry.data["value_domain"]))
            if entry.data.get("contextual"):
                meta.append(("contextual", True))
            kind = "Descriptor" if atom_type in {"AttributeDescriptor", "PropertyDescriptor"} else "Reference"
            if atom_type == "Kind": kind = "Root"
            node_name = entry.data.get("normalized_surface", entry.surface)
            if "literal_number" in entry.data:
                node = Node(kind="Number", type=atom_type, name=node_name, value=entry.data["literal_number"], meta=tuple(meta))
            elif atom_type == "Kind" and entry.data.get("derived_kind"):
                node = self._make_kind_node(entry.data["derived_kind"])
            else:
                node = Node(kind=kind, type=atom_type, name=node_name, meta=tuple(meta))
            candidates.append(Candidate(node, index + 1))
        elif atom_type and not entry.frames:
            self._record_type_mismatch(index, entry.surface, expected_type, atom_type)
        for frame in entry.frames:
            candidates.extend(self._parse_frame(entry, frame, index, expected_type, context))
        if not candidates and atom_type and entry.frames and not self.language.is_assignable(atom_type, expected_type):
            self._record_type_mismatch(index, entry.surface, expected_type, atom_type)
        return candidates

    def _parse_frame(
        self,
        entry: Entry,
        frame: dict,
        head_index: int,
        expected_type: str,
        context: Context,
    ) -> list[Candidate]:
        if frame.get("requires_event_context") and not context.in_event:
            return []

        frame_ctx = context.with_event() if frame.get("event_context") else context
        slots = frame.get("slots", [])
        results: list[Candidate] = []

        @dataclass(frozen=True)
        class State:
            pos: int
            args: tuple[Node, ...]
            roles: tuple[str, ...]
            ctx: Context
            bound_names: tuple[str, ...]

        def finalize(state: State) -> None:
            required = [s["name"] for s in slots if s.get("required", True)]
            if any(name not in state.bound_names for name in required):
                return
            out_type = self._resolve_output_type(frame, state.args)
            if out_type is None:
                issue = self._dimension_output_issue(
                    entry,
                    frame,
                    state.args,
                    head_index,
                    max(head_index, state.pos - 1),
                )
                if issue is not None:
                    self._diagnostics.append(issue)
                return
            if not self.language.is_assignable(out_type, expected_type):
                self._record_type_mismatch(
                    head_index,
                    entry.surface,
                    expected_type,
                    out_type,
                    progress_index=max(head_index, state.pos - 1),
                )
                return
            domain_issue = self._value_domain_issue(
                entry,
                frame,
                state.args,
                state.roles,
                head_index,
                max(head_index, state.pos - 1),
            )
            if domain_issue is not None:
                self._diagnostics.append(domain_issue)
                return
            node = self._make_call_node(entry, frame, state.args, state.roles, out_type)
            unresolved = tuple(
                arg.name for arg in state.args
                if arg.kind == "Binder"
                and arg.meta_dict().get("rune_native")
                and arg.meta_dict().get("bound_type") == "Any"
            )
            if unresolved:
                node = self._resolve_inferred_binders(node, unresolved, head_index)
                if node is None:
                    return
            results.append(Candidate(node, state.pos))

        def recurse(slot_i: int, state: State) -> None:
            if slot_i >= len(slots):
                finalize(state)
                return

            slot = slots[slot_i]
            current = self._fields[state.pos] if state.pos < len(self._fields) else None

            if current is not None and current.startswith(":") and not self._is_binder_token(current):
                self._diagnostics.append(Diagnostic(
                    "InvalidRole",
                    "Named role markers are not current Cuspell. "
                    "Write arguments in frame order and use '_' only to omit an optional slot.",
                    field_index=state.pos,
                    field=current,
                ))
                return

            if current == "_":
                if slot.get("required", True):
                    self._diagnostics.append(Diagnostic(
                        "InvalidOmission",
                        f"Cannot omit required role {slot['name']} for {entry.surface}.",
                        field_index=state.pos,
                        field=current,
                        expected=slot["name"],
                        actual="omitted",
                    ))
                    return
                recurse(slot_i + 1, State(
                    pos=state.pos + 1,
                    args=state.args,
                    roles=state.roles,
                    ctx=state.ctx,
                    bound_names=state.bound_names,
                ))
                return

            expected_slot = self._resolve_slot_type(slot["type"], state.args, expected_type)
            if expected_slot is None:
                return

            if not slot.get("required", True):
                finalize(state)

            if current is None:
                return

            child_candidates = self._parse_expr(state.pos, expected_slot, state.ctx)
            for child in child_candidates:
                resolved_node = child.node
                if resolved_node.kind == "Binder":
                    meta = resolved_node.meta_dict()
                    if meta.get("rune_native") and meta.get("bound_type") == "Any":
                        # Frame-provided types make Create and typed collection
                        # iteration require no externally spelled Entity/type.
                        inferred = slot.get("binds_type")
                        source_role = slot.get("binds_member_of_role")
                        if inferred is None and source_role in state.roles:
                            collection = state.args[state.roles.index(source_role)]
                            if collection.type.startswith("Collection:"):
                                inferred = collection.type.split(":", 1)[1]
                        if inferred is not None:
                            resolved_node = replace(
                                resolved_node,
                                meta=(("bound_type", str(inferred)), ("rune_native", True)),
                            )
                        # Otherwise preserve the unknown type until the complete
                        # typed predicate supplies constraints at finalize().
                if not self._binder_matches_collection_slot(
                    slot, resolved_node, state.args, state.roles, state.pos, self._fields[state.pos]
                ):
                    continue
                new_ctx = state.ctx
                if resolved_node.kind == "Binder":
                    binder_type = resolved_node.meta_dict().get("bound_type", "Entity")
                    if (resolved_node.meta_dict().get("rune_native") and
                            resolved_node.name in state.ctx.variable_map()):
                        self._diagnostics.append(Diagnostic(
                            "DuplicateBinder",
                            f"Rune label {resolved_node.name} is already bound in this scope.",
                            field_index=state.pos, field=current,
                        ))
                        continue
                    if (resolved_node.meta_dict().get("rune_native")
                            and binder_type == "Any"):
                        binder_type = _INFER_BINDER_TYPE
                    new_ctx = new_ctx.with_variable(resolved_node.name or "?", binder_type)
                recurse(slot_i + 1, State(
                    pos=child.next_index,
                    args=state.args + (resolved_node,),
                    roles=state.roles + (slot["name"],),
                    ctx=new_ctx,
                    bound_names=state.bound_names + (slot["name"],),
                ))

        recurse(0, State(head_index + 1, (), (), frame_ctx, ()))
        return results

    def _binder_matches_collection_slot(
        self,
        slot: dict,
        binder: Node,
        args: tuple[Node, ...],
        roles: tuple[str, ...],
        field_index: int,
        field: str,
    ) -> bool:
        if binder.kind != "Binder":
            return True

        required_bound_type = slot.get("binds_type")
        if required_bound_type:
            binder_type = str(binder.meta_dict().get("bound_type", "Any"))
            if not self.language.is_assignable(binder_type, str(required_bound_type)):
                self._diagnostics.append(Diagnostic(
                    "TypeMismatch",
                    (
                        f"Binder {binder.name or '?'} ranges over {binder_type}, "
                        f"but role {slot.get('name')} requires {required_bound_type}."
                    ),
                    field_index=field_index,
                    field=field,
                    expected=f"Binder:{required_bound_type}",
                    actual=f"Binder:{binder_type}",
                ))
                return False

        source_role = slot.get("binds_member_of_role")
        if not source_role:
            return True
        if source_role not in roles:
            self._diagnostics.append(Diagnostic(
                "SyntaxError",
                f"Binder role {slot.get('name')} depends on unbound collection role {source_role}.",
                field_index=field_index,
                field=field,
            ))
            return False
        source = args[roles.index(source_role)]
        if source.type == "Collection":
            return True
        if not source.type.startswith("Collection:"):
            self._diagnostics.append(Diagnostic(
                "TypeMismatch",
                f"Binder role {slot.get('name')} requires {source_role} to be a Collection, received {source.type}.",
                field_index=field_index,
                field=field,
                expected="Collection",
                actual=source.type,
            ))
            return False
        member_type = source.type.split(":", 1)[1]
        binder_type = str(binder.meta_dict().get("bound_type", "Any"))
        if self.language.is_assignable(member_type, binder_type):
            return True
        self._diagnostics.append(Diagnostic(
            "TypeMismatch",
            f"Binder {binder.name or '?'} ranges over {binder_type}, but {source_role} supplies {member_type} members.",
            field_index=field_index,
            field=field,
            expected=f"Binder:{member_type}",
            actual=f"Binder:{binder_type}",
        ))
        return False

    def _resolve_slot_type(self, spec: str, args: tuple[Node, ...], outer_expected: str) -> str | None:
        if spec.startswith("$") and spec[1:].isdigit():
            idx = int(spec[1:])
            return args[idx].type if idx < len(args) else None
        if spec == "$output":
            return outer_expected if outer_expected not in {"Any", "SemanticValue"} else "SemanticValue"
        if spec.startswith("$attribute:"):
            idx = int(spec.split(":", 1)[1])
            if idx >= len(args):
                return None
            return args[idx].meta_dict().get("descriptor_value_type")
        return spec

    def _resolve_output_type(self, frame: dict, args: tuple[Node, ...]) -> str | None:
        if "output" in frame:
            return frame["output"]
        if "output_from_arg" in frame:
            idx = int(frame["output_from_arg"])
            return args[idx].type if idx < len(args) else None
        if "output_collection_of_binder_arg" in frame:
            idx = int(frame["output_collection_of_binder_arg"])
            if idx >= len(args):
                return None
            binder = args[idx]
            if binder.kind != "Binder":
                return None
            bound_type = binder.meta_dict().get("bound_type")
            if not isinstance(bound_type, str) or not bound_type:
                return None
            return f"Collection:{bound_type}"
        if "output_member_of_arg" in frame:
            idx = int(frame["output_member_of_arg"])
            if idx >= len(args): return None
            typ=args[idx].type
            if typ.startswith("Collection:") or typ.startswith("Sequence:"):
                return typ.split(":",1)[1]
            return None
        if "output_sequence_of_arg" in frame:
            idx = int(frame["output_sequence_of_arg"])
            if idx >= len(args):
                return None
            typ=args[idx].type
            if typ.startswith("Collection:"):
                return f"Sequence:{typ.split(':',1)[1]}"
            if typ=="Collection":
                return "Sequence"
            return None
        if "output_partition_of_arg" in frame:
            idx = int(frame["output_partition_of_arg"])
            if idx >= len(args):
                return None
            typ = args[idx].type
            if typ == "Collection":
                return "Collection:Collection"
            if typ.startswith("Collection:"):
                return f"Collection:Collection:{typ.split(':', 1)[1]}"
            return None
        if "output_quantity_dimension_op" in frame:
            operation=frame["output_quantity_dimension_op"]
            value_index=int(operation.get("arg",0))
            if value_index>=len(args):
                return None
            value_type=args[value_index].type
            if not isinstance(value_type,str) or not value_type.startswith("Quantity"):
                return None
            op=str(operation.get("op"))
            if op=="divide_time":
                return self.language.combine_quantity_types(
                    value_type,
                    "Quantity:Time",
                    "divide",
                )
            return None
        if "output_attribute_dimension_op" in frame:
            operation=frame["output_attribute_dimension_op"]
            attribute_index=int(operation.get("attribute_arg",0))
            if attribute_index>=len(args):
                return None
            attribute_type=args[attribute_index].meta_dict().get("descriptor_value_type")
            if not isinstance(attribute_type,str) or not attribute_type.startswith("Quantity"):
                return None
            op=str(operation.get("op"))
            if op=="divide_time":
                return self.language.combine_quantity_types(
                    attribute_type,
                    "Quantity:Time",
                    "divide",
                )
            return None
        if "output_dimension_op" in frame:
            operation=frame["output_dimension_op"]
            indices=operation.get("args",[])
            if len(indices)!=2:
                return None
            left_index,right_index=(int(indices[0]),int(indices[1]))
            if left_index>=len(args) or right_index>=len(args):
                return None
            op=str(operation.get("op"))
            if op in {"multiply","divide"}:
                return self.language.combine_quantity_types(
                    args[left_index].type,
                    args[right_index].type,
                    op,
                )
            if op in {"power","root"}:
                base=args[left_index]
                degree=args[right_index]
                static_degree=self._static_number_value(degree)
                base_vector=self.language.quantity_dimension_vector(base.type)
                if op=="root" and static_degree == 0:
                    return None
                if base_vector == {}:
                    return "Quantity:Number"
                if static_degree is None:
                    return None
                factor=static_degree if op=="power" else Fraction(1,1)/static_degree
                return self.language.scale_quantity_dimension(base.type,factor)
        return None

    def _dimension_output_issue(
        self,
        entry: Entry,
        frame: dict,
        args: tuple[Node, ...],
        field_index: int,
        progress_index: int,
    ) -> Diagnostic | None:
        operation=frame.get("output_dimension_op")
        if not isinstance(operation,dict):
            return None
        op=str(operation.get("op"))
        if op not in {"power","root"}:
            return None
        indices=operation.get("args",[])
        if not isinstance(indices,list) or len(indices)!=2:
            return None
        base_index,degree_index=(int(indices[0]),int(indices[1]))
        if base_index>=len(args) or degree_index>=len(args):
            return None
        base=args[base_index]
        degree=args[degree_index]
        static_degree=self._static_number_value(degree)
        if op=="root" and static_degree == 0:
            return Diagnostic(
                "SemanticallyIncomplete",
                "Root degree cannot be zero.",
                field_index=field_index,
                field=entry.surface,
                progress_index=progress_index,
            )
        base_vector=self.language.quantity_dimension_vector(base.type)
        if base_vector != {} and static_degree is None:
            return Diagnostic(
                "SemanticallyIncomplete",
                f"{entry.surface} over a dimensionful quantity requires a statically known dimensionless exponent/degree.",
                field_index=field_index,
                field=entry.surface,
                expected="static Quantity:Number",
                actual=degree.type,
                progress_index=progress_index,
            )
        if static_degree is not None:
            factor=static_degree if op=="power" else Fraction(1,1)/static_degree
            if self.language.scale_quantity_dimension(base.type,factor) is None:
                return Diagnostic(
                    "DimensionMismatch",
                    f"{entry.surface} would produce non-integral dimension exponents in the current dimension model.",
                    field_index=field_index,
                    field=entry.surface,
                    expected="integral output dimension",
                    actual=base.type,
                    progress_index=progress_index,
                )
        return None

    def _static_number_value(self, node: Node) -> Fraction | None:
        if node.type != "Quantity:Number":
            return None
        return self._static_quantity_value(node)

    def _static_quantity_value(self, node: Node) -> Fraction | None:
        if not self.language.is_assignable(node.type, "Quantity"):
            return None
        if node.kind == "Number" and isinstance(node.value, (int, float, Fraction)):
            return Fraction(node.value)
        if node.kind == "QuantityValue" and node.children:
            return self._static_quantity_value(node.children[0])
        if node.name == "Opposite" and len(node.children) == 1:
            value = self._static_quantity_value(node.children[0])
            return -value if value is not None else None
        if node.name in {"Add", "Multiply", "Divide"} and len(node.children) == 2:
            left = self._static_quantity_value(node.children[0])
            right = self._static_quantity_value(node.children[1])
            if left is None or right is None:
                return None
            if node.name == "Add":
                return left + right
            if node.name == "Multiply":
                return left * right
            if right == 0:
                return None
            return left / right
        return None

    def _slot_value_domain(
        self,
        slot: dict,
        args: tuple[Node, ...],
        roles: tuple[str, ...],
    ) -> str | None:
        direct = slot.get("value_domain")
        if isinstance(direct, str):
            return direct
        source_role = slot.get("value_domain_from_role")
        if not source_role or source_role not in roles:
            return None
        source = args[roles.index(source_role)]
        domain = source.meta_dict().get("value_domain")
        return str(domain) if domain else None

    def _value_domain_issue(
        self,
        entry: Entry,
        frame: dict,
        args: tuple[Node, ...],
        roles: tuple[str, ...],
        field_index: int,
        progress_index: int,
    ) -> Diagnostic | None:
        slots = frame.get("slots", [])
        for role, arg in zip(roles, args):
            slot = next((s for s in slots if s.get("name") == role), None)
            if slot is None:
                continue
            domain = self._slot_value_domain(slot, args, roles)
            if domain is None:
                continue
            value = self._static_quantity_value(arg)
            if value is None:
                continue
            valid = True
            if domain == "nonnegative":
                valid = value >= 0
            elif domain == "positive":
                valid = value > 0
            elif domain == "positive_integer":
                valid = value > 0 and value.denominator == 1
            elif domain == "nonnegative_integer":
                valid = value >= 0 and value.denominator == 1
            if not valid:
                return Diagnostic(
                    "ValueDomainMismatch",
                    f"{entry.surface} role {role} requires {domain}, received {value}.",
                    field_index=field_index,
                    field=entry.surface,
                    expected=domain,
                    actual=str(value),
                    progress_index=progress_index,
                )
        return None

    def _value_domain_constraints(
        self,
        frame: dict,
        args: tuple[Node, ...],
        roles: tuple[str, ...],
    ) -> tuple[tuple[str, str], ...]:
        constraints: list[tuple[str, str]] = []
        slots = frame.get("slots", [])
        for role in roles:
            slot = next((s for s in slots if s.get("name") == role), None)
            if slot is None:
                continue
            domain = self._slot_value_domain(slot, args, roles)
            if domain is not None:
                constraints.append((role, domain))
        return tuple(constraints)

    def _make_call_node(
        self,
        entry: Entry,
        frame: dict,
        args: tuple[Node, ...],
        roles: tuple[str, ...],
        out_type: str,
    ) -> Node:
        normalize = frame.get("normalize")
        if normalize == "kind_predication":
            kind_node = self._make_kind_node(entry.data["derived_kind"]) if entry.data.get("derived_kind") else Node(kind="Root", type="Kind", name=entry.data.get("normalized_surface", entry.surface))
            meta = ()
            if entry.data.get("derived_kind"):
                prop = entry.data["derived_kind"].get("property")
                if prop: meta = (("property_expr", prop),)
            return Node(kind="RelationApply", type="Proposition", name="InstanceOf", children=(args[0], kind_node), roles=("entity", "kind"), meta=meta)
        if normalize == "compound_property_apply":
            return self._make_property_application(entry.data["property_expr"], args[0], out_type)
        if normalize == "state_boundary":
            if entry.data.get("state_relation_surface"):
                state = Node(kind="RelationApply", type="StateProposition", name=entry.data["state_relation_surface"],
                    children=args, roles=tuple(entry.data.get("state_relation_roles") or roles))
            else:
                state = self._make_property_application(entry.data["state_property_expr"], args[0], "StateProposition")
            return Node(kind="OperatorApply", type="EventSpec", name=frame.get("boundary", entry.data.get("boundary", "Boundary")), children=(state,), roles=("state",))
        if normalize == "state_relation_boundary":
            state = Node(kind="RelationApply", type="StateProposition", name=entry.data["state_relation_surface"], children=args, roles=roles)
            return Node(kind="OperatorApply", type="EventSpec", name=frame.get("boundary", "Boundary"), children=(state,), roles=("state",))
        if normalize == "threshold_property_apply":
            expr=entry.data["property_expr"]
            return self._make_property_application(expr, args[0], out_type)
        if normalize == "measured_property_apply":
            measured=entry.data["measured_property"]
            attribute=Node(kind="FunctionCall",type=measured["value_type"],name=measured["attribute"],children=(args[0],),roles=("subject",))
            value=Node(kind="Number",type=measured["value_type"],value=measured.get("literal_number"),name=str(measured.get("literal_number")))
            return Node(kind="RelationApply",type="Proposition",name="Equal",children=(attribute,value),roles=("left","right"))
        if normalize == "unit_quantity":
            unit = entry.data["unit_constructor"]
            amount = args[0]
            scale = Fraction(
                int(unit.get("scale_numerator", 1)),
                int(unit.get("scale_denominator", 1)),
            )
            static_amount = self._static_number_value(amount)
            if static_amount is not None:
                normalized_amount = Node(
                    kind="Number",
                    type="Quantity:Number",
                    value=static_amount * scale,
                    name=str(static_amount * scale),
                )
            elif scale == 1:
                normalized_amount = amount
            else:
                scale_node = Node(
                    kind="Number",
                    type="Quantity:Number",
                    value=scale,
                    name=str(scale),
                )
                normalized_amount = Node(
                    kind="OperatorApply",
                    type="Quantity:Number",
                    name="Multiply",
                    children=(scale_node, amount),
                    roles=("factor", "value"),
                )
            dimension = str(unit["dimension"])
            return Node(
                kind="QuantityValue",
                type=out_type,
                name=f"{dimension}Quantity",
                children=(normalized_amount,),
                roles=("amount",),
                meta=(
                    ("source_unit", entry.surface),
                    ("scale_numerator", scale.numerator),
                    ("scale_denominator", scale.denominator),
                ),
            )
        if normalize == "change_family_value":
            descriptor = args[1]
            meta = descriptor.meta_dict()
            family = meta.get("family")
            value = meta.get("family_value")
            attribute = Node(kind="Descriptor", type="AttributeDescriptor", name=str(family))
            target = Node(kind="Root", type=f"{family}Value" if family else "SemanticValue", name=str(value))
            return Node(kind="ProcessApply", type="EventSpec", name="Change",
                children=(args[0], attribute, target), roles=("theme","attribute","target"),
                meta=(("frame_id",frame.get("id")),("bound_roles",("theme","attribute","target"))))
        if normalize == "event_local_before_value":
            enclosing = Node(kind="EventBoundaryRef", type="Event", name="EnclosingEvent")
            return Node(kind="FunctionCall", type=out_type, name="BeforeValue", children=(args[0], enclosing), roles=("value", "event"))
        if normalize == "event_local_after_value":
            enclosing = Node(kind="EventBoundaryRef", type="Event", name="EnclosingEvent")
            return Node(kind="FunctionCall", type=out_type, name="AfterValue", children=(args[0], enclosing), roles=("value", "event"))
        if entry.surface == "Not" and args:
            child = args[0]
            if child.name == "Not" and len(child.children) == 1:
                return child.children[0]
            meta: list[tuple[str, object]] = []
            child_meta = child.meta_dict()
            if child_meta.get("property_expr"):
                meta.append(("property_expr", {"op":"not","arg":child_meta["property_expr"]}))
            if child_meta.get("property_subject"):
                meta.append(("property_subject", child_meta["property_subject"]))
            return Node(kind="OperatorApply", type=out_type, name="Not", children=(child,), roles=("proposition",), meta=tuple(meta))
        if entry.data.get("category") == "Property":
            return self._make_property_application(self.language.property_expr(entry), args[0], out_type)
        relation_is_proposition = self.language.is_assignable(out_type, "Proposition")
        kind = {"Process":"ProcessApply","Property":"PropertyApply","Relation":"RelationApply" if relation_is_proposition else "FunctionCall","Operator":"OperatorApply","Kind":"RelationApply"}.get(entry.data.get("category"), "Apply")
        meta: list[tuple[str, object]] = []
        if entry.data.get("contextual") or frame.get("contextual"):
            meta.append(("contextual", True))
        output_domain = frame.get("output_value_domain") or entry.data.get("output_value_domain")
        if output_domain:
            meta.append(("value_domain", output_domain))
        constraints = self._value_domain_constraints(frame, args, roles)
        if constraints:
            meta.append(("value_domain_constraints", constraints))
        if frame.get("utterance_context"):
            context_spec = frame["utterance_context"]
            meta.append((
                "utterance_context_roles",
                tuple(
                    context_spec[key]
                    for key in ("speaker_role", "addressee_role", "content_role")
                    if context_spec.get(key)
                ),
            ))
        if entry.data.get("category") == "Process":
            meta.append(("frame_id", frame.get("id")))
            meta.append(("bound_roles", tuple(roles)))
            if frame.get("execution_requires_any"):
                meta.append(("execution_requires_any", tuple(tuple(group) for group in frame["execution_requires_any"])))
        return Node(kind=kind, type=out_type, name=entry.data.get("normalized_surface", entry.surface), children=args, roles=roles, meta=tuple(meta))

    def _make_kind_node(self, expr: dict) -> Node:
        if expr.get("op") == "kind":
            return Node(kind="Root", type="Kind", name=expr["surface"])
        if expr.get("op") == "restrict_kind":
            return Node(kind="CompoundKind", type="Kind", name="RestrictKind",
                children=(self._make_kind_node(expr["base"]), self._make_property_descriptor_node(expr["property"])),
                roles=("base","property"), meta=(("property_expr", expr["property"]),))
        return Node(kind="Root", type="Kind", name="UnknownKind")

    def _make_property_descriptor_node(self, expr: dict) -> Node:
        if expr.get("op") == "atom":
            return Node(kind="Root", type="PropertyDescriptor", name=expr["surface"], meta=(("property_expr",expr),))
        if expr.get("op") == "not":
            return Node(kind="OperatorApply", type="PropertyDescriptor", name="NotProperty",
                children=(self._make_property_descriptor_node(expr["arg"]),), meta=(("property_expr",expr),))
        if expr.get("op") == "and":
            return Node(kind="OperatorApply", type="PropertyDescriptor", name="AndProperty",
                children=tuple(self._make_property_descriptor_node(x) for x in expr.get("args",[])), meta=(("property_expr",expr),))
        if expr.get("op") in {"high","low"}:
            attribute=Node(kind="Descriptor", type="AttributeDescriptor", name=expr["attribute"],
                meta=(("descriptor_value_type",expr["value_type"]),))
            name="HighProperty" if expr["op"]=="high" else "LowProperty"
            return Node(kind="OperatorApply", type="PropertyDescriptor", name=name,
                children=(attribute,), roles=("attribute",), meta=(("property_expr",expr),("contextual",True)))
        return Node(kind="Root", type="PropertyDescriptor", name="UnknownProperty")

    def _make_property_application(self, expr: dict, subject: Node, out_type: str = "Proposition") -> Node:
        meta=(("property_expr",expr),("property_subject",subject.canonical()))
        if expr.get("op") == "atom":
            return Node(kind="PropertyApply", type=out_type, name=expr["surface"], children=(subject,), roles=("subject",), meta=meta)
        if expr.get("op") == "not":
            return Node(kind="OperatorApply", type=out_type, name="Not", children=(self._make_property_application(expr["arg"],subject,out_type),), roles=("proposition",), meta=meta)
        if expr.get("op") == "and":
            return Node(kind="OperatorApply", type=out_type, name="And",
                children=tuple(self._make_property_application(x,subject,out_type) for x in expr.get("args",[])), meta=meta)
        if expr.get("op") in {"high","low"}:
            attribute=Node(kind="FunctionCall",type=expr["value_type"],name=expr["attribute"],children=(subject,),roles=("subject",))
            name="High" if expr["op"]=="high" else "Low"
            return Node(kind="RelationApply",type=out_type,name=name,children=(attribute,),roles=("value",),meta=meta+(("contextual",True),))
        return Node(kind="PropertyApply", type=out_type, name="UnknownProperty", children=(subject,), meta=meta)

    def _parse_binder(self, field: str, index: int, expected_type: str) -> list[Candidate]:
        if not self.language.is_assignable("Binder", expected_type):
            self._record_type_mismatch(index, field, expected_type, "Binder")
            return []
        native = re.fullmatch(r":«([A-Za-z]+)»(?::([A-Za-z][A-Za-z0-9_]*|«.+»))?", field)
        if native:
            label, witness = native.groups()
            if not self.language.resolve_entries(label) and not self.language.has_known_segmentation(label):
                self._diagnostics.append(Diagnostic(
                    "InvalidBinderLabel",
                    "Rune-native binder label must be one or more approved Cuspell roots.",
                    field_index=index, field=field,
                ))
                return []
            if witness is None:
                bound_type = "Any"
            elif witness.startswith("«"):
                # Reuse exactly the established named-Kind domain lookup.
                legacy = self._parse_binder("native:" + witness, index, "Binder")
                if not legacy:
                    return []
                bound_type = legacy[0].node.meta_dict()["bound_type"]
            else:
                exemplar = Parser(self.language).parse_phrase(
                    witness, expected_type="SemanticValue",
                )
                if isinstance(exemplar, Diagnostic):
                    self._diagnostics.append(Diagnostic(
                        "InvalidBinderDomain",
                        f"Cuspell type witness {witness} has no single typed reading.",
                        field_index=index, field=field,
                    ))
                    return []
                # A type witness denotes the *type of its value*; Thing
                # denotes Kind, while This / Self denotes Entity.
                bound_type = exemplar.type
            node = Node(
                kind="Binder", type="Binder", name=f"«{label}»", value=witness or "",
                meta=(("bound_type", bound_type), ("rune_native", True)),
            )
            return [Candidate(node, index + 1)]
        match = re.fullmatch(
            r"(?:\[)?([A-Za-z][A-Za-z0-9_]*):((?:[A-Za-z][A-Za-z0-9_:]*)|(?:«.+»))(?:\])?",
            field,
        )
        if not match:
            self._diagnostics.append(Diagnostic(
                "SyntaxError", f"Invalid binder syntax: {field}", field_index=index, field=field
            ))
            return []
        name, domain_surface = match.groups()

        # Exact semantic type names take precedence over lexical Kind
        # surfaces with the same spelling. This keeps binders such as
        # s:Sign and r:Region typed as Sign/Region rather than Entity.
        if domain_surface in self.language.parents and domain_surface not in {"Any","Binder"}:
            bound_type = domain_surface
        else:
            named_kind_types: list[tuple[str, ...]] = []
            if domain_surface.startswith("«") and domain_surface.endswith("»"):
                sign = domain_surface[1:-1]
                for entry in self.language.old_name_entries(sign):
                    meaning = entry.get("meaning", {})
                    if meaning.get("type") != "Kind":
                        continue
                    if meaning.get("kind") == "concept":
                        concept_id = meaning.get("concept_id")
                        classify_types = (
                            self.language.world_kind_classifies_types(str(concept_id))
                            if concept_id is not None
                            else ()
                        )
                        named_kind_types.append(classify_types or ("Entity",))
                    else:
                        # A non-concept Kind-valued Old Name is an Entity Kind
                        # under the existing lexical Kind system.
                        named_kind_types.append(("Entity",))
                for entry in self.language.new_name_entries(sign):
                    if entry.get("referent_type") != "Kind":
                        continue
                    referent_id = entry.get("referent_id")
                    classify_types = (
                        self.language.world_kind_classifies_types(str(referent_id))
                        if referent_id is not None
                        else ()
                    )
                    named_kind_types.append(classify_types or ("Entity",))
                domains = []
            else:
                domains = [
                    entry
                    for entry in self.language.resolve_entries(domain_surface)
                    if entry.atom_type == "Kind"
                ]

            if len(domains) + len(named_kind_types) > 1:
                self._diagnostics.append(Diagnostic(
                    "AmbiguousCompound",
                    f"Binder domain {domain_surface} has multiple Kind meanings.",
                    field_index=index,
                    field=field,
                ))
                return []

            if domains:
                bound_type = "Entity"
            elif len(named_kind_types) == 1:
                classify_types = named_kind_types[0]
                if len(classify_types) != 1:
                    self._diagnostics.append(Diagnostic(
                        "AmbiguousKindDomain",
                        (
                            f"Binder domain {domain_surface} classifies multiple "
                            f"semantic types: {', '.join(classify_types)}. "
                            "Bind an explicit semantic type and apply the Kind "
                            "predicate in the query."
                        ),
                        field_index=index,
                        field=field,
                    ))
                    return []
                bound_type = classify_types[0]
            else:
                self._diagnostics.append(Diagnostic(
                    "TypeMismatch",
                    f"Binder domain {domain_surface} is neither a registered Kind, named Kind, nor semantic type.",
                    field_index=index,
                    field=field,
                    expected="Kind/semantic type",
                    actual="UnknownDomain",
                ))
                return []
        node = Node(
            kind="Binder",
            type="Binder",
            name=name,
            value=domain_surface,
            meta=(("bound_type", bound_type),),
        )
        return [Candidate(node, index + 1)]

    def _parse_variable(self, field: str, index: int, expected_type: str, context: Context) -> list[Candidate]:
        name = field[1:]
        variables = context.variable_map()
        actual = variables.get(name)
        if actual is None:
            self._diagnostics.append(Diagnostic(
                "FreeVariable",
                f"Variable {field} is not bound in this scope.",
                field_index=index,
                field=field,
            ))
            return []
        if actual == _INFER_BINDER_TYPE:
            # Temporarily bind the type required by this particular typed slot.
            # At completion, all uses must agree on a single semantic type.
            return [Candidate(Node(
                kind="Variable", type=expected_type, name=field,
                meta=(("inference_expected", expected_type),),
            ), index + 1)]
        if not self.language.is_assignable(actual, expected_type):
            self._record_type_mismatch(index, field, expected_type, actual)
            return []
        return [Candidate(Node(kind="Variable", type=actual, name=field), index + 1)]

    def _resolve_inferred_binders(
        self, node: Node, binder_names: tuple[str, ...], field_index: int,
    ) -> Node | None:
        """Determine a native binder type from all typed uses, never by guessing.

        Generic 'Any' / 'SemanticValue' argument slots supply no evidence.
        The unique most specific type *required by a slot* must satisfy every
        collected constraint. Different legal overload readings remain separate
        candidates and are reported by the existing ambiguity diagnostics.
        """
        requirements: dict[str, list[str]] = {name: [] for name in binder_names}

        def collect(part: Node) -> None:
            if (part.kind == "Variable" and part.name
                    and part.name[1:] in requirements):
                required = part.meta_dict().get("inference_expected")
                if required not in (None, "Any", "SemanticValue"):
                    requirements[part.name[1:]].append(str(required))
            for child in part.children:
                collect(child)

        collect(node)
        chosen: dict[str, str] = {}
        for name, constraints in requirements.items():
            if not constraints:
                self._diagnostics.append(Diagnostic(
                    "MissingBinderType",
                    f"Rune label {name} needs a Cuspell type witness: "
                    "no typed use establishes its semantic type.",
                    field_index=field_index,
                ))
                return None
            compatible = [
                typ for typ in set(constraints)
                if all(self.language.is_assignable(typ, other) for other in constraints)
            ]
            if len(compatible) != 1:
                self._diagnostics.append(Diagnostic(
                    "ConflictingBinderTypes",
                    f"Rune label {name} has no uniquely compatible type: "
                    f"{', '.join(sorted(set(constraints)))}.",
                    field_index=field_index,
                ))
                return None
            chosen[name] = compatible[0]

        def resolve(part: Node) -> Node:
            if part.kind == "Binder" and part.name in chosen:
                typ = chosen[part.name]
                return replace(
                    part, value=f"inferred:{typ}",
                    meta=(("bound_type", typ), ("rune_native", True),
                          ("inferred_type", True)),
                )
            if part.kind == "Variable" and part.name and part.name[1:] in chosen:
                typ = chosen[part.name[1:]]
                if part.meta_dict().get("inference_expected"):
                    return replace(
                        part, type=typ, meta=(("inferred_type", True),),
                    )
            if part.children:
                return replace(part, children=tuple(resolve(c) for c in part.children))
            return part

        return resolve(node)

    def _parse_collection(self, field: str, index: int, expected_type: str, context: Context) -> list[Candidate]:
        inner = field[1:-1].strip()
        items = split_top_level(inner, ",") if inner else []
        if expected_type.startswith("Collection:"):
            item_type = expected_type.split(":", 1)[1]
        elif expected_type in {"Collection", "SemanticValue", "Any"}:
            item_type = "SemanticValue"
        else:
            self._record_type_mismatch(index, field, expected_type, "Collection")
            return []
        nodes: list[Node] = []
        for item in items:
            parsed = Parser(self.language).parse_phrase(item, item_type, context)
            if isinstance(parsed, Diagnostic):
                self._diagnostics.append(replace(
                    parsed, field_index=index, field=item, progress_index=index
                ))
                return []
            nodes.append(self._clear_source_spans(parsed))
        if item_type == "SemanticValue" and nodes:
            first = nodes[0].type
            if all(node.type == first for node in nodes):
                collection_type = f"Collection:{first}"
            else:
                collection_type = "Collection"
        else:
            collection_type = f"Collection:{item_type}" if item_type != "SemanticValue" else "Collection"
        if not self.language.is_assignable(collection_type, expected_type):
            self._record_type_mismatch(index, field, expected_type, collection_type)
            return []
        return [Candidate(Node(kind="Collection", type=collection_type, children=tuple(nodes)), index + 1)]

    def _record_type_mismatch(
        self,
        index: int,
        field: str,
        expected: str,
        actual: str,
        progress_index: int | None = None,
    ) -> None:
        code = "TypeMismatch"
        message = f"Expected {expected}, received {actual} at {field}."
        if expected.startswith("Quantity:") and actual.startswith("Quantity:"):
            expected_dimension = self.language.quantity_dimension_vector(expected)
            actual_dimension = self.language.quantity_dimension_vector(actual)
            if (
                expected_dimension is not None
                and actual_dimension is not None
                and expected_dimension != actual_dimension
            ):
                code = "DimensionMismatch"
                message = (
                    f"Expected quantity dimension {expected}, received {actual} at {field}."
                )
        self._diagnostics.append(Diagnostic(
            code,
            message,
            field_index=index,
            field=field,
            expected=expected,
            actual=actual,
            progress_index=progress_index,
        ))

    def mana_cost(self, source: str) -> int:
        text = source.strip()
        if text and text[-1] in ".?!":
            text = text[:-1]
        if text.startswith(("!", "?")):
            text = text[1:]
        # Rune-native binder labels and references are grammatical handles:
        # the quoted root-shaped sign is not invoked as semantic content.
        # Type witnesses are metalinguistic too, like legacy name:Domain.
        text = re.sub(
            r"(?<!\S)(?:\$|:)«[^«»]+»(?::(?:[A-Za-z][A-Za-z0-9_]*|«.+»))?",
            " ", text,
        )
        # Legacy flat-group closer words are not semantic registered runes,
        # even though their Latin spelling can be decomposed into roots.
        text = re.sub(r"(?<!\S)(?:SequenceEnd|ConcurrentEnd)(?=\s|$)", " ", text)
        return self._mana_cost_text(text)

    def _mana_cost_text(self, text: str) -> int:
        """Count written semantic material while respecting exact quoted names.

        A registered Old Name pays the frozen cost of its historical name
        units, not the cost of its semantic expansion. Unregistered/New Names
        remain Signs and gain no macro expansion; any semantic roots physically
        written inside their quoted spelling still cost normally.
        """
        cost = 0
        cursor = 0
        i = 0
        while i < len(text):
            if text[i] != "«":
                i += 1
                continue

            cost += self._plain_mana_cost(text[cursor:i])
            depth = 1
            j = i + 1
            while j < len(text) and depth:
                if text[j] == "«":
                    depth += 1
                elif text[j] == "»":
                    depth -= 1
                j += 1

            if depth:
                # Malformed quote: preserve the old conservative behavior for
                # cost accounting; syntax checking will reject the expression.
                cost += self._plain_mana_cost(text[i:])
                return cost

            content = text[i + 1:j - 1]
            old_cost = self.language.old_name_cost(content)
            if old_cost is not None:
                cost += old_cost
            else:
                cost += self._mana_cost_text(content)
            i = j
            cursor = j

        cost += self._plain_mana_cost(text[cursor:])
        return cost

    def _plain_mana_cost(self, text: str) -> int:
        cost = 0
        token_pattern = re.compile(
            r"\[([A-Za-z][A-Za-z0-9_]*):([A-Za-z][A-Za-z0-9_:]*)\]"
            r"|\$[A-Za-z][A-Za-z0-9_]*"
            r"|:[A-Za-z][A-Za-z0-9_]*"
            r"|@+"
            r"|[A-Za-z][A-Za-z0-9_]*"
        )
        for match in token_pattern.finditer(text):
            token = match.group(0)
            if token.startswith("$") or token.startswith(":"):
                continue
            if token.startswith("["):
                domain = match.group(2)
                domain_cost = self.language.written_rune_cost(domain) if domain else None
                cost += domain_cost or 0
                continue
            if set(token) == {"@"}:
                cost += len(token)
                continue
            token_cost = self.language.written_rune_cost(token)
            if token_cost is not None:
                cost += token_cost
        return cost
