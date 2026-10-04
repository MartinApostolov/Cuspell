from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class TypedWorldKindClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def binder(self, source: str):
        node = self.parser.parse_phrase(source, expected_type="Binder")
        self.assertNotIsInstance(node, Diagnostic, node)
        return node

    def test_default_entity_classification_needs_no_redundant_metadata(self):
        temple = self.language.world_concepts["core.religion.temple"]
        self.assertNotIn("classifies_types", temple)
        self.assertEqual(
            self.language.world_kind_classifies_types("core.religion.temple"),
            ("Entity",),
        )
        binder = self.binder("t:«Worship«JoinedInThing»»")
        self.assertEqual(binder.meta_dict().get("bound_type"), "Entity")

    def test_single_domain_named_kind_binders_use_classifier_type(self):
        story = self.binder("s:«Sequence«MeaningSign»»")
        day = self.binder("d:«AwakeSleepExtent»")
        self.assertEqual(story.meta_dict().get("bound_type"), "Information")
        self.assertEqual(day.meta_dict().get("bound_type"), "TimeInterval")

        story_question = self.parser.check(
            "s:«Sequence«MeaningSign»» Equal $s ThisInformation?"
        )
        day_question = self.parser.check(
            "d:«AwakeSleepExtent» Equal $d ThisInterval?"
        )
        self.assertTrue(story_question.valid, story_question.diagnostics)
        self.assertTrue(day_question.valid, day_question.diagnostics)

    def test_multi_domain_named_kind_binder_requires_explicit_semantic_type(self):
        node = self.parser.parse_phrase(
            "r:«RuleSequence»",
            expected_type="Binder",
        )
        self.assertIsInstance(node, Diagnostic)
        self.assertEqual(node.code, "AmbiguousKindDomain")
        self.assertIn("EventSpec", node.message)
        self.assertIn("Event", node.message)

    def test_core_explicit_classifier_metadata_is_only_non_default_domains(self):
        expected = {
            "core.events.ritual": ("EventSpec", "Event"),
            "core.events.prayer": ("EventSpec", "Event"),
            "core.events.sacrifice": ("EventSpec", "Event"),
            "core.events.dance": ("EventSpec", "Event"),
            "core.events.performance": ("EventSpec", "Event"),
            "core.events.game": ("EventSpec", "Event"),
            "core.events.festival": ("EventSpec", "Event"),
            "core.information.story": ("Information",),
            "core.information.music": ("Information",),
            "core.information.song": ("Information",),
            "core.time.day": ("TimeInterval",),
            "core.time.night": ("TimeInterval",),
            "core.time.season": ("TimeInterval",),
            "core.time.year": ("TimeInterval",),
            "core.time.month": ("TimeInterval",),
            "core.information.date": ("Information",),
        }
        actual = {
            concept_id: tuple(concept["classifies_types"])
            for concept_id, concept in self.language.world_concepts.items()
            if "classifies_types" in concept
        }
        self.assertEqual(actual, expected)

    def test_world_package_classifier_metadata_gets_core_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "language", root / "language")
            shutil.copytree(ROOT / "world", root / "world")

            concepts_path = root / "world" / "yona" / "concepts.json"
            concepts = json.loads(concepts_path.read_text(encoding="utf-8"))
            by_id = {item["id"]: item for item in concepts["concepts"]}
            by_id["yona.system.quest"]["classifies_types"] = ["SemanticValue"]
            by_id["yona.system.skill"]["classifies_types"] = ["Entity", "Entity"]
            concepts_path.write_text(
                json.dumps(concepts, indent=2) + "\n",
                encoding="utf-8",
            )

            errors = validate_language_data(root)
            self.assertTrue(
                any(
                    "yona.system.quest: classifies_types cannot use broad/meta type SemanticValue"
                    in error
                    for error in errors
                ),
                errors,
            )
            self.assertTrue(
                any(
                    "yona.system.skill: duplicate classifies_types member 'Entity'"
                    in error
                    for error in errors
                ),
                errors,
            )


if __name__ == "__main__":
    unittest.main()
