# Gesture review — Batch 2 approved, Batch 3 proposed (2026-10-22)

User replied **“keep all”** to group 4 G117/G118, group 5 G119/G120 and group 6 G121/G122. Their contemporary path directions are approved and **appended without overwriting Batch 1** to `gesture_review/approved_gestures.json` (now six approved mirrored pairs = 12 glyphs). The original proposal JSON is kept with an acceptance note. The 150 actual glyph shapes and generated fonts remain UNCHANGED; no original historical stroke order has been recovered.

Prepared three next proposed groups, all UNAPPROVED: **7 G123/G124** (three strokes; upper rising diagonal, long descending hook, short inner notch), **8 G125/G126** (two strokes; folded upper bend and detached lower arc), **9 G127/G128** (three strokes; upper rising sweep, two lower arms from shared apex). Preview `gesture_review/BATCH_03_G123_G128.svg`, instructions `gesture_review/BATCH_03_G123_G128.md`, paths `gesture_review/batch03_proposals.json`. User prefers reviewing three groups at a time. Do not call those candidate directions approved before their response.

---

# Gesture Batch 1 approved; Batch 2 proposed (2026-10-22)

User said **"keep all of them"** to 3 groups of proposed modern drawing
instructions: G111/G112, G113/G114 and G115/G116.

- Approved exact step paths are now recorded at
  `gesture_review/approved_gestures.json`, with approval statuses and
  provenance. The original `gesture_review/batch01_proposals.json`
  also records the acceptance. Both contemporary guidance artifacts
  are **not authentic lost v0.19 stroke-order evidence**.
- Original user-approved glyph silhouettes and fonts are unchanged.
  Generated post-G100 gesture guide outlines remain placeholders; do
  not mislabel them as reviewed drawing trajectories.
- Current new unapproved next review contact sheet:
  `gesture_review/BATCH_02_G117_G122.svg`.
  Its source JSON is `gesture_review/batch02_proposals.json`.
  Groups 4–6 are G117/G118, G119/G120, G121/G122.
- Preserve per-group decisions, as the user prefers sets of THREE.
  Do not advance gesture status of Batch 2 without their feedback.

---

# Handwriting/air-writing phase — Batch 1 prepared (2026-10-22)

User agreed to move from the completed 13-group visual audit into
handwriting and gesture-guide design, three independent review groups per
sitting. A prior message delivery timed out; work was resumed in this chat.

**First three proposed gesture groups, AWAITING USER APPROVAL:**
- **Group 1:** G111/G112 — outer looping return + inner descending hook,
  suggested 2 pen strokes.
- **Group 2:** G113/G114 — folded upper gesture + detached lower diagonal,
  suggested 2 pen strokes.
- **Group 3:** G115/G116 — arch joined to underline plus two lower legs
  from the shared apex, suggested 3 pen strokes. The guide starts for legs
  2 and 3 are physically the SAME point; numbering labels are offset only
  to avoid visual overlap.

Review sheet (self-contained SVG): `gesture_review/BATCH_01_G111_G116.svg`.
Written descriptions: `gesture_review/BATCH_01_G111_G116.md`.
Machine-readable path candidates: `gesture_review/batch01_proposals.json`.
User-facing copy of SVG rendered as a PNG in the associated chat.

**IMPORTANT:** None of these directions have been approved; original G111–116
SVG silhouettes, glyph source, fonts and placeholder guides are UNCHANGED.
Colored suggested centerlines are not reconstructed original pen motion.
The former original later gesture guides were lost. Mirrored partners
reflect proposal directions without changing appearance.

Next step: ask user to KEEP / ADJUST / REPLACE each of the three groups,
then commit only accepted gesture GUIDE records and preserve drafts.
Continue subsequent batches after review.

---

# Audit complete — groups 11–13 decisions and rebuild (2026-10-22)

