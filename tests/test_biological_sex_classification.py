from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class BiologicalSexClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_male_and_female_are_positive_property_descriptors(self):
        for surface in ("Male", "Female"):
            with self.subTest(surface=surface):
                entry = self.language.entry(surface)
                self.assertIsNotNone(entry)
                self.assertEqual(entry.category, "Property")
                self.assertEqual(entry.data.get("atom_type"), "PropertyDescriptor")
                self.assertTrue(entry.data.get("state_predicate"))

    def test_positive_classification_is_not_logical_negation(self):
        male = self.valid("Male This.").ast.children[0].canonical()
        not_female = self.valid("Not Female This.").ast.children[0].canonical()
        female = self.valid("Female This.").ast.children[0].canonical()
        not_male = self.valid("Not Male This.").ast.children[0].canonical()

        self.assertNotEqual(male, not_female)
        self.assertNotEqual(female, not_male)

    def test_core_language_does_not_force_exhaustive_binary_logic(self):
        for source in (
            "And {Male This,Female This}.",
            "And {Not Male This,Not Female This}.",
            "And {Male This,Not Female This}.",
            "And {Female This,Not Male This}.",
        ):
            with self.subTest(source=source):
                self.valid(source)

    def test_positive_classifiers_keep_persistent_state_transitions(self):
        for source in (
            "Happen Begin Male This.",
            "Happen End Male This.",
            "Happen Begin Female This.",
            "Happen End Female This.",
        ):
            with self.subTest(source=source):
                self.valid(source)

    def test_existing_goddess_old_name_still_uses_female_history(self):
        result = self.valid("«Female«WorshipThing»» This.")
        self.assertIn("Concept(core.religion.goddess)", result.ast.children[0].canonical())
        self.assertTrue(self.language.old_name_entries("Female«WorshipThing»"))


if __name__ == "__main__":
    unittest.main()
