# Checkpoint 119 — Health / Pain / Ill Exact-Reduction Audit

_Status: post-civilization reduction/redundancy audit, target 2_

## Purpose

Checkpoint 107 restored three meanings after the civilization-coverage audit:

- `Health(Entity) -> EvaluationValue`;
- `Pain(Entity) -> EvaluationValue`;
- `Ill(Entity) -> StateProposition`.

Those additions were justified against the smaller language that existed at the time. Checkpoint 119 re-tests them after the later language gained or stabilized:

- the general Attribute/Change machinery;
- contextual `Evaluate`;
- explicit-channel `Sense`;
- typed registered world-Kind classification;
- parameterized expression Old Names.

The question is not whether the English words are useful. It is whether any of the three meanings can now be stated **exactly** without keeping its productive semantic distinction.

## Reduction rule

A successful reduction must preserve:

1. semantic type;
2. truth/value conditions in every allowed world;
3. comparison/state-transition behavior;
4. magical execution meaning;
5. objective world-model grounding;
6. ordinary parser usability.

Moving the same missing distinction into an opaque world predicate, arbitrary mode tag, or hidden macro is not a reduction.

## Health

Current meaning:

`Health(subject) -> EvaluationValue`

Health is an ordered biological functional-condition Attribute.

### Candidate: inverse Damage

This fails.

Equal Damage does not force equal Health. Health may also depend on:

- pathology;
- organ/system function;
- nutrition;
- congenital/developmental condition;
- exhaustion or other world-defined biological factors.

Conversely low Damage does not guarantee high Health.

Cuspell's `Opposite` operator also does not apply to EvaluationValue; its current frames are Quantity and Direction. Adding an EvaluationValue opposite merely to encode Health would introduce new semantics rather than reduce them.

### Candidate: Low/High Damage

Thresholds lose the dimension itself.

Two subjects can both be LowDamage while having very different Health. Likewise a HighDamage subject may retain relatively high functional Health compared with another equally damaged subject.

### Candidate: Ill / Not Ill

Health and pathology are independent.

Allowed worlds include:

- Ill + HighHealth;
- Not Ill + LowHealth.

Therefore neither `Ill` nor its negation determines Health.

### Candidate: Life / Whole / Hunger

Alive/dead, structural completeness, hunger, and overall biological function are distinct axes. None selects the Health value.

### Candidate: Evaluate

`Evaluate(evaluator,target)` or contextual `Evaluate(target)` returns an EvaluationValue, but the result type alone does not identify **what is being evaluated**.

`Evaluate This` can represent a contextual assessment of This; it does not mean biological functional condition.

Replacing Health with Evaluate would therefore collapse unrelated evaluation axes and make the biological interpretation depend on hidden context.

### Candidate: generic Attribute machinery

The Attribute system does not contain an operation like:

`Attribute(subject, "health")`

with a free English label. Instead `Change(subject,attribute,target)`, `BeforeValue`, comparisons, and other generic operations require an actual `AttributeDescriptor`.

Removing `Health` therefore removes the descriptor needed to select this dimension.

Introducing a generic arbitrary named-attribute constructor would be a larger semantic mechanism and would recreate the same distinction as data.

**Health result: KEEP.**

## Pain

Current meaning:

`Pain(subject) -> EvaluationValue`

Pain is ordered experienced pain/nociceptive-suffering intensity.

### Candidate: Damage

This fails in both directions.

Allowed worlds include:

- high Damage + low/no Pain under anesthesia, altered sentience, nerve interruption, or analogous mechanisms;
- high Pain + low/no tissue Damage under neurological, magical, referred, or other pain states.

Damage is physical injury; Pain is experience.

### Candidate: Sense

`Sense(experiencer,channel,stimulus) -> EventSpec`

is an acquisition/perception event.

Pain is not merely the occurrence of a sensing event:

