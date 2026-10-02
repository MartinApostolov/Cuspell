# Checkpoint 109 — TimeInterval Boundary / Extent Access

_Status: implemented typed generalization; no new registered entry_

## Trigger

Checkpoint 106 found that Cuspell could construct a TimeInterval but could not directly inspect an already-referenced interval's boundaries or duration.

Before this checkpoint, the language had:

- `Interval(start,end) -> TimeInterval`;
- `IntervalFor(start,duration) -> TimeInterval`;
- `Begin(Event) -> TimePoint`;
- `End(Event) -> TimePoint`;
- `Extent(Event) -> Quantity:Time`.

A value such as `ThisInterval` therefore lost access to the same basic temporal information once the constructor syntax was no longer present.

## Audit finding

This is not a missing semantic primitive.

Events and TimeIntervals both have temporal boundaries/extent under the same concepts:

- beginning;
- ending;
- temporal extent.

Adding separate IntervalBegin, IntervalEnd, or IntervalDuration roots would duplicate meanings already carried by Begin, End, and Extent.

The exact repair is typed generalization.

## Accepted frames

### Begin

Add:

`Begin(TimeInterval) -> TimePoint`

This shares the temporal-boundary meaning of `Begin(Event)`.

The existing:

`Begin(StateProposition) -> EventSpec`

state-onset meaning remains unchanged.

### End

Add:

`End(TimeInterval) -> TimePoint`

This shares the temporal-boundary meaning of `End(Event) -> TimePoint`.

The existing:

- `End(StateProposition) -> EventSpec`;
- `End(Event) -> EventSpec` for stopping an ongoing event;

remain unchanged and are resolved by type/expected result.

### Extent

Add:

`Extent(TimeInterval) -> Quantity:Time`

for finite interval duration/temporal extent.

This is the same general temporal-extent meaning already used by `Extent(Event)`.

## Unbounded intervals

The TimeInterval semantic type may represent explicitly unbounded intervals.

Therefore these accessors are partial where the requested value does not exist:

- an interval unbounded below has no Begin TimePoint;
- an interval unbounded above has no End TimePoint;
- an interval without finite temporal extent does not produce a finite Quantity:Time.

The world/evaluation layer must treat such a value as unavailable/failing rather than inventing a boundary or finite duration.

Checkpoint 109 deliberately does not add a BoundedTimeInterval subtype merely to encode this partiality.

## Constructor consistency

For:

`Interval(start,end)`

the accessors return the supplied boundaries, and Extent is their finite temporal separation under the time model.

For:

`IntervalFor(start,duration)`

- Begin returns start;
- Extent returns duration;
- End returns the corresponding point under the world-time model.

Named/calendar intervals can expose the same values once the world package maps the name to a TimeInterval.

## Regression requirements

The parser must accept:

- `Begin ThisInterval` as TimePoint;
- `End ThisInterval` as TimePoint;
- `Extent ThisInterval` as Quantity:Time;
- the same accessors directly over a freshly constructed `IntervalFor`.

Event Begin/End/Extent and End(Event)->EventSpec stopping semantics must remain intact.

## Inventory effect

No registered entry is added or removed.

Before checkpoint 109:

- 210 registered entries;
- 129 semantic primitive candidates;
- 55 formal constructors;
- 260 semantic frames;
- 48 multi-frame entries.

After checkpoint 109:

- **210 registered entries**;
- **129 semantic primitive candidates**;
- **55 formal constructors**;
- **263 semantic frames**;
- **48 multi-frame entries**.

Frame distribution changes because Begin moves from two frames to three:

- 22 zero-frame entries;
- 140 one-frame entries;
- 35 two-frame entries;
- 13 three-or-more-frame entries.

## Civilization-audit progress

Checkpoint 109 resolves the third semantic/structural issue from checkpoint 106.

One structural vocabulary question remains before broad Old Name expansion:

- whether historically lexicalized parameterized verbs/relations require a safe Old-Name/template mechanism or should remain transparent compositions.

## Result

Referenced TimeIntervals are now first-class inspectable temporal values rather than opaque results whose constructor history must be reconstructed.

The repair uses existing semantics only: **zero new runes, zero new primitive candidates**.
