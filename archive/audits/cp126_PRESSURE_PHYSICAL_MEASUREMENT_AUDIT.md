# Checkpoint 126 — Pressure / Physical Measurement Attribute Audit

_Status: post-multibook physical-measurement follow-up_

## Trigger

Checkpoint 125's seven-source corpus pass found one genuinely new language-level pressure point in Jules Verne's _Twenty Thousand Leagues under the Sea_.

The current language can already express:

- Length / axis Extent;
- Mass;
- Volume;
- Density;
- Heat;
- Light;
- time extent;
- Rate;
- multiplication/division/powers of typed quantities;
- comparison and Change over registered AttributeDescriptors.

But it cannot state the exact quantitative meaning:

> the mechanical pressure at this place / of this material or contained system has value q

because there is no Pressure semantic descriptor.

Checkpoint 125 therefore left one explicit question:

> should Pressure become another language-level measured Attribute, or should world packages be allowed to register arbitrary first-class AttributeDescriptors/dimensions?

Checkpoint 126 resolves that question.

## Existing measurement architecture

The current system deliberately separates three things.

### 1. Attribute identity

Examples:

- Mass;
- Heat;
- Density;
- Volume;
- Health;
- Pain;
- Form;
- Phase.

An AttributeDescriptor identifies **which functional value of the subject** is being queried or changed.

### 2. Quantity dimension

Examples:

- Quantity:Mass;
- Quantity:Length;
- Quantity:Density;
- Quantity:Time.

The dimension determines arithmetic compatibility.

### 3. World law/value

The active world determines:

- the actual value of an Attribute for a subject;
- whether the Attribute applies;
- natural causal relations among attributes/events;
- what a magical Change is physically allowed to accomplish.

These layers must not be collapsed.

Checkpoint 86 already established the same distinction for Mass/Heat/Light/Volume/Length:

> replacing Mass with Measure(subject, MassKind) does not reduce semantics if MassKind still has to carry the irreducible meaning "mass".

Pressure must pass the same test.

## Candidate A — derive Pressure from dimensional arithmetic

Pressure has the physical dimension:

`Mass · Length^-1 · Time^-2`.

The existing dimension engine can already derive arbitrary integer-exponent combinations of registered base dimensions.

So a quantity expression such as:

`Mass / (Length · Time^2)`

can be typed as Pressure-dimension.

That is useful, but it does **not** define Pressure.

### Counterexample

Consider two world states that agree on:

- an Entity's Mass;
- its Volume;
- its Density;
- its Form;
- its Heat;
- its Location;
- all currently registered relations/events.

The scalar mechanical pressure inside/on that Entity or at a nearby fluid location can still differ.

Likewise, two different physical values may share the same dimension vector without being the same physical quantity or relation.

Dimensional equality answers:

> can these quantities be added/compared as the same dimension?

It does not answer:

> which physical field/value does this expression denote?

Therefore dimension arithmetic cannot reconstruct the Pressure Attribute identity.

**Result: reject dimensional arithmetic as a complete reduction.**

## Candidate B — Pressure = Force / Area

The language currently has Area but no Force semantic relation/Attribute.

Adding Force merely to define Pressure would add at least one new independent physical meaning before Pressure could be reconstructed.

More importantly, an arbitrary Force/Area quotient still requires:

- which force;
- which oriented surface/contact;
- how the force is distributed;
- whether the desired value is local normal stress, average pressure, fluid pressure, etc.

The Verne pressure case is a local scalar mechanical state, not simply any quotient having the correct units.

A future richer mechanics ontology may relate pressure, stress, force, contact area, momentum flux, and material response.

That future physics does not make the present Pressure distinction disappear.

**Result: no current exact Force/Area reduction.**

## Candidate C — reuse Density / Distribution

Density already has:

- `Density(Entity)`;
- `Density(Distribution,Region)`.

But Density means amount per volume / local distribution density.

Pressure is not the density of a resource merely because both can vary through space.

Reinterpreting `Distribution` as a generic scalar-field container would broaden its current resource-distribution meaning and still require an independent label saying which scalar field is being queried.

That label would be equivalent to Pressure.

**Result: Density/Distribution do not replace Pressure.**

## Candidate D — allow world packages to mint callable AttributeDescriptors

At first glance this would avoid adding a universal rune:

- a world package registers "Pressure";
- gives it a Quantity dimension;
- the parser treats it exactly like Heat/Mass/etc.

Checkpoint 126 rejects that mechanism **for now**.

### Why

World packages currently supply ontology and execution facts, not hidden language primitives.

Allowing package metadata to create a new callable semantic descriptor would:

1. move irreducible linguistic meaning outside the registered language inventory;
2. let a setting add spell-capable semantic vocabulary without the normal rune/Old-Name accounting boundary;
3. make parser typing depend on dynamically injected function signatures;
4. undermine the current New Name rule that naming something does not grant semantic macro expansion;
5. disguise primitive growth rather than actually reduce it.

If Pressure is independently necessary, placing the same independent meaning in a package registry does not make it less primitive.

This is the same anti-cheating principle used throughout root minimization.

World packages **may** and should supply:

- actual pressure values;
- applicability rules;
- material equations;
- gradients;
- phase-pressure relations;
- hydrostatic behavior;
- consequences of changing pressure.

They do not currently create new directly callable language semantics.

**Result: reject generic package-defined callable AttributeDescriptors as the Pressure solution.**

## Candidate E — generic Measure/ValueOf constructor plus descriptor values

A new universal constructor such as:

`Measure(subject, descriptor)`

could technically make descriptor application uniform.

But Pressure would still require an atomic descriptor value meaning Pressure.

