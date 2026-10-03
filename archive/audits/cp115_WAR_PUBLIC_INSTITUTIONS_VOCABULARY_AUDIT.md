# Checkpoint 115 — War and Public-Institutions Vocabulary Audit

_Status: fifth balanced civilization-vocabulary batch + one semantic repair_

## Purpose

Checkpoint 106 identified war/military and public institutions as another visibly uneven domain.

Before this pass Cuspell already had:

- Weapon;
- Sword;
- Attack/Stab/Bite and general Cause/Damage/Life machinery;
- Law;
- Court;
- Contract;
- Leader;
- Settlement;
- Market;
- School;
- Hospital;
- Sailor/Crew/Captain;
- ownership, permission, obligation, responsibility, group membership, and control relations.

But ordinary civilization vocabulary still lacked Soldier, Army, Armor, Shield, common ranged/pole weapons, Prison, Judge, Polity, Government, and Citizen.

This audit also checks whether those nouns expose missing productive social/legal semantics.

## Main semantic finding — Authority

The audit exposes one genuine semantic distinction:

`Authority(holder,scope) -> StateProposition`

means that the holder has recognized social/institutional standing to issue or validate binding rules, permissions, obligations, or decisions for the supplied scope.

### Why Control is not enough

`Control(A,B)` is factual persistent control/manipulability.

Authority and Control can diverge:

- a kidnapper may Control a captive without legitimate Authority;
- a judge may have Authority over a case without physically controlling the participants;
- a government can have recognized Authority over a territory while failing to control part of it;
- an occupying force can Control a place whose lawful government retains recognized Authority.

Therefore Authority is not a stylistic synonym for Control.

### Why Permitted is not enough

`Permitted(agent,event,authority?)` records permission for an EventSpec.

Being permitted to do one thing does not imply standing to make binding decisions for others or for a public scope.

Authority is the higher-order/social status that may ground permissions and obligations in a world model, but it is not reducible to any one permission fact.

### Why Own/Have/Cause are not enough

Ownership, possession, and causation also fail to preserve legitimacy/jurisdiction:

- owning land need not confer governmental authority;
- holding an object does not confer authority over its users;
- causing an outcome does not make the causer an authorized decision-maker.

**Result: add Authority as one semantic primitive candidate.**

World ontology supplies:

- jurisdiction;
- legitimacy/source;
- delegation;
- succession/appointment;
- revocation;
- conflicts/precedence.

## Accepted military vocabulary

### Soldier

Old Name:

`«AttackObligated«Know«MoveLifeThing»»»`

Frozen cost: **6**.

World Kind: `core.roles.soldier`.

The historical spelling foregrounds a Human under organized combat duty. The frozen classifier can include defensive/noncombat military service where the setting classifies it as Soldier.

### Army

Old Name:

`«Group«AttackObligated«Know«MoveLifeThing»»»»`

Frozen cost: **7**.

World Kind: `core.social.army`.

An Army is a persistent organized military Group, not a Battle Event.

### Armor

Old Name:

`«PreventAttack««Know«MoveLifeThing»»SurfaceThing»»`

Frozen cost: **8**.

World Kind: `core.artifacts.armor`.

Historical wording foregrounds attack-resistant/protective Clothing.

### Shield

Old Name:

`«PreventAttack«UseThing»»`

Frozen cost: **4**.

World Kind: `core.artifacts.shield`.

Historical wording foregrounds a defensive Tool.

### Spear

Old Name:

`«HighLengthSharp«EndLife«UseThing»»»`

Frozen cost: **7**.

World Kind: `core.artifacts.spear`.

Historical wording foregrounds a long sharp Weapon.

### Bow

Old Name:

`«DistanceAttack«EndLife«UseThing»»»`

Frozen cost: **6**.

World Kind: `core.artifacts.bow`.

The historical wording means roughly “distance-attack weapon”; the frozen classifier distinguishes bows from slings, crossbows, thrown weapons, or fantasy ranged weapons.

### Arrow

Old Name:

`«SharpMoveAttackThing»`

Frozen cost: **4**.

World Kind: `core.artifacts.arrow`.

The etymology foregrounds a sharp moving attack object. Exact projectile construction is world ontology.

## Accepted detention/legal/public vocabulary

### Prison

Old Name:

`«PreventMove«Know«MoveLifeThing»»«JoinedInThing»»`

Frozen cost: **9**.

World Kind: `core.institutions.prison`.

Prison is a persistent detention institution/facility Entity.

The historical wording foregrounds a Building that restricts human movement, but exact detention/security/legal rules are world-defined.

### Prisoner

Old Name:

`«In«PreventMove«Know«MoveLifeThing»»«JoinedInThing»»«Know«MoveLifeThing»»»`

Frozen cost: **14**.

World Kind: `core.roles.prisoner`.

The etymology historically ties Prisoner to being a Human in a Prison. This is not live classification: a prisoner outside the facility for transport, labor, medical care, or escape does not automatically cease to be a Prisoner.

### Judge

Old Name:

`«Authority«EvaluateObligatedGroup»«Know«MoveLifeThing»»»`

