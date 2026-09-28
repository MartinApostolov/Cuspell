# Yona Chapters 1–14 + 47 — Vocabulary Classification Pass


> **Historical scope note:** this document preserves the original Chapters 1–14 + 47 classification pass. The current extended inventory through Chapter 50 is in `YONA_CH01_50_VOCABULARY.md`, with structural findings in `../corpus/yona/CH01_50_V08_FULL_PASS.md`.

_Status: second vocabulary/worldbuilding pass after the v0.7 semantic rerun_

This pass revisits the already-audited Yona material specifically to classify missing vocabulary as:

- **semantic root / molecule**;
- **Cuspell Old Name**;
- **Yona-world New Name**;
- **world ontology/classifier data**;
- or **defer until source/world history makes the category clear**.

It does not promote every source word into magical Old Name vocabulary.

## Classification rule

### Old Name

Use an Old Name when the concept plausibly belonged to the ordinary pre-magic language because society needed it for daily life, anatomy, work, travel, construction, food, violence, records, trade, and similar long-standing activities.

Examples in this pass:

- eye;
- ear;
- claw;
- tail;
- mouth;
- skin;
- corpse;
- fish;
- fisher;
- window;
- spoon;
- sailor;
- crew;
- captain;
- scent trail.

The English gloss is metadata only. The actual language form is the descriptive quoted Old Name.

### New Name

Use a New Name when the source introduces a later/specialized label for:

- a particular person or place;
- a newly identified species;
- a named Skill/Trait/Affinity;
- a System category;
- a technical System sense of an otherwise ordinary word;
- a setting-specific resource/category whose label was coined after the old-language cutoff.

This means ordinary and technical senses can split.

For example, ordinary human capability need not be the same lexical object as the Yona System category named `«Skill»`.

Likewise, Cuspell may have a generic semantic `Mana` root while the Yona-world resource conventionally named `«Mana»` is a world-specific New Name.

## Ordinary roots added

Some recurring source gaps are not object names at all. They are broad reusable predicates/processes that ordinary language needs directly.

This pass adds:

- Body
- Long
- Awake
- Open
- Locked
- Eat
- Attack
- Grab
- Bite
- Climb
- Fall
- Jump
- Stab
- Limp
- Sever

These remain semantic roots/molecules rather than Old Names because they productively describe many unrelated objects/events.

## Old Names added from chapter pressure

| English gloss | Actual Old Name | Why Old |
| --- | --- | --- |
| air | `«LifeGasMatter»` | basic environmental material known to ordinary society |
| fish | `«Water«MoveLifeThing»»` | common animal category |
| fisher | `«Get«Water«MoveLifeThing»»Human` | ordinary profession |
| eye | `«VisionBodyPart»` | common anatomy |
| ear | `«HearingBodyPart»` | common anatomy |
| claw | `«SharpBodyPart»` | common anatomy |
| tail | `«LongBodyPart»` | common anatomy |
| mouth | `«EatBodyPart»` | common anatomy |
| skin | `«SurfaceBodyPart»` | common anatomy |
| corpse | `«FormerLifeBody»` | ordinary life/death vocabulary |
| window | `«SeeThrough«PreventMoveThing»Part»` | ordinary construction vocabulary |
| spoon | `«Move«GiveLifeMatter»«UseThing»»` | ordinary tool vocabulary |
| scent trail | `«SmellPath»` | ordinary tracking/perception vocabulary |
| sailor | `«Use«Big«MoveInLiquidThing»»Human` | ordinary profession |
| crew | `«Group«Use«Big«MoveInLiquidThing»»Human»` | ordinary work/social group |
| captain | `«Control«Group«Use«Big«MoveInLiquidThing»»Human»»Human` | ordinary occupational role |
| tree branch | `«Part«BigHard«GrowLifeMatter»»` | ordinary plant-part vocabulary |
| tree bark | `«Surface«BigHard«GrowLifeMatter»»` | ordinary plant-part vocabulary |

These join the civilization seed that already covers house, door, wall, road, bridge, boat, ship, food, medicine, poison, tool, weapon, blade, sword, blood, bone, flesh, market, settlement, records, books, maps, and similar ordinary concepts.

## Residual ordinary vocabulary added in pass 2

