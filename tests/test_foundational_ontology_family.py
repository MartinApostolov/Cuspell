from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class FoundationalOntologyFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)

    def test_thing_and_matter_remain_distinct_kinds(self):
        self.assert_valid("Thing This.")
        self.assert_valid("Matter This.")

    def test_group_and_member_remain_distinct_from_collection_structure(self):
        self.assert_valid("Group This.")
        self.assert_valid("Member You This.")

    def test_path_and_region_remain_distinct_spatial_domains(self):
        self.assert_valid("Path This.")
        self.assert_valid("Region This.")
        self.assert_valid("Through ThisPath ThisRegion.")

    def test_sign_rule_and_unit_remain_distinct_foundational_kinds(self):
        self.assert_valid("Sign This.")
        self.assert_valid("Rule This.")
        self.assert_valid("Unit This.")

    def test_foundational_state_properties_remain_independent(self):
        for source in (
            "Exist This.",
            "Female This.",
            "Life This.",
            "Magic This.",
            "Whole This.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)


if __name__ == "__main__":
    unittest.main()
