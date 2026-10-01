from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class OperationalStateFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)

    def test_awake_and_sleep_remain_distinct_states(self):
        self.assert_valid("Awake This.")
        self.assert_valid("Sleep This.")

    def test_open_and_locked_remain_distinct_states(self):
        self.assert_valid("Open This.")
        self.assert_valid("Locked This.")

    def test_begin_end_supply_state_transition_composition(self):
        for source in (
            "Happen Begin Awake This.",
            "Happen Begin Sleep This.",
            "Happen Begin Open This.",
            "Happen End Open This.",
            "Happen Begin Locked This.",
            "Happen End Locked This.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)


if __name__ == "__main__":
    unittest.main()
