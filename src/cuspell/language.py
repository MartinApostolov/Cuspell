from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Entry:
    data: dict[str, Any]

    @property
    def surface(self) -> str:
        return self.data["surface"]

    @property
    def rune_cost(self) -> int:
        return int(self.data.get("rune_cost", 1))

    @property
    def atom_type(self) -> str | None:
        return self.data.get("atom_type")

    @property
    def frames(self) -> list[dict[str, Any]]:
        return list(self.data.get("frames", []))


class Language:
    def __init__(self, root: Path, types: dict[str, Any], lexicon: dict[str, Any]):
        self.root = root
        self.parents: dict[str, str | None] = types["parents"]
        self.entries = {item["surface"]: Entry(item) for item in lexicon["entries"]}

    @classmethod
    def load(cls, root: str | Path | None = None) -> "Language":
        root_path = cls._find_root(root)
        types_path = root_path / "language" / "core" / "types.json"
        lexicon_path = root_path / "language" / "core" / "lexicon_minimal.json"
        with types_path.open("r", encoding="utf-8") as f:
            types = json.load(f)
        with lexicon_path.open("r", encoding="utf-8") as f:
            lexicon = json.load(f)
        return cls(root_path, types, lexicon)

    @staticmethod
    def _find_root(explicit: str | Path | None) -> Path:
        candidates: list[Path] = []
        if explicit is not None:
            candidates.append(Path(explicit).resolve())
        env = os.getenv("CUSPELL_ROOT")
        if env:
            candidates.append(Path(env).resolve())
        cwd = Path.cwd().resolve()
        candidates.extend([cwd, *cwd.parents])
        package_here = Path(__file__).resolve()
        candidates.extend(package_here.parents)
        seen: set[Path] = set()
        for candidate in candidates:
            if candidate in seen:
                continue
            seen.add(candidate)
            if (candidate / "language" / "core" / "lexicon_minimal.json").exists():
                return candidate
        raise FileNotFoundError(
            "Could not locate Cuspell language data. Run from the repository root "
            "or set CUSPELL_ROOT."
        )

    def entry(self, surface: str) -> Entry | None:
        return self.entries.get(surface)

    def is_assignable(self, actual: str, expected: str) -> bool:
        if expected in {"Any", "SemanticValue"}:
            return True
        if actual == expected:
            return True
        current = actual
        visited: set[str] = set()
        while current and current not in visited:
            visited.add(current)
            current = self.parents.get(current)
            if current == expected:
                return True
        return False
