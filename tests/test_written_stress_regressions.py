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
        result = self.parser.check("!Move Some [a:«Know«MoveLifeThing»»] Life $a Here.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "TypeMismatch")

    def test_touching_without_joining_is_satisfiable(self):
        result = self.parser.check("And {Touch This Self,Not Joined This Self}.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_hand_shaped_does_not_entail_hand_kind(self):
        result = self.parser.check("And {ShapeLike This «Grab«LifeMatter»Part»,Not «Grab«LifeMatter»Part» This}.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_or_of_events_is_not_an_executable_command(self):
        result = self.parser.check("!Or {Move This Here,EndLife Self}.")
        self.assertFalse(result.valid)

    def test_former_life_is_distinct_from_not_life(self):
        former = self.parser.check("And {Past Life This,Not Life This}.")
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

    def test_gas_water_keeps_named_kind_and_phase_separate(self):
        result = self.parser.check("«LiquidMatter» This And Gas This.")
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("Concept(core.materials.water)", meaning)
        self.assertIn("Gas(subject=This)", meaning)

    def test_reversed_before_is_after_meaning_not_not_before(self):
        reversed_before = self.parser.check("Before ThatEvent ThisEvent.")
        negated = self.parser.check("Not Before ThisEvent ThatEvent.")
        self.assertTrue(reversed_before.valid, reversed_before.diagnostics)
        self.assertTrue(negated.valid, negated.diagnostics)
        self.assertEqual(
            reversed_before.ast.children[0].canonical(),
            "Before(earlier=ThatEvent,later=ThisEvent)",
        )
        self.assertNotEqual(
            reversed_before.ast.children[0].canonical(),
            negated.ast.children[0].canonical(),
        )

    def test_relative_heat_change_uses_heat_dimension(self):
        result = self.parser.check(
            "!Change This Heat Add BeforeValue Heat This Heat Self."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_change_sets_exact_heat_value(self):
        result = self.parser.check("!Change This Heat Heat Self.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "Change(theme=This,attribute=Heat,target=Heat(subject=Self))",
        )

    def test_end_exist_is_destruction_meaning_not_end_life(self):
        destroyed = self.parser.check("!EndExist This.")
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
        generic = self.parser.check("Generic [a:«LowSize«MoveLifeThing»»] Life $a.")
        universal = self.parser.check("All [a:«LowSize«MoveLifeThing»»] Life $a.")
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
