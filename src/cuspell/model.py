from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Node:
    kind: str
    type: str
    name: str | None = None
    value: Any = None
    children: tuple["Node", ...] = ()
    roles: tuple[str, ...] = ()
    meta: tuple[tuple[str, Any], ...] = ()
    source_start: int | None = None
    source_end: int | None = None

    def meta_dict(self) -> dict[str, Any]:
        return dict(self.meta)

    def canonical(self) -> str:
        if self.kind == "Number":
            return str(self.value)
        if self.kind in {"Reference", "Descriptor", "Root", "Variable", "EventBoundaryRef"}:
            return self.name or "?"
        if self.kind == "Binder":
            return f"{self.name}:{self.value}"
        if self.kind == "Collection":
            return "[" + ",".join(child.canonical() for child in self.children) + "]"
        if self.name == "InstanceOf" and len(self.children) == 2:
            return f"InstanceOf({self.children[0].canonical()},{self.children[1].canonical()})"
        if self.name:
            if self.roles and len(self.roles) == len(self.children) and any(self.roles):
                body = ",".join(
                    f"{role}={child.canonical()}" if role else child.canonical()
                    for role, child in zip(self.roles, self.children)
                )
            else:
                body = ",".join(child.canonical() for child in self.children)
            return f"{self.name}({body})"
        return self.kind

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {"kind": self.kind, "type": self.type}
        if self.name is not None:
            out["name"] = self.name
        if self.value is not None:
            out["value"] = self.value
        if self.children:
            out["children"] = [child.to_dict() for child in self.children]
        if self.roles:
            out["roles"] = list(self.roles)
        if self.meta:
            out["meta"] = dict(self.meta)
        if self.source_start is not None and self.source_end is not None:
            out["source_span"] = {"start": self.source_start, "end": self.source_end}
        return out


@dataclass
class Diagnostic:
    code: str
    message: str
    field_index: int | None = None
    field: str | None = None
    expected: str | None = None
    actual: str | None = None
    source_start: int | None = None
    source_end: int | None = None
    # Internal parse-progress marker used to rank competing backtracking failures.
    # This is intentionally not serialized: field_index remains the user-facing location.
    progress_index: int | None = None

    def to_dict(self) -> dict[str, Any]:
        data = {"code": self.code, "message": self.message}
        if self.field_index is not None:
            data["field_index"] = self.field_index
        if self.field is not None:
            data["field"] = self.field
        if self.expected is not None:
            data["expected"] = self.expected
        if self.actual is not None:
            data["actual"] = self.actual
        if self.source_start is not None and self.source_end is not None:
            data["source_span"] = {"start": self.source_start, "end": self.source_end}
        return data


@dataclass
class CheckResult:
    valid: bool
    source: str
    mood: str
    phrases: list[str]
    ast: Node | None = None
    diagnostics: list[Diagnostic] = field(default_factory=list)
    mana: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "source": self.source,
            "mood": self.mood,
            "phrases": self.phrases,
            "mana": self.mana,
            "ast": self.ast.to_dict() if self.ast else None,
            "diagnostics": [d.to_dict() for d in self.diagnostics],
        }
