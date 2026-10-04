# Matter, Life, Integrity, and Biological State

_Status: current working specification_

This file defines the current reusable physical/biological state distinctions. Specific species, anatomy, diseases, materials, and healing rules may belong to world concepts rather than primitive roots.

## 1. Matter and phase

`Matter` is the broad material Kind.

Phase is a value-bearing family represented by:

- Solid
- Liquid
- Gas
- Plasma

A subject's Phase is distinct from its material/world Kind. Changing phase does not by itself change what material it is.

## 2. Integrity

`Whole X` is the persistent structural integrity/completeness state for X relative to its recognized structural profile.

Therefore:

`End Whole X`

describes loss of wholeness.

The former specialized severing meaning is represented agentively as:

`Cause agent (End Whole target)`

with optional `:instrument` on Cause when relevant.

## 3. Damage

`Damage X` returns an ordered EvaluationValue describing physical damage/injury degree under the applicable world model.

`HighDamage X` can represent a contextual high-damage state.

Damage and Whole are related by world rules but are not identical:

- something may be damaged while still Whole;
- a world profile decides what structural changes end Whole;
- ending Whole is not automatically ending Exist or Life.

## 4. Health, pain, and illness

Cuspell keeps three further biological/experienced distinctions because none is an exact reduction of physical `Damage` or `Life`.

`Health X -> EvaluationValue`

is an ordered overall biological functional-condition Attribute under the applicable world model. It is **not** defined as the inverse of Damage. Injury, pathology, congenital/developmental condition, physiological function, nutrition, and other world-defined factors may affect Health independently. `HighHealth` / `LowHealth` use the normal contextual threshold machinery; objective magical use requires a world health model.

`Pain X -> EvaluationValue`

is ordered experienced pain/nociceptive-suffering intensity. Pain is not Damage:

- an anesthetized or non-sentient subject may have high Damage with low/no Pain;
- some neurological, magical, or other states may produce Pain without corresponding tissue Damage.

The world model determines which entities can experience Pain and how it is calibrated.

`Ill X`

is a persistent pathological/illness state. It is distinct from Damage, Pain, Low Health, and Not Life. The general state-transition machinery supplies:

- becoming ill -> `Begin Ill X`;
- recovery from the pathological state -> `End Ill X`.

Ending Ill does not automatically erase independent Damage, Pain, or every other Health deficit.

Checkpoint 119 re-runs the reduction test after the later Attribute, typed world-Kind, and expression-Old-Name machinery is in place. All three meanings remain independently necessary:

- `Health` cannot reduce to generic `Evaluate`: evaluation does not identify the biological functional-condition axis, while `Change` and comparison require an actual AttributeDescriptor;
- `Pain` cannot reduce to `Sense` or generic evaluation: sensing is an EventSpec and neither construction supplies persistent ordered pain intensity;
- `Ill` cannot reduce to Low Health, Damage, Pain, Not Life, or a world Kind: those facts may diverge, and ordinary world-Kind predication does not supply the persistent pathological state used by `Begin`/`End`.

There is still no standalone `Heal` root. “Healing” must state the actual requested result: reduce/repair Damage, end Ill, improve Health, restore a Part/state, or some explicit combination.

Specific diseases/pathologies remain world concepts/classifiers or named vocabulary unless later evidence independently justifies more productive semantic machinery.

## 5. Life

`Life X` is a persistent biological life state.

Death is expressed as:

`End Life X`

This does not imply `End Exist X`.

## 6. Biological classifiers

Species, anatomy, pathology, development stages, and similar biological categories are generally world/classifier data unless a productive language-level distinction justifies a root.

The current base registry does **not** keep standalone Disease, Heal, Repair, Birth, Death, or Grow roots. It does keep the general pathological-state Property `Ill`; a named Disease is not automatically a primitive semantic root.

Historical/common concepts can instead be world concepts with Old Names where appropriate.

### Biological sex classification

`Male X` and `Female X` are independent positive biological-sex classification Properties.

They are **not** defined through logical negation:

- `Male X` is not equivalent to `Not Female X`;
- `Female X` is not equivalent to `Not Male X`.

The core language also does not declare the pair universally exhaustive or mutually exclusive. Exact membership, overlap/exclusivity rules, reproductive biology, developmental state, transformed forms, and any additional classifications belong to the applicable world ontology.

Checkpoint 120 re-tests the representation after typed world-Kind classification exists.

The alternatives still fail exactness:

- `Not Female` does not positively mean Male, and `Not Male` does not positively mean Female;
- a universal `Sex(Entity) -> SexValue` attribute would add a third productive descriptor and impose a single functional axis, which would conflict with the deliberately permitted both/neither/additional-category worlds unless more set-valued machinery were added;
- moving Male/Female to ordinary world Kinds would preserve positive category membership but not the current type/transition semantics: world-Kind predication returns `Proposition`, while these Properties return `StateProposition` and support `Begin`/`End` classification changes.

World ontology still decides when the Properties are true; that grounding does not require turning every world-grounded Property into a Kind.

These roots describe biological classification, not every social/cultural gender category. Social gender identities, roles, titles, or culturally specific categories should use world concepts/Names or later independently justified social semantics rather than silently overloading Male/Female.

## 7. Growth

The former Grow convenience meaning is expressed through constrained positive change of Extent.

A generic shape is:

`Change X Extent (More AfterValue Extent X BeforeValue Extent X)`

The exact development program, permitted axes, new Parts, tissue behavior, maturity rules, and resource requirements belong to biology/world execution.

Thus growth is not merely “make every dimension larger.”

## 8. Eating

`Eat agent theme` remains a distinct ordinary Process because eating manner/biological participation is not identical to generic Transfer or Change.

Whether the consumed thing is nutritionally suitable is a world/classification fact.

The ordinary concept Food is currently a world concept with an Old Name rather than a primitive Food root.

## 9. Anatomy and wounds

Body, Hand, organ, stomach, wrist, tendon, wound, and similar recurring nouns are represented through world concepts/Old Names rather than requiring one primitive root each.

The language can still reason about them as Kinds/Entities once referenced.

## 10. World boundary

Objective magical execution of biological change requires world data such as:

- structural profiles;
- lineage/species classifiers;
- viable developmental transformations;
- metabolic/material requirements;
- injury/pathology models;
- regeneration/repair limits.

Cuspell grammar states the requested semantic result; it does not invent biology from English intuition.

## 11. Result

The reusable core keeps broad distinctions—Matter, Phase, Whole, Damage, Health, Pain, Ill, Life, Change, Cause, Extent—while specific diseases, biological objects, and detailed states are pushed into composition or world ontology.
