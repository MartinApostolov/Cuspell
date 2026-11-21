"""Language v1.0 script/transliteration/parser integration regression tests.

These assert script identity, not merely Latin -> glyph -> Latin convenience.
They use maintained spellcraft examples as real language fixtures.
"""
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
from cuspell.language import Language
from cuspell.parser import Parser


class GlyphLanguageIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.codec = GlyphCodec.from_repository(ROOT)
        cls.parser = Parser(Language.load(ROOT))

    @staticmethod
    def _sentences(tree):
        if isinstance(tree, dict):
            for key, value in tree.items():
                if key == "cuspell" and isinstance(value, str):
                    yield value
                else:
                    yield from GlyphLanguageIntegrationTests._sentences(value)
        elif isinstance(tree, list):
            for item in tree:
                yield from GlyphLanguageIntegrationTests._sentences(item)

    def test_current_spellcraft_fixtures_keep_parser_result_and_mana(self):
        sources = []
        for filename in ("spellcraft_progression_v1.json", "spellcraft_beginner_v0_1.json"):
            data = json.loads((ROOT / "language" / "subsets" / filename).read_text(encoding="utf-8"))
            for source in self._sentences(data):
                sources.append((filename, source))
        self.assertGreaterEqual(len(sources), 82)
        for filename, source in sources:
            with self.subTest(dataset=filename, source=source):
                script = self.codec.encode(source)
                back = self.codec.decode(script)
                self.assertEqual(back, source)
                self.assertEqual(self.codec.encode(back), script)
                before = self.parser.check(source)
                after = self.parser.check(back)
                self.assertEqual(after.valid, before.valid)
                self.assertEqual(after.mana, before.mana)
                self.assertEqual(
                    after.ast.canonical() if after.ast else None,
                    before.ast.canonical() if before.ast else None,
                )
                self.assertEqual(
                    [d.code for d in after.diagnostics],
                    [d.code for d in before.diagnostics],
                )

    def test_surface_forms_preserve_quotes_binders_and_punctuation(self):
        sources = (
            "MatterSelf.",
            "LifeThis?",
            "Move This Here!",
            "If LifeThis EndLifeThis!",
            "Move This _ _ ThisPath!",
            "LifeThis And MagicThis.",
            "Sequence MoveSelfHere MoveSelfThere!",
            "Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd Self.",
            "g:Location At This $g?",
            "All a:«Know«MoveLifeThing»» Life $a.",
            "«HighExtentHard«ChangeExtentLifeMatter»»",
            "{This,Self,You}",
            "Move|This|Here!",
            "Equal Extent ThisEvent @@.",
            "  Move\tThis  There!\n",
        )
        for source in sources:
            with self.subTest(source=source):
                self.assertEqual(self.codec.decode(self.codec.encode(source)), source)

    def test_all_registered_old_names_preserve_quoted_spelling(self):
        registry = json.loads(
            (ROOT / "language/names/old_names.json").read_text(encoding="utf-8")
        )
        self.assertEqual(len(registry["entries"]), 204)
        for entry in registry["entries"]:
            original = "«" + entry["sign"] + "»"
            with self.subTest(old_name=entry["id"]):
                glyphs = self.codec.encode(original)
                self.assertEqual(self.codec.decode(glyphs), original)
                self.assertEqual(self.codec.encode(self.codec.decode(glyphs)).replace(" ", ""), glyphs)

    def test_exact_registered_label_does_not_swallow_two_glyphs(self):
        for left, right, whole in (
            ("This", "Path", "ThisPath"),
            ("This", "Region", "ThisRegion"),
            ("This", "Interval", "ThisInterval"),
        ):
            with self.subTest(parts=(left, right)):
                pair = self.codec.forward[left] + self.codec.forward[right]
                single = self.codec.forward[whole]
                self.assertNotEqual(pair, single)
                self.assertEqual(self.codec.decode(pair), left + " " + right)
                self.assertEqual(self.codec.encode(self.codec.decode(pair)).replace(" ", ""), pair)
                self.assertEqual(self.codec.decode(single), whole)
                self.assertEqual(self.codec.encode(self.codec.decode(single)), single)

    def test_approved_adjacent_glyphs_preserve_codepoints(self):
        # Covers registered-root collisions, numeric @, and broader two-rune joins.
        probes = ("This", "Path", "Region", "Interval", "Life", "Move", "@")
        for left in self.codec.forward:
            for right in probes:
                with self.subTest(left=left, right=right):
                    glyphs = self.codec.forward[left] + self.codec.forward[right]
                    self.assertEqual(self.codec.encode(self.codec.decode(glyphs)).replace(" ", ""), glyphs)
        glyphs = "".join(self.codec.forward[s] for s in
                         ("Life", "This", "Interval", "Move", "This", "Path"))
        self.assertEqual(self.codec.encode(self.codec.decode(glyphs)).replace(" ", ""), glyphs)

    def test_unassigned_spares_and_mixed_text_are_not_reinterpreted(self):
        assignments = json.loads(
            (ROOT / "language/core/glyph_assignments.json").read_text(encoding="utf-8")
        )
        first_spare = assignments["spares"][0]["temporary_character"]
        original = "UnknownText " + self.codec.forward["This"] + first_spare + self.codec.forward["Path"] + "!"
        decoded = self.codec.decode(original)
        self.assertIn(first_spare, decoded)
        self.assertEqual(self.codec.encode(decoded), original)

    @unittest.skipUnless(shutil.which("node"), "Node.js not installed")
    def test_browser_python_parity_for_handwritten_glyph_streams(self):
        html = (ROOT / "assets/glyphs/references/idylwild/keyboard_kit/meaning_keyboard.html"
                ).read_text(encoding="utf-8")
        match = re.search(r'<script id="glyph-codec">([\s\S]+?)</script>', html)
        self.assertIsNotNone(match)
        raw = [
            self.codec.forward["This"] + self.codec.forward["Interval"],
            self.codec.forward["This"] + self.codec.forward["Path"],
            self.codec.forward["This"] + self.codec.forward["Region"],
            self.codec.forward["ThisInterval"],
            "".join(self.codec.forward[s] for s in ("Life", "This", "Interval", "Move")),
            self.codec.forward["@"] * 3,
        ]
        script = (match.group(1) + "\nconst raw=" + json.dumps(raw, ensure_ascii=False)
                  + ";process.stdout.write(JSON.stringify(raw.map(t=>"
                  + "[CuspellGlyphCodec.fromGlyphs(t),"
                  + "CuspellGlyphCodec.toGlyphs(CuspellGlyphCodec.fromGlyphs(t))])));")
        run = subprocess.run(["node", "-e", script], capture_output=True, text=True,
                             encoding="utf-8", check=True)
        actual = json.loads(run.stdout)
        expected = [[self.codec.decode(t), self.codec.encode(self.codec.decode(t))] for t in raw]
        self.assertEqual(actual, expected)
        self.assertTrue(all(back.replace(" ", "") == source for (_, back), source in zip(actual, raw)))


if __name__ == "__main__":
    unittest.main()
