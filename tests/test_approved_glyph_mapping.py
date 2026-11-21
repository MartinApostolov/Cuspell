from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"


class ApprovedGlyphMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.canonical = json.loads((ROOT / "language/core/glyph_assignments.json").read_text())
        cls.lex = json.loads((ROOT / "language/core/lexicon.json").read_text())["entries"]
        with (BASE / "keyboard_kit/glyph_map.csv").open(encoding="utf-8-sig", newline="") as source:
            cls.font = {row["id"]: row for row in csv.DictReader(source)}

    def test_registered_runic_ids_and_numeric_sign_fully_covered_once(self):
        c = self.canonical
        self.assertEqual(c["status"], "USER_APPROVED_CANONICAL_218_GLYPH_MAPPING")
        self.assertEqual((len(c["assignments"]), len(c["spares"])), (218, 16))
        self.assertEqual(len(self.lex), 217)
        self.assertEqual(len(self.font), 234)
        self.assertEqual(len({x["glyph_id"] for x in c["assignments"]}), 218)
        self.assertEqual(len({x["surface"] for x in c["assignments"]}), 218)
        entries = [x for x in c["assignments"] if x["role"] == "registered_rune"]
        numbers = [x for x in c["assignments"] if x["role"] == "numeric_one_sign"]
        self.assertEqual((len(entries), len(numbers)), (217, 1))
        self.assertEqual(numbers[0]["surface"], "@")
        self.assertIsNone(numbers[0]["lexicon_id"])
        self.assertEqual({x["lexicon_id"] for x in entries}, {x["id"] for x in self.lex})
        self.assertEqual({x["surface"] for x in entries}, {x["surface"] for x in self.lex})
        self.assertTrue(all(x["rune_cost"] == 1 for x in entries))
        self.assertTrue(all(x["rune_cost"] == 1 for x in self.lex))

    def test_original_glyph_ids_and_unicode_slots_still_match_prototype(self):
        c = self.canonical
        used = {x["glyph_id"] for x in c["assignments"]}
        spares = {x["glyph_id"] for x in c["spares"]}
        self.assertEqual(set(self.font) - used, spares)
        self.assertFalse(used.intersection(spares))
        for x in c["assignments"] + c["spares"]:
            with self.subTest(glyph_id=x["glyph_id"]):
                original = self.font[x["glyph_id"]]
                self.assertEqual(x["collection"], original["collection"])
                self.assertEqual(x["temporary_codepoint"], original["codepoint"])
                self.assertEqual(x["temporary_character"], original["character"])

    def test_all_user_approvals_match_single_canonical_mapping(self):
        c = self.canonical
        batches = [json.loads((BASE / f"meaning_assignments/draft_{n:02d}.json").read_text())
                   for n in range(1, 9)]
        self.assertTrue(all(d["status"].startswith("USER_APPROVED") for d in batches))
        approved = batches[0]["assignments"] + batches[1]["assignments"]
        approved += [e for batch in batches[2:7] for e in batch["proposed_assignments"]]
        approved += batches[7]["proposed_final_19"]
        self.assertEqual(
            {(e["surface"], e["glyph_id"]) for e in approved},
            {(e["surface"], e["glyph_id"]) for e in c["assignments"]},
        )
        self.assertEqual(
            {x["glyph_id"] for x in batches[7]["proposed_spare_16"]},
            {x["glyph_id"] for x in c["spares"]},
        )

    def test_punctuation_and_existing_font_kept_separate(self):
        c = self.canonical
        signs = json.loads(
            (BASE / "stylized/typography/player_facing/manifest.json").read_text()
        )["entries"]
        self.assertEqual(len(signs), 13)
        self.assertTrue(c["encoding_policy"]["existing_pc_review_font_unchanged"])
        self.assertTrue(c["encoding_policy"]["existing_pua_mapping_preserved"])
        self.assertTrue((BASE / "keyboard_kit/CuspellCodexReview-Regular.ttf").is_file())
        self.assertEqual(c["review_notes"]["exact_mirrored_pairs"], 4)


if __name__ == "__main__":
    unittest.main()
