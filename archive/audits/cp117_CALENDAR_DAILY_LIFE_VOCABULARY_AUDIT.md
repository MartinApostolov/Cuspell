# Checkpoint 117 — Calendar and Daily-Life Vocabulary Audit

_Status: final planned balanced civilization-vocabulary batch_

## Purpose

Checkpoint 106 identified calendar/daily-life vocabulary as the last major ordinary lexical gap after the earlier anatomy, environment, agriculture/material, craft/transport, war/public-institution, and art/ritual batches.

The existing semantic language already had strong time mechanics:

- `TimePoint`;
- `TimeInterval`;
- `Now`;
- `Interval(start,end)`;
- `IntervalFor(start,duration)`;
- `Begin` / `End` / `Extent`;
- `Before`, `During`, `Overlap`, `Simultaneous`;
- `Happen`, `When`, `Repeat`, and Rate;
- a Calendar world Kind;
- a Clock world Kind;
- the canonical DurationUnit.

Checkpoint 116 also generalized registered world Kinds so they can classify explicit semantic domains beyond Entity.

Checkpoint 117 therefore asks whether ordinary words such as day, night, year, season, month, date, and age need new semantic roots or merely historical/world vocabulary.

## Classification result

Accepted as **world Kinds + Old Names**:

1. day/calendar day;
2. night;
3. season;
4. year;
5. month/calendar month;
6. date/calendar date.

No new base semantic entry, type, frame, constructor, Unit, or New Name is required.

## Day / calendar day

Old Name:

`«AwakeSleepExtent»`

Frozen cost: **3**.

World concept:

`core.time.day`

Classifier domain:

`TimeInterval`

The historical spelling foregrounds one waking/sleeping extent. It is not the live day definition.

A world's Day classifier determines:

- civil/astronomical boundaries;
- local reference frame;
- variable or fixed duration;
- how leap/intercalary changes work;
- whether different regions use different day systems.

A Day is not automatically a 24-hour Quantity.

## Night

Old Name:

`«SleepExtent»`

Frozen cost: **2**.

World concept:

`core.time.night`

Classifier domain:

`TimeInterval`

The historical spelling foregrounds a sleeping extent.

The live world classifier may instead use astronomical darkness, cultural convention, light thresholds, or another objective setting rule.

Night need not be exactly complementary to Day.

## Season

Old Name:

`«ChangeHeatExtent»`

Frozen cost: **3**.

World concept:

`core.time.season`

Classifier domain:

`TimeInterval`

The historical spelling foregrounds changing heat/climate.

The live classifier may instead use:

- orbital geometry;
- rainfall;
- ecology;
- magical cycles;
- agricultural convention;
- administrative calendars.

A world may have no Seasons.

## Year

Old Name:

`«Repeat«ChangeHeatExtent»»`

Frozen cost: **4**.

World concept:

`core.time.year`

Classifier domain:

`TimeInterval`

The later historical word is built from Repeat + Season.

The live world classifier decides whether a Year is astronomical, orbital, civil, ritual, or otherwise defined.

The Old Name does not require a Year to contain a fixed number of Seasons.

## Month / calendar month

Old Name:

`«Part«Repeat«ChangeHeatExtent»»`

Frozen cost: **5**.

World concept:

`core.time.month`

Classifier domain:

`TimeInterval`

The historical spelling treats Month as a subdivision of Year.

A world need not have Months at all.

Where Months exist, their:

- number;
- duration;
- lunar relation;
- leap/intercalary behavior;
- naming;

are world/calendar data.

## Date / calendar date

Old Name:

`«Name«RepeatDuration«PersistSignThing»»`

Frozen cost: **6**.

World concept:

`core.information.date`

Classifier domain:

`Information`

A Date is not a TimePoint itself.

It is conventional calendar Information that identifies/describes temporal position or interval under a particular calendar/reference system.

A world maps Date Information and/or its Sign/Name to:

- a TimePoint;
- a Day/other TimeInterval;
- or whatever precise temporal reference the calendar defines.

Different calendars can provide different Date Information for the same underlying time.

## Calendar periods are not Units

Checkpoint 117 keeps a hard distinction between:

- a **calendar category** such as Day/Year;
- a **Quantity:Time Unit** such as a conventional “day” measurement.

The core Day/Year Old Names classify TimeIntervals.

They do not create a hidden fixed conversion to `DurationUnit`.

If a world wants a conventional time Unit called “day”, “hour”, “year”, etc., its Unit registry must state the exact conversion separately.

This prevents Earth assumptions from entering generic Cuspell.

## Today

No `Today` root is required.