User decisions: **11 narrower, 12 keep, 13 keep.** Both **G068 and G070
were narrowed by 15% horizontally** around x=300, preserving the height
and 66-unit stroke weight. These SVG coordinate edits are now canonical
in `source_geometry.json` (and compiled into the TTF/WOFF2 fonts).
G070 retains the approved single continuous lower cross-line (4
separate paths). The previous G068 v0.13 and the prior G070 4-stroke
versions are preserved, with exact before/after geometry and visual
comparison, in `drafts/G068_G070_2026-10-22_narrower/`. G070's
original 5-path historical art is preserved in the earlier draft folder.

**Group 12:** G060/G061 vs G068/G070 bud-family resemblance accepted
without further changes. **Group 13:** dense screenshot-derived
G113/G114, G125/G126, G129/G130 visually acceptable at 16px, kept
unchanged. Genuine post-G100 gesture ordering is still unavailable.

**All 13 visual audit review groups have explicit user decisions.**
Recovery rebuild passed GitHub Actions 2026-10-22. Rebuilt state:
150 active SVGs, 150 private-use mappings, 0 missing font glyphs,
0 flagged mirror errors, **0 edge-clipping warnings** (previously 2),
66-unit consistent nominal strokes. There remain 20 numerically
similar comparisons, all covered by the user's reviews; these are not
errors requiring redesign.

**Current source provenance:** 82 original v0.13 glyph SVGs unchanged,
16 original v0.14 R1 glyph SVGs unchanged, 22 screenshots/traces
(2 tentative screenshot-to-ID assignments), 14 approved newly designed
or modified SVGs, and 16 other approximation-based reconstructed SVGs.
All 100 historic early SVG sources remain in project backups/evidence.
Historic gesture guides for revised G068/G070 do not apply to current
art; generated guides for them are outline placeholders, as are those
for G101–G150.

The glyph recovery branch is still separate from `main`. Next optional
work can be a **hand/air-writing usability session** and genuine stroke
guide design, with batches of 3 groups as user prefers; do not
invent original lost vectors or historical gesture orders. A release
merge should be a separate explicitly approved decision.

---

# Audit review — groups 8, 9 and 10 accepted (October 20, 2026)

User said **"all fine, next"** to three groups: (8) G111/G112 versus
G131/G132, (9) G066/G067 versus G079/G080, and (10) the G115/G116
silhouette pair. **No art changes** were made for these groups. The
screenshot-to-ID assignment for G131/G132 remains tentative and authentic
post-G100 stroke-order guides are still missing; visual acceptance is not
proof of historically correct hand gestures.

All 20 machine-flagged cross-glyph pair comparisons are now in reviewed
groups 1–9 (accepted geometry preserved). The next three-group quality
review is: **11** edge-margin G068/G070 (show optional horizontal-inset
draft only), **12** bud family G060/G061 versus G068/G070, and **13**
screenshot-traced complex glyphs G113/G114, G125/G126, G129/G130 at
true 16px size. These are distinct checks for layout, family
consistency, and readability/hand-drawing, not further duplicates of
completed similarity work. Do not edit sources until user acceptance.
Audit queue includes the recorded decisions.

---

# Audit update — groups 4, 6 and 7 decided (2026-10-20)

User responded **"all fine, next"** after reviewing proposed G070 one-piece
lower line, the G025/G026 vs G073/G074 comparison, and G031/G032 vs G054/G055.

- **G070:** promoted the shown revision from draft to canonical. Upper buds,
  central stem unchanged; two lower side strokes replaced with one inset
  continuous lower cross-line. Four path-starts now, down from five. Marked
  as APPROVED_NEW_VECTOR (modification of original authentic v0.13); the
  exact original historical G070 remains archived in the draft folder. Its
  old G070 gesture order cannot be used as a guide for the new four-stroke
  shape. The recovered font and audit are regenerated by CI.
- **G068:** shown unchanged in same group; user said all fine. Margin issue
  remains technically flagged but accepted provisionally with no edit.
- **Groups 6 & 7:** all glyphs remain exactly unchanged; differences accepted.

User requests audit comparisons **three groups at a time**. Next triad:
(8) G111/G112 versus G131/G132 screenshot-traced similarities;
(9) crossed arc G066/G067 versus marked curve G079/G080;
(10) screenshot-traced G115/G116 at pen-size and the unresolved original
stroke-order guidance.

