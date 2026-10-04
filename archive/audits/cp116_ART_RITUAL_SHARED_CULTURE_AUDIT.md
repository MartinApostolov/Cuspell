# Checkpoint 116 — Art, Ritual, and Shared-Culture Vocabulary Audit

_Status: sixth balanced civilization-vocabulary batch + typed world-Kind generalization_

## Purpose

Checkpoint 106 identified art/music/ritual/shared culture as one of the thinnest remaining civilization domains.

Checkpoint 115 then exposed a structural problem: many ordinary cultural nouns classify Events or Information rather than persistent Entities. Trial, Battle, War, Ceremony, Performance, Festival, Story, Song, and similar meanings should not be forced into Entity Kinds merely because the original world-Kind predication path assumed Entity subjects.

Checkpoint 116 audits the art/ritual/shared-culture domain and resolves that classifier pressure without adding a semantic root.

## Structural result — typed world Kind targets

Registered world concepts with:

`semantic_type: "Kind"`

may now optionally declare:

`classifies_types: [...]`

If the field is omitted, the default remains:

`["Entity"]`

so every pre-existing ordinary noun keeps its old behavior.

The parser uses the registered world concept's target type when an Old Name Kind is used predicatively.

Examples:

`«RuleSequence» ThisEvent.`

classifies an actual Event as Ritual/Ceremony.

`«RuleSequence» Move Self Here.`

classifies an EventSpec as Ritual/Ceremony.

`«Sequence«MeaningSign»» Question True.`

classifies an Information value as Story/Tale.

This is static typed classification. It does not guess a domain from context.

### Why no EventKind rune/type was added

A separate lexical or semantic EventKind root is unnecessary.

The existing semantic value `Kind` can remain the category value while the world concept records the type of values it classifies.

This also generalizes cleanly beyond Events to Information categories.

Direct productive Kind roots such as Thing, Matter, Sign, and Group retain their current frames and are not made universally polymorphic.

## Accepted persistent-Entity vocabulary

### Temple

Old Name:

`«Worship«JoinedInThing»»`

Cost: **4**.

World concept: `core.religion.temple`.

A temple is a persistent worship/religious facility or institution Entity.

### Shrine

Old Name:

`«Worship«UseThing»»`

Cost: **3**.

World concept: `core.religion.shrine`.

A shrine is a persistent devotional focus, sacred structure, or worship artifact Entity family.

### Priest

Old Name:

`«WorshipAuthority«Know«MoveLifeThing»»»`

Cost: **6**.

World concept: `core.roles.priest`.

A priest is a persistent religious-officiant role Kind. The historical wording uses the currently accepted Authority relation; the planned reduction audit may rewrite this dependency if Authority is later reduced through Permitted/deontic semantics.

### Musical instrument

Old Name:

`««HearingSequence»«UseThing»»`

Cost: **4**.

World concept: `core.artifacts.musical_instrument`.

A musical instrument is an artifact designed for producing or controlling musical sound/performance.

### Image / painting

Old Name:

`«Vision«PersistSignThing»»`

Cost: **4**.

World concept: `core.artifacts.image`.

This is the persistent physical/visual-representation artifact family. The represented content may be separate Information.

### Sculpture

Old Name:

`«Form«PersistSignThing»»`

Cost: **4**.

World concept: `core.artifacts.sculpture`.

This is the persistent three-dimensional artwork/representation artifact family.

## Accepted Event/EventSpec categories

These world concepts declare:

`classifies_types: ["EventSpec","Event"]`

### Ritual / ceremony

`«RuleSequence»`

Cost: **2**.

The historical wording foregrounds a prescribed/rule-governed sequence. Ritual may be religious or secular.

### Prayer

`«SayWorship»`

Cost: **2**.

The historical wording foregrounds speech within worship, but the frozen classifier may include silent or nonverbal prayer.

### Sacrifice / offering

`«TransferEndHaveWorship»`

Cost: **4**.

The historical wording foregrounds relinquishment/transfer in worship. A world's classifier determines whether dedication, destruction, symbolic offering, recipient, or exchange is required.

### Dance

`«RepeatMove»`

Cost: **2**.

