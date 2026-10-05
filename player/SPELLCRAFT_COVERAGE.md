# Spellcraft Coverage Projection

_Status: retained 50-sign coverage projection — checkpoint 139_

This is the retained broad spellcraft coverage projection. It is **not** the current first learner lesson; the actual beginner progression is in `BEGINNER_SPELLCRAFT.md` and `spellcraft_beginner_v0_6.json`.

Its purpose is to show how much spell-effect diversity can be expressed inside a fixed 50-sign window. It remains useful as a stress test, but checkpoint 135 stops treating all 50 signs as material a new learner should know up front.

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

The starter Old Names used by the examples are:

- `«HeatUnit»`
- `«LightUnit»`
- `«LowExtent«MoveLifeThing»»` — cat
- `«SharpMoveAttackThing»` — arrow

The last two are ordinary historical vocabulary used to give fresh creation a deterministic Kind domain; they are not spell-name macros.

## 2. The 50-sign coverage set

The set is retained as a cumulative coverage window. It is no longer the recommended learning order.

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

### Transformation and programmable magic — 13 more

`Form Climb Intend Repeat Concurrent Each Collect Member Trigger Touch Say And Not`

These add:

- exact form/size copying;
- climbing capability;
- suggestion/intention effects;
- repeated effects;
- simultaneous effects;
- objective multi-target effects through explicit Collection construction;
- triggered wards;
- speaking objects/messages;
- conjunction and negation.

Cumulative count: **48 signs**.

### Fresh creation — 2 more

`Matter Create`

These add explicit fresh-Entity allocation. `Create` binds the new identity through its post-creation profile and can optionally keep that binder in scope for one immediate continuation EventSpec:

`Create x:Entity Matter $x And At $x Here Move $x There!`

A named Kind is usually better than bare `Entity` when the world needs a deterministic generation profile.

Cumulative count: **50 signs**.

That is under one quarter of the full current 217-sign registry.

## 3. Representative cantrip-like effects

These are Cuspell effects with roughly comparable practical outcomes, not copies of D&D mechanics.

| SRD reference | Cuspell | What the Cuspell command does |
| --- | --- | --- |
| Light | `Create x:Entity At $x Here Change $x Light «LightUnit» @!` | Create a fresh light-emitting Entity at Here, then set its Light output. |
| Mending | `Begin Whole This!` | Restore recognized structural wholeness. |
| Mage Hand | `Move This There!` | Magically move a selected object. |
| Message | `Sense You Hearing ThisInformation!` | Make the addressee hear selected information. |
| Fire Bolt-like | `Change This Heat Add BeforeValue Heat This «HeatUnit» @!` | Raise target Heat by one exact unit. |
| Ray of Frost-like | `Change This Heat Add BeforeValue Heat This Opposite «HeatUnit» @!` | Lower target Heat by one exact unit. |
| Poison Spray-like | `Begin Ill This!` | Begin a pathological state. |
| Spare the Dying-like | `Persist Life This ThisInterval!` | Actively maintain Life through an interval. |
| Minor Illusion-like | `Sense You Vision This!` | Cause the addressee to have a visual sensing event of a prepared stimulus. |

The last example is intentionally only the 50-sign projection's one-shot sensory approximation. Full Cuspell now has `Represent` for persistent shared representation, but `Represent` is outside this fixed projection.

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
| Faerie Fire-like | `Each Collect x:Entity Member $x This y:Entity Change $y Light «LightUnit» @!` | Make every Entity in an explicitly designated Group luminous. |
| Feather Fall | `Prevent Fall You ThisInterval!` | Prevent falling during the interval. |
| Find Familiar-like | `Create x:«LowExtent«MoveLifeThing»» Life $x And At $x Here And Like $x Self!` | Create one fresh living friendly cat-like creature; special familiar rules are not copied. |
| Magic Missile-like | `Repeat @@@ Create x:«SharpMoveAttackThing» At $x Here Move $x There!` | Create three fresh arrow-like projectile identities and immediately move each toward the designated destination; force damage/automatic hit are not copied. |
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

The transformation/programming tier includes `Collect`, `Member`, `Each`, and binders.

For example, to make every member of an explicitly designated Group luminous:

`Each Collect x:Entity Member $x This y:Entity Change $y Light «LightUnit» @!`

This is deliberately taught after direct single-target spells. The contextual plural reference `They` remains part of full Cuspell, but it is not used by executable beginner spells because unresolved contextual references are not objective enough for magic.

## 7. What this fixed coverage projection does not try to imitate

Several SRD 0–2 spell families are deliberately poor beginner targets.

### Fresh entity creation is now available, but profiles still matter

Checkpoint 129 added `Create`, and checkpoint 130 folded it into this 50-sign projection.

`Create` solves identity allocation; it does not make a bare noun into a complete physical blueprint. A usable creation still needs a deterministic Kind/world generation profile plus explicit facts such as location, Life, Matter, relations, or other required constraints.

The coverage projection therefore includes a Find Familiar-like cat example and a created-projectile Magic Missile-like example, but effects such as Unseen Servant, Floating Disk, Goodberry, Flaming Sphere, or generated Web material may still need more exact world templates or additional semantics for their distinctive behavior.

### Bounded unknown-information divination now exists in full Cuspell

Checkpoint 131 adds `Find` for controlled factive information acquisition.

For example:

`Find Self This Magic This!`

asks magic to determine the truthful yes/no answer about the explicitly designated subject.

`Find Self This l:Location At This $l!`

asks for the subject's Location binding(s).

`Find` is deliberately **not added to this fixed 50-sign coverage projection**. The current 11-sign semantic core does teach simple yes/no `Find`; the old projection stays frozen rather than growing again.

Ordinary References, Questions, Sense, and Collect still do not become omniscient search. Find requires an explicit information-access scope tied to the query, and blocked/incomplete access fails rather than pretending the answer was false or empty.

### D&D game-stat modifiers

Bless/Bane/Guidance/Resistance/True Strike-style mechanics alter D&D rolls/bonuses.

Cuspell should describe objective world capabilities, protection, evidence, or physical changes rather than inventing an attack-roll statistic solely to copy another game's mechanics.

### Persistent shared representation

Full Cuspell now supports persistent shared representation through `Represent` plus `Create`/`Persist`/`Trigger`. This fixed 50-sign projection deliberately does not grow to include that machinery; its Minor Illusion-like row remains a marked partial approximation.

## 8. When two reference spells share a recipe

An exact duplicate Cuspell recipe is allowed only when the chosen objective effect slice is genuinely the same.

Examples intentionally sharing a recipe include Cure Wounds / Healing Word (same Health result, different D&D delivery rules) and several heat-change references. Two important collapses were repaired across checkpoints 130 and 135:

- checkpoint 135 makes Light fresh light-source creation, while Faerie Fire remains explicit group illumination of existing targets;
- checkpoint 130 makes Magic Missile stop reusing generic `Move This There!`; it uses fresh projectile creation plus immediate movement.

The regression suite records every remaining exact duplicate recipe so a new accidental collision fails tests.

## 9. Design rule

The SRD list is a **coverage benchmark**, not a vocabulary shopping list.

A D&D spell name does not justify a new Cuspell root.

Prefer:

1. existing composition;
2. existing Old Names/world concepts;
3. a small reusable semantic addition only if several effects expose the same missing distinction.

The beginner set should remain a teachable window into the full language, not a second spell language.
