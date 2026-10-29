> **LATEST 2026-10-29 FULL PUNCTUATION COLLISION AUDIT:** All **252 magic-eligible normalized glyph designs** have been scanned against **13 player-facing punctuation SVG drafts**. New report: `stylized/analysis/PUNCTUATION_COLLISION_FULL_SCAN_2026_10_29.md`. Priority visual collisions for user decisions: `$`↔**G054** (G055 already excluded), `(`/`)`↔**A012/A013**, `?`↔**R099** (also G102/G092), `!`↔**R030/R076** at small sizes. These are **flags only**, not exclusions. Scores are approximate; user visual review comes first. Previous counts remain 252 magic-eligible, 82 excluded, 3 source glyphs reserved for punctuation. Begin by showing four source-rendered collision groups, not by revisiting historical similarity keeps.

> **OPEN ISSUE (2026-10-29):** User questioned if all 13 punctuation prototypes are needed, especially brackets, and flagged a magic glyph that resembles the proposed `$` marker. No decisions to remove punctuation or any magic glyph have been made. Square brackets are already historical-only, parentheses are optional grouping fallback, curly braces/comma remain for literal Collections; full audit is in `stylized/analysis/PUNCTUATION_SYMBOL_SIDEBAR_AUDIT.md`. Before font finalization, review both punctuation necessity and **punctuation-vs-magic visual collisions**, particularly `$` and candidate resemblances. Counts remain unchanged.

> **UPDATE 2026-10-29 (newest decisions, superseding the historical narrative below)**: R076 is kept as a magic candidate (no longer provisional !). All 12 designs in suitability groups 2–4 were retained as candidates (R098 short leash still pending). A new independent Cuspell-style `!` and **13 player-facing punctuation SVG drafts** are in `stylized/typography/player_facing/`. See `stylized/analysis/STAGE2_DECISIONS_SUITABILITY_GROUPS01_04_AND_PUNCTUATION.md` and the Stage 2 JSON ledger. Candidate count remains **252 magic-eligible vs 218 needed**, **3 source designs already reserved for punctuation**. Await visual review of punctuation, then continue suitability. No final font/parser/rebinding/main merge yet.

# Cuspell — current new-thread handoff: Stage 2 symbol suitability & punctuation

**Checkpoint:** 2026-10-25, after user chose punctuation candidates, excluded R070 and R107, and requested a handoff.
**Repository:** `MartinApostolov/Cuspell`  
**Only working branch:** `glyphs/idylwild-style-sample-01` — **NOT `main`**  
**Draft PR:** https://github.com/MartinApostolov/Cuspell/pull/124  
**Current focus:** Stage 2 visual candidate selection, specifically **symbol suitability (punctuation, letters, numerals, mathematical symbols, and overly simple marks)**, rather than automatically continuing mirror-pair comparisons.  
**This document supersedes the historical Batch 14 and pre-stylization handoffs.** Always read the current branch tip.

## 1. What the user wants to do next

The user suggested: instead of continuing near-duplicate mirror reviews, **look for designs that should not be in the magic glyph pool at all**. They noticed a glyph that was just a dot and another resembling `?`. Their preferred solution is to keep useful such designs in a **separate punctuation/font sidebar**, rather than consuming slots among the magic symbols.

**In the next thread:**
1. Read this handoff and the active Stage 2 selection ledger before doing anything else.
2. Continue the **symbol suitability audit** of all remaining candidate designs. Flag apparent ordinary punctuation, letters, digits, mathematical signs, indistinct single-strokes, or glyphs inappropriate for a randomized magic-root alphabet.
3. Show the user **actual pictures**, preferably sets of about four categories/groups per review, with legible IDs, and obtain explicit **KEEP AS MAGIC / MOVE TO TYPOGRAPHY / EXCLUDE / SHORT LEASH** decisions. Render the **existing source SVGs exactly**, not AI-redrawn interpretations.
4. **Do not automatically exclude or move** plausible lookalikes merely because they resemble familiar symbols. A number of designs were explicitly kept in prior reviews.
5. Only after the user approves additional changes should you record them in the Stage 2 ledger and an accompanying decision document on the working branch.

