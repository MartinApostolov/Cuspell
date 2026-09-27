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

    def test_liquid_matter_is_restricted_matter_not_water(self):
        result = self.parser.check("LiquidMatter This.")
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertEqual(
            meaning,
            "InstanceOf(This,RestrictKind(base=Matter,property=Liquid))",
        )
        self.assertNotIn("Water", meaning)

    def test_gas_water_is_phase_restricted_water(self):
        result = self.parser.check("GasWater This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "InstanceOf(This,RestrictKind(base=Water,property=Gas))",
        )

    def test_opposite_before_is_after_not_not_before(self):
        opposite = self.parser.check("OppositeBefore ThisEvent ThatEvent.")
        negated = self.parser.check("Not Before ThisEvent ThatEvent.")
        self.assertTrue(opposite.valid, opposite.diagnostics)
        self.assertTrue(negated.valid, negated.diagnostics)
        self.assertEqual(
            opposite.ast.children[0].canonical(),
            "After(later=ThisEvent,earlier=ThatEvent)",
        )
        self.assertNotEqual(
            opposite.ast.children[0].canonical(),
            negated.ast.children[0].canonical(),
        )

    def test_change_by_heat_uses_heat_dimension(self):
        result = self.parser.check("!ChangeBy This Heat Heat Self.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "ChangeBy(theme=This,attribute=Heat,delta=Heat(subject=Self))",
        )

    def test_change_sets_exact_heat_value(self):
        result = self.parser.check("!Change This Heat Heat Self.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "Change(theme=This,attribute=Heat,target=Heat(subject=Self))",
        )

    def test_destroy_ends_existence_not_life(self):
        destroyed = self.parser.check("!Destroy This.")
        killed = self.parser.check("!EndLife This.")
        self.assertTrue(destroyed.valid, destroyed.diagnostics)
        self.assertTrue(killed.valid, killed.diagnostics)
        self.assertEqual(
            destroyed.ast.children[0].canonical(),
            "End(state=Exist(subject=This))",
        )
        self.assertNotEqual(
            destroyed.ast.children[0].canonical(),
            killed.ast.children[0].canonical(),
        )

    def test_begin_life_is_a_well_typed_state_transition(self):
        result = self.parser.check("!BeginLife This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "Begin(state=Life(subject=This))",
        )

    def test_generic_statement_is_not_strict_universal(self):
        generic = self.parser.check("Generic [a:Cat] Life $a.")
        universal = self.parser.check("All [a:Cat] Life $a.")
        self.assertTrue(generic.valid, generic.diagnostics)
        self.assertTrue(universal.valid, universal.diagnostics)
        self.assertNotEqual(
            generic.ast.children[0].canonical(),
            universal.ast.children[0].canonical(),
        )

    def test_evidence_relation_does_not_normalize_to_cause(self):
        result = self.parser.check("EvidenceFor ThisInformation Life This.")
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("EvidenceFor", meaning)
        self.assertNotIn("Cause(", meaning)

    def test_asserted_content_does_not_become_outer_truth(self):
        asserted = self.parser.check(
            "Happen Assert You Life Self ThisInterval."
        )
        truth = self.parser.check("Life Self.")
        self.assertTrue(asserted.valid, asserted.diagnostics)
        self.assertTrue(truth.valid, truth.diagnostics)
        self.assertNotEqual(
            asserted.ast.children[0].canonical(),
            truth.ast.children[0].canonical(),
        )


if __name__ == "__main__":
    unittest.main()
