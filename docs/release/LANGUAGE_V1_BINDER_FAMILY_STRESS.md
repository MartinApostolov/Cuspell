# Language v1.0 — rare binder-family stress audit

_Status: 2026-11-22, canonical surface v0.10. Automated stress suite passed; subsequent Windows PC UTF-8 acceptance also passed._

## Scope and method

This release-gate pass checks all remaining low-frequency binder-bearing frame families, using native rune-label forms (not the historical ASCII binder notation): `Most`, `Trigger`, `Find`, `Question`, `Each`, `Filter`, `MinBy`, `MaxBy`, and `Prevent`. Existing v0.10 core tests already cover `All`, `Some`, `Collect`, and `Create`.

Each test checks successful semantic typing or a deliberately invalid/ambiguous case, and where applicable calls the glyph converter to verify the same source round-trips through the approved rune script. A quoted proper Sign such as `«Yona»` is allowed to retain its exact spelling; that is *data*, not an English grammar word.

## Tested matrix

| Family | Accepted example / property | Negative or regression coverage |
| --- | --- | --- |
| Most | `Most :«This» Life $«This».` infers Entity; explicit `:«This»:This` is equivalent in mana | `Most :«This» Name «Yona» $«This».` is underconstrained without a witness |
| Trigger | `Trigger :«This» Life $«This» Move $«This» Here ThisInterval!` infers Entity across condition and action | Rejects incompatible Location-vs-Entity uses; underconstrained binding |
| Find | `Find Self This :«Here» At This $«Here»!` infers Location | Enforces information scope use, answer-binder use, and explicit type mismatch |
| Question | `Question :«This» Life $«This»` produces typed QuestionContent, suitable for `AnswerFor` | Rejects generic untyped or genuinely overloaded binders; accepts an explicit Method witness |
| Each | `Each {This,You} :«This» Move $«This» Here!` infers the Collection member type | Maintains registered event-context typing |
| Filter | `Filter {This,You} :«This» Life $«This»` yields Collection:Entity | Preserves member type |
| MinBy | `MinBy {This,You} :«This» Mass $«This»` yields Collection:Entity | Preserves typed extrema operand |
| MaxBy | `MaxBy {This,You} :«This» Mass $«This»` yields Collection:Entity | Preserves typed extrema operand |
| Prevent | `Prevent :«This» Magic $«This» ThisRegion ThisInterval!` infers EventSpec from its fixed binder frame | Rejects incorrect explicitly Entity-typed event binder |
| Scope | Independent sentences can reuse `«This»` | Active nested reuse is rejected (DuplicateBinder) |

**Tests:** `tests/test_binder_family_stress.py` contributes **18** targeted test methods. Full GitHub Actions run **44965975682** passed **867 tests on Python 3.11** and **867 tests on Python 3.12**. The first preliminary test run found one overstrict test assertion: `«Yona»` was incorrectly treated as prohibited leftover Latin. The assertion now checks only Latin *outside* quoted Signs. It was a test correction, not a Cuspell grammar or parser change.

## Conclusion and limits

**No new grammar gaps were found in the nine stressed binder families.** Unique inference, tight Cuspell witnesses, explicit witnesses for overloaded predicates, type conflicts, duplicate active labels, Find information scopes and collection member typing work in the tested forms. No rune meaning, PUA mapping, glyph drawing, font metric, language type registry, parser semantics or mana rule was changed in this PR.

This is strong regression evidence for the registered frame families, not proof that every conceivable typed combination or magical world capability succeeds at runtime. Language v1.0 does not require the game runtime.

## User acceptance completed: Windows Notepad UTF-8 persistence

The user confirmed **Cuspell Compact WinTest** renders in Notepad and excluded VS Code. The following workflow was subsequently completed, with the actual uploaded glyph text independently verified; see [PC acceptance report](LANGUAGE_V1_PC_UTF8_ACCEPTANCE.md):

1. Open the **WinTest kit's** `meaning_keyboard.html`, put these two lines in its *Transliteration* box, and press **Convert → glyphs**:

       All :«This» Life $«This».
       Create :«This» At $«This» There Change $«This» Light «LightUnit» @!

2. Press **Copy glyph text** and paste into Windows Notepad using the installed **Cuspell Compact WinTest** family.
3. Save as **UTF-8 plain text** (e.g. `Cuspell-v1-test.txt`), close Notepad completely, reopen the same file, and select **Cuspell Compact WinTest** again if needed. A plain-text file stores the Unicode characters, not their font family.
4. Copy the reopened glyph text into the web keyboard's **Glyph writing** (right-hand) box; press **Decode → names**. Confirm the original two lines return, with the binder label, dollar reference, quote marks, `@` and final punctuation intact.
5. Report **pass** if it round-trips, or **fail** with the original and decoded text if anything changed. A screenshot is only needed for a visual failure.

**This test passed.** Remaining work is the Language v1.0 final consistency freeze, release manifest, and GitHub tag. No tabletop/game runtime implementation is required.
