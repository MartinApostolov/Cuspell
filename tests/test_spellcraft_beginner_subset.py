from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MANIFEST = ROOT / "language" / "subsets" / "spellcraft_beginner_v0_1.json"
BEGINNER_MANIFEST = ROOT / "language" / "subsets" / "spellcraft_beginner_v0_2.json"


class SpellcraftCoverageProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.data = json.loads(COVERAGE_MANIFEST.read_text(encoding="utf-8"))

    def test_projection_is_50_signs_and_cumulative(self):
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
        self.assertEqual(len(flattened), 50)
        self.assertLess(len(flattened), len(self.language.entries) // 4)

    def test_all_projection_entries_are_current_registered_signs(self):
        missing = [
            surface
            for surface in self.data["entries"]
            if self.language.entry(surface) is None
        ]
        self.assertEqual(missing, [])

    def test_projection_old_names_exist(self):
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

    def test_coverage_examples_do_not_require_parentheses(self):
        failures = [
            (example["spell"], example["cuspell"])
            for example in self.data["reference_effects"]
            if "(" in example["cuspell"] or ")" in example["cuspell"]
        ]
        self.assertEqual(failures, [])

    def test_all_coverage_examples_parse_as_commands(self):
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
        self.assertIn("Create", by_name["Light"])
        self.assertNotEqual(by_name["Light"], by_name["Faerie Fire"])
        self.assertIn("Each Collect", by_name["Faerie Fire"])
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


class SpellcraftBeginnerCoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.data = json.loads(BEGINNER_MANIFEST.read_text(encoding="utf-8"))

    def test_beginner_core_is_16_signs_with_small_cumulative_steps(self):
        tiers = self.data["tiers"]
        flattened = []
        counts = []
        for tier in (
            "first_actions",
            "target_and_condition",
            "discovery",
            "creation_and_light",
        ):
            flattened.extend(tiers[tier]["entries"])
            counts.append(tiers[tier]["cumulative_count"])
        self.assertEqual(flattened, self.data["entries"])
        self.assertEqual(len(flattened), len(set(flattened)))
        self.assertEqual(len(flattened), 16)
        self.assertEqual(counts, [6, 9, 11, 16])

    def test_all_beginner_entries_are_current_registered_signs(self):
        missing = [
            surface
            for surface in self.data["entries"]
            if self.language.entry(surface) is None
        ]
        self.assertEqual(missing, [])

    def test_beginner_core_uses_only_one_old_name(self):
        self.assertEqual(self.data["starter_old_names"], ["LightUnit"])
        self.assertTrue(self.language.old_name_entries("LightUnit"))

    def test_all_beginner_spells_parse_as_commands(self):
        for example in self.data["starter_spells"]:
            source = example["cuspell"]
            with self.subTest(name=example["name"], source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_beginner_spells_stay_flat_and_parenthesis_free(self):
        bad = [
            example["cuspell"]
            for example in self.data["starter_spells"]
            if "(" in example["cuspell"] or ")" in example["cuspell"]
        ]
        self.assertEqual(bad, [])

    def test_first_set_defers_programming_and_advanced_control_signs(self):
        deferred = {
            "And", "Repeat", "Concurrent", "Each", "Collect", "Member",
            "Trigger", "Persist", "Prevent", "Represent", "TimeFlow",
        }
        self.assertTrue(deferred.isdisjoint(self.data["entries"]))

    def test_find_is_taught_only_as_simple_yes_no_discovery(self):
        find_examples = [
            example["cuspell"]
            for example in self.data["starter_spells"]
            if example["cuspell"].startswith("Find ")
        ]
        self.assertEqual(
            find_examples,
            [
                "Find Self This Locked This!",
                "Find Self You Ill You!",
            ],
        )
        self.assertTrue(all(":Location" not in source for source in find_examples))

    def test_light_spell_is_fresh_creation_not_existing_target_mutation(self):
        by_name = {
            example["name"]: example["cuspell"]
            for example in self.data["starter_spells"]
        }
        created = by_name["Create light here"]
        luminous = by_name["Make an existing thing luminous"]
        self.assertTrue(created.startswith("Create "))
        self.assertIn("Change $x Light", created)
        self.assertEqual(luminous, "Change This Light «LightUnit» @!")
        self.assertNotEqual(created, luminous)

    def test_create_is_the_only_beginner_example_that_needs_a_binder(self):
        binder_examples = [
            example["cuspell"]
            for example in self.data["starter_spells"]
            if ":Entity" in example["cuspell"]
        ]
        self.assertEqual(
            binder_examples,
            [
                "Create x:Entity At $x Here Change $x Light «LightUnit» @!",
                "Create x:Entity At $x There Change $x Light «LightUnit» @!",
            ],
        )


if __name__ == "__main__":
    unittest.main()
