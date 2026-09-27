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

    def test_registered_unit_constructor_is_loaded(self):
        entry = self.language.entry("LengthUnit")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.frames[0]["output"], "Quantity:Length")

    def test_canonical_length_unit_constructs_length_quantity(self):
        node = self.parser.parse_phrase("LengthUnit @@", expected_type="Quantity")
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Quantity:Length")
        self.assertEqual(node.canonical(), "LengthQuantity(amount=2)")
        self.assertEqual(node.meta_dict()["source_unit"], "LengthUnit")

    def test_units_participate_in_dimensional_arithmetic(self):
        node = self.parser.parse_phrase(
            "Divide LengthUnit @@ TimeUnit @",
            expected_type="Quantity",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(
            self.language.quantity_dimension_vector(node.type),
            {"Length": 1, "Time": -1},
        )

    def test_add_rejects_incompatible_unit_dimensions(self):
        result = self.parser.parse_phrase(
            "Add LengthUnit @ TimeUnit @",
            expected_type="Quantity",
        )
        self.assertIsInstance(result, Diagnostic)
        self.assertEqual(result.code, "DimensionMismatch")

    def test_reference_unit_data_validates(self):
        self.assertEqual(validate_language_data(ROOT), [])

    def test_noncanonical_scale_normalizes_to_canonical_amount(self):
        types = load_json("language/core/types.json")
        lexicon = load_json("language/core/lexicon.json")
        compounds = load_json("language/core/compounds.json")
        dimensions = load_json("language/core/dimensions.json")
        units = {
            "units": [
                {
                    "id": "unit.length.canonical",
                    "surface": "LengthUnit",
                    "dimension": "Length",
                    "canonical": True,
                    "scale": {"numerator": 1, "denominator": 1},
                    "rune_cost": 1,
                },
                {
                    "id": "unit.length.double",
                    "surface": "DoubleLengthUnit",
                    "dimension": "Length",
                    "canonical": False,
                    "scale": {"numerator": 2, "denominator": 1},
                    "rune_cost": 1,
                },
            ]
        }
        parser = Parser(Language(ROOT, types, lexicon, compounds, dimensions, units))
        canonical = parser.parse_phrase("LengthUnit @@", expected_type="Quantity:Length")
        alternate = parser.parse_phrase("DoubleLengthUnit @", expected_type="Quantity:Length")
        self.assertNotIsInstance(canonical, Diagnostic, canonical)
        self.assertNotIsInstance(alternate, Diagnostic, alternate)
        self.assertEqual(canonical.canonical(), alternate.canonical())


if __name__ == "__main__":
    unittest.main()
