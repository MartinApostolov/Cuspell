from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class DiscourseRefinementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_private_name_can_carry_naming_context(self):
        public = self.valid("Name «Road» This.").ast.children[0].canonical()
        private = self.valid("Name «Road» This Self.").ast.children[0].canonical()
        self.assertNotEqual(public, private)

    def test_contrast_marks_concession_without_negating_either_side(self):
        meaning = self.valid(
            "Contrast Life This Life Self."
        ).ast.children[0].canonical()
        self.assertIn("Life(subject=This)", meaning)
        self.assertIn("Life(subject=Self)", meaning)

    def test_contrast_is_contextual_not_magical_truth(self):
        result = self.parser.check(
            "!If Contrast Life This Life Self Move This Here."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_obligation_state_is_distinct_from_compositional_promise_event(self):
        commitment = self.valid(
            "Obligated Self (Move Self Here) :context You."
        ).ast.children[0].canonical()
        promise = self.valid(
            "Happen And {Say Self (Obligated Self (Move Self Here) :context You) You,Begin (Obligated Self (Move Self Here) :context You)} ThisInterval."
        ).ast.children[0].canonical()
        self.assertNotEqual(commitment, promise)

    def test_first_eventspec_replaces_next_occurrence_and_is_contextual(self):
        self.valid("Happen First Move This Here ThisInterval.")
        result = self.parser.check(
            "!Sequence {First Move This Here,Move Self Here}."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_say_records_nested_utterance_context_roles(self):
        node = self.parser.parse_phrase(
            "Say Self Life This You",
            expected_type="EventSpec",
        )
        self.assertEqual(
            node.meta_dict().get("utterance_context_roles"),
            ("speaker", "recipient", "content"),
        )

    def test_assert_and_promise_speech_component_record_context_boundary(self):
        assertion = self.parser.parse_phrase(
            "Assert Self Life This You",
            expected_type="EventSpec",
        )
        promise_speech = self.parser.parse_phrase(
            "Say Self (Obligated Self (Move Self Here) :context You) You",
            expected_type="EventSpec",
        )
        promise = self.parser.parse_phrase(
            "And {Say Self (Obligated Self (Move Self Here) :context You) You,Begin (Obligated Self (Move Self Here) :context You)}",
            expected_type="EventSpec",
        )
        self.assertIn("utterance_context_roles", assertion.meta_dict())
        self.assertIn("utterance_context_roles", promise_speech.meta_dict())
        self.assertIn("Say(", promise.canonical())
        self.assertIn("Begin(", promise.canonical())


if __name__ == "__main__":
    unittest.main()
