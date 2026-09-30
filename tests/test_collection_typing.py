from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CollectionTypingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def test_each_binder_must_range_over_collection_member_type(self):
        result = self.parser.check(
            "!Each Collect [a:«Know«MoveLifeThing»»] Life $a [b:Quantity:Number] Repeat $b Move This Here."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")
        self.assertIn("supplies Entity members", result.diagnostics[0].message)

    def test_filter_binder_must_range_over_collection_member_type(self):
        result = self.parser.check(
            "Same Unique Filter Collect [a:«Know«MoveLifeThing»»] Life $a [b:Quantity:Number] Equal $b Zero Self."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")
        self.assertIn("supplies Entity members", result.diagnostics[0].message)

    def test_random_explicitly_reduces_collection_to_one_member(self):
        result = self.parser.check("Same Random Collect [a:«Know«MoveLifeThing»»] Life $a Self.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_farthest_preserves_ties_until_unique(self):
        result = self.parser.check(
            "Same Unique MaxBy Collect [a:«Know«MoveLifeThing»»] Life $a [b:Entity] Distance $b Self Self."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_nearest_collection_cannot_fill_singular_entity_role(self):
        nearest = self.parser.parse_phrase(
            "MinBy Collect [a:«Know«MoveLifeThing»»] Life $a [b:Entity] Distance $b Self", expected_type="Collection"
        )
        self.assertEqual(nearest.type, "Collection:Entity")
        result = self.parser.check("Life MinBy Collect [a:«Know«MoveLifeThing»»] Life $a [b:Entity] Distance $b Self.")
        self.assertFalse(result.valid)
        diagnostic = result.diagnostics[0]
        self.assertEqual(diagnostic.code, "TypeMismatch")
        self.assertEqual(diagnostic.field, "MinBy")
        self.assertEqual(diagnostic.expected, "Entity")
        self.assertEqual(diagnostic.actual, "Collection:Entity")
        self.assertNotIn("progress_index", diagnostic.to_dict())


if __name__ == "__main__":
    unittest.main()
