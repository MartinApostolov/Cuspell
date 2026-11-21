from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets/glyphs/references/idylwild"
DRAFTS = BASE / "meaning_assignments"


class GlyphMeaningBatch08Tests(unittest.TestCase):
    def test_final_batch_is_proposed_not_approved_and_all_inventory_is_accounted_for(self):
        earlier = [json.loads((DRAFTS / f"draft_{i:02d}.json").read_text()) for i in range(1, 8)]
        self.assertTrue(all(d["status"].startswith("USER_APPROVED") for d in earlier))
        prior = earlier[0]["assignments"] + earlier[1]["assignments"]
        prior += [a for d in earlier[2:] for a in d["proposed_assignments"]]
        self.assertEqual(len(prior), 199)
        last = json.loads((DRAFTS / "draft_08.json").read_text())
        self.assertEqual(last["status"], "USER_APPROVED_FINAL_19_AND_16_SPARES_PENDING_TYPEABLE_FONT")
        self.assertEqual((len(last["proposed_final_19"]), len(last["proposed_spare_16"])), (19, 16))
        new = last["proposed_final_19"]
        all_signs = prior + new
        self.assertEqual(len(all_signs), 218)
        self.assertEqual(len({a["glyph_id"] for a in all_signs}), 218)
        self.assertEqual(len({a["surface"] for a in all_signs}), 218)

        registry = json.loads((ROOT / "language/core/lexicon.json").read_text())["entries"]
        self.assertEqual(len(registry), 217)
        self.assertTrue(all(x["rune_cost"] == 1 for x in registry))
        self.assertEqual(
            {x["id"] for x in registry},
            {a["lexicon_id"] for a in all_signs if a["surface"] != "@"},
        )
        self.assertEqual(
            {x["surface"] for x in registry},
            {a["surface"] for a in all_signs if a["surface"] != "@"},
        )
        self.assertEqual(sum(a["surface"] == "@" for a in all_signs), 1)
        with (BASE / "keyboard_kit/glyph_map.csv").open(encoding="utf-8-sig", newline="") as f:
            font = {x["id"]: x for x in csv.DictReader(f)}
        self.assertEqual(len(font), 234)
        used = {x["glyph_id"] for x in all_signs}
        spares = {x["glyph_id"] for x in last["proposed_spare_16"]}
        self.assertEqual(set(font) - used, spares)
        self.assertEqual(len(spares), 16)
        for item in new + last["proposed_spare_16"]:
            self.assertEqual(item["codepoint"], font[item["glyph_id"]]["codepoint"])
            self.assertEqual(item["collection"], font[item["glyph_id"]]["collection"])

    def test_integrated_provisional_mapping_file(self):
        draft = json.loads((DRAFTS / "draft_08.json").read_text())
        complete = json.loads((DRAFTS / "complete_mapping_review_08.json").read_text())
        self.assertEqual(complete["status"], "USER_APPROVED_COMPLETE_218_MAPPING_REVIEW_SNAPSHOT")
        self.assertEqual(len(complete["assignments"]), 218)
        self.assertEqual(sum(x["status"] == "USER_APPROVED_BATCH_08" for x in complete["assignments"]), 19)
        self.assertEqual(sum(x["status"] == "USER_APPROVED_PRIOR_BATCH" for x in complete["assignments"]), 199)
        self.assertEqual(set(complete["proposed_unassigned_spares"]),
                         {x["glyph_id"] for x in draft["proposed_spare_16"]})

    def test_exact_mirror_and_other_visual_risks_are_disclosed(self):
        risks = json.loads((DRAFTS / "draft_08.json").read_text())["visual_risk"]
        self.assertEqual(risks["new_high_count"], 11)
        self.assertEqual(len(risks["exact_mirror_pairs"]), 4)
        self.assertTrue(all(x["score"] == 1 and x["transform"] == "horizontal_flip"
                            for x in risks["exact_mirror_pairs"]))
        self.assertEqual(risks["new_moderate_count"], 31)
        for name, count in [
            ("review_08_final_19.svg", 19), ("review_08_spare_16.svg", 16),
            ("review_08_full_35.svg", 35),
        ]:
            self.assertEqual((DRAFTS / name).read_text().count('<rect x="6"'), count)
        for name, count in [
            ("review_08_high_similarity_pairs.svg", 11),
            ("review_08_moderate_pairs_1.svg", 16),
            ("review_08_moderate_pairs_2.svg", 15),
        ]:
            self.assertEqual((DRAFTS / name).read_text().count('<rect x="5"'), count)
        html = (BASE / "keyboard_kit/meaning_assignment_preview_08.html").read_text()
        self.assertIn("All 218 rune/number glyphs and all 16 spare selections are user-approved", html)
        self.assertIn("CuspellCodexReview-Regular.ttf", html)
        self.assertIn("four glyphs are exact horizontal mirror counterparts", html)
        self.assertTrue((BASE / "keyboard_kit/CuspellCodexReview-Regular.ttf").is_file())


if __name__ == "__main__":
    unittest.main()
