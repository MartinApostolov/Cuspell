# Checkpoint 127 — Spell-Focused Beginner Cuspell / SRD 0–2 Pressure Pass

_Status: beginner spellcraft subset v0.1_

## Trigger

Cuspell began as a spell-construction system.

After the broad language/corpus stabilization work, the first beginner subset should therefore optimize for:

> learning enough Cuspell to make useful spells quickly,

rather than for ordinary conversational coverage.

The external benchmark selected for this pass is the diversity of **level 0–2 spell effects in D&D SRD 5.1**.

The benchmark is intentionally used as an effect corpus only.

Cuspell does **not** attempt to copy:

- D&D spell slots;
- casting times/action economy;
- attack rolls;
- saving throws;
- damage dice;
- schools;
- concentration;
- exact ranges/areas;
- D&D condition definitions;
- class spell-list balance.

The relevant source is _System Reference Document 5.1_ by Wizards of the Coast LLC, distributed under CC BY 4.0.

## Design goal

Find a small cumulative projection of current Cuspell that can produce recognizably similar outcomes to a substantial and varied subset of SRD level 0–2 magic.

Rules:

1. no new root merely because an SRD spell has a familiar name;
2. prefer one reusable Cuspell mechanism across many spell analogues;
3. keep beginner commands execution-objective;
4. distinguish exact/close analogues from partial effect analogues;
5. record unsupported families as pressure rather than faking them.

## Result — 47-sign spellcraft starter

Machine-readable subset:

`language/subsets/spellcraft_beginner_v0_1.json`

Player guide:

`player/BEGINNER_SPELLCRAFT.md`

The subset contains **47 current registered signs**, under one quarter of the full 213-sign registry.

It adds no new semantic entry.

### Tier 1 — direct manipulation

20 signs:

`Self This You Here There ThisInformation Change Move Begin End Whole Heat Light Sense Vision Hearing Add BeforeValue Opposite Zero`

This tier already supports useful spell families such as:

- illumination/darkening;
- heating/cooling;
- structural repair/breakage;
- remote movement;
- direct magical hearing/vision;
- simple status onset/termination once the relevant state is later learned.

### Tier 2 — persistence/protection/status

15 more signs:

`ThisInterval Health Life Magic Sleep Ill Like Understand Can Prevent Persist Attack Fall At Locked`

Cumulative total: **35**.

This opens:

- healing/reference-health effects;
- life preservation;
- sleep/illness/restoration;
- charm-like attitude changes;
- comprehension;
- capability buffs;
- wards against attacks/falling/status onset;
- holding position;
- unlocking;
- magical-object status.

### Tier 3 — transformation/programming

12 more signs:

`Form Climb Intend Repeat Concurrent Each They Trigger Touch Say And Not`

Cumulative total: **47**.

This opens:

- exact Form-based transformation;
- climbing capability;
- suggestion/intention effects;
- repetition;
- simultaneous event boundaries;
- group effects;
- triggered wards;
- speaking objects/messages;
- conjunction/negation.

Starter Unit Old Names:

- `«HeatUnit»`;
- `«LightUnit»`.

## Coverage result

The manifest records **47 distinct SRD level-0-to-2 spell references** with parser-validated Cuspell effect analogues.

They span substantially different magical tasks rather than repeating one combat family.

Representative examples include:

### Level 0 / cantrip-like

- Light -> `Change This Light «LightUnit» @!`
- Mending -> `Begin Whole This!`
- Mage Hand -> `Move This There!`
- Message -> `Sense You Hearing ThisInformation!`
- Fire Bolt-like -> exact Heat increase
- Ray of Frost-like -> exact Heat decrease
- Poison Spray-like -> `Begin Ill This!`
- Spare the Dying-like -> `Persist Life This ThisInterval!`
- Minor Illusion-like -> forced visual sensing of a prepared stimulus

### Level 1-like

- Alarm -> finite `Trigger` on `Touch`;
- Animal Friendship / Charm Person -> `Begin Like ...`;
- Comprehend Languages -> `Begin Understand ...`;
- Cure Wounds / Healing Word -> exact Health copied from a designated reference;
- Detect Magic -> sensory access to selected Magic state;
- Disguise Self -> Form copy;
- Feather Fall -> `Prevent Fall`;
- Longstrider-like -> grant movement capability;
- Protection from Poison -> prevent onset of Ill;
- Shield-like -> prevent a selected attacker's attack EventSpec;
- Sleep -> `Begin Sleep`;
- Thunderwave-like -> forced movement.

### Level 2-like

