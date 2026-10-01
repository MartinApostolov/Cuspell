from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class EpistemicDiscourseFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)

    def test_speech_perception_and_inference_processes_remain_distinct(self):
        for source in (
            "Before Say Self Life This You Now.",
            "Before Assert Self Life This You Now.",
            "Before Sense Self Vision This Now.",
            "Before Infer Self ThisInformation Life This Now.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_epistemic_states_remain_distinct(self):
        for source in (
            "Believe Self Life This.",
            "Know Self Life This.",
            "Remember Self ThisInformation.",
            "Understand Self ThisInformation.",
            "High Confidence Self Life This.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)

    def test_information_and_discourse_relations_remain_distinct(self):
        for source in (
            "About ThisInformation This.",
            "Meaning «yes» Life This.",
            "EvidenceFor ThisInformation Life This.",
            "AnswerFor ThisInformation (Question Life This).",
            "Contrast Life This Life Self.",
            "?[x:Explanation] Explains $x Life This.",
        ):
            with self.subTest(source=source):
                self.assert_valid(source)


if __name__ == "__main__":
    unittest.main()
