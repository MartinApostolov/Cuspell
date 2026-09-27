from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class FlatSurfaceStandardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def meaning(self, source: str) -> str:
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result.ast.children[0].canonical()

    def test_kind_reference_tight_binding(self):
        self.assertEqual(
            self.meaning("CatSelf."),
            self.meaning("Cat Self."),
        )

    def test_property_reference_tight_binding(self):
        self.assertEqual(
            self.meaning("LifeThis."),
            self.meaning("Life This."),
        )

    def test_attribute_reference_tight_binding(self):
        tight = self.parser.parse_phrase("DensityThis", expected_type="Quantity:Density")
        spaced = self.parser.parse_phrase("Density This", expected_type="Quantity:Density")
        self.assertEqual(tight.canonical(), spaced.canonical())

    def test_user_comparison_example_is_valid_flat_prose(self):
        result = self.parser.check("More Evaluate CatSelf Evaluate HumanSelf.")
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("More(", meaning)
        self.assertIn("InstanceOf(Self,Cat)", meaning)
        self.assertIn("InstanceOf(Self,Human)", meaning)

    def test_registered_lexical_compound_still_wins(self):
        self.assertEqual(
            self.meaning("SolidWater This."),
            "InstanceOf(This,RestrictKind(base=Water,property=Solid))",
        )

    def test_tight_binding_can_chain_local_expression(self):
        self.assertEqual(
            self.meaning("NotLifeThis."),
            self.meaning("Not Life This."),
        )

    def test_whitespace_still_separates_larger_phrase_units(self):
        self.assertEqual(
            self.meaning("More Evaluate CatSelf Evaluate HumanSelf."),
            self.meaning("More Evaluate (Cat Self) Evaluate (Human Self)."),
        )


if __name__ == "__main__":
    unittest.main()
