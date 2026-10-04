# Checkpoint 122 — Typed World-Kind Structural Audit

_Status: post-civilization structural/redundancy audit, target 1_

## Purpose

Checkpoint 116 generalized registered world `Kind` concepts so their members did not have to be Entities.

A Kind concept may declare:

`classifies_types: [...]`

with omission meaning:

`["Entity"]`.

Checkpoint 117 then reused the same mechanism for calendar periods and Date.

Checkpoint 122 re-audits that mechanism after the productive-root audit is complete. The questions are:

1. Is `classifies_types` genuinely needed, or does another type/classifier mechanism already do the same work?
2. Is the default Entity rule still appropriate?
3. Is the field constrained enough to avoid becoming an untyped escape hatch?
4. Does parser behavior consistently use the registered classifier domain?
5. Does validation cover optional world packages as well as core?
6. Are any current world concepts missing or misusing the metadata?
7. Did the later Male/Female audit reveal a need to turn world Kinds into stateful predicates?

## Mechanism remains necessary

Before checkpoint 116, named world Kinds effectively assumed:

`Kind member -> Entity`.

That works for ordinary objects, organisms, artifacts, places, roles, institutions, and persistent phenomena.

It does not work for the accepted categories whose members are other semantic values:

- Ritual, Prayer, Sacrifice, Dance, Performance, Game, Festival -> EventSpec / Event;
- Story, Music, Song, Date -> Information;
- Day, Night, Season, Year, Month -> TimeInterval.

No existing semantic root or generic relation duplicates this metadata.

Creating separate EventKind, InformationKind, and TimeIntervalKind semantic types would multiply type machinery merely to encode the target domain of a category.

Keeping one semantic value type, `Kind`, plus a registered member-domain declaration remains the smaller design.

**Result: retain `classifies_types`.**

## Default Entity remains correct

The registry contains 197 core world Kind concepts.

Most describe ordinary persistent world individuals:

- organisms;
- anatomy;
- materials;
- artifacts;
- geographic features;
- institutions;
- roles;
- resources;
- weather phenomena modeled as identifiable world features/phenomena.

Making every one repeat:

`classifies_types: ["Entity"]`

would add boilerplate without information.

The omitted-field default therefore remains:

`["Entity"]`.

Checkpoint 116 had explicitly written `["Entity"]` on six concepts from its own batch:

- Temple;
- Shrine;
- Priest;
- Musical Instrument;
- Image/Painting;
- Sculpture.

Those declarations are redundant under the rule above.

Checkpoint 122 removes only that redundant metadata.

After cleanup, exactly sixteen core concepts carry explicit non-default `classifies_types`.

## Full registry scan

The core registry was checked concept-by-concept by effective classifier domain.

### EventSpec / Event

Seven concepts intentionally declare:

`["EventSpec","Event"]`

- ritual/ceremony;
- prayer;
- sacrifice/offering;
- dance;
- performance;
- game/sport;
- festival/feast.

These are occurrence categories and should not be forced into Entity ontology.

### Information

Four concepts intentionally declare:

`["Information"]`

- story/tale;
- music/composition;
- song;
- date/calendar date.

Their descriptions explicitly identify abstract content/calendar Information rather than the physical carrier.

### TimeInterval

Five concepts intentionally declare:

`["TimeInterval"]`

- day/calendar day;
- night;
- season;
- year;
- month/calendar month.

These are calendar-period categories, not fixed Units.

### Legacy/default Entity concepts

No older concept was migrated merely because its registry `domain` label sounds abstract.

In particular, `domain: "information"` is organizational metadata, not a semantic type declaration.

Examples such as Record, Book, Map, Calendar, Contract, Letter, Word, Language, and Law predate the typed-category mechanism and currently remain Entity-classifying world Kinds unless their ontology explicitly says otherwise.

This is important for Law.

A first glance at:

`core.information.law`

suggested a possible missing `["Information"]` declaration.

The deeper audit does **not** support making that change automatically:

- its current description is "Law/legal-rule Kind", not "Law Information category";
- its historical construction uses the productive `Rule` Kind;
- the current productive `Rule` Kind itself predicates Entities;
- unlike Story/Music/Date, the accepted source material never states that this Law concept's members are semantic Information values.

Checkpoint 122 therefore does not infer semantic typing from the folder/domain label.

If the project later decides to distinguish abstract law-content Information from embodied/registered Rule/Law entities, that should be a separate ontology decision.

## Parser defect found — named-Kind binders

Ordinary named-Kind predication already used `classifies_types`.

For example:

`«Sequence«MeaningSign»» ThisInformation.`

correctly treats Story as a Kind over Information.

However the binder parser had a separate older rule:

> every named Kind binder binds Entity.

So conceptually:

`s:«Sequence«MeaningSign»»`

was typed as Entity even though Story classifies Information.

Likewise:

`d:«AwakeSleepExtent»`

was typed as Entity even though Day classifies TimeInterval.

