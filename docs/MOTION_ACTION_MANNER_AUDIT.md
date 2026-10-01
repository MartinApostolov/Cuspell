# Motion and Action Manner Second-Pass Audit

_Status: checkpoint 85 — family-level reduction experiment complete; no net-safe reduction found_

## Scope

This audit tests the highest-priority second-pass family identified in
`docs/SECOND_PASS_PRIMITIVE_FAMILY_MAP.md`.

Primary targets:

- `Bite`
- `Climb`
- `Dodge`
- `Fall`
- `Jump`
- `Limp`
- `Stab`

Boundary cases in the same family:

- `Attack`
- `Eat`
- `Move`
- `Use`
- `Worship`

The goal is not to keep familiar English verbs for convenience. The goal is to see
whether several of these meanings can be reconstructed from a smaller reusable
semantic basis.

## Reduction criterion

A manner abstraction is accepted only if it reduces the number of irreducible
semantic distinctions.

The following does **not** count:

`Manner MoveSelf JumpManner`

if `JumpManner` is simply a new atomic value meaning "jumping". That would replace
one root with one equally primitive value and additionally require the `Manner`
operator.

The same rule applies to moving a distinction into:

- a closed-domain enum;
- a world-model tag;
- a draft Old Name;
- a zero-cost grammar mark.

If the distinction changes truth conditions, it remains semantic and must still be
represented somewhere.

## Existing machinery tested

The current core already supplies several useful general relations/processes:

- `Move` — generic displacement;
- `Touch` — persistent contact;
- `Through` — path/event traversal through a Region;
- `Use` — intentional instrument role/process;
- `Attack` — attack activity;
- `Damage` — ordered physical-damage value;
- `Attempt` — real effort toward an EventSpec goal;
- `Intend` — intended EventSpec;
- `Prevent` — suppress matching Events in a scope;
- `Reflexive` — involuntary/reflex response status;
- `Cause` — causal relation/process;
- `Surface`, `Toward`, `Offset`, `At` — spatial support machinery.

These are enough to describe many facts around an action, but the audit asks whether
they recover the action's exact event type.

## Candidate-by-candidate result

### Bite

Current distinction:

> oral biting action.

Nearby compositions fail:

- `Attack` does not imply biting;
- `Eat` does not imply biting and biting does not imply ingestion;
- `Touch` lacks oral/teeth action and event manner;
- `Damage` is a consequence/degree, not a bite;
- `Cause Begin Touch` is generic contact initiation.

An exact decomposition still needs an irreducible oral/teeth-closing interaction
distinction. No current root supplies it.

**Result: retain.**

### Climb

Current distinction:

> supported/contact locomotion relative to a target; direction may be up, down,
> across, or over.

Nearby compositions fail:

- `Move` gives displacement but not support/contact locomotion;
- `Touch` gives contact but not that contact persists as the support relation of
  the movement;
- `Through` describes traversal through a Region, not movement supported along a
  target surface;
- `Toward` would incorrectly make climbing direction-specific.

An exact decomposition still needs a supported-surface-traversal distinction.

**Result: retain.**

### Dodge

Current distinction:

> evasive action intended to avoid a threat or its contact/effect.

Nearby compositions fail:

- `Move` does not encode evasion;
- `Attempt` encodes effort toward a goal but not the evasive realization itself;
- `Prevent threat scope` suppresses the threatening Event, while a successful
  dodge may leave the threat Event occurring and merely avoid its contact/effect;
- `Intend` describes a mental state, not the evasive action.

An exact decomposition still needs an evasive-realization relation between the
agent's action and the threat.

**Result: retain.**

### Fall

Current distinction:

> non-agentive/context-governed falling motion whose direction/acceleration is
> supplied by the applicable physical/world frame.

Nearby compositions fail:

- `Move` lacks the gravity/world-force and control-mode distinction;
- `Reflexive Move` is wrong because a fall is not a reflex response;
- `Toward` requires an explicit semantic reference and does not encode why the
  motion occurs;
- a generic downward path is not universal across different gravity frames.

An exact decomposition still needs a gravity/world-force-driven uncontrolled-motion
distinction.

**Result: retain.**

### Jump

Current distinction:

> self-launched locomotion with an airborne/unsupported phase.

Nearby compositions fail:

- `Move` does not encode launch or loss of support;
- `Cause Move` adds causation but not jumping;
- `At` state transitions would describe endpoints, not the jumping manner;
- `Touch`/Not-Touch snapshots do not express the event-internal launch/airborne
  structure.

An exact decomposition still needs self-launch plus unsupported/airborne motion.
A single `Airborne` feature would also not distinguish Jump from Fall.

**Result: retain.**

### Limp

Current distinction:

> locomotion with an asymmetric/impaired gait.

Nearby compositions fail:

