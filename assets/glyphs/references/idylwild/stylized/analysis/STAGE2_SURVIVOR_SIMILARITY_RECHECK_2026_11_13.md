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


## User response and next review — 2026-11-13

**Groups 25–28:** User said “All fine. Next set.” All 16 presented designs are provisionally kept, with any older watchlist decisions preserved. The JSON selection ledger records this as a new review event. No source assets, fonts, meaning assignments or eligibility counts changed.

**Groups 29–32 are prepared for user visual review** (clear SVG-derived comparison pictures were shown in chat):

| Group | Drawings | Main comparison issue | Decision |
|---|---|---|---|
| 29 — vertical staffs | R078, R017, R030, R073 | R078 has three lateral branches; R017 crossbar; R030 bare vertical stem, previously explicitly kept; R073 more ornate | Pending |
| 30 — angled staffs | R067, R064, R061, R040 | R067/R064 share branches on the staff under reflection; R061 and R040 upper curving strokes | Pending |
| 31 — looped forms | A016, A063, A032, A025 | **A016/A063 are especially visually alike**; A032 changes the loop, and A025 was previously shown in Group 27 | Pending |
| 32 — forked stems | R037, A051, R050, A071 | Shared central stem with upper branches in R037/A051/R050; A071 oval-staff alternative. A051 was provisionally kept in Group 24 | Pending |

These candidates were selected from the **all-246 survivor** similarity report, not sequentially by ID. Nearness scores are triage only; retain all until direct user selection. R030 was previously retained deliberately despite its simple shape, so no unilateral change.

The next review should continue through remaining not-yet-shown designs and the outstanding members of Groups 17–20; then clear the leash. **Still 246 eligible, 88 excluded, 3 typography source reserves, 218 required, 28 spare.**

## Latest decisions and pending visual review — Groups 29–36 (2026-11-13)

User: **“Get rid of A063 and put R050 on the leash. Next.”** The Stage 2 selection ledger now records **A063 excluded** (the close A016/A063 pair from Group 31) and **R050 short-leash** (Group 32), still eligible. All other Group 29–32 candidates stay as before; no additional approvals/exclusions inferred. Source SVGs are preserved.

**Updated normalized inventory:** 337 original designs; **89 exclusions**; 3 source typography reserves; **245 eligible magic/numeric designs**, 218 required, **27 spare**. Earlier references in this file to 246 survivors/30,135 pairs are a historical snapshot of the pre-exclusion scan; the scan still identifies useful lookalikes among survivors. Remove excluded A063 from future candidate checks.

New high-resolution source-SVG comparison sheets for **Groups 33–36** were created for user review; **all pending**:

| Group | Glyphs | Reason |
| --- | --- | --- |
| 33 | R053, R056, A059, A072 | Forked upper branches, curved crossbars and centered staffs; R053/R056 previously unshown |
| 34 | A027, A046, A044, A043 | Enclosed and axis-crossing structures; A043/A044 have similar enclosed oval details but were previously shown |
| 35 | R084, R111, R041, R086 | Central staffs with crossings, outlines, or enclosed center; some rotational/partial matches |
| 36 | A002, A071, A005, A055 | Head-on-stem and upper geometry; A002/A005 newly shown, A071/A055 prior reference designs |

Do not exclude or short-leash these without further user instructions. Continue displaying actual, high-resolution glyph comparisons **four groups at a time**, avoiding already excluded sources and postponing existing short leashes until unseen review finishes. No merge into `main`, canonical font, parser or semantic root updates.



## Latest update — R084 decision, visual review Groups 37–40

**2026-11-13 user instruction:** “R084 on the leash. next”. R084 remains eligible, newly marked **SHORT_LEASH** in both the final inventory ledger and sample 11 manifest. No other Group 33–36 selection change was requested. Current counts remain **245 magic/numeric-eligible glyphs**, **89 exclusions**, **3 punctuation-reserved**, **218 required**, **27 spare**.

The next four **pending user visual comparison groups**, produced from existing SVG geometry (not auto-reconstructed images):

| Group | Glyphs | Most relevant similarity |
| --- | --- | --- |
| 37 | R006, R068, R019, R095 | R006/R068 share alternating side branches and a long stem; R019 is a simpler one-branch design. R006 was shown in original Group 18 but not explicitly approved. R068 is newly shown. |
| 38 | R011, R077, R054, R014 | R011/R077 closely resemble the Latin N-like angular crossing; R054 is a curved/tilted branch. R011 is outstanding from original Group 19; R054 is newly shown. |
| 39 | R024, R004, A062, G118 | R024 vs R004 on staff-and-side structures; A062 resembles numeral 4; G118 is an isolated enclosed-loop design, shown as a weaker comparator and should not be labeled a close lookalike. R024 was shown in original Group 20 without explicit approval. |
| 40 | R028, R090, R021, R030 | R028/R090 have serpentine strokes, R021 has angular zigzag, R030 is the plain staff previously explicitly kept. R028 outstanding from original Group 20; R090 is newly shown. R030 is a weaker reference, not an alleged duplicate. |

No new exclusions or global watchlist removals were inferred. The 2026-11-13 full-survivor similarity report predates exclusion A063, but its remaining match data are still suitable for prioritizing surviving comparisons. The ultimate review should be updated to current counts before final font selection.

## User decision and next four review groups — 2026-11-13

- User: **“Okay get rid of R077. and do the next sets.”** Direct exclusion of **R077**, and therefore linked Runic alternate-ink **R189** (not separately eligible). The chosen survivor of the previous R011/R077 comparison, **R011**, remains eligible, but no newly inferred permanent root or meaning assignment.
- **90** normalized designs excluded, **244** magic/numeric-eligible, **3** punctuation sources reserved, **218** required and **26** spare. SVG and source archives untouched. The all-246 November 13 pairwise similarity scan is a historical pre-exclusion snapshot, and its edges involving R077 and previously excluded A063 should not be treated as live candidates.
- **Groups 41–44** prepared as source-SVG comparison sheets, awaiting user decisions:

| Group | Designs | Why grouped |
| --- | --- | --- |
| 41 | G068, R108, A075, R017 | G068 has central stem and symmetrical branches, while the others show cross-staff motifs; G068 from earlier Group 17 still needs explicit verdict |
| 42 | G146, G044, R056, R039 | G146's nearest broad-morphology neighbors and other curved/branch designs; not a tight duplicate group; G146 from earlier Group 17 still pending |
| 43 | R001, G062, R004, R088 | R001's broader curved-staff neighbors from the all-pool scan; R001 from earlier Group 18 still pending |
| 44 | A052, A058, A072, R111 | Looped and central-staff shapes, some nearer under flips; A052 and A058 not previously shown |

**No selections inferred** for Groups 41–44. Continue remaining unshown suitability review before clearing existing short leashes.

