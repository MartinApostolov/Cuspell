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


## User decisions on Groups 41–44 (2026-11-13) and next-thread handoff

User: **"R108 on leash keep the rest."**

**SHORT LEASH:** `R108`, still eligible, not a punctuation reserve.
**PROVISIONAL KEEP:** `G068 A075 R017 G146 G044 R056 R039 R001 G062 R004 R088 A052 A058 A072 R111` (15 designs shown in Groups 41–44).
**No new exclusions**, source SVG changes, meaning bindings, or font changes. Selection ledger `potential_overlap_groups.json` records review ID `SURVIVOR_RECHECK_2026_11_13_GROUPS_41_TO_44`.

Current inventory is **244 magic candidates, 90 exclusions, 3 existing punctuation reserves, 218 required, 26 provisional spares**, with **20 individual leash entries plus 2 unresolved leash pairs**. The old similarity JSON has 246 candidates as of its original run, before A063 and R077 were excluded; filter old exclusions before using its nearest-neighbor results.

After cross-checking the 55 previously identified unchecked designs against every corrected visual group **21–44**, **29 of those 55** still have not appeared in those corrected sheets. They are:
`A008 A010 A011 A015 A017 A020 A021 A029 A030 A031 A033 A034 A035 A036 A040 A041 A042 A050 A057 A074 R036 R042 R043 R057 R066 R082 R089 R097 R100`.

**Next action:** show Groups **45–48** as four actual source-SVG similarity picture sheets with at least one of those 29 in each group. Avoid unnecessary re-review of already accepted examples except as comparators, preserve all watchlist decisions. Continue unchecked designs before clearing the leash. Details and exact resume prompt: `../../HANDOFF_NEXT_THREAD_2026_11_13_AFTER_GROUP_44.md`.

## 2026-11-20 — Groups 45–48 user decision; Groups 49–52 shown

**Direct user instruction:** “keep all. Next set.” Applied only to the four actual-SVG comparison sheets shown for Groups 45–48.

- Group 45: `R042 R051 A008 A065` — all provisionally kept.
- Group 46: `A010 A009 A044 A021` — all provisionally kept. **A009 remains on the short leash**; a keep does not clear it.
- Group 47: `R036 R015 R052 A033` — all provisionally kept.
- Group 48: `A017 A065 R104 A024` — all provisionally kept.
- **15 distinct designs** provisionally kept (`A065` was shown twice), **0 exclusions** and **no leash changes**. Recorded in `potential_overlap_groups.json` as `SURVIVOR_RECHECK_2026_11_20_GROUPS_45_TO_48`.
- Counts unchanged: **244** magic/numeric candidates, **90** excluded normalized designs, **3** punctuation reserves, **218** required; **26** provisional spares. Nothing merged into `main`.

The following are newly prepared **pending user decisions**, comparing source SVG drawings at high resolution rather than redrawing approximate glyphs:

| Group | Actual SVGs shown | Unchecked designs prioritized | Comparison reason |
| --- | --- | --- | --- |
| 49 | `A011 A050 A010 A070` | `A011 A050` | Enclosed/nested contours; A011/A050 broad and imperfect silhouette match |
| 50 | `A015 R041 R086 A001` | `A015` | Centered oval/diamond outlines and outer strokes |
| 51 | `A020 R066 A019 R033` | `A020 R066` | Capped diagonals and branch strokes; A020 vs A019 |
| 52 | `A030 R097 R057 A041` | `A030 R097 R057 A041` | Curved/diagonal motifs, some only weakly similar |

All pictured candidates are still eligible; nobody has yet approved or rejected Groups 49–52.

Among the **29** designs absent from corrected Groups 21–44, seven were newly shown in 45–48 and nine more in 49–52, leaving **13** to prioritize afterward:

`A029 A031 A034 A035 A036 A040 A042 A057 A074 R043 R082 R089 R100`.

This count addresses only that specific list of 29; do not assume it resolves all other historically pending, provisionally undecided designs.

**Sequence:** finish unchecked / pending designs, then clear the 20 individual and two pair short-leash entries. No source art, font mapping or meaning/root assignments changed.

## 2026-11-20 — Groups 49–52 kept; Groups 53–56 presented

**User decision:** “keep all, next. how many more are left?” This is provisional visual keep of **all 16 distinct designs** in Groups 49–52, not exclusion or root assignment. Recorded as `SURVIVOR_RECHECK_2026_11_20_GROUPS_49_TO_52` in the authoritative selection ledger.

- Group 49: `A011 A050 A010 A070` — all provisional keep.
- Group 50: `A015 R041 R086 A001` — all provisional keep.
- Group 51: `A020 R066 A019 R033` — all provisional keep.
- Group 52: `A030 R097 R057 A041` — all provisional keep.
- No exclusion, short-leash resolution, source glyph change, font edit or merge. **244 candidates**, **90 exclusions**, **3 punctuation reserves**, **218 required**, **26 spares**.

**Remaining after Groups 49–52:** Exactly **13 specific designs** from the earlier handoff's 29-design list had not yet been introduced in corrected new groups. This is **not a complete inventory of every previously shown-but-undecided design**; Groups 37–40 and `R006 R011 R024 R028` still have historical unresolved decisions. There are also **20 individual leash records plus 2 unresolved pairs** (24 designs), reserved until unchecked audit finishes.

**Groups 53–56 shown as source-SVG comparison sheets, pending user decisions:**

| Group | Glyphs | Newly prioritized for first corrected review | Main relationship |
| --- | --- | --- | --- |
| 53 | `A029 A040 A053 A072` | `A029 A040` | A040 has a vertical/triple-staff arrangement; A053/A072 share a more enclosing crossbar/stem layout; A029 is visually distinct, matching only some structural features |
| 54 | `A031 A034 R038 R023` | `A031 A034` | Loose cross-neighbor comparison; R023 is **already short-leashed** and remains so |
| 55 | `A035 R043 A068 A055` | `A035 R043` | R043's diamond/triangular forms compare with A055/A068; A035 has separate ovals, a weaker silhouette match |
| 56 | `R100 A074 R094 R102` | `R100 A074` | R100 resembles numeral 8, particularly against R094; A074/R102 share triangular/circular attachments |

SVG review sheets committed only to experimental branch as `stylized/analysis/review_group_53_2026_11_20.svg` through `review_group_56_2026_11_20.svg`. All drawings embed actual source paths; cards introduce no new canonical glyph designs. Other reference fonts, source archives, and parser unchanged.

**After showing Groups 53–56**, 8 of the handoff-specific 13 are pictured for user decision; the **five remaining** are: `A036 A042 A057 R082 R089`. Continue with them (against their closest living G/R/A matches) after receiving keep/remove/leash choices, then reconcile historically pending approvals before clearing short leash. No merge to main.

## 2026-11-20 — Groups 53–56 decision; Groups 57–60 shown

**Direct user decision:** “A040 on the short leash. All the rest if fine, next.”

