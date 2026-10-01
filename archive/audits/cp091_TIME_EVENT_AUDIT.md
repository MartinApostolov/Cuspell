# Time and Event-Occurrence Second-Pass Audit

_Status: checkpoint 91 — family-level reduction experiment complete; no net-safe reduction found_

## Scope

This audit tests the compact four-root temporal family:

- `Before`
- `During`
- `Happen`
- `Simultaneous`

The family is already heavily compressed. Earlier passes removed:

- `After` by reversing `Before`;
- `TimeOverlap` into the general typed `Overlap` relation;
- `Sometimes` into `Happen`;
- `Present` / `Ongoing` into `During`;
- `Past` / `Future` into `Before`;
- `Always` / `Never` into Proposition + TimeInterval `During`;
- `Stop` into the EventSpec-output frame of `End`;
- `Duration` into temporal `Extent(Event)`.

The question is whether the four surviving roots still duplicate one another or can
be reconstructed exactly from `Begin`, `End`, `Equal`, `Overlap`,
`Interval`, and ordinary logic.

## Reduction rule

Temporal reductions must preserve:

- strict vs non-strict ordering;
- event identity vs EventSpec occurrence;
- point vs interval vs concrete-event typing;
- full containment vs mere overlap;
- occurrence vs being active across a target;
- exact equality vs contextual/declared simultaneity tolerance.

A shorter expression is not a valid reduction if it changes any of those cases.

## Experiment A — Simultaneous as Overlap

This fails immediately.

`Overlap(Event A, Event B)` only says the temporal extents intersect.

Two long events can overlap for a short period while starting and ending at very
different times. That is not the current Simultaneous relation.

Likewise interval overlap does not imply equal timing.

**Result: Simultaneous is not Overlap.**

## Experiment B — Simultaneous as Equal

The TimePoint frame is individually compositional:

`Simultaneous TimePointA TimePointB`

can be expressed as:

`Equal TimePointA TimePointB`

when exact equality is the intended timing standard.

That does **not** remove the root because its Event frame remains semantically
stronger/different.

The current temporal specification defines Event Simultaneous in terms of equal
relevant timing under a declared temporal tolerance/profile. The core does not yet
have a reusable temporal-distance/tolerance relation that can reconstruct that
Event-level meaning from `Begin` / `End` / `Equal`.

Possible replacements all change semantics:

- `Equal Begin A Begin B` means equal start points only;
- `And {Equal Begin A Begin B,Equal End A End B}` means exact coextensive timing,
  which is stronger than a tolerance-based simultaneous classification;
- `Overlap A B` is weaker;
- `Not Before A B` and `Not Before B A` are broad non-ordering conditions and
  include ordinary overlap.

Adding a new `TemporalTolerance` or `SimultaneousThreshold` primitive solely to
replace Simultaneous would not lower the inventory.

**Result: retain Simultaneous.**

The point frame could be treated as derived surface sugar later, but that would not
change the root count while the Event relation remains primitive.

## Experiment C — Before as Begin/End comparison

For concrete Events the specification says:

`Before(Event A, Event B)`

means the relevant end of A is strictly before the relevant beginning of B.

That suggests a conceptual expansion:

`Before End A Begin B`

but the inner `Before(TimePoint,TimePoint)` is still the same primitive temporal
ordering relation. It does not eliminate Before.

Trying to replace TimePoint Before with generic numeric `More`/reversal is also not
currently exact:

- TimePoint is a temporal semantic type, not merely a scalar Quantity;
- no canonical numeric origin/unit is required for TimePoint ordering;
- the language deliberately lets temporal models supply an ordering without forcing
  absolute timestamp arithmetic.

`Not Before` cannot supply the reverse relation because equality and overlap/non-
ordering cases remain.

**Result: retain Before as the primitive strict temporal order.**

## Experiment D — During from Before boundaries

For a concrete Event contained within a concrete Event or TimeInterval, one could
mathematically characterize containment using endpoint inequalities.

The current language does not have a single non-strict temporal-order primitive.
Using only strict `Before` and `Equal` would require several boundary cases and
typed interval endpoint projections.

More importantly, `During` now has semantic frames beyond concrete interval
containment:

- `During(EventSpec, TimePoint)` — a matching occurrence is active at the point;
- `During(EventSpec, TimeInterval)` — a matching occurrence is active across the
  supplied interval;
- `During(Proposition, TimeInterval)` — the proposition holds throughout the
  interval.

Those are the reusable semantics that already absorbed Present, Ongoing, Always,
Never, and Whenever-style wrappers.

A boundary-only rewrite would therefore either lose these frames or require a new
generic temporal-holding relation equivalent to During.

**Result: retain During.**

## Experiment E — Happen from During

`Happen(EventSpec, interval?)` means that at least one matching concrete Event
occurs in the relevant temporal domain.

`During(EventSpec, target)` is stronger/different: a matching occurrence is active
across the supplied point or interval.

An event can happen within an interval without spanning that interval.

Examples:

- a one-second flash can `Happen` during a one-hour interval;
- that flash does not satisfy the EventSpec+interval `During` reading for the whole
  hour.

Conversely `During E Now` states current activity, not merely that E occurred at
some point in a broader contextual domain.

**Result: retain Happen and During separately.**

## Experiment F — Happen as existential Event quantification

Conceptually one could say:

> there exists a concrete Event matching EventSpec E in interval I.

But the language currently has no generic EventSpec-to-concrete-Event matching
relation exposed as an independent root. `Happen` is exactly the compact semantic
bridge from an EventSpec pattern to existential occurrence.

Introducing a `Matches(Event,EventSpec)` relation plus quantification would add a
new semantic primitive and produce a longer basis rather than reduce it. Such a
matching relation might become independently useful later, but it is not currently
present.

**Result: retain Happen.**

## Shared-basis count test

A proposed generic temporal system would need at least:

- strict temporal order;
- temporal containment/holding;
- EventSpec existential occurrence;
- event simultaneity/tolerance classification.

Those are the four distinctions already represented by the current roots.

`Begin`, `End`, `Interval`, `Equal`, and `Overlap` are useful supporting
constructors/relations but do not eliminate any one of those distinctions without
adding equivalent new machinery.

**Result: no net reduction.**

## Count result

No root is removed and no new temporal wrapper is added.

Current inventory remains:

- **206 registered base entries**;
- **126 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The time/event-occurrence family remains **4 semantic primitive candidates**.

## Design conclusion

This family has already undergone most of its useful compression. The surviving four
roots are a small orthogonal basis:

- `Before` — strict temporal order;
- `During` — temporal containment/holding/activity across a target;
- `Happen` — existential occurrence of an EventSpec;
- `Simultaneous` — equal/relevantly simultaneous timing, distinct from overlap.

The next second-pass family should be the four **operational/body-state** roots:
`Awake`, `Sleep`, `Open`, and `Locked`.
