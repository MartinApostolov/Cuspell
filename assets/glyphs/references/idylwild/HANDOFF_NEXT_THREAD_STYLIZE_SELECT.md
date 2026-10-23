> **UPDATE 2026-10-23:** This is the ORIGINAL pre-stylization handoff from 2026-10-22 and its initial workflow is now superseded. For current progress after **Batch 14**, read [HANDOFF_NEXT_THREAD_AFTER_BATCH14.md](HANDOFF_NEXT_THREAD_AFTER_BATCH14.md) on the `glyphs/idylwild-style-sample-01` branch of Draft PR #124. The current work is *not yet on main*. The historical notes below remain for context.

# Cuspell next-thread handoff — stylize borrowed glyphs, then choose the final inventory

**Date:** 2026-10-22  
**Repository:** `MartinApostolov/Cuspell`  
**Starting point:** latest `main` (do not use the old recovery branch as the starting point).  
**Status:** Planning/handoff only. **No borrowed designs have yet been adopted**, and the active canonical registry remains **G001–G150**.

## What the user wants next

**FIRST** redraw/adapt the two already imported Idylwild collections into **Cuspell's established visual style**. **THEN** examine the entire standardized pool and jointly decide what to KEEP, REPLACE, or REMOVE, including possibly removing **many of Cuspell's current mirrored pairs**. The user wants to see the adapted symbols before judging them, rather than deciding based on mismatched raw pixel-art fonts.

Do **not** begin the next thread by picking winners from unadapted, blocky sprites, assigning roots, or treating the 150 current glyphs as untouchable. Do not bulk-delete existing glyphs without review. Proceed iteratively, with clear visual comparisons and explicit user KEEP / CHANGE / REPLACE decisions.

### Critical clarification from the user

Cuspell glyphs are drawn **in the air by people/characters in the GAME WORLD**. The player does **not** physically trace or draw them with a mouse, controller or hand. Prioritize visual identity, legibility, internal cohesion, and potential animation paths; don't require simple physical handwriting gestures for the player.

### Gameplay and counts

- Current dictionary: **217 registered base roots**, see `docs/CUSPELL_DICTIONARY.md`.
- Plus one special glyph for the number **1** => **218 glyphs required** if every root is present at once.
- Existing active canonical glyphs: **150 (G001–G150)**.
- Borrowed candidate collections: **224 Idylwild Runic** + **75 Idylwild Alchemical** = **299 candidate designs** before de-duplication.
- Total *source candidate count*: **449 = 150 + 224 + 75**, **not** a claim of 449 distinct, suitable glyphs.
- Short-term goal: reach **at least 218 good, visually distinguishable glyphs**. 256 was discussed as a *possible* larger pool, **not a settled target**.
- The first use of Cuspell is a roguelike/game that **reshuffles which glyph represents which root each run**, preventing players from memorizing permanent rune-to-root assignments. The underlying language grammar and spell-building remain learnable. No meanings have been assigned to artwork yet.
- If removing many current mirrors, the *number of additional external designs needed* may exceed the original gap of 68.

## Assets already imported and verified on `main`

Original unmodified CC0 ZIP source archives, downloaded from OpenGameArt and stored **with provenance**:

- `assets/glyphs/references/idylwild/original/idylwilds_runic_codex.zip` — Runic Codex, **224 designs**, 672 PNG style/variant files.
- `assets/glyphs/references/idylwild/original/idylwilds_alchemical_codex.zip` — Alchemical Codex, **75 designs**, 225 PNG variants.
- Primary pages:
  - https://opengameart.org/content/idylwilds-runic-codex
  - https://opengameart.org/content/idylwilds-alchemical-codex
- Both are declared **CC0** on their source pages. Preserve original creator credit, source URLs, exact archives and hash manifests for traceability.

Current comparison assets:

- `assets/glyphs/references/idylwild/reviews/01_runic_vs_alchemical.png` — 224 vs. 75.
- `assets/glyphs/references/idylwild/reviews/02_runic_vs_alchemical_vs_cuspell.png` — 224 vs. 75 vs. all 150.
- `assets/glyphs/references/idylwild/compare_codices.py` — recreates indexed sheets.
- `assets/glyphs/references/idylwild/README.md` — documentation, exact archive checksums, usage.
- `tests/test_idylwild_reference_assets.py` — original archive/checksum tests.

Installable *comparison*, **not final canonical**, font and offline keyboard:

- `assets/glyphs/references/idylwild/keyboard_kit/CuspellCodexReview-Regular.ttf`
- `assets/glyphs/references/idylwild/keyboard_kit/Cuspell_Codex_Keyboard_Kit.zip`
- `assets/glyphs/references/idylwild/keyboard_kit/keyboard.html`
- `assets/glyphs/references/idylwild/keyboard_kit/glyph_map.csv`
- Build: `assets/glyphs/references/idylwild/build_unified_font.py`.
- Currently assigns PUA: Cuspell `U+E001..U+E096`; Runic `U+E100..U+E1DF`; Alchemical `U+E200..U+E24A`.
- **The issue spotted by the user:** viewing symbols together in VS Code revealed the imported glyphs' **severe mismatches in visual size, thickness, weight, geometry, complexity and overall design language**. Current Idylwild glyphs were converted from 16px sprites to monochrome TrueType pixel-based rectangles. The TTF is a *testing utility*, not the visual target. The VS Code display itself worked once the correct font was installed and `editor.fontFamily` was configured.

Current canonical Cuspell SVG + generated font:

