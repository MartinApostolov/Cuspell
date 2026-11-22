"""Pre-v1 binder-family stress tests for canonical rune-native surface v0.10.

Cover every binder-bearing frame that wasn't central to the initial inference
suite, and check semantic scope rules rather than only successful tokenization.
No changes to rune assignments, mana costs or approved font contours.
"""
from __future__ import annotations

from pathlib import Path
import re
import unittest

from cuspell.glyphs import GlyphCodec
from cuspell.language import Language
from cuspell.model import Diagnostic, Node
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class BinderFamilyStressTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.codec = GlyphCodec.from_repository(ROOT)

    def valid(self, text: str):
        result = self.parser.check(text)
        self.assertTrue(
            result.valid,
            (text, [diag.to_dict() for diag in result.diagnostics]),
        )
        self.assertEqual(self.codec.decode(self.codec.encode(text)), text)
        glyphs = self.codec.encode(text)
        # Quoted proper Signs (such as «Yona») are exact data, not Cuspell
        # grammar words. Only Latin outside those quoted Signs is a failure.
        grammar_only = re.sub(r"«[^«»]*»", "«»", glyphs)
        self.assertFalse(re.search(r"[A-Za-z]", grammar_only), text)
        return result

    def invalid(self, text: str):
        result = self.parser.check(text)
        self.assertFalse(result.valid, (text, result.ast))
        self.assertTrue(result.diagnostics, text)
        return result

    def phrase(self, source: str, expected: str):
        parsed = self.parser.parse_phrase(source, expected_type=expected)
        self.assertNotIsInstance(parsed, Diagnostic, (source, parsed))
        self.assertEqual(parsed.type, expected)
        self.assertEqual(self.codec.decode(self.codec.encode(source)), source)
        self.assertFalse(re.search(r"[A-Za-z]", self.codec.encode(source)))
        return parsed

    @staticmethod
    def find_binders(node: Node) -> list[Node]:
        return (
            ([node] if node.kind == "Binder" else [])
            + [b for child in node.children for b in BinderFamilyStressTests.find_binders(child)]
        )

    def assert_bound_type(self, result, expected: str):
        binders = self.find_binders(result.ast if hasattr(result, "ast") else result)
        self.assertTrue(binders, result)
        self.assertEqual(binders[0].meta_dict()["bound_type"], expected)

    def test_most_inferrs_entity_from_life(self):
        result = self.valid("Most :«This» Life $«This».")
        self.assert_bound_type(result, "Entity")
        explicit = self.valid("Most :«This»:This Life $«This».")
        self.assertEqual(result.mana, explicit.mana)

    def test_most_needs_evidence_or_witness(self):
        self.invalid("Most :«This» Name «Yona» $«This».")
        self.valid("Most :«This»:This Name «Yona» $«This».")

    def test_trigger_infers_across_condition_and_action(self):
        result = self.valid(
            "Trigger :«This» Life $«This» Move $«This» Here ThisInterval!"
        )
        self.assert_bound_type(result, "Entity")
        explicit = self.valid(
            "Trigger :«This»:This Life $«This» Move $«This» Here ThisInterval!"
        )
        self.assertEqual(result.mana, explicit.mana)

    def test_trigger_keeps_unrelated_simple_frame(self):
        self.valid("Trigger Life This Move Self Here ThisInterval!")

    def test_trigger_type_conflict_and_missing_binding(self):
        self.invalid(
            "Trigger :«This» At Self $«This» Move $«This» Here ThisInterval!"
        )
        self.invalid(
            "Trigger :«This» Name «Yona» $«This» Move Self Here ThisInterval!"
        )

    def test_find_infers_location_from_query(self):
        result = self.valid("Find Self This :«Here» At This $«Here»!")
        self.assert_bound_type(result, "Location")
        explicit = self.valid("Find Self This :«Here»:Here At This $«Here»!")
        self.assertEqual(result.mana, explicit.mana)

    def test_find_infers_entity_from_scoped_query(self):
        result = self.valid(
            "Find Self ThisRegion :«This» In $«This» ThisRegion And Magic $«This»!"
        )
        self.assert_bound_type(result, "Entity")

    def test_find_retains_information_scope_validation(self):
        self.invalid("Find Self ThisRegion :«This» Life $«This»!")
        self.invalid(
            "Find Self ThisRegion :«This»:This Equal ThisRegion ThisRegion!"
        )

    def test_find_does_not_coerce_explicit_wrong_type(self):
        self.invalid("Find Self This :«Here»:This At This $«Here»!")

    def test_question_content_infers_entity(self):
        p = self.phrase("Question :«This» Life $«This»", "QuestionContent")
        self.assert_bound_type(p, "Entity")
        self.valid("AnswerFor ThisInformation (Question :«This» Life $«This»).")

    def test_question_content_requires_witness_for_generic_usage(self):
        source = "Question :«This» Name «Yona» $«This»"
        result = self.parser.parse_phrase(source, expected_type="QuestionContent")
        self.assertIsInstance(result, Diagnostic, result)
        self.phrase(
            "Question :«This»:ThisMethod Purpose $«This» Move Self Here",
            "QuestionContent",
        )

    def test_question_overload_is_not_guessed(self):
        ambiguous = self.parser.parse_phrase(
            "Question :«This» Explains $«This» Life Self",
            expected_type="QuestionContent",
        )
        self.assertIsInstance(ambiguous, Diagnostic, ambiguous)

    def test_each_infers_collection_member(self):
        result = self.valid("Each {This,You} :«This» Move $«This» Here!")
        self.assert_bound_type(result, "Entity")

    def test_filter_infers_member_and_preserves_collection(self):
        p = self.phrase(
            "Filter {This,You} :«This» Life $«This»", "Collection:Entity"
        )
        self.assert_bound_type(p, "Entity")

    def test_extrema_infer_collection_member(self):
        for op, expr in (("MinBy", "Mass"), ("MaxBy", "Mass")):
            with self.subTest(operator=op):
                p = self.phrase(
                    f"{op} {{This,You}} :«This» {expr} $«This»",
                    "Collection:Entity",
                )
                self.assert_bound_type(p, "Entity")

    def test_prevent_bound_frame_type_from_registered_role(self):
        result = self.valid(
            "Prevent :«This» Magic $«This» ThisRegion ThisInterval!"
        )
        self.assert_bound_type(result, "EventSpec")
        self.invalid(
            "Prevent :«This»:This Magic $«This» ThisRegion ThisInterval!"
        )

    def test_active_label_shadowing_still_forbidden_across_families(self):
        self.invalid(
            "Most :«This»:This All :«This»:This Life $«This»."
        )

    def test_unrelated_sentence_scopes_can_reuse_label(self):
        self.valid("Most :«This» Life $«This».")
        self.valid("Trigger :«This» Life $«This» Move $«This» Here ThisInterval!")


if __name__ == "__main__":
    unittest.main()
