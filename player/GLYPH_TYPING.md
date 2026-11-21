# Writing Cuspell with glyphs

_Status: Language v1.0 typing preparation (2026-11-21)._

Cuspell has **217 approved rune glyphs**, a separate numeric-one sign `@`, 16 approved spare designs and 13 unchanged punctuation/grammar signs.

## Using the keyboard

1. Keep `CuspellCodexReview-Regular.ttf` or `.woff2` in the `assets/glyphs/references/idylwild/keyboard_kit/` directory.
2. Save/open [meaning_keyboard.html](../assets/glyphs/references/idylwild/keyboard_kit/meaning_keyboard.html) in that same directory. It works offline.
3. Type `Move This There!` on the left, then press **Convert → glyphs**. Paste glyphs on the right and press **Decode → names** for the reverse.
4. For variable handles, use approved punctuation and rune labels such as `Create :«This» ... $«This» ...!` rather than Latin `x:Entity`. In general binders, add a Cuspell type witness such as `:«This»:This` (Entity) or `:«Here»:Here` (Location). The standalone `:` closes a flat Sequence/Concurrent group.\n5. Search a rune name or original G/R/A design ID and click its glyph to insert the name into the left editor.

## What converts

- Exact registered names are one glyph, so `ThisInterval` is different from `This Interval`. If you manually place the separate `This` and `Interval` glyphs together, decoding inserts the needed space (`This Interval`) rather than mistaking them for the single `ThisInterval` rune. The same rule protects `ThisPath` and `ThisRegion`.
- Uniquely decomposable tight local writing such as `LifeThis` becomes two adjacent signs.
- Every `@` becomes the numeric-one glyph, including repeated `@@`.
- Punctuation, quotation delimiters `«»`, parentheses, braces, commas, `_`, `$` and variable names remain intact; quoted content is not expanded as a Name or interpreted as a magical command.
- Unrecognized words and the 16 spare font glyphs remain unchanged. The decoder may add a disambiguating **space** to a manually assembled glyph stream; re-encoding preserves rune identities and order but may add a space between originally adjacent glyphs; not every raw glyph layout or original Latin spacing choice can be recovered. This converter does not claim Cuspell grammatical validity.

## Copying to another application

Because the approved review font uses U+E000–U+E0E9 private-use codepoints, select **Cuspell 234 Review** in the destination editor. Other fonts may show boxes. The 234-design font, its original ID keyboard, and historical ZIP are preserved. To validate syntax and mana, decode to Latin and use the Cuspell reference parser.

Before final release, follow the [PC font acceptance check](PC_FONT_CHECK.md) and report any unreadable/mirrored pairs or copy/paste failures. Language v1.0 still requires real-PC acceptance and an explicit version freeze; the playable game magic-engine work is outside scope.