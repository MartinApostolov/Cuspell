# Checkpoint 139 — Programming and Multi-Target Teaching Audit

_Status: completed modular beginner extension_

## Trigger

Checkpoint 138 extended the beginner path through shared visual representation while keeping the semantic core at 11 signs.

The next roadmap item was the programming/multi-target family previously listed as:

`And Repeat Concurrent Each Collect Member Trigger`

The audit asks whether those seven signs should arrive as one block, whether the set is complete, and which advanced overloads should remain outside the required path.

## Finding 1 — the programming family should be staged, not bundled

The seven listed signs do not teach one concept.

They cover at least five distinct ideas:

- logical/state conjunction;
- ordered/simultaneous event composition;
- repetition;
- collection-based target distribution;
- persistent reactive watchers.

Checkpoint 139 therefore splits them into five stages.

## Finding 2 — Sequence was accidentally missing

The previous teaching candidate list included `Concurrent` but omitted `Sequence`.

That omission is not justified semantically.

`Concurrent` means component events are requested concurrently.

`Sequence` means ordered execution, with later EventSpecs evaluated against the world resulting from earlier successful steps.

Create's optional continuation is not a general replacement for Sequence: it exists specifically to keep one fresh identity binder in scope for one immediate follow-on EventSpec.

Therefore checkpoint 139 adds `Sequence` to the teaching path.

## Stage 1 — proposition/state conjunction

Add:

`And`

Cumulative semantic count: **21**.

Examples:

`Begin Whole This And Magic This!`

`Find Self This Whole This And Magic This!`

The first lesson teaches And only as proposition/state conjunction.

Event-level And is a transactional composite with different execution concerns and remains advanced.

Canonical surface is spoken-order infix; no visible collection braces are required.

## Stage 2 — ordered versus concurrent events

Add:

`Sequence Concurrent`

Cumulative semantic count: **23**.

Ordered example:

`Sequence Move This There Begin Magic This!`

Concurrent example:

`Concurrent Move This There Begin Magic You!`

Sentence end closes the flat event list.

`SequenceEnd` / `ConcurrentEnd` remain zero-mana grammatical closers for cases where later same-sentence material follows; they are not semantic signs and are not needed in these first examples.

## Stage 3 — finite repetition

Add:

`Repeat`

Cumulative semantic count: **24**.

Example:

`Repeat @@@ Create x:Entity At $x There Change $x Light «LightUnit» @!`

This repeats the whole Create EventSpec three times.

Because Create allocates one fresh identity per invocation, the result is three distinct created light sources if execution succeeds.

Only finite count-based Repeat is taught.

No omitted count means forever, and Repeat does not imply an unbounded loop.

## Stage 4 — bounded multi-target distribution

Add:

`Collect Member Each`

Cumulative semantic count: **27**.

Canonical teaching example:

`Each Collect x:Entity Member $x This y:Entity Begin Magic $y!`

The three meanings are kept explicit:

1. `Member $x This` states group membership;
2. `Collect x:Entity ...` constructs the typed collection;
3. `Each ... y:Entity ...` instantiates the EventSpec for every resolved member.

The same pattern can reuse measured Light:

`Each Collect x:Entity Member $x This y:Entity Change $y Light «LightUnit» @!`

### Boundedness rule

The designated `This` must have objectively resolvable group membership in the active context.

The binder domain `Entity` does not authorize universal search.

`Collect` remains selection from a resolvable domain, not divination.

A singular Process still never silently distributes over a Collection.

## Stage 5 — simple reactive programming

Add:

`Trigger`

Cumulative semantic count: **28**.

Examples:

`Trigger Locked This End Locked This ThisInterval!`

`Trigger Magic This End Magic This ThisInterval!`

Only the simple form is taught:

`Trigger condition action lifetime`

It is one-shot by default and requires a finite explicit lifetime.

The bound-witness form remains advanced:

`Trigger x:Entity condition($x) action($x) lifetime`

because it adds binder export from a match into the action.

## Why the module does not teach every overload

The teaching path intentionally avoids collapsing powerful multi-frame signs into all of their semantics at once.

Deferred uses include:

- EventSpec-level transactional `And`;
- mixed And/Or branch grouping and branch selection;
- bound-witness Trigger;
- Filter/Unique/MinBy/MaxBy/Random/Count collection work;
- generic bound Prevent interception;
- multi-channel/programmed illusion profiles.

This follows the checkpoint-136 rule that registered-sign count and actual learner load are different measures.

## Current modular progression

Semantic core:

- 6 signs;
- 9 signs;
- 11 signs.

Follow-on modules:

1. `Change Light` -> 13;
2. `At Create` -> 15;
3. `ThisInterval Persist` -> 17;
4. `Prevent` -> 18;
5. `Vision Represent` -> 20;
6. `And` -> 21;
7. `Sequence Concurrent` -> 23;
8. `Repeat` -> 24;
9. `Collect Member Each` -> 27;
10. `Trigger` -> 28.

The required semantic core remains **11 signs**.

## Repository changes

Current machine truth becomes:

`language/subsets/spellcraft_beginner_v0_6.json`

Checkpoint-138 v0.5 is preserved under:

`archive/design/cp138_SPELLCRAFT_BEGINNER_V0_5.json`

The 50-sign v0.1 projection remains a coverage benchmark rather than a teaching target.

## Inventory effect

None.

No root, frame, constructor, Old Name, or world concept is added.

The semantic inventory remains:

- 217 registered entries;
- 136 semantic primitive candidates;
- 55 formal constructors;
- 276 semantic frames;
- 53 multi-frame entries.

## Decision

**KEEP THE REQUIRED SEMANTIC CORE AT 11 SIGNS.**

**SPLIT PROGRAMMING/MULTI-TARGET MAGIC INTO FIVE STAGES.**

**ADD SEQUENCE TO THE TEACHING PATH; CREATE CONTINUATION DOES NOT REPLACE ORDERED PROGRAMMING.**

**KEEP COLLECT BOUNDED BY OBJECTIVELY RESOLVABLE MEMBERSHIP/DOMAINS.**

**TEACH SIMPLE TRIGGER ONLY; KEEP BOUND-WITNESS WATCHERS ADVANCED.**

## Next

Design the final planned time-manipulation teaching module, then stress-test the complete modular progression before declaring the teaching boundary stable.
