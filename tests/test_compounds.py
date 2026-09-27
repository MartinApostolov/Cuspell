from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CompoundParserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str, meaning: str, mana: int):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIsNotNone(result.ast)
        self.assertEqual(result.ast.children[0].canonical(), meaning)
        self.assertEqual(result.mana, mana)

    def test_property_restricts_kind(self):
        self.assert_valid("SolidWater|This.", "InstanceOf(This,RestrictKind(base=Water,property=Solid))", 3)

    def test_exclusive_family_contradiction_on_kind(self):
        result = self.parser.check("SolidLiquidMatter|This.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "ContradictoryConstraint")
        self.assertIn("Phase", result.diagnostics[0].message)
        self.assertEqual(result.mana, 4)

    def test_exclusive_family_contradiction_on_property(self):
        result = self.parser.check("SolidLiquid|This.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "ContradictoryConstraint")

    def test_not_property_compound(self):
        self.assert_valid("NotLife|This.", "Not(proposition=Life(subject=This))", 3)

    def test_property_and_its_negation_contradict(self):
        result = self.parser.check("LifeNotLife|This.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "ContradictoryConstraint")

    def test_double_not_normalizes_without_refunding_mana(self):
        self.assert_valid("NotNotLife|This.", "Life(subject=This)", 4)

    def test_end_state_compound(self):
        self.assert_valid("!EndLife|This.", "End(state=Life(subject=This))", 3)

    def test_opposite_uses_declared_reversible_relation(self):
        self.assert_valid("OppositeBefore|ThisEvent|ThatEvent.", "After(later=ThisEvent,earlier=ThatEvent)", 4)

    def test_converse_uses_declared_role_reversal_relation(self):
        self.assert_valid("ConverseIn|ThisRegion|This.", "Contain(region=ThisRegion,item=This)", 4)

    def test_unlicensed_compound_is_not_unknown_root(self):
        result = self.parser.check("OppositeMatter|This.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "IllegalCompound")
        self.assertIn("Opposite + Matter", result.diagnostics[0].message)
        self.assertEqual(result.mana, 3)

    def test_compound_kind_can_be_binder_domain(self):
        self.assert_valid("All|[a:SolidWater]|Life|$a.", "All(binder=a:SolidWater,predicate=Life(subject=$a))", 4)

    def test_relation_root_still_works_beside_operator_compound(self):
        self.assert_valid("Before|ThisEvent|ThatEvent.", "Before(earlier=ThisEvent,later=ThatEvent)", 3)


if __name__ == "__main__":
    unittest.main()