With the accepted Day classifier, the current calendar day is compositionally selectable:

`Unique Collect d:TimeInterval And {«AwakeSleepExtent» $d,During Now $d}`

assuming the active calendar/world ontology gives one unique Day containing Now.

This is ordinary typed reference construction, not magical inference from English.

## Yesterday and tomorrow

No `Yesterday` or `Tomorrow` semantic root is required.

Once today is selected:

- yesterday is the Day whose End equals Begin(today);
- tomorrow is the Day whose Begin equals End(today).

This remains correct when Day durations vary.

Historical lexical compression can be added later if repeated corpus pressure warrants it.

## Age

Checkpoint 106 listed age as likely daily-life vocabulary.

Checkpoint 117 concludes that **Age should not become a primitive root or world Kind**.

An age value is an elapsed `Quantity:Time` relative to a chosen origin:

`Extent Interval start reference`

For a living person, a civilization may choose:

- birth;
- Begin Life;
- conception;
- legal birth registration;
- another culturally defined origin.

For an artifact it may choose:

- creation;
- completion;
- activation;
- commissioning;
- first use.

Those origins are not universally identical.

Therefore a context-free `Age(subject)` primitive would hide the very choice that makes the result objective.

If the relevant start Event is referenced, then:

`Extent Interval Begin ThisEvent Now`

already yields the elapsed time.

The world may Name/store the appropriate start Event or TimePoint.

Age is therefore **compositional + world/reference data**, not a semantic gap.

## Morning / evening / noon / midnight

These are not added to generic core in checkpoint 117.

They are calendar/day subdivisions whose exact objective boundaries vary strongly by culture, astronomy, latitude, season, and convention.

A world package may register them as TimeInterval/TimePoint world Kinds or New Names where useful.

## Week and similar periods

Week-like periods are explicitly culture-specific.

No universal Week Kind is added.

World/history packages may register:

- week;
- ten-day;
- market cycle;
- work/rest cycle;
- ritual cycle;
- fantasy calendar period;

as local TimeInterval categories and Old/New Names.

## Hours, minutes, seconds

These are primarily **conventional Units**, not generic world Kinds.

A setting may register conventional time Units with explicit conversion to the canonical Time dimension.

No Hour/Minute/Second semantic roots are needed.

## Named calendar vocabulary

The following remain world/history/New-Name data:

- weekday names;
- month names;
- named seasons;
- years/era labels;
- named eras;
- holidays;
- anniversaries;
- birthdays;
- named festivals;
- specific calendar systems.

A particular Date Sign can Name an Information value or directly Name a TimePoint/TimeInterval where the world convention makes that relation appropriate.

## No new time process semantics

The calendar batch does not introduce:

- Pass;
- Wait;
- Age;
- GrowOld;
- Today;
- Yesterday;
- Tomorrow;
- Morning;
- Evening;
- Week.

Existing time ordering, interval, Extent, selection, and world classifier machinery already carries the required distinctions.

## Inventory effect

Before checkpoint 117:

- 212 registered base entries;
- 131 semantic primitive candidates;
- 55 formal constructors;
- 265 semantic frames;
- 48 multi-frame entries;
- 198 Old Names;
- 191 core world concepts.

After checkpoint 117:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

Old Name meaning distribution becomes:

- **197 concept/Kind Old Names**;
- **6 Unit Old Names**;
- **1 parameterized expression Old Name**.

No New Name is added.

## Regression effect

Checkpoint 117 adds seven calendar/daily-life regressions:

- Old Name/root layering;
- recursive historical costs;
- TimeInterval classifier domains;
- Date Information classifier;
- wrong-domain rejection;
- compositional current-Day selection;
- compositional age/elapsed-time behavior.

Expected suite size:

**654 tests**.

## Civilization-audit result

The planned balanced vocabulary expansion from checkpoint 106 is now complete.

The sequence was:

- cp111 — basic anatomy;
- cp112 — natural geography/weather;
- cp113 — food/agriculture/common materials;
- cp114 — craft/manufacturing/transport;
- cp115 — war/public institutions;
- cp116 — art/ritual/shared culture;
- cp117 — calendar/daily life.

The next task is **not another noun batch**.

It is the planned **reduction/redundancy audit** over productive semantic meanings restored or added during the civilization work.

That audit must especially re-check:

- `Authority` against `Permitted`, `Obligated`, Rule/Law, and world-context constructions;
- `Health`, `Pain`, and `Ill` against the now-stabilized state/value system;
- `Male` against the sex-classification design;
- `Rotate` against the spatial/geometric basis.

Old Names that depend on any removed root may be rewritten; they are not untouchable.
