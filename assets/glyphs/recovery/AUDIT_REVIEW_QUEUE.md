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

## Recommended manual order (one group at a time)

1. **G037/G038 vs G066/G067** (largest *unrelated* silhouette similarities:
   approx 0.90 cosine at 60x100 and 0.91 at 16px).
   The later glyphs add a crossbar to the existing upward/downward arc.
   Decide if that difference remains clear when handwritten and at 16px.
2. **G001/G002 vs G023/G024** (~0.87 high-res, ~0.92 at 16px).
   Their distinction relies substantially on a little dot or detached mark;
   check if it survives quick, small writing.
3. **G037/G038 vs G071/G072 and G079/G080**.
   Arched/pointed outlines in the same broad family with short added marks.
   G071/G072 and G079/G080 are each authentic intentional MIRROR pairs,
   not independent lookalike collisions.
4. **G068 and G070**: rendered black silhouettes touch an edge of their
   600x1000 SVG cell; there may be clipping or unsafe glyph margins.
   G070 also contains **five path starts**, well above the usual 1–2
   gesture target (three sometimes). Consult earlier decisions about
   standardized bud + line before changing these original older glyphs.
5. **Secondary lower-priority comparisons**: G054/G057, G055/G056,
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