- **A040 (Group 53)** newly placed on **SHORT LEASH**, still eligible and not excluded.
- The other **15 distinct designs** shown in Groups 53–56 are provisionally kept: `A029 A053 A072 A031 A034 R038 R023 A035 R043 A068 A055 R100 A074 R094 R102`.
- **R023's earlier short leash remains**; a provisional keep does not clear it.
- Selection ledger now includes review event `SURVIVOR_RECHECK_2026_11_20_GROUPS_53_TO_56` plus A040 watchlist entry.
- No exclusions or canonical edits: **244 magic/numeric-eligible**, **90 excluded normalized designs**, **3 punctuation reserves**, **218 required** and **26 spares**.
- Active short leash now **21 individual IDs and 2 unresolved pairs** (23 records, covering 25 still-eligible designs). Do not clear it until unchecked review is resolved.

**Four new comparison sheets are presented for user decision** and committed on experimental branch only:

| Group | Glyph IDs | Main unchecked glyphs | Note |
| --- | --- | --- | --- |
| 57 | `A036 A037 G088` | `A036` | A036's two horizontal zigzags have no especially convincing lookalike among these full-pool reference results; low numerical score; avoid treating weak matches as duplicates |
| 58 | `A042 R066 R054 R047` | `A042` | Diagonal hooked / crossing branches; R066 is a reflection-related full-pool comparison |
| 59 | `A057 A058 A055 A060` | `A057` | A057 double-chevron + dot; others are weaker branch/diamond references |
| 60 | `R082 R050 R089 R103` | `R082 R089` | Two sub-pairs: R082 with R050, and R089 with R103; R050 remains short-leashed |

Saved source-geometry composites: `stylized/analysis/review_group_57_2026_11_20.svg` through `review_group_60_2026_11_20.svg`. These are presentation sheets only, not edited canonical source glyphs.

**Coverage accounting:** these four groups present all five remaining designs in the specific 29-item previously-unshown shortlist from the November 13 handoff. That does **not** imply every previous review is fully decided: outstanding earlier group decisions (especially Groups 37–40 and historical `R006 R011 R024 R028`) still need explicit resolution before clearing the leash. Pending user keep/remove/leash choices for Groups 57–60. No merge into `main`.

## 2026-11-20 — short-leash review opened; first four comparisons pending

The user asked to **begin reviewing the short leash** and compare each flagged design against its surviving lookalikes. The user has **not yet made any keep/spare/remove decisions** on this new round.

**Inventory at review opening:** 244 eligible magical/numeric designs; 218 required signs (217 root signs + one numeric 1); 26 provisional surplus. There are 22 individually short-leashed designs plus two unresolved pairs representing four more distinct eligible designs. These numbers are planning counts, not proof of final root-to-glyph assignments.

**Important:** 26 surplus happen to equal the 26 distinct leashed designs. Automatically removing all leashed designs would leave exactly 218 and no replacement pool; do not infer that the leash should be entirely discarded. Proposed outcomes are `KEEP` (suitable main set), `SPARE` (eligible reserve for future rune changes), `EXCLUDE` (unacceptably confusable). These are advisory statuses pending direct user choice. Review is prioritizing small-size readability, lookalike collisions and Latin/punctuation resemblance.

**Four first-round sheets**, saved on experimental branch only, generated from exact existing SVG paths (with both large and small-size visual previews):

1. `short_leash_review_comparison_01_2026_11_20.svg` — **R060** (leashed) vs **R003**, nearly identical staff/loop plus R060 interior dot.
2. `short_leash_review_comparison_02_2026_11_20.svg` — **R098** (leashed) vs **A007**, **A005**. Open V / top bar difference; ordinary Latin V similarity.
3. `short_leash_review_comparison_03_2026_11_20.svg` — **R058** (leashed) vs **R033**, **R066**. Left vertical with rightward branches, differing curls and counts.
4. `short_leash_review_comparison_04_2026_11_20.svg` — **A028** (leashed) vs **A025**, **A026**, **A024**. Related enclosed loops with upper/lower appendages, with A028 inner detail.

No change to eligibility, watchlists, canonical glyphs, root assignment, punctuation or font. Wait for user's decisions before recording a short-leash disposition or continuing the next batch. **Do not merge to main.**

## 2026-11-20 — Short-leash Round 1 decisions: R003 excluded, R060/R098/R058/A028 kept

User said: **“Get rid of R003, move the rest to the keep.”**

- **R003 directly EXCLUDED** in the full normalized design selection. Its linked runic second-ink archive source **R115** excluded from eligibility as a paired variant, not double-counted as a separate design.
- **R060, R098, R058, A028** explicitly **KEPT** and **CLEARED FROM SHORT LEASH** after comparisons 1–4. Keep means eligible and provisionally visual-approved, **not** a root or meaning assignment.
- Existing reference glyphs in the pictures (R033, R066, A007, A005, A025, A026, A024) remain unchanged.
- Direct source SVG art and archived assets are preserved; no file deletion or canonical font/root change.
- Authoritative `potential_overlap_groups.json` updated: `final_inventory_decisions`, linked variant archive exclusions, count summary, current eligibility, remaining watchlist, and `SHORT_LEASH_2026_11_20_ROUND_01_DECISIONS` review.
- Source sample manifests 03, 05, 08, 11 synced with current selection status; old watchlist reasons retained as history, with resolution marked as kept.

**Inventory:** 337 prototypes → 91 directly excluded, 3 punctuation-reserved, **243 magical/numeric-eligible designs**. Need **218 signs** (217 roots plus one numeric), leaving **25 provisional spare glyphs**. Archived source records: **327 not excluded** overall, **322 magic-eligible** after punctuation reservations, accounting for R115 alternate variant.

**Short leash remaining:** **18 individual glyph IDs** and **2 unresolved pairs** (4 distinct glyphs), **20 watchlist records representing 22 eligible glyphs**. The user has not chosen any spare-only status yet; this review moved all four directly to keep, not to spares.

No merge to `main`. Proceed with the remaining short-leash comparisons on user's next instruction.

## 2026-11-20 — short-leash comparisons 5–8 prepared for user decision

Four comparisons continued the short-leash review **after** the direct decision to exclude R003 and keep/clear R060, R098, R058, A028.

| Comparison | Flagged glyph | Exact original source comparison | Principal concern |
|---|---|---|---|
| 5 | G026 | G025 | Near mirrors, slightly differing curves |
| 6 | G114 | G113, G123, G124 | G114/G113 exact mirror pair, while G123/G124 have related shapes |
| 7 | G115 | G116, G125 | G115/G116 exact mirror pair; G125 is a weaker related reference |
| 8 | G008 | G007 | G008/G007 exact horizontal mirror pair |

Four source-derived SVG comparison sheets were created on `glyphs/idylwild-style-sample-01` at `stylized/analysis/short_leash_review_comparison_05_2026_11_20.svg` through `short_leash_review_comparison_08_2026_11_20.svg`. No underlying glyph geometry was edited. Renderings show large and small-size samples.

**Status: awaiting the user's decisions.** Do not infer exclusion, keep, or spare for these four leashed candidates. Inventory stays at **243 eligible magical/numeric designs**, **218 required**, **25 provisional surplus**, **91 directly excluded**, **18 single-glyph short-leash cases and 2 unresolved pairs**. No merge to `main`.

## 2026-11-20 — Short-leash Round 2 decisions; comparisons 9–12 pending

