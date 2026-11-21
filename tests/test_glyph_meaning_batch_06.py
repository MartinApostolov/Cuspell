from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"
DRAFTS = BASE / "meaning_assignments"


class GlyphMeaningBatch06Tests(unittest.TestCase):
    def test_new_thirty_meanings_are_unambiguous_and_registered(self):
        batches = [json.loads((DRAFTS / f"draft_{n:02}.json").read_text()) for n in range(1, 7)]
        self.assertTrue(all(x["status"].startswith("USER_APPROVED") for x in batches[:5]))
        sixth = batches[5]
        self.assertEqual(sixth["status"], "PROPOSED_30_FOR_USER_REVIEW_NOT_APPROVED")
        old = batches[0]["assignments"] + batches[1]["assignments"]
        old += [x for batch in batches[2:5] for x in batch["proposed_assignments"]]
        new = sixth["proposed_assignments"]
        self.assertEqual((len(old), len(new)), (139, 30))
        self.assertEqual(len({x["glyph_id"] for x in old + new}), 169)
        self.assertEqual(len({x["surface"] for x in old + new}), 169)

        lex = json.loads((ROOT / "language/core/lexicon.json").read_text())["entries"]
        dictionary = {x["surface"]: x for x in lex}
        self.assertEqual(len(dictionary), 217)
        with (BASE / "keyboard_kit/glyph_map.csv").open(encoding="utf-8-sig", newline="") as f:
            glyphs = {x["id"]: x for x in csv.DictReader(f)}
        self.assertEqual(len(glyphs), 234)
        for item in new:
            with self.subTest(surface=item["surface"]):
                entry = dictionary[item["surface"]]
                self.assertEqual(item["lexicon_id"], entry["id"])
                self.assertEqual(entry["rune_cost"], 1)
                self.assertEqual(item["codepoint"], glyphs[item["glyph_id"]]["codepoint"])
                self.assertEqual(item["collection"], glyphs[item["glyph_id"]]["collection"])
        self.assertEqual((217 - 168, 234 - 169), (49, 65))
        self.assertEqual(sixth["similarity"]["new_above_threshold_pairs"], [])
        self.assertEqual(sixth["similarity"]["new_small_size_pair_risks"], [])

    def test_visual_reviews_retain_original_glyphs_and_font(self):
        for name, count in (
            ("review_06_all_30.svg", 30),
            ("review_06_first_15.svg", 15),
            ("review_06_last_15.svg", 15),
        ):
            svg = (DRAFTS / name).read_text()
            self.assertEqual(svg.count('<rect x="6"'), count)
            self.assertEqual(svg.count('<svg x="81"'), count)
        page = (BASE / "keyboard_kit/meaning_assignment_preview_06.html").read_text()
        self.assertIn("Not approved yet", page)
        self.assertIn("CuspellCodexReview-Regular.ttf", page)
        self.assertIn("34 px", page)
        self.assertTrue((BASE / "keyboard_kit/CuspellCodexReview-Regular.ttf").is_file())


if __name__ == "__main__":
    unittest.main()
