# Cuspell — next-thread handoff: Stage 2 glyph similarity review, after Groups 1–12

**Checkpoint date:** 2026-10-24  
**Repository:** `MartinApostolov/Cuspell`  
**WORKING BRANCH — not `main`:** `glyphs/idylwild-style-sample-01`  
**Draft PR:** https://github.com/MartinApostolov/Cuspell/pull/124  
**Last verified branch commit before this handoff:** `6e1e5b11121346843cb2aeedde7c9243a89d7668`. **Fetch the branch head again in the next thread**; the commit adding this handoff will be newer.

## User's current request and preferred workflow

- User asked (1) **how many glyphs are left**, and (2) for **a handoff file for a new thread**. **Do not start Group 13 in the current thread.**
- Next task: continue **Stage 2 — remove designs too alike**, reviewing **FOUR similarity groups at a time**, showing an actual **PNG picture directly inside the chat** (with IDs and large, clearly visible glyphs), then waiting for the user to name exclusions.
- Repeatedly, earlier SVG links, data images, or inline images without backing files **did not display in the user's ChatGPT UI**. **Create/verify a real PNG file under `/mnt/data/` and embed/link its established sandbox path**. Do not invent `sandbox:/mnt/data/...` paths or rely on remotely linked SVG markdown.
- Choices such as "Get rid of R..." mean **exclude from future final active pool**, not permanently delete the original or historical glyph SVG. Record the specific choices on the branch, including +112 Runic counterparts if they reuse the rejected normalized design, but **do not infer that unmentioned glyphs are approved**.
- Never change `main`, original CC0 ZIPs, canonical G001–G150 geometry/meaning assignments, or the current font solely from exclusion decisions.

## Answer: How many glyphs are left?

These are THREE different counts, and they must not be conflated:

| Meaning | Initial | Excluded | Remaining |
| --- | ---: | ---: | ---: |
| **Archived source IDs**: G001–G150 + R001–R224 + A001–A075 | 449 | 30 IDs | **419 source IDs not excluded** |
| **Normalized prototype choices**: 150 G + 112 Runic base designs + 75 Alchemical | 337 | 17 prototypes | **320 candidate designs not excluded** |
| **Genuinely visually distinct, final selected glyphs** | Not determined | Ongoing review | **UNKNOWN** |

How the **320** candidates break down after all current user decisions: **149 Cuspell G** + **99 Runic prototypes** + **72 Alchemical prototypes** = **320**.

Why **419 vs 320**? The 224 Runic records are 112 first/second-ink pairs (R113–R224 index equals earlier ID +112). We standardized corresponding pairs into identical Cuspell-style vector contours. Among the remaining source records there are **99 surviving second-ink Runic variants**, not 99 more distinctive options. Thus `419 - 99 = 320`. Other near-duplicates, mirror pairs and cross-collection overlaps remain and will lower the number of **truly distinct** candidates further.

**Minimum target: at least 218 visually distinct signs** (**217 roots plus one special**). **256 is not an approved target**. There is not yet a selected set of 218 and no guarantee that 320 candidates all count as distinct.

## Stage 1 completion and preserved data

- All **299 external source records** (R001–R224 = 224; A001–A075 = 75) represented once each in 19 batches, validated against on-branch manifests and actual SVG files. Combined with original G001–G150 => 449 **archived source records**, not 449 unique shapes.
- All **19 stylization batches visually approved**, including accepted spacing fixes to A050, A013, R002, A068, R112 and R114. These **style approvals do not adopt candidates into the final pool**.
- All original Idylwild archive art / CC0 attribution and SVG draft histories preserved. Earlier comparison font is for pixel-based comparison and is **not** the final stylized font.
- Existing Cuspell glyphs are not automatically protected from final removal/replacement. **G033 is the first G glyph excluded**, but its canonical SVG and assignment have NOT been changed yet; mark it for later safe font rebuild or replacement.

### Exclusions: Groups 1–12

The user has directly excluded these **17 prototypes** (16 imported candidates, 1 existing Cuspell):

| Review groups | User-rejected prototypes |
| --- | --- |
| **1–4** | R020, R022, R044, R065, R080 |
| **5–8** | A022, R016, A048, A056, R072, R029, R087 |
| **9–12** | R032, R045, R055, R049, **G033** |

The following **13 secondary Runic source records** are also excluded because their normalized SVG contours are copies of rejected Runic prototypes:

| Rejected original | Excluded +112 counterpart |
| --- | --- |
| R020 | R132 |
| R022 | R134 |
| R044 | R156 |
| R065 | R177 |
| R080 | R192 |
| R016 | R128 |
| R072 | R184 |
| R029 | R141 |
| R087 | R199 |
| R032 | R144 |
| R045 | R157 |
| R055 | R167 |
| R049 | R161 |

**Total: 17 direct design exclusions + 13 linked source-variant exclusions = 30 source IDs excluded.** This does **not** mean 30 distinct designs removed. The 13 Runic counterparts were indexed variants of 13 of the rejected originals. The *unmentioned* members of all 12 groups remain undecided.

All removals were recorded in individual batch manifests where the candidates live and in the Stage 2 decision ledger. **Nothing was physically deleted.**

## Key source files to read in the next thread

All paths below are relative to `MartinApostolov/Cuspell`, **on `glyphs/idylwild-style-sample-01`**:

1. **Source of truth for decisions and first 12 groups:**  
   `assets/glyphs/references/idylwild/stylized/analysis/potential_overlap_groups.json`