- `assets/glyphs/recovery/source_geometry.json` — **authoritative 150-glyph editable registry**.
- `assets/glyphs/recovery/generated/glyphs/G001.svg` ... `G150.svg`.
- `assets/glyphs/recovery/generated/fonts/CuspellRecoveredPrototype-Regular.ttf`.
- `assets/glyphs/recovery/README.md` — provenance and architecture.
- `assets/glyphs/recovery/HANDOFF_NEXT_CHAT.md` — earlier recovery decisions, historical context.
- `assets/glyphs/recovery/gesture_review/REVIEW_PROGRESS_2026-10-22.md` — **75 glyph handwriting-review groups accepted**, not a mandate to preserve all 150 silhouettes forever. Original historical v0.19 geometry/gesture trajectories are **not** recovered. The modern accepted paths still need separate later consolidation.

Automation currently works on `main`:
- `.github/workflows/idylwild-comparison.yml` — validates ZIPs and regenerates comparisons.
- `.github/workflows/cuspell-codex-comparison-font.yml` — builds/validates 449-character font + offline keyboard.
- `.github/workflows/cuspell-glyph-recovery.yml` — canonical glyph/font rebuild.
- `.github/workflows/tests.yml` — parser/test matrix.
The unified font CI first passed: https://github.com/MartinApostolov/Cuspell/actions/runs/39848097119

## Recommended new-thread workflow

### Phase 1 — Establish Cuspell's visual standard using *actual* source glyphs

Use Cuspell's current SVGs as visual references, not the blocky Idylwild TrueType import. Explicitly assess representative Cuspell glyphs before setting:
- Typical strokes approximately 66 SVG units on the 600×1000 drawing canvas where appropriate; allow systematic exceptions (not forced uniformity).
- Smooth center-line curves, consistent stroke caps/joins, black/white, recognizable silhouette, visually appropriate height and width, optically consistent negative space.
- Handle intentional detached dots and multiple strokes; preserve a distinctive feature rather than making all borrowed signs identical.
- Check **small-size readability** and coherent appearance when many glyphs appear in sequence.
- No need for physical player gesture comfort, but signs should be credible for in-world air-drawing/animation.

### Phase 2 — Make a representative proof-of-style batch FIRST

Choose a diverse selection of external Runic and Alchemical designs (e.g., 10–20 from each) with indexed IDs. For every selected glyph, display:
1. **Original Idylwild bitmap** (source untouched).
2. **New Cuspell-style editable SVG** (smooth/adapted).
3. **Same adapted SVG beside representative original Cuspell characters** at equal nominal em sizes.

Show actual graphics, not text-only descriptions. Let user approve or tweak the visual conversion rules. Only after that is accepted, batch-apply the standard systematically to remaining external candidates, identifying special cases for manual redrawing.

### Phase 3 — Stylize candidate pool non-destructively

- Store each new vector in a **separate, explicitly candidate** location under `assets/glyphs/references/idylwild/stylized/`, preferably with per-ID SVGs, contact sheets and a machine-readable mapping to original ZIP path, license and conversion parameters.
- Keep original Idylwild ZIPs **untouched**.
- Preserve IDs `R001–R224` and `A001–A075` through review. Do not silently reuse `Gxxx` IDs or modify meanings.
- Design a reproducible converter and test it for vector validity, path closure/stroke consistency, source count, image and font rendering. Do not rely on a blind auto-trace for delicate intricate glyphs; manually flag and correct exceptions.
- Update or produce an **alternate** installable font/keyboard preview of standardized candidate SVGs if that helps the user compare actual strings.

### Phase 4 — Then review what to KEEP / REPLACE / REMOVE

Once the borrowed candidates share a coherent style:
- Compare adapted signs against one another and all 150 current Cuspell signs; identify **exact duplicates, near-duplicates, reflection/rotation variants, weak silhouettes, and likely confusion**.
- Evaluate **replacing many existing mirror-pair variants** with more distinctive external signs. A mirror is not automatically wrong, but many paired signs are a concern.
- Keep a per-ID decision table with source provenance, original Cuspell ID (if being replaced), adaptation ID, and user-approved outcome. Preserve retired art and mappings rather than erase them.
- Present digestible batches for user KEEP / CHANGE / REPLACE votes, following their preference for efficient iterative reviews.
- Only after final inventory selection and sign numbering are agreed should the **canonical 150-entry registry be changed/expanded** and official fonts/guide builds adjusted.
- The goal is at least 218 distinct signs, with any larger reserve agreed on after reviewing the candidates.
- Re-run source count, font cmap, collisions, mirror relations, visual legibility and CI tests after adoption.

## Important constraints

1. **Do not conflate a visual candidate conversion with official adoption.**
2. **Do not mutate existing G001–G150 SVGs or their IDs until the user approves a specific replacement/removal/re-numbering plan.**
3. **Do not delete old or borrowed original artwork.** Archive rejected/retired candidates.
4. **Do not assign root meanings**: procedural rune↔root mapping is intended to vary between runs.
5. Keep historical vs. approved modern vs. newly borrowed provenance clearly separate.
6. User did **not** request starting this process in the current thread; this file is a handoff for the **next** thread.

## Start-of-next-thread action

Read this file and the reference directory README on **current `main`**, inspect representative canonical Cuspell SVGs and the original CC0 asset packs, and prepare a **small visual Cuspell-style conversion batch covering both Idylwild sources**. Show original vs. adapted vs. existing Cuspell examples side by side. Obtain aesthetic feedback before adapting all 299. Do not prematurely prune mirrors or promote candidates.
