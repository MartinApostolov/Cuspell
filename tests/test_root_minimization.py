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
            "During Not LifeThis ThisInterval.",
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
            "Before Assert Self LifeThis Now.",
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

    def test_pass4_away_from_is_composed_from_opposite_toward(self):
        self.assertIsNone(self.language.entry("AwayFrom"))
        result = self.parser.parse_phrase(
            "Opposite Toward This",
            expected_type="Direction",
        )
        self.assertFalse(hasattr(result, "code"), result)
        self.assertEqual(result.type, "Direction")

    def test_pass5_direct_part_is_compositional(self):
        self.assertIsNone(self.language.entry("DirectPart"))
        result = self.parser.check(
            "And {Part This Self,Not Some x:Entity And {Part This $x,Part $x Self,Not Same $x This,Not Same $x Self}}."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass6_former_is_compositional(self):
        self.assertIsNone(self.language.entry("Former"))
        result = self.parser.check("And {Before Life This Now,Not Life This}.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertTrue(self.language.old_name_entries("BeforeLifeNowNotLife«LifeMatter»"))

    def test_pass7_information_type_unlocks_know_answer_composition(self):
        self.assertIsNone(self.language.entry("Information"))
        self.assertIsNone(self.language.entry("KnowAnswer"))
        result = self.parser.check(
            "Some i:Information And {Know Self $i,AnswerFor $i (Question Life This)}."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass8_trend_direction_uses_change_rate_and_typed_zero(self):
        self.assertIsNone(self.language.entry("Increasing"))
        self.assertIsNone(self.language.entry("Decreasing"))
        for source in (
            "More ChangeRate Density This ThisInterval Zero.",
            "More Opposite ChangeRate Density This ThisInterval Zero.",
            "More ChangeRate ChangeRate Density This ThisInterval ThisInterval Zero.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_pass9_approx_equal_is_bounded_difference_composition(self):
        self.assertIsNone(self.language.entry("ApproxEqual"))
        result = self.parser.check(
            "And {Not More Add Mass This Opposite Mass Self Mass You,Not More Add Mass Self Opposite Mass This Mass You}."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass10_sometimes_is_happen(self):
        self.assertIsNone(self.language.entry("Sometimes"))
        result = self.parser.check("Happen Move This Here ThisInterval.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass11_members_is_collect_member(self):
        self.assertIsNone(self.language.entry("Members"))
        result = self.parser.parse_phrase(
            "Collect x:Entity Member $x This",
            expected_type="Collection:Entity",
        )
        self.assertFalse(hasattr(result, "code"), result)
        self.assertEqual(result.type, "Collection:Entity")

    def test_pass12_stop_is_end_event(self):
        self.assertIsNone(self.language.entry("Stop"))
        result = self.parser.check("!End ThisEvent.")
        self.assertTrue(result.valid, result.diagnostics)
        end_point = self.parser.parse_phrase("End ThisEvent", expected_type="TimePoint")
        self.assertFalse(hasattr(end_point, "code"), end_point)
        self.assertEqual(end_point.type, "TimePoint")

    def test_pass13_teach_is_cause_learn(self):
        self.assertIsNone(self.language.entry("Teach"))
        result = self.parser.check("!Cause Self Learn This ThisInformation.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass14_prefer_is_evaluation_order(self):
        self.assertIsNone(self.language.entry("Prefer"))
        result = self.parser.check("More Evaluate Self This Evaluate Self You.")
        self.assertTrue(result.valid, result.diagnostics)
        state = self.parser.parse_phrase(
            "More Evaluate Self This Evaluate Self You",
            expected_type="StateProposition",
        )
        self.assertFalse(hasattr(state, "code"), state)
        self.assertEqual(state.type, "StateProposition")

    def test_pass15_sibling_is_shared_parent_state(self):
        self.assertIsNone(self.language.entry("SiblingOf"))
        source = "Some p:Entity And {ParentOf $p Self,ParentOf $p This,Not Same Self This}"
        state = self.parser.parse_phrase(source, expected_type="StateProposition")
        self.assertFalse(hasattr(state, "code"), state)
        self.assertEqual(state.type, "StateProposition")
        result = self.parser.check(source + ".")
        self.assertTrue(result.valid, result.diagnostics)
    def test_pass16_high_replaces_threshold_convenience_roots(self):
        for surface in ("Long","Hungry","Often"):
            self.assertIsNone(self.language.entry(surface))
        for source in (
            "HighLength This.",
            "HighHunger Self.",
            "Almost HighHunger Self.",
            "High OccurrenceRate Move This Here ThisInterval.",
        ):
            result=self.parser.check(source)
            self.assertTrue(result.valid,result.diagnostics)
        self.assertTrue(self.language.old_name_entries("HighLength«LifeMatter»Part"))

    def test_pass17_confidence_threshold_relations_are_compositional(self):
        for surface in ("PossibleTo", "ProbableTo"):
            self.assertIsNone(self.language.entry(surface))
        for source in (
            "More Confidence Self Life This Zero.",
            "High Confidence Self Life This.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass18_injured_is_high_damage(self):
        self.assertIsNone(self.language.entry("Injured"))
        result = self.parser.check("HighDamage This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertTrue(self.language.old_name_entries("HighDamage«LifeMatter»Part"))

    def test_pass19_stable_is_rate_comparison(self):
        self.assertIsNone(self.language.entry("Stable"))
        for source in (
            "Equal ChangeRate Density This ThisInterval Zero.",
            "And {Not More ChangeRate Density This ThisInterval ChangeRate Density Self ThisInterval,Not More Opposite ChangeRate Density This ThisInterval ChangeRate Density Self ThisInterval}.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass20_low_replaces_rarely(self):
        self.assertIsNone(self.language.entry("Rarely"))
        self.assertIsNotNone(self.language.entry("Low"))
        result = self.parser.check("Low OccurrenceRate Move This Here ThisInterval.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass21_sated_is_low_hunger(self):
        self.assertIsNone(self.language.entry("Sated"))
        result = self.parser.check("LowHunger Self.")
        self.assertTrue(result.valid, result.diagnostics)
        state = self.parser.parse_phrase("LowHunger Self", expected_type="StateProposition")
        self.assertFalse(hasattr(state, "code"), state)
        self.assertEqual(state.type, "StateProposition")

    def test_pass22_important_to_is_high_evaluation(self):
        self.assertIsNone(self.language.entry("ImportantTo"))
        result = self.parser.check("High Evaluate Self This.")
        self.assertTrue(result.valid, result.diagnostics)
        state = self.parser.parse_phrase("High Evaluate Self This", expected_type="StateProposition")
        self.assertFalse(hasattr(state, "code"), state)
        self.assertEqual(state.type, "StateProposition")

    def test_pass23_certain_to_is_maximum_confidence(self):
        self.assertIsNone(self.language.entry("CertainTo"))
        result = self.parser.check("Equal Confidence Self Life This «ConfidenceUnit» @.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass24_continue_is_prevent_end_at_present_boundary(self):
        self.assertIsNone(self.language.entry("Continue"))
        result = self.parser.check("!Prevent End ThisEvent Interval Now Now.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass25_period_is_reciprocal_occurrence_rate(self):
        self.assertIsNone(self.language.entry("Period"))
        result = self.parser.check("Equal Divide @ OccurrenceRate Move This Here «DurationUnit» @.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass26_present_is_bare_state_or_ongoing_now(self):
        self.assertIsNone(self.language.entry("Present"))
        for source in (
            "Life This.",
            "During Move This Here Now.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass27_completed_is_past_eventspec(self):
        self.assertIsNone(self.language.entry("Completed"))
        for source in (
            "Before Move This Here Now.",
            "Before Move This Here Now.",
            "Before Move This Here ThisInterval.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass28_ongoing_is_during_eventspec(self):
        self.assertIsNone(self.language.entry("Ongoing"))
        for source in (
            "During Move This Here Now.",
            "During Move This Here ThisInterval.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass29_big_is_high_size(self):
        self.assertIsNone(self.language.entry("Big"))
        self.assertIsNotNone(self.language.entry("Size"))
        result = self.parser.check("HighSize This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass30_small_is_low_size(self):
        self.assertIsNone(self.language.entry("Small"))
        result = self.parser.check("LowSize This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass31_past_is_before_reference(self):
        self.assertIsNone(self.language.entry("Past"))
        for source in (
            "Before Life This Now.",
            "Before Move This Here Now.",
            "Before Move This Here ThisInterval.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass32_future_is_reference_before_value(self):
        self.assertIsNone(self.language.entry("Future"))
        for source in (
            "Before Now Life This.",
            "Before Now Move This Here.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass33_always_is_during_proposition_interval(self):
        self.assertIsNone(self.language.entry("Always"))
        for source in (
            "During Life This ThisInterval.",
            "During Not Life This ThisInterval.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass34_local_density_is_density_distribution_region(self):
        self.assertIsNone(self.language.entry("LocalDensity"))
        result = self.parser.check("More Density DistributionOf This Self ThisRegion Zero.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass35_height_is_primary_axis_span(self):
        self.assertIsNone(self.language.entry("Height"))
        result = self.parser.check("?[f:CoordinateFrame] Equal Span This $f @ «LengthUnit» @.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass36_width_is_secondary_axis_span(self):
        self.assertIsNone(self.language.entry("Width"))
        result = self.parser.check("?[f:CoordinateFrame] Equal Span This $f @@ «LengthUnit» @.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass37_grow_is_constrained_size_change(self):
        self.assertIsNone(self.language.entry("Grow"))
        result = self.parser.check(
            "!Change This Size More AfterValue Size This BeforeValue Size This."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass38_promise_is_say_plus_begin_commitment(self):
        self.assertIsNone(self.language.entry("Promise"))
        result = self.parser.check(
            "!And {Say Self CommittedTo Self Move Self Here You You,Begin CommittedTo Self Move Self Here You}."
        )
        self.assertTrue(result.valid, result.diagnostics)


if __name__ == "__main__":
    unittest.main()

# Threshold-family continuation
