from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class WrittenStressRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def test_negative_two_parses_and_keeps_written_mana_cost(self):
        value = self.parser.parse_phrase("Opposite @@", expected_type="Quantity")
        self.assertNotIsInstance(value, Diagnostic)
        self.assertEqual(value.type, "Quantity:Number")
        self.assertEqual(self.parser.mana_cost("Opposite@@"), 3)

    def test_existential_quantifier_does_not_select_move_target(self):
        result = self.parser.check("!Move Some [a:Human] Life $a Here.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")

    def test_touching_without_joining_is_satisfiable(self):
        result = self.parser.check("And {Touch This Self,Not Joined This Self}.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_hand_shaped_does_not_entail_hand_kind(self):
        result = self.parser.check("And {ShapeLike This Hand,Not Hand This}.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_or_of_events_is_not_an_executable_command(self):
        result = self.parser.check("!Or {Move This Here,EndLife Self}.")
        self.assertFalse(result.valid)

    def test_former_life_is_distinct_from_not_life(self):
        former = self.parser.check("Former Life This.")
        not_life = self.parser.check("Not Life This.")
        self.assertTrue(former.valid, former.diagnostics)
        self.assertTrue(not_life.valid, not_life.diagnostics)
        self.assertNotEqual(
            former.ast.children[0].canonical(),
            not_life.ast.children[0].canonical(),
        )


if __name__ == "__main__":
    unittest.main()
