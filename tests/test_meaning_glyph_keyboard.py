from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from cuspell.glyphs import GlyphCodec

HTML = ROOT / "assets/glyphs/references/idylwild/keyboard_kit/meaning_keyboard.html"


class MeaningGlyphKeyboardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.codec = GlyphCodec.from_repository(ROOT)
        cls.canonical = json.loads((ROOT / "language/core/glyph_assignments.json").read_text(encoding="utf-8"))
        cls.html = HTML.read_text(encoding="utf-8")

    def test_approved_inventory_and_every_rune(self):
        self.assertEqual(len(self.codec.forward), 218)
        self.assertEqual(len(self.codec.reverse), 218)
        self.assertEqual(len(self.canonical["spares"]), 16)
        for entry in self.canonical["assignments"]:
            name = entry["surface"]
            with self.subTest(name=name):
                self.assertEqual(self.codec.encode(name), entry["temporary_character"])
                self.assertEqual(self.codec.decode(entry["temporary_character"]), name)

    def test_reversible_examples_names_binders_and_quotes(self):
        examples = [
            "Move This There!", "LifeThis?", "NotLifeThis.",
            "ThisInterval This Interval.", "ThisPath This Path!",
            "Create i:Entity At $i There Begin Represent $i This Vision!",
            "Move This _ _ ThisPath!", "If LifeThis MoveThisThere!",
            "Concurrent MoveSelfHere MoveYouThere!",
            "Equal Extent ThisEvent @@.", "Sequence MoveSelfHere MoveSelfThere!",
            "Create Light «LightUnit» @!", "«HighExtentHard«ChangeExtentLifeMatter»»",
            "«A person said: Move This There!»", "x:Entity $x i:Human $i {This,You}",
            "G001 R039 012 OldName_1 and lowercase test",
            "UnrecognizedLongThing «UnknownLabel» :profile",
            "  Move  This\tThere!\nLifeThis?  ",
        ]
        for source in examples:
            with self.subTest(source=source):
                self.assertEqual(self.codec.decode(self.codec.encode(source)), source)
        self.assertNotEqual(self.codec.encode("ThisInterval"), self.codec.encode("This Interval"))
        self.assertEqual(self.codec.segment("ThisInterval"), ("ThisInterval",))
        self.assertEqual(self.codec.segment("LifeThis"), ("Life", "This"))
        self.assertIsNone(self.codec.segment("UnknownLabel"))
        self.assertEqual(self.codec.encode("UnknownLabel"), "UnknownLabel")

    def test_unassigned_spare_symbols_remain_unchanged(self):
        for spare in self.canonical["spares"]:
            with self.subTest(id=spare["glyph_id"]):
                c = spare["temporary_character"]
                self.assertEqual(self.codec.decode(c), c)

    def test_offline_browser_data_matches_canonical_source(self):
        match = re.search(r"const CODEC_DATA = (\[[^\n]+\]);", self.html)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data, [
            [e["surface"], e["temporary_character"], e["glyph_id"]]
            for e in self.canonical["assignments"]
        ])
        for text in ("CuspellCodexReview-Regular.woff2", 'id="latin-text"',
                     'id="glyph-text"', 'id="encode"', 'id="decode"'):
            self.assertIn(text, self.html)

    @unittest.skipUnless(shutil.which("node"), "Node.js not installed")
    def test_browser_javascript_matches_python_for_all_roots(self):
        match = re.search(r'<script id="glyph-codec">([\s\S]+?)</script>', self.html)
        self.assertIsNotNone(match)
        words = [e["surface"] for e in self.canonical["assignments"]]
        inputs = words + [
            "Move This There!", "LifeThis?", "NotLifeThis.",
            "ThisInterval This Interval", "Create Light «LightUnit» @!",
            "Move This _ _ ThisPath!", "Create i:Entity At $i There Begin Represent $i This Vision!",
            "«HighExtentHard«ChangeExtentLifeMatter»»", "UnknownLabel $i i:Entity",
        ]
        script = match.group(1) + "\nconst inputs=" + json.dumps(inputs, ensure_ascii=False) + ";\n" + (
            "process.stdout.write(JSON.stringify(inputs.map(t=>"
            "[CuspellGlyphCodec.toGlyphs(t),CuspellGlyphCodec.fromGlyphs(CuspellGlyphCodec.toGlyphs(t))])));"
        )
        result = subprocess.run(["node", "-e", script], capture_output=True, text=True,
                                encoding="utf-8", check=True)
        output = json.loads(result.stdout)
        self.assertEqual(output, [
            [self.codec.encode(t), self.codec.decode(self.codec.encode(t))]
            for t in inputs
        ])

    def test_cli_roundtrip_does_not_require_spell_parser(self):
        cmd = [sys.executable, str(ROOT / "run_cuspell.py")]
        encode = subprocess.run(cmd + ["to-glyphs", "Move This There!"], cwd=ROOT,
                                capture_output=True, text=True, encoding="utf-8", check=True)
        self.assertEqual(encode.stdout.strip(), self.codec.encode("Move This There!"))
        decode = subprocess.run(cmd + ["from-glyphs", encode.stdout.strip()], cwd=ROOT,
                                capture_output=True, text=True, encoding="utf-8", check=True)
        self.assertEqual(decode.stdout.strip(), "Move This There!")


if __name__ == "__main__":
    unittest.main()
