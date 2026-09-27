from __future__ import annotations

from dataclasses import dataclass, replace
import re
from typing import Iterable

from .language import Entry, Language
from .model import CheckResult, Diagnostic, Node
from .surface import split_fields, split_phrases, split_top_level, strip_sentence
from .validator import validate_semantics


@dataclass(frozen=True)
class Context:
    variables: tuple[tuple[str, str], ...] = ()
    in_event: bool = False

    def variable_map(self) -> dict[str, str]:
        return dict(self.variables)

    def with_variable(self, name: str, typ: str) -> "Context":
        data = self.variable_map()
        data[name] = typ
        return replace(self, variables=tuple(sorted(data.items())))

    def with_event(self) -> "Context":
        return replace(self, in_event=True)


@dataclass(frozen=True)
class Candidate:
    node: Node
    next_index: int


class Parser:
    def __init__(self, language: Language):
        self.language = language
        self._diagnostics: list[Diagnostic] = []
        self._fields: list[str] = []

    def check(self, source: str) -> CheckResult:
        self._diagnostics = []
        try:
            mood, body = strip_sentence(source)
        except ValueError as exc:
            return CheckResult(
                valid=False,
                source=source,
                mood="unknown",
                phrases=[],
                diagnostics=[Diagnostic("SyntaxError", str(exc))],
                mana=self.mana_cost(source),
            )

        phrases = split_phrases(body)
        mana = self.mana_cost(source)
        if len(phrases) != 1:
            return CheckResult(
                valid=False,
                source=source,
                mood=mood,
                phrases=phrases,
                diagnostics=[Diagnostic(
                    "SyntaxError",
                    f"Sentence contains {len(phrases)} uncombined top-level expressions. "
                    "Whitespace does not mean And or Sequence.",
                )],
                mana=mana,
            )

        expected = {
            "command": "EventSpec",
            "assertion": "Proposition",
            "question": "Proposition",
        }[mood]
        parse = self.parse_phrase(phrases[0], expected_type=expected, context=Context())
        if isinstance(parse, Diagnostic):
            return CheckResult(
                valid=False,
                source=source,
                mood=mood,
                phrases=phrases,
                diagnostics=[parse],
                mana=mana,
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
        ast = Node(
            kind=mood.capitalize(),
            type={"command":"Command","assertion":"Assertion","question":"Question"}[mood],
            name=mood.capitalize(),
            children=(parse,),
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
    ) -> Node | Diagnostic:
        self._diagnostics = []
        self._fields = split_fields(phrase)
        ctx = context or Context()
        if not self._fields:
            return Diagnostic("SyntaxError", "Empty expression.")
        candidates = self._parse_expr(0, expected_type, ctx, outer_head=True)
        full = [c for c in candidates if c.next_index == len(self._fields)]
        if not full:
            if self._diagnostics:
                return self._best_diagnostic()
            return Diagnostic(
                "SyntaxError",
                "No legal parse consumed every pipe-bound field in the phrase.",
            )
        unique: dict[str, Node] = {c.node.canonical(): c.node for c in full}
        if len(unique) > 1:
            meanings = "; ".join(sorted(unique))
            return Diagnostic(
                "AmbiguousPhrase",
                f"More than one distinct typed parse is legal: {meanings}",
            )
        return next(iter(unique.values()))

    def _best_diagnostic(self) -> Diagnostic:
        with_index = [d for d in self._diagnostics if d.field_index is not None]
        if not with_index:
            return self._diagnostics[-1]
        furthest = max(d.field_index or 0 for d in with_index)
        best = [d for d in with_index if d.field_index == furthest]
        for code in ("TypeMismatch", "IllegalCompound", "FreeVariable", "UnknownRoot", "MissingRequiredRole", "InvalidRole"):
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
        if index >= len(self._fields):
            return []
        field = self._fields[index]

        if field.startswith("(") and field.endswith(")"):
            inner = field[1:-1].strip()
            nested = Parser(self.language).parse_phrase(inner, expected_type, context)
            if isinstance(nested, Diagnostic):
                self._diagnostics.append(replace(nested, field_index=index, field=field))
                return []
            return [Candidate(nested, index + 1)]

        if field.startswith("{") and field.endswith("}"):
            return self._parse_collection(field, index, expected_type, context)

        if field.startswith("[") and field.endswith("]"):
            return self._parse_binder(field, index, expected_type)

        if field.startswith("$"):
            return self._parse_variable(field, index, expected_type, context)

        if re.fullmatch(r"@+", field):
            node = Node(kind="Number", type="Quantity:Number", value=len(field), name=field)
            if self.language.is_assignable(node.type, expected_type):
                return [Candidate(node, index + 1)]
            self._record_type_mismatch(index, field, expected_type, node.type)
            return []

        if field.startswith(":"):
            self._diagnostics.append(Diagnostic(
                "InvalidRole",
                f"Role marker {field} appeared where an expression was expected.",
                field_index=index,
                field=field,
            ))
            return []

        entries = self.language.resolve_entries(field)
        if not entries:
            if self.language.has_known_segmentation(field):
                segmentations = [" + ".join(parts) for parts in self.language.known_segmentations(field)]
                self._diagnostics.append(Diagnostic(
                    "IllegalCompound",
                    f"Known roots can segment {field}, but no registered composition rule licenses it: " + "; ".join(segmentations),
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
        if entry.atom_type and self.language.is_assignable(entry.atom_type, expected_type):
            meta: list[tuple[str, object]] = []
            if entry.data.get("descriptor_value_type"):
                meta.append(("descriptor_value_type", entry.data["descriptor_value_type"]))
            if entry.data.get("property_expr"):
                meta.append(("property_expr", entry.data["property_expr"]))
            kind = "Descriptor" if entry.atom_type in {"AttributeDescriptor", "PropertyDescriptor"} else "Reference"
            if entry.atom_type == "Kind": kind = "Root"
            node_name = entry.data.get("normalized_surface", entry.surface)
            if entry.atom_type == "Kind" and entry.data.get("derived_kind"):
                node = self._make_kind_node(entry.data["derived_kind"])
            else:
                node = Node(kind=kind, type=entry.atom_type, name=node_name, meta=tuple(meta))
            candidates.append(Candidate(node, index + 1))
        elif entry.atom_type and not entry.frames:
            self._record_type_mismatch(index, entry.surface, expected_type, entry.atom_type)
        for frame in entry.frames:
            candidates.extend(self._parse_frame(entry, frame, index, expected_type, context))
        if not candidates and entry.atom_type and entry.frames and not self.language.is_assignable(entry.atom_type, expected_type):
            self._record_type_mismatch(index, entry.surface, expected_type, entry.atom_type)
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

        def recurse(slot_i: int, state: State) -> None:
            if slot_i >= len(slots):
                finalize_named(state)
                return

            slot = slots[slot_i]
            if state.pos < len(self._fields) and self._fields[state.pos].startswith(":"):
                if slot.get("required", True):
                    self._diagnostics.append(Diagnostic(
                        "MissingRequiredRole",
                        f"Missing required role {slot['name']} for {entry.surface}.",
                        field_index=state.pos,
                        field=self._fields[state.pos],
                    ))
                    return
                finalize_named(state)
                return

            expected_slot = self._resolve_slot_type(slot["type"], state.args, expected_type)
            if expected_slot is None:
                return

            if not slot.get("required", True):
                finalize_named(state)

            child_candidates = self._parse_expr(state.pos, expected_slot, state.ctx)
            for child in child_candidates:
                new_ctx = state.ctx
                if child.node.kind == "Binder":
                    binder_type = child.node.meta_dict().get("bound_type", "Entity")
                    new_ctx = new_ctx.with_variable(child.node.name or "?", binder_type)
                recurse(slot_i + 1, State(
                    pos=child.next_index,
                    args=state.args + (child.node,),
                    roles=state.roles + (slot["name"],),
                    ctx=new_ctx,
                    bound_names=state.bound_names + (slot["name"],),
                ))

        def finalize_named(state: State) -> None:
            states = [state]
            while True:
                advanced: list[State] = []
                changed = False
                for st in states:
                    if st.pos >= len(self._fields) or not self._fields[st.pos].startswith(":"):
                        advanced.append(st)
                        continue
                    role_token = self._fields[st.pos]
                    role = role_token[1:]
                    slot = next((s for s in slots if s["name"] == role), None)
                    if slot is None:
                        self._diagnostics.append(Diagnostic(
                            "InvalidRole",
                            f"{entry.surface} has no role named {role}.",
                            field_index=st.pos,
                            field=role_token,
                        ))
                        continue
                    if role in st.bound_names:
                        self._diagnostics.append(Diagnostic(
                            "InvalidRole",
                            f"Role {role} is already bound for {entry.surface}.",
                            field_index=st.pos,
                            field=role_token,
                        ))
                        continue
                    expected_role = self._resolve_slot_type(slot["type"], st.args, expected_type)
                    if expected_role is None:
                        continue
                    children = self._parse_expr(st.pos + 1, expected_role, st.ctx)
                    for child in children:
                        advanced.append(State(
                            pos=child.next_index,
                            args=st.args + (child.node,),
                            roles=st.roles + (role,),
                            ctx=st.ctx,
                            bound_names=st.bound_names + (role,),
                        ))
                        changed = True
                states = advanced
                if not changed:
                    break

            for st in states:
                required = [s["name"] for s in slots if s.get("required", True)]
                if any(name not in st.bound_names for name in required):
                    continue
                out_type = self._resolve_output_type(frame, st.args)
                if out_type is None or not self.language.is_assignable(out_type, expected_type):
                    if out_type is not None:
                        self._record_type_mismatch(head_index, entry.surface, expected_type, out_type)
                    continue
                node = self._make_call_node(entry, frame, st.args, st.roles, out_type)
                results.append(Candidate(node, st.pos))

        recurse(0, State(head_index + 1, (), (), frame_ctx, ()))
        return results

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
        return None

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
            return self._make_property_application(entry.data["property_expr"], args[0])
        if normalize == "state_boundary":
            state = self._make_property_application(entry.data["state_property_expr"], args[0])
            return Node(kind="OperatorApply", type="EventSpec", name=frame.get("boundary", entry.data.get("boundary", "Boundary")), children=(state,), roles=("state",))
        if normalize == "event_local_before_value":
            enclosing = Node(kind="EventBoundaryRef", type="Event", name="EnclosingEvent")
            return Node(kind="FunctionCall", type=out_type, name="BeforeValue", children=(args[0], enclosing), roles=("value", "event"))
        if normalize == "event_local_after_value":
            enclosing = Node(kind="EventBoundaryRef", type="Event", name="EnclosingEvent")
            return Node(kind="FunctionCall", type=out_type, name="AfterValue", children=(args[0], enclosing), roles=("value", "event"))
        if entry.data.get("category") == "Property":
            return self._make_property_application(self.language.property_expr(entry), args[0])
        kind = {"Process":"ProcessApply","Property":"PropertyApply","Relation":"FunctionCall" if out_type != "Proposition" else "RelationApply","Operator":"OperatorApply","Kind":"RelationApply"}.get(entry.data.get("category"), "Apply")
        return Node(kind=kind, type=out_type, name=entry.data.get("normalized_surface", entry.surface), children=args, roles=roles)

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
        return Node(kind="Root", type="PropertyDescriptor", name="UnknownProperty")

    def _make_property_application(self, expr: dict, subject: Node) -> Node:
        if expr.get("op") == "atom":
            return Node(kind="PropertyApply", type="Proposition", name=expr["surface"], children=(subject,), roles=("subject",), meta=(("property_expr",expr),))
        if expr.get("op") == "not":
            return Node(kind="OperatorApply", type="Proposition", name="Not", children=(self._make_property_application(expr["arg"],subject),), roles=("proposition",), meta=(("property_expr",expr),))
        if expr.get("op") == "and":
            return Node(kind="OperatorApply", type="Proposition", name="And",
                children=tuple(self._make_property_application(x,subject) for x in expr.get("args",[])), meta=(("property_expr",expr),))
        return Node(kind="PropertyApply", type="Proposition", name="UnknownProperty", children=(subject,))

    def _parse_binder(self, field: str, index: int, expected_type: str) -> list[Candidate]:
        if not self.language.is_assignable("Binder", expected_type):
            self._record_type_mismatch(index, field, expected_type, "Binder")
            return []
        match = re.fullmatch(r"\[([A-Za-z][A-Za-z0-9_]*):([A-Za-z][A-Za-z0-9_]*)\]", field)
        if not match:
            self._diagnostics.append(Diagnostic(
                "SyntaxError", f"Invalid binder syntax: {field}", field_index=index, field=field
            ))
            return []
        name, domain_surface = match.groups()
        domains = [entry for entry in self.language.resolve_entries(domain_surface) if entry.atom_type == "Kind"]
        if not domains:
            self._diagnostics.append(Diagnostic(
                "TypeMismatch",
                f"Binder domain {domain_surface} is not a registered or derivable Kind.",
                field_index=index,
                field=field,
                expected="Kind",
                actual="UnknownRoot/NonKind",
            ))
            return []
        if len(domains) > 1:
            self._diagnostics.append(Diagnostic(
                "AmbiguousCompound",
                f"Binder domain {domain_surface} has multiple compound meanings.",
                field_index=index,
                field=field,
            ))
            return []
        node = Node(
            kind="Binder",
            type="Binder",
            name=name,
            value=domain_surface,
            meta=(("bound_type", "Entity"),),
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
        if not self.language.is_assignable(actual, expected_type):
            self._record_type_mismatch(index, field, expected_type, actual)
            return []
        return [Candidate(Node(kind="Variable", type=actual, name=field), index + 1)]

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
                self._diagnostics.append(replace(parsed, field_index=index, field=item))
                return []
            nodes.append(parsed)
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

    def _record_type_mismatch(self, index: int, field: str, expected: str, actual: str) -> None:
        self._diagnostics.append(Diagnostic(
            "TypeMismatch",
            f"Expected {expected}, received {actual} at {field}.",
            field_index=index,
            field=field,
            expected=expected,
            actual=actual,
        ))

    def mana_cost(self, source: str) -> int:
        text = source.strip().rstrip(".")
        if text.startswith(("!", "?")):
            text = text[1:]
        cost = 0
        token_pattern = re.compile(r"\[([A-Za-z][A-Za-z0-9_]*):([A-Za-z][A-Za-z0-9_]*)\]|\$[A-Za-z][A-Za-z0-9_]*|:[A-Za-z][A-Za-z0-9_]*|@+|[A-Za-z][A-Za-z0-9_]*")
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
