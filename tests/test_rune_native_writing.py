"""Canonical rune-native binder handles and punctuation group closer.

Legacy ASCII named binders and SequenceEnd stay parseable for archived corpora;
new examples never require unassigned English type words in the written text.
"""
from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.glyphs import GlyphCodec
from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class NativeWritingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser(Language.load(ROOT))
        cls.codec = GlyphCodec.from_repository(ROOT)

    def checked(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, (source, result.diagnostics))
        self.assertEqual(self.codec.decode(self.codec.encode(source)), source)
        return result

    def test_create_fresh_entity_without_ascii_variable_or_type_name(self):
        native = "Create :«This» At $«This» Here Change $«This» Light «LightUnit» @!"
        legacy = "Create x:Entity At $x Here Change $x Light «LightUnit» @!"
        left = self.checked(native)
        right = self.checked(legacy)
        self.assertEqual(left.mana, right.mana)
        self.assertIn("«This»", native)
        self.assertNotIn("Entity", native)

    def test_explicit_cuspell_kind_witness_for_general_binders(self):
        for source in (
            "All :«This»:Thing Life $«This».",
            "Some :«That»:Thing Life $«That».",
            "Some :«Know»:ThisInformation Know Self $«Know».",
        ):
            with self.subTest(source=source):
                self.checked(source)

    def test_untyped_general_binder_has_explainable_error(self):
        invalid = self.parser.check("All :«This» Life $«This».")
        self.assertFalse(invalid.valid)

    def test_quoted_label_must_be_cuspell_spellable(self):
        bad = self.parser.check("All :«abc»:Thing Life $«abc».")
        self.assertFalse(bad.valid)

    def test_unbound_native_variable_is_an_error(self):
        bad = self.parser.check("Life $«This».")
        self.assertFalse(bad.valid)
        self.assertTrue(any(d.code == "FreeVariable" for d in bad.diagnostics))

    def test_colon_group_closer_has_same_meaning_as_legacy_word(self):
        native = "Permitted You Sequence MoveYouHere MoveYouThere : Self."
        legacy = "Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd Self."
        a = self.checked(native)
        z = self.checked(legacy)
        self.assertEqual(a.ast.canonical(), z.ast.canonical())
        self.assertEqual(a.mana, z.mana)
        self.assertEqual(self.codec.encode(native).count("SequenceEnd"), 0)

    def test_unopened_colon_closer_is_not_a_valid_sentence(self):
        self.assertFalse(self.parser.check("Life This : .").valid)

    def test_rune_binder_mana_is_not_charged_for_grammatical_labels(self):
        native = self.checked("Some :«This»:Thing Life $«This».")
        legacy = self.checked("Some x:Entity Life $x.")
        self.assertEqual(native.mana, legacy.mana)


if __name__ == "__main__":
    unittest.main()
