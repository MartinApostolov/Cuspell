from __future__ import annotations

import csv
import hashlib
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "glyphs" / "references" / "idylwild"
KIT = BASE / "keyboard_kit"


class GlyphAssignmentReadinessTests(unittest.TestCase):
    def test_approved_pc_inventory_is_stable_and_unassigned(self):
        lexicon = json.loads((ROOT / "language/core/lexicon.json").read_text())
        entries = lexicon["entries"]
        self.assertEqual(len(entries), 217)
        self.assertEqual(len({e["id"] for e in entries}), 217)
        self.assertEqual(len({e["surface"] for e in entries}), 217)
        self.assertNotIn("@", {e["surface"] for e in entries})
        self.assertTrue(all(e.get("rune_cost", 1) == 1 for e in entries))
        self.assertIn("BeforeValue", {e["surface"] for e in entries})
        self.assertIn("AfterValue", {e["surface"] for e in entries})

        info = json.loads((KIT / "font_manifest.json").read_text())
        self.assertFalse(info["root_meanings_assigned"])
        self.assertEqual(info["num_total"], 234)
        self.assertEqual(
            (info["num_cuspell"], info["num_runic"], info["num_alchemical"]),
            (94, 76, 64),
        )
        with (KIT / "glyph_map.csv").open(encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.DictReader(fh))
        ids = [row["id"] for row in rows]
        cps = [int(row["codepoint"][2:], 16) for row in rows]
        self.assertEqual(len(set(ids)), 234)
        self.assertEqual(cps, list(range(0xE000, 0xE0EA)))
        self.assertEqual(
            {label: sum(row["collection"] == label for row in rows)
             for label in ("Cuspell", "Runic", "Alchemical")},
            {"Cuspell": 94, "Runic": 76, "Alchemical": 64},
        )
        ledger = json.loads((BASE / "stylized/analysis/potential_overlap_groups.json").read_text())
        excluded = set(ledger["final_inventory_exclusion_summary"]["direct_source_ids"])
        reserved = {x["id"] for x in ledger["final_inventory_typography_reserve"]["entries"]}
        self.assertFalse(set(ids) & (excluded | reserved))
        self.assertEqual(len(ids) - len(entries) - 1, 16)

    def test_punctuation_and_font_package_are_separate_and_present(self):
        manifest = json.loads(
            (BASE / "stylized/typography/player_facing/manifest.json").read_text()
        )
        self.assertEqual(len(manifest["entries"]), 13)
        self.assertEqual(
            {entry["character"] for entry in manifest["entries"]},
            set(".:?!«»$()_{},"),
        )
        self.assertNotIn("@", {entry["character"] for entry in manifest["entries"]})
        self.assertTrue(all(entry["status"].startswith("USER_APPROVED") for entry in manifest["entries"]))
        for entry in manifest["entries"]:
            self.assertTrue((BASE / "stylized/typography/player_facing" / entry["file"]).is_file())
        info = json.loads((KIT / "font_manifest.json").read_text())
        self.assertEqual(
            hashlib.sha256((KIT / info["font"]).read_bytes()).hexdigest(),
            info["font_sha256"],
        )
        with zipfile.ZipFile(KIT / "Cuspell_Codex_Keyboard_Kit.zip") as archive:
            self.assertIsNone(archive.testzip())
            for name in (
                info["font"], "CuspellCodexReview-Regular.woff2",
                "keyboard.html", "chart.html", "glyph_map.csv", "README.md",
            ):
                self.assertIn(name, archive.namelist())


if __name__ == "__main__":
    unittest.main()
