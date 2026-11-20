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