Every item and decision is in AUDIT_REVIEW_QUEUE.md. No other glyphs changed.
---

# Update — audit group decisions 3 and 5 (2026-10-20)

The user said groups **3** (G037/G038 versus G071/G072 and G079/G080) and
**5** (G054/G057 versus G055/G056) are fine. They stay unchanged.

For group **4**, user requested the **two separate lower side lines of G070
become one long continuous line**. A specific 4-stroke draft SVG is stored
under `drafts/G070_2026-10-20_unified_lower_line/`, retaining the original
upper bud paths and central stem, replacing only the two lower wing strokes.
**Awaiting user inspection before editing canonical G070**, which is an
authentic v0.13 historical source. The original vector is archived beside
the draft. G068 has a separate margin issue, not yet resolved.

User prefers 3 independent review groups per batch; keep future previews
organized in threes and track approval per group.

---

# Update — first complete visual audit (October 20, 2026)

Reproducible `audit_glyphs.py` installed in glyph recovery CI and run
successfully on all 150 registered active SVG vectors. Audit images and report
are in `generated/audit/`. Summary: 150 font PUA mappings valid, all declared
mirrors consistent, 21 historical mirrored siblings inferred without metadata,
20 unrelated similarity pair comparisons flagged for human triage,
G068/G070 touch the SVG cell margin and G070 has five distinct strokes.
Detailed human review order and caveats in `AUDIT_REVIEW_QUEUE.md`.

**No glyph artwork modified.** Start first with G037/G038 versus G066/G067,
one comparison set at a time. Do not declare the audit recommendations approved
or rewrite original early source vectors without explicit user input.

---

# Update — 150/150 glyphs visually finalized (October 20, 2026)

User approved **G147/G148 forked-sweep mirrored pair**, responding "Yes?
Let's keep them" to the new replacement preview. Their exact candidate
SVGs were promoted from
`drafts/G147_G148_2026-10-20_forked_sweep/` into
`source_geometry.json`; both now have approval
`approved_current_user` and confidence `APPROVED_NEW_VECTOR`.
G148 remains a true mirror of G147. Earlier rejected candidate artwork
is retained in historical draft folders.

**150 consecutive current glyphs G001–G150, all 150 active, 0 pending.**
G145 and G146 are singles. The new G149/G150 mirrored double-spiral pair
originated as draft G151/G152 (old draft names retained only as evidence).
This is a complete user-selected recovery collection, but NOT the authentic
lost original v0.19 dataset; many glyphs are traces and reconstructions.
No semantics are assigned, and late gesture guides are placeholders.

Recovery CI now enforces exactly 150 active SVGs and correct approvals of the
last pair. Rebuild fonts, guides, previews, archive and hashes from canonical
editable source. Follow-up work, if desired, should be full-glyph similarity,
legibility and handwriting tests. Keep the branch separate from `main`
until explicitly told to merge.

---

# Update — corrected 150-sign numbering, October 20, 2026

The user accepted the two-spiral G151/G152 proposal, rejected the spiral+lower
stroke G147/G148 proposal because it looks like approved G107/G108, requested
a completely new design for G147/G148, and asked that numbering stop at G150.

Canonical ID mapping after approved compaction:
- G001–G145: unchanged.
- **G146 = previous G149** (the accepted curved-stem with two upper branches,
  kept as a single).
- **G147/G148 = two PENDING DESIGN slots** (no active SVGs / font glyphs yet).
  A new two-stroke forked-sweep mirrored proposal is saved under
  `drafts/G147_G148_2026-10-20_forked_sweep/` but NOT approved.
- **G149/G150 = accepted double spirals**, former *draft-only* G151/G152.
- Old G146 and G150 redundant mirror artworks remain stored under
  `retired/`, but these IDs now point to different current designs.
- Original rejected G147/G148 designs remain under drafts and are no longer
  part of the current generated preview/font.
- There never were canonical G151/G152 registrations; only candidate filenames.

