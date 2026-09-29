from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class SemanticExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def valid(self, source: str, meaning: str | None = None):
        result=self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        if meaning is not None:
            self.assertEqual(result.ast.children[0].canonical(),meaning)
        return result

    def test_state_property(self):
        self.valid("Exist This.","Exist(subject=This)")

    def test_end_state_with_spaces(self):
        self.valid("!End Exist This.","End(state=Exist(subject=This))")

    def test_end_state_compound(self):
        self.valid("!EndExist This.","End(state=Exist(subject=This))")

    def test_destroy_meaning_is_end_exist(self):
        self.valid("!EndExist This.","End(state=Exist(subject=This))")

    def test_state_relation_boundary(self):
        self.valid("!EndIn This ThisRegion.","End(state=In(item=This,region=ThisRegion))")

    def test_direct_begin_state_relation(self):
        self.valid("!Begin In This ThisRegion.","Begin(state=In(item=This,region=ThisRegion))")

    def test_join_and_separate(self):
        self.valid("!Join This Self.","Begin(state=Joined(a=This,b=Self))")
        self.valid("!Separate This Self.","End(state=Joined(a=This,b=Self))")

    def test_some_quantifier(self):
        self.valid("Some [a:Human] Life $a.","Some(binder=a:Human,predicate=Life(subject=$a))")

    def test_collect_count_and_zero(self):
        self.valid("More Count Collect [a:Human] Life $a Zero.")

    def test_unique_selector_returns_entity(self):
        self.valid("Same Unique Collect [a:Human] Life $a Self.")

    def test_nearest_then_unique(self):
        self.valid("Same Unique Nearest Collect [a:Human] Life $a Self Self.")

    def test_bad_unique_input_is_typed_error(self):
        result=self.parser.check("Same Unique Self Self.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code,"TypeMismatch")

    def test_distance_is_length_quantity(self):
        self.valid("Equal Distance This Self Distance Self This.")

    def test_center_can_fill_move_goal(self):
        self.valid("!Move This Center ThisRegion.","Move(theme=This,goal=Center(region=ThisRegion))")

    def test_happen_with_interval(self):
        self.valid("Happen Move This Here ThisInterval.")

    def test_repeat_event(self):
        self.valid("!Repeat @@ Move This Here.","Repeat(count=2,event=Move(theme=This,goal=Here))")

    def test_not_with_spaces(self):
        self.valid("Not Life This.","Not(proposition=Life(subject=This))")

    def test_opposite_quantity_with_spaces(self):
        self.valid("Equal Opposite @@ Opposite @@.")

    def test_at_is_state_proposition(self):
        self.valid("At This Here.","At(item=This,location=Here)")


if __name__=="__main__":
    unittest.main()
