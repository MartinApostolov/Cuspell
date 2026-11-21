#!/usr/bin/env python3
"""Make a Windows font-selection compatibility candidate from Cuspell Compact.

Do NOT overwrite the approved original or the previous Cuspell Compact font.
Preserve PUA glyph contours/codepoints/advances and add Latin fallback glyphs
and standard Windows OS/2 declarations used by common text applications.

The source of the Latin fallback subset is DejaVu Sans Mono (Bitstream Vera
license); it provides legible ASCII for mixed-script font selection, NOT any
new Cuspell meaning, root, or punctuation rule.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import zipfile

from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "compact_font" / "CuspellCompact-Regular.ttf"
SOURCE_KEYBOARD = BASE / "compact_font" / "meaning_keyboard.html"
DEST = BASE / "windows_test_font"
DONOR = Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")
FAMILY = "Cuspell Compact WinTest"
FILENAME = "CuspellCompactWinTest-Regular"
PUA = set(range(0xE000, 0xE0EA))
APPROVED_PUNCTUATION = set(map(ord, ".:?!«»$()_{},"))
LATIN = set(range(0x21, 0x7F))  # excludes space, keeps reserved Cuspell punctuation

# DejaVu / Bitstream Vera font distribution license. Retained in the ZIP.
LICENSE = """DejaVu Sans Mono Latin fallback glyphs
Original font copyright (c) 2003 Bitstream, Inc. All Rights Reserved.
Bitstream Vera is a trademark of Bitstream, Inc.
DejaVu changes are in the public domain.

Permission is hereby granted, free of charge, to any person obtaining a
copy of the fonts accompanying this license ("Fonts") and associated
documentation files (the "Font Software"), to reproduce and distribute
the Font Software, including without limitation the rights to use, copy,
merge, publish, distribute, and/or sell copies of the Font Software,
and to permit persons to whom the Font Software is furnished to do so,
subject to the following conditions:

The above copyright and trademark notices and this permission notice
shall be included in all copies of one or more of the Font Software
typefaces.

The Font Software may be modified, altered, or added to, and in particular
the designs of glyphs or characters in the Fonts may be modified and
additional glyphs or characters may be added to the Fonts, only if the fonts
are renamed to names not containing either the words "Bitstream" or "Vera".

The Font Software may be sold as part of a larger software package but
no copy of one or more of the Font Software typefaces may be sold by itself.

THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT OR OTHER RIGHT. IN NO EVENT SHALL BITSTREAM OR
THE GNOME FOUNDATION BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM OTHER DEALINGS
IN THE FONT SOFTWARE.