**Direct user decision:** “Get rid of G026 and G008. Keep the rest. Next.”

- **G026** (near-mirror of G025) and **G008** (exact horizontal mirror of G007): EXCLUDED from final candidate inventory, while source and historical artwork remains on the branch.
- **G114** (mirror of G113) and **G115** (mirror of G116): expressly KEPT / cleared from short leash; not final meaning/root assignments.
- G025, G007, G113, G123, G124, G116 and G125 continue in candidate inventory, no automatic exclusion.
- G026 and G008 are **G-series canonical/recovery designs** so selection ledger retains `canonical_replacement_required=true`; this does **not** edit original source geometry or glyph bindings.

Inventory verified in `potential_overlap_groups.json`:
- **241 eligible** magical/numeric glyph designs, **218 required** = **23 provisional spares**.
- **93 excluded** normalized designs (includes above two), **3 reserved punctuation**.
- **14 individual short-leash entries and 2 unresolved pairs**, 16 watchlist records spanning 18 designs.

**New comparison sheets 9–12 prepared and awaiting user choice**, all drawn from original SVG geometry, no canonical art changes:

| Comparison | Leashed glyph(s) | Reference(s) | Reason |
|---|---|---|---|
| 9 | G012 | G011 **already excluded** | Exact mirror of excluded G011, inspect whether G012 should be retained individually |
| 10 | G016 | G015 (still eligible) | Exact mirror of arced + diagonal crossing glyph |
| 11 | G040 | G039 (still eligible) | Mirrored double-arc glyphs |
| 12 | G085/G086 unresolved pair | G081, G088 (eligible) | G085 and G086 are exact mirrors, one-of-pair choice previously deferred; references help judge distinction from rest |

Four GitHub SVG comparison sheets created under `assets/glyphs/references/idylwild/stylized/analysis/short_leash_review_comparison_09_2026_11_20.svg` through `...12_2026_11_20.svg`.

Do not infer decisions from merely showing comparisons. Do not merge into `main`.

## 2026-11-20 — Short-leash Round 3: G040 and G085 excluded; others kept

**Direct user decision:** “Get rid of G040, G085. Keep the rest.”

- `G040`: EXCLUDED from eligible magic glyph pool. `G039` kept.
- `G085`: EXCLUDED. `G086` kept, resolving the previously unresolved **G085/G086** pair.
- `G012` and `G016`: KEPT, short-leash flags cleared.
- Reference designs `G015`, `G039`, `G081`, and `G088` shown in comparisons 9–12 also kept as eligible.
- Previously excluded `G011` stays excluded, not resurrected by “keep the rest.”
- Original Cuspell SVGs remain preserved. G-series excluded designs are marked as requiring later canonical glyph replacement/coverage reconciliation; no actual glyph/root/font edits.

Updated authority: `stylized/analysis/potential_overlap_groups.json` includes `SHORT_LEASH_2026_11_20_ROUND_03_DECISIONS`, group status updates (57, 59, 64, 80), removed watchlist items, and counts. **No merge to `main`.**

**Inventory:** 239 magical/numeric-eligible normalized designs (218 required, **21 potential spares**), 95 excluded designs, 3 reserved for punctuation. Remaining short leash **11 individual glyphs plus 1 unresolved pair** (`G089/G090`), or 12 leash records covering 13 designs. These are part of the 239 eligible designs.

## 2026-11-20 — Short-leash comparisons 13–16 awaiting decision

Next four comparison sheets assembled from current candidate ledger and the saved SVG source geometry; **no decisions were inferred from the user's “next” instruction**.

| Comparison | Flagged candidates | Comparison glyphs | Reason |
|---|---|---|---|
| 13 | `G089/G090` unresolved pair | `G086`, `G088` eligible references | G089/G090 are mirror forms of a pointed/leaf-like shape across one horizontal bar; whether both are necessary is unresolved |
| 14 | `A009` | `A043`, `A044` explicitly kept earlier | A009 shares the tall oval with central stem/crossbar family but has extra internal ticks |
| 15 | `A012`, `A013` | ordinary reader punctuation `(` and `)` | A012/A013 are doubled parenthesis-like curves, which may be confusing in player-facing text |
| 16 | `R012` | `G041`, `A019`, `R036` still eligible | R012 resembles a bare crossing X (G041); A019 and R036 share the hourglass/crossing silhouette |

Authoritative exact-source SVG sheets saved under `assets/glyphs/references/idylwild/stylized/analysis/short_leash_review_comparison_13_2026_11_20.svg` through `...16_2026_11_20.svg` on `glyphs/idylwild-style-sample-01`. Local PNG renderings use the same source path geometry, with subpixel rounding on long polyline paths in G089/G090, and a separate same-stroke visual drawing of ordinary punctuation. No canonical glyphs or fonts were modified.

**Still 239 eligible glyph designs, 95 excluded, three punctuation reserves; 218 required, 21 potential spares. Short leash: 11 individual IDs and one unresolved pair**. Wait for direct user keep/spare/remove choice before mutating selection status. Do not merge to main.

## 2026-11-20 — Short-leash Round 4 decisions; comparisons 17–20 pending

**Direct user decision:** “Get rid of G090, keep the rest. next set.”

- `G090` EXCLUDED from eligible designs; source geometry stays archived and canonical replacement flag remains for future binding cleanup.
- `G089` KEPT, resolving the final unresolved mirror pair.
- `A009 A012 A013 R012` KEPT and individually CLEARED from the short leash. Their resemblance to parentheses or other symbols is noted, but user decided they are suitable.
- Previously kept comparator glyphs `G086 G088 A043 A044 G041 A019 R036` remain eligible. Reader punctuation `(` and `)` were illustrative only and never glyph candidates.
- Selection ledger includes `SHORT_LEASH_2026_11_20_ROUND_04_DECISIONS`; sample manifests 01, 02, 03, and 05 updated with resolved visual keep statuses. No semantic mapping, canonical glyph art, or font changed.
- Counts checked: **238 eligible normalized magical/numeric glyphs**, **218 required**, **20 provisional spares**, **96 excluded normalized glyph designs**, **3 punctuation reserves**, **7 individual short-leash entries, no unresolved pairs**.

**New comparisons 17–20 prepared**, from exact original source-SVG geometry, shown in both full and small previews and saved as SVGs on the experimental branch:

| Comparison | Flagged glyphs | Reference glyphs | Reason |
| --- | --- | --- | --- |
| 17 | `R023` | `R017 R085 R030` | Similar staff/branch patterns, especially R085 and R017 under transformations |
| 18 | `R050 R082` | `R037 A072` | Both leashed; compare fork/branch outlines and potential crowding |
| 19 | `R084` | `R111 R041 R101` | Cross-stem arms, vertical spine, and diamond/star geometry |
| 20 | `R090` | `R028 A047 R030` | R090 has a curled, zigzag-like stem resembling R028, though extra bars distinguish it |

SVG comparison files: `assets/glyphs/references/idylwild/stylized/analysis/short_leash_review_comparison_17_2026_11_20.svg` through `...20_2026_11_20.svg`. PNGs rendered locally from the same path coordinates. **Await user decision; no actions on these five leashed designs yet.**

