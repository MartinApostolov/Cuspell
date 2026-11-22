# Language v1.0 — Windows PC Unicode acceptance

**Status: PASS (2026-11-22).** This is the human-approved acceptance of the Windows font and UTF-8 preservation check, **not** the Language v1.0 release tag.

## Evidence

The user provided (1) a screenshot of **Cuspell Compact WinTest** displaying the reopened `Cuspell-v1-test.txt` in Windows Notepad, (2) a screenshot of the offline keyboard successfully decoding the glyph text back into the original two transliteration sentences, and (3) the actual `Cuspell-v1-test.txt` file.

The saved file was independently inspected as Unicode in this review:

- File size: **90 bytes**, valid **UTF-8** (no BOM necessary), **2 lines**, no U+FFFD replacement characters.
- Exact SHA-256 of the uploaded file: `79b5c1bdfa8d73c2f85953662f7a6fa10a7104de0c21facbfbdad5977479d228`.
- The entire saved glyph payload matches the registered `language/core/glyph_assignments.json` mapping, punctuation, inter-word spaces, and original source after removing only any optional final newline.
- All runes and punctuation survive: `All`, `Create`, `This`, `Life`, `At`, `There`, `Change`, `Light`, `Unit` (composed as `LightUnit`), numeric `@`, `:`, `$`, `«»`, `.`, and `!`.
- The keyboard screenshot shows the recovered transliteration:

  ```text
  All :«This» Life $«This».
  Create :«This» At $«This» There Change $«This» Light «LightUnit» @!
  ```

- Notepad rendering was previously approved with the separately named `Cuspell Compact WinTest` font. The user deliberately excluded VS Code from the language-release requirements.

The screenshot and user confirmation support the save → close → reopen → copy → decode workflow. The uploaded file independently establishes exact codepoint preservation, not just visual similarity.

## Acceptance boundary and next action

The **Windows PC acceptance gate is complete**. No more user-side Notepad, VS Code, or font glyph review is required for the present Language v1.0 candidate. The remaining work is maintainer-side: final normative/source-of-truth review, a versioned language-only release manifest and font distribution choice, consistency tests on the exact release candidate, and the **GitHub Language v1.0 tag/release**. The parser surface remains version `v0.10`; this is a component version, not a claim that the language has already been released.

No tabletop prototype or general-purpose game system is a dependency.