**Exactly 150 IDs G001–G150; 148 currently active glyph outlines + 2 reserved
pending slots (G147/G148).** When approved the two glyphs can be added without
further renumbering. The rebuilt font keeps the numerical PUA mapping and
omits the pending slots. Check old external documents/reviews referencing
G146–G152 against `NUMBERING_MIGRATION_2026-10-20.md`.

Next action: request feedback on the **new forked-sweep G147/G148 design**.
Do not mark the new design approved. Do not proceed to semantic assignment yet.

---

# Update — G147/G148 correction + proposed new G151/G152 (2026-10-20)

User requested that the accepted-for-edit G147/G148 two-curl *draft* lose the
terminal lower hook and have a straighter lower stroke. The updated proposal
is archived at `assets/glyphs/recovery/drafts/G147_G148_2026-10-20_spiral_straight_lower_R2/` (two SVGs); **not yet approved**, no canonical changes.
The original two-curl draft remains intact.

User ALSO requested a new pair composed of the same top spiral and an
**exact 180°-rotated copy** underneath, mirrored as a pair. Preview draft
SVGs are in `assets/glyphs/recovery/drafts/G151_G152_2026-10-20_opposing_180_spirals/`, provisionally labeled G151/G152, **not yet
registered/approved**. This preserves all 150 existing registry IDs and
the retired G146/G150 positions without renumbering.

Next: show the two updated pairs for user review and await explicit acceptance.
Do not infer approval of either pair from the request for changes.

---

# Update — G141–G150 initial review (2026-10-20)

User decision:
- G141/G142 and G143/G144: **accepted** visually as mirror pairs.
- G145/G146 nearly indistinguishable: **keep only G145 as a SINGLE**, retire G146.
- G149/G150 nearly indistinguishable: **keep only G149 as a SINGLE**, retire G150.
- G147/G148: both **rejected** for similarity to G139/G140. Draft two-curl replacement is backed up under `drafts/G147_G148_2026-10-20_double_curl/` but is **NOT approved**. Keep previous geometry as provisional/pending replacement only; archived under that draft folder.
- G146/G150 historical art preserved in `retired/`, not mapped to font or generated as active SVG. **No renumbering** and **no new designs for these slots** until the user asks.
- Rebuild now has 150 persistent registry slots but **148 active glyphs**, with explicit retired-status placeholders in previews. Existing Unicode assignments for other glyphs are unchanged.

Next user action: review the new G147/G148 proposal. Do not call that proposal approved or assume retired slots should be filled.

---

# Update — G133/G134 replacement accepted (October 20, 2026)

User said "That is fine" in response to the interlaced-curve G133/G134 replacement preview. The vector draft at `assets/glyphs/recovery/drafts/G133_G134_2026-10-20_interlaced_curves/` was promoted into `source_geometry.json`, with explicit modern-artwork approval. The previous angular/Z-like G133/G134 vectors were preserved in `rejected_predecessor/` in that draft folder. The original lost v0.19 geometry is **not** recovered.

G131/G132 visually accepted but IDs remain tentatively matched to the unlabeled screenshot. G135/G136 and G137/G138 visually accepted, approximations still. G139/G140 kept provisionally for now. All 10 IDs in G131–G140 have a current disposition; next review target is G141–G150. Changes must still be approved and backed up in GitHub one batch at a time.

---

# Update — G131–G140 review (October 20, 2026)

User said "131/132, 135/135 and 137/138 are fine. 133/134 are too alike older ones. 139/140 ... let's keep them for now." Interpret the repeated G135 as the existing mirror pair G135/G136.

- G131/G132: **visually accepted**, but screenshot-to-ID attribution remains tentative. Do not call it historically verified.
- G135/G136: **visually accepted** reconstructions. SVGs remain approximate.
- G137/G138: user reconfirmed acceptance; geometry remains approximate.
- G139/G140: **provisionally kept**, may be revisited. Do not treat as final approval.
- G133/G134: current older-looking Z-shaped signs **rejected for similarity**; retain in canonical as history while replacement remains unapproved.
- New proposed G133/G134 interlaced curves preserved in `assets/glyphs/recovery/drafts/G133_G134_2026-10-20_interlaced_curves/`. **Review the draft with the user before promoting it.**

