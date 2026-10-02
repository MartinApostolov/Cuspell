# Checkpoint 104 — Pipe Player-Facing Policy

_Status: completed grouping-policy audit and implementation_

## Question

Should pipe hard-binding remain an advanced player-facing Cuspell mechanism, or become parser/debug compatibility only?

## Audit result

Pipe adds no semantic capability that current Cuspell otherwise lacks.

Player-facing Cuspell already has:

- typed flat prefix parsing for ordinary structure;
- tight adjacency for short local binding;
- parentheses for explicit grouping when a spaced subexpression must be forced;
- SequenceEnd / ConcurrentEnd for flat variadic event-group closure;
- the positional omission marker for optional-slot boundaries.

Pipe therefore duplicates grouping/binding behavior rather than filling an expressive gap.

## Live-repository usage

Before this checkpoint, no concrete player example required pipe.

The active player layer mentioned pipe only generically as an escape/debug tool.

Concrete live pipe forms were found in:

- maintainer/parser specifications;
- parser equivalence and source-span tests;
- legacy compatibility tests;
- provisional old color-system notation.

Executable dependence was therefore compatibility/debugging dependence, not player-language dependence.

## Decision

Pipe hard-binding is **not player-facing Cuspell**.

The reference parser continues to accept it for:

- historical compatibility;
- parser debugging;
- hard-bound diagnostic/source-span tests.

Current player writing uses:

1. flat typed structure where unique;
2. tight adjacency for short local units;
3. parentheses only when explicit grouping is genuinely needed.

## Why not keep both?

Keeping pipe and parentheses player-facing would create two explicit binding systems with overlapping purpose.

That would increase:

- teaching burden;
- glyph-design burden;
- surface choice without semantic gain;
- risk that player prose drifts toward programming/pseudocode notation.

The design target remains a flat foreign-language-like surface, so redundant structural syntax should not be player-visible without a concrete need.

## Parentheses

Parentheses remain legal zero-mana player-facing fallback grammar.

They should be uncommon.

Examples should prefer:

`MoveYouHere`

over a grouped spaced local expression when tight adjacency is unique.

A larger genuinely ambiguous spaced subexpression may use parentheses.

## Machine-readable policy

Surface v0.8 is retained; this checkpoint finalizes an open policy inside v0.8 rather than introducing a new accepted canonical construction.

`language/syntax/surface_v0_8.json` now places pipe under `debug_compatibility.pipe_binding` with:

- `player_facing: false`;
- `debug_only: true`;
- `legacy_compatibility: true`.

Pipe is removed from canonical separators and from the player-facing fallback list.

## Parser behavior

No parser capability is removed.

Historical forms such as:

`Move|This|Here!`

still parse in the reference implementation and remain covered by tests.

This compatibility does not make the syntax current Cuspell, just as legacy leading mood or bracketed binders do not become canonical merely because the parser can reproduce them.

## Documentation cleanup

Current specs now distinguish:

- parentheses — current explicit grouping fallback;
- pipe — parser/debug compatibility only.

Checkpoint 104 also removes residual pre-checkpoint-103 references to named role markers in the linear parsing/AST descriptions and removes pipe from provisional color-system surface examples.

## Learning-complexity effect

Checkpoint 97 counted **8 reusable structural constructions if pipe was included**.

With pipe removed from the player-facing language, the current player-facing count becomes:

**7 universal writing rules, 7 reusable structural constructions, and 1 genuinely irregular multi-frame lexical case (`Distance`).**

## Next step

The grouping-policy question is closed.

The next targeted lexical stabilization task is the remaining `Distance` irregularity.
