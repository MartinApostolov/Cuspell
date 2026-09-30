from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CrossGenreOrdinaryVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_language_data_validates(self):
        self.assertEqual(validate_language_data(ROOT), [])

    def test_social_and_emotional_relations_are_core(self):
        for surface in (
            "Love", "Hate", "Trust", "Respect", "Admire", "GratefulTo",
            "CompassionFor", "JealousOf", "Fear", "GrieveFor", "RemorseFor",
            "ShameAbout", "FriendOf", "ParentOf", "SiblingOf", "SpouseOf",
            "EngagedTo", "Own", "Understand", "Remember", "ResponsibleFor",
        ):
            with self.subTest(surface=surface):
                entry = self.language.entry(surface)
                self.assertIsNotNone(entry)
                self.assertEqual(entry.category, "Relation")

    def test_social_processes_are_core(self):
        for surface in (
            "Consent", "Refuse", "Forgive", "Deceive",
            "Learn", "Apologize", "Thank",
        ):
            with self.subTest(surface=surface):
                entry = self.language.entry(surface)
                self.assertIsNotNone(entry)
                self.assertEqual(entry.category, "Process")

    def test_basic_emotional_states_parse(self):
        for source in (
            "Happy Self.",
            "Sad Self.",
            "Angry Self.",
            "Love Self This.",
            "Hate Self This.",
            "Trust Self This.",
            "Respect Self This.",
            "FriendOf Self This.",
            "ParentOf Self This.",
            "SiblingOf Self This.",
            "SpouseOf Self This.",
            "EngagedTo Self This.",
            "Own Self This.",
            "Fear Self This.",
            "GratefulTo Self This.",
            "CompassionFor Self This.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_cognitive_and_social_change_processes_parse(self):
        for source in (
            "Understand Self ThisInformation.",
            "Remember Self ThisInformation.",
            "Past Learn Self ThisInformation.",
            "Past Cause Self Learn This ThisInformation.",
            "Past Consent Self MoveSelfHere.",
            "Past Refuse Self MoveSelfHere.",
            "Past Forgive Self This.",
            "Past Apologize Self This.",
            "Past Thank Self This.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_reputation_is_an_ordered_attribute(self):
        result = self.parser.check("More Reputation Self Reputation This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_responsibility_remorse_and_shame_can_target_semantic_content(self):
        for source in (
            "ResponsibleFor Self ThisEvent.",
            "RemorseFor Self ThisEvent.",
            "ShameAbout Self ThisEvent.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)


if __name__ == "__main__":
    unittest.main()
