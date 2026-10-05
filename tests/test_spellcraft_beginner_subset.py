from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "language" / "subsets" / "spellcraft_beginner_v0_1.json"


class SpellcraftBeginnerSubsetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_subset_is_small_and_cumulative(self):
        tiers = self.data["tiers"]
        flattened = []
        for tier in (
            "direct_manipulation",
            "persistent_and_protective",
            "transformation_and_programming",
        ):
            flattened.extend(tiers[tier]["entries"])
        self.assertEqual(flattened, self.data["entries"])
        self.assertEqual(len(flattened), len(set(flattened)))
        self.assertEqual(len(flattened), 49)
        self.assertLess(len(flattened), len(self.language.entries) // 4)

    def test_all_subset_entries_are_current_registered_signs(self):
        missing = [
            surface
            for surface in self.data["entries"]
            if self.language.entry(surface) is None
        ]
        self.assertEqual(missing, [])

    def test_starter_old_names_exist(self):
        for sign in self.data["starter_old_names"]:
            with self.subTest(sign=sign):
                self.assertTrue(self.language.old_name_entries(sign))

    def test_reference_effects_are_level_zero_through_two_only(self):
        levels = {example["level"] for example in self.data["reference_effects"]}
        self.assertEqual(levels, {0, 1, 2})
        self.assertGreaterEqual(len(self.data["reference_effects"]), 40)

    def test_reference_effect_spell_names_are_unique(self):
        names = [example["spell"] for example in self.data["reference_effects"]]
        self.assertEqual(len(names), len(set(names)))

    def test_all_reference_effect_examples_parse_as_commands(self):
        for example in self.data["reference_effects"]:
            source = example["cuspell"]
            with self.subTest(spell=example["spell"], source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)


if __name__ == "__main__":
    unittest.main()
