# Cuspell — full player-punctuation vs magic-glyph collision scan

> **CURRENT DECISION — 2026-10-29:** User excluded `G054` and `R099` after punctuation-glyph comparison; `R211` is the equivalent second-ink Runic source and inherits exclusion. User put `A012` and `A013` on the short leash (still eligible). `G055` was excluded previously. No other glyph from the displayed four groups was newly excluded or automatically approved; particularly the `!` collision group remains unresolved and R076 stays a magic candidate. The JSON ledger now records 84 excluded normalized designs, 250 eligible magic designs, 3 source designs reserved for punctuation, 218 required and 32 provisional spare. The 252 count in the pre-decision scan is historical. Render future comparison sheets directly from source SVGs at high resolution, **not by enlarging 60x100 raster masks**.

**Date:** 2026-10-29  
**Branch:** `glyphs/idylwild-style-sample-01` (draft PR #124)  
**Status:** **REVIEW CANDIDATES ONLY**; no exclusion, font change, parser change, meaning assignment, or change to an existing user keep.

## Coverage

- **All 252 currently magic-eligible normalized designs:** 102 canonical original Cuspell `G` SVGs; 84 first-ink Idylwild Runic `R001–R112` designs; and 66 Idylwild Alchemical `A` designs.
- **All 13 draft player-facing punctuation / syntax glyphs** under `stylized/typography/player_facing/`: `.`, `:`, `?`, `!`, `«`, `»`, `$`, `(`, `)`, `_`, `{`, `}`, `,`.
- **3,276 glyph–punctuation pair categories** (252×13), each checked by a source-SVG-derived approximate binary silhouette and additional translation/mirror trials.
- The 112 linked Runic second-ink archive IDs are **not extra distinct designs** and were represented by their normalized partners. Directly excluded designs (including **G055**) and previously approved punctuation designs **R105/R106/A054** were not counted among the 252 magic candidates.
- The special `@` numeric-one glyph is not punctuation and is part of the required 218 semantic/numeric sign slots. No permanent numeric-one art is assigned in this suitability scan.

## Summary / review candidates

| Punctuation | Major or plausible collision candidates | Assessment |
| --- | --- | --- |
| `$` | **G054** (near-dollar), **G055** (similar but **already excluded**); secondary R026 and other curved/staff shapes | **HIGH: G054**. User specifically noticed this and the real SVGs confirm the lookalike. Do not exclude automatically. |
| `(` / `)` | **A012** open crescent and **A013** facing crescent; secondary G127/G128, R021 | **HIGH: A012/A013**. They are visually close to parenthesis forms, especially as a matched pair. The others are more angular/different on direct inspection. |
| `?` | **R099** curled hook without the detached lower dot; secondary G102 and G092 curls | **HIGH: R099**, with G102/G092 **REVIEW**. R099 can read as `?` with the dot omitted. |
| `!` | **R076** (dot above rather than below), **R030** (just an upright stroke), R017 (cross), A047 (upright with four side dots), A075 (crossbar) | **REVIEW**, especially R076/R030 at small sizes. The user explicitly retained R076 as a magic candidate; do not reclassify it as punctuation. The other shapes have distinguishing details. |
| `«` / `»` | G097/G098, A004 and R102/R103 had moderate silhouette matches | **LOW–REVIEW**: no clearly interchangeable source shape identified on this pass. |
| `{` / `}` | A012/A013, G036/G058, R017/R030 and related straight-stem drawings were broad silhouette hits | **LOW–REVIEW**: most hits share vertical extent or curvature but lack the brace's indented middle; not identical to braces. |
| `.` | No direct close match among 252; maximum raster score was low | **LOW**. |
| `:` | No direct close match; R076 score reflects its detached dot and stem but is structurally different | **LOW**. |
| `_` | G025/G026 and R025 had some overlapping lower horizontals | **LOW**, not a clear standalone underscore. |
| `,` | No convincing direct match | **LOW**. |

### Source-confirmed examples from the top visual review

- Dollar row: `$` / G054 / **G055 (already excluded)** / R026 / A047 / G070 / G148.
- Parenthesis row: `(` / `)` / G127 / G128 / R021 / **A012** / **A013**.
- Exclamation row: `!` / **R030** / **R076** / R017 / A047 / G036 / A075.
- Question row: `?` / **R099** / G102 / G092 / A055 / A007 / G133.

The first two problems highlighted by the user (**G054/G055 dollar and parenthesis-like glyphs**) are real concerns. G055 has already been excluded in an earlier similarity pass; G054 and A012/A013 are presently still eligible.

## Machine triage method and caveats

Scanned the authoritative original Cuspell art in `assets/glyphs/recovery/source_geometry.json`; external **actual stylized SVGs** from the 19 Idylwild sample manifests; and the 13 current punctuation drafts. A scan helper is preserved alongside this report as `punctuation_collision_mask_scanner.js` (a JavaScript expression that evaluates to a `score(svg)` function).

The method rasterizes SVG path/circle geometry to a **60×100 ink mask**, approximately respects filled contours, evaluates the Dice overlap with each punctuation image under modest shifts and left/right reflection, then ranks likely collisions for human examination. This is **not** a final uniqueness proof: it can rank unrelated upright strokes highly, underweight distinctions in small terminals, fail to model all font metrics, and produce false positives for parentheses/braces. The **shape judgments in the table** are based on reviewing source-derived visual comparison sheets, not raw score alone. The scan does not certify safety at tiny text sizes or under all game UI effects.

Examples of rough scores as triage indicators (not acceptance thresholds):
- `G054` versus `$`: approximately **0.655** (reflected best overlap).
- `R030` versus `!`: approximately **0.890** (stem alone; lacks punctuation dot).
- `R076` versus `!`: approximately **0.848** (dot at opposite end).
- `R099` versus `?`: approximately **0.699** (question-hook, missing detached dot).
- `A012` and `A013` versus parentheses: approximately **0.53–0.56**, but direct visual inspection reveals a stronger perceptual resemblance than the overlap numbers imply.

## Proposed next human-decision groups

1. `$` vs G054 (context: G055 excluded) — keep G054 as magic, modify glyph, alter `$` typography, or exclude G054?
2. `(` and `)` vs A012/A013 — keep magic crescents, redesign punctuation pair, or exclude either?
3. `?` vs R099 and G102/G092 — keep as magic, modify, or exclude?
4. `!` vs R030/R076/A047 (plus secondary R017/A075) — retain distinct marks at target font size, redesign typography, or otherwise classify?

Then check any further low/medium flagged similarities before finalizing the 218 sign alphabet and font.

## Preservation constraints

**No decision automatically taken from similarity score.** Exclusions remain 82 normalized originals, typography source reserve remains 3 designs, and magic-eligible candidate count remains **252**. `R076` remains eligible as previously directed. No current short-leash or pair decision is cleared, no source SVG deleted or rewritten, and there is no change to the parser, root assignments, font cmap, or `main`.