Frozen cost: **8**.

World Kind: `core.roles.judge`.

Historical wording foregrounds a Human holding Authority in a Court.

### Polity / state

Old Name:

`«Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»»`

Frozen cost: **9**.

World Kind: `core.institutions.polity`.

This is the broad political-community concept. Exact territory, sovereignty, citizenship, constitutional form, and recognition are world ontology.

### Government

Old Name:

`«Authority«Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»»Group»`

Frozen cost: **11**.

World Kind: `core.institutions.government`.

Government is the governing institution/group exercising recognized Authority for a Polity or comparable public scope.

Government is deliberately distinct from the Polity itself.

### Citizen / member of polity

Old Name:

`«Member«Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»»«Know«MoveLifeThing»»»`

Frozen cost: **14**.

World Kind: `core.roles.citizen`.

Exact citizenship rights, duties, inheritance/naturalization rules, and eligibility are world-defined.

## No Imprison / Confined / Free root yet

The usefulness of Prison/Prisoner does not prove that one universal confinement process/state is already formalized.

Physical confinement may involve:

- current spatial containment;
- inability to move through exits/boundaries;
- barriers;
- control;
- prevention;
- restraints.

Legal detention additionally involves:

- law;
- authority;
- permission/forbiddance;
- obligations/status.

Checkpoint 115 therefore does not add `Imprison`, `Confined`, `Free`, or `Escape` simply because English lexicalizes them.

If later corpus or magical execution repeatedly needs an exact general confinement relation/process, audit it on its own truth conditions.

## Event-category classifier pressure

This domain exposes a separate **world-model/type-system pressure**.

Concepts such as:

- Trial;
- Battle;
- War;
- Crime;
- Punishment;

are naturally categories of Events/EventSpecs or extended occurrences/processes.

The current common world-concept layer overwhelmingly uses:

`semantic_type: Kind`

and ordinary Kind predication currently classifies Entities.

Therefore checkpoint 115 does **not** register Trial/Battle/War as fake persistent Entities merely to fit the existing Kind system.

A particular Event can already have a New Name because the Name relation can refer to non-Entity semantic values.

What is still missing is a regular generic mechanism equivalent to:

> this Event/EventSpec belongs to registered event category X.

This is not evidence that Trial, Battle, War, etc. each need a semantic root.

It is a typed world-classification problem.

Checkpoint 115 records the pressure and leaves it open for the next event-heavy vocabulary domains—especially ritual, performance, festival, and calendar events.

## Market ontology cleanup

Checkpoint 106 also flagged Market because its old description said “gathering or institution,” mixing event and persistent-Entity readings.

Checkpoint 115 narrows the core Market concept to:

> persistent trading institution or trading-site Entity.

A market-day gathering/event is separate.

The existing Market Old Name Sign/cost does not change.

This follows the same cleanup principle previously applied to Farm.

## Deliberately deferred political/military vocabulary

The core does not automatically add:

- king/queen/emperor;
- noble/duke;
- senator;
- officer/general;
- police;
- navy;
- cavalry/infantry;
- militia;
- specific military ranks;
- specific political offices;
- constitution;
- tax;
- treaty;
- citizenship grades.

These are common in some civilizations but highly institution-specific. They belong in world/history packages unless later evidence shows a sufficiently broad cross-setting concept.

## Religion boundary

Temple, shrine, priest, ritual, ceremony, sacrifice, festival, music, dance, art, performance, and related vocabulary are deferred to the next **art/ritual/shared-culture** batch.

This keeps religious institutions and event-heavy ritual vocabulary together, where the event-category classifier issue can be audited directly.

## Inventory effect

Before checkpoint 115:

- 211 registered base entries;
- 130 semantic primitive candidates;
- 55 formal constructors;
- 264 semantic frames;
- 48 multi-frame entries;
- 169 Old Names;
- 162 core world concepts.

After checkpoint 115:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **182 Old Names**;
- **175 core world concepts**.

Frame distribution becomes:

- 22 zero-frame entries;
- 142 one-frame entries;
- 35 two-frame entries;
- 13 three-or-more-frame entries.

Old Name meaning distribution becomes:

- **175 concept/Kind Old Names**;
- **6 Unit Old Names**;
- **1 parameterized expression Old Name**.

## Regression effect

Checkpoint 115 adds:

- 4 Authority semantic tests;
- 5 war/public-institution vocabulary tests.

Expected total:

**640 tests**.

## Result

War/public-institution vocabulary is now substantially more balanced.

The audit also:

- adds the independently necessary Authority relation;
- keeps Prison/Prisoner from smuggling in an untested confinement primitive;
- fixes Market's Entity/Event ambiguity;
- identifies generic Event-category classification as the next important world-model pressure.

The next balanced civilization domain is:

**art / ritual / shared culture**.

That pass should audit temple, shrine, priest, ritual/ceremony, sacrifice/offerings, music, song, instrument, dance, painting/image, sculpture, story, theater/performance, game/sport, festival/feast, and related shared-cultural vocabulary while addressing the Event-category classifier pressure rather than forcing occurrence categories into Entity Kinds.
