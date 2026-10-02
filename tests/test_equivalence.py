from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class EquivalenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def assert_equiv(self,a,b):
        x=self.parser.check(a); y=self.parser.check(b)
        self.assertTrue(x.valid,x.diagnostics); self.assertTrue(y.valid,y.diagnostics)
        self.assertEqual(x.mood,y.mood)
        self.assertEqual(x.ast.children[0].canonical(),y.ast.children[0].canonical())
        return x,y

    def test_debug_pipe_matches_space_meaning(self):
        self.assert_equiv("!Move This Here.","!Move|This|Here.")

    def test_double_not_normalization_keeps_higher_cost(self):
        long,short=self.assert_equiv("NotNotLife This.","Life This.")
        self.assertGreater(long.mana,short.mana)

    def test_after_meaning_uses_before_with_reversed_arguments(self):
        reversed_before=self.parser.check("Before ThatEvent ThisEvent.")
        negated_before=self.parser.check("Not Before ThisEvent ThatEvent.")
        self.assertTrue(reversed_before.valid,reversed_before.diagnostics)
        self.assertTrue(negated_before.valid,negated_before.diagnostics)
        self.assertNotEqual(
            reversed_before.ast.children[0].canonical(),
            negated_before.ast.children[0].canonical(),
        )

    def test_spatial_membership_uses_one_canonical_relation(self):
        result=self.parser.check("In This ThisRegion.")
        self.assertTrue(result.valid,result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "In(item=This,region=ThisRegion)",
        )

    def test_endlife_compound_and_spaced_form(self):
        self.assert_equiv("!EndLife This.","!End Life This.")


if __name__=="__main__":
    unittest.main()
