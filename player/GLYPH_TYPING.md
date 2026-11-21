# Writing Cuspell with glyphs

_Status: Language v1.0 typing preparation (2026-11-21)._

Cuspell has **217 approved rune glyphs**, a separate numeric-one sign `@`, 16 approved spare designs and 13 unchanged punctuation/grammar signs.

## Using the keyboard

1. Keep `CuspellCodexReview-Regular.ttf` or `.woff2` in the `assets/glyphs/references/idylwild/keyboard_kit/` directory.
2. Save/open [meaning_keyboard.html](../assets/glyphs/references/idylwild/keyboard_kit/meaning_keyboard.html) in that same directory. It works offline.
3. Type `Move This There!` on the left, then press **Convert → glyphs**. Paste glyphs on the right and press **Decode → names** for the reverse.
4. Search a rune name or original G/R/A design ID and click its glyph to insert the name into the left editor.

## What converts

- Exact registered names are one glyph, so `ThisInterval` is different from `This Interval`.
- Uniquely decomposable tight local writing such as `LifeThis` becomes two adjacent signs.
- Every `@` becomes the numeric-one glyph, including repeated `@@`.
- Punctuation, quotation delimiters `«»`, parentheses, braces, commas, `_`, `$` and variable names remain intact; quoted content is not expanded as a Name or interpreted as a magical command.
- Unrecognized words and the 16 spare font glyphs remain unchanged. This converter does not claim Cuspell grammatical validity.

## Copying to another application

Because the approved review font uses U+E000–U+E0E9 private-use codepoints, select **Cuspell 234 Review** in the destination editor. Other fonts may show boxes. The 234-design font, its original ID keyboard, and historical ZIP are preserved. To validate syntax and mana, decode to Latin and use the Cuspell reference parser.

The playable game magic-engine work is outside Language v1.0.