This was a real structural inconsistency.

### Repair

Checkpoint 122 centralizes effective world-Kind targets in:

`Language.world_kind_classifies_types(concept_id)`.

Both:

- named-Kind predication;
- named-Kind binder typing

now read the same registered metadata/default rule.

Therefore:

- Story binder -> Information;
- Day binder -> TimeInterval;
- ordinary omitted/default Kind binder -> Entity.

## Multi-domain Kind binders

Event-category Kinds currently classify two distinct sibling types:

`["EventSpec","Event"]`.

Cuspell does not have a union type such as:

`EventSpec | Event`.

Silently binding such a named Kind as:

`SemanticValue`

would be unsound and too weak:

- the variable could not safely be passed where Event is required;
- it could not safely be passed where EventSpec is required;
- broad SemanticValue would hide the actual type distinction.

Choosing one of Event/EventSpec would also be wrong.

Checkpoint 122 therefore makes a multi-domain named-Kind binder fail explicitly with `AmbiguousKindDomain`.

The writer should instead bind the intended semantic type and apply the Kind predicate in the query, for example conceptually:

`e:Event ... «RuleSequence» $e ...`

or:

`e:EventSpec ... «RuleSequence» $e ...`.

This is an honest limitation until the language has a justified union-type/binder mechanism.

Checkpoint 122 does **not** add union types merely for this convenience.

## Validation audit

Core concepts already received basic `classifies_types` validation.

Optional world-package concepts did not.

That meant a future package could contain malformed classifier metadata even though the same data would be rejected in core.

Checkpoint 122 applies one shared validation rule to both.

### Accepted field

The field must:

- appear only on semantic_type `Kind` concepts;
- be a non-empty list when present;
- contain registered semantic type names;
- contain no duplicate target;
- avoid the broad/meta targets:
  - `Any`;
  - `SemanticValue`;
  - `Binder`;
  - `Kind`.

`SemanticValue` is specifically rejected because the world-model specification already says not to broaden a category to SemanticValue merely for convenience.

More specific registered supertypes/subtypes remain available when a future ontology genuinely needs them.

## Why no stateful-Kind generalization is added

Checkpoint 120 showed that migrating Male/Female from persistent Properties to ordinary world Kinds would lose:

`StateProposition`

and therefore their normal Begin/End state behavior.

That does **not** mean checkpoint 122 should make all Kinds stateful.

Kind membership and persistent state predication remain different semantic mechanisms.

Adding stateful Kinds would affect species, artifact categories, roles, institutions, materials, event categories, Information categories, and other ontology far beyond the Male/Female question.

No current evidence shows that such a broad change is needed.

Male/Female therefore remain Properties, and world Kinds remain ordinary category predicates returning Proposition.

## Old Names and New Names

`classifies_types` belongs to the referenced world concept.

It is not encoded by the historical spelling of an Old Name.

Old Name Kind predication therefore uses the referenced concept's classifier domain.

New Names remain ordinary naming/reference data and do not become magical macro expansion.

The existing binder-domain support for a uniquely named Kind also consults its referenced concept when a named Kind is used as a binder domain.

No mana rule changes.

## Regression additions

Checkpoint 122 adds five structural regressions:

1. omitted classifier metadata defaults to Entity without redundant explicit data;
2. Story and Day named-Kind binders receive Information / TimeInterval;
3. a multi-domain Ritual binder fails explicitly rather than pretending to be Entity or SemanticValue;
4. the core registry has exactly the sixteen accepted non-default classifier declarations;
5. optional world-package classifier metadata receives the same broad/meta and duplicate validation as core.

Suite size rises:

- **656 -> 661 tests**.

## Inventory effect

No semantic entry, primitive candidate, constructor, frame, Old Name, New Name, or world concept is added or removed.

Inventory remains:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

Only redundant metadata, parser typing, validation, documentation, and regressions change.

## Result

**KEEP AND TIGHTEN: typed world-Kind `classifies_types`.**

Checkpoint 122 concludes:

1. one Kind + registered member-domain metadata is smaller than separate EventKind/InformationKind/etc. type families;
2. omitted metadata should continue to mean Entity;
3. only sixteen current core concepts require explicit non-default domains;
4. six redundant explicit Entity declarations are removed;
5. named-Kind binders now use the same domain truth as Kind predication;
6. multi-domain named-Kind binders fail honestly until a union binder type is independently justified;
7. package concepts are validated by the same rules as core;
8. no legacy world concept is retyped merely from its organizational domain label;
9. stateful Kinds are not introduced.

## Next structural target

Audit checkpoint 110's parameterized expression Old Names.

Re-check:

- whether the feature duplicates ordinary composition or lexical compounds;
- whether it can hide missing semantics;
- parameter typing and scope/capture rules;
- mana accounting;
- whether optional/default parameters are necessary;
- whether `«TransferHave»` = give is an exact and safe pilot;
- whether the mechanism should remain general, be narrowed, or be removed.
