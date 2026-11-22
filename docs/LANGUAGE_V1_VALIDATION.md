# Language v1.0 validation checklist

_Status: **Language v1.0 release source frozen (2026-11-22)**, Windows font/Unicode acceptance completed. The GitHub publication workflow creates tag `v1.0.0` after retesting the exact main commit. Release manifest: [LANGUAGE_V1_0_MANIFEST.json](release/LANGUAGE_V1_0_MANIFEST.json)._

Cuspell v1.0 is a **language** deliverable: syntax, meanings, names, writing, font-based script, documentation and testable tooling. World physics, RequiredPower, balance and a playable game engine are outside this release.

## Immutable choices for this pass

- Keep the approved 217 semantic-rune glyph assignments and the separate `@` numeric-one glyph.
- Keep 16 approved spare designs unassigned.
- Preserve the original 234-design font, installed name **Cuspell 234 Review**, 13 punctuation characters, PUA codepoints, original keyboard/chart, ZIP and source artwork.
- The normative parser input is canonical surface-v0.10 transliteration, which can be encoded into glyph writing without mandatory English type/variable words. Legacy v0.8 syntax remains parser-compatible; archived v0.8 is not current writing.

## Integration checks added

1. Test all **82** current `cuspell` example fields from `language/subsets/spellcraft_progression_v1.json` (34) and `language/subsets/spellcraft_beginner_v0_1.json` (48) through Latin -> glyph -> Latin. Compare validity, mana, normalized AST and diagnostics using the same parser.
2. Test all **204** registered Old Name spellings, including nested quotation, through the typography round trip.
3. Protect exact-root collisions: two separate glyphs `This` + `Interval` / `Path` / `Region` must not decode into a single exact-root spelling. The decoder can insert a disambiguating space, retaining the approved rune identities/order; glyph -> Latin -> glyph may add whitespace to a hand-packed sequence.
4. Exercise typed binders, `$name` references, Old Names, punctuation, optional-slot `_`, numeric `@`, flat control flow, newlines, font spares and mixed unknown text.
5. Check browser-to-Python codec parity on glyph-origin edge cases when Node.js is available.
6. Keep the already-existing per-glyph 218-assignment and 16-spare checks in `tests/test_meaning_glyph_keyboard.py`.
7. Read the **current, existing** executable tests for Yona (chapters 1–168), *Pride and Prejudice*, *Frankenstein*, and six additional sampled books (Alice, Treasure Island, Time Machine, Twenty Thousand Leagues, Origin of Species, Wealth of Nations). Verify Latin → glyph → Latin identity and reference-parser validity, AST, mana, diagnostics, including Yona-world contextual vocabulary.
8. Repeat over related Yona/cross-genre/corpus-gap test examples, and current inline code examples in player/maintainer documents, checking both valid and intentionally invalid parser outcomes without silently upgrading archived syntax.
9. Preserve literal spellings across all **329** Yona world-package New Names; the previously checked 204 Old Names remain separate. Historical seven-source report snippets are typography-only evidence, not newly normative translations.

Run automated checks from the repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The tests live in `tests/test_glyph_language_integration.py` and `tests/test_glyph_book_document_regression.py`. The latter extracts literal examples from maintained source regression tests and current documentation instead of maintaining a second, drifting copy of the book sentences. These are regression examples **sampled** from the named books, **not full translations of those books**. They do not prove that a spell is physically executable in every world.

## Final consistency audit (2026-11-22)

- Registry and inventory-role files agree: **217 one-mana rune entries**, **136 semantic primitive candidates**, **55 formal constructors**, **16 reference forms**, **10 domain values**, **276 semantic frames**, and **53 multi-frame entries**.
- Glyph assignment data agrees with the registry: **217 one-to-one rune mappings plus numeric-one `@`**, and **16 unassigned approved spare designs**. The original 234-glyph review font and 13 approved punctuation designs are unchanged. A separately named proportional Cuspell Compact font has been built without changing the glyph designs or PUA mapping.
- Player rune glossary and maintainer dictionary artwork remain covered by existing source-to-illustration regressions. The 204 Old Name player table entries have been checked for *both* sign coverage and exact recursive historical mana cost.
- Canonical surface v0.10, pipe-as-debug-only, flat control flow, release keyboard availability, and current versus historical checkpoint counts have been reconciled across the current specs, dictionary, player guide, README and mapping metadata. Machine truth remains normative; historical work stays archived.
- New regression guards in `tests/test_language_v1_consistency.py` cover these cross-layer invariants so a later edit cannot quietly restore old 212/131/265/48 counts.

## Rune-native pre-freeze audit (2026-11-22)

