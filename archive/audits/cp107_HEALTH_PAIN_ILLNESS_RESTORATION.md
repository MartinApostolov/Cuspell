# Checkpoint 107 — Health / Pain / Illness Semantic Restoration

_Status: implemented targeted semantic repair from the civilization vocabulary audit_

## Trigger

Checkpoint 106 found that current Cuspell could discuss injury and life state but could not cleanly express three ordinary civilization-level distinctions:

- overall biological health/function;
- experienced pain;
- being ill/sick/pathological.

The reduced core had:

- `Life` — living/alive state;
- `Damage` — ordered physical injury/damage;
- `Whole` — structural integrity;
- `Hunger` — ordered hunger state;
- medicine/healer/hospital/wound Old Names.

Those do not define Health, Pain, or Illness exactly.

## Historical note

An older pre-checkpoint-98 state document referred to a standalone `Disease` pathological-state meaning, while the current minimized machine registry no longer contained it. A current attribute spec also still used Disease as an example despite the root being absent.

Checkpoint 107 does not blindly restore that old spelling. It re-derives the needed distinctions from current semantics and civilization pressure.

## Audit findings

### Damage is not Pain

`Damage X` is physical injury/damage degree.

`Pain X` is experienced pain/nociceptive-suffering intensity.

Neither entails the other:

- anesthesia or lack of relevant sentience can permit high Damage with low/no Pain;
- neurological, magical, referred, or other pain can occur without corresponding tissue Damage.

Therefore Pain cannot be reduced to Damage, Sense(TouchChannel), Sad, or a generic evaluation without losing its semantic dimension.

### Ill is not Damage

A pathological state may exist with little physical damage, and physical injury does not automatically make a subject ill.

Examples include:

- early infection;
- metabolic/endocrine dysfunction;
- poisoning/pathology before major tissue injury;
- a clean traumatic injury with no disease state.

Therefore `Ill` is not `HighDamage`.

### Ill is not Low Health

Overall functional condition and pathological classification are different dimensions.

A subject may:

- be Ill while still functioning well;
- have Low Health because of injury, congenital/developmental condition, malnutrition, aging, exhaustion, or other causes without being Ill under the world classifier.

Therefore Ill cannot be defined as Low Health.

### Health is not inverse Damage

Overall biological functional condition may depend on injury, pathology, organ function, development, nutrition, and other world-defined factors.

Two subjects with equal Damage can have different Health, and low Damage does not guarantee high Health.

Therefore Health is an independent ordered attribute rather than `Opposite Damage` or `Low Damage`.

### Life is separate from all four

Life is the alive/living state. A living entity can be severely damaged, unhealthy, in pain, and ill. Ending Life is not the same operation as worsening any of those attributes.

## Accepted semantics

### Health

Registered as:

`Health(Entity) -> EvaluationValue`

Role:

- AttributeDescriptor;
- semantic primitive candidate;
- ordered overall biological functional condition.

Contextual `HighHealth` / `LowHealth` use the existing High/Low threshold machinery.

Exact calibration and magical executability require a world health model.

### Pain

Registered as:

`Pain(Entity) -> EvaluationValue`

Role:

- AttributeDescriptor;
- semantic primitive candidate;
- ordered experienced pain/nociceptive-suffering intensity.

The world package determines which entities can experience pain and how the scale is grounded.

### Ill

Registered as:

`Ill(Entity) -> StateProposition`

Role:

- persistent PropertyDescriptor;
- semantic primitive candidate;
- pathological/illness state under the applicable biological world model.

Normal state transitions supply:

- becoming ill: `Begin Ill X`;
- recovery from illness: `End Ill X`.

Ending Ill does not automatically erase independent Damage, Pain, or other Health deficits.

## Heal remains compositional

No `Heal` root is added.

“Healing” is not one exact state transition. Depending on the intended result it may mean:

- reduce physical Damage;
- restore structural Whole/Parts;
- end Ill;
- improve Health;
- reduce Pain;
- regenerate tissue;
- restore a previous profile;
- some explicit combination.

A generic Heal root would hide which result was requested and would therefore be less objective than the current language.

Specific medical procedures may later be Old Names/New Names/world concepts when culturally appropriate.

## Disease vocabulary boundary

Checkpoint 107 adds the general state `Ill`, not a universal `Disease` noun/root.

Specific diseases/pathologies should normally be world concepts/classifiers and Names.

If later corpus/world work shows that Cuspell needs a productive relation linking an affected entity to a specific pathology concept, that should be audited separately rather than smuggled into Ill.

## Regression requirements

The new family must support:

- comparison of Health;
- comparison of Pain;
- High/Low threshold properties for both attributes;
- Ill assertion and Begin/End state transitions;
- combinations such as high Pain + low Damage;
- high Damage + low Pain;
- Ill + high Health;
- low Health + not Ill.

These combinations must remain semantically possible unless a particular world model independently forbids them.

## Inventory effect

Before checkpoint 107:

- 206 registered entries;
- 125 semantic primitive candidates;
- 55 formal constructors;
- 256 semantic frames;
- 48 multi-frame entries;
- 102 Old Names.

After checkpoint 107:

- **209 registered entries**;
- **128 semantic primitive candidates**;
- **55 formal constructors**;
- **259 semantic frames**;
- **48 multi-frame entries**;
- **102 Old Names**.

Frame distribution becomes:

- 22 zero-frame entries;
- 139 one-frame entries;
- 36 two-frame entries;
- 12 three-or-more-frame entries.

No grammar rule, type family, Old Name, New Name, or world concept is added.

## Civilization-audit progress

Checkpoint 107 resolves the first structural issue from checkpoint 106.

Still open before large Old Name expansion:

1. positive/symmetric biological-sex classification;
2. TimeInterval Begin/End/Extent access;
3. policy for historical lexicalization of parameterized verbs/relations.

## Result

Cuspell now distinguishes:

- alive vs dead — `Life`;
- structural integrity — `Whole`;
- physical injury — `Damage`;
- overall biological functional condition — `Health`;
- experienced pain — `Pain`;
- pathological illness state — `Ill`.

This increases the semantic primitive count deliberately. The previous smaller inventory did not preserve these ordinary and medically important distinctions exactly.