No merge to `main`.

## 2026-11-20 — Short-leash Round 5 decisions; final two candidates shown

**User instruction:** “Get rid of R082, R090. keep the rest next.”

- **R082 and R090 EXCLUDED** from normalized glyph pool; their linked second-ink Runic archived variants **R194 and R202** also become ineligible (not separately counted as glyph designs).
- **R023, R050 and R084 KEPT** and cleared from the short leash, preserving original SVG artwork and earlier exclusion/keep records.
- All other eligible glyphs shown for context in comparisons 17–20 were not excluded.
- Authoritative `potential_overlap_groups.json` updated with event `SHORT_LEASH_2026_11_20_ROUND_05_DECISIONS`; relevant source `sample_01, sample_05, sample_07, sample_10, sample_11` manifests synced.

**Current tally:** 337 total normalized designs = 98 excluded + 3 punctuation reserves + **236 magic/numeric-eligible**; 218 signs needed, **18 provisional extra**. Archived source records remain preserved. The only short-leashed candidates now **R108 and A040**; no unresolved pairs.

Two final leash comparison sheets produced from original project SVG geometry, on the experimental branch:

| Comparison | Flagged | Context | Concern |
|---|---|---|---|
| 21 | `R108` | Ordinary mathematical `+` (illustrative, not a Cuspell glyph), surviving `R017`, `A075` | R108 is virtually identical to the common plus sign; smaller R017 looks like a cross with shorter bar and A075 has additional fork at top |
| 22 | `A040` | `R033 R051 A038 A053` (all eligible references) | A040 has three parallel verticals and a bent hooked foot; especially similar to A038's upper section but distinct lower ending |

SVGS saved as `stylized/analysis/short_leash_review_comparison_21_2026_11_20.svg` and `...22_2026_11_20.svg`; source stroke geometry unchanged, ordinary + only a visual reference. **Await user decision before clearing R108/A040.** No merge into `main`.

After clearing the leash, revisit historically unresolved selections, including the pending user decisions from older Groups 17–20 and 37–40, before binding final glyphs to meanings; completion of the leash does not mean all earlier review bookkeeping is settled.

## 2026-11-21 — Short leash closed; remaining pre-assignment audit

**Direct user decision:** “Get rid of R108 and A040. Anything else?”

- **R108** and **A040** excluded; R108's linked alternate-ink Runic archived record **R220** marked ineligible (not an additional normalized glyph design).
- Neither candidate SVG nor any historical source artwork is physically deleted. Related sample manifests 12 and 06 were updated. The short-leash watchlist is now **EMPTY**; both mirror pairs were already resolved in preceding rounds.
- Selection ledger entry: `SHORT_LEASH_2026_11_21_ROUND_06_FINAL_DECISIONS`. No root/meaning assignment, canonical glyph rewrite, font rebuild, or merge to `main`.
- Count reconciliation: **337 distinct normalized designs** = **100 excluded** + **3 reserved punctuation** + **234 magical/numeric-eligible**. Target = **218 signs** (217 root signs + 1 numeric), leaving **16 candidate spares**. Linked archived ink variants are not separate normalized designs; 315 unexcluded original archive records remain.

**Remaining work before final font/semantic binding:**

1. **Small focused audit of unconfirmed visual comparisons**, not another full re-review of all 337 designs. Earlier corrected recheck **Groups 37–39** lack clear comprehensive user keep/remove verdicts; **Group 40's R090 has since been excluded and R028/R030 kept as references, but any other remaining group-40 candidates not explicitly decided must not be auto-approved**. Also, newer recheck **Groups 57–59** were rendered on 2026-11-20 but no explicit group-wide keep was given; Group 60 had only R082 singled out for leash, and R082 was subsequently excluded. Original Oct 29 unchecked Groups 17–20 include some unresolved individual decisions; the old note about R012/R023 on leash is historical and **has been resolved by explicit keeps**. Use current exclusion/keep events to avoid re-presenting already-decided glyphs.
2. **Final post-exclusion similarity/legibility pass** on the up-to-date 234 eligible glyphs, at real writing/font sizes, especially designs similar to punctuation, digits or common Latin marks. The `FULL_SURVIVOR_SIMILARITY_RECHECK_2026_11_13.json` scan is a historical snapshot and not a fresh 234-candidate validation; do not use its stale counts as current.
3. **Map 218 signs to distinct glyphs**, selecting the most readable and distinct, and mark **16 provisional extras** as spare/replacement pool (subject to additional exclusions). Identify replacement handling for excluded G-series canonical glyphs without deleting source provenance.
4. **Build the final player-facing font** with actual root/number mapping and approved punctuation (R105 for `.`, R106 for `:`, A054 for `?`, independently designed `!`), and validate rendering, handwriting, installation and parser text interoperability. The historical combined 449-source font is not the final selection.
5. **Regression tests**: spell examples, signs, printable characters, punctuation, runic meanings, and any changes to generated docs. Only after those should merging back to `main` be proposed, never done implicitly.

No next-phase visual keep/remove decisions are inferred here. This is a bookkeeping and planning checkpoint only.

## 2026-11-21 — Historical Stage-2 Groups 37–40 re-presented; decisions pending

The user asked to continue reviewing **historically unresolved comparison groups** after completion of the entire short leash. Groups **37–40** have now been re-presented as exact original Cuspell/Idylwild SVG geometry, with a second small-size rendering. They are still **PENDING USER KEEP/REMOVE CHOICES**; do not infer approval from the user's “do them next”.

| Group | All pictured designs | Prior decisions preserved | Designs requiring explicit verdict |
|---|---|---|---|
| 37 | `R006 R068 R019 R095` | All eligible; no clear full-group keep in past | `R006 R068 R019 R095` |
| 38 | `R011 R077 R054 R014` | `R077` **EXCLUDED** earlier | `R011 R054 R014`; do not resurrect R077 |
| 39 | `R024 R004 A062 G118` | `R004` provisionally **KEPT** via prior comparison | `R024 A062 G118` (G118 is a weak/structural reference, not a near duplicate); A062 resembles ordinary numeral 4 |
| 40 | `R028 R090 R021 R030` | `R090` **EXCLUDED** in short leash; `R028` and `R030` have prior provisional keeps | `R021`; R028 and R030 can be reconsidered only at user request |

New SVG comparison sheets stored on experimental branch:
- `assets/glyphs/references/idylwild/stylized/analysis/pending_recheck_group_37_2026_11_21.svg`
- `assets/glyphs/references/idylwild/stylized/analysis/pending_recheck_group_38_2026_11_21.svg`
- `assets/glyphs/references/idylwild/stylized/analysis/pending_recheck_group_39_2026_11_21.svg`
- `assets/glyphs/references/idylwild/stylized/analysis/pending_recheck_group_40_2026_11_21.svg`

Locally rendered PNGs `cuspell_pending_group_37.png` through `...40.png` faithfully show the source SVG paths; excluded references R077 and R090 are faded gray only in the review sheets. No original source SVG changed and no new keep/exclusion ledger decision. Current pool **234 eligible, 100 excluded, 3 punctuation reserved, 218 needed, 16 potential spares, short leash empty**.

