from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class SentenceTerminatorMoodTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def test_period_marks_assertion(self):
        result = self.parser.check("MatterSelf.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "assertion")

    def test_question_mark_marks_question(self):
        result = self.parser.check("LifeThis?")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "question")
        self.assertEqual(result.ast.children[0].canonical(), "Life(subject=This)")

    def test_exclamation_mark_marks_command(self):
        result = self.parser.check("MoveThisHere!")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "command")
        self.assertEqual(result.ast.children[0].canonical(), "Move(theme=This,goal=Here)")

    def test_open_question_uses_final_question_mark(self):
        result = self.parser.check("[g:Location] Intend You Move You $g?")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "question")
        self.assertEqual(
            result.ast.children[0].canonical(),
            "OpenQuestion(binder=g:Location,query=Intend(agent=You,goal=Move(theme=You,goal=$g)))",
        )

    def test_final_mood_marks_cost_no_mana(self):
        command = self.parser.check("Move This Here!")
        legacy = self.parser.check("!Move This Here.")
        self.assertTrue(command.valid, command.diagnostics)
        self.assertTrue(legacy.valid, legacy.diagnostics)
        self.assertEqual(command.mana, legacy.mana)

    def test_redundant_leading_and_trailing_mood_is_invalid(self):
        result = self.parser.check("!Move This Here!")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SyntaxError")

    def test_sentence_requires_a_mood_terminator(self):
        result = self.parser.check("MatterSelf")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SyntaxError")


if __name__ == "__main__":
    unittest.main()
