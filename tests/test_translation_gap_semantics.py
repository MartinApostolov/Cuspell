from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class TranslationGapSemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_evaluation_values_are_ordered(self):
        self.valid("More Evaluate Self This Evaluate Self You.")

    def test_past_present_future_are_available_for_discourse(self):
        self.valid("Past Life This.")
        self.valid("Present Life This.")
        self.valid("Future Move This Here.")

    def test_contextual_tense_does_not_become_objective_magic(self):
        result = self.parser.check("!If Past Life This Move Self Here.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_ongoing_completed_and_continue(self):
        self.valid("Ongoing Move This Here Now.")
        self.valid("Completed Move This Here.")
        self.valid("!Continue ThisEvent.")
        self.valid("!End ThisEvent.")

    def test_whenever_and_frequency_words(self):
        self.valid("Whenever Life This Move This Here ThisInterval.")
        self.valid("Happen Move This Here ThisInterval.")
        self.valid("Often Move This Here ThisInterval.")
        self.valid("Rarely Move This Here ThisInterval.")

    def test_occurrence_rate_has_frequency_dimension(self):
        node = self.parser.parse_phrase(
            "OccurrenceRate Move This Here ThisInterval",
            expected_type="Quantity",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Quantity:Frequency")
        self.assertEqual(
            self.language.quantity_dimension_vector(node.type),
            {"Time": -1},
        )

    def test_change_rate_derives_attribute_dimension_per_time(self):
        node = self.parser.parse_phrase(
            "ChangeRate Density This ThisInterval",
            expected_type="Quantity",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(
            self.language.quantity_dimension_vector(node.type),
            {"Mass": 1, "Length": -3, "Time": -1},
        )

    def test_trend_relations(self):
        self.valid("More ChangeRate ChangeRate Density This ThisInterval ThisInterval Zero.")
        self.valid("More Opposite ChangeRate Density This ThisInterval Zero.")
        self.valid("Stable Density This ThisInterval.")

    def test_zero_is_polymorphic_over_quantity_dimensions(self):
        node = self.parser.parse_phrase("Zero", expected_type="Quantity:Density")
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Quantity:Density")

    def test_requires_is_distinct_from_if(self):
        requires = self.valid("Requires Life This Life Self.").ast.children[0].canonical()
        conditional = self.valid("If Life Self Life This.").ast.children[0].canonical()
        self.assertNotEqual(requires, conditional)

    def test_should_is_weaker_contextual_modality(self):
        self.valid("Should Self Move Self Here.")
        result = self.parser.check("!If Should Self Move Self Here Move You Here.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_almost_requires_a_gradable_property_descriptor(self):
        self.valid("Almost Life This.")
        result = self.parser.parse_phrase("Almost Same This Self", expected_type="Proposition")
        self.assertIsInstance(result, Diagnostic)

    def test_sense_channels_and_detection_are_distinct(self):
        vision = self.valid("Happen Sense Self Vision This ThisInterval.").ast.children[0].canonical()
        hearing = self.valid("Happen Sense Self Hearing This ThisInterval.").ast.children[0].canonical()
        self.assertNotEqual(vision, hearing)
        detected = self.valid("Detected Self This Vision.").ast.children[0].canonical()
        absent = self.valid("Not Detected Self This Vision.").ast.children[0].canonical()
        self.assertNotEqual(detected, absent)

    def test_generic_sense_process(self):
        self.valid("!Sense Self Vision ThisInformation.")

    def test_transfer_is_explicit_resource_movement(self):
        self.valid("!Transfer This Self You @@.")

    def test_purpose_is_not_current_use(self):
        self.valid("Purpose This Move Self Here.")

    def test_ratio_is_not_divide(self):
        ratio = self.parser.parse_phrase("Ratio @@ @@@", expected_type="Ratio")
        quotient = self.parser.parse_phrase("Divide @@ @@@", expected_type="Quantity:Number")
        self.assertNotIsInstance(ratio, Diagnostic, ratio)
        self.assertNotIsInstance(quotient, Diagnostic, quotient)
        self.assertNotEqual(ratio.canonical(), quotient.canonical())


if __name__ == "__main__":
    unittest.main()
