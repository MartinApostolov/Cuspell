from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class TimeIntervalAccessorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_referenced_interval_exposes_begin_point(self):
        node = self.parser.parse_phrase("Begin ThisInterval", expected_type="TimePoint")
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "TimePoint")

    def test_referenced_interval_exposes_end_point(self):
        node = self.parser.parse_phrase("End ThisInterval", expected_type="TimePoint")
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "TimePoint")

    def test_referenced_interval_exposes_temporal_extent(self):
        node = self.parser.parse_phrase("Extent ThisInterval", expected_type="Quantity:Time")
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Quantity:Time")

    def test_constructed_intervals_use_the_same_accessors(self):
        for source, expected_type in (
            ("Begin IntervalFor Now «DurationUnit» @@", "TimePoint"),
            ("End IntervalFor Now «DurationUnit» @@", "TimePoint"),
            ("Extent IntervalFor Now «DurationUnit» @@", "Quantity:Time"),
        ):
            with self.subTest(source=source):
                node = self.parser.parse_phrase(source, expected_type=expected_type)
                self.assertNotIsInstance(node, Diagnostic, node)
                self.assertEqual(node.type, expected_type)


if __name__ == "__main__":
    unittest.main()
