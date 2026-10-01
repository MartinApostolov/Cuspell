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
        cls.core_parser = Parser(cls.core)
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
        self.assertTrue(self.yona.old_name_entries("HighExtent«MoveInLiquidThing»"))

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
            "«Vision«LifeMatter»Part» This.": "core.anatomy.eye",
            "«Hearing«LifeMatter»Part» This.": "core.anatomy.ear",
            "«Sharp«LifeMatter»Part» This.": "core.anatomy.claw",
            "«HighLength«LifeMatter»Part» This.": "core.anatomy.tail",
            "«VisionThrough«PreventMoveThing»Part» This.": "core.built_environment.window",
            "«Move«GiveLifeMatter»«UseThing»» This.": "core.artifacts.spoon",
        }
        for source, concept_id in cases.items():
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(f"Concept({concept_id})", result.ast.children[0].canonical())

    def test_ordinary_action_roots_parse(self):
        for source in (
            "Before And {Begin Touch Self This,Begin Control Self This} Now.",
            "Before Bite Self This Now.",
            "Before Attack Self This Now.",
            "Before Climb Self This Now.",
            "Before Fall Self Now.",
            "Before Limp Self Now.",
            "Before Stab Self This Now.",
            "Before Cause Self (End Whole This) Now.",
            "Before Eat Self This Now.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)


    def test_residual_ordinary_vocabulary_parses(self):
        for source in (
            "Before Dodge Self Now.",
            "Reflexive Dodge Self.",
            "HighDamage This.",
            "And {Not HighHunger Self,Low Distance HighHunger Self}.",
            "LowHunger Self.",
            "«HearingThing» This.",
            "CamouflagedAgainst This You.",
            "More Hunger This Hunger You.",
            "More Damage This Damage You.",
            "More Extent This @@@ Extent You @@@.",
            "Equal TextureOf This TextureOf You.",
            "More Loudness This Loudness You.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_residual_anatomy_old_names_work_in_semantic_positions(self):
        cases = {
            "«Use«LifeMatter»Part» This.": "core.anatomy.organ",
            "«Eat«Use«LifeMatter»Part»» This.": "core.anatomy.stomach",
            "«Joined«Control«LifeMatter»Part»«LifeMatter»Part» This.": "core.anatomy.wrist",
            "«MoveJoined«LifeMatter»Part» This.": "core.anatomy.tendon",
            "«HighDamage«LifeMatter»Part» This.": "core.anatomy.wound",
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


    def test_historical_religious_and_social_roots_parse(self):
        cases = (
            "Female This.",
            "Before Worship Self This Now.",
        )
        for source in cases:
            with self.subTest(source=source):
                result = self.core_parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_historical_monster_divine_mana_and_meditation_old_names(self):
        cases = {
            "«Attack«Know«MoveLifeThing»»Thing» This.": "core.biology.monster",
            "«WorshipThing» This.": "core.religion.deity",
            "«Female«WorshipThing»» This.": "core.religion.goddess",
            "«Use«WorshipThing»Magic» This.": "core.magic.divine_mana",
            "«AwakeSleep» This.": "core.practice.meditation",
        }
        for source, concept_id in cases.items():
            with self.subTest(source=source):
                result = self.core_parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(f"Concept({concept_id})", result.ast.children[0].canonical())

        self.assertFalse(self.core.new_name_entries("Mana"))
        self.assertTrue(self.core.old_name_entries("Use«WorshipThing»Magic"))
        self.assertTrue(self.yona.new_name_entries("Mana"))
        self.assertTrue(self.yona.old_name_entries("Use«WorshipThing»Magic"))


    def test_ch01_50_system_ontology_is_yona_specific(self):
        for sign in (
            "Title",
            "Named Monster",
            "Named Type",
            "Territory",
            "Dungeon",
            "Dungeon Core",
            "Soul Weapon",
            "Party",
            "Sin Trait",
            "Mental Magic",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["name_kind"], "technical_term")

        for sign in ("Leader", "Hermit", "Infiltrator", "Disaster"):
            with self.subTest(sign=sign):
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["name_kind"], "named_type_value")

    def test_ch01_50_people_places_and_species_are_new_names(self):
        for sign in (
            "Skarn",
            "Lauren",
            "Flarn",
            "Chad",
            "Indarius Pike",
            "Ammasherayalothonathara",
            "Berthariklesionasthitara",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                self.assertEqual(self.yona.new_name_entries(sign)[0]["referent_type"], "Entity")

        for sign in ("Riverfork", "Ryantown", "Triore"):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                self.assertEqual(self.yona.new_name_entries(sign)[0]["referent_type"], "Region")

        for sign in (
            "Gluttonous Feral Fiery Spatial Devourer Thief House Cat",
            "Medusoid",
            "Karkinoid",
            "Crystal Pseudo-Drake",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "species_name")

    def test_ch01_50_class_profession_and_progression_names(self):
        for sign in (
            "Trident Warrior",
            "Beginner Mana Vivitect",
            "Beginner Spatial Mage",
            "Capable Mana Vivitect",
            "Beginner Fire Mana Vivitect",
            "Beginner Space Mana Vivitect",
            "Wannabe Vivitect",
            "Mana Asura",
            "Wannabe Mana Cloner",
            "Beginner Mana Avatar Pilot",
            "Advanced Artillery Mage",
            "Advanced Barrier Mage",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "class_name")

        for sign in ("Taste Tester", "Campfire Cook", "Cook", "Manager", "Carpenter"):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "profession_name")

        self.assertEqual(self.yona.new_name_entries("Mithril")[0]["referent_type"], "OrderedValue")
        self.assertEqual(self.yona.new_name_entries("High")[0]["referent_type"], "OrderedValue")

    def test_ch01_50_skill_trait_and_title_names(self):
        for sign in (
            "Anatomical Blueprint",
            "Phantom Limb Control",
            "Anchor Point",
            "External Mana Manipulation - Anatomical Constructs of the Glutton",
            "Perfect Disguise",
            "Anatomical Analysis",
            "Internal Mana Manipulation - Fleshbender",
            "Timer",
            "Culinary Analysis",
            "Mana Shield",
            "Fire Burst",
            "Spiral Mana Burst",
            "Autonomous Mana Shield",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "skill_name")

        for sign in (
            "Cat-like Reflexes",
            "Nimble",
            "Aura of the Devourer",
            "Homebody",
            "Custom Namecard",
            "Discerning Palate",
            "Diverse Tastes",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "trait_name")

        for sign in (
            "Second Lifer",
            "System Breaker",
            "Nameworthy",
            "Named",
            "Taker of Names I",
            "Dungeon Pioneer I",
            "Dungeon Destroyer I",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "title_name")

    def test_ch01_50_evolution_soul_weapon_and_nickname_names(self):
        for sign in ("Yona, the Devourer", "Yona, the Glutton", "Yona, the Gastronome"):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "evolution_option_name")

        self.assertEqual(
            self.yona.new_name_entries("Gluttonous Greatsword")[0]["name_kind"],
            "soul_weapon_name",
        )
        emma = self.yona.new_name_entries("Emma")
        self.assertTrue(emma)
        self.assertEqual(emma[0]["name_kind"], "nickname")
        self.assertEqual(
            emma[0]["referent_id"],
            "yona.skill.external_anatomical_glutton",
        )


    def test_ch01_50_exact_progression_names_from_fresh_audit(self):
        for sign in (
            "External Mana Manipulation - Greater Anatomical Constructs",
            "External Mana Manipulation - Advanced Anatomical Constructs",
            "External Mana Manipulation - Detailed Anatomical Constructs",
            "External Mana Manipulation - Anatomical Weapons",
            "Greater Detailed Critical Culinary Analysis",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["name_kind"], "skill_upgrade_name")

        for sign in (
            "Devour",
            "Area Scan",
            "Appraise",
            "Heavy Blow",
            "Split Focus",
            "Internal Mana Manipulation",
            "Mana Exoskeleton",
            "Avatar Control",
            "External Mana Manipulation - Brachial Constructs of the Glutton",
            "External Mana Manipulation - Body Constructs of the Glutton",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["name_kind"], "skill_name")

        self.assertEqual(
            self.yona.new_name_entries("Calorie Burner")[0]["name_kind"],
            "trait_name",
        )

    def test_ch01_50_epithets_and_specific_dungeon_names_are_yona_specific(self):
        for sign in ("Ruler of the Shallows", "Bubble Witch"):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "title_name")

        self.assertEqual(
            self.yona.new_name_entries("Rabbit Dungeon")[0]["referent_type"],
            "Region",
        )
        self.assertEqual(
            self.yona.new_name_entries("Rabbit Dungeon Core")[0]["referent_type"],
            "Entity",
        )


    def test_post50_system_terms_remain_yona_specific(self):
        for sign in (
            "Awakened", "Instance", "Field Dungeon", "Tower Dungeon",
            "Challenge Dungeon", "Story Dungeon", "Floor Boss", "Virtue Trait",
            "Path Change", "Epithet", "Skill Morph", "Skill Merge",
            "Skill Evolution", "Dungeon Master", "First Event", "Second Event",
            "Completion Grade", "Trait Selector Token", "Divinity Allotment",
            "Chosen One", "Enlightened Race",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["name_kind"], "technical_term")

    def test_post50_rank_and_affinity_values_are_yona_specific(self):
        for sign in ("Adamantium", "Hero"):
            with self.subTest(sign=sign):
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["referent_type"], "OrderedValue")
                self.assertEqual(entries[0]["name_kind"], "technical_rank_value")
        self.assertEqual(
            self.yona.new_name_entries("Shadow Affinity")[0]["name_kind"],
            "affinity_name",
        )

    def test_post50_classes_and_professions_are_new_names(self):
        for sign in (
            "Beginner Vivitect", "Wannabe Space Vivitect", "Wannabe Fire Vivitect",
            "Beginner Mana Architect", "Wannabe Mana Golemancer",
            "Wannabe Flesh Golemancer", "Wannabe Necromancer",
            "Wannabe Shapeshifter", "Fleshy Horror", "Gluttonous Mana Vivitect",
            "Wannabe Gluttonous Vivitect",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "class_name")
        for sign in (
            "Spell Weaving", "Lazy Cook", "Hungry Cook", "Sous Chef",
            "Experienced Taste Tester", "Lazy Manager", "Automated Cook",
            "Exotic Chef", "Royal Inspector",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "profession_name")

    def test_post50_skills_are_yona_specific(self):
        for sign in (
            "Possess", "Snatch of the Glutton", "Mana Infusion", "Auto-Mix",
            "Flesh Stitching", "Create Golem Core", "Fleshshaped Constructs",
            "Fleshshaped Constructs of the Glutton", "Anatomical Synthesis",
            "Flesh Weaving", "Charged Spatial Slice", "Dungeon of the Glutton",
            "Devour of the Glutton", "Multisnatch of the Glutton", "Greater Blink",
            "Fireball", "Compositional Culinary Analysis",
            "Compressed Autonomous Mana Shield", "Compressed Spiral Mana Burst",
            "Auto-Cook", "Appoint", "Connection", "Telepathy", "Water Portal",
        ):
            with self.subTest(sign=sign):
                self.assertFalse(self.core.new_name_entries(sign))
                entries = self.yona.new_name_entries(sign)
                self.assertTrue(entries)
                self.assertEqual(entries[0]["name_kind"], "skill_name")

    def test_telepathy_stays_a_yona_skill_not_a_core_history_decision(self):
        self.assertFalse(self.core.new_name_entries("Telepathy"))
        self.assertFalse(self.core.old_name_entries("Telepathy"))
        entries = self.yona.new_name_entries("Telepathy")
        self.assertTrue(entries)
        self.assertEqual(entries[0]["referent_id"], "yona.skill.telepathy")
        self.assertEqual(entries[0]["name_kind"], "skill_name")

    def test_post50_traits_and_titles_are_yona_specific(self):
        for sign in (
            "H4rm0n10u5", "Temperance", "Delusional",
            "Aura of Delusional Temperance", "Poison Resistance", "Devourer",
            "True Wrath", "Extreme Spatial Affinity", "Royal Dignity",
            "Royal Bearing", "Traceless", "Stealthy", "Culinary Instincts",
            "Gastronome", "Compression", "Malleable", "Compatible", "Lucky",
            "Synchronicity", "Divine Intuition",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "trait_name")
        for sign in (
            "Taker of Names II", "Taker of Names III", "Taker of Names IV",
            "System Breaker II", "Princess", "Renowned", "Dungeon Destroyer II",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "title_name")

    def test_post50_soul_weapons_and_rewards_are_yona_specific(self):
        for sign in (
            "Terror Blade", "Scepter of the Temperant Idol",
            "Winter's Pistol", "The Avaricious Hunter",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "soul_weapon_name")
        for sign in (
            "Treasure Map (I)", "Treasure Map (IV)", "Treasure Map Upgrade (IV)",
            "Trait Selector Token (Epic)", "Readjusted Divinity Allotment",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "system_reward_name")

    def test_post50_people_places_species_and_epithet_forms_resolve(self):
        for sign in (
            "Melinda", "Francis", "Joshua", "Damien", "Illiana", "Annalise",
            "Joakim", "Arianne Fenn", "Cecilia", "Foundri", "Jeanne", "Lacey",
            "Wesley", "Sebastien", "Zorg", "Metztli", "Fenlith", "Sasha",
            "Herman", "Mac", "Altair", "Jane", "Seria", "Limos", "Menyar",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["referent_type"], "Entity")
        for sign in ("Tarnton", "Pig Palace", "Dryadil", "Eryndell", "Ocula", "Ahuitl Ruins"):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["referent_type"], "Region")
        for sign in ("Shade", "Wraith", "Revenant", "Carnivorous Mussel Swarm", "Child of Limos"):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "species_name")
        for sign in (
            "Annalise, First Blade of Joakim", "Wesley, Defender of Eryndell",
            "Sebastien, the Swamp Butler", "Fenlith, Immortal Herald of Limos",
            "Metztli, Disciple of Limos", "Sasha the Sensitive",
            "Mac, the Diligent Hydromancer", "Altair of the Burning Wrath",
        ):
            with self.subTest(sign=sign):
                self.assertEqual(self.yona.new_name_entries(sign)[0]["name_kind"], "epithet_name")


if __name__ == "__main__":
    unittest.main()
