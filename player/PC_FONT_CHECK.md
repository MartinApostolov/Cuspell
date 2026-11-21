# Language v1.0 — PC font and typing acceptance check

_Status: user-run release gate, not yet signed off. Keep the approved glyph assignments, punctuation and existing font unchanged until failures have been reviewed._

This check confirms that Cuspell works outside the GitHub tests, on your actual computer. It is **not** a review of spell balance or a request to reapprove all 217 rune drawings.

## 1. Prepare the existing files

1. Download/extract the existing [Cuspell Codex Keyboard Kit](../assets/glyphs/references/idylwild/keyboard_kit/Cuspell_Codex_Keyboard_Kit.zip). Install **CuspellCodexReview-Regular.ttf** if it is not already installed; choose font family **Cuspell 234 Review** in a text editor/word processor.
2. Separately save [meaning_keyboard.html](../assets/glyphs/references/idylwild/keyboard_kit/meaning_keyboard.html) beside the extracted TTF/WOFF2. It is **not** in the preserved historical ZIP. Open it in a browser, even without internet.
3. Keep [chart.html](../assets/glyphs/references/idylwild/keyboard_kit/chart.html) available as the complete 234-design reference. Do not uninstall an existing font before verifying the installed family name.

If your operating system does not support installing TTF or your application cannot select the font, report that rather than claiming a glyph-rendering failure.

## 2. Meaning-aware keyboard and Unicode text

Enter each line on the left side of the meaning-aware page; click **Convert → glyphs**, then **Decode → names**:

```text
Move This There!
Create x:Entity At $x There Change $x Light «LightUnit» @!
LifeThis And MagicThis.
ThisInterval This Interval.
ThisPath This Path.
ThisRegion This Region.
```

Check that the original Latin input comes back exactly and glyphs do not appear as replacement boxes in the font preview. The one-rune versions (`ThisInterval`, `ThisPath`, `ThisRegion`) must each look different from the corresponding two-rune sequence. For a *manually joined* pair of rune glyphs, decoding may introduce a separating space so that the two rune identities are not swallowed into one root. That extra space is deliberate.

Also search for a rune by name and by original G/A/R ID, click its palette tile, then confirm it inserts the requested meaning.

## 3. Copy/paste/save test

1. Copy glyph output from the browser into at least one independent plain-text editor and one word processor if available. Select **Cuspell 234 Review** in the destination; the glyphs may show boxes until the font is chosen.
2. Save a **UTF-8** plain-text file, close and reopen it. Paste the saved glyphs back into the keyboard's right-hand editor, use **Decode → names**, and compare the original Cuspell text. Include the `«LightUnit»` quote, `x:Entity` binder, `$x` reference, numeric `@`, and punctuation in the test.
3. Make sure text order, the `@!?` marks, quotation marks, colon, and underscores do not disappear or turn into Unicode replacement characters (`�`). If an editor changes a font when reopening, selecting the Cuspell font again is okay; losing codepoints is not.

Do not use a screenshot as the only preservation check: a screenshot can look fine while its copied Unicode data is broken.

## 4. Readability at actual sizes

Check ordinary multi-rune lines at **34 px** and **32 px**, then try **20 px** as the previously agreed *minimum*, not the default target. Also skim the full [234-design chart](../assets/glyphs/references/idylwild/keyboard_kit/chart.html) for clipping or missing marks.

Specifically compare the four consciously approved exact mirrored pairs:

| Rune A | Rune B | Source design IDs |
| --- | --- | --- |
| Part | Group | G015 / G016 |
| ThisEvent | When | G021 / G022 |
| Rule | Directive | G121 / G122 |
| Happen | Counterfactual | G129 / G130 |

At 32–34 px, also check the seven additional higher-similarity pairs recorded in [approved final review](../assets/glyphs/references/idylwild/meaning_assignments/draft_08.json), especially **Surface / Overlap**, **Unique / CompassionFor**, **UnavailableValueOf / Area**, **MinBy / At**, **Rate / Most**, **All / Filter**, and **At / MaxBy**.

You already approved these glyph designs. This pass asks only whether they remain legible and distinguishable *in practical use*. A failure should be reported as a particular pair, size and application—not silently changed.

## 5. What to report back

A short message is sufficient:

- **Operating system and apps tested:** (e.g. Windows + browser, Notepad, word processor)
- **Typing/decoding:** pass / fail
- **UTF-8 save/reopen/copy:** pass / fail
- **34 px, 32 px, 20 px legibility:** pass / issue (state which size)
- **Mirrored/high-similarity pairs:** acceptable / list problematic pairs
- **Any missing punctuation or clipped glyph:** none / IDs/details

Only provide screenshots for visual failures or difficult-to-explain rendering problems. No need to review every meaning assignment again.

After this passes, the remaining language-only work is to freeze and tag the reviewed normative bundle as Language v1.0 and prepare the release manifest; a gameplay system is not a requirement.
