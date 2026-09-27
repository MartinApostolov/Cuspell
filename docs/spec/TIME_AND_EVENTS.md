# Time, Events, and Temporal Relations

_Status: working specification v0.1_

This specification formalizes time references, intervals, event identity, temporal relations, recurrence, and temporal quantification.

## 1. Temporal values

Cuspell distinguishes:

- **TimePoint** — a position on a time ordering.
- **TimeInterval** — a bounded or explicitly unbounded temporal region.
- **EventSpec** — description of an event that could occur.
- **Event** — concrete occurrence with temporal extent.
- **EventRef** — typed reference to one concrete Event.

These are semantic values/domain types rather than ordinary lexical Categories.

## 2. Now

`Now` is `Reference<TimePoint>`.

For magic it resolves at the defined evaluation/activation instant.

A persistent Trigger may re-evaluate Now at each trigger check; the Trigger specification must say whether references are frozen at creation or dynamically re-resolved.

## 3. Moment

`Moment` is a Kind/domain concept for a TimePoint or sufficiently point-like temporal reference.

It should not silently imply Now.

## 4. Event temporal extent

Every concrete Event has:

- Begin(Event) -> TimePoint
- End(Event) -> TimePoint
- Duration(Event) -> Quantity<Time>

For instantaneous events, Begin and End may be Equal under the world's time resolution.

## 5. Before and After

`Before` is an ordered temporal Relation.

Typed frames include:

`Before(TimePoint A, TimePoint B)`

meaning A < B.

For Events:

`Before(Event A, Event B)`

means End(A) is strictly before Begin(B), unless a later rules profile deliberately permits touching boundaries.

`OppositeBefore = After`.

After is the reversed temporal ordering relation, not NotBefore.

## 6. Simultaneous and temporal overlap

NotBefore is too broad to mean simultaneous.

Add useful temporal Relations:

`Simultaneous(A,B)`

for equal relevant TimePoints or event timing under a declared tolerance.

`TimeOverlap(Event/Interval A, Event/Interval B)`

when their temporal extents intersect.

These are preferable to deriving temporal relations from vague negation.

## 7. During

`During(A,B)`

means the temporal extent/time of A is contained within interval/event B.

Typed examples:

- During(Event, TimeInterval)
- During(TimePoint, TimeInterval)
- During(EventA, EventB)

During is temporal containment, not Before/After.

## 8. Time intervals

A TimeInterval can be constructed from:

- Begin point;
- End point;
- Begin + Duration;
- explicit named/reference interval.

Conceptual constructors:

`Interval(start, end)`

`IntervalFor(start, duration)`

Final lexical names may differ.

## 9. Happen

`Happen(EventSpec, TimeInterval?) -> Proposition`

means at least one concrete Event matching the EventSpec occurs within the specified interval.

Ordinary conversation may use a discourse temporal interval.

Objective magical conditions require an explicit or formally provided evaluation interval.

## 10. Event references

When a Command executes, resulting Event identities can be exposed as EventRefs.

Result-binding grammar may bind them:

`!Move(...):event [e].`

Then later structure within the same Command can use:

- Begin($e)
- End($e)
- Duration($e)

The exact surface binding syntax remains grammatical and zero-mana.

## 11. Sequence

`Sequence(E1,E2,...)`

requires event order:

E1 before E2 before ...

The execution specification already defines stepwise commit behavior.

Sequence order is semantic and therefore the Sequence Operator is meaning-bearing.

## 12. Again

The English idea "again" requires a reference standard: which prior event counts as the same action?

Therefore a generic magical `Again` is contextual and should not be primitive executable control.

Use explicit:

- Repeat(count, EventSpec);
- Happen with prior EventRef;
- repeat-after a specified matching criterion.

An ordinary-language Again rune may exist with discourse context.

## 13. Repeat

`Repeat(count, EventSpec)`

is finite exact recurrence.

Count must be a nonnegative integer.

Default recurrence is sequential unless another frame states otherwise.

Timing between iterations must be either:

- immediate next-step;
- explicitly supplied period/delay;
- determined by the Process definition.

A periodic repeat therefore needs a Period/Delay quantity.

## 14. Period

Add candidate temporal scalar:

`Period(recurrence) -> Quantity<Time>`

or a grammatical Repeat frame:

`Repeat(count, EventSpec, interval-between)`.

This prevents "repeat ten times" from ambiguously meaning simultaneous or once-per-second.

## 15. Former

`Former` is a temporal predicate Operator.

For a state-predicate Proposition P at subject x:

`Former(P)`

means:

1. P held during at least one relevant interval before Now/reference time;
2. P does not hold at the reference time.

This makes FormerLife distinct from merely NotLife.

The relevant historical interval/domain may need explicit scoping for magic.

## 16. Always

`Always(P, interval/domain) -> Proposition`

means P holds throughout the supplied temporal domain under the model's continuity/discrete checking semantics.

There is no free implicit "for all eternity" in magical execution.

An unbounded interval can be explicitly represented if the ontology/magic supports it.

## 17. Never

`Never(P, interval/domain)`

normalizes to:

`Not(SomeTime(interval, P))`

or equivalent temporal quantification.

A conventional Never rune can exist as lexical compression.

## 18. Scheduled events

A command can constrain an EventSpec to a TimePoint/Interval.

Prefer a dedicated temporal attachment concept such as:

`When(EventSpec, TimePoint/Interval)`

rather than overloading spatial At.

This can produce a scheduled EventSpec/Command if the magic engine supports deferred execution.

Deferred execution generally creates an active Magic state similar to Trigger/Persist until activation.

## 19. Trigger versus scheduled time

A scheduled command activates based on a temporal condition.

Trigger activates based on an arbitrary Proposition transition.

A time Trigger may normalize to scheduled execution, but the language can keep both common constructions if useful.

## 20. Temporal reference frames

Calendars, dates, named eras, and units are Information/conventional reference systems mapped to TimePoints.

They are not themselves fundamental time.

The full language can support calendar vocabulary without changing event semantics.

## 21. Yesterday/tomorrow

The earlier failure to express Yesterday is solved through temporal measurement/reference.

A conversational semantic molecule can define:

- previous calendar day relative to Now;
- next calendar day relative to Now.

Magic should use the registered calendar/day definition rather than assuming a 24-hour rolling interval unless that is what the root specifies.

## 22. Tense

Cuspell does not need obligatory tense morphology.

Assertions about Processes use Happen plus temporal relations/references.

Ordinary language may lexicalize common tense shortcuts later.

Magic normalizes them to explicit temporal semantics.

## 23. Historical information and access

A Proposition about the past can be objectively true even if a speaker does not know it.

Whether a magical Command/Question can evaluate hidden historical truth is an Information-access/capability rule, not a temporal-semantic ambiguity.

## 24. Temporal contradiction

Examples of contradictory constraints:

- A strictly Before B and A strictly After B;
- negative Duration where Duration is nonnegative;
- one Event required wholly During two disjoint intervals when no split-event model applies.

These are well-typed constraint failures.

## 25. Result

Time semantics now distinguish:

- time point;
- interval;
- event description;
- actual Event;
- duration;
- order;
- containment;
- recurrence;
- historical state.

This removes the need to rely on English tense or vague words such as Again for magical precision.
