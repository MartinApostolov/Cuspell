# Cuspell Stage 2 — first visual similarity review (no removals)

A broad similarity scan has examined all **449** glyph source records (150 canonical G, 224 Runic and 75 Alchemical). For computational cross-comparison, 112 later Runic sources R113–R224 were grouped with their corresponding R001–R112 variants, leaving **337 prototypes**. SVG stroke centerlines were rasterized into 32×56 image masks; pairwise similarity was evaluated both as drawn and under horizontal reflection, vertical reflection or 180-degree rotation. Scores are optical screening indicators, **not proof of interchangeability**. Some detailed distinctions may disappear at this small raster size; false positives must be checked by human review.

## Strong initial candidates to consolidate
- **Provenance duplicates:** R113–R224 are +112 alternate-ink versions of R001–R112. These are separate archived source records but not extra normalized silhouette choices. **112** redundantly indexed vector candidates.
- **Current Cuspell mirror pairs:** **64** pairs (128 current G signs) score as exact left/right mirrors on the coarse grid. See `review_cuspell_mirror_pairs.svg`. We can retain one orientation per pair *if the user agrees*. Some distinctive orientation families may be worth retaining.
- **Existing Cuspell rotated quartets:** G071/G072/G079/G080 and G091/G092/G105/G106; these are extremely closely related via 90/180-degree view/flip handling and merit separate review.
- **Runic high-priority near-identical pairs:** R020/R030 (visually identical on coarse mask), R065/R074, R071/R080, R022/R044 and R032/R040.
- **Alchemical high-priority cluster:** A022, A043 and A044, with A009 a reflection/rotation relative.
- **Cross-pack cases:** R016/A048/A056/R101, R072/R108/A073/A075, and R049/A060.
- **Existing-to-imported overlap:** G033 vs R037 (a candidate potential collision even without reflected orientation).

See `review_close_matches_1.svg` and `review_close_matches_2.svg` for actual vector illustrations in the saved source orientation.

## Review method and limits

Use this as a **shortlist**, not a delete list. A glyph pair that resembles itself after reflection/rotation might be acceptable if orientation is semantically significant, but the stated project direction is to reduce learning burden and mirrored signs. Keep stroke spacing and small-size legibility in mind. Follow-up should verify actual outline geometry at intended font size before accepting any automatic pair; consider whether subtle dots or short strokes reliably survive downscaling. Preserve all source archives, variant IDs, revisions, and reasons for any future retirements.

**No canonical G001–G150 has been edited, no variant source deleted, and no Cuspell meanings assigned.** User approval is required for every final keep/remove/modify decision.
