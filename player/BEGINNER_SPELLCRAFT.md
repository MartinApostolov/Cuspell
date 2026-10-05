# Beginner Spellcraft

_Status: spell-focused beginner subset v0.1 — checkpoint 127_

This is the first deliberately small teaching subset of Cuspell.

Its purpose is not to teach the whole language. It teaches enough Cuspell to write a broad family of useful magical Commands first.

The design target is inspired by the **level 0–2 spell effects in D&D SRD 5.1**. Cuspell is not converting D&D spell slots, saving throws, damage dice, schools, ranges, or action economy. The SRD spells are used as an external stress test:

> can a new Cuspell writer produce recognizably similar magical outcomes with a small sign set?

Spell names/effect references are from _System Reference Document 5.1_ by Wizards of the Coast LLC, licensed CC BY 4.0.

## 1. What you need to write first

A magical Command is an EventSpec ending in:

`!`

Examples:

`Move This There!`

`Begin Whole This!`

`Change This Light «LightUnit» @!`

Normal spell prose should stay flat. Tight adjacency makes a complete local unit, while typed argument structure handles the larger phrase:

`Prevent AttackThisYou ThisInterval!`

Parentheses remain a zero-mana fallback for genuinely ambiguous or debugging cases; none of the curated beginner spells require them.

Spaces are free. Tight adjacency remains optional where the parse is unique.

`That` is intentionally not in this spell-first subset. It is useful ordinary-language context reference, but current magical execution rejects it when it has not been made objectively resolvable. Beginner spells therefore prefer explicit `This`, `You`, `Self`, and selected locations.

`@` is the positive unit number 1.

The two starter measurement Old Names are:

- `«HeatUnit»`
- `«LightUnit»`

## 2. The 47-sign starter set

The set is cumulative. A learner can begin with the first group and add the next groups as needed.

### Direct manipulation — 20 signs

References:

`Self This You Here There ThisInformation`

Event/state change:

`Change Move Begin End`

Physical/structural values:

`Whole Heat Light`

Perception:

`Sense Vision Hearing`

Simple quantity change:

`Add BeforeValue Opposite Zero`

These already support light/darkening, heating/cooling, repair, remote movement, and magical hearing/vision effects.

### Persistent and protective magic — 15 more

`ThisInterval Health Life Magic Sleep Ill Like Understand Can Prevent Persist Attack Fall At Locked`

These add:

- healing/reference-health effects;
- life preservation;
- magical status;
- sleep;
- illness/restoration;
- charm-like attitude changes;
- language/content comprehension;
- capability buffs;
- attack/fall prevention;
- holding a target at a place;
- unlocking.

Cumulative count: **35 signs**.

### Transformation and programmable magic — 12 more

`Form Extent Climb Intend Repeat Concurrent Each They Trigger Touch Say And Not`

These add:

- exact form/size copying;
- climbing capability;
- suggestion/intention effects;
- repeated effects;
- simultaneous effects;
- multi-target effects;
- triggered wards;
- speaking objects/messages;
- conjunction and negation.

Cumulative count: **47 signs**.

That is under one quarter of the full current 213-sign registry.

## 3. Representative cantrip-like effects

These are Cuspell effects with roughly comparable practical outcomes, not copies of D&D mechanics.

| SRD reference | Cuspell | What the Cuspell command does |
| --- | --- | --- |
| Light | `Change This Light «LightUnit» @!` | Set an object's Light output to an exact value. |
| Mending | `Begin Whole This!` | Restore recognized structural wholeness. |
| Mage Hand | `Move This There!` | Magically move a selected object. |
| Message | `Sense You Hearing ThisInformation!` | Make the addressee hear selected information. |
| Fire Bolt-like | `Change This Heat Add BeforeValue Heat This «HeatUnit» @!` | Raise target Heat by one exact unit. |
| Ray of Frost-like | `Change This Heat Add BeforeValue Heat This Opposite «HeatUnit» @!` | Lower target Heat by one exact unit. |
| Poison Spray-like | `Begin Ill This!` | Begin a pathological state. |
| Spare the Dying-like | `Persist Life This ThisInterval!` | Actively maintain Life through an interval. |
| Minor Illusion-like | `Sense You Vision This!` | Cause the addressee to have a visual sensing event of a prepared stimulus. |

The last example is intentionally only an illusion-like sensory result. The starter subset does not yet define a reusable persistent illusion-object ontology.

## 4. Representative 1st-level-like effects

