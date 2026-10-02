# Checkpoint 106 — Civilization Vocabulary Coverage Audit

_Status: documentation-only coverage audit; no names or semantic entries added_

## Scope

This checkpoint audits whether current Cuspell can support ordinary civilization/world communication using the existing combination of:

1. productive semantic roots and grammar;
2. frozen historical Old Names;
3. ordinary New Names;
4. world-package concepts/classifiers.

The audit deliberately does **not** assume that every English noun deserves an Old Name, and it does not reopen the root-minimization sweep.

Source-of-truth material inspected:

- `language/core/lexicon.json` — 206 registered base entries / 256 frames;
- `language/core/types.json`;
- `language/names/old_names.json` — 102 Old Names;
- `world/core/concepts.json` — 96 core concepts;
- `world/core/new_names.json`;
- `world/yona/concepts.json` and `world/yona/new_names.json`;
- player Old/New Name projections;
- current Names/worldbuilding, Kind, time, space, vocabulary-layer specs;
- civilization, cross-genre, Yona, possession, social, time/space, and written-regression tests.

The existing 102 Old Names are distributed unevenly because many were added under corpus pressure:

- biology: 14;
- anatomy: 13;
- artifacts: 13;
- information: 10;
- roles: 9;
- built environment: 8;
- institutions: 7;
- materials: 5;
- resources: 4;
- measurement: 3;
- transport: 2;
- social groups: 2;
- religion: 2;
- economy: 1;
- physics: 1;
- practice: 1;
- magic: 1;
- canonical Units: 6.

That is a useful base, but it is not yet a balanced civilization vocabulary.

## Classification used

Every apparent gap is classified as one of the following:

1. **Compositional** — existing semantics can express it naturally enough without a new lexical item.
2. **Old Name candidate** — common, culturally salient pre-magic vocabulary that speakers would plausibly lexicalize.
3. **New Name category** — individual people, places, institutions, artifacts, titles, local technical terms, etc. handled by ordinary Name facts.
4. **Semantic-language gap** — current roots/types/frames cannot state an important distinction accurately.
5. **World-model concept** — the concept needs a stable classifier/value in a world package, but not necessarily a new semantic rune.

A sixth audit note is used where necessary:

6. **Lexicalization-mechanism pressure** — the meaning is compositionally expressible, but current Old Names do not provide a parameterized historical verb/relation mechanism. This is not a semantic gap by itself.

## Domain coverage

