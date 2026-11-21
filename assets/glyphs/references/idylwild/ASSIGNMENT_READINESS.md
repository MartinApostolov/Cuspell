# Cuspell glyph-to-meaning assignment readiness

_Status: all 218 rune/number glyph assignments and 16 spare designs user-approved, 2026-11-21; meaning-aware keyboard and Python converter implemented, original review font deliberately unchanged. Final installed-font PC verification is pending._

## Frozen inventory

- **217 distinct registered core rune meanings**: `language/core/lexicon.json`. Every registered entry has `rune_cost: 1`, including the formal operators `BeforeValue` and `AfterValue`. A registered rune always receives **one distinct glyph**.
- **1 distinct numeric sign**: `@` (number one), not an ordinary punctuation mark and not a lexicon entry.
- **234 approved source designs, 218 meaning-assigned and 16 spare**: 94 Cuspell (G), 76 Runic (R), 64 Alchemical (A); temporary slots U+E000–U+E0E9 and design IDs listed in `keyboard_kit/glyph_map.csv`.
- **16 approved spare designs** remain after 218 approved assignments; see `language/core/glyph_assignments.json`.
- **13 separately approved punctuation signs**: `stylized/typography/player_facing/manifest.json` and SVGs. They do not consume any of the 218 magic/number slots.

## Preservation and precedence

- The survivor/exclusion source of truth is `stylized/analysis/potential_overlap_groups.json`; its review notes and provisional stage/status labels are historical, and the later approved punctuation manifest takes precedence for punctuation status.
- The selected A/R source snapshot is `stylized/analysis/FRESH_SURVIVOR_A_R_SOURCE_SNAPSHOT_2026_11_21.json`; the 94 G shapes come from `../../recovery/source_geometry.json`. Do not alter source geometry during semantic assignment.
- The approved PC kit is `keyboard_kit/Cuspell_Codex_Keyboard_Kit.zip` with TTF/WOFF2, keyboard, chart, map and SHA-256 font manifest; the initial VS Code preview is acceptable, at target 32–34 px. The temporary private-use codepoints are **not meanings**.
- `language/names/old_names.json` contains historical Names with expansions/constituent costs; these are not 217 additional glyph requests. New Names and ordinary multi-rune phrases likewise do not require dedicated glyphs.
- Original CC0 ZIPs, rejected designs, handoffs and older font builders are preserved. Old 150-glyph recovery / 449-glyph comparison workflows are manual-only historic tools, not active production builders.

## Assignment complete; next steps

The authoritative semantic-to-glyph source is `language/core/glyph_assignments.json`, keyed by stable lexicon IDs and preserving G/R/A provenance IDs and existing PUA test positions. All 217 registered runes and the numeric `@` sign have approved one-to-one assignments, and all 16 leftovers are approved spares. Seven previous batches and the final eighth have explicit user approval. The geometric similarity findings are preserved for final legibility proofing.

**Implementation complete:** `keyboard_kit/meaning_keyboard.html` and `src/cuspell/glyphs.py` map approved transliteration names such as `Move` and `Light` to existing PUA characters; they also reverse-decode without inventing meanings for spare glyphs. Both maintainer and player dictionaries display approved source SVG artwork. **Do not replace or re-encode the original installable 234-glyph PC review font.** The remaining language-release gate is practical copy/paste and visual proofing on an installed PC, followed by a deliberate version freeze. A separately named release font is optional and must not be silently substituted. The font alone does not parse spells or substitute English rune names.

## Approval history (the remaining counts below are historical snapshots, not the current inventory)

### Approved assignment subset (2026-11-21)

The user explicitly approved all **18 beginner spellcraft runes plus numeric `@`** as first visual assignment batch. The exact mapping is in `meaning_assignments/draft_01.json`, whose status is now `USER_APPROVED_FIRST_19_PENDING_FULL_FONT_MAPPING`. These 19 IDs are reserved for their approved meanings; the 215 other eligible glyphs remain unassigned. The first visual sheet is retained for reproducibility; do not rewrite the 234-glyph PC-review font until the complete semantic mapping is decided.

