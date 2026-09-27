from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class LogicalConstraintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def test_and_detects_property_and_negation(self):
        result=self.parser.check("And {Life This,Not Life This}.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code,"ContradictoryConstraint")

    def test_and_detects_exclusive_family_values(self):
        result=self.parser.check("And {Solid This,Liquid This}.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code,"ContradictoryConstraint")
        self.assertIn("Phase",result.diagnostics[0].message)

    def test_same_properties_on_different_subjects_do_not_conflict(self):
        result=self.parser.check("And {Life This,Not Life Self}.")
        self.assertTrue(result.valid,result.diagnostics)

    def test_or_allows_opposed_alternatives(self):
        result=self.parser.check("Or {Life This,Not Life This}.")
        self.assertTrue(result.valid,result.diagnostics)

    def test_spaced_double_not_normalizes(self):
        a=self.parser.check("Not Not Life This.")
        b=self.parser.check("Life This.")
        self.assertTrue(a.valid,a.diagnostics)
        self.assertTrue(b.valid,b.diagnostics)
        self.assertEqual(a.ast.children[0].canonical(),b.ast.children[0].canonical())
        self.assertGreater(a.mana,b.mana)


if __name__=="__main__":
    unittest.main()
