# Stage 2 suitability — first four groups & punctuation (2026-10-29)

Working branch: `glyphs/idylwild-style-sample-01`; draft PR #124, not main.

## Explicit decisions

1. **R076 is a magic glyph candidate**, not the exclamation point. The R188 linked alternate source remains available. User requested a **new independent `!`** drawn in Cuspell style.
2. User had **no suitability concerns** with the 12 other displayed designs: Group 2 — R030, R108, R009, A018; Group 3 — A039, A062, R098, R019; Group 4 — R083, A070, A073, A075. Keep eligible; do not mark final/root-accepted. Existing **R098 short leash** on near-similarity remains until explicitly changed.
3. Draw **only player-facing punctuation** in the same styling: `.`, `:`, `?`, `!`, `«`, `»`, `$`, `(`, `)`, `_`, `{`, `}`, `,`.

## Draft art and implementation

All 13 drawings are individual editable SVGs in `../typography/player_facing/`, using 600×1000 coordinates and 66-unit rounded black strokes. Existing chosen punctuation sources R105 / R106 / A054 stay the approved visual sources for `.` / `:` / `?`; their source assets are untouched. New punctuation `!` does not borrow/reclassify R076.

Typography is fixed-function: it does **not** consume randomly assigned semantic roots. Numeric `@` remains a special numeric magic sign. No debug pipe, compatibility square brackets, or optional non-core punctuation added.

New punctuation is in **visual draft**, not compiled into a new font; no cmap, parser, gameplay, root assignment or source-art changes.

## Counts unchanged

Normalized designs before selection **337**; directly excluded **82**; imported normalized designs reserved for punctuation **3**; magic-eligible normalized designs **252**; needed semantic/numeric signs **218**; provisional headroom **34** (visual uniqueness not yet established). No destructive deletion.

Next: visually approve/tweak punctuation prototypes and continue systematic symbol suitability on remaining unreviewed candidates.
