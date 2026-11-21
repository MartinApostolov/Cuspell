#!/usr/bin/env python3
"""Build a separately named proportional Cuspell font without changing shapes or PUA.

Source font remains unchanged. Ink contours are TRANSLATED only, not scaled;
proportional advances reduce the extra space around narrow runes. The output
works in other programs (VS Code, word processors), not only HTML previews.
"""
from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path
from fontTools.ttLib import TTFont

BASE = Path(__file__).resolve().parent
LEGACY = BASE / "keyboard_kit"
OUT = BASE / "compact_font"
SOURCE = LEGACY / "CuspellCodexReview-Regular.ttf"
NAME = "Cuspell Compact"
FILENAME = "CuspellCompact-Regular"
# At 32 px, two adjacent signs have about 1.5 px of combined side bearings.
SIDE = 24
MIN_ADVANCE = 130
# Punctuation has separate glyphs; retain readable marks and whitespace.
PUNCT_SIDE = 25
PUNCT_MIN_ADVANCE = 135
SPACE_ADVANCE = 310

def build() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    font = TTFont(SOURCE)
    cmap = font.getBestCmap()
    raw = font["glyf"]
    used_pua = set(range(0xE000, 0xE0EA))
    punctuation = ".:?!«»$()_{},"
    expected = used_pua | {ord(c) for c in punctuation}
    if not expected.issubset(cmap):
        raise ValueError("Original font must include all 234 designs + 13 punctuation")
    old_widths = {}
    new_widths = {}
    for cp in sorted(expected):
        name = cmap[cp]
        glyph = raw[name]
        if glyph.isComposite():
            raise ValueError(f"Unexpected composite source glyph: {name}")
        glyph.recalcBounds(raw)
        x_min, x_max = glyph.xMin, glyph.xMax
        width = x_max - x_min
        inset = SIDE if cp in used_pua else PUNCT_SIDE
        min_advance = MIN_ADVANCE if cp in used_pua else PUNCT_MIN_ADVANCE
        old_width, _ = font["hmtx"].metrics[name]
        new_width = max(width + 2 * inset, min_advance)
        shift = inset + (new_width - (width + 2 * inset)) // 2 - x_min
        # Shift contours only: preserve angles, shapes and their vertical positions.
        glyph.coordinates.translate((shift, 0))
        glyph.recalcBounds(raw)
        font["hmtx"].metrics[name] = (new_width, glyph.xMin)
        old_widths[name] = old_width
        new_widths[name] = new_width
    font["hmtx"].metrics[cmap[0x20]] = (SPACE_ADVANCE, 0)
    for record in font["name"].names:
        name_id = record.nameID
        if name_id == 1:
            record.string = NAME.encode(record.getEncoding())
        elif name_id == 3:
            record.string = b"CuspellCompact-2026-11".decode().encode(record.getEncoding())
        elif name_id == 4:
            record.string = (NAME + " Regular").encode(record.getEncoding())
        elif name_id == 6:
            record.string = b"CuspellCompact-Regular".decode().encode(record.getEncoding())
        elif name_id == 5:
            record.string = b"Version 1.0; 2026-11".decode().encode(record.getEncoding())
    font["head"].modified = 0
    ttf = OUT / (FILENAME + ".ttf")
    font.save(ttf)
    font.flavor = "woff2"
    woff = OUT / (FILENAME + ".woff2")
    font.save(woff)
    font.close()
    check = TTFont(ttf)
    if check.getBestCmap() != cmap:
        raise AssertionError("The original glyph mapping must remain exactly identical")
    if check["name"].getDebugName(1) != NAME:
        raise AssertionError("The compact font must have its own installable family")
    for cp in expected:
        glyph_name = cmap[cp]
        g = check["glyf"][glyph_name]
        g.recalcBounds(check["glyf"])
        ink_width = g.xMax - g.xMin
        advance, left = check["hmtx"].metrics[glyph_name]
        if g.xMin < 0 or advance < g.xMax or left != g.xMin:
            raise AssertionError(f"Glyph clipped: {glyph_name}")
        if advance < ink_width + 2 * (SIDE if cp in used_pua else PUNCT_SIDE) and advance != (MIN_ADVANCE if cp in used_pua else PUNCT_MIN_ADVANCE):
            raise AssertionError(f"Spacing too tight: {glyph_name}")
    check.close()

    # Duplicate the functionality of the approved meaning keyboard; replace
    # only the font resource path. The old kit remains byte-for-byte unchanged.
    keyboard = (LEGACY / "meaning_keyboard.html").read_text(encoding="utf-8")
    keyboard = keyboard.replace(
        'src:url("CuspellCodexReview-Regular.woff2") format("woff2"),url("CuspellCodexReview-Regular.ttf") format("truetype")',
        'src:url("CuspellCompact-Regular.woff2") format("woff2"),url("CuspellCompact-Regular.ttf") format("truetype")'
    )
    if 'CuspellCodexReview-Regular.woff2") format("woff2")' in keyboard:
        raise AssertionError("Meaning keyboard still selects the old font")
    (OUT / "meaning_keyboard.html").write_text(keyboard, encoding="utf-8")
    manifest = {
        "status": "LANGUAGE_V1_COMPACT_PC_TEST",
        "font_family": NAME,
        "source_font": str(SOURCE.relative_to(BASE)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "ttf_sha256": hashlib.sha256(ttf.read_bytes()).hexdigest(),
        "woff2_sha256": hashlib.sha256(woff.read_bytes()).hexdigest(),
        "pua_start": "E000", "pua_end": "E0E9",
        "approved_designs": 234, "punctuation": 13,
        "side_bearing_units": SIDE,
        "minimum_advance": MIN_ADVANCE,
        "space_advance": SPACE_ADVANCE,
        "mean_old_advance": round(sum(old_widths.values()) / len(old_widths), 1),
        "mean_new_advance": round(sum(new_widths.values()) / len(new_widths), 1),
        "source_preserved": True
    }
    (OUT / "font_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (OUT / "README.md").write_text(
        "# Cuspell Compact PC test font\n\n"
        "Install **CuspellCompact-Regular.ttf** (family **Cuspell Compact**) and "
        "open the included **meaning_keyboard.html** from the same folder. "
        "Type Cuspell, convert it to glyphs, and paste into an editor using Cuspell Compact. "
        "At 32–34 px, adjacent glyphs should be close like letters within a word. "
        "Try 20 px as a minimum and verify no overlapping/clipped contours.\n\n"
        "All glyph drawings and U+E000–U+E0E9 assignments come from the untouched "
        "Cuspell 234 Review source. Only left/right spacing and the installable "
        "font family name change. The original review TTF/WOFF2/ZIP remain preserved.\n",
        encoding="utf-8"
    )
    with zipfile.ZipFile(OUT / "Cuspell_Compact_PC_Kit.zip", "w", compression=zipfile.ZIP_DEFLATED) as z:
        for name in (FILENAME+".ttf", FILENAME+".woff2", "meaning_keyboard.html", "font_manifest.json", "README.md"):
            z.write(OUT / name, name)
    print("COMPACT FONT OK:", manifest["mean_old_advance"], "->", manifest["mean_new_advance"])

if __name__ == "__main__":
    build()
