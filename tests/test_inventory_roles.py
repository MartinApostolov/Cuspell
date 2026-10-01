from __future__ import annotations

import json
import unittest
from pathlib import Path

from cuspell.language import Language

ROOT = Path(__file__).resolve().parents[1]


class InventoryRoleAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.lexicon_data = json.loads(
            (ROOT / "language" / "core" / "lexicon.json").read_text()
        )
        cls.roles_data = json.loads(
            (ROOT / "language" / "core" / "inventory_roles.json").read_text()
        )

    def test_every_core_entry_has_exactly_one_inventory_role(self):
        lexicon_ids = {entry["id"] for entry in self.lexicon_data["entries"]}
        role_ids = {entry["id"] for entry in self.roles_data["entries"]}
        self.assertEqual(role_ids, lexicon_ids)
        self.assertEqual(len(self.roles_data["entries"]), len(lexicon_ids))

    def test_inventory_role_counts_match_entries(self):
        actual = {role: 0 for role in self.roles_data["counts"]}
        for entry in self.roles_data["entries"]:
            role = entry["inventory_role"]
            actual[role] = actual.get(role, 0) + 1
        self.assertEqual(actual, self.roles_data["counts"])

    def test_inside_outside_keep_their_strict_geometry_distinction(self):
        self.assertIsNotNone(self.language.entry("Inside"))
        self.assertIsNotNone(self.language.entry("Outside"))
        roles = {entry["surface"]: entry["inventory_role"] for entry in self.roles_data["entries"]}
        self.assertEqual(roles["Inside"], "semantic_primitive_candidate")
        self.assertEqual(roles["Outside"], "semantic_primitive_candidate")

    def test_inventory_keeps_primitive_candidates_separate_from_registry_total(self):
        total = len(self.roles_data["entries"])
        primitive = self.roles_data["counts"]["semantic_primitive_candidate"]
        self.assertEqual(total, 208)
        self.assertEqual(primitive, 128)
        self.assertEqual(self.roles_data["counts"]["unresolved_candidate"], 0)
        self.assertLess(primitive, total)
        self.assertGreaterEqual(total - primitive, 80)


if __name__ == "__main__":
    unittest.main()
