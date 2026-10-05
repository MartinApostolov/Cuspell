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
- End(Event) -> TimePoint when a temporal boundary value is expected;
- End(Event) -> EventSpec when the requested meaning is termination of that ongoing concrete Event.
- Extent(Event) -> Quantity<Time>

For instantaneous events, Begin and End may be Equal under the world's time resolution.

There is no separate `Duration` root in the minimized core. The duration of a concrete Event is its Time-valued `Extent(Event)`.

There is no separate `Stop` root in the minimized core. Stopping a concrete ongoing Event is the EventSpec-typed use of `End(Event)`.

## 5. Before and reversed temporal order

`Before` is an ordered temporal Relation.

Typed frames include:

`Before(TimePoint A, TimePoint B)`

meaning A < B.

For Events:

`Before(Event A, Event B)`

means End(A) is strictly before Begin(B), unless a later rules profile deliberately permits touching boundaries.

There is no separate `After` root in the minimized core. “A is after B” is written by reversing the arguments of the same ordering relation:

`Before(B,A)`

This is not equivalent to `Not Before(A,B)`, which is broader.

## 6. Simultaneous and temporal overlap

NotBefore is too broad to mean simultaneous.

Add useful temporal Relations:

`Simultaneous(A,B)`

for equal relevant TimePoints or event timing under a declared tolerance.

`Overlap(Event A, Event B)` or `Overlap(TimeInterval A, TimeInterval B)`

when their temporal extents intersect. `Overlap` is the same general topological relation used elsewhere, with typed temporal frames; there is no separate `TimeOverlap` root.

This is preferable to deriving temporal relations from vague negation or duplicating the same overlap concept by domain.

## 7. During

`During(A,B)`

means the temporal extent/time of A is contained within interval/event B.

Typed examples:

- During(Event, TimeInterval)
- During(TimePoint, TimeInterval)
- During(EventA, EventB)

During is temporal containment, not a Before relation in either argument order.

## 8. Time intervals

A TimeInterval can be constructed from:

- Begin point;
- End point;
- Begin + temporal Extent;
- explicit named/reference interval.

Current constructors are:

`Interval(start, end)`

`IntervalFor(start, duration)`

A TimeInterval also exposes the same temporal-boundary/extent vocabulary used for concrete Events:

- `Begin(TimeInterval) -> TimePoint`;
- `End(TimeInterval) -> TimePoint`;
- `Extent(TimeInterval) -> Quantity<Time>`.

This is important for named or referenced intervals whose original constructor is no longer syntactically present. A speaker can ask for the beginning, ending, or duration of `ThisInterval` directly rather than reconstructing it from hidden history.

These accessors are partial where the requested value does not exist. An explicitly unbounded interval may lack one boundary, and an interval without finite temporal extent does not silently produce a finite Quantity. World/evaluation machinery must report the missing/unavailable value rather than inventing one.

For `Interval(start,end)`, the registered boundaries are the supplied points. For `IntervalFor(start,duration)`, Begin is the supplied start, Extent is the supplied duration, and End is the corresponding world-time point under the time model.

## 9. Happen

`Happen(EventSpec, TimeInterval?) -> Proposition`

means at least one concrete Event matching the EventSpec occurs within the specified interval.

Ordinary conversation may use a discourse temporal interval.

Objective magical conditions require an explicit or formally provided evaluation interval.

## 10. Event references

Concrete Event identities may be exposed through typed event references such as `ThisEvent` / `ThatEvent` or future explicit result-binding machinery.

Once a concrete Event reference E is available, the language can use:

- `Begin E`;
- `End E`;
- `Extent E`.

The current canonical binder syntax (`name:Domain`, `$name`) covers ordinary typed variables, but no player-facing event-result binding shorthand is standardized beyond the currently registered reference forms.

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

A periodic repeat therefore needs an explicit recurrence interval/delay quantity.

## 14. Period

There is no separate `Period` root in the minimized core.

For a recurrence with a well-defined occurrence rate, period is the reciprocal of that rate:

`Divide @ Rate recurrence`

or, with an explicit measurement interval:

`Divide @ Rate recurrence interval`

This yields `Quantity<Time>`. If the occurrence rate is zero or no stable recurrence rate is defined, period is correspondingly undefined rather than silently guessed.

Exact Repeat timing remains supplied directly as the optional Time quantity in:

`Repeat(count, EventSpec, interval-between)`.

This prevents "repeat ten times" from ambiguously meaning simultaneous or once-per-second.

## 15. Relative local time flow

