# Cuspell original PC font and meaning-aware writing

1. Download and extract Cuspell_Codex_Keyboard_Kit.zip.
2. Install CuspellCodexReview-Regular.ttf. Select font family Cuspell 234 Review in your word processor.
3. Open keyboard.html from the extracted folder, click glyphs to type, and copy/paste the result. chart.html is the printable catalog.
4. Test at 32–34px or larger (minimum 20px). The glyph meanings have been approved; report spacing or readability problems before releasing a separately named final font.

Contains exactly 234 source glyphs and 13 approved punctuation marks. Private use U+E000–U+E0E9 maps to G/A/R source glyph IDs in glyph_map.csv. Although all 217 rune meanings plus numeric `@` now have approved mappings in `language/core/glyph_assignments.json`, this preserved PC test font and keyboard still use their original nonsemantic selection/typing behavior. The separate meaning-aware typing workflow is available in the new `meaning_keyboard.html`, which is intentionally not part of the historical ZIP. Save/open it next to the original TTF/WOFF2 from a checkout or download it into the extracted kit folder.

## Language v1.0 typing workflow

Open [meaning_keyboard.html](meaning_keyboard.html) in your browser from the keyboard-kit folder. The page works offline using the unchanged font.

- Write `Move This There!` on the left, then choose Convert to glyphs; paste PUA glyphs on the right to decode them back to rune names.
- Search any of the 217 rune names (or `@`) or G/R/A source IDs and click its tile to insert the correct transliteration.
- The exact rune `ThisInterval` takes priority over the two-rune sequence `This Interval`. Tight forms such as `LifeThis` convert only if their decomposition is unique. When **decoding glyph-origin text**, adjoining `This` and `Interval` glyphs acquire a separating space so they cannot be confused with the single `ThisInterval` glyph. The same applies to `ThisPath` and `ThisRegion`.
- Quoted `«... »` Old/New Names, arbitrary names, variable labels, grammar punctuation, spaces and line breaks are preserved exactly through round trips; there is no magical Name expansion.
- Unrecognized Latin words and the 16 approved spare font glyphs are preserved, never silently assigned meanings. The decoder may insert spaces in a raw sequence of approved glyphs when needed to retain the exact glyph sequence on re-encoding.
- To display copied private-use glyphs in another application, install and select **Cuspell 234 Review**. In other fonts they may display as boxes.
- The converter is orthographic, not a parser; use `check`, `parse`, or `mana` on transliteration for language validation.

Command-line alternatives from the repo root:

```bash
python run_cuspell.py to-glyphs 'Move This There!'
python run_cuspell.py from-glyphs '<paste copied private-use glyphs here>'
```

The 234-glyph legacy keyboard, chart, ZIP, font binaries, source SVGs, glyph IDs and PUA mapping are unchanged. For the remaining installed-font acceptance step, see [PC_FONT_CHECK.md](../../../../../player/PC_FONT_CHECK.md).

## New proportional release candidate

The separately named [Cuspell Compact PC Kit](../compact_font/Cuspell_Compact_PC_Kit.zip) is built from this unchanged review font but uses narrower, proportional glyph advances. Install **Cuspell Compact**, not **Cuspell 234 Review**, when evaluating the new close-together rune spacing. It includes its own meaning-aware offline keyboard and preserves the approved glyph designs, mapping and old kit.