2. **Decision explanation checkpoints:**  
   `assets/glyphs/references/idylwild/stylized/analysis/STAGE2_DECISIONS_GROUPS01_04.md`  
   `assets/glyphs/references/idylwild/stylized/analysis/STAGE2_DECISIONS_GROUPS05_08.md`  
   `assets/glyphs/references/idylwild/stylized/analysis/STAGE2_DECISIONS_GROUPS09_12.md`
3. **Ranked machine-generated similarity screening:**  
   `assets/glyphs/references/idylwild/stylized/analysis/stage2_similarity_scan.json`
4. **First 12 comparison groups + Cuspell mirror atlas (NOT the complete backlog):**  
   `assets/glyphs/references/idylwild/stylized/analysis/review_close_matches_1.svg`  
   `assets/glyphs/references/idylwild/stylized/analysis/review_close_matches_2.svg`  
   `assets/glyphs/references/idylwild/stylized/analysis/review_cuspell_mirror_pairs.svg`
5. **Cached stylized vector markup for all imported source IDs:**  
   `assets/glyphs/references/idylwild/stylized/analysis/stage2_vectors_batches01_09.json`  
   `assets/glyphs/references/idylwild/stylized/analysis/stage2_vectors_batches10_19.json`  
   (Re-read actual batch SVG files if there is any inconsistency; these are analysis caches.)
6. **Original canonical Cuspell shapes, do not edit without user approval:**  
   `assets/glyphs/recovery/source_geometry.json` and `assets/glyphs/recovery/generated/glyphs/G001.svg` ... `G150.svg`.
7. **Coverage audit and script:**  
   `assets/glyphs/references/idylwild/stylized/STAGE1_COVERAGE_AUDIT_AFTER_BATCH19.md`  
   `assets/glyphs/references/idylwild/stylized/verify_stage1_coverage.py`.
8. **Original borrowed source images and archives:**  
   `assets/glyphs/references/idylwild/reviews/01_runic_vs_alchemical.png`  
   `assets/glyphs/references/idylwild/original/idylwilds_runic_codex.zip`  
   `assets/glyphs/references/idylwild/original/idylwilds_alchemical_codex.zip`.

The 19 manifests use differing candidate-record keys (`samples`, `glyphs`, `decisions`, `candidates`) and selection-field names. New exclusions use `final_inventory_selection: "EXCLUDED"` plus `final_inventory_exclusion`; always consult the central Stage 2 ledger for canonical counts.

## How the similarity scan works — and its limits

- All **449** source IDs included, but the **112 later Runic ink-variants** grouped with corresponding earlier IDs before pair ranking, leaving **337** comparison prototypes.
- For each prototype, SVG strokes rasterized at about **32×56** cells and pairwise overlap scored (Dice) in natural orientation, horizontal reflection, vertical reflection and 180-degree rotation. The first scan ranked strong collisions; its saved `ranked` array is only a **limited high-scoring shortlist**, not a comprehensive final exact-shape proof.
- Group 1–12 reviews were manually prepared from notable matches and **are finished only for named exclusions**. More collisions likely exist, including across G/R/A and within collections.
- There are **64 existing G-vs-G left/right mirror pairs** (128 G source IDs, with overlapping/rotation families). A separate user-facing mirror review is still needed. Rotated quartets `G071/G072/G079/G080` and `G091/G092/G105/G106` merit checking. Do **not** automatically drop all mirrors; the user decides.
- Coarse raster can miss thin dots, crowding, inner gaps and 90-degree relations; comparison groups need human review at readable/small sizes.
- The glyphs are drawn **in the air by in-world characters**, not necessarily written by human players. Prioritize distinctive silhouettes and internal readability over penmanship.

## Next immediate work (new thread)

1. Fetch **latest branch head** and the central decision ledger.
2. Assemble **four NEW** high-priority similarity clusters, tentatively call them **Groups 13–16**. Exclude already-rejected candidates (including +112 source variants), de-duplicate overlapping clusters, and ensure these are still genuinely confusing after visual inspection. Compare **across all three collections**, not just borrowed-vs-borrowed.
3. Generate a **real, legible PNG contact sheet directly viewable in the chat**, with each group and each glyph ID; provide a working sandbox link too. Do not repeat the earlier broken-attachment issue. If needed, render on-container from SVG with PIL/cairosvg and check that the file exists before linking.
4. Briefly propose removals; **wait for user decisions**. Group choices are final-pool exclusions only; preserve original assets and all history. Update manifests and Stage 2 ledger after their choice.
5. Repeat in groups of four; then review existing Cuspell mirrors/rotations in batches and legibility/crowding. Finalize a distinct pool of at least 218, decide replacements for excluded G glyphs, create the final font, and test Cuspell sentences/spells. **Do not assign permanent root↔glyph meanings**: mappings are intended to vary per game run.

## Ready-to-paste prompt

> Continue Cuspell in `MartinApostolov/Cuspell` from the **latest** `glyphs/idylwild-style-sample-01` branch (draft PR #124). Read `assets/glyphs/references/idylwild/HANDOFF_NEXT_THREAD_STAGE2_AFTER_GROUP12.md` and the Stage 2 decision ledger. All 449 source records have been processed; 112 later Runic sources are standardized copies of R001–R112. We have excluded 17 prototype glyph designs (including G033) plus 13 associated Runic variant source records: 419 source IDs still unexcluded, or 320 normalized candidate designs (149 G +99 Runic +72 Alchemical), **not** 320 proven distinct signs. Stage 2 Groups 1–12 already have user exclusion choices recorded. Continue by showing the next **four** strong similarity groups (13–16) **as a real PNG image directly in the chat**, comparing all three collections. Nothing should be removed until I name it; preserve rejected source files and canonical art.
