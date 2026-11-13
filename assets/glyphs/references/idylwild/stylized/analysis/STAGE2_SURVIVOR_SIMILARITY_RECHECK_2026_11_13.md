# Stage 2 — complete surviving-pool visual similarity re-check (2026-11-13)

## Review decision — 2026-11-13, Groups 21–24

User: “For the ones in the last set I don't see problems.” This means **provisional visual keep for all 14 glyphs in Groups 21–24** (G041, R012, A019, R004, G062, R034, R046, G069, R031, R083, A059, R005, R110, A051). They remain eligible; none received a new exclusion or permanent root mapping. **R012 stays on its previously assigned short leash.** Other earlier review flags remain unchanged.

The earlier Groups **17–20 were not renamed or dropped**: they used numeric-ID presentation, then each surviving member was included in the full 246-design similarity scan. Among those 16: R010/R018 were excluded, R012/R023 were put on the leash, G041/G069/R004/R005 were re-presented in the newly grouped 21–24 and provisionally approved; **G068/G146/R001/R006/R008/R011/R024/R028** were shown in 17–20 but have no explicit acceptance decision yet. Show those with relevant nearest neighbors in subsequent similarity-based groups before treating their suitability as resolved. Do not infer implicit keep solely from absence of a removal instruction.

No eligibility-count change: 246 eligible, 88 exclusions, 3 reserved punctuation sources, 218 required, 28 spare.

**Branch:** `glyphs/idylwild-style-sample-01` (PR #124); this is a **screening report**, not a decision to remove glyphs.

## Coverage and corrected methodology

- Verified the current Stage 2 ledger: **337 normalized starting designs; 88 excluded; 3 original designs reserved for player punctuation; 246 magic/numeric-eligible designs**.
- Scanned all **246** surviving designs, comparing every pair (**30,135 distinct pairs**) using **their original G source art or stylized Idylwild SVG art**. The source Runic alternate-ink variants R113–R224 were not double-counted.
- Screening method: rasterize source SVG strokes/filled paths to 60 × 100 masks; compare pixel Dice overlap under original orientation, horizontal reflection, vertical reflection, and 180-degree rotation. The scan had **0 empty/invalid masks**. Numerical scores rank examples for **visual inspection**, not automatic duplication decisions.
- **55** eligible designs remain outside the original 116 similarity groups, later shown suitability/punctuation sheets, and short-leash lists **without yet having been shown to the user**. The previously shown Groups 17–20 were arranged by ID, not similarity, so those designs have now been cross-checked too.
- Lookalike ranking alone is insufficient: a straight staff can score highly against an arrow even when the actual glyph is obviously different; magnified images, small-size text tests, symmetry under rotations, and the user's actual decisions still matter.

## First four source-derived, visual comparison sets (Groups 21–24)

| New group | Source glyph IDs | Preliminary evidence | Status |
| --- | --- | --- | --- |
| 21 — X-shaped designs | G041, R012, A019 | G041/R012 ≈ **0.730** (vertical flip); R012/A019 ≈ **0.710** | Compare; **R012 already on short leash**; no new exclusion |
| 22 — several branches from one stem | R004, G062, R034, R046 | R004/G062 ≈ **0.721** (vertical flip); R004/R034 ≈ **0.715** | Visually examine R004 and R034, particularly at small size; no decision yet |
| 23 — branching/forked verticals | G069, R031, R083, A059 | G069/R031 ≈ **0.726** (vertical flip); G069/R083 ≈ **0.713** | Broad morphology overlap, **not** a confirmed duplicate; R031/R083 already provisionally kept earlier |
| 24 — V/forked stems | R005, R110, A051 | R005/R110 ≈ **0.723**; R005/A051 ≈ **0.664** | Compare; all still eligible |

Pictures for these four groups were rendered in chat directly from the project's SVG path geometry; images are review aids and do not redefine canonical glyph assets.

## Further unresolved clusters to display next

The highest-ranking **previously unshown** design pairs from the full scan include:

- R112 ↔ R014 ≈ **0.792**, plus R051 ↔ R014 ≈ 0.757
- A038 ↔ A053 ≈ **0.787**, A038 ↔ A072 ≈ **0.784**, and A038 ↔ A068 ≈ 0.749 under rotation
- A064 ↔ A065 ≈ **0.783** under vertical flip (also R104 ≈ 0.703 with A064)
- R046 ↔ R074 ≈ **0.780**, and R074 ↔ R094 ≈ 0.751 under rotation
- R078 ↔ R017 ≈ **0.764**, R067 ↔ R064 ≈ 0.738, A016 ↔ A063 ≈ 0.704

High scores among *previously reviewed* pairs also appeared (R031/R083 ≈ 0.943; R030/R076 ≈ 0.923; G085/G086 ≈ 0.911); they retain prior user decisions and are **not** automatically re-excluded.

**Full machine-readable ranked scan:** `FULL_SURVIVOR_SIMILARITY_RECHECK_2026_11_13.json` in this directory. It contains all 55 as-yet-unshown candidates with their nearest six surviving neighbors, the previously shown Group 17–20 candidates with their neighbors, and the 150 highest-scoring pairs.

## Next steps / preservation

1. Get user KEEP / EXCLUDE / SHORT LEASH choices for Groups 21–24 after showing **high-resolution pictures in the chat**.
2. Continue four grouped visual comparisons per round using the strongest remaining unchecked matches, not sequentially sorted IDs.
3. Finish the unchecked designs before clearing individual and paired short leashes. Last, test the selected set at small rendered font sizes and against punctuation.

**No changes to eligibility, rooted meanings, source archives, font mappings or parser.** Keep all previous explicit decisions; no glyph exclusions based solely on this score.

## Prepared visual review — Groups 25–28 (2026-11-13)

These are the next four comparison sheets, based on nearest-neighbor search against all 246 surviving designs. **No user decisions yet; do not mark these as finally kept/excluded.** Source SVGs rendered at native high resolution rather than enlarging low-resolution similarity masks.

| Group | Designs | Reason to compare | Note |
| --- | --- | --- | --- |
| 25 | R112, R014, R051, R088 | R112/R014 and R051/R014 are close in the full-pool scan | R014 resembles Latin N; R112 includes a distinct detached dot |
| 26 | A038, A053, A072, A068 | Dense parallel vertical elements; mirror and rotational matches | A038/A053/A072 are closer than A068 |
| 27 | A064, A065, R104, A025 | Ovals with stems or small features | A064/A065 are vertical-flip lookalikes; conventional symbol resemblance needs visual review |
| 28 | R046, R074, R094, R008 | Curved-staff loops, with partial similarity | R008 was already shown in ID-based Group 19 without an explicit keep decision; R094 resembles 8 |

Original art and source archive files are unchanged; all four groups are awaiting user visual decisions. Other Groups 17–20 pending designs remain eligible and should receive their own full-pool neighbor comparisons later. Inventory unchanged at **246 magic-eligible, 88 excluded, 3 punctuation-reserved**.

