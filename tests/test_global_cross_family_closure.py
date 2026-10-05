from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class GlobalCrossFamilyClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.roles = json.loads(
            (ROOT / "language" / "core" / "inventory_roles.json").read_text()
        )

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_global_closure_keeps_current_inventory_counts(self):
        self.assertEqual(len(self.roles["entries"]), 214)
        self.assertEqual(self.roles["counts"]["semantic_primitive_candidate"], 133)
        self.assertEqual(self.roles["counts"]["unresolved_candidate"], 0)

    def test_use_is_not_agentive_cause(self):
        using = self.valid("!Use Self This Move Self Here.").ast.children[0].canonical()
        causing = self.valid("!Cause Self Move Self Here.").ast.children[0].canonical()
        self.assertNotEqual(using, causing)

    def test_at_anchor_and_in_containment_keep_different_role_types(self):
        at = self.language.entry("At")
        inside = self.language.entry("In")
        self.assertIsNotNone(at)
        self.assertIsNotNone(inside)
        self.assertEqual(at.frames[0]["slots"][1]["type"], "Location")
        self.assertEqual(inside.frames[0]["slots"][1]["type"], "Region")

    def test_density_still_has_distribution_frame(self):
        density = self.language.entry("Density")
        self.assertIsNotNone(density)
        frame_ids = {frame["id"] for frame in density.frames}
        self.assertIn("density.value", frame_ids)
        self.assertIn("density.distribution_region", frame_ids)

    def test_assert_and_say_remain_distinct_processes(self):
        assertion = self.language.entry("Assert")
        saying = self.language.entry("Say")
        self.assertIsNotNone(assertion)
        self.assertIsNotNone(saying)
        self.assertNotEqual(assertion.data["id"], saying.data["id"])

    def test_simultaneous_keeps_event_semantics_beyond_equal_timepoints(self):
        simultaneous = self.language.entry("Simultaneous")
        self.assertIsNotNone(simultaneous)
        frame_ids = {frame["id"] for frame in simultaneous.frames}
        self.assertIn("simultaneous.events", frame_ids)
        self.assertIn("simultaneous.points", frame_ids)


if __name__ == "__main__":
    unittest.main()