The user often cannot see linked comparison sheets unless the image is **embedded directly in the chat**, so use an inline markdown image `![...](sandbox:/mnt/data/...) ` plus a full-size link. Prior groups were shown in **four-group batches**. Don't run a new batch or overwrite existing decisions merely to prepare this handoff.

## 2. Project design constraints

- Cuspell is a magical language/spell system. Characters in the world **draw runes in the air**; the player does **not** need to hand-trace each glyph with mouse/controller. Optimize distinctiveness, recognizability at small sizes, and coherent appearance.
- The Cuspell dictionary currently registers **217 base roots**. There is **one special sign for numeric 1** (current transliteration `@`), so the glyph inventory needs **at least 218 genuinely distinguishable magic/numeric signs**, not counting punctuation.
- Glyph-to-root meanings are **randomized between game runs**. Do **not** permanently assign roots to particular glyph drawings during this review.
- Canonical current source-of-truth remains **150 original `G001–G150`**, `assets/glyphs/recovery/source_geometry.json`. Rejected/candidate replacements are review decisions **only**: original SVGs, historical data, existing font, parser, and root bindings remain unchanged.
- Source collections: 150 Cuspell original G designs; 224 Idylwild Runic source IDs; 75 Idylwild Alchemical source IDs. **449 archived source glyph records** are not 449 distinct designs. The Runic codex has 112 pairs of alternate-ink sources `R001..R112` ↔ `R113..R224` (offset 112). The pre-selection **normalized design pool = 337** (150 G + 112 R + 75 A).
- All external R/A SVGs have been stylistically adapted in 19 batches on the experimental branch. Source ZIP archives are CC0 and must stay byte-for-byte intact.

## 3. Exact latest selection numbers — verified from active ledger

After **116 comparison groups** and the punctuation suitability decisions:

| Measure | Current count |
| --- | ---: |
| Original normalized designs before selection | **337** |
| Directly excluded normalized designs | **82** (48 Cuspell G + 34 Runic/Alchemical) |
| Additionally excluded linked Runic alternate-ink archival IDs | **26** |
| Archived source records excluded | **108 of 449** |
| Archived source records not excluded | **341** |
| Normalized designs not directly excluded | **255** |
| Approved for typography instead of magic roots | **3 normalized designs** |
| **Currently eligible magic/numeric glyph candidates** | **252** = **102 G + 84 R + 66 A** |
| Minimum genuinely distinct root/numeric signs needed | **218** |
| Headroom above minimum *before visual uniqueness proof* | **34** |

Note especially: **255** includes three approved punctuation designs. It is **252** candidates for the 218 root/number-sign slots. An apparent 34-design buffer **does not** establish that 252 signs are visually unique. The provisional exclamation design R076 **is still counted** in 252 until user decides to repurpose it.

**Current watchlist:** 12 individual IDs — `R060, R098, R058, A028, G026, G114, G115, G008, G012, G016, G040, A009`.  
Four unresolved pair choices — `G046/G047`, `G081/G082`, `G085/G086`, `G089/G090`.  
The old `G095/G096` watch pair was removed by user: **G095 excluded**, G096 still eligible/undecided.

## 4. User-approved punctuation, tentative exclamation, exclusions

These decisions **are already saved to the ledger**; do not ask the user to decide them again:

| Source design | Typographic mark | Decision | Source variant |
| --- | --- | --- | --- |
| **R105** | `.` | **Approved punctuation**, NOT a magic-root candidate | R217 reserved alongside R105 |
| **R106** | `:` | **Approved punctuation**, NOT a magic-root candidate | R218 reserved alongside R106 |
| **A054** | `?` | **Approved punctuation**, NOT a magic-root candidate | — |
| **R076** | `!` | **Provisional ONLY** if no better design emerges; still root-eligible until confirmed | R188, not yet reserved |
| **R070** | — | **Excluded**, not reserved for punctuation | R182 also excluded |
| **R107** | — | **Excluded**, not reserved for punctuation | R219 also excluded |

