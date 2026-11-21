from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"
ASSIGNMENTS = BASE / "meaning_assignments"


class GlyphMeaningBatch03Tests(unittest.TestCase):
    def test_30_draft_choices_are_distinct_and_registered(self):
        first = json.loads((ASSIGNMENTS / "draft_01.json").read_text())
        second = json.loads((ASSIGNMENTS / "draft_02.json").read_text())
        third = json.loads((ASSIGNMENTS / "draft_03.json").read_text())
        self.assertEqual(first["status"], "USER_APPROVED_FIRST_19_PENDING_FULL_FONT_MAPPING")
        self.assertEqual(second["status"], "USER_APPROVED_BATCH_02_30_PENDING_FULL_FONT_MAPPING")
        self.assertEqual(third["status"], "PROPOSED_30_FOR_USER_REVIEW_NOT_APPROVED")
        prev = first["assignments"] + second["assignments"]
        new = third["proposed_assignments"]
        self.assertEqual((len(prev), len(new)), (49, 30))
        self.assertEqual(len({x["glyph_id"] for x in prev + new}), 79)
        self.assertEqual(len({x["surface"] for x in prev + new}), 79)

        lex = json.loads((ROOT / "language/core/lexicon.json").read_text())
        by_name = {x["surface"]: x for x in lex["entries"]}
        self.assertEqual(len(by_name), 217)
        with (BASE / "keyboard_kit/glyph_map.csv").open(encoding="utf-8-sig", newline="") as fh:
            glyph_map = {x["id"]: x for x in csv.DictReader(fh)}
        self.assertEqual(len(glyph_map), 234)
        for entry in new:
            with self.subTest(entry=entry["surface"]):
                self.assertEqual(entry["lexicon_id"], by_name[entry["surface"]]["id"])
                self.assertEqual(by_name[entry["surface"]].get("rune_cost", 1), 1)
                self.assertEqual(entry["codepoint"], glyph_map[entry["glyph_id"]]["codepoint"])
                self.assertEqual(entry["collection"], glyph_map[entry["glyph_id"]]["collection"])
        self.assertEqual((217 - 78, 234 - 79), (139, 155))
        self.assertEqual(third["similarities"]["additional_high_risk_pairs"], [])
        self.assertEqual(third["similarities"]["additional_small_size_risks"], [])

    def test_review_files_are_complete_and_existing_font_is_preserved(self):
        for name, count in (
            ("review_03_all_30.svg", 30),
            ("review_03_first_15.svg", 15),
            ("review_03_last_15.svg", 15),
        ):
            with self.subTest(name=name):
                svg = (ASSIGNMENTS / name).read_text()
                self.assertEqual(svg.count('<rect x="6"'), count)
                self.assertEqual(svg.count('<svg x="78"'), count)
        html = (BASE / "keyboard_kit/meaning_assignment_preview_03.html").read_text()
        self.assertIn("Not approved yet", html)
        self.assertIn("CuspellCodexReview-Regular.ttf", html)
        self.assertIn("34 px", html)
        self.assertTrue((BASE / "keyboard_kit/CuspellCodexReview-Regular.ttf").is_file())


if __name__ == "__main__":
    unittest.main()
