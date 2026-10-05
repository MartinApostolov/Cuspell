from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser
from cuspell.model import Diagnostic

ROOT = Path(__file__).resolve().parents[1]


class TimeFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_entity_time_flow_is_explicitly_relative(self):
        result = self.assert_valid("TimeFlow Self ThisRegion @.")
        self.assertIn("TimeFlow", result.ast.children[0].canonical())

    def test_region_time_flow_can_be_stopped_relative_to_entity(self):
        self.assert_valid("TimeFlow ThisRegion Self Zero.")

    def test_persist_can_maintain_time_stop_style_region(self):
        self.assert_valid(
            "Persist TimeFlow ThisRegion Self Zero ThisInterval!"
        )

    def test_faster_entity_time_flow_uses_dimensionless_factor(self):
        self.assert_valid(
            "Persist TimeFlow You Self @@ ThisInterval!"
        )

    def test_slower_entity_time_flow_can_use_arithmetic_factor(self):
        self.assert_valid(
            "Persist TimeFlow You Self Divide @ @@ ThisInterval!"
        )

    def test_time_flow_reference_must_be_spatial_frame_or_worldline(self):
        result = self.parser.check("TimeFlow Self @ @.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")

    def test_time_flow_is_distinct_from_event_frequency_rate(self):
        flow = self.assert_valid("TimeFlow Self ThisRegion @.")
        rate = self.parser.parse_phrase(
            "Rate Move Self Here ThisInterval",
            expected_type="Quantity:Frequency",
        )
        self.assertNotIsInstance(rate, Diagnostic, rate)
        self.assertNotEqual(
            flow.ast.children[0].canonical(),
            rate.canonical(),
        )


if __name__ == "__main__":
    unittest.main()
