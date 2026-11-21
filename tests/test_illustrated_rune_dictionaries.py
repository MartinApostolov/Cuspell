from __future__ import annotations

import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "language/core/glyph_assignments.json"
DOCS = ROOT / "docs/CUSPELL_DICTIONARY.md"
PLAYER = ROOT / "player/RUNES.md"
SOURCE = ROOT / "assets/glyphs/references/idylwild"


class IllustratedRuneDictionaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.canonical = json.loads(MAPPING.read_text(encoding="utf-8"))
        cls.runes = {x["surface"]: x for x in cls.canonical["assignments"]
                     if x["role"] == "registered_rune"}
        cls.number = next(x for x in cls.canonical["assignments"] if x["surface"] == "@")
        snap = json.loads((SOURCE / "stylized/analysis/FRESH_SURVIVOR_A_R_SOURCE_SNAPSHOT_2026_11_21.json").read_text())
        cls.stylized_paths = {x["id"]: x["path"] for x in snap["eligibleFiles"]}

    def check_glyph_image(self, cell: str, surface: str, parent: Path):
        item = self.number if surface == "@" else self.runes[surface]
        glyph_id = item["glyph_id"]
        m = re.search(r'<img src="([^"]+)" width="28" height="46" alt="([^"]+)"\s*/>', cell)
        self.assertIsNotNone(m, f"Missing SVG image for {surface}")
        path, alt = m.groups()
        self.assertEqual(alt, f"{surface} ({glyph_id})")
        self.assertIn(f"<sub>{glyph_id}</sub>", cell)
        expected = (f"assets/glyphs/recovery/generated/glyphs/{glyph_id}.svg"
                    if glyph_id.startswith("G") else self.stylized_paths[glyph_id])
        art = (parent / path).resolve()
        self.assertEqual(art, (ROOT / expected).resolve())
        self.assertTrue(art.is_file(), str(art))
        self.assertIn('viewBox="0 0 600 1000"', art.read_text(encoding="utf-8"))

    def test_maintainer_dictionary_has_217_illustrated_runes(self):
        text = DOCS.read_text(encoding="utf-8").split("## How to write Cuspell")[0]
        seen = []
        for line in text.splitlines():
            parts = [x.strip() for x in line.split("|")]
            if len(parts) == 5 and parts[2] in self.runes:
                seen.append(parts[2])
                self.check_glyph_image(parts[1], parts[2], DOCS.parent)
        self.assertEqual(set(seen), set(self.runes))
        self.assertEqual(len(seen), 219)  # Female/Worship repeated for history.
        self.assertEqual({k for k, v in Counter(seen).items() if v > 1},
                         {"Female", "Worship"})
        self.assertNotIn("intentionally blank", text)
        number = next(s for s in text.splitlines() if "| `@` |" in s)
        self.check_glyph_image(number.split("|")[1], "@", DOCS.parent)

    def test_player_dictionary_has_same_217_signs_plus_numeric_one(self):
        text = PLAYER.read_text(encoding="utf-8")
        found = []
        for line in text.splitlines():
            parts = [x.strip() for x in line.split("|")]
            if len(parts) != 5:
                continue
            name = parts[2].strip("`")
            if name in self.runes:
                self.check_glyph_image(parts[1], name, PLAYER.parent)
                found.append(name)
        self.assertEqual(len(found), 217)
        self.assertEqual(set(found), set(self.runes))
        number = next(s for s in text.splitlines() if "| `@` |" in s)
        self.check_glyph_image(number.split("|")[1], "@", PLAYER.parent)
        self.assertNotIn("no design has been assigned", text)

    def test_noncore_and_spare_designs_stay_separate(self):
        assigned = {x["glyph_id"] for x in self.canonical["assignments"]}
        spares = {x["glyph_id"] for x in self.canonical["spares"]}
        self.assertEqual((len(assigned), len(spares)), (218, 16))
        self.assertEqual(len(self.runes), 217)
        self.assertFalse(assigned & spares)


if __name__ == "__main__":
    unittest.main()
