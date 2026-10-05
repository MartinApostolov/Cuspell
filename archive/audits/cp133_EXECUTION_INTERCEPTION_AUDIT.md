# Checkpoint 133 — Generic Magical-Execution Interception Audit

_Status: advanced spellcraft gap audit 4_

## Trigger

Checkpoint 128 identified Counterspell, Antimagic Field, Globe of Invulnerability, Forbiddance, and related effects as pressure for a generic way to stop a class of future magical executions before they commit.

## Existing tools

- simple `Prevent event interval` blocks one explicitly written EventSpec;
- `EndMagic` terminates an already active selected magical state/effect;
- `Trigger` reacts when a condition becomes true;
- ordinary Power/resistance resolves competing magic.

None alone expresses a pre-commit class interceptor.

## Why Trigger is not enough

A Trigger condition based on `Happen E` observes occurrence after the event has happened.

Counterspell/antimagic needs a veto point before the candidate world change commits.

Therefore this is an executor exposure problem, not a reason to add a Counterspell root.

## Typed Magic provenance

Existing `Magic` already states the magical state of an Entity.

Checkpoint 133 adds typed same-concept frames:

`Magic(EventSpec) -> Proposition`

`Magic(Event) -> Proposition`

For EventSpec, the proposition classifies attempted magical-execution provenance supplied by the executor.

For Event, it records that the realized Event was magical.

No rune is added.

## Bound Prevent

Prevent gains:

`Prevent(binder:Binder<EventSpec>, predicate:Proposition, region?:Region, scope:TimeInterval) -> EventSpec`

Canonical antimagic-style ward:

`Prevent e:EventSpec Magic $e ThisRegion ThisInterval!`

Without a spatial Region:

`Prevent e:EventSpec Magic $e _ ThisInterval!`

The binder is matcher-local and must be used by the predicate.

The executor presents attempted EventSpecs to active bound Prevent matchers before commit.

If the predicate matches, the interceptor contests/prevents the candidate.

The optional Region limits interception to candidate realization footprints that objectively affect, occur within, or pass through the Region.

## Generality

The form is not magic-specific.

Other predicates or typed world EventSpec Kinds can define wards against other event classes.

`Magic $e` is simply the predicate needed for antimagic.

This avoids spell-name roots and avoids hard-coding one list of magic types into Prevent.

## Power behavior

An active interceptor is magic and participates in the existing Power/resistance contest.

Insufficient interception Power means the candidate proceeds if otherwise executable.

A successful interceptor blocks commit; it does not partially realize the candidate and then undo it.

## Inventory effect

No registered entry or primitive candidate is added.

Frame changes:

- Magic: +2 frames (EventSpec, Event);
- Prevent: +1 bound matcher frame.

Totals after checkpoint 133:

- 216 registered entries;
- 135 semantic primitive candidates;
- 55 formal constructors;
- 274 semantic frames;
- 52 multi-frame entries.

Eight regressions cover EventSpec/Event Magic classification, simple Prevent compatibility, regional/global bound interception, EventSpec binder typing, binder use, and distinction between Entity Magic state and EventSpec Magic provenance.

## Decision

**DO NOT ADD Counterspell OR Antimagic ROOTS.**

Expose attempted execution to generic typed matching and extend Prevent with a pre-commit bound matcher.

## Next

Audit time-flow manipulation.
