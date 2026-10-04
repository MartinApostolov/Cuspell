from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class StabilizationRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.yona = Language.load(ROOT, world_package="yona")
        cls.parser = Parser(cls.language)
        cls.yona_parser = Parser(cls.yona)
        cls.old_names = json.loads(
            (ROOT / "language" / "names" / "old_names.json").read_text(
                encoding="utf-8"
            )
        )["entries"]

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_language_and_all_world_packages_validate_after_minimization(self):
        self.assertEqual(validate_language_data(ROOT), [])

    def test_every_core_old_name_cost_resolves(self):
        for entry in self.old_names:
            with self.subTest(old_name=entry["id"], sign=entry["sign"]):
                cost = self.language.old_name_cost(entry["sign"])
                self.assertIsInstance(cost, int)
                self.assertGreater(cost, 0)

    def test_every_concept_old_name_resolves_with_declared_classifier_type(self):
        concepts = [
            entry
            for entry in self.old_names
            if entry.get("meaning", {}).get("kind") == "concept"
        ]
        self.assertEqual(len(concepts), 197)
        representative_subjects = {
            "Entity": "This",
            "EventSpec": "Move Self Here",
            "Event": "ThisEvent",
            "Information": "Question True",
            "TimeInterval": "ThisInterval",
        }
        for entry in concepts:
            sign = entry["sign"]
            concept_id = entry["meaning"]["concept_id"]
            concept = self.language.world_concepts[concept_id]
            classify_types = concept.get("classifies_types") or ["Entity"]
            with self.subTest(old_name=entry["id"], sign=sign):
                node = self.parser.parse_phrase(
                    f"«{sign}»",
                    expected_type="Kind",
                )
                self.assertNotIsInstance(node, Diagnostic, node)
                self.assertEqual(
                    node.canonical(),
                    f"Concept({concept_id})",
                )

                subject = next(
                    (
                        representative_subjects[typ]
                        for typ in classify_types
                        if typ in representative_subjects
                    ),
                    None,
                )
                self.assertIsNotNone(
                    subject,
                    f"No stabilization example for classifier types {classify_types}",
                )
                result = self.parser.check(f"«{sign}» {subject}.")
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(
                    f"Concept({concept_id})",
                    result.ast.children[0].canonical(),
                )

    def test_every_canonical_unit_old_name_still_constructs_a_quantity(self):
        units = [
            entry
            for entry in self.old_names
            if entry.get("meaning", {}).get("kind") == "unit"
        ]
        self.assertEqual(len(units), 6)
        for entry in units:
            sign = entry["sign"]
            with self.subTest(old_name=entry["id"], sign=sign):
                node = self.parser.parse_phrase(
                    f"«{sign}» @",
                    expected_type="Quantity",
                )
                self.assertNotIsInstance(node, Diagnostic, node)
                self.assertTrue(node.type.startswith("Quantity:"))

    def test_no_old_name_name_unit_refers_to_a_removed_root(self):
        current_roots = set(self.language.entries)
        for entry in self.old_names:
            for unit in entry.get("name_units", []):
                root = unit.get("root")
                if root is not None:
                    with self.subTest(old_name=entry["id"], root=root):
                        self.assertIn(root, current_roots)

    def test_recent_second_pass_replacements_are_executable(self):
        for source, expected_type in (
            ("Rate Density This ThisInterval", "Quantity"),
            ("Extent ThisEvent", "Quantity:Time"),
        ):
            with self.subTest(source=source):
                node = self.parser.parse_phrase(source, expected_type=expected_type)
                self.assertNotIsInstance(node, Diagnostic, node)

        for source in (
            "And {In This ThisRegion,Not Touch Extent This ThisRegion}.",
            "Not Overlap Extent This ThisRegion.",
            "Concurrent EndHave Self This BeginHave You This!",
        ):
            with self.subTest(source=source):
                self.valid(source)

    def test_recent_removed_roots_are_not_required_by_core_or_yona(self):
        for surface in (
            "ChangeRate",
            "OccurrenceRate",
            "Duration",
            "Inside",
            "Outside",
            "Give",
        ):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))
                self.assertIsNone(self.yona.entry(surface))


if __name__ == "__main__":
    unittest.main()
