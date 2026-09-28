# Yona Chapters 1–14 + 47 — Vocabulary Classification Pass

_Status: first vocabulary/worldbuilding pass after the v0.7 semantic rerun_

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

## Deferred / history-dependent cases

The following should not be forced into Old or New without more world-history evidence:

- **monster** — Old if pre-magic society already had a stable monster category; New if monsters arrived with/after the System;
- **goddess / divine categories** — depends on whether these were established referents/concepts before magic became executable;
- **mana terminology in Cuspell's own world** — the generic root exists for the magic system, but specific cultures/resources may still have New Names;
- **telepathy** — ordinary conceptual description is possible, but the source may use a setting-specific named technique/channel;
- **meditation** — likely ordinary/pre-magic, but the source sometimes treats it as a mechanically effective technique/Skill, so ordinary practice and System technique should be separated;
- **monster threat ranks such as Silver** — clearly technical when used as a System/world rank, but exact rank ontology should be registered from source data rather than guessed;
- **Skill upgrade names/evolution option names** — New Names, but add each only when its exact source spelling/referent is audited.

## Remaining vocabulary work

This pass does not claim lexical completeness.

The earlier chapter audit still exposes ordinary/action vocabulary such as dodge, wound/injury detail, reflexive body motion, camouflage/texture vocabulary, hunger/satiety, sound/intensity language, and additional anatomy.

The next pass should add these only when their semantics can be typed cleanly.

For Yona-specific vocabulary, continue source-by-source and add exact New Names rather than inventing approximations.

