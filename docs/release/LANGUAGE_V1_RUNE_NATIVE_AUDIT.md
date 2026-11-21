# Language v1.0 — Rune-native writing audit

_Status: 2026-11-22; pre-freeze audit and proposal, **not** an approved language-rule change. Normative parser surface remains v0.9._

## Goal and scope

The user wants **all ordinary Cuspell writing to be composed of approved runes, approved punctuation, and Cuspell Names**. English labels such as `x:Entity`, `m:Method`, and `SequenceEnd` must not be *required* to write valid current sentences. English explanations in documentation, type identifiers inside machine files, and exact quoted external/proper Signs are a different matter: they are not grammatical words in a Cuspell sentence.

Reviewed current sources: `language/core/{lexicon,types,glyph_assignments}.json`, `language/syntax/surface_v0_9.json`, `src/cuspell/{parser,language,glyphs}.py`, the live `docs/spec` and `player` guides, current 82 spellcraft examples and regression tests. The original glyph mapping and font designs were not edited.

## Confirmed results

- The 217 registered rune roots and the special `@` sign still have 218 distinct approved assignments, with 16 spare designs. The v0.9 native handle `:«This»` and reference `$«This»` encode to approved glyph/punctuation characters; `Create` gets its `Entity` binder type from the registered frame.
- **Explanation is not missing a rune.** The registered atomic root `ThisExplanation` has semantic type `Explanation`. A native question can say `:«This»:ThisExplanation Explains $«This» Life Self?` with no outside English type name. Likewise `ThisMethod` supplies type `Method` for `:«This»:ThisMethod Purpose $«This» Life Self?`. See `tests/test_rune_native_final_audit.py`.
- The 52 semantic type identifiers are **internal typing metadata**. Seventeen have at least one directly atomic registered word (e.g., `ThisExplanation`, `ThisMethod`, `ThisRegion`, `ThisInterval`, `Here`, `Now`); 35 do not. **This does not imply 35 missing runes**: composite expressions and event/frame inference already supply some of those types.
- The current lexicon has **14 frame slots explicitly typed Binder**. Two declare `binds_type` directly (`Create`/Entity and `Prevent`/EventSpec), and four refer to an already supplied collection member type (`Each`, `Filter`, `MinBy`, `MaxBy`). Eight remain dependent on an explicit type witness or future inference from the predicate/context: `All`, `Collect`, `Most`, two `Some` frames, `Trigger`, `Find`, and `Question`.
- Historic syntactic forms are retained for backwards parser compatibility and archived corpora. They are **not** canonical v0.9 writing. The player-facing colon group closer is already implemented.
- Live normative specs still included older `p:Entity`, `x:Entity`, `d:TimeInterval`, `m:Method`, and schematic `x:Type` examples. This pass converts those examples to current rune-native spellings and corrects the misleading assertion that a grammatical Old Name **type witness** incurs normal semantic Old Name mana cost.

## Gaps that still need an explicit language-design decision

1. **Constraint-based binder type inference.** An open question like `:«This» Explains $«This» Life Self?` has no type witness; current v0.9 `check()` does not solve the binder type from the `Explains` frame backwards. The same affects quantifiers/collection comprehensions whose binder slot has neither `binds_type` nor a prior collection-member type. The existing explicit `:«This»:ThisExplanation` form works, but that does not prove every future needed type has a short witness.
2. **Compound type-witness surface.** The parser accepts a single registered/tight Latin root sequence (e.g. `ThisExplanation`) or a quoted named Kind after the second colon. It does **not** yet accept an arbitrary longer, space-separated Cuspell expression as the type witness. Some internal types (e.g. `Sign`, `QuestionContent`, `CoordinateFrame`, `GeometryProfile`) have no direct atomic witness in the current lexicon, so their universal explicit-binder coverage is **not demonstrated**. We should not add one rune per internal type without evidence.
3. **Kind versus member type.** `:«This»:Thing` gives the binder type `Kind` (the atomic type of `Thing`), *not* automatically `Entity`. A quoted registered Old/New Kind witness follows the named-Kind classification rules instead. This distinction must be explained and tested before teaching generic written type witnesses.
4. **Label uniqueness/shadowing.** `Context.with_variable` stores bindings by label and overwrites an existing label in its context. For a sequence of open-question binders, there is not yet an explicit duplicate-label/shadowing rule in the current surface snapshot. This needs a deliberate scope policy rather than arbitrary parser behavior.
5. **Literal quoted Signs.** Names and Signs can contain human-readable content as exact quoted data by design (e.g. `«Yona»`). That must not be confused with allowing English variable or semantic type words as *grammar*. No new rune meaning is needed simply to spell a proper name.

## Recommended next grammar decision

**Prefer evidence-based inference first, explicit rune-native witnesses second; never silently guess on ambiguity.**

For binders whose typed role is unambiguous from the registered frame, use the already implemented inferred type. For `All`, `Some`, `Collect`, `Question`, `Find`, and other underspecified slots, optionally infer a type from *all* typed uses of that label **only if their constraints have a unique compatible semantic type**. Retain the present `:«label»:ThisExplanation` and `:«label»:«NamedKind»` forms as explicit alternatives. If a type still lacks a suitable compact witness, consider a grammatical enclosure for a full Cuspell type expression (not a new English type word or a new root for every internal type). Reject conflicting or underconstrained cases with a specific diagnostic.

**This recommendation is not an implementation approval.** Confirm scope/shadowing behavior and type inference policy before changing `src/cuspell/parser.py`, `language/core/types.json`, or the normative v0.9 syntax. Until then the explicit verified native witness forms are usable, and the language should remain **pre-v1.0**.

## Validation and release boundary

- The existing 82 maintained spellcraft examples, glyph conversion checks, Old Names and sampled nine-book regressions remain the automated baseline.
- New tests demonstrate registered Explanation/Method witnesses, current examples and source–glyph round trips; they do **not** falsely claim exhaustive binder type coverage.
- Windows Notepad rendering of the separately named WinTest compact font has been observed by the user. VS Code remains optional. Separate UTF-8 save/reopen acceptance and final release tagging remain outstanding.
- Do not re-open the 217 approved glyph meanings, 16 spare assignments, original font mapping, game-system rules, or magical execution/balance as part of this audit.
