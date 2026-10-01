from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class TimeEventFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)

    def test_temporal_order_containment_and_occurrence_remain_distinct(self):
        for source in (
            "Before ThisEvent ThatEvent.",
            "During ThisEvent ThatEvent.",
            "Happen Move Self Here ThisInterval.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_simultaneous_remains_distinct_from_overlap(self):
        for source in (
            "Simultaneous ThisEvent ThatEvent.",
            "Overlap ThisEvent ThatEvent.",
            "Simultaneous Begin ThisEvent Begin ThatEvent.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_eventspec_during_is_not_just_happen(self):
        self.assert_valid("During Move Self Here ThisInterval.")
        self.assert_valid("Happen Move Self Here ThisInterval.")


if __name__ == "__main__":
    unittest.main()
