# Surface v0.10 — binder inference validation

_Status: approved design implemented; Python 3.11 and 3.12 CI passed (2026-11-22). This is still a pre-v1.0 language candidate, not a published release._

## What was implemented

The canonical grammar can now write the following without adding English metasyntax or any rune:

| Case | Canonical writing | Verified behavior |
| --- | --- | --- |
| Typed predicate | `All :«This» Life $«This».` | Infer Entity from Life's typed argument |
| Open question | `:«This» Life $«This»?` | Bind one Entity from the query |
| Location question | `:«This» At Self $«This»?` | Infer Location from At's second slot |
| Collection | `Collect :«This» Life $«This»` | Output Collection:Entity after inference |
| Two binders | `:«This» :«Here» At $«This» $«Here»?` | Infer Entity and Location independently |
| Explicit tight witness | `:«This»:MassSelf` | Existing MassSelf expression supplies Quantity:Mass, no parentheses |
| Underconstrained query | `:«This» Name «Yona» $«This»?` | Reject; generic SemanticValue is insufficient |
| Conflicting usages | `:«This» (Life $«This» And At Self $«This»)?` | Reject Entity-vs-Location conflict |
| Overloaded query | `:«This» Explains $«This» Life Self?` | Reject distinct valid Explanation/Proposition readings |
| Duplicate binder | `:«This»:This :«This»:Here At $«This» Here?` | DuplicateBinder; no active label shadowing |
| Independent scopes | `All :«This» Life $«This».` / `Some :«This» Life $«This».` | Label reuse across separate sentences is okay |

These are literal Cuspell syntax samples; syntax and semantics are checked through the project parser and glyph codec, not by English examples alone. Existing typed explicit binders and archived historical Latin binders remain accepted. Type witnesses in binder positions carry no mana and do not evaluate their represented value.

## Code/data touched

- `src/cuspell/parser.py` — gather typed variable uses, resolve one compatible type, defer dependent collection output types until after inference, reject active duplicate labels
- `src/cuspell/model.py` — preserve distinct inferred-type readings in canonical AST/ambiguity comparison
- `language/syntax/surface_v0_10.json` — canonical current grammar; `archive/syntax/surface_v0_9.json` preserves the prior snapshot
- `tests/test_native_binder_inference.py` and `tests/test_rune_native_writing.py` — new positive and negative cases
- Player and maintainer grammar/typing references updated

**Verification:** CI run `44965252507` executed **849 tests successfully** under Python **3.11** and **3.12**, including the established parser, book-derived corpora, glyph mapping and font integrity tests. All **217 rune meanings**, numeric-one `@`, **218 approved mappings** and **16 spare designs** remain untouched.

## What remains for Language v1.0

1. Targeted semantic test coverage for the less-common binder families (especially `Trigger`, `Find`, `Most`, and `Question`) across unambiguous, underconstrained, explicitly witnessed, and overloaded cases. Current full-suite success is not exhaustive proof of all 52 internal semantic types.
2. The user's real-PC UTF-8 test: copy approved glyphs, save in Notepad, close, reopen, and decode them to confirm Unicode survives storage. Notepad rendering already works with Cuspell Compact WinTest; VS Code is optional.
3. Final post-PC normative consistency verification, a versioned Language v1.0 release manifest, GitHub tag and release. Game-system execution and RequiredPower remain out of scope.

Do not infer that every internal type needs a new rune: most are type-system machinery, and the fallback is existing Cuspell composition or an explicit type witness only when actually needed.
