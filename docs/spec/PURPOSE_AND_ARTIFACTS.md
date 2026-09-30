# Purpose, Function, and Artifact Kinds

_Status: working specification v0.1_

This file resolves purpose/function semantics used by Tool, Weapon, Container, Door, House, Sword, Food, Medicine, and similar artifact Kinds.

## 1. Generic `For` is too broad for magic

English "for" can mean:

- purpose;
- beneficiary;
- destination;
- exchange;
- duration;
- representation.

Therefore a generic magical `For` should not carry all English uses.

Recommended treatment:

- keep a conversational For linker only if desired;
- magical/formal expressions use typed relations below.

## 2. Purpose

`Purpose(entity/process/design, goal) -> Proposition[state/context relation]`

relates something to an intended function/goal under a recognized design/social context.

The goal may be:

- EventSpec type;
- State/Proposition;
- beneficiary-oriented outcome.

Purpose is not the same as current Use.

## 3. DesignedFor

For objective artifact classification, use a stronger registered relation:

`DesignedFor(artifact/design, function-profile) -> Proposition`

This means the artifact's recognized construction/design profile is organized for the function.

A rock temporarily used to strike something does not become DesignedFor striking merely because it was used once.

## 4. Use

`Use(agent, instrument, goal/EventSpec) -> EventSpec`

`Use(event-or-EventSpec, instrument) -> Proposition`

means the agent intentionally employs instrument toward the goal.

The three-argument Use form is an Event. The two-argument form is the instrument participant relation formerly written `Using`.

DesignedFor/Purpose are persistent design/social relations.

## 5. Beneficiary

`Beneficiary(EventSpec/Event, entity) -> Relation`

marks who is intended to benefit from the event.

This is separate from Purpose.

## 6. Tool

A Tool is an artifact Kind satisfying a registered design relation such as:

> an Entity constructed/organized to serve as an instrument in one or more Processes.

The exact superclass "artifact" may be setting-specific, but Tool is function/design-based.

## 7. Weapon

A Weapon is a Tool/artifact whose registered design function includes causing selected kinds of Damage/incapacitation to a target.

Actual current use need not match design.

Therefore:

- a sword used as decoration can remain Weapon;
- a chair used once to cause Damage does not automatically become Weapon by Kind.

## 8. Container

A Container is a structural artifact whose design function includes maintaining other Entities in an interior Region.

Classifier ingredients can include:

- interior Region;
- boundary/surface;
- access/opening;
- DesignedFor containment.

This is more precise than merely "something that currently has an object In it."

## 9. Open and Closed

Open/Closed should be represented as a state/Attribute of structures with controllable passage/access.

A Door or Container can expose:

`OpenState(x) -> state/value`

A conventional `Open` Process can normalize to changing that state to Open.

A close Process can be the corresponding target-state transition.

The actual names of the Attribute/value runes can be polished later.

## 10. Door

A Door is a registered artifact/structural Kind whose classifier includes:

- Part of or associated with a boundary;
- movable/changeable access state;
- DesignedFor controlling passage through an opening.

A hole is not automatically a Door.

A permanently sealed wall panel is not necessarily a Door unless its design/profile qualifies.

## 11. House

A House is a registered structure Kind whose classifier can include:

- enclosing habitable Region;
- structural stability;
- access;
- DesignedFor habitation/shelter.

Exact cultural edge cases belong to the world lexicon classifier, not casting-time interpretation.

## 12. Sword

A Sword is a registered artifact semantic molecule/Kind.

A typical classifier can include:

- elongated blade component;
- grip/handle structure;
- hand-held design;
- cutting and/or thrusting Weapon function.

Material is not necessarily fixed to metal; fantasy variants can satisfy the design classifier with other materials.

A damaged/broken Sword may retain Sword Kind if identity-essential structure/history remains sufficient.

## 13. Clothing

Clothing is a function/design Kind intended to be worn on/around a Body for covering, protection, signaling, insulation, etc.

Specific garment Kinds refine structure and placement.

## 14. Food and Medicine

Food and Medicine remain target-biology-relative function Kinds.

Their classifiers should use explicit relations such as:

- suitable nutrient/consumption relation;
- DesignedFor therapeutic effect;
- target organism Kind.

Generic Purpose alone should not hide the target biology.

## 15. Temporary use versus Kind

Cuspell distinguishes:

- `Use(A,X,Goal)` — an Event;
- `Purpose(X,Goal)` — intended relation;
- `DesignedFor(X,Goal)` — artifact design classifier;
- artifact Kind membership.

This distinction is essential for objective noun semantics.

## 16. Function loss

An artifact can remain its Kind after becoming unable to perform its normal function due to Damage.

Example:

a broken Sword can remain Sword historically/structurally while failing current cutting function.

Therefore Kind identity is not identical to current capability.

## 17. Repair

Repairing an artifact can target its registered intact design profile.

The Design/Kind classifier provides one possible restoration template, but if several variants exist the exact template still must be selected or deterministically recorded.

## 18. Result

Purpose-based nouns now rely on explicit design/function relations rather than vague "For."

This improves Tool/Weapon/Container/Door/House/Sword semantics and prevents temporary use from silently changing Kind.
