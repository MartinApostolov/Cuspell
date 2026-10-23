# Cuspell — new-thread handoff after Idylwild stylization Batch 14

**Checkpoint:** 2026-10-23, after user approved the visual styling of Batch 14.  
**Repo:** `MartinApostolov/Cuspell`  
**WORKING BRANCH (NOT MAIN):** `glyphs/idylwild-style-sample-01`  
**Draft PR:** https://github.com/MartinApostolov/Cuspell/pull/124  
**Branch head at this handoff:** The commit containing this file and the Batch 14 approval; read the *latest branch head*, not this document's parent commit.  
**Canonical registry:** untouched: `assets/glyphs/recovery/source_geometry.json` with G001–G150.  
**No further batch has been started in this thread.**

## Start here — what to do in the next thread

1. Fetch this document and `assets/glyphs/references/idylwild/stylized/sample_14/manifest.json` from `glyphs/idylwild-style-sample-01`, rather than from `main` (the experimental work is still in a draft PR).
2. Resume **Stage 1 stylization at Batch 15**: process Runic **R150–R165** (16 source IDs), keeping the user's established review workflow. Save to `assets/glyphs/references/idylwild/stylized/sample_15/`. Produce editable SVGs, a true three-column visual comparison (**original source pixels / adapted Cuspell SVG / unchanged original Cuspell SVG**), manifest, readme, and validation script.
3. Before reusing geometry, verify the relationship between these source IDs and **R038–R053**, because the Runic pack's latter 112 IDs appear to form alternate-ink/shape versions of R001–R112 (offset +112). Where the silhouette truly corresponds, **reuse the previously approved vector** rather than inventing a new design. Keep both distinct source IDs and all source/provenance files.
4. Show the actual comparisons for user review. Record **KEEP** as approval of visual stylization only; do not adopt to canonical or assign meanings.
5. Do **not** rush ahead to Stage 2 pruning or make a canonical-registry change. When all external sources are represented, audit duplicates/near-duplicates/mirrors and then review the whole pool for final selection.

Potential subsequent batches of about 16: **R166–R181**, **R182–R197**, **R198–R213**, **R214–R224** (last 11). All should be checked against the corresponding **R054–R112** source shapes.

## Counts and approvals — VERIFIED THROUGH BATCH 14

| Collection | Source IDs covered | Source IDs remaining |
| --- | ---: | ---: |
| Existing canonical Cuspell G001–G150 | 150 | Not being changed |
| Runic Idylwild R001–R224 | **149** (R001–R149) | **75** (R150–R224) |
| Alchemical Idylwild A001–A075 | **75** | **0** |
| **External total** | **224 / 299 source IDs** | **75 source IDs** |

- Batches **01–12**: stylistically approved, including the spacing fixes detailed below.
- Batch **13 (R118–R133)**: stylistically approved with the user's "keep next". The source variants R118–R133 have the normalized geometry of **R006–R021**.
- Batch **14 (R134–R149)**: stylistically approved by the user's latest "keep" (while asking for a handoff instead of another batch). The sources use the normalized geometry of **R022–R037**, with each source ID retained.
- **Do not equate 224 processed external source IDs with 224 unique useful signs.** In fact, R113–R149 were explicitly treated as alternate renditions of earlier Runic symbols and do not automatically add new distinctive shapes. The final unique count is **not yet measured**.
- The remaining R150–R224 may likewise be source variants; verify the actual pictures against the corresponding R038–R112 artwork. The 224 Runic source files may contain only 112 indexed base families before considering further near-duplicates.
- The game currently needs at least **218 visually distinct symbols**: **217 base roots plus one special symbol**. **256** has been discussed only as a possible larger pool, **not an approved goal**.
- The existing 150 are *not* automatically protected. The user may remove/replace many of their mirrored pairs in Stage 2.

## What Stage 1 currently looks like

Established visual grammar, approved over 14 batches:

- SVG coordinate system `viewBox="0 0 600 1000"`, typically `stroke-width="66"`, rounded caps and joins.
- Smooth organic centerline strokes, consistent visual scale and strong silhouette, not raster-style square strokes.
- Keep meaningful gaps, rings, detached dots and multiple strokes. **Avoid crowded interiors**, especially at small display sizes.
- The user **does not physically draw** glyphs. Characters draw them in the air inside the game world. Optimize symbol identity and legibility, not human gesture ergonomics.
- Root-to-glyph meanings are **randomized per game run**. Artwork has no permanent root assignments at this stage.
- Use original Idylwild CC0 source images in the comparison, not only the comparison font's pixel-blocky TTF. Existing Cuspell Gxxx samples on the right are **style references only**, never assumed replacements.

### User-flagged crowding fixes (all accepted, don't regress)

| Candidate | Fix |
| --- | --- |
| **A050** (Batch 01) | Opened spacing between the lower ends of three nested arches. |
| **A013** (Batch 05) | Increased gap between its two crescent curves. |
| **R002** (Batch 09) | Shortened/moved the inner descending arch to clear the outer arch. |
| **A068** (Batch 09) | Separated roof, horizontal bar and spaced uprights. |
| **R112** (Batch 12) | Moved the detached dot into open lower interior, away from the curve. |
| **R114** (Batch 12) | Shortened/repositioned the inner arch for an open channel. |