Unless several existing descriptor roots can be removed exactly, this would add one formal constructor while preserving the independent descriptor identities.

Checkpoint 86 already warned against this non-reduction.

Checkpoint 126 finds no new evidence that a Measure constructor reduces the current family.

**Result: do not add Measure/ValueOf merely for Pressure.**

## Accepted result — Pressure AttributeDescriptor

Register:

`Pressure`

as one semantic primitive candidate / AttributeDescriptor.

### Query frames

`Pressure(Entity) -> Quantity:Pressure`

where the active world defines an absolute scalar mechanical pressure state for that Entity/material/system.

`Pressure(Location) -> Quantity:Pressure`

for local ambient scalar mechanical pressure.

The Entity frame supports:

- enclosed fluid/gas systems;
- material portions where the world exposes one scalar pressure value;
- other world-defined scalar-pressure carriers.

The Location frame supports:

- water pressure at depth;
- atmospheric/ambient pressure at a point;
- local environmental pressure.

A Region is deliberately not given a direct single-value frame because pressure may vary across a Region. A world/query should select a Location or otherwise state an aggregation/profile explicitly.

## Absolute scalar pressure and sign

The registered Attribute means **absolute scalar mechanical pressure**.

Its registered value domain is nonnegative.

This does not claim that every stress quantity in mechanics is nonnegative.

Signed normal stress, tension, full stress tensors, anisotropic stress, and related mechanics are separate future semantics if corpus/world execution requires them.

The language does not silently encode those as negative Pressure.

## Pressure dimension

Add a named derived dimension alias:

`Pressure = Mass · Length^-1 · Time^-2`.

This adds:

`Quantity:Pressure`

to the registered Quantity type set.

It does **not** add a new base dimension.

The base dimension list remains:

- Length;
- Time;
- Mass;
- Heat;
- Light;
- Confidence.

Pressure therefore participates in the existing dimensional arithmetic system.

A derived Mass/Length/Time expression with the Pressure vector normalizes to `Quantity:Pressure`.

## No PressureUnit Old Name

Checkpoint 126 does not add:

`«PressureUnit»`.

The current Unit design intentionally uses a small canonical set.

A Pressure-valued quantity can be constructed dimensionally from:

- `«MassUnit»`;
- `«LengthUnit»`;
- `«DurationUnit»`;

with ordinary Divide/Multiply/Power.

This preserves the existing rule:

> derived dimensions do not automatically receive independent Unit vocabulary.

A later civilization/world may of course have conventional named pressure units as ordinary measurement vocabulary, but that is a separate naming/conversion question.

## Generic Attribute machinery now works automatically

Because Pressure is an AttributeDescriptor, the existing machinery applies without new grammar:

- `Pressure This`;
- `Pressure Here`;
- `More Pressure Here Zero`;
- `HighPressure This`;
- `ZeroPressure This`;
- `Change This Pressure target!`;
- `BeforeValue Pressure This` in event-local contexts;
- `AfterValue Pressure This`;
- `UnknownValueOf subject Pressure`;
- `UnavailableValueOf subject Pressure`.

No new Change/operator family is introduced.

## Verne corpus closure

The checkpoint-125 technical pressure can now be represented at language level.

The world/execution model still has to supply the actual law connecting such things as:

- depth;
- fluid density;
- gravity/acceleration;
- pressure;
- hull forces/stress;
- physiological effects.

That is intentional.

Cuspell can now **name/query/compare/change Pressure** without pretending to contain a full mechanics simulator in its lexicon.

## Why Force/Energy/etc. are not added now

Pressure does not create a rule:

> every named quantity from physics becomes a rune.

Each future candidate must be audited independently.

Some may be:

- exact arithmetic derivatives;
- event rates;
- relations rather than Attributes;
- world-defined laws;
- structured profiles;
- independently necessary semantic descriptors.

Examples still deferred:

- Force;
- Energy;
- acceleration;
- electric charge;
- voltage;
- current;
- momentum;
- stress tensor.

No conclusion about their root status follows automatically from Pressure.

## Regression additions

Checkpoint 126 adds six Pressure regressions:

1. Entity and Location Pressure query as `Quantity:Pressure`;
2. Mass/Length/Time arithmetic normalizes to the Pressure dimension;
3. no separate PressureUnit is required: existing units compose to a Pressure quantity;
4. dimensional equality does not make the arithmetic expression semantically identical to `Pressure(subject)`;
5. Pressure participates in generic measured/threshold/Change machinery;
6. Change rejects a target with the wrong Quantity dimension.

Suite size rises:

- **673 -> 679 tests**.

## Inventory effect

Checkpoint 126 adds:

- 1 registered base entry: `Pressure`;
- 1 semantic primitive candidate;
- 2 semantic frames;
- 1 multi-frame entry;
- 1 derived named Quantity dimension/type alias.

No Old Name or world concept is added.

New totals:

- **213 registered base entries**;
- **132 semantic primitive candidates**;
- **55 formal constructors**;
- **267 semantic frames**;
- **49 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

## Decision

**ADD Pressure as one independently necessary physical AttributeDescriptor.**

**DO NOT add a new base dimension.**

**DO NOT add PressureUnit.**

**DO NOT add a generic world-package callable-descriptor mechanism from this one case.**

The governing rule is:

> dimension algebra determines Quantity compatibility; a semantic Attribute root is required only when the identity of the queried physical value cannot be reconstructed exactly from existing language meanings.

## Next work

The multi-book round and its Pressure follow-up are now closed.

Return to the planned stabilization sequence:

**define and test beginner Cuspell** before final glyph/rune design.
