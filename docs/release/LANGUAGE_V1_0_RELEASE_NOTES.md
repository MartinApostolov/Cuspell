# Cuspell Language v1.0

**Stable language-only release** · Git tag `v1.0.0` · 22 November 2026

Cuspell is a compositional, typed rune language with a meaning-mapped script. This release freezes the approved core vocabulary, the canonical v0.10 written grammar, the 234-design glyph inventory, the dictionary and name registries, and the reference parser/tooling used to validate sentences. It **does not** provide a tabletop ruleset or a game-execution engine.

## What's included

- **217 approved meaning runes**, a separate numeric-one sign `@`, and **218 one-to-one meaning assignments**. **16 spare approved glyph designs** remain unassigned. The 13 punctuation glyphs and original private-use codepoint assignments are unchanged.
- Canonical **surface syntax v0.10**, including rune-native `:«This»` binder labels, `$«This»` references, uniquely inferred binder types, tight Cuspell type witnesses such as `:«This»:MassSelf`, and errors on duplicate active labels.
- **204 registered Old Names**, world-facing example New Names and a typed grammar/parser, full current illustrated dictionary, player reference, beginner spellcraft progression and the maintained example corpora.
- **Cuspell Compact WinTest**, the proportional Windows font that was successfully tested in Notepad, and an improved self-contained offline keyboard. This remains the *existing approved font binary* under its installed Windows family name; no glyph drawings, PUA mapping, or inter-rune spacing were modified during release packaging.
- Full-language source, documentation, test data, approved artwork and provenance; the original **Cuspell 234 Review** and older Compact packages remain available as historical assets.

## Download and install

Download **Cuspell-Language-v1.0-Windows-Font-Kit.zip** for just the font and meaning-aware offline keyboard. Extract it, install `CuspellCompactWinTest-Regular.ttf`, and open the included `meaning_keyboard.html` from the same folder. In Windows Notepad choose **Cuspell Compact WinTest**. The page converts transliteration to glyphs and back; it **does not** type-check spells.

Download **Cuspell-Language-v1.0.zip** for the complete language distribution (including current docs, data, reference parser, approved glyph assets, and a copy of the Windows font kit). Start at `README.md`, `player/README.md` and `docs/CUSPELL_DICTIONARY.md`.

The standalone `CuspellCompactWinTest-Regular.ttf` is also attached for users who already have the keyboard.

## Writing examples

```text
All :«This» Life $«This».
Create :«This» At $«This» There Change $«This» Light «LightUnit» @!
```

A binder's type can be inferred when its registered typed uses have exactly one compatible interpretation. A Cuspell type witness may be written explicitly when needed. Arbitrary English variable/type words are not required by canonical Cuspell grammar. Quoted proper Signs may retain their own lettering as exact data.

## Compatibility and validation

- Canonical written surface: **v0.10**. Archived v0.8/v0.9 syntax inputs remain supported as backwards-compatible parser input, but are **not** the current recommended writing form.
- Python reference parser/component package: **0.3.0** (component version, not the Cuspell language release version). Python **3.11+**.
- **867 automated tests passed on each of Python 3.11 and 3.12**, covering glyph round trips, the maintained 82 spellcraft examples, sampled book/Yona corpora, and stress tests for rare binder families.
- User-approved Windows Notepad display and **actual UTF-8 save/reopen/decode round trip**; see `docs/release/LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md`.
- VS Code is **not** a release requirement. In a program that does not have the custom font selected, the private-use characters may appear as boxes.

## Attribution and licensing notices

The original Cuspell designs and 140 stylized Idylwild Runic/Alchemical designs are documented in `assets/glyphs/references/idylwild/keyboard_kit/SOURCES.txt`; Idylwild source artwork is **CC0**. The working Windows font includes Latin fallback outlines originating from **DejaVu Sans Mono**; the relevant license is included in the Windows kit as `DEJAVU-LICENSE.txt`. This document makes no new claim about the license of the entire repository.

## Scope

Language, glyphs, names, spelling, grammar, parser, documentation and testable tools **only**. Game rules, magical energy/balance systems, world physics and a complete magic runtime are intentionally excluded. The tagged GitHub repository source remains the authoritative immutable versioned snapshot.

See `docs/release/LANGUAGE_V1_0_MANIFEST.json` for the exact release inventory, font checksum, normative paths and user-acceptance reference.
