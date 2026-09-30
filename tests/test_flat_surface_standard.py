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
            self.meaning("MatterSelf."),
            self.meaning("Matter Self."),
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
        result = self.parser.check("More Evaluate MatterSelf Evaluate ThingSelf.")
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("More(", meaning)
        self.assertIn("InstanceOf(Self,Matter)", meaning)
        self.assertIn("InstanceOf(Self,Thing)", meaning)

    def test_registered_lexical_compound_still_wins(self):
        self.assertEqual(
            self.meaning("SolidMatter This."),
            "InstanceOf(This,RestrictKind(base=Matter,property=Solid))",
        )

    def test_tight_binding_can_chain_local_expression(self):
        self.assertEqual(
            self.meaning("NotLifeThis."),
            self.meaning("Not Life This."),
        )


    def test_multi_root_lexical_compound_can_stay_one_word(self):
        result = self.parser.check("SolidMagicMatter This.")
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("RestrictKind", meaning)
        self.assertIn("Solid", meaning)
        self.assertIn("Magic", meaning)

    def test_large_tight_expression_can_be_one_written_unit(self):
        result = self.parser.check("MoreDensityThisDensityThat.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "More(left=Density(subject=This),right=Density(subject=That))",
        )

    def test_whitespace_still_separates_larger_phrase_units(self):
        self.assertEqual(
            self.meaning("More Evaluate MatterSelf Evaluate ThingSelf."),
            self.meaning("More Evaluate (Matter Self) Evaluate (Thing Self)."),
        )


if __name__ == "__main__":
    unittest.main()
