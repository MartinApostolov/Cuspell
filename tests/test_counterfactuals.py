from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CounterfactualTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def test_counterfactual_is_a_proposition(self):
        result = self.parser.check(
            "Counterfactual Before Move Self Here Now Before Life Self Now."
        )
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "assertion")
        self.assertEqual(
            result.ast.children[0].canonical(),
            "Counterfactual(antecedent=Before(earlier=Move(theme=Self,goal=Here),later=Now),consequent=Before(earlier=Life(subject=Self),later=Now))",
        )

    def test_counterfactual_is_not_ordinary_if(self):
        counterfactual = self.parser.check(
            "Counterfactual LifeThis MagicThis."
        )
        conditional = self.parser.check(
            "If LifeThis MagicThis."
        )
        self.assertTrue(counterfactual.valid, counterfactual.diagnostics)
        self.assertTrue(conditional.valid, conditional.diagnostics)
        self.assertNotEqual(
            counterfactual.ast.children[0].canonical(),
            conditional.ast.children[0].canonical(),
        )

    def test_counterfactual_does_not_assert_actual_antecedent_or_consequent(self):
        result = self.parser.check("Counterfactual LifeThis MagicThis.")
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertEqual(
            meaning,
            "Counterfactual(antecedent=Life(subject=This),consequent=Magic(subject=This))",
        )

    def test_counterfactual_is_contextual_and_not_implicit_magic(self):
        result = self.parser.check(
            "If Counterfactual LifeThis MagicThis MoveSelfHere!"
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")
        self.assertIn("context-dependent", result.diagnostics[0].message)


if __name__ == "__main__":
    unittest.main()
