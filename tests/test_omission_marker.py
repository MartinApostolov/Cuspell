from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser


ROOT = Path(__file__).resolve().parents[1]


class OmissionMarkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_repeated_omission_reaches_later_optional_slot(self):
        result = self.parser.check("Move This _ _ ThisPath!")
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("theme=This", meaning)
        self.assertIn("path=ThisPath", meaning)
        self.assertNotIn("goal=", meaning)
        self.assertNotIn("source=", meaning)

    def test_omission_skips_transfer_amount_before_profile(self):
        result = self.parser.check(
            "Transfer DistributionOf This Self ThisRegion ThisRegion "
            "_ DistributionOf You Self!"
        )
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("profile=", meaning)
        self.assertNotIn("amount=", meaning)

    def test_omission_closes_broad_optional_tail_for_outer_argument(self):
        flat = self.parser.check(
            "Say Self Obligated Self MoveSelfHere _ You!"
        )
        grouped = self.parser.check(
            "Say Self (Obligated Self MoveSelfHere) You!"
        )
        self.assertTrue(flat.valid, flat.diagnostics)
        self.assertTrue(grouped.valid, grouped.diagnostics)
        self.assertEqual(
            flat.ast.children[0].canonical(),
            grouped.ast.children[0].canonical(),
        )

    def test_required_slot_cannot_be_omitted(self):
        result = self.parser.check("Move _ Here!")
        self.assertFalse(result.valid)
        self.assertTrue(
            any(d.code == "InvalidOmission" for d in result.diagnostics),
            result.diagnostics,
        )

    def test_omission_marker_is_not_a_free_expression(self):
        result = self.parser.check("_.")
        self.assertFalse(result.valid)
        self.assertTrue(
            any(d.code == "InvalidOmission" for d in result.diagnostics),
            result.diagnostics,
        )

    def test_named_role_marker_is_rejected(self):
        result = self.parser.check("Move This :path ThisPath!")
        self.assertFalse(result.valid)
        self.assertTrue(
            any(d.code == "InvalidRole" for d in result.diagnostics),
            result.diagnostics,
        )

    def test_omission_marker_costs_no_mana(self):
        self.assertEqual(self.parser.mana_cost("Move This _ _ ThisPath!"), 3)

    def test_active_lexicon_contains_no_named_only_slots(self):
        for entry in self.language.entries:
            for frame in entry.frames:
                for slot in frame.get("slots", []):
                    self.assertNotIn(
                        "named_only",
                        slot,
                        f"{entry.surface}/{frame.get('id')}/{slot.get('name')}",
                    )


if __name__ == "__main__":
    unittest.main()
