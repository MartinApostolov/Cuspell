# Checkpoint 100 — Sense / Sign Interpretation Redesign

_Status: completed stabilization audit_

## Question

Checkpoint 99 identified `Sense` as one of three genuine multi-frame lexical irregularities. The explicit-channel frame represented raw sensory acquisition, while a contextual two-argument frame inherited the former `Read` meaning and additionally guaranteed successful semantic interpretation of a Sign.

The two frames did not share one semantic core.

## Previous state

`Sense experiencer channel stimulus` meant sensory acquisition through a named `SenseChannel`.

`Sense experiencer stimulus` meant successful Sign perception **plus semantic interpretation**. The latter existed only so the former `Read` root could be removed.

This contradicted the information model's established distinction between detecting a Sign and understanding what it means.

## Alternatives checked

### Keep the overload

Rejected. It preserves a learner-visible hidden meaning and violates the checkpoint-99 overload rule.

### Replace interpretation with `Understand`

Rejected. `Understand` is a persistent comprehension state. `Begin Understand` would additionally claim that a new state begins, which ordinary successful interpretation does not require.

### Replace interpretation with `Meaning`

Rejected. `Meaning(sign, content)` is a static Sign-to-content relation. It does not represent an interpreter performing a successful decoding event.

### Replace interpretation with `Infer`

Rejected. `Infer` is reasoning from Information to a Proposition and carries different participant roles and truth conditions.

### Restore `Read`

Possible but unnecessarily medium-specific. The atomic missing operation is successful semantic interpretation of a Sign, which also covers heard, tactile, gestural, or otherwise perceived Signs.

## Resolution

Add one semantic primitive candidate:

`Interpret(interpreter: Entity, sign: Sign) -> EventSpec`

`Interpret` means a successful semantic-decoding episode: the interpreter resolves/comprehends what the Sign conveys under the applicable language/context.

It does not:

- assert the conveyed content is true;
- imply that a new `Understand` state begins;
- specify a sensory channel;
- replace the static `Meaning` relation.

`Sense` now has only one frame:

`Sense(experiencer: Entity, channel: SenseChannel, stimulus: SemanticValue) -> EventSpec`

It means sensory acquisition only.

The former ordinary `Read` meaning is compositional:

`Concurrent Sense reader channel sign Interpret reader sign`

A reader can therefore Sense unfamiliar writing without successfully Interpreting it.

## Inventory effect

Checkpoint 99 state:

- 205 registered base entries;
- 125 semantic primitive candidates;
- 258 semantic frames;
- 50 multi-frame entries;
- 3 genuine irregular overloads.

Checkpoint 100 state:

- **206 registered base entries**;
- **126 semantic primitive candidates**;
- **258 semantic frames**;
- **49 multi-frame entries**;
- **2 genuine irregular overloads**: `Name` and `Distance`.

Frame-distribution after the change:

- 22 entries with no callable frame;
- 135 with exactly one frame;
- 36 with exactly two frames;
- 13 with three or more.

The frame total stays unchanged because one `Sense` frame is removed and one `Interpret` frame is added.

## Design consequence

Root count is not an optimization target that overrides semantic exactness. A previous reduction may be reversed or generalized when later audit evidence shows that it collapsed distinct truth conditions.

The current learning-complexity summary becomes:

**7 universal writing rules, 8 reusable structural constructions, and 2 genuinely irregular multi-frame lexical cases.**

If pipe becomes debug-only, the player-facing structural count becomes 7.
