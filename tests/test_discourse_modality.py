from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class DiscourseModalityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def valid(self,source):
        result=self.parser.check(source)
        self.assertTrue(result.valid,result.diagnostics)
        return result

    def test_generic_is_valid_ordinary_assertion(self):
        self.valid("Generic [a:«LowSize«MoveLifeThing»»] Life $a.")

    def test_generic_condition_is_not_objective_magic(self):
        result=self.parser.check("!If Generic [a:«LowSize«MoveLifeThing»»] Life $a Move This Here.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code,"SemanticallyIncomplete")
        self.assertIn("context-dependent",result.diagnostics[0].message)

    def test_habitual_is_valid_ordinary_assertion(self):
        self.valid("Habitual Move This Here ThisInterval.")

    def test_habitual_condition_is_not_objective_magic(self):
        result=self.parser.check("!If Habitual Move This Here ThisInterval Move Self Here.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code,"SemanticallyIncomplete")

    def test_most_quantifier(self):
        self.valid("Most [a:«Know«MoveLifeThing»»] Life $a.")

    def test_like_and_prefer(self):
        self.valid("Like Self This.")
        self.valid("More Evaluate Self This Evaluate Self You.")

    def test_can_and_intend_are_distinct(self):
        can=self.valid("Can Self Move Self Here.").ast.children[0].canonical()
        intend=self.valid("Intend Self Move Self Here.").ast.children[0].canonical()
        self.assertNotEqual(can,intend)

    def test_obligation_and_permission(self):
        self.valid("Obligated Self Move Self Here.")
        self.valid("Permitted Self Move Self Here.")


if __name__=="__main__":
    unittest.main()
