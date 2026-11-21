# Language v1.0 validation checklist

_Status: final normative/reference consistency audit complete in repository; physical PC acceptance and the deliberate Language v1.0 release freeze remain outstanding (2026-11-22). This is **not** a v1.0 release declaration._

Cuspell v1.0 is a **language** deliverable: syntax, meanings, names, writing, font-based script, documentation and testable tooling. World physics, RequiredPower, balance and a playable game engine are outside this release.

## Immutable choices for this pass

- Keep the approved 217 semantic-rune glyph assignments and the separate `@` numeric-one glyph.
- Keep 16 approved spare designs unassigned.
- Preserve the original 234-design font, installed name **Cuspell 234 Review**, 13 punctuation characters, PUA codepoints, original keyboard/chart, ZIP and source artwork.
- The normative parser input is still surface-v0.8 Latin transliteration; the Unicode private-use glyph text is a script representation, not a new semantic grammar.

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
- Glyph assignment data agrees with the registry: **217 one-to-one rune mappings plus numeric-one `@`**, and **16 unassigned approved spare designs**. The 234-glyph font and 13 approved punctuation designs are unchanged.
- Player rune glossary and maintainer dictionary artwork remain covered by existing source-to-illustration regressions. The 204 Old Name player table entries have been checked for *both* sign coverage and exact recursive historical mana cost.
- Canonical surface v0.8, pipe-as-debug-only, flat control flow, release keyboard availability, and current versus historical checkpoint counts have been reconciled across the current specs, dictionary, player guide, README and mapping metadata. Machine truth remains normative; historical work stays archived.
- New regression guards in `tests/test_language_v1_consistency.py` cover these cross-layer invariants so a later edit cannot quietly restore old 212/131/265/48 counts.

## Remaining release gates

- [x] Run script/parser round-trip checks over preserved representative book, cross-genre, Yona, corpus-gap, and current-document examples. Existing book test methods remain the source of their validity assertions; archived passages are not promoted to normative syntax.
- [ ] On a real PC, follow [the acceptance guide](../player/PC_FONT_CHECK.md): install/select **Cuspell 234 Review**, type at 32–34 px and at the 20 px minimum, and visually confirm close/mirrored pairs in ordinary text.
- [ ] Test copy -> paste -> save as UTF-8 -> reopen -> decode in an editor/word processor and browser; check that no glyphs become replacement characters. Also verify the expected fallback boxes when the custom font is not selected.
- [ ] Resolve any PC-only spacing/legibility defects without silently changing the approved glyph meanings or old Unicode mapping. A separately named final font can be considered only after those checks.
- [x] Reconcile normative registry, syntax, dictionary, player documentation, glyph metadata, and historical-vs-current counts; add regression guards.
- [ ] Freeze and tag the Language v1.0 normative snapshot after PC acceptance, and publish a language-only release manifest and migration notes. Internal parser version 0.3 and surface syntax 0.8 are component versions, not a claim that Language v1.0 is already tagged.

## Manual ambiguity spot check

In the meaning-aware offline keyboard, type and convert each of `ThisInterval`, `This Interval`, `ThisPath`, `This Path`, `ThisRegion`, `This Region`. Their separate-root forms and their one-root forms must use different glyph sequences. Manually paste the two separate glyphs together with no space and decode them: a boundary must be inserted in Latin so re-encoding gives back the same **two rune glyphs**, separated by a space rather than accidentally becoming one different glyph.

Do not infer spell meaning from similarity of the English names; check the written glyph sequence and run the typed parser on the decoded Latin form.