The second pass closes the ordinary buckets that were still explicitly listed after the first pass.

### Reusable semantic roots / molecules

- `Damage(subject) -> EvaluationValue` for ordered physical-damage degree;
- `Depth(subject, frame?) -> Quantity:Length` for contextual penetration/depth;
- `Hunger(subject) -> EvaluationValue` plus contextual `Hungry` and `Sated` state Properties;
- `TextureOf(subject) -> TextureProfile`;
- `Sound` as the broad acoustic-phenomenon Kind/domain and `Loudness(subject) -> EvaluationValue`;
- `Dodge(agent, threat?) -> EventSpec`;
- `Reflexive(event) -> Proposition`;
- contextual `CamouflagedAgainst(subject, background, observer?)`;
- persistent `Injured(subject)` state.

The paired Attribute/Property design is deliberate. For example, `Hunger` supplies an ordered degree while `Hungry` supplies the ordinary thresholded state. `Sated` is not declared the logical Opposite of `Hungry`: intermediate states can exist.

Camouflage remains observer/background-sensitive. `ColorOf` and `TextureOf` express the concrete appearance data rather than hiding it inside a magically objective one-word shortcut.

### Additional ordinary Old Names

| English gloss | Actual Old Name | Why Old |
| --- | --- | --- |
| organ | `«UseBodyPart»` | ordinary anatomy; historically foregrounds a functional body part |
| stomach | `«Eat«UseBodyPart»»` | ordinary anatomy; later term built from the earlier Organ Old Name |
| wrist | `«JoinHandBodyPart»` | ordinary anatomy; historically foregrounds the hand-joining region |
| tendon | `«MoveJoinBodyPart»` | ordinary anatomy; historically foregrounds connective movement function |
| wound | `«InjuredBodyPart»` | ordinary injury vocabulary; localized injury-site concept |

As with the earlier Old Names, these are historical names, not live classifiers. Their objective membership rules still belong to world ontology.

## Yona New Names added

### People / place

- `«Yona»`
- `«Abby»`
- `«Sally»`
- `«Henry»`
- `«Ryan»`
- `«Oakville»`

### System terminology

- `«System»`
- `«Quest»`
- `«Skill»`
- `«Trait»`
- `«Class»`
- `«Profession»`
- `«Species»`
- `«Race»` as a technical synonym for the Species category where the source uses it
- `«Affinity»`
- `«Level»`
- `«Tier»`
- `«Proficiency»`
- `«Stage»`
- `«Status Window»`
- `«Royal Status Window»`
- `«Evolution»`
- `«Mana»`
- `«Stat»`
- `«Experience»`

The capitalized/technical meaning is the important distinction. An ordinary old-language word with similar spelling or gloss would be a separate lexical/history question.

### Proficiency values

- `«Early»`
- `«Middle»`
- `«Peak»`

These are System-specific ordered labels, not claims that the ordinary temporal/adjectival meanings are magical vocabulary.

### Species names

- `«Ichthyoid»`
- `«Encheloid»`
- `«Octopoid»`
- `«House Cat»` as a System species/evolution label

### Named Skills

- `«Scratch»`
- `«Food Sense»`
- `«Stomach of the Glutton»`
- `«Blink»`
- `«Snatch»`
- `«External Mana Manipulation»`
- `«Mana Barrier»`
- `«Mana Burst»`
- `«Spatial Slice»`
- `«Ember»`

### Trait / Affinity names

- `«Gluttony»`
- `«Spatial Affinity»`
- `«Fire Affinity»`
- `«Unattributed Mana Affinity»`


## Exact Yona-specific rank, evolution, and Skill-upgrade names

These labels are setting/System vocabulary and are therefore **New Names**, not Cuspell Old Names, even when their component words are ordinary English-looking terms.

### Metal rank values

Chapter 13 explicitly establishes the Yona Guild/threat metal ranking vocabulary:

- `«Bronze»`
- `«Silver»`
- `«Gold»`
- `«Platinum»`

They are registered as Yona-specific `OrderedValue` concepts. The chapter directly uses Bronze/Silver for Adventurer ranks and Silver/Gold/Platinum for threat severity. The shared metal labels are world technical values; their exact progression/rank rules remain Yona-world ontology.

