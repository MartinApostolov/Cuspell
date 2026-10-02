from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser
from cuspell.surface import split_phrases_with_spans

ROOT = Path(__file__).resolve().parents[1]


class DiagnosticSpanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))

    def test_type_mismatch_span_uses_original_sentence_offsets(self):
        source = "  !Move This @@.  "
        result = self.parser.check(source)
        self.assertFalse(result.valid)
        diagnostic = result.diagnostics[0]
        self.assertEqual(diagnostic.code, "TypeMismatch")
        self.assertEqual(source[diagnostic.source_start:diagnostic.source_end], "@@")
        self.assertEqual(diagnostic.to_dict()["source_span"], {"start": 13, "end": 15})

    def test_debug_pipe_group_span_survives_spacing_normalization(self):
        source = "!Move | This | @@."
        result = self.parser.check(source)
        self.assertFalse(result.valid)
        diagnostic = result.diagnostics[0]
        self.assertEqual(
            source[diagnostic.source_start:diagnostic.source_end],
            "Move | This | @@",
        )
        self.assertEqual(diagnostic.field, "Move|This|@@")

    def test_open_question_binder_error_keeps_sentence_offset(self):
        source = "? [q:DefinitelyNotARoot] Life Self."
        result = self.parser.check(source)
        self.assertFalse(result.valid)
        diagnostic = result.diagnostics[0]
        self.assertEqual(diagnostic.code, "TypeMismatch")
        self.assertEqual(
            source[diagnostic.source_start:diagnostic.source_end],
            "[q:DefinitelyNotARoot]",
        )

    def test_parse_phrase_spans_are_relative_unless_offset_supplied(self):
        phrase = "Move This @@"
        diagnostic = self.parser.parse_phrase(phrase, expected_type="EventSpec")
        self.assertEqual(phrase[diagnostic.source_start:diagnostic.source_end], "@@")

        shifted = self.parser.parse_phrase(
            phrase,
            expected_type="EventSpec",
            source_offset=20,
        )
        self.assertEqual((shifted.source_start, shifted.source_end), (30, 32))

    def test_phrase_splitter_preserves_debug_pipe_connected_span(self):
        body = "Move | This Here"
        pieces = split_phrases_with_spans(body)
        self.assertEqual([piece.text for piece in pieces], ["Move|This", "Here"])
        self.assertEqual(body[pieces[0].start:pieces[0].end], "Move | This")
        self.assertEqual(body[pieces[1].start:pieces[1].end], "Here")

    def test_valid_ast_node_retains_original_source_span(self):
        source = "!Move This Here."
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        event = result.ast.children[0]
        self.assertEqual(
            source[event.source_start:event.source_end],
            "Move This Here",
        )
        self.assertEqual(
            event.to_dict()["source_span"],
            {"start": event.source_start, "end": event.source_end},
        )

    def test_semantic_contradiction_inherits_expression_span(self):
        source = "And {Life This,Not Life This}."
        result = self.parser.check(source)
        self.assertFalse(result.valid)
        diagnostic = result.diagnostics[0]
        self.assertEqual(diagnostic.code, "ContradictoryConstraint")
        self.assertEqual(
            source[diagnostic.source_start:diagnostic.source_end],
            "And {Life This,Not Life This}",
        )

    def test_execution_closure_points_to_incomplete_nested_event(self):
        source = "!If Life This Move This."
        result = self.parser.check(source)
        self.assertFalse(result.valid)
        diagnostic = result.diagnostics[0]
        self.assertEqual(diagnostic.code, "SemanticallyIncomplete")
        self.assertEqual(
            source[diagnostic.source_start:diagnostic.source_end],
            "Move This",
        )

    def test_collection_child_falls_back_to_collection_source_phrase(self):
        source = "!Sequence {Move This,EndLife Self}."
        result = self.parser.check(source)
        self.assertFalse(result.valid)
        diagnostic = result.diagnostics[0]
        self.assertEqual(diagnostic.code, "SemanticallyIncomplete")
        self.assertEqual(
            source[diagnostic.source_start:diagnostic.source_end],
            "{Move This,EndLife Self}",
        )


if __name__ == "__main__":
    unittest.main()