| SRD reference | Cuspell | Notes |
| --- | --- | --- |
| Alarm | `Trigger x:Entity Touch $x This Sense Self Hearing $x ThisInterval!` | Alert when an Entity touches the warded subject. |
| Animal Friendship | `Begin Like This Self!` | Begin positive attitude from an explicitly designated creature toward the caster. |
| Charm Person | `Begin Like You Self!` | Charm-like attitude change, without importing the D&D condition rules. |
| Comprehend Languages | `Begin Understand Self ThisInformation!` | Understand selected information/content. |
| Cure Wounds / Healing Word | `Change You Health Health Self!` | Match the exact Health value of the caster as a designated reference. |
| Detect Magic | `Sense Self Vision Magic This!` | Perceive the Magic state of a selected subject. |
| Disguise Self | `Change Self Form Form This!` | Copy an explicitly designated reference Form. |
| Faerie Fire-like | `Change This Light «LightUnit» @!` | Make the selected subject luminous. |
| Feather Fall | `Prevent Fall You ThisInterval!` | Prevent falling during the interval. |
| Longstrider / Jump-like | `Begin CanYouMoveYouThere!` | Grant a selected movement capability. |
| Protection from Poison | `Prevent BeginIllYou ThisInterval!` | Prevent onset of illness/pathology. |
| Shield-like | `Prevent AttackThisYou ThisInterval!` | Prevent attacks from an explicitly designated attacker for the interval. |
| Sleep | `Begin Sleep You!` | Begin Sleep state. |
| Thunderwave-like | `Move This There!` | Force an explicitly designated target to a designated location. |

## 5. Representative 2nd-level-like effects

| SRD reference | Cuspell | Notes |
| --- | --- | --- |
| Alter Self | `Change Self Form Form This!` | Copy an exact explicitly designated reference Form. |
| Darkness-like | `Change This Light Zero!` | Reduce selected subject Light to zero. |
| Darkvision-like | `Begin CanYouSenseYouVisionThis!` | Grant a selected vision capability. |
| Enhance Ability-like | `Begin CanYouMoveYouThere!` | Representative capability increase. |
| Enlarge/Reduce-like | `Change Self Form Form This!` | Copy an exact reference Form/geometry profile whose scale supplies the desired larger or smaller body. |
| Gentle Repose-like | `Persist Whole This ThisInterval!` | Preserve recognized structural wholeness. |
| Gust of Wind-like | `Move This There!` | Force an explicitly designated matter/target toward a destination. |
| Heat Metal | `Change This Heat Add BeforeValue Heat This «HeatUnit» @!` | Raise exact Heat of the selected metal object. |
| Hold Person-like | `Persist At You There ThisInterval!` | Hold the target at a designated location. |
| Invisibility-like | `Prevent SenseThisVisionYou ThisInterval!` | Stop one explicitly designated observer from visually sensing the target. |
| Knock | `End Locked This!` | End Locked state. |
| Lesser Restoration-like | `End Ill You!` | End pathological Ill state. |
| Levitate-like | `Move You There!` | Move target to a designated elevated location. |
| Magic Mouth | `Trigger x:Entity Touch $x This Say This ThisInformation $x ThisInterval!` | Make a warded object speak stored information to its triggerer. |
| Magic Weapon-like | `Begin Magic This!` | Begin Magic state on an object/weapon. |
| Misty Step-like | `Concurrent EndAtSelfHere BeginAtSelfThere!` | Discontinuous relocation between two locations. |
| Pass without Trace-like | `Prevent SenseThisVisionYou ThisInterval!` | One explicitly designated observer/channel concealment pattern. |
| Scorching Ray-like | `Repeat @@@ Change This Heat Add BeforeValue Heat This «HeatUnit» @!` | Three sequential heat strikes. |
| Shatter-like | `End Whole This!` | Destroy structural wholeness of a selected subject. |
| Spider Climb | `Begin CanYouClimbYouThis!` | Grant capability to climb a selected surface/entity. |
| Suggestion-like | `Begin IntendYouMoveYouThere!` | Begin an intention toward a concrete action. |

## 6. Multi-target extension

The final teaching group includes `Each`, `They`, and binders.

For example, to make a selected group luminous:

`Each They x:Entity Change $x Light «LightUnit» @!`

This is deliberately taught after direct single-target spells.

## 7. What this starter does not try to imitate yet

Several SRD 0–2 spell families are deliberately poor beginner targets.

### Fresh entity creation

Current core Cuspell has no universal fresh-Entity allocator.

That affects effects resembling:

- Find Familiar;
- Unseen Servant;
- Floating Disk;
- Goodberry;
- Flaming Sphere;
- Web if treated as newly generated material.

Those belong to the existing fresh-generation/world-template problem, not to beginner syntax.

### Open-world magical search or unknown-information divination

Effects such as broad Locate Object, Find Traps, Identify, Augury, or Detect Thoughts require controlled access to information the caster does not already possess.

Ordinary References and Questions must not become omniscient search.

### D&D game-stat modifiers

Bless/Bane/Guidance/Resistance/True Strike-style mechanics alter D&D rolls/bonuses.

Cuspell should describe objective world capabilities, protection, evidence, or physical changes rather than inventing an attack-roll statistic solely to copy another game's mechanics.

### Full illusion systems

A one-shot forced sensing event is easy to express.

A persistent illusion with spatial appearance, independent observers, interaction rules, investigation, and programmed behavior needs more explicit semantics than this starter subset.

## 8. Design rule

The SRD list is a **coverage benchmark**, not a vocabulary shopping list.

A D&D spell name does not justify a new Cuspell root.

Prefer:

1. existing composition;
2. existing Old Names/world concepts;
3. a small reusable semantic addition only if several effects expose the same missing distinction.

The beginner set should remain a teachable window into the full language, not a second spell language.
