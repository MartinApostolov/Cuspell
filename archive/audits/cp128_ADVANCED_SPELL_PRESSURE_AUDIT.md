# Checkpoint 128 — Advanced Spell Pressure / Parenthesis-Free Spellcraft Audit

_Status: post-beginner spellcraft pressure pass_

## Trigger

Checkpoint 127 defined a 47-sign spell-first beginner projection using level 0–2 SRD 5.1 spell effects as an external coverage benchmark.

Two follow-up questions were raised:

1. should a normal spell such as the Misty Step analogue require parentheses?
2. what do higher-level SRD spell families expose that low-level magic did not?

Checkpoint 128 answers both.

The external reference remains _System Reference Document 5.1_ / Basic Rules spell material from Wizards of the Coast. It is used as an effect-diversity corpus, not as a Cuspell balance or compatibility target.

## 1. Parentheses are not required for the Misty Step analogue

Canonical surface v0.8 already states:

- `Concurrent` takes a flat EventSpec list;
- sentence end closes the list;
- tight adjacency forms uniquely typed local application;
- parentheses are a fallback rather than canonical style.

Therefore the canonical spell is:

`Concurrent EndAtSelfHere BeginAtSelfThere!`

not:

`Concurrent (End At Self Here) (Begin At Self There)!`

The two grouped forms can be parser-compatible, but the grouped version should not be the beginner teaching form.

This is now executable regression truth.

The beginner manifest is also flattened for every example that had been using parentheses only to display AST grouping.

Examples include:

`Prevent AttackThisYou ThisInterval!`

`Begin CanYouMoveYouThere!`

`Prevent SenseThisVisionYou ThisInterval!`

`Repeat @@@ ChangeThisHeatAddBeforeValueHeatThis«HeatUnit»@!`

`Trigger x:Entity Touch$xThis SenseSelfHearing$x ThisInterval!`

The beginner subset gains a regression that rejects parentheses in its curated spell examples.

This does **not** delete parentheses from Cuspell. They remain a zero-mana fallback for a genuinely ambiguous or structurally difficult expression.

The design target remains:

> normal player spell prose should not need visible AST punctuation.

## 2. Advanced reference scope

The higher-level pressure pass samples SRD level 3–9 effects across all major families, including examples such as:

- level 3: Counterspell, Dispel Magic, Fear, Fly, Gaseous Form, Glyph of Warding, Major Image, Sending;
- level 4: Banishment, Dimension Door, Hallucinatory Terrain, Locate Creature, Polymorph;
- level 5: Animate Objects, Creation, Dominate Person, Geas, Modify Memory, Raise Dead, Scrying, Teleportation Circle;
- level 6: Contingency, Create Undead, Disintegrate, Flesh to Stone, Programmed Illusion, True Seeing;
- level 7: Etherealness, Forcecage, Mirage Arcane, Plane Shift, Regenerate, Resurrection, Symbol, Teleport;
- level 8: Antimagic Field, Clone, Control Weather, Demiplane, Dominate Monster, Mind Blank;
- level 9: Astral Projection, Foresight, Gate, Imprisonment, Shapechange, Time Stop, True Resurrection, Wish.

The goal is not one Cuspell recipe per spell.

The goal is to ask:

> which semantic mechanisms recur once spell power becomes extreme?

## 3. Advanced families already well covered

### Direct magical state termination

A selected active magical state can already be ended:

`EndMagic This!`

This is the semantic core needed by many Dispel Magic / Remove Curse-like cases once the effect being ended is objectively selected.

SRD-specific level checks, ability checks, and slot scaling are execution/game rules rather than language semantics.

**Classification: covered at language level.**

### Fear / attitude / control

Examples:

`Begin FearYouThis!`

`Begin ControlSelfYou!`

Current persistent state relations already provide reusable semantics for:

- Fear;
- Like/Love/Hate;
- Control;
- Intend;
- Obligated;
- Understand;
- Remember.

This covers the semantic core of many enchantment/control effects without importing D&D's "charmed" condition as a root.

**Classification: covered / world-execution resistance still later.**

