# Writing Cuspell with glyphs

_Status: Language v1.0 approved writing and Windows-font instructions (2026-11-22)._

Cuspell has **217 approved rune glyphs**, a separate numeric-one sign `@`, 16 approved spare designs and 13 unchanged punctuation/grammar signs.

## Which font to use

For approved tight, word-like spacing on Windows, use the **Cuspell Language v1.0 Windows Font Kit** attached to the [release](../docs/release/LANGUAGE_V1_0_RELEASE_NOTES.md). Install **CuspellCompactWinTest-Regular.ttf**, open the kit's included `meaning_keyboard.html`, and select **Cuspell Compact WinTest** in Notepad. This exact font binary passed a real-PC Unicode save/reopen/decode test. The original Cuspell 234 Review and earlier Compact fonts are preserved separately.

## Using the keyboard

1. Keep `CuspellCompactWinTest-Regular.ttf` and `.woff2` in the extracted Language v1.0 Windows kit directory.
2. Open the v1.0 Windows kit's included `meaning_keyboard.html` from the same directory. It works offline.
3. Type `Move This There!` on the left, then press **Convert → glyphs**. Paste glyphs on the right and press **Decode → names** for the reverse.
4. For variable handles, use rune labels like `Create :«This» ... $«This» ...!` rather than `x:Entity`. General binders can infer types from unique typed uses; when inference is ambiguous, use a Cuspell type witness such as `:«This»:ThisExplanation` or `:«This»:MassSelf`. Standalone `:` closes a flat Sequence/Concurrent group.
5. Search a rune name or original G/R/A design ID and click its glyph to insert the name into the left editor.

## What converts

- Exact registered names are one glyph, so `ThisInterval` is different from `This Interval`. If you manually place the separate `This` and `Interval` glyphs together, decoding inserts the needed space (`This Interval`) rather than mistaking them for the single `ThisInterval` rune. The same rule protects `ThisPath` and `ThisRegion`.
- Uniquely decomposable tight local writing such as `LifeThis` becomes two adjacent signs.
- Every `@` becomes the numeric-one glyph, including repeated `@@`.
- Punctuation, quotation delimiters `«»`, parentheses, braces, commas, `_`, `$` and variable names remain intact; quoted content is not expanded as a Name or interpreted as a magical command.
- Unrecognized words and the 16 spare font glyphs remain unchanged. The decoder may add a disambiguating **space** to a manually assembled glyph stream; re-encoding preserves rune identities and order but may add a space between originally adjacent glyphs; not every raw glyph layout or original Latin spacing choice can be recovered. This converter does not claim Cuspell grammatical validity.

## Copying to another application

All approved fonts use U+E000–U+E0E9 private-use codepoints. Select **Cuspell Compact WinTest** in Notepad for approved word-like spacing (or **Cuspell 234 Review** for historical comparisons). Other fonts may show boxes. The 234-design font, its original ID keyboard, and historical ZIP are preserved. To validate syntax and mana, decode to Latin and use the Cuspell reference parser.

The [PC font acceptance check](PC_FONT_CHECK.md) has passed in Windows Notepad, including UTF-8 save/reopen/decode. No additional user font test is required for Language v1.0; the playable game magic engine remains out of scope.


### Native binder shorthand

Canonical v0.10 typing allows `All :«This» Life $«This».` with no English type word. When a type cannot be inferred uniquely, use an existing rune or tight composition such as `:«This»:ThisExplanation` or `:«This»:MassSelf`. The parser enforces ambiguity and variable-scope rules; the font and keyboard simply convert script.
