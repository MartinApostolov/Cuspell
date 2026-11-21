"""Language v1.0 glyph round-trips across maintained book and document examples.

The existing corpus tests remain the source of examples and their semantics:
this integration layer reads those files rather than transcribing a second corpus.
Archived reports are historical context, not normative parser truth.
"""
from __future__ import annotations

import ast
import json
import re
import unittest
from pathlib import Path

from cuspell.glyphs import GlyphCodec
from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]

# Each method is a previously accepted executable book-pressure test.
BOOK_CASES = {
    "Yona chapters 1–168": (
        "test_corpus_post_minimization_regression.py",
        "test_yona_chapters_1_168_semantic_pressure_survives_minimization",
        "yona",
    ),
    "Pride and Prejudice": (
        "test_corpus_post_minimization_regression.py",
        "test_pride_and_prejudice_social_semantics_survive_minimization",
        "core",
    ),
    "Frankenstein": (
        "test_corpus_post_minimization_regression.py",
        "test_frankenstein_epistemic_causal_and_narrative_semantics_survive_minimization",
        "core",
    ),
    "Alice's Adventures in Wonderland": (
        "test_multibook_corpus_pressure.py",
        "test_alice_identity_and_size_change_pressure",
        "core",
    ),
    "Treasure Island": (
        "test_multibook_corpus_pressure.py",
        "test_treasure_island_apple_barrel_paragraph",
        "core",
    ),
    "The Time Machine": (
        "test_multibook_corpus_pressure.py",
        "test_time_machine_temporal_claim_can_be_reported_without_time_travel_root",
        "core",
    ),
    "The Wealth of Nations": (
        "test_multibook_corpus_pressure.py",
        "test_wealth_of_nations_productive_rate_is_compositional",
        "core",
    ),
    "On the Origin of Species": (
        "test_multibook_corpus_pressure.py",
        "test_origin_of_species_dependency_and_population_pressure_are_compositional",
        "core",
    ),
    "Twenty Thousand Leagues under the Sea": (
        "test_multibook_corpus_pressure.py",
        "test_twenty_thousand_leagues_measurement_pressure_uses_current_geometry",
        "core",
    ),
}

OTHER_CORPUS_TESTS = (
    "test_corpus_bridge.py",
    "test_corpus_gap_completion.py",
    "test_cross_genre_vocabulary.py",
    "test_yona_vocabulary.py",
    "test_stabilization_regression.py",
)

CURRENT_DOCUMENTS = (
    "docs/PARSER.md",
    "docs/spec/SURFACE_SYNTAX.md",
    "player/RULES.md",
    "player/BEGINNER_SPELLCRAFT.md",
    "player/SPELLCRAFT_PROGRESSION.md",
)
HISTORICAL_REPORT = "archive/corpus/cross_genre/MULTIBOOK_SEVEN_SOURCE_V08_PASS.md"

# Only complete candidate sentences, not prose paragraphs, test identifiers,
# parser error strings or a standalone sentence-final punctuation character.
_SENTENCE = re.compile(r"^[!]?([A-Z]|«)[^\r\n]*[.!?]$")
_CODE_SPAN = re.compile(r"(?<!`)`([^\n`]+)`(?!`)")


def _looks_like_sentence(text: str, codec: GlyphCodec) -> bool:
    return (len(text) >= 7 and bool(_SENTENCE.fullmatch(text))
            and codec.encode(text) != text)


def _test_literals(path: Path, codec: GlyphCodec, method: str | None = None) -> tuple[str, ...]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    funcs = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name.startswith("test_")
        and (method is None or node.name == method)
    ]
    if method is not None and len(funcs) != 1:
        raise AssertionError(f"Expected one existing corpus method {method!r}: {path}")
    sentences = []
    for func in funcs:
        for node in ast.walk(func):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                text = node.value
                if _looks_like_sentence(text, codec):
                    sentences.append(text)
    return tuple(dict.fromkeys(sentences))


def _document_examples(path: Path, codec: GlyphCodec) -> tuple[str, ...]:
    content = path.read_text(encoding="utf-8")
    return tuple(dict.fromkeys(
        match.group(1) for match in _CODE_SPAN.finditer(content)
        if _looks_like_sentence(match.group(1), codec)
    ))


class GlyphBookDocumentRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.codec = GlyphCodec.from_repository(ROOT)
        cls.core_parser = Parser(Language.load(ROOT))
        cls.yona_parser = Parser(Language.load(ROOT, world_package="yona"))

    def assert_script_parser_equivalence(self, source: str, parser: Parser, require_valid: bool):
        glyphs = self.codec.encode(source)
        self.assertNotEqual(glyphs, source)
        restored = self.codec.decode(glyphs)
        self.assertEqual(restored, source)
        self.assertEqual(self.codec.encode(restored), glyphs)
        original = parser.check(source)
        decoded = parser.check(restored)
        if require_valid:
            self.assertTrue(original.valid, original.diagnostics)
        self.assertEqual(decoded.valid, original.valid)
        self.assertEqual(decoded.mana, original.mana)
        self.assertEqual(
            original.ast.canonical() if original.ast else None,
            decoded.ast.canonical() if decoded.ast else None,
        )
        self.assertEqual(
            tuple(d.code for d in original.diagnostics),
            tuple(d.code for d in decoded.diagnostics),
        )

    def test_nine_book_sources_preserve_parser_meaning_and_mana(self):
        total = 0
        for book, (filename, method, package) in BOOK_CASES.items():
            examples = _test_literals(ROOT / "tests" / filename, self.codec, method)
            with self.subTest(book=book, source="inventory"):
                self.assertGreaterEqual(len(examples), 2, "Original book corpus fixture was removed")
            parser = self.yona_parser if package == "yona" else self.core_parser
            for source in examples:
                with self.subTest(book=book, source=source):
                    self.assert_script_parser_equivalence(source, parser, require_valid=True)
                total += 1
        self.assertGreaterEqual(total, 75)

    def test_additional_yona_social_and_gap_regressions_round_trip(self):
        total = 0
        for filename in OTHER_CORPUS_TESTS:
            examples = _test_literals(ROOT / "tests" / filename, self.codec)
            parser = self.yona_parser if filename == "test_yona_vocabulary.py" else self.core_parser
            with self.subTest(filename=filename, source="inventory"):
                self.assertGreaterEqual(len(examples), 2)
            for source in examples:
                with self.subTest(filename=filename, source=source):
                    # These test files intentionally include both valid and invalid
                    # examples. Preserve the existing outcome; do not relabel it.
                    self.assert_script_parser_equivalence(source, parser, require_valid=False)
                total += 1
        self.assertGreaterEqual(total, 70)

    def test_current_player_and_maintainer_document_examples_round_trip(self):
        total = 0
        for filename in CURRENT_DOCUMENTS:
            examples = _document_examples(ROOT / filename, self.codec)
            with self.subTest(filename=filename, source="inventory"):
                self.assertGreaterEqual(len(examples), 4)
            for source in examples:
                with self.subTest(filename=filename, source=source):
                    self.assert_script_parser_equivalence(source, self.core_parser, require_valid=False)
                total += 1
        self.assertGreaterEqual(total, 45)

    def test_historical_multibook_report_is_retained_as_non_normative_evidence(self):
        examples = _document_examples(ROOT / HISTORICAL_REPORT, self.codec)
        self.assertGreaterEqual(len(examples), 6)
        for source in examples:
            with self.subTest(source=source):
                # The archived report is historical; only typography is asserted.
                self.assertEqual(self.codec.decode(self.codec.encode(source)), source)

    def test_all_yona_world_new_names_preserve_literal_spellings(self):
        names = json.loads((ROOT / "world/yona/new_names.json").read_text(encoding="utf-8"))["entries"]
        self.assertGreaterEqual(len(names), 329)
        for item in names:
            sign = item["sign"]
            spelling = f"«{sign}»"
            with self.subTest(new_name=sign):
                glyphs = self.codec.encode(spelling)
                self.assertEqual(self.codec.decode(glyphs), spelling)
                self.assertEqual(self.codec.encode(spelling), glyphs)


if __name__ == "__main__":
    unittest.main()
