from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class NaturalSurfaceFollowupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def meaning(self, source: str) -> str:
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result.ast.children[0].canonical()

    def test_infix_and_matches_collection_form(self):
        self.assertEqual(
            self.meaning("LifeThis And MagicThis."),
            self.meaning("And {LifeThis,MagicThis}."),
        )

    def test_infix_and_chains(self):
        result = self.parser.check("LifeThis And MagicThis And WholeThis.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "assertion")
        self.assertIn("And(", result.ast.children[0].canonical())

    def test_event_and_is_valid_in_command_mood(self):
        result = self.parser.check("MoveSelfHere And MoveYouThere!")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "command")

    def test_infix_or_matches_collection_form(self):
        self.assertEqual(
            self.meaning("LifeThis Or MagicThis."),
            self.meaning("Or {LifeThis,MagicThis}."),
        )

    def test_infix_or_chains(self):
        result = self.parser.check("LifeThis Or MagicThis Or WholeThis.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "assertion")
        self.assertIn("Or(", result.ast.children[0].canonical())

    def test_mixed_and_or_requires_grouping(self):
        result = self.parser.check("LifeThis And MagicThis Or WholeThis.")
        self.assertFalse(result.valid)

        grouped = self.parser.check("(LifeThis And MagicThis) Or WholeThis.")
        self.assertTrue(grouped.valid, grouped.diagnostics)

    def test_sequence_uses_sentence_boundary_when_outermost(self):
        self.assertEqual(
            self.meaning("Sequence MoveSelfHere MoveSelfThere!"),
            self.meaning("Sequence {MoveSelfHere,MoveSelfThere}!"),
        )

    def test_sentence_boundary_closes_nested_sequence(self):
        result = self.parser.check(
            "If LifeThis Sequence MoveSelfHere MoveSelfThere!"
        )
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("If(", meaning)
        self.assertIn("Sequence(", meaning)

    def test_sequence_end_is_used_when_material_follows(self):
        result = self.parser.check(
            "Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd Self."
        )
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn("Permitted(", result.ast.children[0].canonical())

    def test_sequence_without_end_cannot_stop_before_later_material(self):
        result = self.parser.check(
            "Permitted You Sequence MoveYouHere MoveYouThere Self."
        )
        self.assertFalse(result.valid)

    def test_concurrent_uses_sentence_boundary_when_outermost(self):
        self.assertEqual(
            self.meaning("Concurrent MoveSelfHere MoveYouThere!"),
            self.meaning("Concurrent {MoveSelfHere,MoveYouThere}!"),
        )

    def test_sentence_boundary_closes_nested_concurrent(self):
        result = self.parser.check(
            "If LifeThis Concurrent MoveSelfHere MoveYouThere!"
        )
        self.assertTrue(result.valid, result.diagnostics)
        meaning = result.ast.children[0].canonical()
        self.assertIn("If(", meaning)
        self.assertIn("Concurrent(", meaning)

    def test_concurrent_end_is_used_when_material_follows(self):
        result = self.parser.check(
            "Permitted You Concurrent MoveYouHere MoveYouThere ConcurrentEnd Self."
        )
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn("Permitted(", result.ast.children[0].canonical())

    def test_concurrent_without_end_cannot_stop_before_later_material(self):
        result = self.parser.check(
            "Permitted You Concurrent MoveYouHere MoveYouThere Self."
        )
        self.assertFalse(result.valid)

    def test_bare_binder_matches_legacy_bracket_binder(self):
        self.assertEqual(
            self.meaning("All a:«Know«MoveLifeThing»» Life $a."),
            self.meaning("All [a:«Know«MoveLifeThing»»] Life $a."),
        )

    def test_bare_open_question_binder(self):
        result = self.parser.check("g:Location Intend You Move You $g?")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.mood, "question")
        self.assertEqual(
            result.ast.children[0].canonical(),
            "OpenQuestion(binder=g:Location,query=Intend(agent=You,goal=Move(theme=You,goal=$g)))",
        )

    def test_real_collection_values_still_exist(self):
        result = self.parser.parse_phrase(
            "{This,Self,You}",
            expected_type="Collection:Entity",
        )
        self.assertEqual(result.type, "Collection:Entity")


if __name__ == "__main__":
    unittest.main()
