from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser


ROOT = Path(__file__).resolve().parents[1]


class DistanceAlmostRedesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_distance_has_one_spatial_frame(self):
        distance = self.language.entry("Distance")
        self.assertIsNotNone(distance)
        self.assertEqual([frame["id"] for frame in distance.frames], ["distance.spatial"])
        self.assertEqual(distance.frames[0]["output"], "Quantity:Length")
        self.assertEqual(
            [slot["type"] for slot in distance.frames[0]["slots"]],
            ["SpatialValue", "SpatialValue"],
        )

    def test_spatial_value_covers_current_distance_carriers(self):
        for actual in ("Entity", "Location", "Region"):
            with self.subTest(actual=actual):
                self.assertTrue(self.language.is_assignable(actual, "SpatialValue"))
        for actual in ("Proposition", "EventSpec", "EvaluationValue"):
            with self.subTest(actual=actual):
                self.assertFalse(self.language.is_assignable(actual, "SpatialValue"))

    def test_physical_distance_still_parses(self):
        for source in (
            "Distance This Here",
            "Distance This Self",
            "Distance ThisRegion Here",
        ):
            with self.subTest(source=source):
                node = self.parser.parse_phrase(source, expected_type="Quantity:Length")
                self.assertNotIsInstance(node, Diagnostic, node)

    def test_distance_rejects_old_boundary_senses(self):
        for source in (
            "Distance LifeThis",
            "Distance HighHunger Self",
            "Distance MoveThisHere",
        ):
            with self.subTest(source=source):
                node = self.parser.parse_phrase(source, expected_type="EvaluationValue")
                self.assertIsInstance(node, Diagnostic)

    def test_almost_has_one_semantic_core_over_two_target_types(self):
        almost = self.language.entry("Almost")
        self.assertIsNotNone(almost)
        self.assertEqual(
            {frame["id"] for frame in almost.frames},
            {"almost.proposition", "almost.event"},
        )
        self.assertTrue(all(frame.get("contextual") for frame in almost.frames))
        self.assertEqual({frame["output"] for frame in almost.frames}, {"Proposition"})

    def test_almost_covers_property_and_event_nearness(self):
        for source in (
            "Almost LifeThis.",
            "Almost HighHunger Self.",
            "Almost MoveThisHere.",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertTrue(result.valid, result.diagnostics)

    def test_almost_is_not_objective_magic_while_contextual(self):
        for source in (
            "If Almost LifeThis MoveSelfHere!",
            "If Almost MoveThisHere MoveSelfThere!",
        ):
            with self.subTest(source=source):
                result = self.parser.check(source)
                self.assertFalse(result.valid)
                self.assertTrue(
                    any(d.code == "SemanticallyIncomplete" for d in result.diagnostics),
                    result.diagnostics,
                )

    def test_inventory_and_frame_counts(self):
        lexicon = json.loads(
            (ROOT / "language" / "core" / "lexicon.json").read_text(encoding="utf-8")
        )
        frames = [frame for entry in lexicon["entries"] for frame in entry.get("frames", [])]
        multi = [entry for entry in lexicon["entries"] if len(entry.get("frames", [])) >= 2]
        self.assertEqual(len(lexicon["entries"]), 217)
        self.assertEqual(len(frames), 276)
        self.assertEqual(len(multi), 53)


if __name__ == "__main__":
    unittest.main()
