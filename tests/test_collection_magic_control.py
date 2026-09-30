from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class CollectionAndMagicControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def valid(self,source,meaning=None):
        result=self.parser.check(source)
        self.assertTrue(result.valid,result.diagnostics)
        if meaning is not None:
            self.assertEqual(result.ast.children[0].canonical(),meaning)
        return result

    def test_filter_existing_collection(self):
        self.valid("More Count Filter Collect [a:«Know«MoveLifeThing»»] Life $a [b:Entity] Exist $b Zero.")

    def test_each_distributes_event(self):
        self.valid("!Each Collect [a:«Know«MoveLifeThing»»] Life $a [b:Entity] EndLife $b.")

    def test_lowest_by_mass_preserves_collection(self):
        self.valid("Same Unique MinBy Collect [a:«Know«MoveLifeThing»»] Life $a [b:Entity] Mass $b Self.")

    def test_highest_by_density_preserves_collection(self):
        self.valid("Same Unique MaxBy Collect [a:«Know«MoveLifeThing»»] Life $a [b:Entity] Density $b Self.")

    def test_persist_state_requires_time_scope(self):
        self.valid("!Persist Life This ThisInterval.")

    def test_persist_without_duration_is_typed_but_incomplete_syntax(self):
        result=self.parser.check("!Persist Life This.")
        self.assertFalse(result.valid)

    def test_simple_trigger(self):
        self.valid("!Trigger Life This Move Self Here ThisInterval.")

    def test_bound_trigger_exports_witness(self):
        self.valid("!Trigger [x:«Know«MoveLifeThing»»] Life $x Move $x Here ThisInterval.")

    def test_stop_specific_event(self):
        self.valid("!Stop ThisEvent.","Stop(event=ThisEvent)")

    def test_prevent_event_over_interval(self):
        self.valid("!Prevent Move This Here ThisInterval.")

    def test_dispel_core_is_end_magic(self):
        self.valid("!EndMagic This.","End(state=Magic(subject=This))")

    def test_approx_equal_quantity_is_compositional(self):
        self.valid(
            "And {Not More Add Density This Opposite Density Self Density This,"
            "Not More Add Density Self Opposite Density This Density This}."
        )


if __name__=="__main__":
    unittest.main()
