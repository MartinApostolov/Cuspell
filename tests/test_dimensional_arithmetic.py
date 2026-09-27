from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class DimensionalArithmeticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def parse_quantity(self, source: str):
        node = self.parser.parse_phrase(source, expected_type="Quantity")
        self.assertNotIsInstance(node, Diagnostic, node)
        return node

    def test_number_scaling_preserves_dimension(self):
        node = self.parse_quantity("Multiply @@ Density This")
        self.assertEqual(node.type, "Quantity:Density")
        self.assertEqual(
            node.canonical(),
            "Multiply(factor=2,value=Density(subject=This))",
        )

    def test_length_times_length_is_area(self):
        node = self.parse_quantity(
            "Multiply Distance This Self Distance This Self"
        )
        self.assertEqual(node.type, "Quantity:Area")

    def test_density_times_volume_is_mass(self):
        node = self.parse_quantity("Multiply Density This Volume This")
        self.assertEqual(node.type, "Quantity:Mass")

    def test_registered_dimension_aliases_are_assignable(self):
        self.assertTrue(
            self.language.is_assignable("Quantity:Area", "Quantity")
        )
        self.assertEqual(
            self.language.quantity_type_for_vector({"Length": 2}),
            "Quantity:Area",
        )

    def test_unregistered_product_gets_stable_derived_dimension(self):
        left = self.parse_quantity("Multiply Mass This Distance This Self")
        right = self.parse_quantity("Multiply Distance This Self Mass This")
        self.assertEqual(left.type, right.type)
        self.assertTrue(left.type.startswith("Quantity:Dim_"))
        self.assertTrue(self.language.is_assignable(left.type, "Quantity"))

    def test_add_still_requires_matching_dimensions(self):
        result = self.parser.parse_phrase(
            "Add Density This Volume This",
            expected_type="Quantity",
        )
        self.assertIsInstance(result, Diagnostic)
        self.assertEqual(result.code, "TypeMismatch")


if __name__ == "__main__":
    unittest.main()
