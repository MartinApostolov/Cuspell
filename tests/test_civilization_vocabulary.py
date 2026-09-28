from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CivilizationVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_productive_foundational_roots_are_registered(self):
        for surface in (
            "Big",
            "Small",
            "Hard",
            "Sharp",
            "Grow",
            "Sleep",
            "Sign",
            "Information",
            "Rule",
            "Region",
            "Path",
            "Write",
            "Read",
        ):
            with self.subTest(surface=surface):
                self.assertIsNotNone(self.language.entry(surface))

    def test_common_object_words_are_old_names_not_direct_roots(self):
        for surface in (
            "Plant",
            "Animal",
            "Tree",
            "Tool",
            "Weapon",
            "Sword",
            "Container",
            "House",
            "Door",
            "Boat",
            "Ship",
            "Food",
            "Medicine",
            "Poison",
            "Market",
            "School",
            "Record",
            "Book",
            "Map",
            "Calendar",
            "Clock",
        ):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))

    def test_first_vocabulary_batch_is_substantial(self):
        self.assertGreaterEqual(len(self.language.world_concepts), 60)
        self.assertGreaterEqual(
            sum(len(v) for v in self.language.old_names_by_sign.values()),
            60,
        )

    def test_plant_old_name_resolves_as_world_kind(self):
        result = self.parser.check("«GrowLifeMatter» This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "InstanceOf(This,Concept(core.biology.plant))",
        )
        # Grow + Life + Matter + This
        self.assertEqual(result.mana, 4)

    def test_tree_reuses_earlier_plant_name(self):
        result = self.parser.check("«BigHard«GrowLifeMatter»» This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "InstanceOf(This,Concept(core.biology.tree))",
        )
        self.assertEqual(self.language.old_name_cost("GrowLifeMatter"), 3)
        self.assertEqual(
            self.language.old_name_cost("BigHard«GrowLifeMatter»"),
            5,
        )

    def test_ship_reuses_boat_name_with_recursive_cost(self):
        result = self.parser.check("«Big«MoveInLiquidThing»» This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "InstanceOf(This,Concept(core.transport.ship))",
        )
        self.assertEqual(self.language.old_name_cost("MoveInLiquidThing"), 4)
        self.assertEqual(
            self.language.old_name_cost("Big«MoveInLiquidThing»"),
            5,
        )
        # Ship Old Name 5 + This 1.
        self.assertEqual(result.mana, 6)

    def test_tool_family_builds_historically(self):
        self.assertEqual(self.language.old_name_cost("UseThing"), 2)
        self.assertEqual(self.language.old_name_cost("SeparateMatter«UseThing»"), 4)
        self.assertEqual(
            self.language.old_name_cost("Sharp«SeparateMatter«UseThing»»"),
            5,
        )
        self.assertEqual(
            self.language.old_name_cost(
                "MoreLength«Sharp«SeparateMatter«UseThing»»»"
            ),
            7,
        )

    def test_information_vocabulary_builds_from_record(self):
        self.assertEqual(self.language.old_name_cost("MeaningSign"), 2)
        self.assertEqual(self.language.old_name_cost("PersistSignThing"), 3)
        self.assertEqual(
            self.language.old_name_cost("Group«PersistSignThing»"),
            4,
        )
        self.assertEqual(
            self.language.old_name_cost("Region«PersistSignThing»"),
            4,
        )

    def test_old_name_exact_spelling_is_not_english_gloss(self):
        # English glosses are metadata for us. The actual Cuspell Old Names
        # remain the descriptive exact Signs.
        self.assertFalse(self.language.old_name_entries("Ship"))
        self.assertTrue(self.language.old_name_entries("Big«MoveInLiquidThing»"))
        self.assertFalse(self.language.old_name_entries("Sword"))
        self.assertTrue(
            self.language.old_name_entries(
                "MoreLength«Sharp«SeparateMatter«UseThing»»»"
            )
        )


if __name__ == "__main__":
    unittest.main()
