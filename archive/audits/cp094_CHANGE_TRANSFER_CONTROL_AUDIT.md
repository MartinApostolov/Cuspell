# Change, Causation, Transfer, and Control Second-Pass Audit

_Status: checkpoint 94 — family-level reduction experiment complete; one exact reduction found_

## Scope

This audit tests the five-root change/causation/transfer/control family:

- `Change`
- `Cause`
- `Give`
- `Transfer`
- `Control`

These entries are unusually important because they are already reused as supporting
machinery for many earlier reductions. The audit therefore distinguishes a true
specialized convenience root from a broad operation that merely resembles another
one in English.

## Reduction rule

A deletion is accepted only when the old root's complete executable meaning can be
written with surviving roots and ordinary zero-mana grammar, without:

- adding a replacement enum/value atom;
- weakening participant roles;
- strengthening the event beyond the old meaning;
- moving the same distinction into a hidden world rule;
- or conflating possession, physical/resource transfer, causal force, attribute
  change, and control.

## Experiment A — Give as generic Transfer

The tempting one-rune rewrite is:

`Give giver theme recipient` -> `Transfer theme giver recipient`

This is **not** accepted as the semantic definition.

`Transfer` is deliberately generic over `SemanticValue` source/destination roles.
It covers resource/value transfer and Distribution transfer. Those roles do not by
themselves assert the persistent possession relation `Have`.

The existing Give specification, by contrast, already fixes its exact possession
semantics.

Therefore generic Transfer remains broader than Give.

## Experiment B — Give as coordinated Have boundaries

The possession layer already supplies the complete meaning:

- giving ends `Have(giver, theme)`;
- giving begins `Have(recipient, theme)`.

The minimized event is:

`Concurrent EndHave giver theme BeginHave recipient theme`

This uses only surviving general machinery:

- `Have` is a persistent state relation;
- `Begin` / `End` create state-boundary EventSpecs;
- `Concurrent` coordinates the two possession boundaries into one transfer event.

The former Give entry has no additional manner, speech, permission, ownership,
location, or beneficiary semantics. Optional downstream control/location effects were
already world/context consequences rather than part of the lexical core.

This is therefore an exact specialized-process reduction, analogous to the earlier
removal of Get/Lose/Join/Separate-style transition conveniences.

**Result: remove Give.**

## Experiment C — Change from Begin/End or Cause

`Change` remains the generic value-bearing Attribute transition:

`Change(theme, attribute, target)`

It is not replaceable by `Begin` / `End`, which operate on truth-valued persistent
states rather than arbitrary functional Attribute values.

It is also not `Cause`. A Change EventSpec can occur without naming an external
causer; `Cause A E` adds a causal participant relation to an effect EventSpec.

Encoding every Change as a before/after equality pair plus generic event machinery
would require a new event-local transition constructor equivalent to Change and
would lose the existing target-value/family-value closure rules.

**Result: retain Change.**

## Experiment D — Cause from Change, control, or temporal order

`Cause` has two coherent roles:

- a Proposition relating actual Event cause/effect;
- an agentive EventSpec in which an Entity causes an EventSpec/state, optionally
  with an instrument.

Neither temporal ordering nor coexistence implies causation. `Control` is a
persistent controller-target state, not occurrence of an effect. `Change` describes
an attribute transition but does not state who/what caused it.

Removing Cause would therefore require another primitive causal relation/operator.

**Result: retain Cause.**

## Experiment E — Transfer from Change or possession boundaries

`Transfer` moves a resource/value from a source to a destination, optionally with
an amount and, for Distribution values, a destination profile.

It cannot be reduced to Give/Have boundaries because:

- resources need not be possessed Entities;
- source/destination are `SemanticValue` roles rather than necessarily holders;
- amount transfer can be partial;
- Distribution transfer carries profile semantics already used to replace
  `Redistribute`.

Nor is Transfer merely Change: it preserves explicit source and destination roles
for one transferred resource/value rather than setting one Entity Attribute to a
target value.

**Result: retain Transfer.**

## Experiment F — Control from Have, Own, Can, Cause, or Prevent

`Control(controller, target)` is a persistent state relation.

It is not:

- `Have`: possession/holding can exist without effective control;
- `Own`: institutional ownership can exist without current control;
- `Can`: capability is agent + EventSpec, not controller + target;
- `Cause`: a causal episode does not imply persistent control;
- `Prevent`: successfully preventing an event does not establish general control.

The earlier Grab reduction also depends on this exact relation:

`Concurrent Begin Touch A T Begin Control A T`.

Replacing Control with a generic relation wrapper plus a Control-value atom would
not reduce the semantic alphabet.

**Result: retain Control.**

## Old Name migration

Draft Old Names do not protect Give.

Three historical names used Give directly, and several later names nested the food
name. They are rebuilt with `Transfer` wording while retaining the same world-concept
meanings and the same rune costs:

- food: `«TransferLifeMatter»`;
- currency: `«TransferBeginHaveThing»`;
- market: `«TransferBeginHaveGroup»`.

Nested farm, farmer, food-store, and spoon spellings are updated accordingly.

This is only historical-name maintenance. Their present membership remains supplied
by world concepts rather than by re-running the literal etymology.

## Count result

One primitive root is removed.

Inventory changes:

- registered base entries: **206 -> 205**;
- semantic primitive candidates: **126 -> 125**;
- formal constructors: **54**;
- reference forms: **16**;
- domain values: **10**;
- unresolved candidates: **0**;
- derived candidates: **0**.

The change/causation/transfer/control family therefore becomes four surviving
semantic primitive candidates:

- `Change`
- `Cause`
- `Transfer`
- `Control`

## Design conclusion

The family contains one conventional specialization and four genuinely different
semantic mechanisms.

`Give` is exactly coordinated loss/acquisition of the persistent `Have` relation,
so it no longer needs its own rune.

The surviving four separate:

- value-bearing attribute transition;
- causal force/relation;
- resource/value source-to-destination transfer;
- persistent controller-target state.

Checkpoint 94 therefore removes **Give** and completes the second-pass audit of all
ten primitive families.

The next reduction step should be a **global cross-family closure pass** over the
remaining **125 semantic primitive candidates**, looking specifically for reductions
that only become visible after the successful second-pass generalizations
(`Rate`, temporal `Extent`, typed Region topology, and the accumulated
Begin/End/Cause machinery).