- Pain has an ordered intensity value;
- Pain can persist between individual sensory-acquisition events;
- the relevant world model may generate pain internally rather than from an external sensed stimulus;
- Sense requires an explicit channel and stimulus structure that Pain does not.

The types also differ: Sense returns EventSpec while Pain returns EvaluationValue.

### Candidate: Evaluate

As with Health, generic evaluation does not identify a pain axis.

A contextual evaluation of a subject may concern quality, desirability, danger, beauty, performance, or another axis. Returning EvaluationValue is not enough to make two meanings identical.

### Candidate: sadness/negative evaluation

Pain is not merely negative affect. Physical pain can coexist with many emotional states, and sadness can occur without pain.

**Pain result: KEEP.**

## Ill

Current meaning:

`Ill(subject) -> StateProposition`

Ill is a persistent pathological/illness state.

### Candidate: Low Health

This fails because overall function and pathology can diverge.

Allowed worlds include:

- Ill + HighHealth;
- Not Ill + LowHealth.

### Candidate: High Damage

Injury need not be illness, and pathology can precede or avoid significant physical damage.

### Candidate: Pain

Illness may be painless; pain may occur without illness.

### Candidate: Not Life

Living ill subjects are ordinary allowed cases. Death is not illness.

### Candidate: world Kind

Checkpoint 116 lets registered world Kinds classify values of declared semantic types.

That is useful for:

- particular disease categories;
- named pathologies;
- organism/species classifiers;
- event/information/time categories.

It does not replace the general Ill state.

Ordinary world-Kind predication yields category membership. `Ill` is a reusable persistent state predicate that supports:

`Begin Ill X`

and:

`End Ill X`.

Turning Ill into a world Kind would also blur the intended boundary between:

- "X is currently ill";
- "X is a member/instance of disease category D";
- "X has pathology D".

Those are not the same relation.

If a world package stored a hidden boolean `is_ill(X)` to recover the lost behavior, that hidden relation would simply be Ill under another name.

### Candidate: specific disease concepts

A collection of named diseases does not exhaust the generic pathological state across arbitrary worlds. It also requires a separate relation connecting the subject to the disease/pathology occurrence.

Checkpoint 119 therefore keeps specific diseases as world concepts while retaining the general Ill predicate.

**Ill result: KEEP.**

## Cross-family countermodels

The strongest exactness evidence is the set of independently allowed combinations already protected by regression tests:

- High Pain + Low Damage;
- High Damage + Low Pain;
- Ill + High Health;
- Not Ill + Low Health.

These are not merely unusual Earth examples. They demonstrate that the dimensions have independent truth/value conditions in the language's allowed world space.

Any proposed reduction that makes one member determine another rejects valid worlds.

## Old Name / historical lexicalization check

Parameterized expression Old Names do not help here.

They lexicalize an **existing exact composition** with typed parameters.

There is no existing composition whose expansion means Health, Pain, or Ill exactly. Making an Old Name expand to a hidden special classifier/value function would therefore introduce the missing semantics rather than compress existing semantics.

## Magical execution consequence

The distinctions also matter for commands.

A caster may intentionally request:

- lower Damage without directly changing Pain;
- lower Pain without repairing Damage;
- improve Health without ending a specific pathology;
- end Ill without restoring every Health deficit.

World laws may cause downstream consequences, but the direct requested semantic target remains distinct.

Collapsing the roots would make these scopes less explicit or impossible to state.

## Inventory result

**KEEP AS IRREDUCIBLE SEMANTIC BASIS:**

- `Health`;
- `Pain`;
- `Ill`.

No base entry, frame, type, Old Name, New Name, or world concept is added or removed.

Inventory remains:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

The executable suite remains **654 tests**; existing health-state regressions already exercise the required independence cases.

## Next reduction target

Re-test checkpoint 108's positive biological-sex classification:

- `Male`;
- its relationship to `Female`;
- whether the best final representation is still two productive Properties rather than a typed Sex attribute/value family or world classification.