| Domain | Current coverage | Main finding |
| --- | --- | --- |
| People / kinship | strong semantic, partial lexical | ParentOf, SpouseOf, EngagedTo, FriendOf, Family and Human cover the structure. Child is inverse ParentOf; sibling/grandparent/cousin can be composed. Common sex/kin vocabulary remains thin. |
| Body / anatomy | partial | Body, Hand, Eye, Ear, Mouth, Skin, Bone, Flesh, Blood, Organ, Stomach, Wrist, Tendon, Wound exist, but ordinary high-frequency anatomy is still missing. |
| Animals / plants / ecology | partial/world-dependent | Animal, Plant, Tree, Bush, Fish, Cat and several parts exist. Species/taxa should mostly be world concepts + Old Names, not semantic roots. |
| Food / agriculture | partial | Food, Farm, Farmer, Fisher, food store, Eat and transfer semantics exist. Crop/seed/grain/cooking vocabulary is thin. |
| Materials / resources | partial | Water, Air, Stone, Wood, Metal, Fire, Poison, Medicine exist. Common craft materials and specific metals are absent. |
| Tools / craft / manufacturing | partial | Tool, cutting tool, blade, sword, hammer, shovel, container, bucket, rope, spoon exist. Core craft/production technology is underrepresented. |
| Clothing | minimal but serviceable | General Clothing exists. Culture-specific garment names do not need core semantics; very common footwear/armor may deserve Old Names. |
| Buildings / architecture | moderate | House, Door, Wall, Window, Road, Bridge, Well and several institutions exist. Building-part and production-building vocabulary is thin. |
| Settlements / geography | weak outside settlement | Settlement and general Region/Path/Map semantics are good, but natural geographic feature vocabulary is mostly absent. |
| Transport / navigation | maritime-biased | Boat, Ship, Sailor, Crew, Captain exist. Land transport and navigation vocabulary are missing. Direction is a semantic type, but fixed world directions need world values/names. |
| Trade / economy | strong semantics, thin lexicon | Transfer, Own, Have, Obligated, Concurrent, Currency, Market and Contract can model exchange, debt and obligations. Buy/sell/trade/price are not primitive and can become verbose. |
| Property / ownership | strong | Own, Have, Transfer, Begin/End and obligations are enough for possession, acquisition, loss, gifts and inheritance descriptions. |
| Government / authority | strong semantics, partial lexical | Control, Permitted, Obligated, Rule, Law, Leader, Council, Court and ResponsibleFor cover the machinery. Polity/citizen/office/title vocabulary is thin. |
| Law / crime / punishment | semantically adequate, lexically thin | Theft and murder can be described through ownership, permission, responsibility and End Life. Judge/prison/trial/crime/punishment are plausible Old/world concepts. |
| War / military | weak lexical | Attack, Weapon, Sword and Guard exist, but Soldier/Army/Armor/Shield/Spear/Bow/Arrow/War/Battle are absent. |
| Medicine / health | **semantic pressure** | Damage, Hunger, Life, Medicine, Healer, Hospital and Wound do not cleanly express pain, illness or general health state. |
| Education / knowledge | strong | Know, Understand, Remember, Believe, Infer, Question/Answer, Teacher, School, Book and Record provide good coverage. Learn remains compositional as a state transition. |
| Writing / records | strong semantics, lexical-action pressure | Sign, Word, Language, Record, Book, Letter, Meaning and Say are strong. Reading/writing can be composed, but there is no compact historical parameterized lexeme mechanism. |
| Language / communication | strong | Say, Meaning, Name, Understand, Sense, Messenger, Word, Language and Letter cover the core. |
| Religion / ritual | partial | Deity, Goddess, Worship, divine mana and Meditation exist. Temple/priest/prayer/ritual/sacrifice are absent; soul/spirit should be setting-dependent unless metaphysics requires them. |
| Art / music / entertainment | weak | Almost no historical noun vocabulary exists for music, song, instrument, story, image/painting, dance, game or performance. |
| Time / calendar | strong mechanics, thin vocabulary, one frame gap | TimePoint/TimeInterval/Event, Before/During/Interval/IntervalFor, Calendar, Clock and DurationUnit are strong. Day/night/year/month/season/date/age are missing. Referenced TimeIntervals lack Begin/End/Extent accessors. |
| Measurement | strong | Quantity/dimensions, Unit, Length/Area/Volume/Mass/Heat/Light/Density/Rate and measure tools are adequate. Conventional units beyond the six canonical units can remain world/history vocabulary. |
| Occupations / social roles | partial | Farmer, Fisher, Healer, Teacher, Messenger, Guard, Leader, Sailor, Captain exist. Craft/trade/religious/legal/military roles are uneven. |
| Organizations / groups | strong semantics, thin historical labels | Group + Member handles generic organizations. Named institutions use New Names; common organization Kinds such as army/guild/temple/company may be Old/world concepts. |
| Technology / infrastructure | era-dependent and thin | Roads, bridges, wells and basic institutions exist. Mills, furnaces, ports, sewers, aqueducts, carts, etc. should depend on the intended historical/technological baseline. |
| Natural phenomena / weather | weak | Fire, Air, Water and Sound exist, but sky/cloud/rain/snow/wind/storm/river/lake/sea/mountain/forest etc. are largely absent. |
| Abstract social concepts | strong | Obligation, permission, responsibility, ownership, reputation, trust, affection and evaluation are unusually well covered already. |
| Fantasy / magical-world vocabulary | correctly layered | Magic is semantic; ancient divine mana is an Old Name; Yona System terms, Skills, Classes, Professions, ranks and species are correctly handled as world-package concepts + New Names. |

## High-priority Old Name candidate families

These are **candidate families**, not an instruction to add every item immediately.

### A. Basic anatomy

Strong candidates because they are extremely frequent, objectively classifiable world Kinds, and awkward to rebuild constantly:

- head;
- face;
- arm;
- leg;
- foot;
- finger;
- nose;
- tooth/teeth;
- tongue;
- heart;
- brain;
- hair.

The current registry is visibly corpus-shaped: Wrist, Tendon and Stomach exist while Head, Foot and Tooth do not.

### B. Natural world and geography

Strong candidates for a civilization-scale common lexicon:

- soil/earth;
- sand;
- river;
- lake;
- sea/ocean;
- mountain;
- hill;
- island;
- coast/shore;
- forest;
- field;
- sky;
- cloud;
- rain;
- snow/ice;
- wind;
- storm.

Many are compositionally describable, but repeated descriptive reconstruction would be unnatural. Exact membership belongs to world classifiers.

### C. Food/agriculture and common materials

Likely candidates, subject to world ecology/technology:

- seed;
- leaf;
- fruit;
- grain/crop;
- bread or equivalent staple;
- milk;
- salt;
- clay;
- cloth/textile;
- leather/hide;
- glass;
- fuel;
- culturally important specific metals/materials.

Specific species, crops and materials should be added only when the world actually contains and culturally distinguishes them.

### D. Craft, transport and infrastructure

Likely historical vocabulary if the target civilization has the technology:

- knife;
- axe;
- saw;
- pot/cooking vessel;
- needle;
- wheel;
- cart/wagon;
- plow;
- loom;
- furnace/kiln;
- anvil;
- sail;
- oar;
- anchor;
- port/harbor;
- roof;
- room;
- floor;
- building/structure;
- workshop;
- mill;
- fortification.

These should not become semantic roots merely because English has short words for them.

### E. War / law / public institutions

Likely Old/world concepts where culturally present:

- soldier;
- army;
- armor;
- shield;
- spear;
- bow;
- arrow;
- prison;
- judge;
- trial;
- government/state/polity;
- citizen/member-of-polity;
- temple;
- priest.

Specific official titles, named armies, named courts and named temples are New Name data.

### F. Art, ritual and shared culture

The current core has almost no vocabulary here. Candidate concepts include:

- music;
- song;
- musical instrument;
- story/tale;
- image/painting;
- dance;
- game/play-object;
- ritual;
- prayer.

Several of these describe events/processes rather than ordinary artifact Kinds, which connects to the lexicalization-mechanism issue below.

### G. Calendar / daily life

Likely historical words:

- day;
- night;
- year;
- season;
- month where the world's calendar has one;
- date/calendar-day;
- age.

Week-like periods are cultural and should be world vocabulary, not assumed universal semantics.

## Concepts that should usually stay compositional

The audit does **not** justify restoring convenience roots for meanings that current semantics already state precisely.

Examples:

- child-of — reverse ParentOf roles;
- sibling — shared parent constraint;
- grandparent — chained ParentOf;
- acquisition/loss — Begin/End Have or Own as appropriate;
- gift — Transfer plus ownership/permission/context facts;
- inheritance — transfer/ownership change constrained by death, kinship, law/contract;
- debt — persistent Obligation to Transfer;
- tax — Obligation to Transfer under an authority/law context;
- theft — acquisition/transfer/ownership change without the relevant permission;
- killing — Cause End Life;
- murder — killing plus the applicable permission/legal/responsibility conditions;
- army as a collection — Group/Member once Soldier is available;
- student — participation/member/learning relation to a School or teaching process;
- reading — sensing a Sign plus Meaning/Understand;
- writing — causing Sign existence/persistence;
- building/making — Cause/Change/Begin Joined/Whole/Purpose combinations when the exact construction matters;
- buying/selling/trading — coupled Transfer/Own changes and reciprocal obligations.

These may still receive historical vocabulary if ordinary speech needs compact words, but that is a lexicalization decision rather than evidence for new semantic primitives.

## New Name categories that are already handled correctly

No additional grammar is needed for:

- personal names;
- settlement/place names;
- named roads, rivers, mountains, ships, weapons or buildings;
- named governments, guilds, schools, temples, armies or companies;
- occupational titles tied to one institution;
- named laws, treaties, books, calendars and currencies;
- named festivals/holidays;
- named species/classes/skills/traits/ranks in a particular setting;
- named directions or reference frames when the world supplies an actual Direction/CoordinateFrame value.

The Yona package already demonstrates this architecture at scale: hundreds of setting concepts and 329 current New Name facts remain outside the generic semantic root inventory.

## Actual semantic-language gaps / pressure

### 1. Health, illness and pain

Current Cuspell can state:

- Life;
- physical Damage;
- Wound Kind;
- Hunger;
- Medicine/Healer/Hospital vocabulary.

It cannot cleanly distinguish:

- subjective pain from tissue damage;
- illness/sickness from generic Damage;
- general health state from Life/non-Life.

Those distinctions matter to ordinary conversation, medicine and magic. Treat this as real semantic pressure rather than trying to define Pain as Damage or Illness as Low Life.

Recommended next design task:

- decide whether health is an ordered Attribute, a family of state Properties, or both;
- preserve Pain as an experience distinct from physical Damage;
- let named diseases remain world concepts/Names unless a general disease relation is independently justified.

### 2. Biological sex classification is asymmetric

The core has **Female** as a reusable Property but no corresponding positive male/sex classification system.

`Not Female` is not generally equivalent to Male unless the world ontology explicitly makes that exhaustive binary assumption.

A civilization that discusses parentage, animals, reproduction and social roles needs a positive, objective sex-classification path.

Recommended next design task:

- decide between a symmetric Male/Female property pair and a typed Sex attribute/value family;
- do not infer a universal metaphysics from English grammar;
- keep man/woman/mother/father etc. as Old/world concepts or compositions once the underlying classifier is sound.

### 3. Referenced TimeInterval boundary/extent access

The language can construct:

- `Interval(start,end)`;
- `IntervalFor(start,duration)`.

But current callable frames expose:

- `Begin(Event) -> TimePoint`;
- `End(Event) -> TimePoint`;
- `Extent(Event) -> Quantity:Time`;