No changes to glyph IDs, language meanings, original G091/92, or the G101–G110 approvals. Remain on G131–G140 for now.

---

# Update — G105/G106 approved (2026-10-20)

The user explicitly accepted the proposal to use original G091/G092 flipped upside down for G105/G106. Copied the *exact 180-degree coordinate-rotated* candidate SVGs from
`drafts/G105_G106_2026-10-20_inverted_G091_G092/` into canonical `source_geometry.json`. The rotated designs are new *approved derived glyphs*, **not** authentic lost v0.19 geometry. Original G091/G092 unchanged. Confidence `APPROVED_NEW_VECTOR`, approval `approved_current_user`, with `derived_from` and `transform_from_source` metadata.

G101/G102, G105/G106, and G107/G108 now carry explicit approvals.
G103/G104 and G109/G110 were deemed acceptable by the user but are still approximation-based SVGs, not authentic vector recovery. Keep working one batch at a time.

---

# Update — October 20: Review of G101–G110 (most recent)

- User approved **G101/G102** Revision 3 (the two strokes share a starting point), committed earlier to canonical source.
- User rejected the earlier G107/G108 versions, but **approved** the fresh curl-with-separate-lower-curve pair. It is now copied from `drafts/G107_G108_2026-10-20_revision3/` to the canonical source.
- User flagged **G105/G106's then-current top-leaf-on-curved-stem draft** as visually confusable with authentic **G091/G092**. That former draft was never canonically approved. It is preserved under `drafts/G105_G106_2026-10-20_side_leaf/prior_rejected/`.
- The newer G105/G106 **side-leaf sprig proposal** is saved as an unapproved candidate under `drafts/G105_G106_2026-10-20_side_leaf/`. This stays out of `source_geometry.json` until explicit approval.
- Work only on **G101–G110** until the user is happy. Do not jump to G131–G150.

---

# UPDATE — authentic v0.14 Revision 1 pack found, October 20, 2026

**This section supersedes the earlier recovery counts and workflow directions
below. Keep the older handoff for historical revision/approval decisions.**

The user uploaded `Cuspell_Glyph_Prototype_Pack_v0.14_R1.zip` (230,950 bytes,
SHA256 `8155354307d9abb2e261fa5e88962bb04eab2729553587d08bd2a03215bdbbf0`).
Its `README.md` explicitly says it builds from v0.13, retains 84 original
unchanged glyphs, and introduces 16 unapproved candidates in G081–G086 and
G091–G100. The rejected first v0.14 proposal contributes no designs.

**Verified authoritative provenance for today's recovery branch:**
- 84 exact historical v0.13 SVGs (G001–G080, G087–G090), unchanged in v0.14 R1;
- **16 exact v0.14 R1 source SVGs** (G081–G086, G091–G100), formerly guessed;
- 20 screenshot-traced G111–G130;
- 2 screenshot-traced G131–G132 with uncertain identification;
- 28 description-based approximations (G101–G110, G133–G150).

100 historical v0.14 R1 gesture marker records are now stored in GitHub.
Full original R1 guide SVGs for the 16 newly recovered glyphs and original
start/end markers for all 100 are backed up. Generated G101–G150 guides remain
placeholder outlines, not genuine drawing instructions.

**Durable GitHub inputs:** `evidence/v0.14_R1_confirmed_source.br.b64`,
`evidence/v0.14_R1_guide_markers.br.b64`, `apply_v014r1.py`, editable
`source_geometry.json`, rebuilt fonts and SVGs under `generated/`.
The original full v0.14 ZIP with its historic font binaries has *not* been
backed up as an intact GitHub binary; an exact copy is now saved in the
owner's ChatGPT Library at
`/Cuspell/Glyph Sources/Cuspell_Glyph_Prototype_Pack_v0.14_R1.zip`.
See recovery `README.md` for the exact contents and caveats.

**Do NOT use `bootstrap.py` to prepare normal edits.** It is an emergency
v0.13-based payload restore and overwrites `source_geometry.json`. The
GitHub recovery workflow now uses `apply_v014r1.py` then `restore.py`,
which builds from the canonical editable source and does not revert it.
Every later accepted revision must update `source_geometry.json` and be
committed; workflow dispatch can regenerate derived fonts and preview images.

