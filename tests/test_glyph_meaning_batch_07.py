from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"
DRAFTS = BASE / "meaning_assignments"


class GlyphMeaningBatch07Tests(unittest.TestCase):
    def test_new_thirty_are_registered_unique_and_review_only(self):
        data = [json.loads((DRAFTS / f"draft_{n:02}.json").read_text()) for n in range(1, 8)]
        self.assertTrue(all(d["status"].startswith("USER_APPROVED") for d in data[:6]))
        last = data[6]
        self.assertEqual(last["status"], "USER_APPROVED_BATCH_07_30_PENDING_FULL_FONT_MAPPING")
        old = data[0]["assignments"] + data[1]["assignments"]
        old += [e for d in data[2:6] for e in d["proposed_assignments"]]
        new = last["proposed_assignments"]
        self.assertEqual((len(old), len(new)), (169, 30))
        self.assertEqual(len({x["glyph_id"] for x in old + new}), 199)
        self.assertEqual(len({x["surface"] for x in old + new}), 199)
        lex = {e["surface"]: e for e in json.loads((ROOT / "language/core/lexicon.json").read_text())["entries"]}
        self.assertEqual(len(lex), 217)
        with (BASE / "keyboard_kit/glyph_map.csv").open(encoding="utf-8-sig", newline="") as handle:
            font = {g["id"]: g for g in csv.DictReader(handle)}
        self.assertEqual(len(font), 234)
        for entry in new:
            with self.subTest(surface=entry["surface"]):
                self.assertEqual(lex[entry["surface"]]["id"], entry["lexicon_id"])
                self.assertEqual(lex[entry["surface"]]["rune_cost"], 1)
                self.assertEqual(font[entry["glyph_id"]]["codepoint"], entry["codepoint"])
                self.assertEqual(font[entry["glyph_id"]]["collection"], entry["collection"])
        self.assertEqual((217 - 198, 234 - 199), (19, 35))

    def test_15_moderate_pairs_are_disclosed_in_review(self):
        d = json.loads((DRAFTS / "draft_07.json").read_text())
        risks = d["similarity_review"]
        self.assertEqual(risks["new_above_threshold_pairs"], [])
        self.assertEqual(risks["moderate_count"], 15)
        self.assertEqual(len(risks["moderate_same_orientation_pairs"]), 15)
        self.assertLessEqual(risks["max_moderate_score"], 0.85)
        proposed_ids = {e["glyph_id"] for e in d["proposed_assignments"]}
        for p in risks["moderate_same_orientation_pairs"]:
            self.assertTrue(proposed_ids.intersection((p["a"], p["b"])))
        possible_spares = d["potential_final_spares_NOT_APPROVED"]
        self.assertEqual(len(possible_spares), 16)
        self.assertFalse(proposed_ids.intersection(possible_spares))

    def test_exact_source_svg_sheets_and_local_font_page(self):
        for name, count in (
            ("review_07_all_30.svg", 30),
            ("review_07_first_15.svg", 15),
            ("review_07_last_15.svg", 15),
        ):
            svg = (DRAFTS / name).read_text()
            self.assertEqual(svg.count('<rect x="6"'), count)
            self.assertEqual(svg.count('<svg xmlns="http://www.w3.org/2000/svg" x="81"'), count)
        close = (DRAFTS / "review_07_close_pairs.svg").read_text()
        self.assertEqual(close.count('<rect x="5"'), 15)
        html = (BASE / "keyboard_kit/meaning_assignment_preview_07.html").read_text()
        self.assertIn("Batch 07: all 30 glyphs user-approved", html)
        self.assertIn("CuspellCodexReview-Regular.ttf", html)
        self.assertIn("34 px", html)
        self.assertTrue((BASE / "keyboard_kit/CuspellCodexReview-Regular.ttf").is_file())


if __name__ == "__main__":
    unittest.main()
