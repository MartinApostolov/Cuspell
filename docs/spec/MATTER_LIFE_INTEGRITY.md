# Matter, Life, Integrity, and Biological State

_Status: working specification v0.1_

This specification refines physical phase, integrity, damage, life, disease, healing, and several biological/process concepts.

## 1. Matter and material identity

`Matter` is a broad Kind/domain for physical material Entities/substances.

Material Kind identity (Water, Iron, Stone, etc.) is separate from temporary physical state.

Changing phase does not automatically change material Kind.

## 2. Phase family

Use a registered phase family with values/predicates such as:

- Solid
- Liquid
- Gas
- Plasma

For a homogeneous material portion under the phase model, these are mutually exclusive values.

Therefore a single subject constrained simultaneously as exactly Solid and exactly Liquid is contradictory unless a mixed/multiphase model is explicitly invoked.

A composite Entity can contain Parts with different Phase values.

## 3. Mixed phase

Do not treat a slush/foam/composite as proof that Solid and Liquid are never exclusive.

Represent mixture structurally:

- Part A is Solid;
- Part B is Liquid;
- Whole contains both.

A future MixedPhase semantic molecule can compress this when useful.

## 4. Heat

Per measurement specification, Heat is a scalar thermal attribute.

Cold/Hot are threshold comparisons, not independent substances.

Changing Heat can cause phase changes under world physics, but Heat and Phase remain distinct attributes.

Magic may directly set one or request a transformation whose physical consequences are then handled by the world model.

## 5. Whole

`Whole(x)` is an integrity/completeness Property.

It means required structural Parts/relations for x's recognized structural profile are present and sufficiently intact.

Whole is not the converse relation of Part.

## 6. Damage

Damage represents integrity loss relative to a structural/functional profile.

It should support:

- type/category of damage;
- magnitude/severity;
- affected feature/Part;
- source Event when known.

A single scalar Damage amount may be useful but cannot replace damage topology/type in all cases.

## 7. Broken

Broken is a conventional integrity state meaning structural Damage exceeds a Kind/profile-specific threshold such that one or more required functions/relations fail.

Because thresholds depend on Kind/function, Broken may be a semantic molecule rather than a universal primitive.

## 8. Repair

Repair is a Process that reduces Damage/restores required structure toward an explicit restoration profile.

Possible restoration profiles include:

- canonical healthy/intact Kind profile;
- recorded prior state;
- referenced template.

Repair must not guess between multiple possible profiles.

## 9. Cut, Crush, Burn

These are candidate conventional Processes that can be defined through physical state changes.

Examples conceptually:

- Cut: create separation/boundary through material structure.
- Crush: compress/deform with integrity loss.
- Burn: thermal/chemical Process causing material transformation/Damage.

They can be lexicalized for common use even when compositionally definable.

## 10. Life

`Life(x)` is a biological state-predicate Property.

Life is distinct from:

- Exist;
- biological Kind;
- Mind;
- Whole.

An Entity can:

- Exist and NotLife;
- retain biological classification after EndLife;
- be Life while Damaged/NotWhole.

## 11. Birth and Death

Recommended:

- Birth = BeginLife in the appropriate organism/development context.
- Death = EndLife.

A conventional Birth/Death rune may lexicalize these common meanings.

Death does not mean Destroy.

## 12. Dead

`Dead(x)` should normalize to a historical state such as:

- Former(Life(x));
- Not(Life(x));
- x still Exists or is represented by relevant remains, depending on the frame.

A rock is NotLife but not Dead because it was never Life.

## 13. Undead

Do not derive Undead from OppositeLife or NotLife.

"Undead" is setting-specific and must be given an explicit world-ontology definition.

Possible fantasy worlds may define several distinct states/Kinds that ordinary language groups under "undead."

The lexicon can register those once the setting model is chosen.

## 14. Disease

Per lexical resolution:

`Disease(x)`

is a pathological biological state-predicate.

Specific disease types may have structured profiles including:

- affected systems;
- causal agent/process;
- transmission;
- severity;
- progression.

