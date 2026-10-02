from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.ast import Diagnostic
from cuspell.language import Language
from cuspell.parser import Parser


ROOT = Path(__file__).resolve().parents[1]


class GeneralRelationSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_collect_preserves_non_entity_binder_type(self):
        collected = self.parser.parse_phrase(
            "Collect i:Information Meaning «yes» $i",
            expected_type="Collection:Information",
        )
        self.assertNotIsInstance(collected, Diagnostic, collected)
        self.assertEqual(collected.type, "Collection:Information")

    def test_unique_collect_selects_relation_value_with_same_type(self):
        information = self.parser.parse_phrase(
            "Unique Collect i:Information Meaning «yes» $i",
            expected_type="Information",
        )
        entity = self.parser.parse_phrase(
            "Unique Collect e:Entity Name «Yona» $e",
            expected_type="Entity",
        )
        region = self.parser.parse_phrase(
            "Unique Collect r:Region Name «Oakville» $r",
            expected_type="Region",
        )
        for value in (information, entity, region):
            self.assertNotIsInstance(value, Diagnostic, value)

    def test_name_is_only_the_nonfunctional_relation(self):
        name = self.language.entry("Name")
        self.assertIsNotNone(name)
        self.assertEqual([frame["id"] for frame in name.frames], ["name.relation"])

        shortcut = self.parser.parse_phrase("Name «Yona»", expected_type="Entity")
        self.assertIsInstance(shortcut, Diagnostic)

    def test_interpret_root_is_removed(self):
        self.assertIsNone(self.language.entry("Interpret"))
        result = self.parser.check("Interpret Self «yes»!")
        self.assertFalse(result.valid)

    def test_successful_familiar_reading_is_compositional(self):
        result = self.parser.check(
            "If (Meaning «yes» ThisInformation And Understand Self "
            "(Meaning «yes» ThisInformation)) (Sense Self Vision «yes»)!"
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_learning_a_new_sign_mapping_stays_distinct(self):
        result = self.parser.check(
            "Sequence Sense Self Vision «yes» "
            "Begin Understand Self Meaning «yes» ThisInformation!"
        )
        self.assertTrue(result.valid, result.diagnostics)


if __name__ == "__main__":
    unittest.main()
