# Checkpoint 138 — Shared Representation Teaching Module

_Status: completed modular beginner extension_

## Trigger

Checkpoint 137 extended the modular beginner progression through duration/maintenance and exact-event protection while keeping the semantic core at 11 signs.

The next roadmap item was shared representation/illusion.

The main teaching question was whether a useful first representation lesson really needs the previously suggested bundle:

`Represent Vision Sign And`

or whether the already-learned state, persistence, and creation machinery can do more of the work.

## Finding 1 — Represent + Vision is enough for the first lesson

The existing semantic relation is:

`Represent(carrier, content, channel) -> StateProposition`

The learner already knows:

- `Begin`;
- `End`;
- `Persist`;
- `ThisInterval`;
- `Create`;
- `At`;
- typed creation binders.

Therefore the first representation module needs only two new semantic signs:

`Vision Represent`

Cumulative semantic count: **20**.

## Existing-carrier examples

Begin a visual representation:

`Begin Represent This You Vision!`

End it:

`End Represent This You Vision!`

Actively maintain an already-established representation:

`Persist Represent This You Vision ThisInterval!`

These examples reuse earlier grammar instead of teaching another control structure.

## Finding 2 — shared representation is not forced Sense

`Represent This You Vision` states that the carrier This visually depicts You.

It does not state that:

- Self senses it;
- You senses it;
- every observer senses it;
- anyone believes it;
- anyone understands it.

Observers independently perceive the same carrier under ordinary channel/access rules.

That is the reusable meaning of “shared”: one objective carrier state, not an enumerated list of forced perception events.

## Finding 3 — representation does not make content real

Represented content need not be true or physically present.

A carrier visually representing a wall does not automatically:

- create a wall;
- gain the wall's Matter;
- gain collision or mass;
- gain the wall's Form;
- become evidence that a real wall exists.

Those effects require their own explicit semantics.

## Finding 4 — Sign is useful but not a prerequisite

A Sign is a representation/token capable of carrying Information, and image/painting vocabulary exists as a historical world Kind.

But Represent itself accepts any Entity carrier.

The first lesson therefore does not need to teach `Sign` classification merely to understand the carrier/content/channel relation.

Sign remains useful optional vocabulary for more specific carrier profiles.

## Finding 5 — And should stay with programming/composition

A richer created illusion can use conjunction to give one fresh carrier several simultaneous profile facts.

But pulling `And` into this module would teach a new composition structure merely to make one example more elaborate.

The existing Create continuation is enough for a simpler fresh-carrier example:

`Create i:Entity At $i There Begin Represent $i This Vision!`

Meaning:

1. allocate one fresh Entity;
2. place it at the designated Location There;
3. keep the fresh binder in scope;
4. begin a visual representation of This on that carrier.

No new conjunction syntax is required.

The exact visible realization is still controlled by deterministic world/media rules. If the world cannot realize the generic carrier/content/channel combination precisely enough, execution fails instead of inventing details.

## Finding 6 — only one channel belongs in the required module

Vision is enough to teach the channel role.

After that, Hearing or TouchChannel are ordinary vocabulary expansion:

`Begin Represent This You Hearing!`

`Begin Represent This You TouchChannel!`

Multi-channel carriers require conjunction/composition and belong with later programming material.

Tactile representation still does not automatically imply Matter, collision, mass, or damage.

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
5. `Vision Represent` -> 20.

The required semantic core remains 11 signs.

## Repository changes

Current machine truth becomes:

`language/subsets/spellcraft_beginner_v0_5.json`

Checkpoint-137 v0.4 is preserved under:

`archive/design/cp137_SPELLCRAFT_BEGINNER_V0_4.json`

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

**ADD ONLY VISION + REPRESENT FOR THE FIRST SHARED-REPRESENTATION MODULE.**

**DO NOT REQUIRE SENSE, SIGN, AND, HEARING, OR TOUCHCHANNEL.**

**TEACH SHARED REPRESENTATION AS ONE OBJECTIVE CARRIER STATE, NOT FORCED OBSERVER PERCEPTION.**

**KEEP EXACT WORLD/MEDIA REALIZATION EXPLICITLY OUTSIDE HIDDEN LANGUAGE SEMANTICS.**

## Next

Design the programming/multi-target teaching module without changing the 11-sign semantic core.