Except as contained in this notice, the names of Gnome, the Gnome
Foundation, and Bitstream Inc., shall not be used in advertising or
otherwise to promote the sale, use or other dealings in the Font
Software without prior written authorization from the Gnome Foundation
or Bitstream Inc. For further information, contact: fonts at gnome dot org.
"""

def build():
    if not DONOR.is_file():
        raise FileNotFoundError(f"Install fonts-dejavu-core on build runner: {DONOR}")
    DEST.mkdir(parents=True, exist_ok=True)
    font = TTFont(SOURCE)
    original_map = font.getBestCmap().copy()
    if not (PUA | APPROVED_PUNCTUATION).issubset(original_map):
        raise AssertionError("Source Compact font lacks approved mappings")
    old_metrics = {original_map[cp]: font["hmtx"].metrics[original_map[cp]]
                   for cp in PUA | APPROVED_PUNCTUATION}

    donor = TTFont(DONOR)
    donor_map = donor.getBestCmap()
    donor_set = donor.getGlyphSet()
    scale = font["head"].unitsPerEm / donor["head"].unitsPerEm
    latin_added = {}
    names = font.getGlyphOrder()
    for cp in sorted(LATIN - set(original_map)):
        donor_name = donor_map.get(cp)
        if not donor_name:
            raise AssertionError(f"DejaVu missing U+{cp:04X}")
        # Draw through a decomposing pen so no donor composite component can
        # retain a reference to a glyph absent from the destination font.
        recorder = DecomposingRecordingPen(donor_set)
        donor_set[donor_name].draw(recorder)
        pen = TTGlyphPen(None)
        recorder.replay(TransformPen(pen, (scale, 0, 0, scale, 0, 0)))
        glyph = pen.glyph()
        name = f"latin_u{cp:04X}"
        font["glyf"].glyphs[name] = glyph
        glyph.recalcBounds(font["glyf"])
        advance = round(donor["hmtx"].metrics[donor_name][0] * scale)
        left = getattr(glyph, "xMin", 0)
        font["hmtx"].metrics[name] = (max(advance, getattr(glyph, "xMax", 0) + 16), left)
        names.append(name)
        latin_added[cp] = name
    font.setGlyphOrder(names)
    font["maxp"].numGlyphs = len(names)
    for table in font["cmap"].tables:
        if table.isUnicode():
            table.cmap.update(latin_added)

    os2 = font["OS/2"]
    os2.ulCodePageRange1 |= 1  # Latin-1 Windows codepage, now genuinely supported
    os2.fsSelection |= 0x40   # regular-style bit
    os2.recalcUnicodeRanges(font)
    os2.usFirstCharIndex = min(font.getBestCmap())
    os2.usLastCharIndex = max(font.getBestCmap())
    os2.xAvgCharWidth = round(
        sum(font["hmtx"].metrics[font.getBestCmap()[ord(c)]][0]
            for c in "abcdefghijklmnopqrstuvwxyz") / 26)
    font["post"].isFixedPitch = 0  # Original Cuspell runes are proportional

    replacements = {
        1: FAMILY, 2: "Regular",
        3: "CuspellCompactWinTest-2026-11",
        4: FAMILY + " Regular",
        5: "Version 1.1; Windows font-selection test; 2026-11",
        6: "CuspellCompactWinTest-Regular",
        16: FAMILY, 17: "Regular"
    }
    for record in font["name"].names:
        if record.nameID in replacements:
            record.string = replacements[record.nameID].encode(record.getEncoding())

    ttf = DEST / (FILENAME + ".ttf")
    font.flavor = None
    font.save(ttf)
    font.flavor = "woff2"
    font.save(DEST / (FILENAME + ".woff2"))
    donor.close()
    font.close()

    # Verify Windows Unicode cmap, expanded Latin coverage and untouched PUA.
    test = TTFont(ttf)
    new_map = test.getBestCmap()
    for cp in PUA | APPROVED_PUNCTUATION:
        if new_map[cp] != original_map[cp]:
            raise AssertionError(f"Altered approved map U+{cp:04X}")
        if test["hmtx"].metrics[new_map[cp]] != old_metrics[new_map[cp]]:
            raise AssertionError(f"Altered approved metrics U+{cp:04X}")
    for cp in range(0x21, 0x7F):
        if cp not in new_map:
            raise AssertionError(f"Latin font coverage missing U+{cp:04X}")
    if not any(t.platformID == 3 and t.platEncID == 1 and t.isUnicode()
               for t in test["cmap"].tables):
        raise AssertionError("Windows Unicode cmap missing")
    if not (test["OS/2"].ulCodePageRange1 & 1):
        raise AssertionError("Windows Latin code page range missing")
    if not (test["OS/2"].fsSelection & 0x40):
        raise AssertionError("Windows regular-style flag missing")
    if test["name"].getDebugName(1) != FAMILY:
        raise AssertionError("Incorrect distinct Windows test font family")
    test.close()

    source_html = SOURCE_KEYBOARD.read_text(encoding="utf-8")
    if source_html.count("CuspellCompact-Regular") < 2:
        raise AssertionError("Unexpected Compact HTML font URLs")
    html = source_html.replace("CuspellCompact-Regular", FILENAME)
    (DEST / "meaning_keyboard.html").write_text(html, encoding="utf-8")
    (DEST / "DEJAVU-LICENSE.txt").write_text(LICENSE, encoding="utf-8")
    manifest = {
        "status": "WINDOWS_RENDERING_DIAGNOSTIC_ONLY",
        "font_family": FAMILY, "source_font": "Cuspell Compact",
        "font_file": ttf.name, "source_sha256": sha256(SOURCE.read_bytes()).hexdigest(),
        "ttf_sha256": sha256(ttf.read_bytes()).hexdigest(),
        "approved_designs_unchanged": 234,
        "approved_punctuation_unchanged": 13,
        "pua_map_unchanged": True,
        "additional_latin_glyphs": len(latin_added),
        "windows_unicode_cmap": True,
        "latin_codepage_bit": True,
        "regular_style_bit": True,
        "spacing": "Identical to Cuspell Compact"
    }
    (DEST / "font_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (DEST / "README.md").write_text(
        "# Cuspell Compact WinTest — Windows rendering diagnosis\n\n"
        "This is a separately named compatibility experiment. Do not replace "
        "or uninstall the existing Cuspell Compact font yet.\n\n"
        "1. Install **CuspellCompactWinTest-Regular.ttf** as a new Windows font.\n"
        "2. In VS Code set `editor.fontFamily` to "
        "`\"'Cuspell Compact WinTest', Consolas, monospace\"`.\n"
        "3. Open the included offline `meaning_keyboard.html`, convert "
        "`Create :«This» At $«This» There Change $«This» Light «LightUnit» @!` "
        "and paste the glyph output in VS Code.\n"
        "4. Also choose **Cuspell Compact WinTest** explicitly in Notepad. "
        "If both apps render runes, Windows font selection was the problem.\n\n"
        "Spacing, all 234 PUA outlines and 13 approved punctuation are unchanged. "
        "The only new characters are display-only basic Latin fallback glyphs "
        "from DejaVu Sans Mono, under the included license. This adds no Cuspell meanings.\n",
        encoding="utf-8")
    zip_path = DEST / "Cuspell_Compact_WinTest_Kit.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name in (FILENAME + ".ttf", FILENAME + ".woff2",
                     "meaning_keyboard.html", "font_manifest.json",
                     "README.md", "DEJAVU-LICENSE.txt"):
            z.write(DEST / name, name)
    print("Windows font test OK:", len(latin_added),
          "Latin fallback glyphs, original PUA mapping and spacing intact")

if __name__ == "__main__":
    build()
