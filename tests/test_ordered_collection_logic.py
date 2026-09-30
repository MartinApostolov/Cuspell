from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class OrderedCollectionLogicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_sequence_value_preserves_member_type(self):
        node = self.parser.parse_phrase(
            "Sequence {This,Self}",
            expected_type="Sequence",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Sequence:Entity")
        self.assertTrue(self.language.is_assignable(node.type, "Collection:Entity"))

    def test_first_and_last_require_ordered_sequence(self):
        first = self.parser.parse_phrase(
            "First Sequence {This,Self}",
            expected_type="Entity",
        )
        last = self.parser.parse_phrase(
            "Last Sequence {This,Self}",
            expected_type="Entity",
        )
        self.assertNotIsInstance(first, Diagnostic, first)
        self.assertNotIsInstance(last, Diagnostic, last)
        self.assertEqual(first.type, "Entity")
        self.assertEqual(last.type, "Entity")

    def test_first_rejects_unordered_collection(self):
        result = self.parser.parse_phrase(
            "First {This,Self}",
            expected_type="Entity",
        )
        self.assertIsInstance(result, Diagnostic)
        self.assertEqual(result.code, "TypeMismatch")

    def test_event_sequence_remains_event_spec(self):
        self.valid("!Sequence {Move This Here,EndLife Self}.")

    def test_sufficient_for_is_distinct_from_requires(self):
        sufficient = self.valid(
            "SufficientFor Life Self Life This."
        ).ast.children[0].canonical()
        required = self.valid(
            "Requires Life This Life Self."
        ).ast.children[0].canonical()
        self.assertNotEqual(sufficient, required)

    def test_because_is_contextual_ordinary_language(self):
        self.valid("Because Life This Life Self.")
        result = self.parser.check(
            "!If Because Life This Life Self Move This Here."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_strict_between_is_composed_from_more(self):
        self.valid("More Mass This Mass Self And More Mass You Mass This.")
        self.valid(
            "More Evaluate Self This Evaluate Self You "
            "And More Evaluate Self That Evaluate Self This."
        )

    def test_direct_part_is_composed_from_part_without_intermediate_part(self):
        direct = self.valid(
            "Part This Self And Not Some x:Entity "
            "(Part This $x And Part $x Self "
            "And Not Same $x This And Not Same $x Self)."
        ).ast.children[0].canonical()
        member = self.valid(
            "Member This {This,Self}."
        ).ast.children[0].canonical()
        self.assertNotEqual(direct, member)

    def test_group_and_members_are_distinct_from_collection_literal(self):
        self.valid("Group This.")
        members = self.parser.parse_phrase(
            "Members This",
            expected_type="Collection:Entity",
        )
        self.assertNotIsInstance(members, Diagnostic, members)
        self.assertEqual(members.type, "Collection:Entity")


if __name__ == "__main__":
    unittest.main()
