from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class LogicSpaceTimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def valid(self,source):
        result=self.parser.check(source)
        self.assertTrue(result.valid,result.diagnostics)
        return result.ast.children[0].canonical()

    def test_and_propositions(self):
        self.assertEqual(self.valid("And {Life This,Exist This}."),"And(items=[Life(subject=This),Exist(subject=This)])")

    def test_or_propositions(self):
        self.assertEqual(self.valid("Or {Life This,Exist This}."),"Or(items=[Life(subject=This),Exist(subject=This)])")

    def test_and_events_command(self):
        result=self.parser.check("!And {Move This Here,EndLife Self}.")
        self.assertTrue(result.valid,result.diagnostics)

    def test_concurrent_events(self):
        result=self.parser.check("!Concurrent {Move This Here,EndLife Self}.")
        self.assertTrue(result.valid,result.diagnostics)

    def test_former_state(self):
        self.assertEqual(self.valid("Former Life This."),"Former(state=Life(subject=This))")

    def test_true_false_literals(self):
        self.assertEqual(self.valid("True."),"True()")
        self.assertEqual(self.valid("False."),"False()")

    def test_inside_outside(self):
        self.assertEqual(self.valid("Inside This ThisRegion."),"Inside(item=This,region=ThisRegion)")
        self.assertEqual(self.valid("Outside This ThisRegion."),"Outside(item=This,region=ThisRegion)")

    def test_surface_returns_region_for_center(self):
        result=self.parser.check("!Move This Center Surface Self.")
        self.assertTrue(result.valid,result.diagnostics)

    def test_during_event(self):
        self.assertEqual(self.valid("During ThisEvent ThatEvent."),"During(event=ThisEvent,container=ThatEvent)")

    def test_simultaneous(self):
        self.assertEqual(self.valid("Simultaneous ThisEvent ThatEvent."),"Simultaneous(a=ThisEvent,b=ThatEvent)")

    def test_when_schedules_event(self):
        result=self.parser.check("!When Move This Here Now.")
        self.assertTrue(result.valid,result.diagnostics)

    def test_inclusive_comparison_dimension_check(self):
        result=self.parser.check("AtLeast Distance This Self Distance Self This.")
        self.assertTrue(result.valid,result.diagnostics)


if __name__=="__main__":
    unittest.main()
