from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CausationInformationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_actual_cause_is_a_proposition(self):
        self.valid("Cause ThisEvent ThatEvent.")

    def test_agent_causative_can_be_commanded(self):
        self.valid("!Cause Self Move This Here.")

    def test_use_has_explicit_agent_instrument_and_goal(self):
        self.valid("!Use Self This Move Self Here.")

    def test_possession_giving_is_not_generic_transfer(self):
        possession = self.valid(
            "Concurrent EndHave Self This BeginHave You This!"
        ).ast.children[0].canonical()
        transfer = self.valid("!Transfer This Self You.").ast.children[0].canonical()
        self.assertNotEqual(possession, transfer)

    def test_purpose_is_persistent_function_not_current_use(self):
        purpose = self.valid(
            "Purpose This Move Self Here."
        ).ast.children[0].canonical()
        using = self.valid(
            "Use Move Self Here This."
        ).ast.children[0].canonical()
        self.assertNotEqual(purpose, using)

    def test_beneficiary_marks_event_participant(self):
        self.valid("Beneficiary Move Self Here You.")

    def test_information_topic(self):
        self.valid("About ThisInformation This.")

    def test_meaning_relates_sign_to_content(self):
        self.valid("Meaning «meow» ThisInformation.")
        self.valid("Meaning «yes» Life This.")

    def test_say_can_carry_semantic_or_quoted_content(self):
        self.valid("!Say Self ThisInformation You.")
        self.valid("!Say Self «hello» You.")
        self.valid("!Say Self Life This You.")

    def test_want_accepts_event_or_proposition(self):
        self.valid("Want Self Move Self Here.")
        self.valid("Want Self Life This.")

    def test_plan_can_hold_ordered_actions(self):
        self.valid(
            "Plan Self Sequence {Move Self Here,Move Self There}."
        )

    def test_expect_is_contextual_epistemic_state(self):
        self.valid("Expect Self Life This.")
        result = self.parser.check(
            "!If Expect Self Life This Move Self Here."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_infer_changes_epistemic_state_without_asserting_truth(self):
        self.valid("!Infer Self ThisInformation Life This.")


if __name__ == "__main__":
    unittest.main()