### Flight and exotic locomotion as capability

A simple Fly-like result can use:

`Begin CanYouMoveYouThere!`

Cuspell does not need a universal Fly root merely because a spell grants a movement mode. A world may require more exact aerial locomotion constraints, but the capability distinction already exists.

**Classification: covered at generic capability level.**

### Gaseous Form / phase change

`Change You Gas!`

uses the existing exclusive Phase family.

This is a good example of high-level magic needing no new spell vocabulary.

**Classification: covered.**

### Teleportation to a known destination

Dimension Door / Teleport / Plane Shift-like discontinuous relocation uses the same state-boundary structure already found at low level:

`Concurrent EndAtSelfHere BeginAtSelfThere!`

or for another selected subject:

`Concurrent EndAtYouHere BeginAtYouThere!`

If the destination is a valid resolved Location, the fact that it lies far away or on another plane belongs to world reachability/capability and RequiredPower.

A separate Teleport root is unnecessary.

**Classification: covered for resolved source/destination.**

### Transformation slices

An exact Form target remains expressible:

`Change You Form FormThis!`

Phase and other attributes can be changed similarly.

This supports substantial parts of Polymorph, Flesh to Stone, Shapechange, Seeming, and related magic when the target profile is explicitly available.

The difficult part is not the word "polymorph"; it is obtaining a complete deterministic transformation profile.

**Classification: language mechanism covered; exact world transformation profiles remain world machinery.**

### Domination / binding / geas-like social control

Persistent Control, Intend, Obligated, Trigger, Prevent, and Cause compose into many advanced compulsion structures.

For example, a simple domination core is:

`Begin ControlSelfYou!`

A geas-like obligation can use the existing Obligated relation plus a separately specified magical consequence/Trigger.

The D&D saving throw and damage-on-disobedience rules are not themselves semantic roots.

**Classification: covered compositionally.**

### Memory editing

Current Remember is a persistent StateProposition.

Therefore selected memory content can be ended or begun:

`EndRememberYouThisInformation!`

`BeginRememberYouThisInformation!`

This is enough to state the semantic core of many Modify Memory-like operations once the exact Information is selected.

**Classification: covered.**

### Death / restoration slices

Current state boundaries already express:

`EndLife This!`

`BeginLife This!`

and existence itself can be ended:

`EndExist This!`

This means Power Word Kill, lethal effects, Raise Dead-like life restoration, and Disintegrate-like existence loss do not automatically require spell roots.

However body reconstruction and resurrection with no remaining body cross into the generation/template problem discussed below.

**Classification: core state transitions covered; reconstruction may not be.**

### Holding / imprisonment

A simple hold at a resolved place can be:

`Persist AtYouThere ThisInterval!`

Longer or conditional imprisonment can add explicit duration/end-condition machinery.

**Classification: covered for spatial/state restraint.**

### Triggered wards

Glyph of Warding, Symbol, Contingency, Magic Mouth, and many "when X happens, do Y" structures strongly validate the existing Trigger design.

The important semantic ingredients are:

- explicit condition;
- bound participant when needed;
- explicit action;
- explicit lifetime;
- no hidden target selection.

**Classification: strong existing coverage.**

## 4. Known gaps become much more important at high levels

### A. Fresh Entity / structure generation

Higher levels heavily reuse the already known generation problem.

Examples include effects analogous to:

- Conjure Animals / Elementals / Fey / Celestial;
- Phantom Steed;
- Creation;
- Mordenkainen's Sword;
- Simulacrum;
- Clone;
- Demiplane;
- parts of Gate;
- True Resurrection when no usable body remains.

Current `Begin Exist X` works only when `X` is already an identifiable semantic subject.

It is not a fresh allocator.

Advanced spells confirm that this is not a niche low-level issue.

The missing reusable mechanism is approximately:

> allocate a new identity from a deterministic world/template profile and return/select that identity.

This remains one of the strongest future spell-engine requirements.

**Classification: confirmed structural gap.**

### B. Controlled unknown-information acquisition

Advanced divination makes the information boundary unavoidable.

Examples include:

