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
- **G145 (1):** accepted as a **single**; G146's redundant mirror **retired**.
- **G147–G148 (2):** original designs rejected for similarity to G139/G140; replacement proposal under `drafts/G147_G148_2026-10-20_double_curl/` awaiting review. Current files remain provisional pending replacement.
- **G149 (1):** accepted as a **single**; G150's redundant mirror **retired**.
- **G146/G150 (2):** retired ID slots, no active SVGs or font mappings. Original geometry preserved in `retired/`. Do not renumber existing glyphs without an explicit decision.

**Inventory:** 150 registered ID slots, **148 active**, 2 retired (G146, G150). The rejected G147/G148 drawings are visible only until a replacement is approved.

**In total: 100 genuine historical SVG outlines, 20 visually traced shapes,
2 tentative screenshot traces, 18 active approximate drawings and 8 user-approved new vectors; plus 2 retired slots.** An authentic v0.14 R1
outline is not guaranteed unchanged in the later lost v0.19.

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
  from the **editable** source, preserving authentic 100-glyph start/end
  guide information; guides G101–G150 are outline copies, not real directions.
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
