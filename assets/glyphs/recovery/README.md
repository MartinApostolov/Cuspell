# Cuspell glyph recovery (October 2026)

This directory is a **reconstruction**, not the lost original v0.19 glyph set.
The recovered 150 entries mix authentic older artwork, screenshot traces and
description-based candidates. Glyphs remain unassigned to meanings.

## Authentic input recovered on October 20

The owner located the **original v0.14 Revision 1 prototype pack** (100 glyphs).
The archive's SHA256 is `8155354307d9abb2e261fa5e88962bb04eab2729553587d08bd2a03215bdbbf0`.

- **G001–G080, G087–G090 (84):** original v0.13 SVGs, documented as unchanged
  in the authentic v0.14 R1 pack. Confidence: `EXACT_V013`.
- **G081–G086, G091–G100 (16):** exact v0.14 R1 original SVGs; the older
  prose approximations have been replaced. Confidence: `EXACT_V014_R1`.
- **G101–G102 (2):** newly approved editable vectors (Revision 3), based on the user's reference sketches. Their shapes are NOT historical recovered source. Confidence: `APPROVED_NEW_VECTOR`.
- **G103–G104, G109–G110 (4):** reconstructed approximations judged acceptable in recent review; not exact historical vectors.
- **G105–G106 (2):** user-approved 180° rotations of authentic v0.14 R1 G091/G092, in canonical SVG source, with mirrored pair relationship. `APPROVED_NEW_VECTOR` (approved derived design, not recovered historical v0.19 artwork). Rejected top-leaf and unapproved side-leaf drafts are still archived.
- **G107–G108 (2):** user-approved new curled gesture plus detached rising sweep; canonical vector mirrors, `APPROVED_NEW_VECTOR`.
- **G111–G130 (20):** screenshot silhouette traces, NOT original Bézier geometry.
- **G131–G132 (2):** accepted visually in the current review, while screenshot IDs remain **tentative**.
- **G133–G134 (2):** user-approved new two-stroke interlaced-curve replacement, `APPROVED_NEW_VECTOR`. The rejected angular glyphs and the selected candidate vectors are preserved in `drafts/G133_G134_2026-10-20_interlaced_curves/`.
- **G135–G136 (2):** accepted visually, but reconstructed geometry remains approximate.
- **G137–G138 (2):** historically liked, reconfirmed in the current review; still approximate.
- **G139–G140 (2):** kept **provisionally** pending possible later review, not final geometry approval.
- **G141–G144 (4):** accepted visually as two mirror pairs, but their recreated geometry remains approximate.
- **G145 (1):** original accepted pointed enclosure, kept as a single.
- **G146 (1):** the previously approved **G149 single** (curved backbone with branches), copied unchanged into the former redundant-mirror G146 slot.
- **G147/G148 (2):** **approved two-stroke forked-sweep mirror pair**, sourced from `drafts/G147_G148_2026-10-20_forked_sweep/` on 2026-10-20. Earlier angular and spiral-tail variants were rejected, and remain archived. The accepted vectors are modern approved artwork, not original v0.19 recovery.
- **G149/G150 (2):** user-approved mirrored double spirals, promoted without geometric changes from the provisional G151/G152 draft.
- **G146/G150 historical artwork:** their old redundant mirror variants remain archived at `retired/G146.svg` and `retired/G150.svg` but **these ID numbers now have different active artwork**.

**Inventory:** **150 active glyphs with contiguous IDs G001–G150**, no
gaps or pending slots. All current SVGs are included in generated fonts,
the review site, and graphical inventory. Historical names G151/G152 only
occur in the draft evidence directory and are NOT registered current glyph IDs.

**Current canonical provenance (2026-10-22):** 98 unchanged authentic earlier
SVG vectors (82 exact v0.13 + 16 exact v0.14 R1), 20 screenshot-traced
outlines, 2 tentatively attributed screenshot traces, **14 user-approved
modern or revised vectors**, and 16 description-based reconstructions.
The earlier original artwork for both revised G068/G070 is fully preserved,
so **100 genuine historical source outlines** remain in the backups. Approval
of the modern designs does not mean the lost original v0.19 geometry,
or authentic later gesture-guide stroke order, has been recovered.

## Preserved evidence

- `evidence/v0.14_R1_confirmed_source.br.b64`: the 16 newly recovered source
  SVGs, their 16 original gesture guides, and the v0.14 R1 glyph map,
  review notes, prototype text, and design rules.
