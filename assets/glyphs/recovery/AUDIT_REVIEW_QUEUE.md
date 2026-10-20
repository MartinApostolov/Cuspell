# Final glyph quality audit — human review queue (October 20, 2026)

The complete reproducible numerical and preview audit lives in
`generated/audit/GLYPH_AUDIT.md`, `generated/audit/audit_data.json`,
`generated/audit/near_pairs.png`, and
`generated/audit/all_at_16_and_18px.png`.
The script `audit_glyphs.py` runs from the glyph recovery GitHub workflow.

**No original or user-approved glyph geometry changed during this audit.**
Automated visual scores prioritize review; they do not constitute rejection.

## Machine-verified baseline

- 150/150 current SVGs rendered; 150/150 private-use font mappings; no
  missing or empty font outlines; WOFF2 present; all advances 600.
- All centerline `stroke-width` declarations are 66 units. This does not
  validate stroke thickness in 22 screenshot-filled silhouette vectors.
- 32 explicit mirror links tested and all geometrically consistent; 21
  older exact mirrored siblings were inferred directly from their original
  vectors because the early records did not always include `mirror_of`.
  The inferred historical siblings are *excluded* from unrelated-pair rankings.
- No tiny detached components detected by the current alpha threshold.
  All glyphs leave >=5 solid pixels at a 16px em rendering, but this alone
  cannot prove readability.
- 20 similarity pair-comparisons flagged above conservative numeric
  thresholds, representing fewer than 20 independent design families.

## Review decision 1: accepted unchanged

2026-10-20: User chose to **keep G037/G038 and G066/G067 as they are** after viewing their similarity. No SVGs were changed. Next comparison: G001/G002 versus G023/G024.

## Review decision 2: accepted unchanged

2026-10-20: User chose **KEEP G001/G002 and G023/G024**, accepting the detached
dot as sufficient distinction. No SVG geometry changed.

## Review cadence: three groups at a time

Per user request, show **three independent comparison groups per round**,
while still recording decisions on each group separately.

**Previous rounds:** groups 1,2,3,5,6,7 kept; group 4 G070 revised and approved. Review previews were rasterized from
authentic older vector sources and show a true native 16px sample.
All designs stay unchanged until explicitly reviewed.

## Human decisions — batch G03–G05 (2026-10-20)

- **Group 3: KEEP UNCHANGED** G037/G038, G071/G072, and G079/G080. The user accepts the distinct curved-family variants. Old vector data unaffected.
- **Group 5: KEEP UNCHANGED** G054/G057 and G055/G056. The user accepts their subtle historical differences. Old vector data unaffected.
- **Group 4: REVIEWED AND APPROVED G070 REVISION.** The two lower strokes became one continuous arc (`M 74 636 C 184 670 416 670 526 636`), reducing path starts from 5 to 4. The new SVG IS NOW CANONICAL. The original authentic v0.13 SVG survives in `drafts/G070_2026-10-20_unified_lower_line/G070_original_v013.svg`. After regeneration, G070 is still flagged for cell-edge proximity, so the margin warning remains open.
- **G068 remains flagged for SVG-cell horizontal margin**; no request to edit G068 has been made.

**Next three groups presented:** 8 G111/G112 vs G131/G132; 9 G066/G067 vs G079/G080; 10 G115/G116 gesture usability. Saved as `audit/REVIEW_BATCH_08_09_10.svg`.

## Human decisions — groups 4, 6, and 7 (2026-10-20)

- **Group 4: APPROVED G070 REVISED LOWER STROKE.** User said "all fine" to the visual comparison showing the continuous lower line; promoted exactly the draft SVG into canonical `source_geometry.json`. Five path starts become **four**. Original v0.13 source remains archived in the draft folder. G068 was also shown unchanged; its margin alert is acknowledged and **kept** at this review, not geometrically fixed.
- **Group 6: KEEP** G025/G026 versus G073/G074; accept their underlying resemblance.
- **Group 7: KEEP** G031/G032 versus G054/G055; accept their related curves. No geometric edits.

**Remaining audit review batches (three at a time):**
8. Screenshot-traced G111/G112 versus tentatively identified G131/G132.
9. G066/G067 crossed-curves versus G079/G080 opposite-direction marked curves.
10. Stroke-order usability of screenshot-derived G115/G116 (original hand sketch was approved; authentic gesture guide still missing).

## Recommended manual order (three groups per review round)

1. **REVIEWED, KEEP:** G037/G038 vs G066/G067 (largest *unrelated* silhouette similarities:
   approx 0.90 cosine at 60x100 and 0.91 at 16px).
   The later glyphs add a crossbar to the existing upward/downward arc.
   Decide if that difference remains clear when handwritten and at 16px.
2. **REVIEWED, KEEP:** G001/G002 vs G023/G024 (~0.87 high-res, ~0.92 at 16px).
   Their distinction relies substantially on a little dot or detached mark;
   check if it survives quick, small writing.
3. **REVIEWED, KEEP:** G037/G038 vs G071/G072 and G079/G080.
   Arched/pointed outlines in the same broad family with short added marks.
   G071/G072 and G079/G080 are each authentic intentional MIRROR pairs,
   not independent lookalike collisions.
4. **G068 and G070**: rendered black silhouettes touch an edge of their
   600x1000 SVG cell; there may be clipping or unsafe glyph margins.
   G070 also contains **five path starts**, well above the usual 1–2
   gesture target (three sometimes). Consult earlier decisions about
   standardized bud + line before changing these original older glyphs.
5. **REVIEWED, KEEP G054/G057 and G055/G056**; other secondary comparisons: G054/G057, G055/G056,
   G025/G073, G026/G074, G031/G054, G032/G055, and screenshot-traced
   G111/G131, G112/G132. These are numeric candidates and require
   visual rather than automatic decisions.

## Historical source caveats

The early 100 original historical SVG outlines are authentic v0.13/v0.14 R1;
that does **not** prove they exactly match the later lost v0.19. After
G100, 22 entries were traced from screenshots and multiple others were
modern descriptions or explicitly approved redesigns. Their original
stroke direction cannot be established from outlines alone.

### Guardrails

- No automatic deletion, reassignment, semantic assignment, or vector
  substitution, even when similarity score is high.
- Keep history of every accepted revision and rejected alternative.
- Review **one cluster at a time** and commit only accepted changes.
- Repeat the full audit after any accepted vector changes and verify fonts.