**Separate main-branch CI improvement:** main commit `e2b9d0a2` added
workflow-level concurrency that cancels obsolete checks for the *same PR*.
It retained both Python 3.11 and 3.12 checks and leaves main push CI intact.
Main's test run passed on October 20. Other CI suggestions are still proposals.

**Next actions:** inspect the recovered G081–G110 review sheet with authentic
16 SVGs, revisit G101–G110 approximations, and review G131–G150. Do not
reapprove all original 84. Avoid merging unreconciled glyph candidates to main.

---

# Cuspell glyph recovery — handoff for next conversation
**Date:** 2026-10-20  
**Repository:** `MartinApostolov/Cuspell` (private)  
**Working branch:** `glyph-recovery-2026-10-20`  
**Do not start over. Read this document and the linked files first.**

## 1. Immediate state

The original post-v0.13 glyph prototype source files were lost when previous ChatGPT downloadable artifacts expired. The owner has only v0.13 plus surviving screenshots. We attempted a full **150-glyph recovery** on this branch and successfully checked in reconstruction data and generated artifacts. This is a **recovered draft**, NOT the exact lost v0.19. Never imply perfect fidelity or that every design was approved.

The recovery branch already contains:
- `assets/glyphs/recovery/source_geometry.json` — editable canonical reconstruction for 150 glyphs, with provenance/confidence records.
- `assets/glyphs/recovery/generated/glyphs/G001.svg` ... `G150.svg` — individual SVGs.
- `assets/glyphs/recovery/generated/gesture_guides/` — 150 SVG copies **not authentic stroke-order guides**.
- `assets/glyphs/recovery/generated/fonts/` — regenerated TTF + WOFF2.
- `assets/glyphs/recovery/generated/preview.html`.
- `assets/glyphs/recovery/generated/Cuspell_Recovery_Full_Inventory.png`.
- `assets/glyphs/recovery/generated/Cuspell_Recovery_G081_G110.png`, `...G111_G120.png`, `...G121_G130.png`, `...G131_G140.png`, `...G141_G150.png`.
- `assets/glyphs/recovery/generated/Cuspell_Glyph_Recovery_v0.19_150_glyphs.zip` — convenient single download/archival snapshot.
- `assets/glyphs/recovery/generated/RECOVERY_NOTICE.md` and `SHA256SUMS.txt`.
- `assets/glyphs/recovery/restore.py`, `bootstrap.py`, `make_review_sheets.py`, `payload/source.part01.b64` through `source.part08.b64`, and `payload/restore.py.br.b64`. These preserve reconstruction data and a regeneration path in GitHub; if using source JSON directly, `restore.py` or regenerated output is easiest.
- `assets/glyphs/recovery/README.md` contains short provenance summary.

