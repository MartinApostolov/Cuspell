from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class YonaVocabularyPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = Language.load(ROOT)
        cls.yona = Language.load(ROOT, world_package="yona")
        cls.parser = Parser(cls.yona)

    def test_all_language_and_world_packages_validate(self):
        self.assertEqual(validate_language_data(ROOT), [])

    def test_yona_package_is_opt_in(self):
        self.assertIsNone(self.core.world_concept("yona.species.ichthyoid"))
        self.assertFalse(self.core.new_name_entries("Ichthyoid"))
        self.assertIsNotNone(self.yona.world_concept("yona.species.ichthyoid"))
        self.assertTrue(self.yona.new_name_entries("Ichthyoid"))

    def test_yona_package_keeps_core_civilization_vocabulary(self):
        self.assertIsNotNone(self.yona.world_concept("core.transport.ship"))
        self.assertTrue(self.yona.old_name_entries("Big«MoveInLiquidThing»"))

    def test_specialized_system_words_are_new_names(self):
        for sign in (
            "System",
            "Quest",
            "Skill",
            "Trait",
            "Class",
            "Profession",
            "Species",
            "Affinity",
            "Level",
            "Tier",
            "Proficiency",
            "Stage",
            "Evolution",
            "Mana",
        ):
            with self.subTest(sign=sign):
                self.assertTrue(self.yona.new_name_entries(sign))
                self.assertFalse(self.yona.old_name_entries(sign))

    def test_named_species_are_new_names(self):
        for sign in ("Ichthyoid", "Encheloid", "Octopoid", "House Cat"):
            with self.subTest(sign=sign):
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["referent_type"], "Kind")

    def test_named_skills_are_new_names(self):
        for sign in (
            "Scratch",
            "Food Sense",
            "Stomach of the Glutton",
            "Blink",
            "Snatch",
            "External Mana Manipulation",
            "Mana Barrier",
            "Mana Burst",
        ):
            with self.subTest(sign=sign):
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["name_kind"], "skill_name")

    def test_person_names_are_new_names(self):
        for sign in ("Yona", "Abby", "Sally", "Henry", "Ryan"):
            with self.subTest(sign=sign):
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["referent_type"], "Entity")

    def test_new_ordinary_old_names_work_in_semantic_positions(self):
        cases = {
            "«VisionBodyPart» This.": "core.anatomy.eye",
            "«HearingBodyPart» This.": "core.anatomy.ear",
            "«SharpBodyPart» This.": "core.anatomy.claw",
            "«LongBodyPart» This.": "core.anatomy.tail",
            "«SeeThrough«PreventMoveThing»Part» This.": "core.built_environment.window",
            "«Move«GiveLifeMatter»«UseThing»» This.": "core.artifacts.spoon",
        }
        for source, concept_id in cases.items():
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(f"Concept({concept_id})", result.ast.children[0].canonical())

    def test_ordinary_action_roots_parse(self):
        for source in (
            "Past Grab Self This.",
            "Past Bite Self This.",
            "Past Attack Self This.",
            "Past Climb Self This.",
            "Past Fall Self.",
            "Past Limp Self.",
            "Past Stab Self This.",
            "Past Sever Self This.",
            "Past Eat Self This.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)


    def test_residual_ordinary_vocabulary_parses(self):
        for source in (
            "Past Dodge Self.",
            "Reflexive Dodge Self.",
            "Injured This.",
            "Almost Hungry Self.",
            "Sated Self.",
            "Sound This.",
            "CamouflagedAgainst This You.",
            "More Hunger This Hunger You.",
            "More Damage This Damage You.",
            "More Depth This Depth You.",
            "Equal TextureOf This TextureOf You.",
            "More Loudness This Loudness You.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_residual_anatomy_old_names_work_in_semantic_positions(self):
        cases = {
            "«UseBodyPart» This.": "core.anatomy.organ",
            "«Eat«UseBodyPart»» This.": "core.anatomy.stomach",
            "«JoinHandBodyPart» This.": "core.anatomy.wrist",
            "«MoveJoinBodyPart» This.": "core.anatomy.tendon",
            "«InjuredBodyPart» This.": "core.anatomy.wound",
        }
        for source, concept_id in cases.items():
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(f"Concept({concept_id})", result.ast.children[0].canonical())


    def test_yona_threat_rank_values_are_new_names(self):
        expected = {
            "Bronze": "yona.threat_rank.bronze",
            "Silver": "yona.threat_rank.silver",
            "Gold": "yona.threat_rank.gold",
            "Platinum": "yona.threat_rank.platinum",
        }
        for sign, concept_id in expected.items():
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["referent_type"], "OrderedValue")
                self.assertEqual(entries[0]["name_kind"], "technical_rank_value")
                self.assertEqual(entries[0]["referent_id"], concept_id)

    def test_named_evolution_options_are_yona_specific_new_names(self):
        for sign in (
            "Greater Spatial House Cat",
            "Gluttonous House Cat",
            "Slothful House Cat",
            "Spatial Thief House Cat",
            "Gluttonous Devourer House Cat",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["referent_type"], "Kind")
                self.assertEqual(entries[0]["name_kind"], "evolution_option_name")

    def test_ch15_skill_upgrades_are_yona_specific_new_names(self):
        self.assertTrue(self.yona.new_name_entries("Meditate"))
        self.assertFalse(self.core.new_name_entries("Meditate"))
        for sign in (
            "External Mana Manipulation - Constructs",
            "External Mana Manipulation - Anatomical Constructs",
            "External Mana Manipulation - Equipment Constructs",
            "External Mana Manipulation - Fire",
            "Meditate - Deep",
            "Meditate - Alert",
            "Meditate - Split",
            "Meditate - Efficient",
            "Meditate - Sensitive",
            "Meditate - Precise",
            "Meditate of the Glutton",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["referent_type"], "Kind")
                self.assertEqual(entries[0]["name_kind"], "skill_upgrade_name")


if __name__ == "__main__":
    unittest.main()