## Approved meaning-assignment Batch 02 (2026-11-21)

The user explicitly approved **30 additional mappings**, recorded in `meaning_assignments/draft_02.json` as `USER_APPROVED_BATCH_02_30_PENDING_FULL_FONT_MAPPING`. Together with the first 19, this reserves **49 distinct glyphs for 48 registered runes plus numeric-one `@`**. The 185 remaining candidate designs are unassigned (169 future rune slots, 16 future spares). The same unmodified 234-glyph test font remains the baseline. Do not reuse these 49 source IDs for later meanings.

## Approved meaning-assignment Batch 03 (2026-11-21)

The user explicitly approved **all 30 physical-world, spatial and geometry mappings** in `meaning_assignments/draft_03.json` (`USER_APPROVED_BATCH_03_30_PENDING_FULL_FONT_MAPPING`). Across the first three batches, **79 distinct eligible glyphs are selected for 78 registered runes plus numeric-one `@`**. The 155 remaining designs have no meanings yet (139 required rune slots and 16 eventual spares). All 13 punctuation designs and the current 234-glyph test font remain unchanged. Reserve these 79 choices against reuse.

## Approved meaning-assignment Batch 04 (2026-11-21)

The user explicitly approved **all 30 temporal, event/reference, boundary and arithmetic mappings** in `meaning_assignments/draft_04.json`, with status `USER_APPROVED_BATCH_04_30_PENDING_FULL_FONT_MAPPING`. The first four batches now reserve **109 unique approved source glyphs for 108 registered runes plus numeric-one `@`**. Exactly 109 rune meanings and 125 glyph designs remain unassigned (including 16 eventual spares). The 234-glyph PC test font and all 13 punctuation glyphs are unchanged.

## Approved meaning-assignment Batch 05 (2026-11-21)

The user approved **all 30 information, speech, cognition, senses, intention, permission and control mappings** in `meaning_assignments/draft_05.json` (`USER_APPROVED_BATCH_05_30_PENDING_FULL_FONT_MAPPING`). Across five approved batches, **139 unique glyph designs now represent 138 registered runes plus numeric-one `@`**. The 95 remaining source candidates have no assigned meanings (79 future rune slots and 16 eventual spares). Preserve all reviewed shapes, punctuation and existing PC test font until full mapping completion.

## Approved meaning-assignment Batch 06 (2026-11-21)

The user approved **all 30 bodily-state, physical-action, health, biological and agency signs** in `meaning_assignments/draft_06.json` (`USER_APPROVED_BATCH_06_30_PENDING_FULL_FONT_MAPPING`). Across Batches 01–06, **169 unique designs cover 168 registered rune meanings plus the numeric-one `@`**. There are 49 registered rune meanings and 65 candidate source designs remaining, including the eventual 16 spares. Preserve the 234-glyph review font, all punctuation and all earlier approved assignments unchanged. `Ill` denotes illness, and it should be displayed with normal capitalization in explanatory prose to avoid mistaking the letters for vertical bars.

## Approved meaning-assignment Batch 07 (2026-11-21)

The user approved **all 30 emotional and social-interaction mappings** in `meaning_assignments/draft_07.json` (`USER_APPROVED_BATCH_07_30_PENDING_FULL_FONT_MAPPING`). The first seven batches reserve **199 unique source designs for 198 registered runes plus numeric-one `@`**. Exactly **19 rune meanings and 35 unused designs remain** (16 eventual spares). The user has seen the 15 moderate small-size comparison pairs; retain the audit as font-production quality-assurance evidence. Original source artwork and the 234-glyph review font remain untouched.

## Final approval (2026-11-21)

All 19 final registered meanings and all 16 spare shapes were explicitly accepted, completing **218 source assignments (217 runes + `@`)**. See `language/core/glyph_assignments.json` for current machine-readable truth and `meaning_assignments/BATCH_08_REVIEW.md` for the preserved exact-mirror and smaller-size similarity review. The 234-glyph prototype font remains unchanged.