Checkpoint 134 adds `TimeFlow(subject, reference, rate)` as a persistent StateProposition.

The subject is an Entity or Region.

The reference is an explicit SpatialValue anchoring the comparison worldline/frame.

The rate is a nonnegative dimensionless Quantity:Number:

- `@` = local progression matches the reference;
- `Zero` = local progression is stopped relative to the reference;
- greater than `@` = faster local progression;
- between Zero and `@` = slower local progression.

Examples:

`TimeFlow Self ThisRegion @.`

`TimeFlow ThisRegion Self Zero.`

`TimeFlow You Self @@.`

This is not the same as `Rate EventSpec interval`. Event Rate measures how often one selected EventSpec occurs per already-defined time; TimeFlow changes the progression rate of the subject's whole temporally evolving physical/process state relative to a reference.

TimeFlow also does not rewrite TimePoint/TimeInterval definitions, logical truth, or historical ordering. It changes world/execution scheduling and physical/process progression.

Entity TimeFlow applies to temporally evolving processes of that Entity. Region TimeFlow applies to world evolution whose realization footprint lies in the Region, under objective boundary/crossing rules supplied by the world/executor.

Negative factors are excluded. Time reversal would require separate semantics rather than being smuggled in as a negative rate.

## 16. Former-state meaning

There is no separate `Former` root in the minimized core.

For a state-predicate Proposition P, the former-state meaning is:

`Before P Now And Not P`

That means P held in the relevant past domain and does not hold at the reference time. Bare P is the present/reference-time state, so no Present wrapper is needed. This remains distinct from merely `Not(P)`.

The relevant historical interval/domain may need explicit scoping for magic.

## 17. Throughout-time meaning

There is no separate `Always` root in the minimized core.

`During P I`

with P a Proposition and I a TimeInterval means P holds throughout the supplied temporal domain under the model's continuity/discrete checking semantics.

There is no free implicit "for all eternity" in magical execution. An unbounded interval can be explicitly represented if the ontology/magic supports it.

## 18. Never meaning

There is no separate `Never` root in the minimized core.

For a supplied interval/domain, the meaning is represented through temporal quantification, for example:

`Not(SomeTime(interval, P))`

or the direct minimized form `During Not(P) interval`.

## 19. Scheduled events

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

## 20. Calendars and everyday temporal categories

Calendars, dates, named eras, conventional units, and named period categories are world/conventional reference systems over fundamental TimePoints/TimeIntervals.

They are not themselves fundamental time.

Checkpoint 117 registers historical world Kinds for:

- Day / calendar day;
- Night;
- Season;
- Year;
- Month / calendar month.

Each classifies `TimeInterval`.

The world ontology decides the actual boundaries and membership. No universal rule says that every Day has the same duration, every Year has the same number of Days, or every world has Months/Seasons.

These period Kinds are **not Quantity:Time units**. A conventional “day” or “year” measurement unit may be registered separately with an explicit conversion rule when a setting needs one.

Date / calendar date is instead an Information Kind. A Date is a conventional calendar coordinate/description that a world calendar maps to the corresponding TimePoint and/or TimeInterval. Different calendars may describe the same underlying time differently.

### Current calendar period

Existing typed selection can identify the current Day without a new reference root:

`Unique Collect d:TimeInterval («AwakeSleepExtent» $d And During Now $d)`

provided the chosen world/calendar supplies one unique Day containing Now.

### Age

Age does not require a primitive root.

It is elapsed temporal extent from an explicitly selected origin to a reference point:

`Extent Interval start reference`

For a living Entity the relevant origin may be its birth/begin-life event; for an artifact it may be creation, completion, activation, or another world-defined point. Those choices are not universally interchangeable.

When the relevant start Event is already referenced:

`Extent Interval Begin ThisEvent Now`

returns `Quantity:Time`.

A world may store/name the relevant birth/creation Event or TimePoint. The language does not hide that choice inside an ambiguous context-free Age operator.

## 21. Yesterday/tomorrow

Yesterday and tomorrow are derived from the registered Day classifier, not from a universal fixed-duration offset.

Conceptually:

- today is the unique Day containing Now;
- yesterday is the Day whose End equals Begin(today);
- tomorrow is the Day whose Begin equals End(today).

This remains valid even when civil Days vary in duration.

Conversational historical lexicalization may later compress these selections if corpus pressure justifies it. Objective magic still uses the registered calendar/day definition rather than assuming a 24-hour rolling interval.

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

- A strictly Before B and B strictly Before A;
- negative temporal Extent where Event extent is nonnegative;
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