If R076 is adopted, **modify/reflow for punctuation**: current source shape has a dot **above** the vertical stroke, unlike the conventional `!` whose dot is below the stem. User said use R076 for `!` only *if a better option is not found*. Keep the current source file intact and make a punctuation-specific derivative only when approved.

The separate typographic pool will contain **fixed-function signs**, which do not participate in the game's random semantic glyph assignment. The present approved visual choices are stored as **metadata/proposals for future font mapping**, not as new installed font cmap entries.

## 5. Grammar punctuation audit: what Cuspell actually needs

**Authoritative source:** `docs/CUSPELL_DICTIONARY.md`, sections 7–13 on current working branch.

- Sentence-final `.`, `?`, `!`: assertion, question, command respectively. Their punctuation **costs no mana**.
- `:` introduces a typed binder, e.g. `a:Location`.
- `«` `»`: Old/New Names and quoted Signs, including nesting; **not the same thing as straight double quotes**.
- `$`: binder references, e.g. `$a`.
- `(` `)`: explicit grouping fallback (valid although usually avoided).
- `_`: skip an optional positional argument.
- `{` `}` and `,`: real collection literals, e.g. `{This,Self,You}`.
- `@`: the special **numeric 1 sign**, repeating for small numbers: `@@` means 2, `@@@` means 3. This **still counts toward the 218** and must not be quietly downgraded to free punctuation.
- Spaces separate words/phrases; no glyph needed.
- Historical hard-binding `|` is **debug-only**, not new player-facing Cuspell. Historical `[a:...]` brackets are compatibility-only. Semicolon, hyphen, em dash and ellipsis are **not required** by the current core grammar; the font might optionally support them for non-core writing.

Do not invent new punctuation requirements or conflate ordinary font glyphs with mandatory parser grammar. No parser change was requested in this thread.

## 6. Other recognizable marks worth showing for user selection (no decisions yet)

The first source-grounded proposal-only scan found:
- **R030**: one full-height vertical stroke (resembles `|` or `I`); likely too simple for magic, but **not excluded**.
- **R108**: plain `+` cross; user **explicitly kept it** in Group 107. Treat that retention as valid unless the user reconsiders.
- **R009**: looks like mathematical `<`; **not excluded**.
- **A018**: resembles `∞`; **not excluded**.
- **A039**: resembles Greek `Ω` with added bars; **not excluded**.
- **A062**: resembles digit `4` with a lower crossbar; **not excluded**.
- **R076**: question about possible reuse as punctuation `!` remains open.
- Other designs throughout all G/R/A families should be checked systematically, rather than limiting the pass to these examples.

Remember other earlier keeps: Groups 105–112 retained all shown except A009 put on short leash; Groups 113–116 were **"keep for now"**; explicit pairwise `R014` and `R015` both kept. Distinguish **provisional keeps** from exclusions and from final canon adoption.

## 7. Canonical file pointers — read these, not outdated handoffs

**Stage 2 selection ledger (authoritative decisions/counters, working branch):**  
`assets/glyphs/references/idylwild/stylized/analysis/potential_overlap_groups.json`

**Punctuation suitability and user decisions:**  
`assets/glyphs/references/idylwild/stylized/analysis/PUNCTUATION_SYMBOL_SIDEBAR_AUDIT.md`

**Stage 2 user-decision journal:**  
`assets/glyphs/references/idylwild/stylized/analysis/STAGE2_DECISIONS_GROUPS*.md` (documents up through `STAGE2_DECISIONS_GROUPS113_116.md`; additional final exclusions are in the authoritative JSON ledger and punctuation audit).

