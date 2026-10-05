from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class MultiBookCorpusPressureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_alice_identity_and_size_change_pressure(self):
        # Semantic core of Alice's report that she has changed repeatedly
        # during the current day and is uncertain about her present identity.
        self.assert_valid("Not Know Self ThisInformation.")
        self.assert_valid(
            "Believe Self Happen "
            "(Change Self Extent More AfterValue Extent Self BeforeValue Extent Self) "
            "ThisInterval."
        )

    def test_treasure_island_apple_barrel_paragraph(self):
        # Discourse mapping for the sampled paragraph:
        # Self=Jim, This=apple barrel, That=Silver,
        # ThisInformation=Silver's speech, ThisInterval=the scene interval.
        for sentence in (
            "In Self Extent This.",
            "Happen Say That ThisInformation ThisInterval.",
            "Happen Sense Self Hearing ThisInformation ThisInterval.",
            "Want Self Not Happen Sense That Vision Self.",
            "Fear Self That.",
            "Know Self ThisInformation.",
        ):
            with self.subTest(sentence=sentence):
                self.assert_valid(sentence)

    def test_time_machine_temporal_claim_can_be_reported_without_time_travel_root(self):
        self.assert_valid("Before Say Self ThisInformation You Now.")
        self.assert_valid("Before Move This Here Now.")

    def test_wealth_of_nations_productive_rate_is_compositional(self):
        self.assert_valid("Can You Begin Exist This.")
        self.assert_valid("More Rate (Begin Exist This) ThisInterval Zero.")

    def test_origin_of_species_dependency_and_population_pressure_are_compositional(self):
        self.assert_valid("Requires Life This Life That.")
        self.assert_valid("More Count They Zero.")

    def test_twenty_thousand_leagues_measurement_pressure_uses_current_geometry(self):
        self.assert_valid("Equal Extent This @@@ «LengthUnit» @@@.")
        self.assert_valid("More Rate (Move This Here) ThisInterval Zero.")


if __name__ == "__main__":
    unittest.main()