After user decisions, reconcile corrected Groups 57–60 (`A036 A042 A057 R089` previously shown but not explicitly kept, while `R082` already excluded), and any truly unresolved old IDs without re-showing those now finalized. Continue in batches of four; never merge to main implicitly.

## 2026-11-21 — Historical Groups 37–40 kept; corrected Groups 57–60 reopened

User: **“All are fine keep all that were not excluded. Next.”**

**Recorded direct decision** in `potential_overlap_groups.json` as `HISTORICAL_SURVIVOR_RECHECK_2026_11_21_GROUPS_37_TO_40_KEEP`: all **14 eligible** designs shown in the earlier corrected Stage-2 comparison Groups 37–40 provisionally **KEPT**. Specifically:
- Group 37: `R006 R068 R019 R095` kept.
- Group 38: `R011 R054 R014` kept; previously excluded `R077` remains excluded.
- Group 39: `R024 R004 A062 G118` kept.
- Group 40: `R028 R021 R030` kept; previously excluded `R090` remains excluded.

These group identifiers are from the historical *corrected survivor recheck* and **not** the original numbered overlap groups in `review_groups`. No changes to source SVGs, font, meaning assignment, or counts: **234 magic/numeric eligible, 100 excluded, 3 punctuation reserved, 218 required, 16 spare candidates; short leash empty.**

**Next four newer group sheets 57–60 presented again**, using the source-derived rendered images already created on the experimental branch:
- **57:** `A036` still needs user decision, with `A037 G088` surviving references (double zigzags vs branches).
- **58:** `A042` still needs decision, with `R066 R054 R047` surviving references (angled stems).
- **59:** `A057` still needs decision, with `A058 A055 A060` surviving references (double chevrons vs related forms).
- **60:** `R089` still needs decision, with `R050 R103` surviving references; **R082 was EXCLUDED** in the short-leash round 5 and is shown gray only as a historical reference, and **R050 was KEPT** in that round. The locally rendered Group 60 PNG has updated statuses because the older 2026-11-20 SVG's labels predate those decisions.

**Await explicit user keep/remove choices for `A036 A042 A057 R089`**; no new selections inferred from “next.” Keep all other recorded decisions intact. Then audit any genuinely outstanding earlier decisions only if needed and proceed to the post-exclusion global similarity/legibility pass and 218 sign assignments. No merge to `main`.

## 2026-11-21 — Groups 57–60 kept; next focused decision reconciliation

**Direct user instruction:** “Keep all, A036, A042, A057, and R089. What is next?”

- **Explicit provisional visual keeps:** `A036 A042 A057 R089`, plus all other eligible comparison glyphs in corrected survivor recheck Groups 57–60: `A037 G088 R066 R054 R047 A058 A055 A060 R050 R103`.
- `R082` was already **EXCLUDED**, and is not resurrected by “keep all.”
- Canonical ledger updated with `SURVIVOR_RECHECK_2026_11_21_GROUPS_57_TO_60_ALL_ELIGIBLE_KEPT`; original source manifests for A036 (sample 01), A042 (sample 06), A057 (sample 02), and R089 (sample 11) updated with the user keep. Geometry untouched, no root mapping.
- Inventory unchanged and reconciled: **234 eligible normalized magic/numeric designs, 100 excluded, 3 punctuation-reserved, 218 signs required, 16 possible extras, 0 leash entries**.

**Best next task: finish the truly unresolved positive keep/reject bookkeeping for corrected survivor recheck Groups 29–36 before a new global legibility scan.**

A conservative reconciliation against explicit `final_inventory_suitability_reviews` records finds **14 unique still-eligible IDs** in those eight groups with no explicit positive keep stored (not automatically “bad” or “unreviewed”):
- Group 29: `R078 R073` (R017 and R030 previously kept).
- Group 30: `R067 R064 R061 R040`.
- Group 31: `A016 A032` (A063 already excluded, A025 previously kept).
- Group 32: `A071` (R037, A051 and R050 already kept).
- Group 33: `R053` (R056, A059, A072 already kept).
- Group 34: `A027 A046` (A044 and A043 already kept).
- Group 35: no outstanding IDs among `R084 R111 R041 R086` (already kept).
- Group 36: `A002 A071 A005` (A055 already kept; A071 also appears in Group 32).

The above is a targeted **documented-approval gap list**, not an exhaustive claim about all pending IDs in every older review. Some historical Oct 29 Groups 17–20 also have unspecified individual keeps; do not silently mark them approved. Next batch can show four corrected comparison groups (29–32) at a time with every glyph labeled `KEPT`, `EXCLUDED`, or `NEEDS EXPLICIT VERDICT`, asking for user decisions only on the latter.

After approval gaps are reconciled: run **fresh 234-survivor global similarity/legibility audit** (real output sizes, common-character collisions), choose best **218** for sign/root assignment and mark remaining **16** as spare candidates, then build and validate final font + punctuation + tests. Any further exclusions alter the 16 count. Keep all work on `glyphs/idylwild-style-sample-01`; no implicit merge to main.

## 2026-11-21 — Corrected Groups 29–32 presented for outstanding visual approvals

Presented four real-SVG comparison sheets for **corrected Stage-2 survivor-review groups 29–32**, preserving prior keep/exclusion decisions. This differs from the original `review_groups` numbering in `potential_overlap_groups.json`.

| Group | Unconfirmed eligible candidates | Previously kept comparison candidates | Previously excluded |
|---|---|---|---|
| 29 | `R078 R073` | `R017 R030` | none |
| 30 | `R067 R064 R061 R040` | none | none |
| 31 | `A016 A032` | `A025` | `A063` |
| 32 | `A071` | `R037 A051 R050` | none |

**Correction:** these four groups contain **nine**, not eight, surviving glyphs without an explicit recorded positive keep. The user has **not yet decided** what to keep or exclude here.

Comparison SVGs saved to `assets/glyphs/references/idylwild/stylized/analysis/pending_recheck_group_29_2026_11_21.svg` through `pending_recheck_group_32_2026_11_21.svg`; the corresponding local PNG sheets were faithfully rendered from the original SVG path data in both large and small previews.

**No decision or count changes.** Eligible **234**, required **218**, potential spares **16**, excluded **100**, reserved punctuation **3**, leash empty. Previously excluded A063 remains excluded; all other previous explicit keeps remain. Next ask user to decide on the nine marked REVIEW. Then Groups 33–36 have further approval gaps, followed by any remaining older cases, a fresh global similarity/legibility pass, sign binding and final font build. Do not merge into `main`.

## 2026-11-21 — Corrected Groups 29–32 all kept; Groups 33–36 presented

**Direct user decision:** “All fine, next”. All **nine** previously undecided eligible designs in corrected Stage-2 survivor Groups 29–32 were **provisionally kept**:

- Group 29: `R078 R073`. Previously kept `R017 R030` remain kept.
- Group 30: `R067 R064 R061 R040`.
- Group 31: `A016 A032`. `A025` remains kept; `A063` remains **EXCLUDED**.
- Group 32: `A071`. Previously kept `R037 A051 R050` remain kept.

