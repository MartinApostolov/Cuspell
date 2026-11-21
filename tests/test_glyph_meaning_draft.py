from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"


class DraftMeaningAssignmentTests(unittest.TestCase):
    def test_proposed_beginner_mapping_matches_current_progression(self):
        draft = json.loads((BASE / "meaning_assignments/draft_01.json").read_text())
        self.assertEqual(draft["status"], "PROPOSED_FOR_USER_VISUAL_REVIEW_NOT_CANONICAL")
        entries = draft["assignments"]
        self.assertEqual(len(entries), 19)
        self.assertEqual(len({x["glyph_id"] for x in entries}), 19)
        self.assertEqual(len({x["surface"] for x in entries}), 19)

        lexicon = json.loads((ROOT / "language/core/lexicon.json").read_text())
        by_surface = {x["surface"]: x for x in lexicon["entries"]}
        progression = json.loads(
            (ROOT / "language/subsets/spellcraft_progression_v1.json").read_text()
        )
        required = progression["core"]["entries"] + [
            surface for mod in progression["modules"]
            if mod.get("course_level") == "beginner"
            for surface in mod["add_entries"]
        ]
        self.assertEqual([x["surface"] for x in entries[:-1]], required)
        for entry in entries[:-1]:
            self.assertEqual(entry["lexicon_id"], by_surface[entry["surface"]]["id"])
            self.assertEqual(by_surface[entry["surface"]].get("rune_cost", 1), 1)
        self.assertEqual(entries[-1]["surface"], "@")
        self.assertIsNone(entries[-1]["lexicon_id"])
        self.assertNotIn("@", by_surface)

        with (BASE / "keyboard_kit/glyph_map.csv").open(
            encoding="utf-8-sig", newline=""
        ) as stream:
            selected = {x["id"]: x for x in csv.DictReader(stream)}
        self.assertEqual(len(selected), 234)
        for entry in entries:
            self.assertIn(entry["glyph_id"], selected)
            self.assertEqual(entry["codepoint"], selected[entry["glyph_id"]]["codepoint"])
            self.assertEqual(entry["collection"], selected[entry["glyph_id"]]["collection"])
        self.assertEqual(len(lexicon["entries"]), 217)
        self.assertEqual(234 - len(entries), 215)

    def test_visual_review_artifacts_present_without_replacing_font(self):
        svg = (BASE / "meaning_assignments/review_01.svg").read_text()
        html = (BASE / "keyboard_kit/meaning_assignment_preview_01.html").read_text()
        self.assertEqual(svg.count('<rect x="8"'), 19)
        self.assertIn("NOT FINAL", svg)
        self.assertIn("CuspellCodexReview-Regular.ttf", html)
        self.assertIn("Draft for approval", html)


if __name__ == "__main__":
    unittest.main()
