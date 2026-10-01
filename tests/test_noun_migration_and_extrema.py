from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class NounMigrationAndExtremaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_language_data_validates(self):
        self.assertEqual(validate_language_data(ROOT), [])

    def test_direct_noun_roots_are_removed(self):
        for surface in ("Cat", "Hand", "Human", "Water", "Body", "Sound"):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))

    def test_migrated_nouns_resolve_as_old_names(self):
        cases = {
            "Know«MoveLifeThing»": "core.biology.human",
            "LowExtent«MoveLifeThing»": "core.biology.cat",
            "LiquidMatter": "core.materials.water",
            "LifeMatter": "core.anatomy.body",
            "Grab«LifeMatter»Part": "core.anatomy.hand",
            "HearingThing": "core.physics.sound",
        }
        for sign, concept_id in cases.items():
            with self.subTest(sign=sign):
                result = self.parser.check(f"«{sign}» This.")
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(f"Concept({concept_id})", result.ast.children[0].canonical())

    def test_specialized_extrema_roots_are_removed(self):
        for surface in ("Nearest", "Farthest", "Highest", "Lowest"):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))
        self.assertIsNotNone(self.language.entry("MinBy"))
        self.assertIsNotNone(self.language.entry("MaxBy"))

    def test_minmax_by_distance_replace_nearest_and_farthest(self):
        nearest = self.parser.parse_phrase(
            "MinBy {This,You} x:Entity Distance $x Here",
            expected_type="Collection:Entity",
        )
        farthest = self.parser.parse_phrase(
            "MaxBy {This,You} x:Entity Distance $x Here",
            expected_type="Collection:Entity",
        )
        self.assertNotIsInstance(nearest, Diagnostic, nearest)
        self.assertNotIsInstance(farthest, Diagnostic, farthest)
        self.assertIn("MinBy", nearest.canonical())
        self.assertIn("Distance", nearest.canonical())
        self.assertIn("MaxBy", farthest.canonical())

    def test_minmax_by_attribute_replace_highest_and_lowest(self):
        lowest = self.parser.parse_phrase(
            "MinBy {This,You} x:Entity Mass $x",
            expected_type="Collection:Entity",
        )
        highest = self.parser.parse_phrase(
            "MaxBy {This,You} x:Entity Mass $x",
            expected_type="Collection:Entity",
        )
        self.assertNotIsInstance(lowest, Diagnostic, lowest)
        self.assertNotIsInstance(highest, Diagnostic, highest)
        self.assertIn("Mass", lowest.canonical())
        self.assertIn("Mass", highest.canonical())


if __name__ == "__main__":
    unittest.main()
