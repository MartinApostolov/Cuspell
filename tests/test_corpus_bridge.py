from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT=Path(__file__).resolve().parents[1]


class CorpusBridgeTests(unittest.TestCase):
    """Executable semantic forms motivated by the Yona corpus analyses."""

    @classmethod
    def setUpClass(cls):
        cls.parser=Parser(Language.load(ROOT))

    def valid(self,source):
        result=self.parser.check(source)
        self.assertTrue(result.valid,result.diagnostics)
        return result.ast.children[0].canonical()

    def test_narrator_is_cat_core(self):
        self.assertEqual(self.valid("Cat Self."),"InstanceOf(Self,Cat)")

    def test_concurrent_actions_core(self):
        self.valid("!Concurrent {Move This Here,EndLife Self}.")

    def test_relative_density_change(self):
        self.valid("!Change This Density Multiply @@ BeforeValue Density This.")

    def test_preserve_volume_during_density_change(self):
        self.valid("!Preserve Volume This Change This Density Multiply @@ BeforeValue Density This.")

    def test_touch_does_not_mean_joined(self):
        touch=self.valid("Touch This Self.")
        joined=self.valid("Joined This Self.")
        self.assertNotEqual(touch,joined)

    def test_hand_shaped_does_not_assert_hand_kind(self):
        shape=self.valid("ShapeLike This Hand.")
        membership=self.valid("Hand This.")
        self.assertNotEqual(shape,membership)

    def test_control_is_separate_state_relation(self):
        self.assertEqual(self.valid("Control Self This."),"Control(controller=Self,target=This)")

    def test_density_comparison(self):
        self.valid("More Density This Density Self.")

    def test_mass_comparison(self):
        self.valid("More Mass Self Mass This.")


if __name__=="__main__":
    unittest.main()