**Initial automated similarity scan (scores are prompts for human review, not verdicts):**  
`assets/glyphs/references/idylwild/stylized/analysis/stage2_similarity_scan.json`

**Stylized external SVGs (actual art):**  
`assets/glyphs/references/idylwild/stylized/sample_01/svgs/` through `sample_19/svgs/` (source ID ↔ batch location is in each `sample_XX/manifest.json`; manifest schemas vary).

**Original Cuspell SVGs:**  
`assets/glyphs/recovery/generated/glyphs/G001.svg` ... `G150.svg`; registry `assets/glyphs/recovery/source_geometry.json`.

**Original unmodified Idylwild ZIPs:**  
`assets/glyphs/references/idylwild/original/`.

**Existing comparison font:**  
`assets/glyphs/references/idylwild/keyboard_kit/` — **old pixel-based 449-character review font**, not a final font built from new stylized SVGs.

**Dictionary:** `docs/CUSPELL_DICTIONARY.md` (217 registered roots, grammar and punctuation).

## 8. Procedure for continuing without accidental regressions

1. **Fetch active branch ledger and latest handoff first.** Do not start from `main` — Stage 2 is experimental and unmerged. Don't overwrite user exclusions with style-only "KEEP" approvals from early batches.
2. Audit candidate suitability visually from **real existing SVG source paths**, showing the exact glyph ID next to each example. For ambiguous symbols, show full-size and small-size rendering where useful. Use **actual embedded PNG** in chat; merely linking GitHub image/SVG sometimes does not display for user. Avoid `image_gen` because it changes the glyph shapes.
3. Present about four groups at a time; ask user whether to retain as magic, reserve for typography, exclude, or short-leash. **Do not preemptively prune.**
4. Write explicit decisions non-destructively to `potential_overlap_groups.json` (create a separate suitability audit grouping/decision structure if useful) and an accompanying markdown journal. Reserve typography separately: **do not treat as "excluded"/deleted** in the same way as R070/R107. If excluding an R001–R112 prototype, also exclude its variant `R+112` archival ID; likewise link variants when reserved for punctuation. No source file deletions.
5. Recompute separately: **direct normalized exclusions**, linked Runic source exclusions, **typography-reserved** designs, magic-eligible normalized designs, and raw archive records. Keep all existing short-leash decisions unless user explicitly changes them. 
6. When Stage 2 suitability and global similarity reviews are truly finished, decide final pool of >=218 distinct signs, then plan canonical registry/root-safe font rebuild and tests. **Do not begin that irreversible step without user approval.**

**Not done at this checkpoint:** final official glyph inventory, installed new font, punctuation-specific cmap/font glyph designs, new parser syntax, permanent root assignments, merging PR #124 to `main`.

## Ready-to-paste prompt for a new thread

> Continue the Cuspell glyph project from the **latest commit of experimental branch `glyphs/idylwild-style-sample-01`**, draft PR #124 in `MartinApostolov/Cuspell`. Read `assets/glyphs/references/idylwild/HANDOFF_NEXT_THREAD_STAGE2_SUITABILITY.md` and the authoritative Stage 2 ledger `assets/glyphs/references/idylwild/stylized/analysis/potential_overlap_groups.json`, plus the punctuation audit. We finished 116 similarity review groups and are switching to **symbol suitability**: identify remaining shapes too much like punctuation, ordinary letters/digits, math signs, or trivial marks. We have **252 magic-eligible normalized designs** (goal >=218 distinct), three designs reserved for typography (**R105='.', R106=':', A054='?'**), **R076** provisional for `!`, and **R070/R107 plus linked variants excluded**. All original assets must stay intact. Show actual embedded visual sheets about four groups at a time, ask for explicit keep/move/exclude/watchlist decisions, save approved outcomes to the **experimental branch only**, and don't re-open already settled decisions or rebuild the canonical font yet.
