from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class BoundedFindTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_find_yesno_acquires_truth_about_explicit_scope(self):
        result = self.assert_valid("Find Self This Magic This!")
        canonical = result.ast.children[0].canonical()
        self.assertIn("Find(", canonical)
        self.assertIn("scope=This", canonical)
        self.assertIn("query=Magic", canonical)

    def test_find_open_query_can_acquire_unknown_location_of_known_subject(self):
        result = self.assert_valid("Find Self This l:Location At This $l!")
        canonical = result.ast.children[0].canonical()
        self.assertIn("answer=l:Location", canonical)
        self.assertIn("At", canonical)

    def test_find_can_search_entities_inside_explicit_region(self):
        self.assert_valid(
            "Find Self ThisRegion x:Entity In $x ThisRegion And Magic $x!"
        )

    def test_find_query_must_use_its_scope(self):
        result = self.parser.check("Find Self This Magic You!")
        self.assertFalse(result.valid)
        self.assertTrue(
            any(
                diagnostic.code == "SemanticallyIncomplete"
                and "information-access scope" in diagnostic.message
                for diagnostic in result.diagnostics
            ),
            result.diagnostics,
        )

    def test_open_find_query_must_use_answer_binder(self):
        result = self.parser.check(
            "Find Self ThisRegion x:Entity Equal ThisRegion ThisRegion!"
        )
        self.assertFalse(result.valid)
        self.assertTrue(
            any(
                diagnostic.code == "SemanticallyIncomplete"
                and "answer binder" in diagnostic.message
                for diagnostic in result.diagnostics
            ),
            result.diagnostics,
        )

    def test_region_scope_is_not_decorative_global_search(self):
        result = self.parser.check("Find Self ThisRegion x:Entity Life $x!")
        self.assertFalse(result.valid)
        self.assertTrue(
            any(
                diagnostic.code == "SemanticallyIncomplete"
                and "information-access scope" in diagnostic.message
                for diagnostic in result.diagnostics
            ),
            result.diagnostics,
        )

    def test_begin_know_with_written_content_is_not_find(self):
        found = self.assert_valid("Find Self This Magic This!")
        imposed = self.assert_valid("Begin Know Self Magic This!")
        self.assertNotEqual(
            found.ast.children[0].canonical(),
            imposed.ast.children[0].canonical(),
        )

    def test_question_mood_remains_non_command_query(self):
        question = self.parser.check("Magic This?")
        self.assertTrue(question.valid, question.diagnostics)
        self.assertEqual(question.mood, "question")
        found = self.assert_valid("Find Self This Magic This!")
        self.assertEqual(found.mood, "command")


if __name__ == "__main__":
    unittest.main()
