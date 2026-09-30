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

    def test_former_state_is_compositional(self):
        self.assertEqual(
            self.valid("And {Past Life This,Not Life This}."),
            "And(items=[Past(state=Life(subject=This)),Not(proposition=Life(subject=This))])",
        )

    def test_true_and_compositional_false(self):
        self.assertEqual(self.valid("True."),"True()")
        self.assertEqual(self.valid("Not True."),"Not(proposition=True())")

    def test_in_inside_outside_and_not_in_are_distinct(self):
        inside_or_boundary = self.valid("In This ThisRegion.")
        strict_inside = self.valid("Inside This ThisRegion.")
        outside = self.valid("Outside This ThisRegion.")
        not_in = self.valid("Not In This ThisRegion.")
        self.assertEqual(inside_or_boundary, "In(item=This,region=ThisRegion)")
        self.assertEqual(strict_inside, "Inside(item=This,region=ThisRegion)")
        self.assertEqual(outside, "Outside(item=This,region=ThisRegion)")
        self.assertEqual(not_in, "Not(proposition=In(item=This,region=ThisRegion))")
        self.assertNotEqual(strict_inside, inside_or_boundary)
        self.assertNotEqual(outside, not_in)

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
        result=self.parser.check(
            "More Distance This Self Distance Self This Or Equal Distance This Self Distance Self This."
        )
        self.assertTrue(result.valid,result.diagnostics)


if __name__=="__main__":
    unittest.main()
