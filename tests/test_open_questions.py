from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class OpenQuestionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def valid(self,source):
        result=self.parser.check(source)
        self.assertTrue(result.valid,result.diagnostics)
        return result

    def test_yes_no_question_unchanged(self):
        result=self.valid("?Life This.")
        self.assertEqual(result.ast.children[0].canonical(),"Life(subject=This)")

    def test_open_location_question(self):
        result=self.valid("?[g:Location] Equal $g Here.")
        self.assertEqual(
            result.ast.children[0].canonical(),
            "OpenQuestion(binder=g:Location,query=Equal(left=$g,right=Here))",
        )

    def test_open_question_over_kind(self):
        result=self.valid("?[h:Human] Life $h.")
        self.assertEqual(result.ast.children[0].canonical(),"OpenQuestion(binder=h:Human,query=Life(subject=$h))")
        self.assertEqual(result.mana,2)

    def test_where_are_you_intending_to_move(self):
        result=self.valid("?[g:Location] Intend You Move You $g.")
        self.assertEqual(
            result.ast.children[0].canonical(),
            "OpenQuestion(binder=g:Location,query=Intend(agent=You,goal=Move(theme=You,goal=$g)))",
        )

    def test_open_question_requires_query(self):
        result=self.parser.check("?[g:Location].")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code,"SyntaxError")

    def test_unknown_binder_type_fails(self):
        result=self.parser.check("?[x:NoSuchType] Life This.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code,"TypeMismatch")


if __name__=="__main__":
    unittest.main()