- Alter Self -> exact Form copy;
- Darkness-like -> zero Light;
- Darkvision-like -> grant a vision capability;
- Enhance Ability-like -> grant a selected capability;
- Enlarge/Reduce-like -> use an exact reference Form/geometry profile with the target scale;
- Gentle Repose-like -> persist Whole;
- Gust of Wind-like -> forced movement;
- Heat Metal -> exact Heat increase;
- Hold Person-like -> persist At a location;
- Invisibility-like -> prevent an observer's visual Sense;
- Knock -> `End Locked`;
- Lesser Restoration-like -> `End Ill`;
- Levitate-like -> Move to an elevated Location;
- Magic Mouth -> Trigger + Say;
- Magic Weapon-like -> `Begin Magic`;
- Misty Step-like -> concurrent end/begin At boundaries;
- Scorching Ray-like -> Repeat a heat-strike effect;
- Shatter-like -> `End Whole`;
- Spider Climb -> grant Climb capability;
- Suggestion-like -> begin Intend toward a concrete EventSpec.

These are effect analogues, not claims of D&D mechanical equivalence.

## Important executable-reference finding

The first draft used `That` in several spells because it is convenient ordinary discourse.

CI correctly rejected those Commands.

Current magical execution marks unresolved contextual `That` as semantically incomplete:

> context-dependent references must be made objective before magical execution.

This is a valuable beginner-design result.

Spell-first Cuspell should teach:

- `This` for an explicitly designated subject;
- `You` for the addressee/selected target when appropriate;
- `Self` for the caster;
- `Here` / `There` for resolved locations;
- explicit binders only when programming/multi-target behavior genuinely needs them.

`That` remains ordinary Cuspell. It is simply not part of this executable starter slice.

## Extent finding

The first Enlarge/Reduce analogue used contextual holistic `Extent`.

Execution closure also rejected that as too contextual.

The starter therefore uses an exact reference `Form` / geometry profile whose registered scale supplies the desired larger or smaller body.

This is again a teaching restriction rather than a change to Extent semantics.

Advanced Cuspell can still use objective coordinate-frame/axis Extent measures when the complete spell specifies them.

## Deliberately excluded pressure families

Several low-level SRD effects are useful precisely because they reveal boundaries.

### Fresh Entity generation

Examples include effects analogous to:

- Find Familiar;
- Unseen Servant;
- Floating Disk;
- Goodberry;
- Flaming Sphere;
- some interpretations of Web or conjured material.

The current core intentionally has no universal allocator that creates a fresh Entity merely from a Kind.

This is already a known world/template-generation problem.

Do not add a beginner Create rune just to imitate these spells.

### Controlled unknown-information acquisition

Broad effects analogous to:

- Locate Object;
- Find Traps;
- Identify;
- Augury;
- Detect Thoughts;

must not turn ordinary References, Questions, or Sense into omniscient world search.

Cuspell needs an explicit, bounded information-acquisition semantic if such effects become a genuine design target.

This is one of the strongest follow-up spellcraft questions.

### D&D game-stat modifiers

Examples include:

- Bless;
- Bane;
- Guidance;
- Resistance;
- True Strike.

Their exact D&D effects modify game abstractions such as rolls/bonuses.

Cuspell should prefer objective world changes—capability, protection, perception, confidence/evidence, movement, physical state—rather than inventing an attack-roll Attribute solely for compatibility.

### Full persistent illusion systems

A one-shot or selected forced Sense event is easy.

A reusable illusion that:

- occupies a spatial region;
- persists;
- presents to multiple observers;
- may be touched/investigated;
- behaves independently;
- can be programmed;

requires a richer persistent sensory/representation model.

This is another legitimate follow-up pressure family, but it is not smuggled into beginner `Sense`.

## Why the subset is a projection, not a second language

Every starter sign is already a full Cuspell sign.

Every example is ordinary current surface-v0.8 Cuspell.

There is:

- no beginner-only grammar;
- no reduced hidden semantics;
- no spell-name macro system;
- no special D&D execution layer.

Learning the starter therefore transfers directly into advanced Cuspell.

## Regression effect

Checkpoint 127 adds six subset/regression tests.

They verify:

1. the subset is cumulative, unique, and 47 signs;
2. every starter sign is a current registered entry;
3. the two starter Unit Old Names exist;
4. reference effects stay within levels 0–2;
5. the reference spell names are unique;
6. every curated Cuspell effect analogue parses as a valid magical Command.

Suite size:

- **679 -> 685 tests**.

Python 3.11 and 3.12 both pass.

## Inventory effect

None.

The repository remains:

- **213 registered base entries**;
- **132 semantic primitive candidates**;
- **55 formal constructors**;
- **267 semantic frames**;
- **49 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

## Decision

**BEGINNER CUSPELL IS SPELL-FIRST.**

Use SRD level 0–2 spell-effect diversity as the first external benchmark, not as a spell vocabulary or balance contract.

The v0.1 starter is:

- **47 signs**;
- **2 starter Unit Old Names**;
- **47 parser-validated reference effect analogues**;
- no new semantics.

## Next work

Pressure-test the excluded low-level spell families before glyph design.

The most useful semantic questions are now:

1. fresh Entity generation from closed world templates;
2. bounded unknown-information acquisition/divination;
3. persistent multi-observer illusion/representation structure.

Do not automatically solve all three.

First determine which can already be built from advanced current Cuspell and which expose genuinely missing reusable semantics.
