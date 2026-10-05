from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class PressureAttributeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_pressure_is_a_typed_attribute_on_entity_and_location(self):
        for source in ("Pressure This", "Pressure Here"):
            with self.subTest(source=source):
                node = self.parser.parse_phrase(
                    source,
                    expected_type="Quantity:Pressure",
                )
                self.assertNotIsInstance(node, Diagnostic, node)
                self.assertEqual(node.type, "Quantity:Pressure")

    def test_pressure_dimension_is_derived_from_mass_length_and_time(self):
        node = self.parser.parse_phrase(
            "Divide (Mass This) "
            "(Multiply (Distance This Self) (Power (Extent ThisInterval) @@))",
            expected_type="Quantity",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Quantity:Pressure")
        self.assertEqual(
            self.language.quantity_dimension_vector(node.type),
            {"Mass": 1, "Length": -1, "Time": -2},
        )

    def test_pressure_needs_no_new_canonical_unit_old_name(self):
        self.assertEqual(self.language.old_name_entries("PressureUnit"), ())
        node = self.parser.parse_phrase(
            "Divide («MassUnit» @) "
            "(Multiply («LengthUnit» @) (Power («DurationUnit» @) @@))",
            expected_type="Quantity:Pressure",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Quantity:Pressure")

    def test_dimension_equality_does_not_replace_pressure_attribute_identity(self):
        pressure = self.parser.parse_phrase(
            "Pressure This",
            expected_type="Quantity:Pressure",
        )
        dimensional = self.parser.parse_phrase(
            "Divide (Mass This) "
            "(Multiply (Distance This Self) (Power (Extent ThisInterval) @@))",
            expected_type="Quantity:Pressure",
        )
        self.assertNotIsInstance(pressure, Diagnostic, pressure)
        self.assertNotIsInstance(dimensional, Diagnostic, dimensional)
        self.assertNotEqual(pressure.canonical(), dimensional.canonical())

    def test_pressure_uses_generic_measured_attribute_machinery(self):
        for source in (
            "ZeroPressure This.",
            "HighPressure This.",
            "More Pressure Here Zero.",
            "Change This Pressure Zero!",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_change_pressure_rejects_wrong_quantity_dimension(self):
        result = self.parser.check("Change This Pressure Mass Self!")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "DimensionMismatch")


if __name__ == "__main__":
    unittest.main()
