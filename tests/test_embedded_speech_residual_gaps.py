from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class EmbeddedSpeechResidualGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_yes_no_question_content_is_information(self):
        node = self.parser.parse_phrase(
            "Question Life This",
            expected_type="Information",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "QuestionContent")

    def test_open_question_content_scopes_typed_binder(self):
        node = self.parser.parse_phrase(
            "Question [g:Location] Intend You Move You $g",
            expected_type="QuestionContent",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "QuestionContent")
        self.assertIn("binder=", node.canonical())
        self.assertIn("$g", node.canonical())

    def test_say_embeds_semantic_yes_no_question(self):
        self.valid("!Say Self (Question Life You) You.")

    def test_say_embeds_semantic_open_question(self):
        self.valid(
            "!Say Self (Question [g:Location] Intend You Move You $g) You."
        )

    def test_directive_content_is_information_but_not_active_command(self):
        node = self.parser.parse_phrase(
            "Directive Move You Here",
            expected_type="Information",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "CommandContent")

    def test_say_can_transfer_embedded_directive(self):
        self.valid("!Say Self (Directive Move You Here) You.")

    def test_say_can_carry_question_or_directive_information(self):
        self.valid("!Say Self (Question Life You) You.")
        self.valid("!Say Self (Directive Move You Here) You.")

    def test_embedded_question_does_not_retrieve_truth(self):
        question = self.parser.parse_phrase(
            "Question Life This",
            expected_type="QuestionContent",
        )
        proposition = self.parser.parse_phrase(
            "Life This",
            expected_type="Proposition",
        )
        self.assertNotEqual(question.canonical(), proposition.canonical())

    def test_near_event_occurrence_uses_boundary_distance(self):
        self.valid("And {Not Happen (Move This Here),Low Distance (Move This Here)}.")

    def test_event_boundary_distance_remains_contextual_not_magical_condition(self):
        result = self.parser.check(
            "!If And {Not Happen (Move This Here),Low Distance (Move This Here)} Move Self Here."
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.diagnostics[0].code, "SemanticallyIncomplete")

    def test_permission_can_name_authority(self):
        with_authority = self.valid(
            "Permitted You (Move You Here) :authority Self."
        ).ast.children[0].canonical()
        without_authority = self.valid(
            "Permitted You Move You Here."
        ).ast.children[0].canonical()
        self.assertNotEqual(with_authority, without_authority)
        self.assertIn("authority=Self", with_authority)

    def test_denied_permission_by_explicit_authority(self):
        self.valid("Not Permitted You (Move You Here) :authority Self.")

    def test_say_records_nested_utterance_context(self):
        question_say = self.parser.parse_phrase(
            "Say Self (Question Life You) You",
            expected_type="EventSpec",
        )
        say = self.parser.parse_phrase(
            "Say Self (Directive Move You Here) You",
            expected_type="EventSpec",
        )
        self.assertEqual(
            question_say.meta_dict().get("utterance_context_roles"),
            ("speaker", "recipient", "content"),
        )
        self.assertEqual(
            say.meta_dict().get("utterance_context_roles"),
            ("speaker", "recipient", "content"),
        )


if __name__ == "__main__":
    unittest.main()