EndDisease can therefore mean ending the pathological state, but the required physical restoration may still demand sufficient Power and structural changes.

## 15. Wound and Heal

A Wound is Damage specialized to living biological structure.

Heal can lexicalize biological Repair:

> restore biological integrity/function toward the selected healthy/reference profile.

Healing does not automatically remove every Disease, Poison, curse, or foreign object unless those are part of the selected repair target/causal model.

This prevents Heal from becoming an undefined universal "make healthy" instruction.

## 16. Growth

`Grow` is a biological development Process, not merely Increase(Size).

Growth follows a biological/developmental profile and may change:

- dimensions;
- Parts;
- tissue;
- maturity state.

Magical Grow therefore requires a recognized organism/development program or explicit target profile.

## 17. Reproduction

`Reproduce` is a biological Process producing one or more new organism identities linked by the world's heredity/lineage model.

It therefore uses fresh result binders and is not the same as Copy.

## 18. Eat

Eat is a Life Process involving:

- eater;
- consumed Matter/Entity;
- transfer/transformation of material into the organism's metabolic system.

Eating something does not imply it is Food by Kind.

## 19. Food

Food is a relational/function-defined Kind:

> material normally suitable for consumption/nutrition by a specified organism Kind under specified conditions.

Therefore Food is relative to consumer biology.

A generic magical Food root must either fix a reference consumer class or accept it as an argument.

## 20. Breathe

Breathe is a biological exchange Process between organism and environmental medium.

Its exact material requirements depend on organism Kind.

Do not define it as universally "inhale oxygen," because fantasy organisms may differ.

## 21. Poison and toxicity

Avoid treating Poison as an absolute unary material Property.

Use an objective relation such as:

`ToxicTo(substance, organism-kind/entity, dose/route) -> Proposition`

A conventional Poison Kind can be defined relative to a standard target/dose only if the lexicon records that standard.

This handles the fact that toxicity depends on dose and organism.

## 22. Medicine

Medicine is likewise relational/function-defined:

> material/tool/process designed or conventionally used to reduce a specified Disease/Damage state for a target biology.

"Medicine" is not an intrinsic chemistry Property.

A registered Medicine Kind can use a design/function classifier.

## 23. Blood

Blood can be a canonical biological Material Kind associated with particular organism Kinds.

It is not derived merely from RedLiquidMatter.

This is another example of why material/anatomical noun roots are useful.

## 24. Body

Body is a biological structural Entity/Kind associated with an organism identity.

Mind and Body are not automatically identical.

The world's metaphysics must state whether a Mind is:

- a Part/state of Body;
- a distinct Entity;
- informational pattern;
- soul-like entity.

Cuspell semantics should not assume one philosophy before the setting chooses it.

## 25. Human, Animal, Plant

These are biological Kinds/taxa/classifiers, not collections of surface Properties.

Their exact recognition rules live in the setting ontology.

## 26. Fire

Do not define Fire as simply Heat + Light + Gas.

A recommended ordinary Fire classifier is a Process/phenomenon Kind involving a self-sustaining energetic/material transformation that produces thermal/light effects.

The setting may distinguish:

- ordinary combustion-like Fire;
- magically sustained flame phenomena;
- other visually similar processes.

A Fire rune can be registered once this world-physics boundary is chosen.

## 27. Energy

Energy is a scalar physical quantity/dimension if the setting uses an energy-conserving physical model.

It should not be a vague synonym for "magic power."

Mana/MagicPower remain separate magical quantities unless explicitly convertible.

## 28. Physical law versus magical command

A Command can request state changes directly, but the execution engine determines:

- whether the change is allowed;
- RequiredPower;
- secondary consequences.

For example, setting Heat may naturally alter Phase after execution.

The language does not need to spell every downstream physical consequence unless the caster wants to constrain them.

## 29. Result

Physical/biological semantics now separate:

- material Kind;
- phase;
- thermal state;
- integrity;
- life;
- disease;
- biological function;
- toxicity/purpose relations.

This avoids defining ordinary nouns from superficial property bundles.
