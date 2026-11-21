# Cuspell glyph-to-meaning assignment readiness

_Status: current source-of-truth handoff, 2026-11-21; mappings are NOT yet assigned._

## Frozen inventory

- **217 distinct registered core rune meanings**: `language/core/lexicon.json`. Every registered entry has `rune_cost: 1`, including the formal operators `BeforeValue` and `AfterValue`. A registered rune always receives **one distinct glyph**.
- **1 distinct numeric sign**: `@` (number one), not an ordinary punctuation mark and not a lexicon entry.
- **234 available unassigned source designs**: 94 Cuspell (G), 76 Runic (R), 64 Alchemical (A); temporary slots U+E000–U+E0E9 and design IDs listed in `keyboard_kit/glyph_map.csv`.
- **16 spare designs** remain after assigning 218; the precise spares are not yet chosen.
- **13 separately approved punctuation signs**: `stylized/typography/player_facing/manifest.json` and SVGs. They do not consume any of the 218 magic/number slots.

## Preservation and precedence

- The survivor/exclusion source of truth is `stylized/analysis/potential_overlap_groups.json`; its review notes and provisional stage/status labels are historical, and the later approved punctuation manifest takes precedence for punctuation status.
- The selected A/R source snapshot is `stylized/analysis/FRESH_SURVIVOR_A_R_SOURCE_SNAPSHOT_2026_11_21.json`; the 94 G shapes come from `../../recovery/source_geometry.json`. Do not alter source geometry during semantic assignment.
- The approved PC kit is `keyboard_kit/Cuspell_Codex_Keyboard_Kit.zip` with TTF/WOFF2, keyboard, chart, map and SHA-256 font manifest; the initial VS Code preview is acceptable, at target 32–34 px. The temporary private-use codepoints are **not meanings**.
- `language/names/old_names.json` contains historical Names with expansions/constituent costs; these are not 217 additional glyph requests. New Names and ordinary multi-rune phrases likewise do not require dedicated glyphs.
- Original CC0 ZIPs, rejected designs, handoffs and older font builders are preserved. Old 150-glyph recovery / 449-glyph comparison workflows are manual-only historic tools, not active production builders.

## Required next actions

1. Start a dedicated **canonical semantic-to-glyph mapping file**, based on exact `lexicon.json` IDs rather than transient table ordering. Preserve all original G/R/A IDs for provenance.
2. Assign one unique selected glyph ID to each of 217 registered runes, then one unique glyph to `@`, leaving exactly 16 explicitly unassigned spares.
3. Check visual confusability in the beginner spellcraft tier before locking assignments; do not remove approved glyphs without direct user choice.
4. Validate all assigned IDs against `glyph_map.csv`, no duplicates/missing meaning entries, all punctuation separate, and every source registration still costs one rune. Then update typeable language font/keyboard and parser integration, leaving the PC-review kit as a reproducible snapshot.

No glyph meanings are assigned by this file.

## Approved assignment subset (2026-11-21)

The user explicitly approved all **18 beginner spellcraft runes plus numeric `@`** as first visual assignment batch. The exact mapping is in `meaning_assignments/draft_01.json`, whose status is now `USER_APPROVED_FIRST_19_PENDING_FULL_FONT_MAPPING`. These 19 IDs are reserved for their approved meanings; the 215 other eligible glyphs remain unassigned. The first visual sheet is retained for reproducibility; do not rewrite the 234-glyph PC-review font until the complete semantic mapping is decided.

## Approved meaning-assignment Batch 02 (2026-11-21)

The user explicitly approved **30 additional mappings**, recorded in `meaning_assignments/draft_02.json` as `USER_APPROVED_BATCH_02_30_PENDING_FULL_FONT_MAPPING`. Together with the first 19, this reserves **49 distinct glyphs for 48 registered runes plus numeric-one `@`**. The 185 remaining candidate designs are unassigned (169 future rune slots, 16 future spares). The same unmodified 234-glyph test font remains the baseline. Do not reuse these 49 source IDs for later meanings.

## Approved meaning-assignment Batch 03 (2026-11-21)

The user explicitly approved **all 30 physical-world, spatial and geometry mappings** in `meaning_assignments/draft_03.json` (`USER_APPROVED_BATCH_03_30_PENDING_FULL_FONT_MAPPING`). Across the first three batches, **79 distinct eligible glyphs are selected for 78 registered runes plus numeric-one `@`**. The 155 remaining designs have no meanings yet (139 required rune slots and 16 eventual spares). All 13 punctuation designs and the current 234-glyph test font remain unchanged. Reserve these 79 choices against reuse.

## Approved meaning-assignment Batch 04 (2026-11-21)

The user explicitly approved **all 30 temporal, event/reference, boundary and arithmetic mappings** in `meaning_assignments/draft_04.json`, with status `USER_APPROVED_BATCH_04_30_PENDING_FULL_FONT_MAPPING`. The first four batches now reserve **109 unique approved source glyphs for 108 registered runes plus numeric-one `@`**. Exactly 109 rune meanings and 125 glyph designs remain unassigned (including 16 eventual spares). The 234-glyph PC test font and all 13 punctuation glyphs are unchanged.
