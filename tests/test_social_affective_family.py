from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class SocialAffectiveFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)

    def test_affective_attitudes_remain_independently_expressible(self):
        for source in (
            "Like Self This.",
            "Love Self This.",
            "Hate Self This.",
            "Admire Self This.",
            "Respect Self This.",
            "Trust Self This.",
            "Fear Self ThisEvent.",
            "CompassionFor Self This.",
            "GratefulTo Self This ThisEvent.",
            "GrieveFor Self ThisEvent.",
            "RemorseFor Self ThisEvent.",
            "ShameAbout Self ThisEvent.",
            "JealousOf Self This.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_emotional_states_and_social_evaluation_remain_distinct(self):
        for source in (
            "Happy Self.",
            "Sad Self.",
            "Angry Self.",
            "More Evaluate Self This Evaluate Self You.",
            "More Reputation Self Reputation This.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_institutional_relations_and_forgiveness_remain_expressible(self):
        for source in (
            "FriendOf Self You.",
            "ParentOf Self This.",
            "SpouseOf Self You.",
            "EngagedTo Self You.",
            "Have Self This.",
            "Own Self This.",
            "ResponsibleFor Self ThisEvent.",
            "Before Forgive Self This Now.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)


if __name__ == "__main__":
    unittest.main()
