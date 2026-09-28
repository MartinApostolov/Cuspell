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


if __name__ == "__main__":
    unittest.main()
