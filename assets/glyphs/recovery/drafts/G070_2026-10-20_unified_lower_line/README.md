# G070 — one long lower cross-line (unapproved review draft)

User instruction, 2026-10-20: merge the two small lower side lines of G070
into one big continuous line. The original G070 design is an authentic
v0.13 outline; avoid losing it.

The proposed design:
- Keeps the original long central stem and two upper curved bud strokes
  **byte-for-byte**.
- Replaces two lower outward-curving strokes with **one long, shallow
  continuous curved bar** from x=74 to x=526, crossing the central stem.
- Maintains rounded 66-unit monoline stroke and 600×1000 cell.
- Reduces separate path starts **5 → 4**. This is an improvement but remains
  above the usual 1–2 stroke target.
- Insetting the new line avoids G070's previously flagged left/right
  cell-boundary contact; this does not resolve G068's separate margin concern.

The proposal is NOT yet canonical or visually approved; current
`source_geometry.json` remains unchanged. Exact original SVG is preserved
as `G070_original_v013.svg`. Wait for user's decision, then repeat the
150-glyph audit and font generation if the edit is accepted.
