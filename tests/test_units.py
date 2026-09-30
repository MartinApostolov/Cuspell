from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str):
    with (ROOT / path).open(encoding="utf-8") as handle:
        return json.load(handle)


class UnitRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_unit_is_the_only_general_unit_root(self):
        self.assertIsNotNone(self.language.entry("Unit"))
        for surface in (
            "LengthUnit", "TimeUnit", "MassUnit",
            "HeatUnit", "LightUnit", "ConfidenceUnit",
        ):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))

    def test_canonical_units_are_old_names(self):
        for sign in (
            "LengthUnit", "DurationUnit", "MassUnit",
            "HeatUnit", "LightUnit", "ConfidenceUnit",
        ):
            with self.subTest(sign=sign):
                entries = self.language.old_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["meaning"]["kind"], "unit")
                self.assertEqual(entries[0]["meaning"]["type"], "Unit")

    def test_canonical_length_unit_constructs_length_quantity(self):
        node = self.parser.parse_phrase(
            "«LengthUnit» @@",
            expected_type="Quantity",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Quantity:Length")
        self.assertEqual(node.canonical(), "LengthQuantity(amount=2)")
        self.assertEqual(node.meta_dict()["source_unit"], "LengthUnit")

    def test_duration_unit_constructs_time_quantity(self):
        node = self.parser.parse_phrase(
            "«DurationUnit» @",
            expected_type="Quantity:Time",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.canonical(), "TimeQuantity(amount=1)")

    def test_units_participate_in_dimensional_arithmetic(self):
        node = self.parser.parse_phrase(
            "Divide «LengthUnit» @@ «DurationUnit» @",
            expected_type="Quantity",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(
            self.language.quantity_dimension_vector(node.type),
            {"Length": 1, "Time": -1},
        )

    def test_add_rejects_incompatible_unit_dimensions(self):
        result = self.parser.parse_phrase(
            "Add «LengthUnit» @ «DurationUnit» @",
            expected_type="Quantity",
        )
        self.assertIsInstance(result, Diagnostic)
        self.assertEqual(result.code, "DimensionMismatch")

    def test_unit_old_name_cost_comes_from_roots(self):
        self.assertEqual(self.language.old_name_cost("LengthUnit"), 2)
        self.assertEqual(self.language.old_name_cost("DurationUnit"), 2)
        self.assertEqual(self.parser.mana_cost("«LengthUnit» @@."), 4)

    def test_reference_unit_data_validates(self):
        self.assertEqual(validate_language_data(ROOT), [])

    def test_noncanonical_scale_normalizes_to_canonical_amount(self):
        types = load_json("language/core/types.json")
        lexicon = load_json("language/core/lexicon.json")
        compounds = load_json("language/core/compounds.json")
        dimensions = load_json("language/core/dimensions.json")
        old_names = load_json("language/names/old_names.json")
        old_names["entries"] = [
            *old_names["entries"],
            {
                "id": "old.test.double_length_unit",
                "sign": "DoubleLengthUnit",
                "gloss": "double length unit",
                "established_before_magic": True,
                "name_units": [
                    {"sign": "Double", "mana_cost": 1},
                    {"root": "Length"},
                    {"root": "Unit"},
                ],
                "meaning": {
                    "kind": "unit",
                    "type": "Unit",
                    "unit_id": "unit.length.double",
                },
            },
        ]
        units = {
            "units": [
                {
                    "id": "unit.length.canonical",
                    "old_name_id": "old.core.unit.length",
                    "dimension": "Length",
                    "canonical": True,
                    "scale": {"numerator": 1, "denominator": 1},
                },
                {
                    "id": "unit.length.double",
                    "old_name_id": "old.test.double_length_unit",
                    "dimension": "Length",
                    "canonical": False,
                    "scale": {"numerator": 2, "denominator": 1},
                },
            ]
        }
        parser = Parser(
            Language(
                ROOT,
                types,
                lexicon,
                compounds,
                dimensions,
                units,
                old_names,
            )
        )
        canonical = parser.parse_phrase(
            "«LengthUnit» @@",
            expected_type="Quantity:Length",
        )
        alternate = parser.parse_phrase(
            "«DoubleLengthUnit» @",
            expected_type="Quantity:Length",
        )
        self.assertNotIsInstance(canonical, Diagnostic, canonical)
        self.assertNotIsInstance(alternate, Diagnostic, alternate)
        self.assertEqual(canonical.canonical(), alternate.canonical())


if __name__ == "__main__":
    unittest.main()
