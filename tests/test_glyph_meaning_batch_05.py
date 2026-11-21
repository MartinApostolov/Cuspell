from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"
DRAFTS = BASE / "meaning_assignments"


class GlyphMeaningBatch05Tests(unittest.TestCase):
    def test_30_new_glyphs_match_registered_lexicon_and_prior_approvals(self):
        batches = [json.loads((DRAFTS / f"draft_{i:02d}.json").read_text()) for i in range(1, 6)]
        self.assertTrue(all(x["status"].startswith("USER_APPROVED") for x in batches[:4]))
        fifth = batches[4]
        self.assertEqual(fifth["status"], "PROPOSED_30_FOR_USER_REVIEW_NOT_APPROVED")
        earlier = (batches[0]["assignments"] + batches[1]["assignments"]
                   + batches[2]["proposed_assignments"] + batches[3]["proposed_assignments"])
        proposed = fifth["proposed_assignments"]
        self.assertEqual((len(earlier), len(proposed)), (109, 30))
        self.assertEqual(len({x["glyph_id"] for x in earlier + proposed}), 139)
        self.assertEqual(len({x["surface"] for x in earlier + proposed}), 139)

        lexicon = json.loads((ROOT / "language/core/lexicon.json").read_text())["entries"]
        by_name = {x["surface"]: x for x in lexicon}
        self.assertEqual(len(by_name), 217)
        with (BASE / "keyboard_kit/glyph_map.csv").open(encoding="utf-8-sig", newline="") as stream:
            glyphs = {x["id"]: x for x in csv.DictReader(stream)}
        self.assertEqual(len(glyphs), 234)
        for item in proposed:
            with self.subTest(name=item["surface"]):
                entry = by_name[item["surface"]]
                self.assertEqual(item["lexicon_id"], entry["id"])
                self.assertEqual(entry.get("rune_cost", 1), 1)
                self.assertEqual(item["codepoint"], glyphs[item["glyph_id"]]["codepoint"])
                self.assertEqual(item["collection"], glyphs[item["glyph_id"]]["collection"])
        self.assertEqual(fifth["similarity"]["new_above_threshold_pairs"], [])
        self.assertEqual(fifth["similarity"]["new_small_size_pair_risks"], [])
        self.assertEqual((217 - 138, 234 - 139), (79, 95))

    def test_review_images_and_existing_font_preview(self):
        for name, count in (
            ("review_05_all_30.svg", 30),
            ("review_05_first_15.svg", 15),
            ("review_05_last_15.svg", 15),
        ):
            svg = (DRAFTS / name).read_text()
            self.assertEqual(svg.count('<rect x="6"'), count)
            self.assertEqual(svg.count('<svg x="77"'), count)
        page = (BASE / "keyboard_kit/meaning_assignment_preview_05.html").read_text()
        self.assertIn("Not approved yet", page)
        self.assertIn("CuspellCodexReview-Regular.ttf", page)
        self.assertIn("34 px", page)
        self.assertTrue((BASE / "keyboard_kit/CuspellCodexReview-Regular.ttf").is_file())


if __name__ == "__main__":
    unittest.main()
