"""Guard current Language v1 release references against authoritative registry drift.

The language is not frozen by these tests: all checks read the current registered
data rather than treating historical checkpoint counts as a second truth.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class LanguageV1ConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lexicon = load_json("language/core/lexicon.json")["entries"]
        cls.roles = load_json("language/core/inventory_roles.json")
        cls.glyphs = load_json("language/core/glyph_assignments.json")
        cls.old_names = load_json("language/names/old_names.json")["entries"]
        cls.syntax = load_json("language/syntax/surface_v0_8.json")
        cls.by_surface = {e["surface"]: e for e in cls.lexicon}
        cls.by_old_id = {e["id"]: e for e in cls.old_names}
        cls.role_counts = Counter(e["inventory_role"] for e in cls.roles["entries"])

    def test_registry_roles_and_glyphs_form_one_consistent_inventory(self):
        self.assertEqual(len(self.by_surface), len(self.lexicon))
        self.assertEqual(len(self.roles["entries"]), len(self.lexicon))
        self.assertEqual(self.role_counts, Counter(self.roles["counts"]))
        self.assertEqual(
            {e["id"] for e in self.roles["entries"]},
            {e["id"] for e in self.lexicon},
        )
        self.assertTrue(all(e["rune_cost"] == 1 for e in self.lexicon))
        self.assertEqual(self.glyphs["status"], "USER_APPROVED_CANONICAL_218_GLYPH_MAPPING")
        assigned = self.glyphs["assignments"]
        spares = self.glyphs["spares"]
        self.assertEqual(
            {x["surface"] for x in assigned},
            set(self.by_surface) | {"@"},
        )
        self.assertEqual(len({x["surface"] for x in assigned}), len(assigned))
        self.assertEqual(len({x["temporary_character"] for x in assigned}), len(assigned))
        self.assertEqual(len({x["glyph_id"] for x in assigned + spares}), len(assigned) + len(spares))
        self.assertEqual(len(assigned) + len(spares), 234)
        self.assertEqual(len(spares), 16)

    def test_current_inventory_and_frame_counts_are_documented_correctly(self):
        n = len(self.lexicon)
        frames = sum(len(e.get("frames", [])) for e in self.lexicon)
        multiframes = sum(len(e.get("frames", [])) > 1 for e in self.lexicon)
        self.assertEqual(n, 217)
        self.assertEqual(frames, 276)
        self.assertEqual(multiframes, 53)
        texts = {
            p: read(p) for p in (
                "docs/CURRENT_STATE.md",
                "docs/CUSPELL_DICTIONARY.md",
                "docs/spec/LEXICON.md",
            )
        }
        for path, body in texts.items():
            with self.subTest(path=path):
                self.assertIn(f"**{n} entries**", body)
                for role, phrase in (
                    ("semantic_primitive_candidate", "semantic primitive candidates"),
                    ("formal_constructor", "formal constructors"),
                    ("reference_form", "reference forms"),
                    ("domain_value", "domain values"),
                ):
                    self.assertIn(
                        f"**{self.role_counts[role]} {phrase}**", body,
                        f"Inventory drift in {path}: {phrase}",
                    )
        lexicon_spec = texts["docs/spec/LEXICON.md"]
        self.assertIn(f"**{frames} semantic frames**", lexicon_spec)
        self.assertIn(f"**{multiframes} multi-frame entries**", lexicon_spec)
        self.assertNotIn("**212 entries**", lexicon_spec)

    def test_old_name_costs_match_player_reference(self):
        root_costs = {e["surface"]: e["rune_cost"] for e in self.lexicon}

        @lru_cache(maxsize=None)
        def name_cost(old_id: str) -> int:
            entry = self.by_old_id[old_id]
            return sum(
                root_costs[unit["root"]]
                if "root" in unit else name_cost(unit["old_name"])
                for unit in entry["name_units"]
            )

        table = {}
        for line in read("player/names/OLD_NAMES.md").splitlines():
            match = re.search(r"`«(.+)»`\s*\|\s*(\d+)\s*\|", line)
            if match:
                self.assertNotIn(match.group(1), table)
                table[match.group(1)] = int(match.group(2))
        self.assertEqual(len(table), len(self.old_names))
        self.assertEqual(set(table), {e["sign"] for e in self.old_names})
        for entry in self.old_names:
            with self.subTest(old_name=entry["id"]):
                self.assertEqual(table[entry["sign"]], name_cost(entry["id"]))

    def test_surface_and_player_guidance_do_not_reopen_completed_decisions(self):
        self.assertEqual(self.syntax["version"], "0.8")
        self.assertEqual(
            self.syntax["separators"]["sentence_terminators"],
            {".": "assertion", "?": "question", "!": "command"},
        )
        pipe = self.syntax["debug_compatibility"]["pipe_binding"]
        self.assertTrue(pipe["debug_only"])
        self.assertFalse(pipe["player_facing"])
        self.assertEqual(self.syntax["optional_arguments"]["omission_marker"], "_")
        self.assertEqual(self.syntax["sequence_surface"]["explicit_end"], "SequenceEnd")
        self.assertEqual(self.syntax["concurrent_surface"]["explicit_end"], "ConcurrentEnd")
        for path in ("docs/spec/SURFACE_SYNTAX.md", "player/RULES.md"):
            with self.subTest(path=path):
                content = read(path)
                self.assertIn("SequenceEnd", content)
                self.assertIn("ConcurrentEnd", content)
        grammar = read("docs/spec/SENTENCE_GRAMMAR.md")
        self.assertNotIn("decide whether pipe stays player-facing", grammar)
        self.assertNotIn("audit the 51 multi-frame roots", grammar)
        self.assertNotIn("reconcile all remaining specs/examples with v0.8", grammar)
        rune_guide = read("player/RUNES.md")
        self.assertNotIn("separate planned typing-page feature", rune_guide)
        self.assertIn("meaning_keyboard.html", rune_guide)

    def test_release_checklist_keeps_manual_requirements_explicit(self):
        checks = read("docs/LANGUAGE_V1_VALIDATION.md")
        self.assertIn("- [x] Run script/parser round-trip checks", checks)
        self.assertIn("- [x] Reconcile normative", checks)
        self.assertRegex(checks, r"- \[ \] On a real PC")
        self.assertRegex(checks, r"- \[ \] Test copy")
        self.assertRegex(checks, r"- \[ \] Freeze and tag")
        self.assertIn("not", checks.lower())


if __name__ == "__main__":
    unittest.main()
