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
            "fresh_creation",
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
        self.assertEqual(len(self.data["reference_effects"]), 48)

    def test_reference_effect_spell_names_are_unique(self):
        names = [example["spell"] for example in self.data["reference_effects"]]
        self.assertEqual(len(names), len(set(names)))

    def test_beginner_spell_examples_do_not_require_parentheses(self):
        failures = [
            (example["spell"], example["cuspell"])
            for example in self.data["reference_effects"]
            if "(" in example["cuspell"] or ")" in example["cuspell"]
        ]
        self.assertEqual(failures, [])

    def test_all_reference_effect_examples_parse_as_commands(self):
        for example in self.data["reference_effects"]:
            source = example["cuspell"]
            with self.subTest(spell=example["spell"], source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_post_create_repairs_keep_distinct_spell_meanings_distinct(self):
        by_name = {
            example["spell"]: example["cuspell"]
            for example in self.data["reference_effects"]
        }
        self.assertNotEqual(by_name["Light"], by_name["Faerie Fire"])
        self.assertIn("Each They", by_name["Faerie Fire"])
        self.assertIn("Create", by_name["Magic Missile"])
        self.assertIn("Create", by_name["Find Familiar"])

    def test_remaining_exact_duplicate_recipes_are_explicitly_intentional(self):
        recipes: dict[str, set[str]] = {}
        for example in self.data["reference_effects"]:
            recipes.setdefault(example["cuspell"], set()).add(example["spell"])
        duplicates = {
            recipe: names
            for recipe, names in recipes.items()
            if len(names) > 1
        }
        expected = {
            "Change This Heat Add BeforeValue Heat This «HeatUnit» @!": {
                "Fire Bolt",
                "Prestidigitation",
                "Heat Metal",
            },
            "Move This There!": {
                "Mage Hand",
                "Thunderwave",
                "Gust of Wind",
            },
            "Change You Health Health Self!": {
                "Cure Wounds",
                "Healing Word",
            },
            "Change Self Form Form This!": {
                "Disguise Self",
                "Alter Self",
                "Enlarge/Reduce",
            },
            "Begin CanYouMoveYouThere!": {
                "Longstrider",
                "Enhance Ability",
            },
            "Prevent SenseThisVisionYou ThisInterval!": {
                "Invisibility",
                "Pass without Trace",
            },
        }
        self.assertEqual(duplicates, expected)


if __name__ == "__main__":
    unittest.main()
