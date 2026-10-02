from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CorpusGapCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_quoted_sign_and_name_relation(self):
        result = self.valid("Name «Sally» This.")
        self.assertIn("«Sally»", result.ast.children[0].canonical())

    def test_name_can_form_explicit_unique_entity_selection(self):
        node = self.parser.parse_phrase(
            "Unique Collect e:Entity Name «Sally» $e",
            expected_type="Entity",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Entity")

    def test_contextual_name_selection_is_not_free_magic_targeting(self):
        result = self.parser.check(
            "!Move Unique Collect e:Entity Name «Sally» $e Here."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_anaphoric_that_is_ordinary_contextual_reference(self):
        self.valid("Life That.")
        result = self.parser.check("!EndLife That.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_plural_anaphora_is_collection_typed(self):
        node = self.parser.parse_phrase("They", expected_type="Collection:Entity")
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Collection:Entity")

    def test_partition_preserves_nested_member_type(self):
        node = self.parser.parse_phrase(
            "Partition {This,Self} @@",
            expected_type="Collection",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Collection:Collection:Entity")
        self.assertTrue(node.meta_dict().get("contextual"))

    def test_partition_requires_positive_integer_group_size(self):
        result = self.parser.parse_phrase(
            "Partition {This,Self} Zero",
            expected_type="Collection",
        )
        self.assertIsInstance(result, Diagnostic)
        self.assertEqual(result.code, "ValueDomainMismatch")

    def test_unknown_and_unavailable_attribute_values_are_distinct(self):
        unknown = self.valid("UnknownValueOf This Mass.").ast.children[0].canonical()
        unavailable = self.valid("UnavailableValueOf This Mass.").ast.children[0].canonical()
        self.assertNotEqual(unknown, unavailable)

    def test_distribution_field_queries(self):
        self.valid(
            "Equal Density DistributionOf This Self ThisRegion Density This."
        )
        amount = self.parser.parse_phrase(
            "TotalAmount DistributionOf This Self ThisRegion",
            expected_type="Quantity",
        )
        self.assertNotIsInstance(amount, Diagnostic, amount)

    def test_distribution_transfer_replaces_redistribute(self):
        self.valid(
            "!Transfer DistributionOf This Self ThisRegion ThisRegion."
        )
        self.valid(
            "!Transfer DistributionOf This Self ThisRegion ThisRegion _ DistributionOf You Self."
        )

    def test_absolute_mass_change_rejects_negative_static_target(self):
        result = self.parser.check(
            "!Change This Mass Opposite «MassUnit» @."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "ValueDomainMismatch")

    def test_absolute_mass_change_accepts_nonnegative_target(self):
        self.valid("!Change This Mass «MassUnit» @@.")

    def test_relative_change_may_use_negative_delta(self):
        self.valid(
            "!Change This Mass Add BeforeValue Mass This Opposite «MassUnit» @."
        )

    def test_repeat_count_is_nonnegative_integer(self):
        result = self.parser.check("!Repeat Opposite @ Move This Here.")
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "ValueDomainMismatch")

    def test_dynamic_absolute_value_carries_domain_constraint(self):
        node = self.parser.parse_phrase(
            "Change This Mass Mass Self",
            expected_type="EventSpec",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertIn(
            ("target", "nonnegative"),
            node.meta_dict().get("value_domain_constraints", ()),
        )


if __name__ == "__main__":
    unittest.main()
