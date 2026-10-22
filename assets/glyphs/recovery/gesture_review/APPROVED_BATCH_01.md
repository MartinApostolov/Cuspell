# Approved modern gesture directions: G111–G116 (three mirrored pairs)

**User-approved on 2026-10-22:** "keep all of them."

The exact three colored line sequences first presented in
`BATCH_01_G111_G116.svg` have been retained, without editing the
canonical black glyph silhouettes. The full machine-readable stroke
coordinates, pen-down order and start/end points are in
`approved_gestures.json` and a preserved snapshot of the original
proposal remains in `batch01_proposals.json`.

- G111/G112: 2 strokes, outer return then inner hook.
- G113/G114: 2 strokes, folded upper sweep then detached diagonal.
- G115/G116: 3 strokes, connected arch/underline then two lower legs
  from a common true pen-down location (offset number badges are merely
  labels in the illustration).

**These are approved contemporary guides, not rediscovered historical
v0.19 gesture orders or a proof of effortless handwriting.** The original
post-G100 direction guides are still unavailable. Mirror partners
reverse the horizontal coordinate direction of the first partner.

The existing `generated/gesture_guides/` continue to contain placeholder
outlines for these IDs. They are not silently overwritten by approval.
Use `approved_gestures.json` for current approved paths. A deliberate
future generator integration can create dedicated current approved guide
files, but must distinguish them from authentic archived historical
start/end guides. No semantic dictionary entry or actual glyph geometry
was modified by this decision.