Canonical ledger entry: `SURVIVOR_RECHECK_2026_11_21_GROUPS_29_TO_32_ALL_ELIGIBLE_KEEP`. The corresponding source manifests (samples 02, 04, 06, 08, 09 and 10) now record visual keep, without root assignment. No source SVG geometry edited.

**Next set corrected Groups 33–36**, all visuals drawn faithfully from saved source SVGs with large and small previews and archived on experimental branch:

| Group | Newly presented for decision | Previously kept |
|---|---|---|
| 33 | `R053` | `R056 A059 A072` |
| 34 | `A027 A046` | `A044 A043` |
| 35 | **None**; fully resolved already | `R084 R111 R041 R086` |
| 36 | `A002 A005` | `A071 A055` |

Five unique designs remain pending user decision in this set. Actual vector sheets archived as `assets/glyphs/references/idylwild/stylized/analysis/pending_recheck_group_33_2026_11_21.svg` through `pending_recheck_group_36_2026_11_21.svg`. The PNG renderings `/mnt/data/cuspell_unresolved_group_33.png` through `...36.png` show the same original path geometry. **No group 33–36 decisions are inferred from “next”.**

Current inventory unchanged: **234 eligible, 100 excluded, three punctuation reserves, zero leash; 218 required and 16 potential surplus designs**. All experimental, not merged into `main`.

After user verdict, reconcile any remaining earlier undecided cases (including some from Oct 29 Groups 17–20 if not superseded by specific direct keeps), then run an updated global lookalike and handwriting readability validation before assigning glyphs to 218 roots/numeric and building final font.

## 2026-11-21 — Close corrected Groups 33–36 and begin final legibility pass

**Direct user instruction:** “keep all next”. Five outstanding candidates accepted in corrected Stage-2 survivor comparison Groups 33–36:
- **33:** `R053` kept; existing `R056 A059 A072` remain kept.
- **34:** `A027 A046` kept; existing `A044 A043` remain kept.
- **35:** no decision outstanding; prior visual keeps `R084 R111 R041 R086` continue.
- **36:** `A002 A005` kept; prior `A071 A055` remain kept.

Ledger event: `SURVIVOR_RECHECK_2026_11_21_GROUPS_33_TO_36_REMAINING_KEPT`. Source sample manifests for 02, 03, 04 and 07 updated. The originally identified eight unfinished Oct 29 designs (`G068 G146 R001 R006 R008 R011 R024 R028`) have **all subsequently received explicit provisional keeps** in corrected reviews or focused comparisons, and no longer need repeat presentation. Do not confuse old review group numbers with corrected survivor recheck numbers.

**Current inventory:** **234** magic/numeric-eligible designs, **218** required signs, **16** provisional extras, **100** excluded normalized designs, **3** punctuation reserved, **0** short-leash records. Nothing merged into `main`; no original SVGs altered.

**Next phase opened: final cross-collection legibility/differentiation audit, four comparisons at a time.** The first four are backed by source-vector comparison sheets `final_legibility_comparison_01_2026_11_21.svg`–`04_2026_11_21.svg`, and locally rendered large/small PNGs. All currently eligible sources shown retain their keep status until explicitly changed:
1. `R031 R083` (+ `A059` reference), score **0.943** under vertical flip in the prior scan; R031 upward fork vs R083 downward fork. They are distinct by direction, potentially confused when rotated.
2. `G092 G105`, score **0.924** under vertical flip; loop attached above vs below.
3. `R030 R076 R017` (+ excluded reference `R108`), historical score **0.923** for R030/R076; R030 straight staff vs R076 dotted lower staff vs R017 small crossbar. R076 is a MAGIC candidate (not punctuation), per explicit prior user decision. Do not change typography semantics.
4. `A043 A044 A009`, historical score **0.916** A043/A044 and **0.890** A009/A044; A043 has half crossbar, A044 full, A009 many additional ticks.

The historical `FULL_SURVIVOR_SIMILARITY_RECHECK_2026_11_13.json` scored 246 survivors before 12 further exclusions. Its top 150 similarities were filtered to current eligibility (138 surviving scored pairs), archived as `FINAL_SURVIVOR_RISK_QUEUE_2026_11_21.json` with source references. This is **not** yet a fresh exhaustive 234-pairwise mask rerun; it is an up-to-date *membership-filtered shortlist* with valid stored pairwise scores. Ensure the distinction is made in user-facing reports. No new selections have yet been made for comparisons 1–4.

## 2026-11-21 — Final legibility comparisons 1–4 kept; mirrored comparisons 5–8 presented

**User:** “All is fine, next.”

**Direct keep:** all 11 currently eligible glyphs in final legibility comparison sheets 01–04: `R031 R083 A059 G092 G105 R030 R076 R017 A043 A044 A009`. Historical excluded reference `R108` remains excluded. Selection-ledger event `FINAL_LEGIBILITY_2026_11_21_COMPARISONS_01_TO_04_KEEP`. No candidate glyph SVG modified or assigned to any semantic root.

Next four high-similarity surviving pairs, all with source SVGs and locally-rendered side-by-side large and miniature PNG previews:

| Comparison | Current candidate IDs | Prior masked similarity | Distinguishing concern |
|---|---|---|---|
| 5 | `G107 G108` | 0.913, mirror | Spiral curl and lower stroke mirrored across vertical axis |
| 6 | `G060 G061` | 0.909, mirror | Double curved leaf-like strokes against left vs right vertical staff |
| 7 | `G109 G110` | 0.906, mirror | Upper and lower curved lines with diagonal crossing, mirrored |
| 8 | `G097 G098` | 0.904, mirror | Curling single-stroke shape reflected left-right |

Authoritative comparison source sheets:
`final_legibility_comparison_05_2026_11_21.svg`,
`final_legibility_comparison_06_2026_11_21.svg`,
`final_legibility_comparison_07_2026_11_21.svg`,
`final_legibility_comparison_08_2026_11_21.svg`
in `assets/glyphs/references/idylwild/stylized/analysis/`. Matching PNGs in conversation `/mnt/data/cuspell_final_legibility_05.png` through `...08.png` generated from the exact source path geometry (G061 is an exact mathematical mirror of G060). Status: **user decisions pending**. Do not infer keep just from prior eligibility. No merge.

Candidate counts remain **234 eligible / 100 excluded / 3 typography reserved**, target **218**, spare candidate pool **16**, no short-leash entries. Historical similarity scores come from the 2026-11-13 full-scan ranking with now excluded items removed. This is **not a newly recomputed 234-design exhaustive pairwise comparison**.

## 2026-11-21 — Final legibility comparisons 5–8 kept, 9–12 presented

**User instruction:** “All is fine, next.”

All eight currently surviving G-designs shown in final legibility Comparisons 5–8 explicitly **kept**: `G107 G108 G060 G061 G109 G110 G097 G098`. They remain separate glyph candidates despite horizontal-mirror relationships. Selection-ledger event: `FINAL_LEGIBILITY_2026_11_21_COMPARISONS_05_TO_08_KEEP`. No semantic/root assignments or source path changes.

