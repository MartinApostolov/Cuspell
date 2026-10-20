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