**Critical:** The ZIP archive used as a source for the uploaded reconstruction (on the assistant's temporary filesystem when produced) also contained the original v0.13 ZIP, `RECOVERY_HISTORY.md`, user evidence screenshots, and scripts. The GitHub recovery ZIP may have a different subset and naming than the locally produced ZIP; inspect its contents rather than assuming every original binary is a separate GitHub blob. GitHub now holds the reconstructed SVGs, fonts, source and reference images. Preserve both Git history and downloaded backups.

**Status when interrupted:** Most recovery artifacts had been committed to the dedicated branch. The user needed to leave and requested this handoff. Do not claim any PR was merged or `main` was modified: work is on the recovery branch. Verify branch head and files through GitHub connector before changing anything.

## 2. Recovery provenance — do NOT flatten confidence classes

| IDs | What we have | Confidence |
| --- | --- | --- |
| G001–G080, G087–G090 (84 glyphs) | v0.13 original SVG data, preserved | Exact original **v0.13** outlines, not necessarily later lost editions |
| G081–G086 (6) | Last revision notes | Approximation |
| G091–G110 (20) | Descriptions and revisions | Approximation |
| G111–G120 (10) | User's v0.16 Revision 3 screenshot | Screenshot **silhouette trace** (not original Bézier/source order) |
| G121–G130 (10) | User's v0.17 Revision 1 screenshot | Screenshot **silhouette trace** |
| G131–G132 (2) | Unlabeled screenshot of a pair | Traced shape but identification as G131/G132 is **tentative**; ask user if needed |
| G133–G140 (8) | v0.18 Revision 1 descriptions | Approximation |
| G141–G150 (10) | v0.19 first proposal descriptions | Approximation, **not yet reviewed** |

A recovered design can be *visually approved in the past* and still have an *approximate recovered outline*. These are separate concepts. Do not silently promote approximations to original art.

## 3. Design rules (from the user's saved original glyph rules)

- One root maps to one glyph/monospaced character cell. Advance 600 units, em 1000; compound glyphs concatenate with no space; a space is one empty cell.
- Glyphs are **abstract** and MUST NOT hint at their meaning. Meanings can be remapped separately later. Do not assign rune meanings during this visual recovery.
- Primary medium is **hand/air writing**. Prefer continuous strokes and comfortably drawable shapes; two strokes are fine, three occasional.
- Small-size readability at **16 px**, 18 px comfortable. Rounded ends/joins, mostly monoline (~66 units), gentle hand-drawn irregularity rather than ruler geometry.
- Avoid tiny detached parts, imperceptible little hooks, crowded crossings, lookalike S variants, blobs, or too many nearly circular loops. **A tiny modification of an old glyph is not a new glyph**; prefer fundamentally different gesture topology.
- Exact, deliberate left/right **mirror pairs** normally appear consecutively; top/bottom flips are separately recorded. Not all glyphs must have a mirror; symmetric singles may stand alone. Do not mislabel a mirror as single.
- Reused *bud motif* should share recognizable shape/proportions. Earlier G060/G061: a bud and a line, **not two buds**; G070 should reflect that construction.
- Review against all existing inventory for collision, including at 16–18 px. Don't generate 10 forced variations where fewer distinct gestures are better.
- The user disliked the overhauled HTML review style in v0.14 but said to keep it temporarily. Future preview layout changes should be separately discussed.

## 4. Chronological decisions (very important to avoid reverting to rejected shapes)

- **v0.13:** baseline ZIP; G077/G078 had the **stronger tilt** approved; G087/G088 and G089/G090 were liked. Many early glyph mirrors corrected, repeated buds standardized.
- **first v0.14 proposal:** COMPLETELY rejected; never use it as a visual source.
- **new v0.14:** built from v0.13, G081–G086 redrawn, G091–G100 new. G083/G084 and G099/G100 rejected, G085/G086 needed steeper top-bottom tilt.
- **v0.14 R1:** G083/G084 became an **angular folded gesture**; G085/G086 staff tilt increased from ~18° to ~30°; G099/G100 became **curved line + crossing stroke**. Rest retained. Approval of replacements was implicit by moving on; don't overstate.
- **v0.15:** G101–G110 proposed. G101/G102 and G107/G108 disliked.
- **v0.15 R1:** G101/G102 = **separate curved upper stroke and lower sweep**; G107/G108 = **long hooked curve with detached diagonal**, other 106 glyphs retained. User moved to next batch.
- **v0.16:** G111–G120 proposed; G113/G114 rejected and G115/G116 needed horizontal opening.
- **v0.16 R1:** G113/G114 open fork rejected again; G115/G116 worse.
- **v0.16 R2:** G113/G114 crossed long curve rejected; G115/G116 still not what user sketched.
- **v0.16 R3:** user's drawing used for G115/G116: **rounded upper arch + nearly horizontal underscoring joined at one end, lower pointed apex with two descending curved legs**. G116 exact mirror. G113/G114 = two separate sweeping strokes replacing earlier failed attempts. User said "**That works. Next 10**", so do not resurrect previous rejects. Screenshot of complete G111–G120 v0.16 R3 survives, traced.
- **v0.17:** G121–G130 proposal; G125/G126 three stacked strokes rejected, all other 8 liked.
- **v0.17 R1:** G125/G126 replaced with angular flowing upper gesture + lower sweep; user explicitly said "**That is fine. Next 10**". Screenshot survives, traced.
- **v0.18:** G131–G140 proposal. User first typed 138/139, then corrected: ONLY **G137/G138** liked. G131–G136 and G139/G140 rejected.
- **v0.18 R1:** G131/G132 became asymmetric U shape, G133/G134 angular inward crossing gesture, G135/G136 three crossing sweep strokes, G139/G140 upper folded curve with distinct angular lower gesture. G137/G138 unchanged. User moved on; no separate formal approval of replacements.
- **v0.19:** added G141/G142 (detached upper curve + hooked branching gesture below), G143/G144 (tall sweep crossed by short arch), G145/G146 (pointed elongated closed form divided by curved crossbar), G147/G148 (angular upper hook + detached descending curve), G149/G150 (tall curved backbone with two upper branches). **None was reviewed** because user left and links later expired.

User is understandably concerned about losing source files. **Persist each subsequent update to GitHub BEFORE treating it as completed**, including all SVGs/fonts/source and screenshots where possible. Avoid relying on transient ChatGPT sandbox links.

## 5. Useful supplemental sources / evidence

- The original **v0.13 ZIP** was in this conversation, and was also copied into the recovery kit / locally generated archive. Preserve rather than overwrite.
- User supplied an image sketch for G115/G116 and full review-card screenshots for G111–G120 v0.16 R3 and G121–G130 v0.17 R1.
- There is a separate unlabeled two-glyph screenshot provisionally interpreted as G131/G132. Reassess identity before saying this is confirmed.
- Git archive source `source_geometry.json` stores `confidence` metadata (e.g. exact v0.13, screenshot traced, tentative identification, description approximation). Use those fields instead of guessing.
- The full original conversation's design descriptions are valuable evidence but often describe **rejected** iterations. Above notes summarize the latest revision.
- The recovery ZIP should not be labeled `v0.19` without `RECOVERED` in its user-facing title; actual lost original v0.19 is not present.

## 6. Immediate next actions for the next assistant

1. **Check GitHub** branch `glyph-recovery-2026-10-20` and inspect `assets/glyphs/recovery/`. Work from committed source; don't recreate everything from scratch.
2. Verify the 150 saved SVGs, two fonts, review PNGs, and editable JSON. Check `generated/SHA256SUMS.txt` or regenerate and compare; verify exactly 150 glyphs and correct mirror relationships. Assess whether screenshot traces are too heavy or materially distorted compared with the user's screenshots.
3. Ensure source evidence (v0.13 ZIP + screenshots) and recovery notes are backed up **inside the repository** if not already in archived ZIP. Avoid overwriting authentic v0.13 files.
4. Provide user a concise path to the recovery review images and discuss only the uncertain / approximation groups, especially G081–G110, G131–G150. Explain confidence transparently. Don't require reapproval of every original exact glyph.
5. Fix any obvious collisions and readability only after user input, and commit each accepted batch to GitHub. Consider a PR to merge validated work into `main` when ready; don't merge unreconciled candidates by default.

**Branch folder:** `assets/glyphs/recovery/`  
**High-value starting files:** `source_geometry.json`, `generated/Cuspell_Recovery_Full_Inventory.png`, `generated/Cuspell_Recovery_G081_G110.png`, `generated/Cuspell_Recovery_G131_G140.png`, `generated/Cuspell_Recovery_G141_G150.png`.

## 7. Important caveat / fidelity audit

One earlier recovery summary said 84 exact v0.13, 20 traced G111–G130, 2 tentative traced, 44 description approximations: **84 + 20 + 2 + 44 = 150**. Counts are consistent. The 84 originals are exact only **relative to v0.13**. The recovered fonts and 150 SVGs are rebuild outputs, not the missing proprietary originals from each intervening version. Some earlier versions had been marked candidates; user approval must be tracked independently from reconstruction quality.

Keep the language glyph project separate from the semantic dictionary and spellcraft source-of-truth in the Cuspell repo. Meaning assignment comes later.

---
**Created as a durable chat-to-chat handoff during recovery, at the user's request.**