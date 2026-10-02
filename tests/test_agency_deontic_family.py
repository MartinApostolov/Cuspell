from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class AgencyDeonticFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)

    def test_mental_stances_remain_independently_expressible(self):
        for source in (
            "Want Self MoveSelfHere.",
            "Expect Self MoveSelfHere.",
            "Intend Self MoveSelfHere.",
            "Plan Self Sequence {Move Self Here,Move Self There}.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_capability_and_deontic_relations_remain_distinct(self):
        for source in (
            "Can Self MoveSelfHere.",
            "Obligated Self MoveSelfHere You.",
            "Permitted Self MoveSelfHere You.",
            "Permitted MoveSelfHere Self.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_event_role_execution_mode_and_purpose_remain_distinct(self):
        for source in (
            "Before Attempt Self MoveSelfHere Now.",
            "Reflexive Dodge Self.",
            "Beneficiary Move Self Here You.",
            "Purpose This Move Self Here.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)


if __name__ == "__main__":
    unittest.main()
