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
        self.assertEqual(result.code, "DimensionMismatch")

    def test_ordered_comparison_reports_dimension_mismatch(self):
        result = self.parser.check("More Density This Volume This.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "DimensionMismatch")
        self.assertEqual(result.diagnostics[0].expected, "Quantity:Density")
        self.assertEqual(result.diagnostics[0].actual, "Quantity:Volume")

    def test_volume_divided_by_length_is_area(self):
        node = self.parse_quantity("Divide Volume This Distance This Self")
        self.assertEqual(node.type, "Quantity:Area")

    def test_mass_divided_by_volume_is_density(self):
        node = self.parse_quantity("Divide Mass This Volume This")
        self.assertEqual(node.type, "Quantity:Density")

    def test_equal_dimensions_divide_to_number(self):
        node = self.parse_quantity(
            "Divide Distance This Self Distance Self This"
        )
        self.assertEqual(node.type, "Quantity:Number")

    def test_length_divided_by_time_gets_derived_rate_dimension(self):
        node = self.parse_quantity(
            "Divide Distance This Self Duration ThisEvent"
        )
        self.assertTrue(node.type.startswith("Quantity:Dim_"))
        self.assertEqual(
            self.language.quantity_dimension_vector(node.type),
            {"Length": 1, "Time": -1},
        )


if __name__ == "__main__":
    unittest.main()
