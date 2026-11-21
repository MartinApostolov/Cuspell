# Historical Cuspell glyph-development materials

This folder contains **superseded reference material**, not current glyph-selection truth.

- `handoffs/` — earlier handoffs preserved as historical review and recovery context. They have been removed from active source folders so new sessions do not accidentally resume outdated stages.
- `old_font_builders/build_unified_font_449.py` — retired builder for the previous **449-glyph mixed comparison package** (150 original Cuspell + 299 Idylwild pixel candidates). The earlier generated ZIP/TTF versions remain retrievable from Git history.

## Current truth

- Glyph selection ledger: `assets/glyphs/references/idylwild/stylized/analysis/potential_overlap_groups.json`.
- Exhaustive 234-glyph visual similarity audit: `assets/glyphs/references/idylwild/stylized/analysis/FRESH_ALL_234_SURVIVOR_SIMILARITY_AUDIT_2026_11_21.json`.
- Current font builder: `assets/glyphs/references/idylwild/build_selected_review_font.py`.
- Current PC-test font/keyboard/chart package: `assets/glyphs/references/idylwild/keyboard_kit/`.
- Documentation: `assets/glyphs/references/idylwild/README.md`.

## Counts and next step (2026-11-21)

234 surviving visual candidates + 13 approved typography characters. All 234 must be tested as unassigned glyphs in the installable font before selecting 218 meaningful signs; the remaining 16 are provisional spares. Prefer a practical minimum of 20px, and test at 32–34px. No semantic-root-to-shape assignments have yet been made.

The original SVGs, CC0 source ZIPs and decision history are kept on the repository; none were discarded by archive cleanup.
