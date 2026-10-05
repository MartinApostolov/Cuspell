from __future__ import annotations

from typing import Any, Iterable

from .model import Diagnostic, Node


def validate_semantics(node: Node) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for current, source_span in walk_with_source_span(node):
        expr = current.meta_dict().get("property_expr")
        if isinstance(expr, dict):
            conflict = property_conflict(expr)
            if conflict is not None:
                diagnostics.append(diagnostic_at("ContradictoryConstraint", conflict, source_span))
        if current.name == "Create" and current.children:
            role_map = dict(zip(current.roles, current.children))
            binder = role_map.get("result")
            profile = role_map.get("profile")
            if binder is not None and binder.kind == "Binder" and profile is not None:
                variable_name = "$" + (binder.name or "")
                if not any(
                    candidate.kind == "Variable"
                    and candidate.name == variable_name
                    for candidate in walk(profile)
                ):
                    diagnostics.append(diagnostic_at(
                        "SemanticallyIncomplete",
                        "Create profile must constrain or relate its fresh result binder.",
                        source_span,
                    ))
        if current.name == "And" and current.children:
            items = current.children[0].children if current.children[0].kind == "Collection" else current.children
            grouped: dict[str, list[dict[str, Any]]] = {}
            for item in items:
                meta = item.meta_dict()
                subject = meta.get("property_subject")
                prop = meta.get("property_expr")
                if subject and isinstance(prop, dict):
                    grouped.setdefault(str(subject), []).append(prop)
            for subject, properties in grouped.items():
                if len(properties) < 2:
                    continue
                conflict = property_conflict({"op":"and","args":properties})
                if conflict is not None:
                    diagnostics.append(diagnostic_at(
                        "ContradictoryConstraint",
                        f"For {subject}: {conflict}",
                        source_span,
                    ))
    unique: dict[tuple[str, str, int | None, int | None], Diagnostic] = {}
    for diag in diagnostics:
        unique[(diag.code, diag.message, diag.source_start, diag.source_end)] = diag
    return list(unique.values())



def validate_execution_closure(node: Node) -> list[Diagnostic]:
    """Check command-only closure requirements after language semantics are valid."""
    diagnostics: list[Diagnostic] = []
    for current, source_span in walk_with_source_span(node):
        meta = current.meta_dict()
        if meta.get("contextual"):
            diagnostics.append(diagnostic_at(
                "SemanticallyIncomplete",
                f"{current.name or current.kind} is context-dependent and must be made objective before magical execution.",
                source_span,
            ))
        if current.type != "EventSpec":
            continue
        groups = meta.get("execution_requires_any") or ()
        bound = set(meta.get("bound_roles") or ())
        for group in groups:
            options = tuple(group)
            if options and not any(role in bound for role in options):
                diagnostics.append(diagnostic_at(
                    "SemanticallyIncomplete",
                    f"{current.name or current.kind} requires at least one of: {', '.join(options)}.",
                    source_span,
                ))
    unique: dict[tuple[str, str, int | None, int | None], Diagnostic] = {}
    for diag in diagnostics:
        unique[(diag.code, diag.message, diag.source_start, diag.source_end)] = diag
    return list(unique.values())

def diagnostic_at(
    code: str,
    message: str,
    source_span: tuple[int, int] | None,
) -> Diagnostic:
    if source_span is None:
        return Diagnostic(code, message)
    return Diagnostic(
        code,
        message,
        source_start=source_span[0],
        source_end=source_span[1],
    )


def walk_with_source_span(
    node: Node,
    inherited_span: tuple[int, int] | None = None,
) -> Iterable[tuple[Node, tuple[int, int] | None]]:
    source_span = inherited_span
    if node.source_start is not None and node.source_end is not None:
        source_span = (node.source_start, node.source_end)
    yield node, source_span
    for child in node.children:
        yield from walk_with_source_span(child, source_span)


def walk(node: Node) -> Iterable[Node]:
    for current, _ in walk_with_source_span(node):
        yield current


def property_conflict(expr: dict[str, Any]) -> str | None:
    literals = list(_literals(expr, True))
    by_surface: dict[str, set[bool]] = {}
    for literal in literals:
        by_surface.setdefault(literal["surface"], set()).add(literal["positive"])
    for surface, polarities in sorted(by_surface.items()):
        if len(polarities) > 1:
            return f"Property constraints require both {surface} and Not{surface}."
    by_family: dict[str, set[str]] = {}
    for literal in literals:
        if not literal["positive"]: continue
        family = literal.get("family"); value = literal.get("family_value")
        if family and value: by_family.setdefault(family, set()).add(value)
    for family, values in sorted(by_family.items()):
        if len(values) > 1:
            return f"Exclusive family {family} is constrained to incompatible values: {', '.join(sorted(values))}."
    return None


def _literals(expr: dict[str, Any], positive: bool):
    op = expr.get("op")
    if op == "atom":
        yield {"surface":expr["surface"],"positive":positive,"family":expr.get("family"),"family_value":expr.get("family_value")}
    elif op == "not":
        yield from _literals(expr["arg"], not positive)
    elif op == "and":
        for arg in expr.get("args", []): yield from _literals(arg, positive)
