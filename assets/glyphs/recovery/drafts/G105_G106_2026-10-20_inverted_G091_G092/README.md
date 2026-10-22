# G105 / G106 — exact 180-degree inversion of original G091 / G092

**APPROVED on 2026-10-20 and promoted into canonical `source_geometry.json`.**
This remains the historical draft record of the precise SVG files accepted; do not remove.

Request: "Can we take 91/92 and flip them upside down for 105/106?"

Construction: G105 is G091 rotated exactly 180° in the 600 × 1000 unit glyph
cell: `x_new = 600 - x_old`, `y_new = 1000 - y_old`. G106 is G092 rotated
180° and is an exact horizontal mirror of G105.

The Bézier paths are *flattened to actual SVG path coordinates*, not wrapped
in an unrecognized rotation transform. This matters for the recovery script's
font-outline generation (which parses SVG path coordinates and only explicitly
supports mirror transforms). No original G091 or G092 artwork was modified.

Source original: recovered authentic original v0.14 R1.
Proposal date: October 20, 2026.
Previous G105/G106 leaf-on-stem and side-leaf alternatives remain preserved in
the adjacent previous draft folder.
