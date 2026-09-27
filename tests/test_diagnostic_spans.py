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

    def test_pipe_group_span_survives_spacing_normalization(self):
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

    def test_phrase_splitter_preserves_pipe_connected_span(self):
        body = "Move | This Here"
        pieces = split_phrases_with_spans(body)
        self.assertEqual([piece.text for piece in pieces], ["Move|This", "Here"])
        self.assertEqual(body[pieces[0].start:pieces[0].end], "Move | This")
        self.assertEqual(body[pieces[1].start:pieces[1].end], "Here")


if __name__ == "__main__":
    unittest.main()