Earlier SVG revisions were archived under the appropriate `sample_XX/revisions/` folders where available; never erase them. Other pre-review optical adjustments occurred (e.g. R086, A070 and R057); consult the sample READMEs and current SVGs before cloning shapes.

## Directory structure and repository records

- Experimental batch files: `assets/glyphs/references/idylwild/stylized/sample_01/` through `sample_14/`. Typical batch contents: `svgs/*.svg`, `manifest.json`, `README.md`, `index.html`, `validate_sample.py`, one or two `*_comparison.svg` files, and sometimes `batchNN_adapted.svg`.
- **Sample manifest schemas vary across batches**: collection property names are `samples`, `glyphs`, `decisions`, or `candidates`; be careful when aggregating. Records carry `Rxxx/Axxx` IDs and may include alternate-source links. Use the actual on-branch JSON rather than assuming one schema.
- Latest checkpoint: `assets/glyphs/references/idylwild/stylized/sample_14/manifest.json`.
- Batch 14 preview: `assets/glyphs/references/idylwild/stylized/sample_14/batch14_adapted.svg`.
- Batch 14 three-column sheet: `assets/glyphs/references/idylwild/stylized/sample_14/runic_comparison.svg`.
- Original contact sheet (indexed 224 Runic and 75 Alchemical): `assets/glyphs/references/idylwild/reviews/01_runic_vs_alchemical.png`.
- Additional combined source-vs-Cuspell reference: `assets/glyphs/references/idylwild/reviews/02_runic_vs_alchemical_vs_cuspell.png`.
- Original ZIPs (preserve byte-for-byte):
  - `assets/glyphs/references/idylwild/original/idylwilds_runic_codex.zip` (224 indexed designs, 672 PNG variants)
  - `assets/glyphs/references/idylwild/original/idylwilds_alchemical_codex.zip` (75 indexed designs, 225 PNG variants).
- Provenance/CC0 archive hashes and rebuild info: `assets/glyphs/references/idylwild/README.md`.
- Current original Cuspell source-of-truth: `assets/glyphs/recovery/source_geometry.json` and `assets/glyphs/recovery/generated/glyphs/G001.svg` ... `G150.svg`.
- The old 449-symbol `keyboard_kit/` TTF is the **original pixel-based comparison font**, *not* an updated font from the newly stylized SVGs. It is for reference and may appear visually inconsistent until rebuilt from approved final candidates.
- PR #124 is a **draft**. Do **not** merge unreviewed source candidates to `main` or change canonical glyphs simply because they have been stylized.

## Key lessons from the source-variant sequence

- Batch 12 introduced **R113–R117**, annotated as second ink variants of R001–R005.
- Batch 13 created **R118–R133**, with source-to-prototype mapping R118→R006 through R133→R021.
- Batch 14 created **R134–R149**, with mapping R134→R022 through R149→R037.
- For Batch 15, expect **R150→R038** through **R165→R053**; verify actual source thumbnails before automatically reusing paths. Matching variants **need a separate file and source map** but *do not* expand the count of proven distinct shapes.
- Stage 2 must perform systematic exact/near/mirrored/rotated checks across **150 current G** plus the normalized **299 R/A source records**, grouping source variants and retaining links and archives. Distinctiveness at small sizes and variation across the full set should guide actual keep/replace/remove decisions.

## Absolutely preserve these decisions

1. **Styling approval ≠ final pool selection.** The user's "keep" has consistently meant "looks fine, move to the next conversion batch." No canonical adoption vote has occurred.
2. **Do not change existing G001–G150** or their canonical source/TTF until the user approves the exact final pool.
3. **Do not delete** original borrowed ZIPs, early shapes, rejected/retired designs or source attribution. Archive everything.
4. **Do not permanently map meanings to glyph IDs**; game-run root↔glyph permutation is intended.
5. **Don't assume 256** is the target; **218** is the currently stated minimum, and reducing mirrors may increase required replacements.
6. **The user has requested a handoff now, NOT Batch 15 in this thread.** Stop here after saving this checkpoint.

## Ready-to-paste new-thread prompt

> Continue Cuspell from branch `glyphs/idylwild-style-sample-01` in `MartinApostolov/Cuspell` (Draft PR #124). Read `assets/glyphs/references/idylwild/HANDOFF_NEXT_THREAD_AFTER_BATCH14.md` and the Batch 14 manifest. Batch 14 is stylistically approved; we have 224/299 Idylwild source IDs covered and 75 Runic IDs left. Start Batch 15 (R150–R165), verifying each artwork variant against R038–R053 before reusing geometry. Show real original/adapted/existing Cuspell visual comparisons, preserve sources and registries, and do not treat source coverage as unique glyph count. Do not start final pool selection or alter G001–G150 yet.
