from __future__ import annotations

from .model import Node


def tree(node: Node, prefix: str = "", is_last: bool = True) -> str:
    label = node.name or node.kind
    if node.kind == "Number":
        label = str(node.value)
    elif node.kind == "Binder":
        label = f"[{node.name}:{node.value}]"
    label += f" : {node.type}"
    lines = [prefix + ("└─ " if prefix else "") + label]
    child_prefix = prefix + ("   " if is_last else "│  ")
    for i, child in enumerate(node.children):
        last = i == len(node.children) - 1
        child_label = child.name or child.kind
        if child.kind == "Number":
            child_label = str(child.value)
        elif child.kind == "Binder":
            child_label = f"[{child.name}:{child.value}]"
        child_label += f" : {child.type}"
        connector = "└─ " if last else "├─ "
        lines.append(child_prefix + connector + child_label)
        if child.children:
            lines.extend(_child_lines(child, child_prefix + ("   " if last else "│  ")))
    return "\n".join(lines)


def _child_lines(node: Node, prefix: str) -> list[str]:
    lines: list[str] = []
    for i, child in enumerate(node.children):
        last = i == len(node.children) - 1
        label = child.name or child.kind
        if child.kind == "Number":
            label = str(child.value)
        elif child.kind == "Binder":
            label = f"[{child.name}:{child.value}]"
        label += f" : {child.type}"
        lines.append(prefix + ("└─ " if last else "├─ ") + label)
        if child.children:
            lines.extend(_child_lines(child, prefix + ("   " if last else "│  ")))
    return lines