**Next four high-priority visual comparisons presented for user review**, using actual original source SVG vectors in the archived comparison sheets, and local PNG previews (source point rounding below 0.5 design-coordinate units, visually negligible):
- **9:** `R041 R086 R111` — diamond outline, central stem, or circular loop; R041/R086 historical score **0.902** under vertical flip.
- **10:** `G015 G016` — mirrored sweeping curves crossed by diagonal, score **0.894** under horizontal mirror.
- **11:** `G037 G066 G038 G067` — upper and lower arch silhouettes with/without a central crossbar. G037/G066 score **0.892** and G038/G067 **0.891** in original orientation.
- **12:** `G021 G022` — mirrored stem-and-leaf, historical score **0.891** under horizontal mirror.

Exact SVG sheets saved in `assets/glyphs/references/idylwild/stylized/analysis/final_legibility_comparison_09_2026_11_21.svg` through `...12_2026_11_21.svg`. PNGs rendered locally to `/mnt/data/cuspell_final_legibility_09.png`–`12.png`. `FINAL_SURVIVOR_RISK_QUEUE_2026_11_21.json` tracks current status, and remains only a **surviving-IDs-filtered rank from the earlier 246-design similarity scan**, not a new 234-design pairwise recomputation. **No keep/remove decision for comparisons 9–12 yet.**

Inventory unchanged: **234 eligible magical/numeric glyphs, 100 excluded, 3 punctuation reserves**, 218 signs required, **16 provisional extras**, 0 short-leash entries. Continue on experimental `glyphs/idylwild-style-sample-01`; never merge without user permission.

## 2026-11-21 — Final legibility comparisons 9–12 kept; next action

**User decision:** “All is fine. What is next?”

- **Kept:** all eleven designs pictured across final legibility comparisons **9–12**: `R041 R086 R111 G015 G016 G037 G066 G038 G067 G021 G022`.
- Event recorded in `potential_overlap_groups.json` as `FINAL_LEGIBILITY_2026_11_21_COMPARISONS_09_TO_12_KEEP`.
- No new exclusions or artwork/meaning changes. Current totals **234 eligible magical/numeric designs**, **100 excluded**, **3 punctuation reserves**, **218 signs required**, **16 possible spares**, **0 leash entries**. No merge to main.
- Queue `FINAL_SURVIVOR_RISK_QUEUE_2026_11_21.json` now marks final-legibility **1–12 all accepted**.

**Next recommended phase:** Finish the remaining highest-priority lookalikes in small batches before semantic glyph assignment, but cap review using a risk threshold rather than displaying every historical pair. The historical surviving top-150 subset has 138 currently eligible scored pairs; excluding the **13 main pairings already explicitly checked** in Comparisons 1–12 leaves **17 scored pairs ≥0.850**, including repeated cross-references from the accepted sheets. New candidate pairings to prioritize are `A073/A075` (0.882), `G129/G130` (0.880), `R040/R064` (0.879), and `G121/G122` (0.875). Distinguish risk-screening suggestions from mandatory deletion; all survivors remain eligible until the user says otherwise.

Historical scores are still valid for pairs with unchanged original geometry, but the top-150 historical list is truncated and no **fresh 234-glyph exhaustive audit** has yet been run. After a bounded similarity/legibility pass, finalize which **218** distinct designs map to canonical signs (217 roots + 1 numeric sign), reserve any extras, build player punctuation/font, and regression-test actual spell text. Never merge `glyphs/idylwild-style-sample-01` without explicit user permission.

## 2026-11-21 — Final legibility comparisons 13–16 presented; awaiting decision

**User instruction:** “Okay, next.”

Final legibility comparison sheets **13–16** prepared from exact original `G` SVGs and stylized `A/R` SVG path geometry, saved on experimental branch `glyphs/idylwild-style-sample-01`:

| Comparison | Surviving glyphs | Historical mask score | Why reviewed |
|---|---|---:|---|
| 13 | `A073 A075` | 0.882 same | Same central cross and fork-like top; A073 has extra lower crossbar and different top |
| 14 | `G129 G130` | 0.880 mirrored | Exact left-right mirror of curling filled shape |
| 15 | `R040 R064` | 0.879 mirrored | Similar staff with top-side hanging branch, but distinct geometry |
| 16 | `G121 G122` | 0.875 mirrored | Exact left-right mirror of upper separated arc and lower curl |

The files are `assets/glyphs/references/idylwild/stylized/analysis/final_legibility_comparison_13_2026_11_21.svg` to `...16_2026_11_21.svg`; locally rendered PNG images `/mnt/data/cuspell_final_legibility_13.png` to `...16.png` preview original geometry at large and small sizes. `FINAL_SURVIVOR_RISK_QUEUE_2026_11_21.json` records **AWAITING_USER_VERDICT** for 13–16. Previous Comparisons 1–12 remain kept, and no decisions are inferred for the new four.

Inventory **unchanged**: 234 eligible, 100 excluded, 3 punctuation reserved, 0 short leash entries, 218 signs required, 16 provisional spare options. No SVG modified, root mapping/typography/font untouched, no merge to main.

## 2026-11-21 — Final legibility 13–16 kept; 17–20 presented

**User:** "All fine, next". All eight surviving glyphs from final legibility comparisons 13–16 were directly kept: `A073 A075 G129 G130 R040 R064 G121 G122`. This is recorded in the ledger as `FINAL_LEGIBILITY_2026_11_21_COMPARISONS_13_TO_16_KEEP`. No exclusions, no source art or root/meaning changes.

**Next four groups (comparisons 17–20) presented for user decisions** using exact original SVG vector paths, also rendered at large and miniature sizes:

| Group | Candidate IDs | Historical 246-survivor scan score | Concern |
|---|---|---|---|
| 17 | `R037 R069` | 0.873 (vertical flip) | Top-fork versus lower fork-like stem; inverted resemblance |
| 18 | `R035 R052` | 0.872 (same) | Almost identical M-shaped staff; R052 has extra lower bar |
| 19 | `G115 G116` | 0.871 (horizontal mirror) | Mirror-symmetric ornate filled forms |
| 20 | `G131 G132` | 0.863 (horizontal mirror) | Mirror-symmetric hollow-filled oval/curl forms |

Saved source-exact sheets in `assets/glyphs/references/idylwild/stylized/analysis/final_legibility_comparison_17_2026_11_21.svg` through `...20_2026_11_21.svg`, and rendered identical local PNG assets `/mnt/data/cuspell_final_legibility_17.png` through `...20.png`. Queue `FINAL_SURVIVOR_RISK_QUEUE_2026_11_21.json` records comparisons 17–20 as `AWAITING_USER_VERDICT`, and 1–16 as kept.

Current totals: **234 eligible magic/numeric glyphs**, **100 excluded**, **3 punctuation-reserved**, **218 sign slots required**, **16 potential spares**, **0 short leash**. This is a filtered historical score ranking; a *fresh full 234-survivor pixel similarity recomputation* remains a separate task. No font rebuilt, no meaning assignments, and no merge to main.

## 2026-11-21 — Final legibility Comparisons 17–20 kept; stage audit-status clarification

**User:** “All. is that all the checks we needed to make?”