not the same accessors for an already referenced **TimeInterval**.

That makes ordinary questions such as “when does this interval end?” or “how long is this named interval?” unnecessarily unexpressible once the construction history is unavailable.

This does **not** require new roots. The likely repair is coherent typed generalization:

- `Begin(TimeInterval) -> TimePoint`;
- `End(TimeInterval) -> TimePoint`;
- `Extent(TimeInterval) -> Quantity:Time`.

### 4. Historical lexicalization of parameterized verbs/relations

Old Names currently work very well for frozen Kind concepts, Units, and closed frozen expressions.

They do not currently provide an obvious historical mechanism for a common **parameterized** lexical item such as:

- buy(agent,item,seller/payment...);
- sell(...);
- read(reader,sign/information);
- write(writer,sign);
- trade(participants/resources);
- pray(worshipper,deity/content);
- dance(agent/...).

All of these can be expressed compositionally, so this is **not** a semantic-language gap.

It is, however, a vocabulary-system pressure: if common historical verbs can only be compact when promoted to semantic roots, the noun-focused Old Name mechanism may force the core root inventory to carry lexical frequency rather than semantic necessity.

Recommended next design task:

- explicitly decide whether common parameterized meanings are expected to remain multi-rune compositions forever;
- or extend the historical lexicalization model with safe typed parameterized semantic molecules that preserve frozen mana cost without becoming arbitrary player macros.

Do not add such a mechanism merely to imitate English one-word verbs; add it only if real corpus/civilization pressure shows repeated unnatural verbosity.

## World-model gaps rather than rune gaps

Several missing concepts require objective world data, not new semantic roots:

- species/taxa and lineage classifiers;
- exact anatomical classifiers;
- specific materials/elements;
- disease categories;
- geographic feature membership;
- polity/citizenship/institution definitions;
- calendar systems and cultural periods;
- cardinal/global directions and coordinate frames;
- technological artifact classes;
- religious metaphysics such as soul/spirit/afterlife;
- setting-specific magical resources and progression systems.

The current Yona package already shows the correct pattern for setting-specific concepts: world concepts + New Names rather than generic core roots.

## Review of existing Old Names

No current Old Name is automatically invalid, but the registry has several **coverage asymmetries** worth correcting before treating it as civilization-complete:

- Spoon exists while Knife/Pot/Needle do not.
- Wrist/Tendon/Stomach exist while Head/Foot/Tooth/Nose do not.
- Sailor/Crew/Captain exist while Soldier/Army/Armor do not.
- Goddess exists while the general biological sex system is Female-only.
- Scent Trail exists while River/Rain/Wind/Forest do not.
- Monster/divine mana/meditation exist while broad art/music vocabulary does not.

These are understandable products of corpus-driven development, not reasons to delete the existing entries. They are reasons not to mistake the current 102-name registry for a balanced historical lexicon.

A separate historical-baseline review should also confirm that broad concepts such as Hospital, School, Court, Currency, Contract and Clock fit the intended pre-magic civilization. Their current glosses are broad enough to include ancient equivalents (healing institution, teaching institution, tribunal, exchange token, obligation record, time-measuring tool), so none is inherently “too modern” if the classifier is kept at that broad level.

Two current world-concept descriptions deserve later classifier cleanup:

- Farm is described as a place **or** establishment.
- Market is described as a gathering **or** institution.

Those may be intentionally broad Kinds, but the world ontology should eventually specify whether one concept legitimately spans physical place, organization and event-like social institution, or whether the English gloss is hiding distinct Kinds.

## Overall result

The current language is **semantically much closer to civilization-capable than its noun list suggests**.

Strong general machinery already exists for:

- identity/reference;
- space and motion;
- time/events;
- possession/ownership/transfer;
- groups and institutions;
- obligation/permission/law;
- knowledge/records/language;
- social relations and emotions;
- measurement;
- objective world concepts and names.

The main deficiency is **lexical balance**, not a need for another broad root expansion.

Immediate follow-up should therefore be:

1. repair/decide the three clear semantic issues: health/pain, biological-sex classification, and TimeInterval accessors;
2. decide whether historical parameterized lexicalization is needed;
3. then add Old Names in balanced domain batches, beginning with anatomy + natural world/geography + ordinary craft/war/calendar vocabulary;
4. add setting-specific species, materials, technologies, institutions and proper names in world packages rather than the generic semantic core;
5. re-audit existing Old Name spellings/dependencies only after candidate concepts are chosen, so etymology work follows the vocabulary decision rather than driving it.

Checkpoint 106 therefore makes **no inventory change**:

- registered base entries remain **206**;
- semantic primitive candidates remain **125**;
- Old Names remain **102**;
- no new root, constructor, world concept or Name is accepted by this checkpoint.