- Clairvoyance;
- Locate Creature;
- Scrying;
- Legend Lore;
- Commune / Contact Other Plane;
- Find the Path;
- True Seeing;
- Foresight.

Current Cuspell can represent Information, Questions, Evidence, Knowing, Sensing, and Understanding.

What it does **not** provide for free is:

> ask reality for previously unknown information under a bounded access rule.

That is deliberate.

Turning ordinary Question or Sense into omniscient search would break the language/world boundary.

Advanced spell pressure strengthens the need for an explicit future information-acquisition capability with objectively bounded:

- source/domain;
- scope/range;
- information type;
- access conditions;
- failure/uncertainty behavior.

**Classification: confirmed structural spellcraft gap.**

### C. Persistent multi-observer illusion / representation

Higher-level illusion spells repeatedly require more than one forced Sense event:

- Major Image;
- Hallucinatory Terrain;
- Programmed Illusion;
- Mirage Arcane;
- Project Image;
- Mislead;
- Weird.

A real persistent illusion needs an object/state comparable to:

- a spatially anchored Representation;
- one or more sensory channels;
- a content/profile;
- a lifetime;
- an observer-access rule;
- possibly behavior/Trigger logic.

The current one-shot:

`Sense observer Vision stimulus!`

does not create such a persistent shared perceptual object.

**Classification: confirmed structural gap.**

## 5. New advanced-only pressure

### D. Generic magical execution suppression / interception

Counterspell, Antimagic Field, Globe of Invulnerability, Forbiddance, and related wards expose a distinction that low-level spell analogues did not force sharply enough.

Current tools include:

- `Prevent(EventSpec, interval)`;
- `EndMagic(entity/effect)`;
- `Trigger`;
- ordinary Properties/Relations.

But these do not yet provide one exact first-class way to state:

> prevent any future magical execution of a qualifying class from taking effect in/on this scope.

Important missing pieces include:

- a first-class classification/reference for an attempted magical Command/Event;
- scope over future qualifying spell executions rather than one already written EventSpec;
- region/target interception before commit;
- rules for competing Power/resistance.

This may belong partly to **magic execution semantics**, not necessarily to a new rune.

In particular, adding a Counterspell or Antimagic rune would be the wrong first response.

The right audit question is:

> can magical attempted executions be exposed as typed Events/EventSpecs to ordinary Trigger/Prevent/selection machinery, or does the executor need a separate capability-restriction layer?

**Classification: new advanced execution-layer gap.**

### E. Time-flow manipulation

Time Stop is qualitatively different from ordinary teleportation or state change.

Current Cuspell can:

- order Events;
- reference TimePoints/TimeIntervals;
- measure interval extent;
- express event Rate/frequency;
- Prevent a specified EventSpec.

It does not currently expose a state meaning:

> this subject/region experiences temporal progression at a different rate relative to another frame.

Trying to imitate Time Stop by individually preventing every other possible EventSpec is not equivalent and is not finitely specifiable with the current spell machinery.

Haste/Slow contain D&D-specific action-economy pieces, but they also point toward the same deeper family when interpreted physically.

A future world might model this through:

- a temporal-flow/rate Attribute;
- a world reference-frame relation;
- execution scheduling semantics;
- or another smaller physical basis.

No root is added from this pass.

**Classification: new advanced physical/execution pressure.**

### F. Embodied identity / mind / soul projection

Effects such as:

- Magic Jar;
- Astral Projection;
- Clone;
- some resurrection forms;

treat a person's continuing identity as separable from the current body.

Current Cuspell has:

- Entity identity;
- Life;
- Body as a world concept;
- brain/anatomy concepts;
- mental relations such as Know/Remember/Understand.

It does not currently commit to a universal "Soul" entity or a universal Mind-in-Body relation.

That omission is appropriate because worlds may disagree about whether souls literally exist.

Advanced spell pressure therefore belongs primarily to world ontology:

> if a world has detachable souls/minds, register the relevant Entities/relations there rather than forcing one metaphysics into universal Cuspell.

A generic identity-continuity mechanism may later be needed if execution needs to preserve "same person" across body replacement, but this pass does not prove a universal Soul root.

