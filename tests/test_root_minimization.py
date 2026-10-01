from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.model import Diagnostic
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
            "Not Some c:SenseChannel Happen Sense Self $c This.",
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
            "And {Part This Self,Not Some x:Entity And {Part This $x,Part $x Self,Not Equal $x This,Not Equal $x Self}}."
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
            "More Rate Density This ThisInterval Zero.",
            "More Opposite Rate Density This ThisInterval Zero.",
            "More Rate Rate Density This ThisInterval ThisInterval Zero.",
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

    def test_pass13_teach_is_cause_learning_transition(self):
        self.assertIsNone(self.language.entry("Teach"))
        result = self.parser.check("!Cause Self Begin Know This ThisInformation.")
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
        source = "Some p:Entity And {ParentOf $p Self,ParentOf $p This,Not Equal Self This}"
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
            "And {Not HighHunger Self,Low Distance HighHunger Self}.",
            "High Rate Move This Here ThisInterval.",
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
            "Equal Rate Density This ThisInterval Zero.",
            "And {Not More Rate Density This ThisInterval Rate Density Self ThisInterval,Not More Opposite Rate Density This ThisInterval Rate Density Self ThisInterval}.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass20_low_replaces_rarely(self):
        self.assertIsNone(self.language.entry("Rarely"))
        self.assertIsNotNone(self.language.entry("Low"))
        result = self.parser.check("Low Rate Move This Here ThisInterval.")
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
        result = self.parser.check("Equal Divide @ Rate Move This Here «DurationUnit» @.")
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
        self.assertIsNone(self.language.entry("Size"))
        self.assertIsNotNone(self.language.entry("Extent"))
        result = self.parser.check("HighExtent This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass30_small_is_low_size(self):
        self.assertIsNone(self.language.entry("Small"))
        result = self.parser.check("LowExtent This.")
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
        result = self.parser.check("?[f:CoordinateFrame] Equal Extent This $f @ «LengthUnit» @.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass36_width_is_secondary_axis_span(self):
        self.assertIsNone(self.language.entry("Width"))
        result = self.parser.check("?[f:CoordinateFrame] Equal Extent This $f @@ «LengthUnit» @.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass37_grow_is_constrained_size_change(self):
        self.assertIsNone(self.language.entry("Grow"))
        node = self.parser.parse_phrase(
            "Change This Extent More AfterValue Extent This BeforeValue Extent This",
            expected_type="EventSpec",
        )
        self.assertFalse(hasattr(node, "code"), node)
        magic = self.parser.check(
            "!Change This Extent More AfterValue Extent This BeforeValue Extent This."
        )
        self.assertFalse(magic.valid)
        self.assertEqual(magic.diagnostics[0].code, "SemanticallyIncomplete")

    def test_pass38_promise_is_say_plus_begin_commitment(self):
        self.assertIsNone(self.language.entry("Promise"))
        result = self.parser.check(
            "!And {Say Self (Obligated Self (Move Self Here) :context You) You,Begin (Obligated Self (Move Self Here) :context You)}."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass39_same_is_entity_equal(self):
        self.assertIsNone(self.language.entry("Same"))
        result = self.parser.check("Equal Self This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(result.ast.children[0].type, "StateProposition")

    def test_pass40_detected_is_happened_sense(self):
        self.assertIsNone(self.language.entry("Detected"))
        for source in (
            "Happen Sense Self Vision This.",
            "Some c:SenseChannel Happen Sense Self $c This.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass41_method_for_is_purpose(self):
        self.assertIsNone(self.language.entry("MethodFor"))
        result = self.parser.check("?[m:Method] Purpose $m Move This Here.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass42_using_is_use_relation_overload(self):
        self.assertIsNone(self.language.entry("Using"))
        for source in (
            "Use ThisEvent This.",
            "Use Move Self Here This.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)


    def test_pass43_habitual_is_high_occurrence_rate(self):
        self.assertIsNone(self.language.entry("Habitual"))
        result = self.parser.check("High Rate Move This Here ThisInterval.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass44_depth_is_third_axis_span(self):
        self.assertIsNone(self.language.entry("Depth"))
        for source in (
            "?[f:CoordinateFrame] More Extent This $f @@@ Extent You $f @@@.",
            "More Extent This @@@ Extent You @@@.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass45_thank_is_say_gratitude(self):
        self.assertIsNone(self.language.entry("Thank"))
        for source in (
            "Before Say Self (GratefulTo Self This) This Now.",
            "Before Say Self (GratefulTo Self This :basis ThisInformation) This Now.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass46_apologize_is_say_remorse(self):
        self.assertIsNone(self.language.entry("Apologize"))
        for source in (
            "Before Say Self (RemorseFor Self) This Now.",
            "Before Say Self (RemorseFor Self ThisInformation) This Now.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)


    def test_pass47_whenever_is_during_sufficient_for(self):
        self.assertIsNone(self.language.entry("Whenever"))
        result = self.parser.check(
            "During SufficientFor Life This Move This Here ThisInterval."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass48_next_occurrence_is_first_eventspec(self):
        self.assertIsNone(self.language.entry("NextOccurrence"))
        result = self.parser.check(
            "Happen First Move This Here ThisInterval."
        )
        self.assertTrue(result.valid, result.diagnostics)
        contextual = self.parser.check(
            "!Sequence {First Move This Here,Move Self Here}."
        )
        self.assertFalse(contextual.valid)
        self.assertEqual(contextual.diagnostics[0].code, "SemanticallyIncomplete")

    def test_pass49_redistribute_is_distribution_transfer(self):
        self.assertIsNone(self.language.entry("Redistribute"))
        for source in (
            "!Transfer DistributionOf This Self ThisRegion ThisRegion.",
            "!Transfer DistributionOf This Self ThisRegion ThisRegion :profile DistributionOf You Self.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass50_because_is_contextual_explains(self):
        self.assertIsNone(self.language.entry("Because"))
        result = self.parser.check("Explains Life Self Life This.")
        self.assertTrue(result.valid, result.diagnostics)
        contextual = self.parser.check(
            "!If Explains Life Self Life This Move This Here."
        )
        self.assertFalse(contextual.valid)
        self.assertEqual(contextual.diagnostics[0].code, "SemanticallyIncomplete")


    def test_pass51_almost_is_false_plus_low_boundary_distance(self):
        self.assertIsNone(self.language.entry("Almost"))
        for source in (
            "And {Not Life This,Low Distance Life This}.",
            "And {Not Happen (Move This Here),Low Distance (Move This Here)}.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
        magic = self.parser.check(
            "!If And {Not Life This,Low Distance Life This} Move Self Here."
        )
        self.assertFalse(magic.valid)
        self.assertEqual(magic.diagnostics[0].code, "SemanticallyIncomplete")

    def test_pass52_should_is_contextual_high_evaluation(self):
        self.assertIsNone(self.language.entry("Should"))
        result = self.parser.check("High Evaluate Self Move Self Here.")
        self.assertTrue(result.valid, result.diagnostics)
        magic = self.parser.check("!If (High Evaluate Self (Move Self Here)) (Move You Here).")
        self.assertFalse(magic.valid)
        self.assertEqual(magic.diagnostics[0].code, "SemanticallyIncomplete")

    def test_pass53_designed_for_is_purpose(self):
        self.assertIsNone(self.language.entry("DesignedFor"))
        result = self.parser.check("Purpose This Move Self Here.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass54_learn_is_typed_begin_state(self):
        self.assertIsNone(self.language.entry("Learn"))
        for source in (
            "Before Begin Know Self ThisInformation Now.",
            "Before Begin Understand Self ThisInformation Now.",
            "Before Begin Can Self Move Self Here Now.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)


    def test_pass55_generic_is_contextual_high_prevalence(self):
        self.assertIsNone(self.language.entry("Generic"))
        result = self.parser.check(
            "High Ratio Count Collect [a:Entity] Life $a Count Collect [b:Entity]."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass56_size_is_contextual_extent_evaluation(self):
        self.assertIsNone(self.language.entry("Size"))
        for source in (
            "HighExtent This.",
            "More Extent This Extent You.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass57_span_is_axis_extent(self):
        self.assertIsNone(self.language.entry("Span"))
        for source in (
            "?[f:CoordinateFrame] More Extent This $f @ Extent You $f @@.",
            "More Extent This @@@ Extent You @@@.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_pass58_committed_to_is_contextual_obligation(self):
        self.assertIsNone(self.language.entry("CommittedTo"))
        for source in (
            "Obligated Self (Move Self Here) :context You.",
            "!And {Say Self (Obligated Self (Move Self Here) :context You) You,Begin (Obligated Self (Move Self Here) :context You)}.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)


    def test_pass59_teleport_is_discontinuous_at_state_transition(self):
        self.assertIsNone(self.language.entry("Teleport"))
        result = self.parser.check(
            "!And {End At This There,Begin At This Here}."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass60_write_is_agentive_begin_exist_of_sign(self):
        self.assertIsNone(self.language.entry("Write"))
        result = self.parser.check(
            "?[s:Sign] Happen (Cause Self (Begin Exist $s)) ThisInterval."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass61_read_is_interpreted_sign_sense(self):
        self.assertIsNone(self.language.entry("Read"))
        result = self.parser.check(
            "Happen (If (Sign This) (Sense Self This)) ThisInterval."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass62_grab_is_begin_touch_plus_begin_control(self):
        self.assertIsNone(self.language.entry("Grab"))
        result = self.parser.check(
            "Before And {Begin Touch Self This,Begin Control Self This} Now."
        )
        self.assertTrue(result.valid, result.diagnostics)


    def test_pass63_consent_is_say_of_explicit_permission(self):
        self.assertIsNone(self.language.entry("Consent"))
        result = self.parser.check(
            "Before Say Self (Permitted MoveSelfHere :authority Self) Now."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass64_refuse_is_say_of_permission_denial(self):
        self.assertIsNone(self.language.entry("Refuse"))
        result = self.parser.check(
            "Before Say Self (Not (Permitted MoveSelfHere :authority Self)) Now."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass65_deceive_is_cause_of_false_belief(self):
        self.assertIsNone(self.language.entry("Deceive"))
        result = self.parser.check(
            "!If (Not Life This) (Cause Self (Believe You (Life This)))."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass66_sever_is_causative_end_whole(self):
        self.assertIsNone(self.language.entry("Sever"))
        for source in (
            "!Cause Self (End Whole This).",
            "!Cause Self (End Whole This) :instrument You.",
        ):
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)


    def test_pass67_meaning_survives_as_distinct_sign_content_relation(self):
        self.assertIsNotNone(self.language.entry("Meaning"))
        result = self.parser.check("Meaning «yes» Life This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass68_about_survives_as_information_topic_relation(self):
        self.assertIsNotNone(self.language.entry("About"))
        result = self.parser.check("About ThisInformation This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass69_distribution_of_survives_as_distribution_constructor(self):
        self.assertIsNotNone(self.language.entry("DistributionOf"))
        result = self.parser.check(
            "Equal DistributionOf This Self DistributionOf This Self."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass70_total_amount_survives_as_distribution_aggregate(self):
        self.assertIsNotNone(self.language.entry("TotalAmount"))
        result = self.parser.check(
            "Equal TotalAmount DistributionOf This Self ThisRegion TotalAmount DistributionOf This Self ThisRegion."
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass71_beneficiary_survives_as_distinct_event_role(self):
        self.assertIsNotNone(self.language.entry("Beneficiary"))
        result = self.parser.check("Beneficiary Move Self Here This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass72_bite_survives_as_action_manner(self):
        self.assertIsNotNone(self.language.entry("Bite"))
        result = self.parser.check("!Bite Self This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass73_camouflaged_against_survives_as_perceptual_relation(self):
        self.assertIsNotNone(self.language.entry("CamouflagedAgainst"))
        result = self.parser.check("CamouflagedAgainst Self This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass74_climb_survives_as_locomotion_manner(self):
        self.assertIsNotNone(self.language.entry("Climb"))
        result = self.parser.check("!Climb Self This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass75_contrast_survives_as_discourse_relation(self):
        self.assertIsNotNone(self.language.entry("Contrast"))
        result = self.parser.check("Contrast (Life This) (Magic This).")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass76_dodge_survives_as_evasive_action(self):
        self.assertIsNotNone(self.language.entry("Dodge"))
        result = self.parser.check("Happen Dodge Self (Attack You Self).")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass77_fall_survives_as_nonagentive_motion_manner(self):
        self.assertIsNotNone(self.language.entry("Fall"))
        result = self.parser.check("!Fall This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass78_forgive_survives_as_social_state_transition(self):
        self.assertIsNotNone(self.language.entry("Forgive"))
        result = self.parser.check("!Forgive Self You.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass79_reflexive_survives_as_involuntary_event_status(self):
        self.assertIsNotNone(self.language.entry("Reflexive"))
        result = self.parser.check("Reflexive Attack Self This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass80_jump_survives_as_locomotion_manner(self):
        self.assertIsNotNone(self.language.entry("Jump"))
        result = self.parser.check("Happen Jump Self Here.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass81_limp_survives_as_gait_manner(self):
        self.assertIsNotNone(self.language.entry("Limp"))
        result = self.parser.check("Happen Limp Self.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass82_stab_survives_as_puncturing_action_manner(self):
        self.assertIsNotNone(self.language.entry("Stab"))
        result = self.parser.check("!Stab Self This.")
        self.assertTrue(result.valid, result.diagnostics)

    def test_pass83_rate_consolidates_change_and_occurrence_rate(self):
        self.assertIsNone(self.language.entry("ChangeRate"))
        self.assertIsNone(self.language.entry("OccurrenceRate"))
        self.assertIsNotNone(self.language.entry("Rate"))

        change = self.parser.parse_phrase(
            "Rate Density This ThisInterval",
            expected_type="Quantity",
        )
        self.assertNotIsInstance(change, Diagnostic, change)
        self.assertEqual(
            self.language.quantity_dimension_vector(change.type),
            {"Mass": 1, "Length": -3, "Time": -1},
        )

        occurrence = self.parser.parse_phrase(
            "Rate Move This Here ThisInterval",
            expected_type="Quantity:Frequency",
        )
        self.assertNotIsInstance(occurrence, Diagnostic, occurrence)
        self.assertEqual(
            self.language.quantity_dimension_vector(occurrence.type),
            {"Time": -1},
        )


if __name__ == "__main__":
    unittest.main()

# Threshold-family continuation
