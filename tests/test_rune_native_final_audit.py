"""Pre-v1 audit: native type witnesses and absence of legacy binders in live examples.

This intentionally does *not* claim that every internal semantic type is
expressible as a zero-argument Cuspell word. That remains a separate design gate.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

from cuspell.glyphs import GlyphCodec
from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]

# These are independently maintainable, approved rune-native samples.
SENTENCES = (
    ":«This»:ThisExplanation Explains $«This» Life Self?",
    ":«This»:ThisMethod Purpose $«This» Life Self?",
    ":«This»:This ParentOf $«This» Self?",
    ":«Here»:Here At This $«Here»?",
    "Collect :«This»:This Member $«This» They",
    "Unique Collect :«This»:This Name «Yona» $«This»",
)

# These selected specifications contain current Cuspell notation rather than
# only archived examples. Explanatory comments can mention legacy forms, but
# active examples must not *depend* on them.
REQUIRED_NATIVE_SPELLINGS = {
    "docs/spec/EPISTEMIC_REASONING.md": ":«This»:ThisExplanation Explains $«This» Life Self?",
    "docs/spec/RELATIVE_CHANGE_AND_FIELDS.md": ":«This»:ThisMethod Purpose $«This» Life Self?",
    "docs/spec/DISCOURSE_AND_NARRATIVE.md": ":«This»:This ParentOf $«This» Self?",
    "docs/spec/IDENTITY_AND_EXISTENCE.md": "Create :«This» Matter $«This» And At $«This» Here!",
    "docs/spec/LEXICAL_RESOLUTIONS.md": "Unique Collect :«This»:This Name «Yona» $«This»",
    "docs/spec/STRUCTURE_AND_MEREOLOGY.md": "Collect :«This»:This Member $«This» They",
    "docs/spec/TIME_AND_EVENTS.md": "Unique Collect :«This»:ThisInterval",
}


class FinalRuneNativeAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))
        cls.codec = GlyphCodec.from_repository(ROOT)

    def test_known_atomic_type_witnesses_have_actual_registered_meanings(self):
        lexicon = json.loads((ROOT / "language/core/lexicon.json").read_text(encoding="utf-8"))
        declared = {entry["surface"]: entry.get("atom_type") for entry in lexicon["entries"]}
        pairs = {
            "This": "Entity",
            "Here": "Location",
            "ThisEvent": "Event",
            "ThisExplanation": "Explanation",
            "ThisInformation": "Information",
            "ThisMethod": "Method",
            "ThisRegion": "Region",
            "ThisPath": "Path",
            "ThisInterval": "TimeInterval",
            "Now": "TimePoint",
        }
        for rune, expected_type in pairs.items():
            with self.subTest(rune=rune):
                self.assertEqual(declared[rune], expected_type)
                # Check the parser itself: this is not a guessed mapping.
                binder = self.parser.parse_phrase(f":«This»:{rune}", expected_type="Binder")
                self.assertNotIsInstance(binder, Diagnostic)
                self.assertEqual(binder.meta_dict()["bound_type"], expected_type)

    def test_existing_explanation_and_method_binders_are_ordinary_questions(self):
        for sentence in SENTENCES[:4]:
            with self.subTest(sentence=sentence):
                result = self.parser.check(sentence)
                self.assertTrue(result.valid, result.diagnostics)
                glyphs = self.codec.encode(sentence)
                self.assertFalse(re.search(r"[A-Za-z]", glyphs), glyphs)
                self.assertEqual(self.codec.decode(glyphs), sentence)

    def test_other_current_examples_are_native_and_parseable(self):
        for source in SENTENCES[4:]:
            with self.subTest(source=source):
                result = self.parser.parse_phrase(source, expected_type="SemanticValue")
                self.assertNotIsInstance(result, Diagnostic)
                self.assertEqual(self.codec.decode(self.codec.encode(source)), source)

    def test_current_specifications_contain_new_native_examples(self):
        for path, sentence in REQUIRED_NATIVE_SPELLINGS.items():
            with self.subTest(path=path):
                self.assertIn(sentence, (ROOT / path).read_text(encoding="utf-8"))

    def test_no_new_direct_rune_required_for_explanation_or_method(self):
        assignments = json.loads(
            (ROOT / "language/core/glyph_assignments.json").read_text(encoding="utf-8")
        )
        surfaces = {item["surface"] for item in assignments["assignments"]}
        self.assertTrue({"ThisExplanation", "ThisMethod"}.issubset(surfaces))
        self.assertEqual(len(assignments["assignments"]), 218)
        self.assertEqual(len(assignments["spares"]), 16)


if __name__ == "__main__":
    unittest.main()
