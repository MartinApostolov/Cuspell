from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"
DRAFTS = BASE / "meaning_assignments"


class GlyphMeaningBatch02Tests(unittest.TestCase):
    def test_batch02_proposals_are_30_distinct_new_approved_source_glyphs(self):
        first = json.loads((DRAFTS / "draft_01.json").read_text())
        current = json.loads((DRAFTS / "draft_02.json").read_text())
        self.assertEqual(first["status"], "USER_APPROVED_FIRST_19_PENDING_FULL_FONT_MAPPING")
        self.assertEqual(current["status"], "PROPOSED_30_FOR_VISUAL_REVIEW_NOT_APPROVED")
        old, new = first["assignments"], current["assignments"]
        self.assertEqual((len(old), len(new)), (19, 30))
        self.assertEqual(len({x["glyph_id"] for x in old + new}), 49)
        self.assertEqual(len({x["surface"] for x in old + new}), 49)

        lex = json.loads((ROOT / "language/core/lexicon.json").read_text())
        entries = {x["surface"]: x for x in lex["entries"]}
        self.assertEqual(len(entries), 217)
        self.assertTrue(all(x.get("rune_cost", 1) == 1 for x in entries.values()))
        with (BASE / "keyboard_kit/glyph_map.csv").open(encoding="utf-8-sig", newline="") as stream:
            glyphs = {x["id"]: x for x in csv.DictReader(stream)}
        self.assertEqual(len(glyphs), 234)
        for x in new:
            self.assertIn(x["surface"], entries)
            self.assertEqual(x["lexicon_id"], entries[x["surface"]]["id"])
            self.assertEqual(x["codepoint"], glyphs[x["glyph_id"]]["codepoint"])
            self.assertEqual(x["collection"], glyphs[x["glyph_id"]]["collection"])

        progression = json.loads((ROOT / "language/subsets/spellcraft_progression_v1.json").read_text())
        extended = [s for mod in progression["modules"] if mod.get("course_level") in
                    ("intermediate", "advanced") for s in mod["add_entries"]]
        self.assertEqual(len(extended), 11)
        self.assertTrue(set(extended).issubset({x["surface"] for x in new}))
        self.assertEqual((len(entries)-48, len(glyphs)-49), (169,185))

    def test_review_artifacts_and_font_test_page(self):
        full = (DRAFTS / "review_02_all_30.svg").read_text()
        a = (DRAFTS / "review_02_first_15.svg").read_text()
        b = (DRAFTS / "review_02_second_15.svg").read_text()
        html = (BASE / "keyboard_kit/meaning_assignment_preview_02.html").read_text()
        self.assertEqual(full.count('<rect x="6"'), 30)
        self.assertEqual(a.count('<rect x="6"'), 15)
        self.assertEqual(b.count('<rect x="6"'), 15)
        self.assertIn("Not approved yet", html)
        self.assertIn("CuspellCodexReview-Regular.ttf", html)
        self.assertIn("34 px", html)


if __name__ == "__main__":
    unittest.main()
