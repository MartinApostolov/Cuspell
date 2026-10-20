# Glyph ID compaction — October 20, 2026

The user approved the provisional G151/G152 double-spiral designs and asked
to correct numbering to **150 total IDs**, while rejecting the current
spiral-plus-curve G147/G148 candidate for resemblance to G107/G108.

## Exact migration map

| Prior design ID / state | New canonical ID | Result |
| --- | --- | --- |
| G001–G145 | unchanged | All previously established glyph positions retained |
| Old G146 redundant mirror of G145 | none (art archived) | Former vector still under `retired/G146.svg`; number reused |
| G149 accepted single (branched stem) | **G146** | Identical SVG and current visual acceptance carried over |
| G147/G148, rejected variants | G147/G148 still reserved | Original and spiral/tail designs archived, **current slots empty/pending** |
| Old G150 redundant mirror of old G149 | none (art archived) | Former vector still under `retired/G150.svg`; number reused |
| Draft-only G151/G152 (accepted twin spirals) | **G149/G150** | Exact accepted SVGs, mirror pair, new final IDs |

Result: **G001–G150 exist as consecutive registry keys**, **148 have active
SVG artwork and font mappings**, and **G147/G148 are pending**. The fresh
forked-sweep pair proposed for G147/G148 is kept only as a separate draft
until explicitly approved. After that decision we can produce 150 active signs.

The old draft IDs G151/G152 were never official entries, and are retained as
the source filenames in `drafts/G151_G152_2026-10-20_opposing_180_spirals/`
for traceability. Earlier rejected G147/G148 SVGs and discarded G146/G150
mirrors likewise remain in historical directories.

Font codepoints are derived from final ID number: G001=U+E001,
G146=U+E092, G149=U+E095, and G150=U+E096.
Existing prototype text that used G146–G150 needs checking against
this renumbering. No glyph meanings have been assigned yet.
