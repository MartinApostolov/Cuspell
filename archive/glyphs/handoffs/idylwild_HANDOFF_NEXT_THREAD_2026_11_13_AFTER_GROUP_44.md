# Cuspell — next thread handoff after similarity Group 44

**As of:** 2026-11-13
**Repository:** [MartinApostolov/Cuspell](https://github.com/MartinApostolov/Cuspell)
**Active experimental branch:** `glyphs/idylwild-style-sample-01`
**PR:** [#124](https://github.com/MartinApostolov/Cuspell/pull/124)
**Do not merge to `main` without the user's explicit instruction.**

## Immediate user decision (recorded)

User said: **"R108 on leash keep the rest. Can you make a hand off file so I can go to a new tread and contiue?"**

- **R108** from comparison Group 41 is now on the **SHORT LEASH**. It remains eligible, not excluded, and retains any earlier suitability history.
- **Other 15 distinct designs in Groups 41–44** were **provisionally kept**: `G068 A075 R017 G146 G044 R056 R039 R001 G062 R004 R088 A052 A058 A072 R111`.
- No exclusion, root assignment, SVG edit, or font change was made by this decision.
- Recorded in `assets/glyphs/references/idylwild/stylized/analysis/potential_overlap_groups.json`, review ID `SURVIVOR_RECHECK_2026_11_13_GROUPS_41_TO_44`.

### Inventory after this decision

- Starting normalized designs: **337** = 150 original Cuspell G, 112 normalized Runic R, 75 normalized Alchemical A.
- Directly excluded normalized designs: **90** (retain original artwork in source/archive).
- Existing glyph designs reserved for punctuation: **3** (`R105` = `.`, `R106` = `:`, `A054` = `?`). The custom `!` is separate; `R076` remains a magical glyph candidate.
- **244 magical/numeric candidate designs remain**, with **218 signs needed** (217 roots + numeric 1); **26 provisional spares**.
- Runic linked second-ink exclusions: **30**, including most recent `R077 → R189`; these archived variants must not be double-counted as independently eligible designs.
- Archive source records and all original SVGs remain preserved; do not delete or redraw anything on user decisions alone.

## Stage and exact next action

**Still doing unchecked/non-leash suitability + whole-pool lookalike review. We are NOT yet clearing the short leash.**

1. Continue with **Groups 45–48**, four side-by-side source-SVG comparison sheets with visible pictures in the chat. Use IDs on each image.
2. Select groups based on the **full-pool similarity screening** and compare against all surviving `G/R/A` glyphs, not numerical adjacency. Consider mirror, vertical flip, rotation, small-font readability, ordinary punctuation/Latin/numeric resemblance.
3. Show the original SVG drawings via CairoSVG/Pillow or other precise vector rendering. Avoid generative reimagination and low-res enlargements. Ask user what to keep, exclude, or leash after showing exactly four groups.
4. Only record exclusions and short-leash entries when explicitly decided. `keep` remains a provisional visual approval, not a final meaning/root assignment.
5. Finish all unchecked glyphs, then go through the **short leash**, and finally audit 218 sign coverage, small-size uniqueness, and player typography.

### Still not presented in corrected Groups 21–44

The full-survivor scan originally identified 55 glyphs absent from earlier comparison/side-review tracking. After checking actual membership in **Groups 21–44**, **29 of those 55** have still not appeared in the corrected visual groups:

```
A008 A010 A011 A015 A017 A020 A021 A029 A030 A031
A033 A034 A035 A036 A040 A041 A042 A050 A057 A074
R036 R042 R043 R057 R066 R082 R089 R097 R100
```

These 29 should be prioritized for subsequent review; 'not in corrected Groups 21–44' does **not** assert they were never seen incidentally in any earlier historical sheet. Their approximate nearest neighbors from the all-pool screening include:
- `R042` ↔ `R051`
- `A010` ↔ `A009` (**A009 already leashed**)
- `A008` ↔ `A065`
- `R036` ↔ `R015`
- `A017` ↔ `A065`
- `A033` ↔ `R014`
- `R043` ↔ `A068`
- `R066` ↔ `R033`
- `R100` ↔ `R094`

Suggested first set **Groups 45–48** (check candidate eligibility before rendering):
- Group 45: `R042 R051 A008 A065` — structural/mirrored similarity; two subclusters may be separated if better pairing is found.
- Group 46: `A010 A009 A044 A021` — rings/seals; keep A009 leashed.
- Group 47: `R036 R015 R052 A033` — angular/crossing marks; verify best match layout.
- Group 48: `A017 A065 R104 A024` — looped symbols; some already provisionally kept.
You may choose **stronger groups based on the source SVGs**. Each group should introduce at least one genuinely not-yet-presented design and show its real closest lookalikes.

### Previously shown, still without explicit keep decision

From the original ID-arranged Groups 17–20, the following still lack an explicit keep decision even though they were later shown alongside neighbors in Groups 37–40:
`R006 R011 R024 R028`.

They remain eligible, **not short-leashed**. The user directly excluded `R077` after its Group 38 comparison with `R011`, so `R011` survived; do not misstate this as a request to leash it.

**Groups 37–40** otherwise remain largely undecided. `R090` is on the leash, `R077` was excluded; no implicit acceptance of the other members.

### Active short leash — do not clear early

**20 individual IDs:**
```
R060 R098 R058 A028 G026 G114 G115 G008 G012 G016
G040 A009 A012 A013 R012 R023 R050 R084 R090 R108
```

**2 unresolved pairs (both members still eligible, no arbitrary choice):**
```
G085/G086   G089/G090
```

Total **22 watchlist records** representing **24 distinct still-eligible designs**. The active selection ledger, not this snapshot, is authoritative for changes.

### Important recent decisions

- Groups 21–24: provisional keep of all 14 shown; **R012** retained its preexisting leash.
- Groups 25–28: all 16 shown provisionally kept.
- Groups 29–32: **A063 excluded**, **R050 leash**; other designs unchanged unless earlier approval exists.
- Groups 33–36: **R084 leash**; others unchanged.
- Groups 37–40: **R090 leash**; **R077 excluded** with linked archive variant **R189**; others unchanged.
- Groups 41–44: **R108 leash**; other 15 provisionally kept.
- Additional earlier exclusions: **R010/R018** (linked archive variants **R122/R130**). Earlier leash: **R012/R023**.
- Group 19 originally showed R011 with R008/R010/R012; original Group 9 included R077. They were *not* both on the leash. R077 has now been excluded.
- No deletion of SVGs, archives, font mappings or parser changes in this suitability stage.

## Source-of-truth files

1. **Selection ledger:** `assets/glyphs/references/idylwild/stylized/analysis/potential_overlap_groups.json` — definitive exclusions, short leash, counts, and approved review records.
2. **Whole-pool similarity machine results:** `assets/glyphs/references/idylwild/stylized/analysis/FULL_SURVIVOR_SIMILARITY_RECHECK_2026_11_13.json` — original 246-eligible screening, 30,135 pairs; **historical snapshot before A063/R077 exclusions**, so filter excluded IDs when using its ranked neighbors.
3. **Similarity method and review chronology:** `assets/glyphs/references/idylwild/stylized/analysis/STAGE2_SURVIVOR_SIMILARITY_RECHECK_2026_11_13.md`.
4. **Running chronological handoff/history:** `assets/glyphs/references/idylwild/HANDOFF_NEXT_THREAD_STAGE2_SUITABILITY.md`.
5. **Original Cuspell G geometry:** `assets/glyphs/recovery/source_geometry.json` (`.glyphs.G###.svg`).
6. **Stylized Runic/Alchemical SVGs and manifests:** `assets/glyphs/references/idylwild/stylized/sample_01/` ... `sample_12/` (paths `svgs/R###.svg`, `svgs/A###.svg`); the full Idylwild source archives remain in the repo.

## Suggested opening instruction for the new chat

> Continue Cuspell glyph suitability review from `glyphs/idylwild-style-sample-01`, PR #124. Read `assets/glyphs/references/idylwild/HANDOFF_NEXT_THREAD_2026_11_13_AFTER_GROUP_44.md` and the current selection ledger. Start with **Groups 45–48** of previously unchecked glyphs and their closest surviving lookalikes. Show four actual SVG-derived comparison pictures in chat. Do **not** clear the short leash yet and do not merge to main. Wait for my keep/remove/leash choices before modifying inventory.
