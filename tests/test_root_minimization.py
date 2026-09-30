from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class RootMinimizationPassOneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_language_data_validates_after_reduction(self):
        self.assertEqual(validate_language_data(ROOT), [])

    def test_removed_exact_redundancy_roots_are_gone(self):
        for surface in (
            "After", "Less", "AtLeast", "AtMost", "EvidenceAgainst",
            "NotDetected", "Never", "False", "Claim", "Lose", "Destroy",
        ):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))

    def test_reversed_relations_replace_after_and_less(self):
        for source in (
            "Before ThatEvent ThisEvent.",
            "More Reputation This Reputation Self.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_atleast_and_atmost_are_compositional(self):
        cases = (
            "More Reputation Self Reputation This Or Equal Reputation Self Reputation This.",
            "More Reputation This Reputation Self Or Equal Reputation Self Reputation This.",
        )
        for source in cases:
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_negative_relations_use_not(self):
        cases = (
            "EvidenceFor ThisInformation Not LifeThis.",
            "Not Detected Self This.",
            "Always Not LifeThis ThisInterval.",
            "Not True.",
            "Not In This ThisRegion.",
        )
        for source in cases:
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_state_boundaries_replace_lose_and_destroy(self):
        for source in (
            "!EndHave Self This.",
            "!EndExist This.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_assert_replaces_claim_and_in_remains_base_containment(self):
        for source in (
            "Past Assert Self LifeThis.",
            "In This ThisRegion.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)


    def test_pass2_removed_compositional_roots_are_gone(self):
        for surface in (
            "Contain", "Get", "Join", "Separate", "Tell",
            "See", "Hear", "Smell", "Taste", "ChangeBy", "Converse",
        ):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))

    def test_pass2_state_and_spatial_replacements_parse(self):
        for source in (
            "In This ThisRegion.",
            "!BeginHave Self This.",
            "!BeginJoined This Self.",
            "!EndJoined This Self.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_pass2_say_replaces_tell(self):
        result = self.parser.check("!Say Self ThisInformation You.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass2_generic_sense_replaces_channel_specific_verbs(self):
        for channel in ("Vision", "Hearing", "Olfaction", "Gustation"):
            with self.subTest(channel=channel):
                result = self.parser.check(f"!Sense Self {channel} ThisInformation.")
                self.assertTrue(result.valid, result.diagnostics)

    def test_pass2_change_by_is_composed_from_change_add_before_value(self):
        result = self.parser.check(
            "!Change This Density Add BeforeValue Density This Density Self."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass2_rebuilt_old_names_resolve(self):
        for sign in (
            "InThing",
            "GiveBeginHaveThing",
            "BeginJoinedThing",
            "EndJoinedMatter«UseThing»",
            "SayKnow«Know«MoveLifeThing»»",
            "VisionThrough«PreventMoveThing»Part",
            "OlfactionPath",
        ):
            with self.subTest(sign=sign):
                self.assertTrue(self.language.old_name_entries(sign))


    def test_pass3_removed_derived_wrappers_are_gone(self):
        for surface in ("Between", "Ask", "TimeOverlap"):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))

    def test_pass3_replacements_parse(self):
        for source in (
            "More Mass This Mass Self And More Mass You Mass This.",
            "!Say Self (Question Life You) You.",
            "Overlap ThisInterval ThisInterval.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_pass3_rebuilt_bridge_old_name_resolves(self):
        self.assertTrue(self.language.old_name_entries("MoveSidesThing"))


if __name__ == "__main__":
    unittest.main()