The etymology foregrounds patterned/repeated movement. This is not a live reduction of Dance to Repeat Move.

### Performance

`«SensePurpose»`

Cost: **2**.

The historical wording foregrounds an event intended for observation/audience perception.

### Game / sport

`«RuleAttempt»`

Cost: **2**.

The historical wording foregrounds rule-governed attempts/goals. Specific sports, games, teams, and rulesets belong to world packages.

### Festival / feast

`«GroupHappyEat»`

Cost: **3**.

The etymology foregrounds communal celebration, happiness, and eating. None is a universal live requirement.

## Accepted Information categories

These world concepts declare:

`classifies_types: ["Information"]`

### Story / tale

`«Sequence«MeaningSign»»`

Cost: **3**.

A Story is narrative Information, not the physical Book, speaker, or record that carries it.

### Music / composition

`«HearingSequence»`

Cost: **2**.

This is musical content/composition Information. Its performance is an Event and the produced acoustic phenomenon may be Sound.

### Song

`«Say«HearingSequence»»`

Cost: **3**.

A Song is a vocal-musical composition Information category. A particular singing occurrence is a Performance/Event.

## Important distinctions

Checkpoint 116 deliberately separates:

- Story Information from Book/Record Entities;
- Music/Song composition from Performance Events;
- Image/Painting artifacts from represented Information;
- Ritual category from Worship Process;
- Prayer category from Say Process;
- Dance category from generic Move;
- Festival category from one exact Sequence of events.

This lets ordinary vocabulary be concise without pretending that historical etymology supplies exact live mechanics.

## No new action roots

Checkpoint 116 does not add:

- Dance;
- Sing;
- Play;
- Perform;
- Pray;
- Celebrate;
- Sacrifice;
- Tell;
- Paint;
- Sculpt;
- Compose;
- generic Art.

An event can be classified as Dance or Performance without Cuspell thereby acquiring a one-rune executable constructor for an unspecified dance/performance.

To magically cause a specific performance, movement, song realization, ritual sequence, etc., the EventSpec still needs enough actual structure/reference to be objectively determined.

This preserves the language-validity vs magical-execution boundary.

## Proper names and setting vocabulary

Specific names remain New Name/world data:

- named temples/shrines;
- priestly offices and orders;
- named rituals;
- holidays/festivals;
- named stories/songs/compositions;
- named games/sports;
- artistic styles;
- named instruments;
- specific paintings/sculptures;
- gods/religions/cults beyond the accepted broad core categories.

A civilization may also have world-specific Old Names for culturally central categories if they predate the magical cutoff.

## Inventory effect

Before checkpoint 116:

- 212 registered base entries;
- 131 semantic primitive candidates;
- 55 formal constructors;
- 265 semantic frames;
- 48 multi-frame entries;
- 182 Old Names;
- 175 core world concepts.

After checkpoint 116:

- **212 registered base entries**;
- **131 semantic primitive candidates**;
- **55 formal constructors**;
- **265 semantic frames**;
- **48 multi-frame entries**;
- **198 Old Names**;
- **191 core world concepts**.

Old Name meaning distribution becomes:

- **191 concept/Kind Old Names**;
- **6 Unit Old Names**;
- **1 parameterized expression Old Name**.

No New Name is added.

## Regression effect

Checkpoint 116 adds seven art/ritual/culture classifier regressions.

Expected suite size:

**647 tests**.

## Authority note

The user correctly raised that `Permitted` may make checkpoint-115 `Authority` reducible.

Checkpoint 116 intentionally does not redesign that relation mid-sweep.

The roadmap now explicitly queues Authority for the planned post-vocabulary reduction/redundancy audit, where it should be tested against Permitted, Obligated, Rule/Law, Control, and world-context constructions under the same exactness standard used by the earlier reduction passes.

## Result

The art/ritual/shared-culture layer is now substantially balanced, and the world concept system can classify Events/EventSpecs and Information without forcing them into Entity ontology.

The final planned balanced civilization-vocabulary domain is:

**calendar and daily life**.

After that batch, run the dedicated reduction/redundancy audit over productive meanings added or restored during the civilization work.
