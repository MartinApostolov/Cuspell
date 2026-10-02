# Checkpoint 103 — Positional Omission Marker Migration

_Status: implemented canonical grammar migration_

## Trigger

Checkpoint 102 found that zero-mana English `:role` tokens such as `:authority`, `:context`, and `:path` were not pure grammar. The label itself selected semantic structure, so it carried meaning while bypassing the meaning-bearing-sign mana rule.

## Resolution

Canonical surface syntax moves from **v0.7** to **v0.8**.

Named role selectors are removed from current Cuspell.

Frame arguments remain ordered and positional.

A single zero-mana omission marker is introduced:

`_`

It means only:

> leave the current optional frame slot unspecified and advance to the next slot.

The marker has no role identity and no world meaning. Frame position determines what was omitted.

## Rules

- trailing optional slots may simply be absent;
- `_` is needed only when a later slot or outer argument must follow;
- one `_` skips exactly one optional slot;
- repeated `_` markers may skip repeated optional slots;
- `_` is invalid at a required slot;
- `_` is invalid as a free-standing semantic expression;
- internal slot names remain maintainer/parser metadata only;
- current English `:role` selectors are rejected by the parser;
- `named_only` frame metadata is obsolete and rejected by language-data validation.

## Canonical examples

Path with no goal/source:

`Move This _ _ ThisPath!`

Transfer profile with no explicit amount:

`Transfer DistributionOf This Self ThisRegion ThisRegion _ DistributionOf You Self!`

Closing an omitted broad optional tail so an outer argument can follow:

`Say Self Obligated Self MoveSelfHere _ You!`

The last example distinguishes the inner optional obligation context from the outer Say recipient without naming either role in the written language.

## Ordinary positional arguments

When an optional value is actually supplied, no marker is needed:

`Name «Road» This Self.`

`GratefulTo Self This ThisEvent.`

`Cause Self (End Whole This) You!`

`Permitted MoveSelfHere Self.`

The frame fixes what those positions mean.

## Surface-version history

The former current `language/syntax/surface_v0_7.json` is preserved as:

`archive/syntax/surface_v0_7.json`

Current machine-readable syntax is:

`language/syntax/surface_v0_8.json`

## Power notation cleanup

The execution specification also had a temporary `:power <Quantity>` notation. Although it was not parser frame syntax, it repeated the same semantic-English-after-colon defect. That notation is retired; Power surface syntax remains deliberately undecided until the later execution-layer design.

## Semantic/inventory effect

No semantic root or frame is added or removed.

Inventory remains:

- 205 registered base entries;
- 125 semantic primitive candidates;
- 256 semantic frames;
- 48 multi-frame entries.

The learning-complexity construction count is unchanged: the named-role construction is replaced by the single omission-marker construction rather than supplemented by another mechanism.

## Follow-up

With argument omission grammar stabilized, the remaining targeted language-stabilization jobs are:

1. decide player-facing pipe versus debug-only policy;
2. resolve the final genuine multi-frame lexical irregularity, `Distance`;
3. define/test the beginner subset.

Targeted semantic review of `Permitted` and `Cause` may still simplify those roots, but it is no longer required to repair optional-slot grammar.
