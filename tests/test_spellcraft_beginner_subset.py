from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]
COVERAGE_MANIFEST = ROOT / "language" / "subsets" / "spellcraft_beginner_v0_1.json"
BEGINNER_MANIFEST = ROOT / "language" / "subsets" / "spellcraft_progression_v1.json"


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

    def test_course_boundaries_split_18_24_29(self):
        boundaries = self.data["course_boundaries"]
        self.assertEqual(boundaries["beginner"]["semantic_count"], 18)
        self.assertEqual(boundaries["intermediate"]["semantic_count"], 24)
        self.assertEqual(boundaries["advanced"]["semantic_count"], 29)
        self.assertEqual(
            boundaries["beginner"]["includes_modules"],
            [
                "attribute_light",
                "fresh_creation",
                "duration_maintenance",
                "exact_prevention",
            ],
        )
        self.assertEqual(
            boundaries["intermediate"]["includes_modules"],
            [
                "shared_visual_representation",
                "state_conjunction",
                "event_ordering_and_concurrency",
                "finite_repetition",
            ],
        )
        self.assertEqual(
            boundaries["advanced"]["includes_modules"],
            [
                "bounded_multitarget_distribution",
                "simple_trigger",
                "relative_time_flow",
            ],
        )

    def test_module_course_levels_are_monotonic(self):
        expected = [
            "beginner", "beginner", "beginner", "beginner",
            "intermediate", "intermediate", "intermediate", "intermediate",
            "advanced", "advanced", "advanced",
        ]
        self.assertEqual(
            [module["course_level"] for module in self.data["modules"]],
            expected,
        )

    def test_every_module_example_uses_only_already_introduced_registered_signs(self):
        available = set(self.data["core"]["entries"])
        for module in self.data["modules"]:
            available.update(module["add_entries"])
            for example in module["spells"]:
                source = example["cuspell"]
                with self.subTest(module=module["id"], source=source):
                    used = self.registered_names_in(source)
                    self.assertLessEqual(used, available, (used - available, source))

    def test_beginner_boundary_stops_before_general_composition(self):
        beginner = set(self.data["course_boundaries"]["beginner"]["includes_modules"])
        self.assertNotIn("shared_visual_representation", beginner)
        self.assertNotIn("state_conjunction", beginner)
        self.assertNotIn("event_ordering_and_concurrency", beginner)
        self.assertNotIn("finite_repetition", beginner)
        self.assertNotIn("bounded_multitarget_distribution", beginner)
        self.assertNotIn("simple_trigger", beginner)
        self.assertNotIn("relative_time_flow", beginner)

    def test_advanced_boundary_contains_nested_binders_watchers_and_timeflow(self):
        advanced = set(self.data["course_boundaries"]["advanced"]["includes_modules"])
        self.assertEqual(
            advanced,
            {
                "bounded_multitarget_distribution",
                "simple_trigger",
                "relative_time_flow",
            },
        )

    def test_module_progression_stays_small_and_cumulative(self):
        modules = self.data["modules"]
        self.assertEqual(
            [module["id"] for module in modules],
            [
                "attribute_light",
                "fresh_creation",
                "duration_maintenance",
                "exact_prevention",
                "shared_visual_representation",
                "state_conjunction",
                "event_ordering_and_concurrency",
                "finite_repetition",
                "bounded_multitarget_distribution",
                "simple_trigger",
                "relative_time_flow",
            ],
        )
        self.assertEqual(
            [module["cumulative_semantic_count"] for module in modules],
            [13, 15, 17, 18, 20, 21, 23, 24, 27, 28, 29],
        )
        self.assertEqual(
            [module["add_entries"] for module in modules],
            [
                ["Change", "Light"],
                ["At", "Create"],
                ["ThisInterval", "Persist"],
                ["Prevent"],
                ["Vision", "Represent"],
                ["And"],
                ["Sequence", "Concurrent"],
                ["Repeat"],
                ["Collect", "Member", "Each"],
                ["Trigger"],
                ["TimeFlow"],
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

    def test_shared_representation_module_adds_only_vision_and_represent(self):
        module = self.data["modules"][4]
        self.assertEqual(module["id"], "shared_visual_representation")
        self.assertEqual(module["add_entries"], ["Vision", "Represent"])
        self.assertEqual(module["cumulative_semantic_count"], 20)
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            [
                "Begin Represent This You Vision!",
                "End Represent This You Vision!",
                "Persist Represent This You Vision ThisInterval!",
                "Create i:Entity At $i There Begin Represent $i This Vision!",
            ],
        )
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_shared_representation_reuses_existing_begin_end_persist_and_create(self):
        module = self.data["modules"][4]
        sources = {example["cuspell"] for example in module["spells"]}
        self.assertIn("Begin Represent This You Vision!", sources)
        self.assertIn("End Represent This You Vision!", sources)
        self.assertIn("Persist Represent This You Vision ThisInterval!", sources)
        created = "Create i:Entity At $i There Begin Represent $i This Vision!"
        self.assertIn(created, sources)
        result = self.parser.check(created)
        self.assertTrue(result.valid, result.diagnostics)
        canonical = result.ast.children[0].canonical()
        self.assertIn("Create(", canonical)
        self.assertIn("continuation=Begin", canonical)
        self.assertIn("Represent", canonical)

    def test_shared_representation_does_not_require_sense_sign_or_conjunction(self):
        module = self.data["modules"][4]
        module_entries = set(module["add_entries"])
        self.assertTrue({"Sense", "Sign", "And", "Hearing", "TouchChannel"}.isdisjoint(module_entries))
        for example in module["spells"]:
            source = example["cuspell"]
            self.assertNotIn("Sense ", source)
            self.assertNotIn(" And ", source)
            self.assertNotIn("Sign ", source)

    def test_represent_is_not_forced_sense_or_truth(self):
        represented = self.parser.check("Begin Represent This You Vision!")
        sensed = self.parser.check("Sense Self Vision This!")
        self.assertTrue(represented.valid, represented.diagnostics)
        self.assertTrue(sensed.valid, sensed.diagnostics)
        self.assertNotEqual(
            represented.ast.children[0].canonical(),
            sensed.ast.children[0].canonical(),
        )
        scope = self.data["modules"][4]["teaching_scope"]
        self.assertIn("does not force any observer", scope)
        self.assertIn("physically present or true", scope)

    def test_and_module_teaches_state_conjunction_before_event_and(self):
        module = self.data["modules"][5]
        self.assertEqual(module["id"], "state_conjunction")
        self.assertEqual(module["add_entries"], ["And"])
        self.assertEqual(module["cumulative_semantic_count"], 21)
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            [
                "Find Self This Whole This And Magic This!",
                "Create i:Entity At $i There And Magic $i Begin Represent $i This Vision!",
            ],
        )
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
            self.assertIn("And", result.ast.children[0].canonical())
        self.assertIn("event-level And composites", module["teaching_scope"])

    def test_sequence_and_concurrent_are_taught_as_a_contrastive_pair(self):
        module = self.data["modules"][6]
        self.assertEqual(module["id"], "event_ordering_and_concurrency")
        self.assertEqual(module["add_entries"], ["Sequence", "Concurrent"])
        self.assertEqual(module["cumulative_semantic_count"], 23)
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            [
                "Sequence Move This There Begin Magic This!",
                "Concurrent Move This There Begin Magic You!",
            ],
        )
        parsed = []
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
            parsed.append(result.ast.children[0].canonical())
        self.assertIn("Sequence", parsed[0])
        self.assertIn("Concurrent", parsed[1])
        self.assertNotEqual(parsed[0], parsed[1])

    def test_sequence_repairs_previous_programming_candidate_omission(self):
        module_entries = {
            entry
            for module in self.data["modules"][5:]
            for entry in module["add_entries"]
        }
        self.assertIn("Sequence", module_entries)
        self.assertIn("Concurrent", module_entries)
        rationale = self.data["modules"][6]["rationale"]
        self.assertIn("accidentally omitted Sequence", rationale)

    def test_repeat_module_is_finite_and_reuses_create(self):
        module = self.data["modules"][7]
        self.assertEqual(module["id"], "finite_repetition")
        self.assertEqual(module["add_entries"], ["Repeat"])
        self.assertEqual(module["cumulative_semantic_count"], 24)
        source = module["spells"][0]["cuspell"]
        self.assertEqual(
            source,
            "Repeat @@@ Create x:Entity At $x There Change $x Light «LightUnit» @!",
        )
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        canonical = result.ast.children[0].canonical()
        self.assertIn("Repeat(", canonical)
        self.assertIn("Create(", canonical)
        self.assertIn("No unbounded loop", module["teaching_scope"])

    def test_multitarget_module_requires_collect_member_and_each_together(self):
        module = self.data["modules"][8]
        self.assertEqual(module["id"], "bounded_multitarget_distribution")
        self.assertEqual(module["add_entries"], ["Collect", "Member", "Each"])
        self.assertEqual(module["cumulative_semantic_count"], 27)
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            [
                "Each Collect x:Entity Member $x This y:Entity Begin Magic $y!",
                "Each Collect x:Entity Member $x This y:Entity Change $y Light «LightUnit» @!",
            ],
        )
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
            canonical = result.ast.children[0].canonical()
            self.assertIn("Each(", canonical)
            self.assertIn("Collect(", canonical)
            self.assertIn("Member", canonical)

    def test_multitarget_collection_is_explicitly_bounded_not_omniscient(self):
        module = self.data["modules"][8]
        requirements = " ".join(module["context_requirements"])
        self.assertIn("group membership is objectively resolvable", requirements)
        self.assertIn("does not grant omniscient world search", requirements)
        scope = module["teaching_scope"]
        self.assertIn("No singular Process silently applies", scope)

    def test_trigger_module_teaches_only_simple_one_shot_watcher(self):
        module = self.data["modules"][9]
        self.assertEqual(module["id"], "simple_trigger")
        self.assertEqual(module["add_entries"], ["Trigger"])
        self.assertEqual(module["cumulative_semantic_count"], 28)
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            [
                "Trigger Locked This End Locked This ThisInterval!",
                "Trigger Magic This End Magic This ThisInterval!",
            ],
        )
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
            canonical = result.ast.children[0].canonical()
            self.assertIn("Trigger(", canonical)
            self.assertNotIn("binder=", canonical)
        self.assertIn("one-shot by default", module["teaching_scope"])

    def test_bound_trigger_remains_advanced(self):
        module_sources = {
            example["cuspell"]
            for module in self.data["modules"]
            for example in module["spells"]
        }
        advanced = "Trigger x:Entity Locked $x End Locked $x ThisInterval!"
        self.assertNotIn(advanced, module_sources)
        result = self.parser.check(advanced)
        self.assertTrue(result.valid, result.diagnostics)

    def test_timeflow_module_adds_only_timeflow(self):
        module = self.data["modules"][10]
        self.assertEqual(module["id"], "relative_time_flow")
        self.assertEqual(module["add_entries"], ["TimeFlow"])
        self.assertEqual(module["cumulative_semantic_count"], 29)
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertEqual(
            sources,
            [
                "Persist TimeFlow You Self @@ ThisInterval!",
                "Persist TimeFlow Self You @@ ThisInterval!",
            ],
        )
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
            canonical = result.ast.children[0].canonical()
            self.assertIn("Persist(", canonical)
            self.assertIn("TimeFlow", canonical)

    def test_timeflow_reference_is_explicit_and_not_repeat_or_rate(self):
        module = self.data["modules"][10]
        sources = [example["cuspell"] for example in module["spells"]]
        self.assertIn("TimeFlow You Self @@", sources[0])
        self.assertIn("TimeFlow Self You @@", sources[1])
        for source in sources:
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)
            canonical = result.ast.children[0].canonical()
            self.assertNotIn("Repeat(", canonical)
            self.assertNotIn("Rate(", canonical)
        incomplete = self.parser.check("Persist TimeFlow You @@ ThisInterval!")
        self.assertFalse(incomplete.valid)

    def test_zero_and_divide_are_optional_timeflow_extensions(self):
        required = set(self.data["core"]["entries"])
        for module in self.data["modules"]:
            required.update(module["add_entries"])
        self.assertNotIn("Zero", required)
        self.assertNotIn("Divide", required)
        optional = {item["entry"]: item for item in self.data["optional_vocabulary"]}
        self.assertIn("Zero", optional)
        self.assertIn("Divide", optional)
        for entry in ("Zero", "Divide"):
            source = optional[entry]["example"]
            result = self.parser.check(source)
            self.assertTrue(result.valid, result.diagnostics)

    def test_timeflow_does_not_smuggle_time_reversal(self):
        result = self.parser.check(
            "Persist TimeFlow You Self Opposite @ ThisInterval!"
        )
        self.assertFalse(result.valid)
        scope = self.data["modules"][10]["teaching_scope"]
        self.assertIn("not Repeat", scope)
        advanced = self.data["deferred_modules"][0]["note"]
        self.assertIn("time-reversal", advanced)

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
