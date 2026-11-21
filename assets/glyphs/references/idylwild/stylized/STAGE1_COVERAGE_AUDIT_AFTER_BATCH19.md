# Cuspell / Idylwild — Stage 1 source-coverage audit after Batch 19

**Audit date:** 2026-10-23  
**Branch:** `glyphs/idylwild-style-sample-01` (draft PR #124)  
**Scope:** Are all original Idylwild source IDs represented and saved? **YES.**  
**Not in scope:** final pool pruning, artistic uniqueness across collections, meaning assignments.

## Independently cross-checked on GitHub

| Collection | Expected IDs | Manifest records | Existing candidate SVGs | Missing IDs |
| --- | ---: | ---: | ---: | ---: |
| Idylwild Runic | R001–R224 (224) | 224 | 224 | **0** |
| Idylwild Alchemical | A001–A075 (75) | 75 | 75 | **0** |
| **Borrowed-source total** | **299** | **299** | **299** | **0** |
| Canonical Cuspell (separate, untouched) | G001–G150 (150) | outside this audit | 150 original assets | — |

The audit separately enumerated all **19 batch manifests** and all **19 physical `svgs/` directories** through GitHub, then compared against the complete numeric ranges. Both yielded exactly the same 299 distinct IDs: **no missing source IDs, no repeated IDs, no unexpectedly named candidate files**, and all manifest candidate paths have the expected `svgs/{ID}.svg` shape.

### Why some were reviewed out of order

Early batches were *mixed selections* from the Runic and Alchemical collections, not consecutive numeric ranges. For example, Batch 01 contained Runic **R001, R012, R022, R027, R041, R049, R090, R094** together with eight Alchemical sources. Many remaining early IDs were covered in later mixed batches.

| Batch | Source records represented |
| --- | ---: |
| 01–10 | 16 per batch = 160 |
| 11 | 16 |
| 12 | 16 (R102–R117) |
| 13 | 16 (R118–R133) |
| 14 | 16 (R134–R149) |
| 15 | 16 (R150–R165) |
| 16 | 16 (R166–R181) |
| 17 | 16 (R182–R197) |
| 18 | 16 (R198–R213) |
| 19 | 11 (R214–R224) |
| **Total** | **299** |

The manifests use four historical record-field names (`samples`, `glyphs`, `decisions`, `candidates`). The audit deliberately reads all of them. Batch 01's early metadata had retained its original "unreviewed" status despite later approval; a separate **style-review** field was reconciled after Batch 19, without altering its `decision` (which still means pending final inventory selection).

## Source variants and what the count means

- Every Runic ID **R113–R224** correctly records its **R001–R112** partner (index minus 112): 112/112 valid source-provenance links.
- The later Runic ink variants have their own source identity but normally reuse the approved contour of the earlier version. **224 Runic source IDs do not mean 224 independently distinctive Runic signs.**
- **150 existing Cuspell + 299 borrowed source IDs = 449 archived source records**, *not* 449 unique signs or a final font.
- The currently described minimum final inventory is **218 visually distinct signs** (217 roots and one special sign); **256 was not an approved target.**

## Preserved assets / non-adoption

GitHub asset blob hashes were compared between `main` and the experimental branch:

| Asset | Matching blob/tree SHA |
| --- | --- |
| Canonical `assets/glyphs/recovery/source_geometry.json` | `afa213766ba30632523aa918a005341044e8aaec` |
| Canonical `assets/glyphs/recovery/generated/` | `98751a6d34f758365872198475343494b91e7b64` |
| Original Idylwild Runic ZIP | `a0d3a7d793e8a590c6059f32a316b97fdef06048` |
| Original Idylwild Alchemical ZIP | `3c0bbeff0660c34c1156e3d8c2a7d519530ee90a` |

All four match across branches, so canonical art and both original Idylwild archive blobs remained untouched during the stylization work. Original revisions and source attribution remain archived.

## Reproducible follow-up verification

Run `python assets/glyphs/references/idylwild/stylized/verify_stage1_coverage.py` from the repository after checkout. It checks numeric source coverage, every manifest's referenced SVG existence and XML canvas, physical file counts, approved styling metadata, 112 variant partner mappings, original archive SHA-256 values, and existing canonical G001–G150 SVG presence.

**Next step (only after explicit selection work begins):** audit exact duplicates, near duplicates, reflections, rotations and small-size legibility across the canonical and stylized sources; then vote keep / modify / replace / remove. Stage 1 visual approvals **do not** make any glyph canonical and meanings remain unassigned.