- `Move` has no gait semantics;
- `Damage` neither entails nor is entailed by limping;
- `Reflexive` is unrelated to gait asymmetry;
- repeated contact alone does not identify a limp.

An exact decomposition still needs an asymmetric/impaired-gait distinction.

**Result: retain.**

### Stab

Current distinction:

> directed puncturing/thrust action against a target, optionally with an
> instrument.

Nearby compositions fail:

- `Attack` is broader and can include non-stabbing attacks;
- `Damage` is a possible consequence, not the event type;
- `Touch` lacks penetration and thrust;
- `Use` records instrumentation but not stabbing;
- `Through Move instrument Surface target` would at best describe a traversal
  geometry and does not by itself encode a puncturing/thrust action. It also fails
  when no separate instrument is supplied.

An exact decomposition still needs a puncturing/thrust interaction distinction.

**Result: retain.**

## Shared-feature experiments

### Experiment A — generic Manner + one value per verb

Proposed shape:

`Manner base-event manner-value`

Required manner values would still include at least:

- Bite manner;
- Climb manner;
- Dodge manner;
- Fall manner;
- Jump manner;
- Limp manner;
- Stab manner.

That replaces seven roots with seven atomic values **plus** one new semantic
constructor.

**Inventory effect: 7 -> 8 or worse. Reject.**

### Experiment B — factor shared physical features

The strongest apparent overlaps are:

- Jump + Fall: unsupported/airborne motion;
- Bite + Stab: penetrating/contact interaction;
- Climb + Limp + Jump + Fall: locomotion based on `Move`.

But exactness still requires extra distinctions:

For Jump/Fall:

- shared airborne/unsupported feature;
- self-launch distinction for Jump;
- gravity/world-force/control distinction for Fall.

That is at least **3 new distinctions for 2 old roots**.

For Bite/Stab:

- shared penetrating/contact feature;
- oral/teeth-closing distinction for Bite;
- directed thrust distinction for Stab.

Again at least **3 new distinctions for 2 old roots**.

Climb, Dodge, and Limp each still require their own missing distinction:

- supported traversal;
- evasive realization;
- asymmetric gait.

Even before adding a generic modifier relation, the plausible feature inventory is
larger than the roots it would replace.

**Result: reject for now.**

### Experiment C — hide manner in the world model

A world model can define gravity, support, anatomy, surfaces, instruments, and
material penetration. That is useful for executing or validating an already
specified action.

It does not remove the lexical problem: the spell/language still needs to state
which event type is intended. If "jump", "limp", or "stab" survives only as an
atomic world tag, the semantic primitive has merely moved layers.

**Result: not a root reduction.**

### Experiment D — move the verbs to Old Names

Old Names can fossilize an existing compositional meaning. They are not a mechanism
for inventing a smaller semantic expansion where none exists.

Moving `Jump` to an Old Name whose expansion still contains an atomic "jump"
concept would only hide the root.

**Result: not a root reduction.**

## Boundary-case audit

### Move

`Move` is the reusable displacement base used by multiple possible manner
analyses. Removing it would make the family less compositional, not more.

**Retain as foundational Process.**

### Use

`Use` is already a successful abstraction: it separates an instrument role from
specific action manners and can relate both EventSpecs and concrete Events to an
instrument.

**Retain.**

### Attack

Attack is not simply a physical manner. It carries the activity classification that
an agent is attacking a target. Damage, Touch, Cause, and Use do not reconstruct
that classification exactly.

**Retain.**

### Eat

Eating is ingestion/consumption activity. Bite may participate in eating, but
neither implies the other. Generic transfer/contact/containment machinery does not
currently encode ingestion and consumption exactly.

**Retain.**

### Worship

Worship is a social/ritual activity directed at a target. It does not reduce to a
physical movement manner, Say, Respect, or Love without changing truth conditions.

**Retain.**

## Count result

No entry is removed and no new manner machinery is added.

Current inventory therefore remains:

- **209 registered base entries**;
- **129 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The motion/action-manner family remains **12 semantic primitive candidates**.

## Design conclusion

The family-level hypothesis was worth testing because seven roots had survived for
similar reasons. The detailed audit shows that the similarity is structural rather
than yet reducible: they are all event manners, but the **missing distinguishing
content is mostly different for each root**.

A generic `Manner` layer would currently increase, not decrease, the irreducible
inventory.

The family should be revisited only after another independently useful abstraction
appears, especially one of:

- event-internal support/contact phases;
- generic control/volition mode;
- body-part/instrument roles;
- penetration/interaction geometry;
- world-force-driven motion.

The next second-pass target should therefore move to the **measurement/descriptor
architecture**, where many roots already share typed value-access structure and a
real Rate consolidation has demonstrated that the family can yield net reductions.
