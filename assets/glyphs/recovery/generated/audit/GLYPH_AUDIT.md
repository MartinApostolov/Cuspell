# Cuspell 150-glyph visual audit

**Audit scope:** all 150 current active glyphs from the canonical `source_geometry.json`. The audit does **not** modify approved glyph geometry. All numeric scores are automatic *review flags*, not proof two glyphs are identical or approved/rejected.

## 1. Summary

| Check | Result |
| --- | --- |
| Registered & rendered source SVGs | 150/150 |
| Declared mirrored links tested | 32 |
| High visual-similarity pairs excluding declared mirrors | 23 candidates above thresholds |
| Declared mirrored links with visual mismatch (MAE > 0.055) | 0 |
| Declared mirrors almost identical *unmirrored* at 16px (cos≥0.94) | 0 |
| Multiple strokes (>3 start commands) excluding traced-fill images | 1 |
| Tiny high-res detached pieces (<1.5% of ink area) | 0 |
| Glyphs with <5 solid pixels at 16px | 0 |
| High-resolution silhouette touching SVG cell boundary | 2 |
| Observed SVG stroke widths (units) | 66.0 |

## 2. Potentially confusable *unrelated* pairs

The ranking excludes declared direct mirror pairs, but **not intentional 180° variants** or historical visual families. Both high-res and native 16px scores are shown so that similar-looking strokes are not overlooked. A score of 1.0 means equal sampled alpha silhouettes; 0.0 means no overlapping ink in the fixed cell. These measures alone do not model handwriting variation.

| Glyphs | 60×100 cosine | 16px cosine | 60×100 IoU | 16px IoU |
|---|---:|---:|---:|---:|
| G071 / G072 | 0.906 | 0.924 | 0.824 | 0.895 |
| G079 / G080 | 0.906 | 0.924 | 0.824 | 0.895 |
| G037 / G066 | 0.898 | 0.912 | 0.804 | 0.780 |
| G038 / G067 | 0.897 | 0.912 | 0.802 | 0.769 |
| G001 / G023 | 0.870 | 0.919 | 0.717 | 0.765 |
| G002 / G024 | 0.870 | 0.919 | 0.717 | 0.765 |
| G037 / G079 | 0.870 | 0.919 | 0.711 | 0.789 |
| G037 / G080 | 0.870 | 0.919 | 0.711 | 0.789 |
| G038 / G072 | 0.837 | 0.894 | 0.678 | 0.650 |
| G038 / G071 | 0.837 | 0.893 | 0.678 | 0.650 |
| G054 / G057 | 0.795 | 0.841 | 0.655 | 0.706 |
| G055 / G056 | 0.795 | 0.841 | 0.656 | 0.706 |
| G025 / G073 | 0.724 | 0.845 | 0.532 | 0.640 |
| G066 / G079 | 0.789 | 0.842 | 0.613 | 0.638 |
| G066 / G080 | 0.789 | 0.842 | 0.613 | 0.638 |
| G026 / G074 | 0.729 | 0.835 | 0.538 | 0.680 |
| G089 / G090 | 0.785 | 0.822 | 0.610 | 0.600 |
| G031 / G054 | 0.670 | 0.825 | 0.479 | 0.529 |
| G032 / G055 | 0.670 | 0.825 | 0.478 | 0.529 |
| G112 / G132 | 0.668 | 0.825 | 0.485 | 0.517 |
| G111 / G131 | 0.668 | 0.825 | 0.485 | 0.517 |
| G067 / G072 | 0.752 | 0.815 | 0.573 | 0.531 |
| G067 / G071 | 0.752 | 0.815 | 0.573 | 0.531 |

See `near_pairs.png` (first 24 candidates) and `audit_data.json` (all candidate scores).

## 3. Mirroring and small-size ambiguity

A mirror relationship is measured after horizontally flipping the declared partner's alpha mask. Large MAE (>0.055) suggests the `mirror_of` metadata or geometry needs checking; values near zero usually indicate correct mirroring. The 16px cosine shown separately measures *the two signs as printed*, without flipping: a score ≥0.94 may mean the pair becomes almost indistinguishable at that size.

Mirrored links with largest post-flip error: G083/G084: 0.0004, G091/G092: 0.0004, G095/G096: 0.0004, G105/G106: 0.0004, G133/G134: 0.0004, G081/G082: 0.0003, G093/G094: 0.0003, G097/G098: 0.0003, G099/G100: 0.0003, G103/G104: 0.0003, G107/G108: 0.0003, G123/G124: 0.0003.

Mirror pairs with nearly identical 16px appearances (0): none.

## 4. Construction, pen strokes and small print

SVG stroke widths: **66.0**. These reflect `stroke-width` declarations for centerline SVGs only; filled screenshot traces cannot be assigned a reliable pen-width or gesture order from silhouettes alone.

Filled-outline source SVGs (typically screenshot traces, not pen-path guides): **22**. Their stroke count is not objectively recoverable from outline geometry; a hand-drawing test is still required.

Four-or-more distinct path starts (untraced SVGs): **G070**.

Suspicious tiny detached pieces in high-res raster: **none**.

Less than five strong ink pixels at 16px em: **none**.

Touches outer cell boundary (possible SVG clipping): **G068, G070**.

See `all_at_16_and_18px.png` for the entire inventory at native target rendering sizes. Text intended for users at this size must be evaluated by a human, because automated tests cannot establish legibility.

## 5. Generated font integrity

- TTF present: **True**. WOFF2 present: **True**.
- Font private-use mappings G001–G150: **150** (expected 150).
- Missing/wrong cmap entries: **none**.
- Missing glyph names: **none**.
- Non-600 advance widths: **0**.
- Empty TTF glyph outlines: **none**.

## 6. Interpretation / next review

1. Inspect `near_pairs.png`, especially pairs with cosine ≥0.90 at 60×100 or ≥0.95 at 16px. Decide whether apparent similarities are deliberate family members, accepted transformations or truly confusing alternatives.
2. Check pairs that mirror correctly but render almost identical at 16px. The historical glyph register may deliberately include some near-symmetric mirrors; do not remove them automatically.
3. Inspect `all_at_16_and_18px.png` at *actual* size, then perform a handwriting trial for multi-stroke candidates and screenshot-derived outlines.
4. Do not revise or delete user-approved vectors without user review; preserve both the original sources and archived rejected variants.

**Caveat:** all 150 active glyphs have been selected for the current recovery, but many later SVGs are reconstructed rather than authentic lost v0.19 geometry; 100 early glyphs have authentic historical vectors. Exact handwritten gesture orders for later reconstructions are not recovered.
