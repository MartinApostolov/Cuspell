# Language v1.0 — PC font and typing acceptance check

_Status: **Windows PC acceptance PASS (2026-11-22)** — Cuspell Compact WinTest displays in Notepad; the user successfully saved, reopened and decoded glyph text, with the uploaded UTF-8 file independently verified. VS Code remains optional and outside Language v1.0. Approved designs and original review font remain preserved. [Acceptance evidence](../docs/release/LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md)._

This check confirms that Cuspell works outside the GitHub tests, on your actual computer. It is **not** a review of spell balance or a request to reapprove all 217 rune drawings.

## Completed required PC check (Windows Notepad only)

**Completed and accepted.** The procedure below documents the test that passed; it is retained for repeatability, not because the user needs to run it again. No VS Code setup or repeated glyph approval is required.

1. Open the **WinTest kit's** `meaning_keyboard.html`. In the left **Transliteration** box enter these two lines, then select **Convert → glyphs**:

   ```text
   All :«This» Life $«This».
   Create :«This» At $«This» There Change $«This» Light «LightUnit» @!
   ```

2. Click **Copy glyph text**. Paste into Windows **Notepad**, select **Cuspell Compact WinTest**, and save a plain-text file named `Cuspell-v1-test.txt` in **UTF-8**.
3. Completely close Notepad, then reopen that file. If necessary, reselect **Cuspell Compact WinTest**; a `.txt` file stores Unicode characters, not its font choice.
4. Copy the reopened glyph text into the keyboard's right **Glyph writing** box and press **Decode → names**. Check that the two original Cuspell lines, including `:«This»`, `$«This»`, `«LightUnit»`, `@`, and sentence punctuation, return exactly.
5. Report **PASS** if the round trip is unchanged, otherwise **FAIL** and paste the decoded text. Screenshots are only needed if the glyphs display incorrectly.

The longer visual/comparison tests below are reference and troubleshooting material; **VS Code is not a release requirement**.

## Windows-only diagnosis: runes show as boxes in Notepad and VS Code

If the browser's glyph page looks correct but Windows Notepad and VS Code show
square/question-mark placeholders, **do not change the rune mappings or the
language grammar**. The initial Compact TTF has Windows Unicode cmap entries,
but lacks ordinary Latin character coverage and some Windows font-style/codepage
metadata. The separate [Cuspell Compact WinTest kit](../assets/glyphs/references/idylwild/windows_test_font/Cuspell_Compact_WinTest_Kit.zip)
tests whether these font-selection details are the cause.

1. Install `CuspellCompactWinTest-Regular.ttf` from the WinTest ZIP. **Do not
   uninstall the other Cuspell fonts yet.** This is a separately named family,
   **Cuspell Compact WinTest**, to avoid Windows font-cache collisions.
2. Keep your other VS Code settings, but set
   `"editor.fontFamily": "'Cuspell Compact WinTest', Consolas, monospace"`.
   Use 32 px for the visual test if practical, save settings, and reload VS Code.
3. Open the WinTest ZIP's **own** `meaning_keyboard.html`, convert the current
   Create sample below, copy its **glyph** output and paste into VS Code.
4. In classic Notepad use **Format → Font** to select **Cuspell Compact WinTest**
   explicitly before comparing. In modern Notepad select the font from Settings.
   Simply pasting into the default Notepad font does not test the installed font.
5. Tell us whether the same glyph text renders in **both** programs. If it
   still shows squares, this candidate has not solved the Windows issue; send a
   screenshot and the selected font family.

WinTest adds display-only basic Latin fallback outlines and Windows metadata.
It changes **none** of the 234 approved PUA drawings, punctuation drawings,
Unicode assignments or compact advance widths. It is a diagnostic candidate,
a separately named Windows-compatible font whose Notepad and UTF-8 acceptance has now passed; final release packaging remains a separate maintainer task.

## 1. Install the compact, closer-spaced candidate

1. Download/extract the new [Cuspell Compact PC Kit](../assets/glyphs/references/idylwild/compact_font/Cuspell_Compact_PC_Kit.zip). Install **CuspellCompact-Regular.ttf** (font family **Cuspell Compact**) and select that family in VS Code or your word processor. This is the revised proportionally spaced font; do **not** choose **Cuspell 234 Review** when evaluating spacing.
2. Open the included **meaning_keyboard.html** beside the compact TTF/WOFF2. It works offline and automatically selects the compact font for its preview.
3. Keep the [original 234-design chart](../assets/glyphs/references/idylwild/keyboard_kit/chart.html) available as a glyph-ID reference. The original review font and ZIP remain intact and can be compared, but need not be uninstalled.

If your operating system does not support installing TTF or your application cannot select the font, report that rather than claiming a glyph-rendering failure.

## 2. Meaning-aware keyboard and Unicode text

Enter each line on the left side of the meaning-aware page; click **Convert → glyphs**, then **Decode → names**:

```text
Move This There!
Create :«This» At $«This» There Change $«This» Light «LightUnit» @!
LifeThis And MagicThis.
ThisInterval This Interval.
ThisPath This Path.
ThisRegion This Region.
```

Check that the original Latin input comes back exactly and glyphs do not appear as replacement boxes in the font preview. The one-rune versions (`ThisInterval`, `ThisPath`, `ThisRegion`) must each look different from the corresponding two-rune sequence. For a *manually joined* pair of rune glyphs, decoding may introduce a separating space so that the two rune identities are not swallowed into one root. That extra space is deliberate.

Also search for a rune by name and by original G/A/R ID, click its palette tile, then confirm it inserts the requested meaning.

## 3. Copy/paste/save test

1. Copy glyph output from the browser into at least one independent plain-text editor and one word processor if available. Select **Cuspell Compact** in the destination; the glyphs may show boxes until the font is chosen.
2. Save a **UTF-8** plain-text file, close and reopen it. Paste the saved glyphs back into the keyboard's right-hand editor, use **Decode → names**, and compare the original Cuspell text. Include the `«LightUnit»` quotation, `:«This»` binder, `$«This»` reference, numeric `@`, and punctuation in the test.
3. Make sure text order, the `@!?` marks, quotation marks, colon, and underscores do not disappear or turn into Unicode replacement characters (`�`). If an editor changes a font when reopening, selecting the Cuspell font again is okay; losing codepoints is not.

Do not use a screenshot as the only preservation check: a screenshot can look fine while its copied Unicode data is broken.

## 4. Readability at actual sizes

Compare the new Compact font with the original review font if useful; the Compact font should have proportional rune widths and roughly 1–2 px total inter-rune side bearing at 32–34 px on narrow marks. Check ordinary multi-rune lines at **34 px** and **32 px**, then try **20 px** as the previously agreed *minimum*, not the default target. Also skim the full [234-design chart](../assets/glyphs/references/idylwild/keyboard_kit/chart.html) for clipping or missing marks.

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

The Windows test has passed. The remaining language-only work is to freeze and tag the reviewed normative bundle as Language v1.0 and prepare the release manifest; a gameplay system is not a requirement.
