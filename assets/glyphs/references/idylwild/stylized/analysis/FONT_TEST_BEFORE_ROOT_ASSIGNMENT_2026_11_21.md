# Cuspell — approve punctuation, then make the full 234-glyph PC-test font

**Status:** User-approved workflow order, 2026-11-21. Branch: `glyphs/idylwild-style-sample-01`. No merge into `main` without direct approval.

## Binding decisions

1. The original-source SVG readability proofs are acceptable for actual use **at 20 px or larger**; normal writing/testing target is **32–34 px**. Degradation below 18–20 px is accepted and should not itself cause glyph removal. This approval is not a claim that a compiled installed font has been tested.
2. **Finish punctuation next**, using the 13 drafted symbols in `assets/glyphs/references/idylwild/stylized/typography/player_facing/`. User has already selected original source R105 for `.`, R106 for `:`, and A054 for `?`. Ten other punctuation/grammar shapes remain pending user visual approval. `!` is independently drawn, and `R076` remains an eligible magic glyph.
3. **Then build an installable, PC-testable prototype font containing all 234 currently eligible glyph designs**, without first selecting just 218 or assigning any glyph to a word/root/number meaning. Preserve G originals plus stylized R and A designs exactly. Excluded designs and punctuation-reserved glyphs must not be counted among the 234.
4. For temporary **non-semantic** typing access, map the sorted 234 glyph IDs (G/R/A named IDs retained in lookup files) to 234 Private Use Area codepoints **U+E000 through U+E0E9**. This is strictly a test mapping, not Cuspell meaning assignment. In addition, map approved punctuation to ordinary Unicode `.`, `:`, `?`, `!`, `«`, `»`, `$`, `(`, `)`, `_`, `{`, `}`, `,`. Include space character, character map (ID → PUA Unicode), and a copy-and-paste typing/test page so all 234 symbols can be exercised on the user's PC. Do not repurpose the Cuspell `@` numeric-one sign as punctuation or assign its shape yet.
5. Validate: glyph coverage 234/234, no missing glyphs, Unicode cmap consistent with character map, install/uninstall, word spacing and baseline, em widths and strokes, sample dense sequences at 20/32/34 px, punctuation appearing inline, and normal Windows-style text rendering. Fix any font or layout issues identified by the user before semantic assignments.
6. **Only after successful PC trial** choose which 218 glyphs correspond to 217 canonical roots + the one special numeric sign and label the remaining 16 as spares. No root/name assignment before this checkpoint.

## Artifact and safety rules

- All original SVGs and prior decisions preserved on experimental branch. Do not silently change glyph style or exclude designs.
- Punctuation approval and installable-font creation are **separate checkpoints**. Font build is next once user approves/edits punctuation.
- The current 234 eligible count and 16 possible surplus are provisional inventory facts, not proof final font is installed or meanings are assigned.
- A prototype PUA font is for direct visual/typing tests; a separate final encoded font and parser integration will come later after root mapping.

## Next immediate action

Present source-accurate punctuation SVGs side by side at visually useful 100px reference, 34px primary, and 20px lower intended use sizes, distinguish 3 preapproved source references from 10 drafts, ask user which drafts need revision. Upon signoff, build the complete 234-glyph installable test font.
