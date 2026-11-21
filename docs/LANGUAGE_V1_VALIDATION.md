# Language v1.0 validation checklist

_Status: integration audit in progress (2026-11-21); this is **not** a v1.0 release declaration._

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

Run automated checks from the repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The specific new tests are in `tests/test_glyph_language_integration.py`. They are regressions for the representation boundary; they do not prove that every intended spell is physically executable in every game world.

## Remaining release gates

- [ ] Run additional end-to-end script/parser checks on the broader prose/document corpus, beyond the two maintained spellcraft fixture sets.
- [ ] On a real PC, install/select **Cuspell 234 Review**, type at 32-34 px and at the 20 px minimum, and visually confirm close/mirrored pairs in ordinary text.
- [ ] Test copy -> paste -> save as UTF-8 -> reopen -> decode in an editor/word processor and browser; check that no glyphs become replacement characters. Also verify the expected fallback boxes when the custom font is not selected.
- [ ] Resolve any PC-only spacing/legibility defects without silently changing the approved glyph meanings or old Unicode mapping. A separately named final font can be considered only after those checks.
- [ ] Review outstanding normative references and drift checks, decide a frozen Language v1.0 snapshot, tag a version and publish a language-only release manifest and migration notes.

## Manual ambiguity spot check

In the meaning-aware offline keyboard, type and convert each of `ThisInterval`, `This Interval`, `ThisPath`, `This Path`, `ThisRegion`, `This Region`. Their separate-root forms and their one-root forms must use different glyph sequences. Manually paste the two separate glyphs together with no space and decode them: a boundary must be inserted in Latin so re-encoding gives back the same **two rune glyphs**, separated by a space rather than accidentally becoming one different glyph.

Do not infer spell meaning from similarity of the English names; check the written glyph sequence and run the typed parser on the decoded Latin form.
