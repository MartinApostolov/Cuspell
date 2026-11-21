"""Orthographic Cuspell glyph-to-transliteration codec, not a spell parser."""
from __future__ import annotations
from functools import lru_cache
import json
from pathlib import Path
import re

_WORD = re.compile(r"[A-Za-z]+|@")

class GlyphCodec:
    def __init__(self, assignments: list[dict]):
        if len(assignments) != 218:
            raise ValueError("Expected 217 runes plus numeric-one @")
        self.forward: dict[str, str] = {}
        self.reverse: dict[str, str] = {}
        for item in assignments:
            name = item["surface"]
            glyph = item["temporary_character"]
            if len(glyph) != 1 or ord(glyph) != int(item["temporary_codepoint"][2:], 16):
                raise ValueError(f"Incorrect codepoint for {name}")
            if name in self.forward or glyph in self.reverse:
                raise ValueError("Non-unique name/glyph assignment")
            self.forward[name] = glyph
            self.reverse[glyph] = name
        if "@" not in self.forward:
            raise ValueError("Missing numeric-one glyph")
        self.roots = tuple(sorted((s for s in self.forward if s != "@"),
                                  key=lambda s: (-len(s), s)))

    @classmethod
    def from_repository(cls, root: str | Path | None = None) -> GlyphCodec:
        repo = Path(root) if root is not None else Path(__file__).resolve().parents[2]
        data = json.loads((repo / "language/core/glyph_assignments.json").read_text(encoding="utf-8"))
        if data["status"] != "USER_APPROVED_CANONICAL_218_GLYPH_MAPPING":
            raise ValueError("Glyph assignments are not approved")
        return cls(data["assignments"])

    @lru_cache(maxsize=32768)
    def segment(self, word: str) -> tuple[str, ...] | None:
        """Exact roots win; otherwise allow exactly one all-root segmentation."""
        if word in self.forward:
            return (word,)

        @lru_cache(maxsize=None)
        def search(i: int) -> tuple[tuple[str, ...], ...]:
            if i == len(word):
                return ((),)
            result: list[tuple[str, ...]] = []
            for root in self.roots:
                if word.startswith(root, i):
                    for tail in search(i + len(root)):
                        result.append((root,) + tail)
                        if len(result) >= 2:
                            return tuple(result)
            return tuple(result)
        candidates = search(0)
        return candidates[0] if len(candidates) == 1 else None

    def encode(self, text: str) -> str:
        """Convert only registered roots and unique tight sequences; preserve other text."""
        def convert(match: re.Match[str]) -> str:
            token = match.group()
            if token == "@":
                return self.forward[token]
            roots = self.segment(token)
            return "".join(self.forward[r] for r in roots) if roots else token
        return _WORD.sub(convert, text)

    def decode(self, text: str) -> str:
        """Decode approved glyphs without altering unknown or spare glyph codepoints."""
        return "".join(self.reverse.get(c, c) for c in text)