**Recorded direct user keep:** `R037 R069 R035 R052 G115 G116 G131 G132` (eight glyphs in final legibility comparisons 17–20). Ledger event: `FINAL_LEGIBILITY_2026_11_21_COMPARISONS_17_TO_20_KEEP`. Therefore **all 20 manually presented final legibility comparisons 1–20** have user approval. No selections or meanings changed; no merge to main.

**Answer: Not all system checks are finished.** Earlier historical survivor mask scan was on 246 candidates. The current count is 234; filtering an old top-150 ranking isn't a fresh exhaustive 234 candidate scan. There are **five** high-similarity pairs (score ≥0.850) in the current eligible historical shortlist not co-presented in Comparisons 1–20: `A066/A067 0.859`, `G071/G080 0.855`, `G119/G120 0.855`, `G113/G114 0.853`, `G123/G124 0.850`. These are remaining *screening flags*, not required removals; user may prefer one last small image batch or the new automated pass first.

**Outstanding essential work before finalizing the font:**
1. Run a **current, exhaustive all-eligible 234-glyph similarity/legibility scan**, including mirror/rotation/small-size checks and inspect only newly significant flags. Spot-check possible Latin, digit, punctuation resemblance.
2. Choose and validate **218** distinct magic/numeric glyph designs for **217 roots plus one number sign**, reserve/label any remaining **16 potential extras** rather than indiscriminately binding all.
3. Implement punctuation: R105 period, R106 colon, A054 question mark, separately drafted exclamation (R076 remains magic candidate). Verify legibility at usable text size.
4. Rebuild/install-test actual player font and spell/parser/test corpus; preserve original asset SVGs and leave all work on experimental branch until user approves merge.

**Inventory unchanged:** 337 normalized designs = 100 excluded + 3 typography-reserved + 234 eligible; short leash zero. Manual visual approvals do not constitute an exhaustive complete runtime font audit. The status in `FINAL_SURVIVOR_RISK_QUEUE_2026_11_21.json` now marks first twenty as kept and documents all five remaining top-score unshown pairs.

## 2026-11-21 — Last five high-scoring historical lookalikes presented (Comparisons 21–25)

**User request:** “Okay, next.”

The next five surviving highly similar glyph pairs (threshold `score >= 0.850` in the older source-accurate 246-design scan, filtered to current eligible pool) have been checked against live exclusion and punctuation records and **presented with original source SVG geometry**:

| Comparison | Glyphs | Similarity | Principal difference |
|---|---|---:|---|
| 21 | `A066 A067` | 0.859 same | Similar forked staffs; upper extension and lower bar variation |
| 22 | `G071 G080` | 0.855 vertical flip | Cup/inverted cup forms, inner branch at opposite ends |
| 23 | `G119 G120` | 0.855 horizontal mirror | Left/right mirrored curl with separate lower arch |
| 24 | `G113 G114` | 0.853 horizontal mirror | Mirrored filled upper curl and diagonal lower slash |
| 25 | `G123 G124` | 0.850 horizontal mirror | Mirrored filled broad curled form |

Source-accurate sheets saved as `assets/glyphs/references/idylwild/stylized/analysis/final_legibility_comparison_21_2026_11_21.svg` through `...25_2026_11_21.svg`; local PNG preview images `/mnt/data/cuspell_final_legibility_21.png` through `...25.png` rendered at both large and small sizes. The current image previews use original stroke and filled path coordinates (G designs original, A designs stylized).

`FINAL_SURVIVOR_RISK_QUEUE_2026_11_21.json` records all five as **AWAITING_USER_VERDICT**. **No new keep/exclusion decision recorded**, source geometry unchanged, no semantic glyph assignments. These were the *last five unpresented pairs* in the surviving historical high-risk shortlist at threshold 0.850, **not proof that no newly risky cases exist**; a fresh current all-234 candidate scan and actual-font small-size stress test are still to be completed.

Inventories remain **234 eligible**, **100 excluded**, **3 punctuation-reserved**, **218 required signs**, **16 potential spare designs**, **0 leash entries**. No merge to `main`.

## 2026-11-21 — Historical 25-comparison shortlist closed; corrected full 234 scan

**Direct user instruction:** “All fine, next.”

All ten remaining candidates in historical final-legibility comparison sheets **21–25** were explicitly **kept**:
`A066 A067 G071 G080 G119 G120 G113 G114 G123 G124`.
Ledger event `FINAL_LEGIBILITY_2026_11_21_COMPARISONS_21_TO_25_KEEP` marks this direct visual approval. All **25 original high-risk comparison sheets** have now been accepted. No new exclusions; inventory stays **234 eligible, 100 excluded, 3 typography-reserved**, with **218 sign slots required / 16 potential spares / zero leash entries**.

### Fresh 234-source exhaustive similarity audit: COMPLETED

- Snapshot assembled from the **140 currently eligible normalized Runic/Alchemical stylized source SVGs** plus the **94 currently eligible original G SVGs** from `assets/glyphs/recovery/source_geometry.json`, all on `glyphs/idylwild-style-sample-01`.
- Cached exact A/R source paths and SVG content: `assets/glyphs/references/idylwild/stylized/analysis/FRESH_SURVIVOR_A_R_SOURCE_SNAPSHOT_2026_11_21.json`. Original geometry remains untouched.
- Compared **all 27,261 distinct unordered pairs** of the 234 candidates using 60x100 rasterized source geometry (with even-odd filled paths, stroked paths, circles and near-black source strokes), Dice similarity under identity/horizontal/vertical/180° transformations. Also computed a 24x40 downsampled same-orientation readability-screening ranking.
- First trial had six empty masks for near-black (#080b0e) R102/R103/R104/R110/R111/R112. Corrected renderer to accept those strokes and source `<circle>` details and reran. Final audit **234/234 masks nonempty** and complete.
- Report: `assets/glyphs/references/idylwild/stylized/analysis/FRESH_ALL_234_SURVIVOR_SIMILARITY_AUDIT_2026_11_21.json` **v2**, with method, coverage and ranked pairs.
- With threshold **Dice ≥0.850** over orientation transformations, **30 scored pairs** were flagged. **27 pairs had already appeared together** in one of the 25 accepted comparison sheets; **three additional pairs** were flagged. All three are *mathematically exact horizontal mirrors* in source geometry, scoring 1.000 **after flipping**:
  1. `G111 G112`
  2. `G117 G118`
  3. `G127 G128`
- **No newly unreviewed non-mirror pair** crossed this threshold in the corrected exhaustive audit. Exact mirror pair does **not** mean identical when upright; remember other prior mirror pairs were deliberately kept as distinct.
- Next: these three source-derived pairs are displayed in `fresh_scan_flag_comparison_26_2026_11_21.svg`, `...27_2026_11_21.svg` and `...28_2026_11_21.svg`, with actual-size mini previews. **Await user's keep/exclude judgment** before marking them approved. Existing eligibility does not itself represent a new direct approval of the final scan.
- Remaining *non-selection validation*: actual font-size legibility, user glyph-to-217-root-plus-number-sign mappings, punctuation R105 '.' / R106 ':' / A054 '?' / separately drafted '!', font build and parser/spell corpus regression. Do not automatically exclude flagged forms. Do not merge the experimental branch to `main`.

