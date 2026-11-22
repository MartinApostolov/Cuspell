"""Accepted pre-v1 rules: infer only from typed slots, tight witnesses, scope.

No additional rune, punctuation, font, or magic runtime semantics are needed.
"""
from __future__ import annotations

import unittest
from pathlib import Path
import json
import re

from cuspell.language import Language
from cuspell.parser import Parser
from cuspell.glyphs import GlyphCodec
from cuspell.model import Diagnostic

ROOT = Path(__file__).resolve().parents[1]


class NativeBinderInferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))
        cls.codec = GlyphCodec.from_repository(ROOT)

    def valid(self, text):
        checked = self.parser.check(text)
        self.assertTrue(checked.valid, (text, [x.to_dict() for x in checked.diagnostics]))
        self.assertEqual(self.codec.decode(self.codec.encode(text)), text)
        self.assertFalse(re.search("[A-Za-z]", self.codec.encode(text)))
        return checked

    def invalid(self, text, codes=None):
        checked = self.parser.check(text)
        self.assertFalse(checked.valid, text)
        if codes:
            self.assertIn(checked.diagnostics[0].code, codes, (text, checked.diagnostics))
        return checked

    def test_simple_quantifier_infers_entity_from_life(self):
        result = self.valid("All :«This» Life $«This».")
        binder = result.ast.children[0].children[0]
        self.assertEqual(binder.meta_dict()["bound_type"], "Entity")
        self.assertEqual(result.mana, self.valid("All :«This»:This Life $«This».").mana)

    def test_open_question_infers_entity_from_life(self):
        question = self.valid(":«This» Life $«This»?")
        open_question = question.ast.children[0]
        self.assertEqual(open_question.kind, "OpenQuestion")
        self.assertEqual(open_question.children[0].meta_dict()["bound_type"], "Entity")

    def test_location_inference_and_repeated_uses(self):
        a = self.valid(":«This» At Self $«This»?")
        self.assertEqual(a.ast.children[0].children[0].meta_dict()["bound_type"], "Location")
        b = self.valid("All :«This» (Life $«This» And At $«This» Here).")
        self.assertEqual(b.ast.children[0].children[0].meta_dict()["bound_type"], "Entity")

    def test_infer_collection_member_for_collect(self):
        parsed = self.parser.parse_phrase("Collect :«This» Life $«This»")
        self.assertNotIsInstance(parsed, Diagnostic, parsed)
        self.assertEqual(parsed.type, "Collection:Entity")

    def test_underconstrained_binder_still_requires_cuspell_witness(self):
        result = self.invalid(":«This» Name «Yona» $«This»?")
        self.assertTrue(any(
            d.code in {"MissingBinderType", "TypeMismatch", "AmbiguousPhrase"}
            for d in result.diagnostics
        ))

    def test_conflicting_and_overloaded_types_are_never_guessed(self):
        ambiguous = self.parser.check(":«This» Explains $«This» Life Self?")
        self.assertFalse(ambiguous.valid, ambiguous.ast)
        self.assertTrue(any(d.code in {
            "AmbiguousPhrase", "ConflictingBinderTypes", "MissingBinderType"
        } for d in ambiguous.diagnostics), ambiguous.diagnostics)

    def test_conflicting_entity_and_location_constraints_fail(self):
        self.invalid(":«This» (Life $«This» And At Self $«This»)?",
                     {"ConflictingBinderTypes", "AmbiguousPhrase"})

    def test_two_independent_question_labels_infer_two_types(self):
        result = self.valid(":«This» :«Here» At $«This» $«Here»?")
        binders = result.ast.children[0].children[:-1]
        self.assertEqual([b.meta_dict()["bound_type"] for b in binders],
                         ["Entity", "Location"])

    def test_tight_cuspell_expression_is_type_witness(self):
        witness = self.parser.parse_phrase(":«This»:MassSelf", expected_type="Binder")
        self.assertNotIsInstance(witness, Diagnostic, witness)
        self.assertEqual(witness.meta_dict()["bound_type"], "Quantity:Mass")
        self.assertEqual(witness.value, "MassSelf")
        self.assertEqual(self.codec.decode(self.codec.encode(":«This»:MassSelf")),
                         ":«This»:MassSelf")
        # Equivalent to grouping Mass(Self), but the tight word is preferable.
        ordinary = self.parser.parse_phrase("MassSelf", expected_type="Quantity:Mass")
        spaced = self.parser.parse_phrase("Mass Self", expected_type="Quantity:Mass")
        self.assertNotIsInstance(ordinary, Diagnostic)
        self.assertNotIsInstance(spaced, Diagnostic)
        self.assertEqual(ordinary.canonical(), spaced.canonical())

    def test_duplicate_labels_in_one_open_question_are_rejected(self):
        result = self.invalid(":«This»:This :«This»:Here At $«This» Here?",
                              {"DuplicateBinder"})
        self.assertFalse(result.valid)

    def test_nested_shadowing_of_active_label_is_rejected(self):
        self.invalid(":«This»:This All :«This»:This Life $«This»?",
                     {"DuplicateBinder"})

    def test_separate_scopes_can_reuse_same_label(self):
        self.valid("All :«This» Life $«This».")
        self.valid("Some :«This» Life $«This».")

    def test_legacy_historical_binder_still_parses(self):
        self.assertTrue(self.parser.check("Some x:Entity Life $x.").valid)

    def test_registered_inventory_and_font_assignments_unchanged(self):
        data = json.loads((ROOT / "language/core/glyph_assignments.json").read_text())
        self.assertEqual(len(data["assignments"]), 218)
        self.assertEqual(len(data["spares"]), 16)


if __name__ == "__main__":
    unittest.main()
