from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class QuestionKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_answer_for_links_information_to_question_content(self):
        self.valid("AnswerFor ThisInformation (Question Life This).")

    def test_know_answer_can_state_open_question_knowledge(self):
        self.valid(
            "KnowAnswer Self (Question [m:Method] MethodFor $m Move Self Here)."
        )

    def test_unknown_method_is_not_same_as_false_proposition(self):
        unknown = self.valid(
            "Not KnowAnswer Self (Question [m:Method] MethodFor $m Move Self Here)."
        ).ast.children[0].canonical()
        falsehood = self.valid("Not Life This.").ast.children[0].canonical()
        self.assertNotEqual(unknown, falsehood)

    def test_question_content_remains_information_not_truth(self):
        question = self.parser.parse_phrase(
            "Question [m:Method] MethodFor $m Move Self Here",
            expected_type="Information",
        )
        self.assertNotIsInstance(question, Diagnostic, question)
        self.assertEqual(question.type, "QuestionContent")


if __name__ == "__main__":
    unittest.main()
