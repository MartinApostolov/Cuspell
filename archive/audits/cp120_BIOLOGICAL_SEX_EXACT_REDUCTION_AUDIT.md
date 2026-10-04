# Checkpoint 120 — Biological-Sex Exact-Reduction Audit

_Status: post-civilization reduction/redundancy audit, target 3_

## Purpose

Checkpoint 108 added positive `Male` alongside the already-existing `Female` Property because:

`Male X`

is not exactly:

`Not Female X`.

Checkpoint 120 re-tests that decision after later Cuspell gained a stronger Attribute model and typed registered world-Kind classification.

The candidates are:

1. one Property plus logical negation;
2. a universal typed Sex attribute/value family;
3. world-Kind/classifier data + Old Names;
4. the current two independent positive Properties.

The goal is exact semantic reduction, not enforcing Earth biology or preserving the old design by inertia.

## Current semantics

Current productive meanings are:

`Male(Entity) -> StateProposition`

and:

`Female(Entity) -> StateProposition`.

Both are:

- PropertyDescriptors;
- positive classifiers;
- persistent state predicates;
- world-ontology grounded;
- non-contextual.

The core deliberately does **not** declare them:

- logical complements;
- universally exhaustive;
- universally mutually exclusive;
- sufficient to model every biological or social category.

## Candidate 1 — define one through Not

This still fails exactly.

`Not Female X`

means only that Female classification is false.

That allowed set can contain:

- Male entities;
- entities satisfying another biological classification;
- entities for which neither positive classifier applies;
- entities in transformed/atypical states;
- other setting-defined cases.

Likewise `Not Male X` does not positively identify Female.

The existing regression cases correctly permit:

- Male + Female;
- Not Male + Not Female;
- Male + Not Female;
- Female + Not Male.

A particular world may constrain these combinations. The core language must not manufacture those constraints from Boolean negation.

**Result: negation is not converse.**

## Candidate 2 — Sex attribute/value family

A tempting normalized design is:

`Sex(Entity) -> SexValue`

with Male/Female as family values.

This is useful in a world whose biology really is one single-valued exclusive axis.

It is not a smaller universal core representation.

### It adds machinery

The current design has two positive meanings.

The attribute design requires at least:

- a `Sex` AttributeDescriptor;
- Male value/classifier semantics;
- Female value/classifier semantics.

So it does not reduce the semantic alphabet.

### A functional Attribute imposes metaphysics

Cuspell's Attribute model is functional: the selected subject has a value of the Attribute's output type.

A simple single-valued Sex axis would therefore push toward one value at a time.

That is stronger than the current semantics, which intentionally permit worlds where:

- both classifiers apply;
- neither applies;
- additional categories exist;
- classification changes or overlaps according to setting biology.

A set-valued Sex profile could avoid some of this, but would add further structured-value machinery merely to replace two already-clear predicates.

### Property-family machinery does not save the reduction

Phase works well as an exclusive family because the underlying world semantics justify a Phase Attribute and mutually exclusive values for a selected homogeneous subject.

No equally universal biological-sex family rule has been established for every Cuspell world.

**Result: a Sex attribute/value family is not a reduction and would overcommit the core ontology.**

## Candidate 3 — world Kinds + Old Names

Checkpoint 116 makes this alternative genuinely worth re-testing.

Male and Female are world-grounded biological classifications, so one could imagine:

- `core.biology.male` Kind;
- `core.biology.female` Kind;
- historical Old Names for each;
- no productive Male/Female roots.

This preserves positive category membership and avoids binary negation.

However it is **not type-equivalent under the current language**.

### Current world-Kind predication

A Kind-valued Old Name used as a classifier produces ordinary:

`Proposition`.

This is appropriate for registered category membership.

### Current Male/Female properties

Male/Female produce:

`StateProposition`.

Because they are persistent state predicates, the current language supports transitions such as:

`Begin Male X`

`End Male X`

`Begin Female X`

`End Female X`.

This does not require every world to permit such a biological transition magically. It means the language can describe the beginning or end of the classification when the world model says such a transition is coherent.

Migrating to ordinary world Kinds would silently remove that semantic capability.

### Could world Kinds be made stateful?

Possibly, but that would be a new structural mechanism.

It would affect more than biological sex:

- roles;
- statuses;
- institutions;
- species/taxa;
- artifact categories;
- other mutable or immutable Kinds.

Checkpoint 120 does not introduce a generalized stateful-Kind system merely to save two roots. That mechanism should be audited on its own if future pressure shows it is broadly useful.

### Old Name dependency cost is not the deciding factor

Current historical vocabulary uses Female directly in:

- Goddess;
- Milk.

Those Old Names are design-stage and could be rewritten if the semantic reduction were valid.

They therefore do **not** justify keeping Female by themselves.

The reduction fails first on semantics/type behavior.

**Result: ordinary world Kinds are not exact replacements today.**

## Candidate 4 — independent positive Properties

The current representation preserves all required distinctions with the smallest already-working mechanism:

- Male is positive;
- Female is positive;
- neither implies the negation of the other;
- world ontology decides membership;
- both remain persistent StatePropositions;
- Begin/End can describe classification transitions;
- social/cultural gender categories are not silently collapsed into these biological classifiers.

No additional type family or structural classifier feature is required.

## Regression change

Checkpoint 120 adds one regression test covering the already-declared persistent-state behavior:

- Begin Male;
- End Male;
- Begin Female;
- End Female.

This protects the exact semantic distinction that makes ordinary world-Kind migration non-equivalent.

The executable suite therefore rises from **654 to 655 tests**.

## Result

**KEEP AS IRREDUCIBLE SEMANTIC BASIS:**

- `Male`;
- `Female`.

This is not a claim that every world has exactly two biological categories.

It is the opposite: the two roots are independent positive classifiers precisely so the language does not encode a universal exhaustive binary.

World packages may:

- make them mutually exclusive;
- allow overlap;
- add other categories;
- define transformed/developmental states;
- omit their applicability for some entities.

The core supplies the two broadly reusable positive meanings without dictating the full biology.

Inventory remains:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

Only the regression count changes to:

- **655 tests**.

## Next reduction target

Re-test checkpoint 114's:

`Rotate`

against Move, CoordinateFrame/Direction, Offset/geometry, and constrained movement of Parts.

After Rotate, audit the structural additions:

- typed world-Kind `classifies_types`;
- parameterized expression Old Names.