**Classification: world-ontology pressure, not yet core-language gap.**

## 6. Region barriers and portals

Several advanced spells look at first like they require special "wall", "circle", or "portal" magic.

Examples include:

- Magic Circle;
- Wall of Force;
- Forcecage;
- Teleportation Circle;
- Gate;
- Forbiddance.

The existing building blocks are already substantial:

- Region / Location / Path;
- In / At / Touch / Overlap;
- Prevent;
- Trigger with witness binder;
- Persist;
- Move;
- discontinuous At transitions.

Therefore no Portal or ForceWall root is justified yet.

The difficult cases reduce to two previously identified questions:

1. can a persistent ward intercept a **class of future Events** before commit?
2. can a fresh portal/region/entity be allocated when the spell creates one?

That folds most high-level barrier/portal pressure into **execution interception** and **fresh generation**, rather than adding separate spell nouns.

**Classification: mostly composition plus the two structural gaps above.**

## 7. Weather, earthquakes, storms, and large-area damage

Control Weather, Earthquake, Fire Storm, Meteor Swarm, Storm of Vengeance, large clouds, and similar spells are spectacular because of scale.

Scale alone is not a new language meaning.

Cuspell already has:

- collections and `Each`;
- Region;
- Heat / Pressure / physical Attributes;
- Move;
- Change;
- Damage/Health;
- Repeat/Concurrent;
- weather/material world concepts.

The missing exact physics—precipitation, wind velocity profiles, ground acceleration, electrical discharge, etc.—belongs to the world physics/Attribute program as evidence demands.

The fact that an effect is enormous should primarily increase RequiredPower.

**Classification: no generic advanced-spell root; world physics + power.**

## 8. Wish

Wish is a useful sanity check for Cuspell.

In a conventional spell-list game, Wish is a spell whose effect can emulate many other spells or request extraordinary outcomes.

In Cuspell, the **language already is the thing that states the wished-for outcome**.

There is no need for a universal `Wish` semantic root merely to mean "do the following magical thing."

What matters is:

- whether the requested EventSpec is semantically closed;
- whether magic is capable of realizing it;
- RequiredPower;
- any world-level restrictions.

This is exactly why Cuspell was designed as a spell language rather than a catalogue of spell names.

**Classification: no language gap.**

## 9. Resulting advanced spellcraft priorities

After levels 0–9, five families deserve explicit follow-up, in this order:

1. **fresh generation / deterministic templates** — already known and repeatedly confirmed;
2. **bounded unknown-information acquisition** — repeatedly confirmed by divination;
3. **persistent shared illusion/representation** — repeatedly confirmed by higher illusion magic;
4. **generic magical execution interception/suppression** — newly sharpened by Counterspell/Antimagic/Globe/Forbiddance;
5. **time-flow manipulation** — newly sharpened by Time Stop and physical interpretations of Haste/Slow.

Mind/soul/body separation remains world-ontology dependent rather than automatically joining this list as a universal root.

## 10. Regression effect

Checkpoint 128 adds:

- a beginner-spell regression requiring curated starter spells to remain parenthesis-free;
- a direct regression for `Concurrent EndAtSelfHere BeginAtSelfThere!`;
- advanced-spell pressure regressions for existing reusable mechanisms;
- a guard that advanced spell names do not silently become language roots.

No semantic inventory change is proposed by this pass.

## Decision

**NORMAL SPELL SURFACE REMAINS FLAT.**

The Misty Step analogue is canonically:

`Concurrent EndAtSelfHere BeginAtSelfThere!`

Parentheses are fallback/debug grouping, not required spell punctuation.

**ADVANCED SPELLS DO NOT INVALIDATE THE COMPOSITIONAL DESIGN.**

They mostly increase:

- scale;
- world-model complexity;
- persistence/programming;
- information access;
- generation requirements;
- executor-level interception/control.

The advanced pass does not justify adding spell-name roots.

It does, however, make generation, divination, illusion persistence, magical-execution interception, and time-flow control the next meaningful spell-system audits.
