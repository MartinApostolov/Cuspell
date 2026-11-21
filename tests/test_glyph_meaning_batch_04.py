from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"
DRAFTS = BASE / "meaning_assignments"


class GlyphMeaningBatch04Tests(unittest.TestCase):
    def test_30_new_glyphs_match_lexicon_and_prior_approvals(self):
        batches = [json.loads((DRAFTS / f"draft_{n:02}.json").read_text()) for n in range(1, 5)]
        self.assertTrue(all(x["status"].startswith("USER_APPROVED") for x in batches[:3]))
        fourth = batches[3]
        self.assertEqual(fourth["status"], "PROPOSED_30_FOR_USER_REVIEW_NOT_APPROVED")
        earlier = (batches[0]["assignments"] + batches[1]["assignments"]
                   + batches[2]["proposed_assignments"])
        proposed = fourth["proposed_assignments"]
        self.assertEqual((len(earlier), len(proposed)), (79, 30))
        self.assertEqual(len({x["glyph_id"] for x in earlier + proposed}), 109)
        self.assertEqual(len({x["surface"] for x in earlier + proposed}), 109)

        lexicon = json.loads((ROOT / "language/core/lexicon.json").read_text())["entries"]
        registered = {x["surface"]: x for x in lexicon}
        self.assertEqual(len(registered), 217)
        with (BASE / "keyboard_kit/glyph_map.csv").open(encoding="utf-8-sig", newline="") as handle:
            glyphs = {x["id"]: x for x in csv.DictReader(handle)}
        self.assertEqual(len(glyphs), 234)
        for entry in proposed:
            with self.subTest(surface=entry["surface"]):
                root = registered[entry["surface"]]
                self.assertEqual(root["id"], entry["lexicon_id"])
                self.assertEqual(root.get("rune_cost", 1), 1)
                self.assertEqual(glyphs[entry["glyph_id"]]["codepoint"], entry["codepoint"])
                self.assertEqual(glyphs[entry["glyph_id"]]["collection"], entry["collection"])
        self.assertEqual(fourth["similarity"]["new_above_threshold_pairs"], [])
        self.assertEqual(fourth["similarity"]["new_small_size_pair_risks"], [])
        self.assertEqual((217 - 108, 234 - 109), (109,125))
        self.assertEqual({x["surface"] for x in proposed if x["surface"] in
                         ("BeforeValue", "AfterValue")}, {"BeforeValue", "AfterValue"})

    def test_exact_source_review_sheet_and_font_preview_files_exist(self):
        for name, count in (
            ("review_04_all_30.svg", 30), ("review_04_first_15.svg", 15),
            ("review_04_last_15.svg", 15),
        ):
            svg = (DRAFTS / name).read_text()
            self.assertEqual(svg.count('<rect x="6"'), count)
            self.assertEqual(svg.count('<svg x="77"'), count)
        html = (BASE / "keyboard_kit/meaning_assignment_preview_04.html").read_text()
        self.assertIn("Draft for review", html)
        self.assertIn("CuspellCodexReview-Regular.ttf", html)
        self.assertIn("34 px", html)
        self.assertTrue((BASE / "keyboard_kit/CuspellCodexReview-Regular.ttf").is_file())


if __name__ == "__main__":
    unittest.main()
