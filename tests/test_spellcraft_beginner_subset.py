from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MANIFEST = ROOT / "language" / "subsets" / "spellcraft_beginner_v0_1.json"
BEGINNER_MANIFEST = ROOT / "language" / "subsets" / "spellcraft_beginner_v0_4.json"


def walk(node):
    yield node
    for child in node.children:
        yield from walk(child)


class SpellcraftCoverageProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.data = json.loads(COVERAGE_MANIFEST.read_text(encoding="utf-8"))

    def test_projection_is_50_signs_and_cumulative(self):
        tiers = self.data["tiers"]
        flattened = []
        for tier in (
            "direct_manipulation",
            "persistent_and_protective",
            "transformation_and_programming",
            "fresh_creation",
        ):
            flattened.extend(tiers[tier]["entries"])
        self.assertEqual(flattened, self.data["entries"])
        self.assertEqual(len(flattened), len(set(flattened)))
        self.assertEqual(len(flattened), 50)
        self.assertLess(len(flattened), len(self.language.entries) // 4)

    def test_all_projection_entries_are_current_registered_signs(self):
        missing = [
            surface
            for surface in self.data["entries"]
            if self.language.entry(surface) is None
        ]
        self.assertEqual(missing, [])

    def test_projection_old_names_exist(self):
        for sign in self.data["starter_old_names"]:
            with self.subTest(sign=sign):
                self.assertTrue(self.language.old_name_entries(sign))

    def test_reference_effects_are_level_zero_through_two_only(self):
        levels = {example["level"] for example in self.data["reference_effects"]}
        self.assertEqual(levels, {0, 1, 2})
        self.assertEqual(len(self.data["reference_effects"]), 48)

    def test_reference_effect_spell_names_are_unique(self):
        names = [example["spell"] for example in self.data["reference_effects"]]
        self.assertEqual(len(names), len(set(names)))

    def test_coverage_examples_do_not_require_parentheses(self):
        failures = [
            (example["spell"], example["cuspell"])
            for example in self.data["reference_effects"]
            if "(" in example["cuspell"] or ")" in example["cuspell"]
        ]
        self.assertEqual(failures, [])

    def test_all_coverage_examples_parse_as_commands(self):
        for example in self.data["reference_effects"]:
            source = example["cuspell"]
            with self.subTest(spell=example["spell"], source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_post_create_repairs_keep_distinct_spell_meanings_distinct(self):
        by_name = {
            example["spell"]: example["cuspell"]
            for example in self.data["reference_effects"]
        }
        self.assertIn("Create", by_name["Light"])
        self.assertNotEqual(by_name["Light"], by_name["Faerie Fire"])
        self.assertIn("Each Collect", by_name["Faerie Fire"])
        self.assertIn("Create", by_name["Magic Missile"])
        self.assertIn("Create", by_name["Find Familiar"])

    def test_remaining_exact_duplicate_recipes_are_explicitly_intentional(self):
        recipes: dict[str, set[str]] = {}
        for example in self.data["reference_effects"]:
            recipes.setdefault(example["cuspell"], set()).add(example["spell"])
        duplicates = {
            recipe: names
            for recipe, names in recipes.items()
            if len(names) > 1
        }
        expected = {
            "Change This Heat Add BeforeValue Heat This «HeatUnit» @!": {
                "Fire Bolt",
                "Prestidigitation",
                "Heat Metal",
            },
            "Move This There!": {
                "Mage Hand",
                "Thunderwave",
                "Gust of Wind",
            },
            "Change You Health Health Self!": {
                "Cure Wounds",
                "Healing Word",
            },
            "Change Self Form Form This!": {
                "Disguise Self",
                "Alter Self",
                "Enlarge/Reduce",
            },
            "Begin CanYouMoveYouThere!": {
                "Longstrider",
                "Enhance Ability",
            },
            "Prevent SenseThisVisionYou ThisInterval!": {
                "Invisibility",
                "Pass without Trace",
            },
        }
        self.assertEqual(duplicates, expected)


class SpellcraftBeginnerStressTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.data = json.loads(BEGINNER_MANIFEST.read_text(encoding="utf-8"))

    def registered_names_in(self, source: str) -> set[str]:
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        names = set()
        for node in walk(result.ast):
            if node.name and self.language.entry(node.name) is not None:
                names.add(node.name)
        return names

    def test_core_is_11_signs_in_three_clean_steps(self):
        tiers = self.data["core"]["tiers"]
        flattened = []
        counts = []
        for tier in (
            "first_actions",
            "reusable_state_vocabulary",
            "bounded_discovery",
        ):
            flattened.extend(tiers[tier]["entries"])
            counts.append(tiers[tier]["cumulative_count"])
        self.assertEqual(flattened, self.data["core"]["entries"])
        self.assertEqual(len(flattened), len(set(flattened)))
        self.assertEqual(len(flattened), 11)
        self.assertEqual(counts, [6, 9, 11])

    def test_all_core_and_module_entries_are_registered(self):
        surfaces = list(self.data["core"]["entries"])
        for module in self.data["modules"]:
            surfaces.extend(module["add_entries"])
        missing = [
            surface for surface in surfaces if self.language.entry(surface) is None
        ]
        self.assertEqual(missing, [])

    def test_each_core_spell_uses_only_signs_available_at_its_step(self):
        tier_entries = []
        available_by_count = {}
        for tier in (
            self.data["core"]["tiers"]["first_actions"],
            self.data["core"]["tiers"]["reusable_state_vocabulary"],
            self.data["core"]["tiers"]["bounded_discovery"],
        ):
            tier_entries.extend(tier["entries"])
            available_by_count[tier["cumulative_count"]] = set(tier_entries)

        for example in self.data["core"]["starter_spells"]:
            source = example["cuspell"]
            with self.subTest(name=example["name"], source=source):
                used = self.registered_names_in(source)
                allowed = available_by_count[example["introduced_at"]]
                self.assertLessEqual(used, allowed, (used, allowed))

    def test_every_core_sign_is_used_by_the_core_spellbook(self):
        used = set()
        for example in self.data["core"]["starter_spells"]:
            used |= self.registered_names_in(example["cuspell"])
        self.assertEqual(used, set(self.data["core"]["entries"]))

    def test_state_vocabulary_reuses_begin_end_and_find_uniformly(self):
        by_source = {
            example["cuspell"]
            for example in self.data["core"]["starter_spells"]
        }
        for state in ("Whole", "Locked", "Magic"):
            with self.subTest(state=state):
                self.assertIn(f"Begin {state} This!", by_source)
                self.assertIn(f"End {state} This!", by_source)
                self.assertIn(f"Find Self This {state} This!", by_source)

    def test_magic_replaces_ill_in_the_semantic_core(self):
        self.assertIn("Magic", self.data["core"]["entries"])
        self.assertNotIn("Ill", self.data["core"]["entries"])
        optional = {item["entry"] for item in self.data["optional_vocabulary"]}
        self.assertIn("Ill", optional)

    def test_find_is_yes_no_only_in_the_core(self):
        find_examples = [
            example["cuspell"]
            for example in self.data["core"]["starter_spells"]
            if example["pattern"] == "find-yes-no"
        ]
        self.assertEqual(len(find_examples), 3)
        self.assertTrue(all(":" not in source for source in find_examples))
        self.assertTrue(all("$" not in source for source in find_examples))

    def test_core_stays_flat_and_defers_advanced_control(self):
        forbidden = {
            "And", "Repeat", "Concurrent", "Each", "Collect", "Member",
            "Trigger", "Persist", "Prevent", "Represent", "TimeFlow",
            "Create", "Change", "At", "Light",
        }
        self.assertTrue(forbidden.isdisjoint(self.data["core"]["entries"]))
        for example in self.data["core"]["starter_spells"]:
            source = example["cuspell"]
            self.assertNotIn("(", source)
            self.assertNotIn(")", source)
            self.assertNotIn(":", source)
            self.assertNotIn("$", source)
            self.assertNotIn("«", source)
            self.assertNotIn("@", source)

    def test_light_attribute_module_adds_only_two_semantic_signs(self):
        module = self.data["modules"][0]
        self.assertEqual(module["id"], "attribute_light")
        self.assertEqual(module["add_entries"], ["Change", "Light"])
        self.assertEqual(module["cumulative_semantic_count"], 13)
        self.assertEqual(module["starter_old_names"], ["LightUnit"])
        self.assertTrue(self.language.old_name_entries("LightUnit"))
        for example in module["spells"]:
            result = self.parser.check(example["cuspell"])
            self.assertTrue(result.valid, result.diagnostics)

    def test_creation_module_adds_only_at_and_create_then_reuses_light(self):
        module = self.data["modules"][1]
        self.assertEqual(module["id"], "fresh_creation")
        self.assertEqual(module["add_entries"], ["At", "Create"])
        self.assertEqual(module["cumulative_semantic_count"], 15)
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            ["Create x:Entity At $x There Change $x Light «LightUnit» @!"],
        )
        result = self.parser.check(sources[0])
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn("continuation=", result.ast.children[0].canonical())

    def test_here_is_convenience_not_a_hidden_creation_prerequisite(self):
        required = set(self.data["core"]["entries"])
        for module in self.data["modules"]:
            required.update(module["add_entries"])
        self.assertNotIn("Here", required)
        optional = {item["entry"] for item in self.data["optional_vocabulary"]}
        self.assertIn("Here", optional)
        create_source = self.data["modules"][1]["spells"][0]["cuspell"]
        self.assertIn("There", create_source)
        self.assertNotIn("Here", create_source)

    def test_module_progression_stays_small_and_cumulative(self):
        modules = self.data["modules"]
        self.assertEqual(
            [module["id"] for module in modules],
            [
                "attribute_light",
                "fresh_creation",
                "duration_maintenance",
                "exact_prevention",
            ],
        )
        self.assertEqual(
            [module["cumulative_semantic_count"] for module in modules],
            [13, 15, 17, 18],
        )
        self.assertEqual(
            [module["add_entries"] for module in modules],
            [
                ["Change", "Light"],
                ["At", "Create"],
                ["ThisInterval", "Persist"],
                ["Prevent"],
            ],
        )

    def test_duration_module_reuses_known_state_propositions(self):
        module = self.data["modules"][2]
        self.assertEqual(module["id"], "duration_maintenance")
        self.assertEqual(module["add_entries"], ["ThisInterval", "Persist"])
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            [
                "Persist Whole This ThisInterval!",
                "Persist Locked This ThisInterval!",
                "Persist Magic This ThisInterval!",
            ],
        )
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
            canonical = result.ast.children[0].canonical()
            self.assertIn("Persist(", canonical)
            self.assertIn("duration=ThisInterval", canonical)

    def test_duration_module_does_not_hide_an_infinite_default(self):
        module = self.data["modules"][2]
        requirements = " ".join(module["context_requirements"])
        self.assertIn("objectively designated TimeInterval", requirements)
        self.assertIn("does not mean forever", requirements)
        result = self.parser.check("Persist Whole This!")
        self.assertFalse(result.valid)

    def test_prevention_module_teaches_only_simple_exact_event_form(self):
        module = self.data["modules"][3]
        self.assertEqual(module["id"], "exact_prevention")
        self.assertEqual(module["add_entries"], ["Prevent"])
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            [
                "Prevent Move This There ThisInterval!",
                "Prevent End Whole This ThisInterval!",
                "Prevent Begin Locked This ThisInterval!",
            ],
        )
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
            canonical = result.ast.children[0].canonical()
            self.assertIn("Prevent(", canonical)
            self.assertIn("scope=ThisInterval", canonical)
            self.assertNotIn("binder=", canonical)
            self.assertNotIn("region=", canonical)

    def test_bound_antimagic_prevent_remains_outside_beginner_module(self):
        module_sources = {
            example["cuspell"]
            for module in self.data["modules"]
            for example in module["spells"]
        }
        advanced = "Prevent e:EventSpec Magic $e _ ThisInterval!"
        self.assertNotIn(advanced, module_sources)
        result = self.parser.check(advanced)
        self.assertTrue(result.valid, result.diagnostics)

    def test_all_required_examples_parse(self):
        sources = [
            example["cuspell"]
            for example in self.data["core"]["starter_spells"]
        ]
        for module in self.data["modules"]:
            sources.extend(example["cuspell"] for example in module["spells"])
        for source in sources:
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)


if __name__ == "__main__":
    unittest.main()
