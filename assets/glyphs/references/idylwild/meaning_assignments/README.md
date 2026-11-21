# Cuspell approved glyph assignments — visual review history

**Current truth (2026-11-21): all 217 registered runes and numeric-one `@` have user-approved distinct glyph designs, with 16 approved spare designs.** The single canonical mapping is [`language/core/glyph_assignments.json`](../../../../../language/core/glyph_assignments.json). Its visual reference now appears in the [maintainer dictionary](../../../../../docs/CUSPELL_DICTIONARY.md) and [player rune chart](../../../../../player/RUNES.md).

The `draft_01.json` through `draft_08.json` filenames are preserved visual-review history; each records an explicit user-approved status, not a competing source of truth. All SVG proof sheets, close-pair audits, the 234-glyph prototype font and prior handoffs are retained.

## Approved batch 01 record

**First 19 assignments user-approved (2026-11-21; “Keep all”).** The first 18 beginner spellcraft rune-to-glyph assignments plus `@` are now accepted as the initial mapping subset. This does not change language semantics, the font's Unicode mappings, the 217 registered runes, or the 234 approved glyph designs.

- `draft_01.json`: first 18 beginner spellcraft signs from the stress-tested checkpoint-141 progression, plus approved numeric-one `@` glyph, with registered lexicon IDs and original G/A/R source IDs.
- `review_01.svg`: self-contained labeled visual sheet from the existing approved source SVGs. No modifications to individual shapes.
- `../keyboard_kit/meaning_assignment_preview_01.html`: copy this file into the extracted keyboard kit alongside its TTF to see real-font examples at 20/32/34 px.

The approved first batch intentionally makes the most frequent spellcraft contrasts legible: `Move / This / There`, `Begin / End`, `This / You / Self`, `Whole / Locked / Magic`, and `Persist / Prevent`. `Begin` and `End` use distinguishable up/down-arrow relatives for a mnemonic opposition; if the mirrored relationship is too easy to misread, swap one during user review. `Light` uses the existing solar-form A015, `Persist` the infinity-like A018, `Prevent` the crossing G041; `@` uses the approved circled-staff R039.

User approved all 19 choices. Treat these glyph-to-meaning choices as locked for later batches unless the user reopens them. They are not yet encoded into a final language font. At this first checkpoint the other 215 source IDs were unassigned; Batches 02–08 have since completed the full assignment.