"Low Silver threat" is not registered as a separate invented rank. It remains a use of the Silver band with a lower-within-band qualifier until the setting explicitly defines a formal subrank.

### Evolution options explicitly named in Chapter 8

The source presents thirteen evolution choices, but only five are actually named in the audited prose. Exactly those five are registered:

- `«Greater Spatial House Cat»`
- `«Gluttonous House Cat»`
- `«Slothful House Cat»`
- `«Spatial Thief House Cat»`
- `«Gluttonous Devourer House Cat»`

The other eight remain unregistered rather than being guessed.

### Skill-upgrade options explicitly named in Chapter 15

Chapter 15 explicitly displays four upgrades for `«External Mana Manipulation»`:

- `«External Mana Manipulation - Constructs»`
- `«External Mana Manipulation - Anatomical Constructs»`
- `«External Mana Manipulation - Equipment Constructs»`
- `«External Mana Manipulation - Fire»`

It also establishes `«Meditate»` as a named System Skill and displays seven upgrade choices:

- `«Meditate - Deep»`
- `«Meditate - Alert»`
- `«Meditate - Split»`
- `«Meditate - Efficient»`
- `«Meditate - Sensitive»`
- `«Meditate - Precise»`
- `«Meditate of the Glutton»`

All eleven upgrade labels are Yona-specific New Names. Selecting an option may make that label the name of an upgraded Skill in-world, but the name remains a later technical/System name and gains no Old-Name magical compression.

## Why most Yona terminology is New rather than Old

The System vocabulary is specialized technical ontology.

Even if a pre-magic society already had ordinary concepts corresponding to words such as "class", "skill", "trait", "level", "profession", or "species", the source's capitalized System meanings have explicit rules, progression, unlock conditions, and values.

Therefore the technical denotation is registered as a New Name rather than retroactively granting an ancient magical Old Name to the System concept.

This also prevents an accidental exploit where a modern game/system taxonomy inherits magical compression merely because it reused an old ordinary word.

## World package boundary

Yona-specific vocabulary lives in:

- `world/yona/concepts.json`
- `world/yona/new_names.json`

It is opt-in:

`Language.load(root, world_package="yona")`

The default core world does not automatically know Ichthyoid, Blink, Abby, the System, etc.

Core civilization Old Names remain available when the Yona package is loaded.

## World-history decisions supplied after the audit

The previously deferred historical classifications are now encoded in core vocabulary:

- **monster** — pre-magic Old Name `«AttackHumanThing»`;
- **god/deity** — pre-magic Old Name `«WorshipThing»`;
- **goddess** — pre-magic Old Name `«Female«WorshipThing»»`;
- **mana** — pre-magic Old Name `«Use«WorshipThing»Magic»`, reflecting the older understanding of mana as god-used/divine magic rather than an ordinary human-usable technical resource;
- **meditation** — ordinary pre-magic Old Name `«AwakeSleep»`;
- **telepathy** — still undecided; do not force it into Old or New until its history is established.

The productive roots `Female` and `Worship` were added to core because they are broadly reusable ordinary vocabulary. Worship does not entail objective divinity.

The historical wording of these Old Names is not a live classifier. Monster, deity, goddess, mana, and meditation membership still belongs to world ontology.

Yona-specific `«Mana»` and `«Meditate»` remain separate New Names and do not inherit Old-Name magical compression from the older concepts.

No generic `Divine` root has been introduced yet; its objective semantic boundary remains future world-ontology work.

## Remaining vocabulary work

The seven explicitly listed **ordinary** residual buckets from the first pass are now closed at the language/world-vocabulary level: dodge; injury/wounds; reflexive body motion; camouflage/texture; hunger/satiety; sound/intensity; and the currently identified additional anatomy.

This still does not claim universal lexical completeness. Fresh chapters may expose new ordinary concepts, and objective classifiers/generation profiles remain world-ontology work.

The exact threat-rank labels and currently source-visible evolution/Skill-upgrade labels are registered as Yona-specific New Names. The previously deferred monster/deity/goddess/pre-magic-mana/ordinary-meditation vocabulary is now encoded in core. Telepathy is the only still-undecided history-dependent item from this audit, plus whatever new exact setting labels fresh chapters expose.

