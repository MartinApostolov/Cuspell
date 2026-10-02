from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class PostMinimizationCorpusRegressionTests(unittest.TestCase):
    """Regression sweep over the semantic pressure recorded by the three book corpora."""

    @classmethod
    def setUpClass(cls):
        cls.core = Language.load(ROOT)
        cls.yona = Language.load(ROOT, world_package="yona")
        cls.core_parser = Parser(cls.core)
        cls.yona_parser = Parser(cls.yona)

    def assert_valid_cases(self, parser: Parser, cases: tuple[str, ...]):
        for source in cases:
            with self.subTest(source=source):
                result = parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_language_and_yona_world_data_still_validate(self):
        self.assertEqual(validate_language_data(ROOT), [])

    def test_yona_chapters_1_168_semantic_pressure_survives_minimization(self):
        self.assert_valid_cases(
            self.yona_parser,
            (
                "«LowExtent«MoveLifeThing»» Self.",
                "!Concurrent {Move This Here,EndLife Self}.",
                "!Change This Density Multiply @@ BeforeValue Density This.",
                "!Preserve Volume This Change This Density Multiply @@ BeforeValue Density This.",
                "Before Attempt Self MoveSelfHere Now.",
                "Happen Sense Self Vision This ThisInterval.",
                "Not Happen Sense Self Vision This.",
                "Some i:Information And {Know Self $i,AnswerFor $i (Question [m:Method] Purpose $m Move Self Here)}.",
                "!And {End At This There,Begin At This Here}.",
                "!Transfer This Self You @@.",
                "Concurrent EndHave Self This BeginHave You This!",
                "More Rate Density This ThisInterval Zero.",
                "And {In This ThisRegion,Not Touch Extent This ThisRegion}.",
                "Not Overlap Extent This ThisRegion.",
                "Before Bite Self This Now.",
                "Before Climb Self This Now.",
                "Before Fall Self Now.",
                "Happen Dodge Self (Attack You Self).",
                "Reflexive Dodge Self.",
                "Happen Jump Self Here.",
                "Before Limp Self Now.",
                "Before Stab Self This Now.",
            ),
        )

    def test_yona_published_world_vocabulary_remains_available(self):
        expected = (
            "System",
            "Skill",
            "Trait",
            "Class",
            "Profession",
            "Dungeon",
            "Dungeon Core",
            "Soul Weapon",
            "Connection",
            "Telepathy",
            "Skill Morph",
            "Skill Merge",
            "Skill Evolution",
            "Path Change",
            "Epithet",
            "First Event",
            "Divine Intuition",
        )
        for sign in expected:
            with self.subTest(sign=sign):
                self.assertTrue(self.yona.new_name_entries(sign))

    def test_pride_and_prejudice_social_semantics_survive_minimization(self):
        self.assert_valid_cases(
            self.core_parser,
            (
                "Love Self This.",
                "Trust Self This.",
                "Respect Self This.",
                "Admire Self This.",
                "GratefulTo Self This.",
                "ShameAbout Self ThisEvent.",
                "More Reputation Self Reputation This.",
                "More Evaluate Self This Evaluate Self You.",
                "High Evaluate Self Move Self Here.",
                "Some p:Entity And {ParentOf $p Self,ParentOf $p This,Not Equal Self This}.",
                "SpouseOf Self This.",
                "EngagedTo Self This.",
                "Own Self This.",
                "Before Say Self (Permitted MoveSelfHere Self) Now.",
                "Before Say Self (Not (Permitted MoveSelfHere Self)) Now.",
                "Happen And {Say Self (Obligated Self (Move Self Here) You) You,Begin (Obligated Self (Move Self Here) You)} ThisInterval.",
                "Before Forgive Self This Now.",
                "Before Say Self (RemorseFor Self) This Now.",
                "Before Say Self (GratefulTo Self This) This Now.",
                "Before Begin Know Self ThisInformation Now.",
                "Before Cause Self Begin Know This ThisInformation Now.",
                "!If (Not Life This) (Cause Self (Believe You (Life This))).",
                "Counterfactual LifeThis MagicThis.",
            ),
        )

    def test_frankenstein_epistemic_causal_and_narrative_semantics_survive_minimization(self):
        self.assert_valid_cases(
            self.core_parser,
            (
                "Intend Self MoveSelfHere.",
                "Plan Self Sequence {Move Self Here,Move Self There}.",
                "And {Before Attempt Self MoveSelfHere Now,Not Before MoveSelfHere Now}.",
                "Before Cause Self Begin Life This Now.",
                "ResponsibleFor Self ThisEvent.",
                "EvidenceFor ThisInformation Life This.",
                "EvidenceFor ThisInformation Not Life This.",
                "Before Begin Know Self ThisInformation Now.",
                "Understand Self ThisInformation.",
                "Remember Self ThisInformation.",
                "Fear Self ThisEvent.",
                "GrieveFor Self ThisEvent.",
                "RemorseFor Self ThisEvent.",
                "CompassionFor Self This.",
                "Hate Self This.",
                "Before Say Self (Believe You (Life This)) You Now.",
                "Counterfactual Before Move Self Here Now Before Life Self Now.",
                "Before Forgive Self This Now.",
            ),
        )

    def test_removed_corpus_convenience_roots_are_not_required(self):
        for surface in (
            "Tell",
            "Ask",
            "See",
            "Hear",
            "Smell",
            "Taste",
            "ChangeBy",
            "Between",
            "Former",
            "Increasing",
            "Decreasing",
            "ApproxEqual",
            "Sometimes",
            "Stop",
            "Teach",
            "Prefer",
            "SiblingOf",
            "PossibleTo",
            "ProbableTo",
            "CertainTo",
            "Injured",
            "Sated",
            "ImportantTo",
            "Continue",
            "Present",
            "Completed",
            "Ongoing",
            "Past",
            "Future",
            "Always",
            "Promise",
            "Detected",
            "Whenever",
            "Because",
            "Almost",
            "Should",
            "Learn",
            "Generic",
            "Teleport",
            "Grab",
            "Consent",
            "Refuse",
            "Deceive",
            "Sever",
            "ChangeRate",
            "OccurrenceRate",
            "Duration",
            "Inside",
            "Outside",
            "Give",
        ):
            with self.subTest(surface=surface):
                self.assertIsNone(self.core.entry(surface))


if __name__ == "__main__":
    unittest.main()