The [rune-native audit](release/LANGUAGE_V1_RUNE_NATIVE_AUDIT.md) verifies that **Explanation and Method already have usable Cuspell rune witnesses**, and replaces remaining live English binder examples without altering any approved rune. That audit identified binder-type inference, tight Cuspell witnesses and active-label shadowing as design decisions; all three were subsequently implemented and regression-tested in canonical surface v0.10. An atomic witness does not exist for every internal semantic type, but that does **not** justify adding one new root per type.

Windows **Notepad renders Cuspell Compact WinTest** with the approved glyphs, and the user has now confirmed the UTF-8 save / close / reopen / decode workflow. The uploaded 90-byte, two-line file was checked byte-for-byte against the current rune assignments with no replacement characters. See [PC Unicode acceptance](release/LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md). VS Code remains optional and out of scope.

## Language v1.0 release acceptance gates

- [x] Run script/parser round-trip checks over preserved representative book, cross-genre, Yona, corpus-gap, and current-document examples. Existing book test methods remain the source of their validity assertions; archived passages are not promoted to normative syntax.
- [x] Confirm the **Cuspell Compact WinTest** font visually renders the approved glyphs in Windows Notepad; the user approved the result and explicitly excluded VS Code from the Language v1.0 requirement. Additional legibility comparisons remain optional unless a defect is reported.
- [x] **User's final PC gate:** Cuspell Compact WinTest in Notepad; UTF-8 `.txt` saved, reopened and decoded back to the two original Cuspell sentences. Uploaded file verified to match approved Unicode mappings exactly. [Acceptance evidence](release/LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md).
- [x] Accept WinTest as the working Windows font after successful real-PC display and Unicode preservation; retain the original and earlier Compact packages unchanged. No remaining PC-only defects were reported.
- [x] Create the rune-native v0.9 binder syntax and new standalone punctuation closer, preserving old v0.8 in archive.
- [x] Reconcile normative registry, syntax, dictionary, player documentation, glyph metadata, and historical-vs-current counts; add regression guards.
- [x] Freeze the Language v1.0 canonical registry, grammar (surface v0.10), meanings, glyphs and Windows-accepted font at tagged commit `v1.0.0`. [Versioned manifest](release/LANGUAGE_V1_0_MANIFEST.json), [release notes](release/LANGUAGE_V1_0_RELEASE_NOTES.md), and automated exact-commit release workflow are included. Internal parser package version 0.3.0 and syntax v0.10 remain independent component versions.

## Manual ambiguity spot check

In the meaning-aware offline keyboard, type and convert each of `ThisInterval`, `This Interval`, `ThisPath`, `This Path`, `ThisRegion`, `This Region`. Their separate-root forms and their one-root forms must use different glyph sequences. Manually paste the two separate glyphs together with no space and decode them: a boundary must be inserted in Latin so re-encoding gives back the same **two rune glyphs**, separated by a space rather than accidentally becoming one different glyph.

Do not infer spell meaning from similarity of the English names; check the written glyph sequence and run the typed parser on the decoded Latin form.


## Surface v0.10 native binder tests

- [x] Preserve canonical v0.9 syntax in archive and register the v0.10 syntax snapshot
- [x] Add unique typed-use inference, tight `MassSelf` witnesses, scope uniqueness and ambiguity regression cases
- [x] Pass the complete 849-test Python 3.11 and 3.12 corpus regression suite on v0.10 (GitHub Actions run 44965252507). Remaining less-common binder family coverage is recorded separately.
- [x] Obtain Windows UTF-8 save, close, reopen and decode confirmation ([accepted file, glyphs and screenshots](release/LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md))

See the [v0.10 binder inference validation](release/LANGUAGE_V1_BINDER_INFERENCE_VALIDATION.md) for observed valid/invalid cases and the remaining release gates.

## Rare binder-family stress — 2026-11-22

- [x] Stress native v0.10 `Most`, `Trigger`, `Find`, `Question`, `Each`, `Filter`, `MinBy`, `MaxBy` and `Prevent` with valid, invalid, ambiguous and scope-sensitive cases. See [binder-family stress report](release/LANGUAGE_V1_BINDER_FAMILY_STRESS.md).
- [x] Pass **867 tests on Python 3.11 and 867 on Python 3.12** (GitHub Actions run `44965975682`), including the new 18 focused methods and preserved earlier corpus tests.
- [x] PC UTF-8 persistence/decode passed; release source frozen and packaging/tag publication defined in `.github/workflows/cuspell-language-v1-release.yml`. No tabletop or game execution system is required.

## Published release artifacts

The release workflow validates the complete parser suite, checks font outlines/Windows metadata and all canonical inventory counts, builds two versioned ZIPs, generates SHA-256 checksums and publishes the tag/release on **main only**. The Windows kit contains the same WinTest TTF/WOFF2 bytes accepted on the real PC, with corrected offline keyboard instructions. The original review fonts and early test kits remain untouched. See [Language v1.0 release notes](release/LANGUAGE_V1_0_RELEASE_NOTES.md).