- `evidence/v0.14_R1_guide_markers.br.b64`: original stroke start/end marker
  markup for all **100** v0.14 R1 guides.
- `apply_v014r1.py`: applies the original 16 candidates to approximate
  entries without overwriting later reviewed artwork.
- `source_geometry.json`: the editable 150-glyph canonical recovery source.
- `restore.py`: regenerates SVGs, TTF, WOFF2, review website and directions
  from the **editable** source; 100 historic gesture records remain backed
  up, but current generated guides for the revised G068/G070 are outline
  copies, along with G101–G150. Guides for the 98 unchanged historical
  outlines retain historical marker information.
- `generated/`: the rebuilt output with review sheets and archive.
- `payload/` and `bootstrap.py`: emergency backup of the original
  v0.13-based 150-candidate reconstruction. Do not run `bootstrap.py`
  during normal revision work: it rewrites the editable source with OLD data.

The 230,950-byte uploaded **full original v0.14 R1 ZIP, including its original
font binaries**, has not been copied as an intact ZIP into this repository.
Its changed SVGs, guidelines, gestures and metadata have been retained in
the compact evidence records. The intact user-supplied ZIP is additionally backed up in the owner's
personal ChatGPT Library at `/Cuspell/Glyph Sources/Cuspell_Glyph_Prototype_Pack_v0.14_R1.zip`.
The Library copy is not a GitHub blob.

Never merge reconstructed candidates into the approved inventory without
review. Keep the glyph designs separate from semantic dictionaries.

## Complete visual review (2026-10-20)

The user accepted the completely new G147/G148 forked-sweep design. The
approved SVGs are now canonical in `source_geometry.json`, and the original
reviewed proposal and rejected alternatives remain safely archived under
`drafts/`.

The approved opposite-spiral drafts G151/G152 were assigned the final IDs
G149/G150. The earlier accepted G149 single moved to G146. For details
and old-to-new mapping see `NUMBERING_MIGRATION_2026-10-20.md`.
The active registry now ends at G150.

Visual selection is complete; collision/readability/stroke-order audits and
release readiness checks are separate tasks. Do not merge reconstructed
signs to `main` without an explicit release decision.

## Visual audit amendments (October 20, 2026)

G070 was historically an exact v0.13 SVG. After reviewing the audit preview,
the user approved a revised lower line: its two outward lower strokes are
now one continuous sweeping crossbar. The design has **four** separate stroke
paths, down from five, and keeps the historic upper buds and central stem.
The current G070 is tagged `APPROVED_NEW_VECTOR`, not `EXACT_V013`.
The original exact older SVG survives in
`drafts/G070_2026-10-20_unified_lower_line/G070_original_v013.svg`.
G068 was still unchanged at that October 20 stage, and groups 6 and 7 were retained.
Both G068 and G070 were subsequently narrowed by 15% on October 22 (see below).

## Final visual audit decisions (October 22, 2026)

- **Group 11:** G068 and G070 were approved **15% horizontally narrower** about x=300 (stroke width held at 66 and vertical dimensions unchanged). Before/after SVGs and a comparative preview are stored under `drafts/G068_G070_2026-10-22_narrower/`. Both now have provenance `APPROVED_NEW_VECTOR` rather than `EXACT_V013`.
- **Group 12:** Keep G060/G061, G068/G070 as a coherent design family; no extra edits.
- **Group 13:** Keep screenshot-traced G113/G114, G125/G126 and G129/G130 at 16px; real historic stroke-order guides remain unavailable.

**All 13 visual-review groups have user decisions.** The automatic rebuild and font audit after the final narrowing passed, with 150 active SVGs, 150 font mappings, consistent declared mirrors and **zero edge-clipping flags**. These technical checks do not verify every glyph's real-world handwriting ease or lost historical gestures. Nothing has been merged into `main`.

## Handwriting / gesture review

Batch 1 for G111–G116 **approved modern gesture paths** on October 22,
in `gesture_review/approved_gestures.json`. Their paths describe user-
approved current hand directions, **not original historical stroke order**.
Batch 2 for G117–G122 is awaiting review. See `gesture_review/`.
This process does not alter canonical glyph silhouettes or post-G100
placeholder generated gesture guides until explicitly integrated.
