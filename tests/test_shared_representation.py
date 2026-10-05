from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class SharedRepresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def assert_valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_represent_is_objective_channel_specific_state(self):
        result = self.assert_valid("Represent This You Vision.")
        self.assertIn("Represent(", result.ast.children[0].canonical())

    def test_begin_and_end_represent_are_state_transitions(self):
        self.assert_valid("Begin Represent This You Vision!")
        self.assert_valid("End Represent This You Vision!")

    def test_persist_can_maintain_a_representation(self):
        self.assert_valid("Persist Represent This You Vision ThisInterval!")

    def test_create_can_make_fresh_visual_representation_carrier(self):
        result = self.assert_valid(
            "Create i:Entity Sign $i And Magic $i And At $i Here And Represent $i This Vision!"
        )
        canonical = result.ast.children[0].canonical()
        self.assertIn("Create(", canonical)
        self.assertIn("Represent", canonical)
        self.assertIn("Vision", canonical)

    def test_created_carrier_can_present_multiple_channels(self):
        self.assert_valid(
            "Create i:Entity Sign $i And Magic $i And At $i Here "
            "And Represent $i This Vision And Represent $i This Hearing!"
        )

    def test_existing_image_old_name_can_be_a_representation_carrier(self):
        self.assert_valid(
            "Create i:«Vision«PersistSignThing»» Magic $i And At $i Here "
            "And Represent $i This Vision!"
        )

    def test_represent_is_not_meaning_or_forced_sense(self):
        represented = self.assert_valid("Represent This You Vision.")
        sensed = self.assert_valid("Sense Self Vision This!")
        self.assertNotEqual(
            represented.ast.children[0].canonical(),
            sensed.ast.children[0].canonical(),
        )


if __name__ == "__main__":
    unittest.main()
