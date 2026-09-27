from __future__ import annotations

from typing import Any, Iterable

from .model import Diagnostic, Node


def validate_semantics(node: Node) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for current in walk(node):
        expr = current.meta_dict().get("property_expr")
        if isinstance(expr, dict):
            conflict = property_conflict(expr)
            if conflict is not None:
                diagnostics.append(Diagnostic("ContradictoryConstraint", conflict))
    unique: dict[tuple[str, str], Diagnostic] = {}
    for diag in diagnostics:
        unique[(diag.code, diag.message)] = diag
    return list(unique.values())



def validate_execution_closure(node: Node) -> list[Diagnostic]:
    """Check command-only closure requirements after language semantics are valid."""
    diagnostics: list[Diagnostic] = []
    for current in walk(node):
        if current.type != "EventSpec":
            continue
        meta = current.meta_dict()
        groups = meta.get("execution_requires_any") or ()
        bound = set(meta.get("bound_roles") or ())
        for group in groups:
            options = tuple(group)
            if options and not any(role in bound for role in options):
                diagnostics.append(Diagnostic(
                    "SemanticallyIncomplete",
                    f"{current.name or current.kind} requires at least one of: {', '.join(options)}.",
                ))
    unique: dict[tuple[str, str], Diagnostic] = {}
    for diag in diagnostics:
        unique[(diag.code, diag.message)] = diag
    return list(unique.values())

def walk(node: Node) -> Iterable[Node]:
    yield node
    for child in node.children:
        yield from walk(child)


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
