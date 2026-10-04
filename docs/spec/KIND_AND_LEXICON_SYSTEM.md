# Kind, Noun, and Lexicalization System

_Status: working specification v0.1_

This file addresses the earlier problem:

> How can Cuspell identify specific kinds such as Water, Iron, Oak, Wolf, Human, Hand, and Sword without making every noun an irreducible semantic primitive, requiring absurd descriptions, or allowing player-created aliases to become free magical compression?

The solution is deliberately plural rather than forcing every noun through one mechanism.

## 1. Core distinction: Kind semantics versus word length

A **Kind** is a semantic class.

A **rune/word** is a lexical encoding of a meaning.

Those are separate questions.

A Kind may be represented by:

- one atomic lexical root;
- a transparent compound;
- a conventional semantic molecule;
- a longer predicate definition.

Therefore the language does **not** need a rule that all Kinds must be compositionally derived from a tiny primitive inventory.

Likewise, having a one-rune word for a Kind does not make that Kind ontologically primitive.

This is important for both language naturalness and mana balance.

## 2. Four sources of Kinds

## 2.1 Ontological base Kinds

Very general classes used by the semantic system itself.

Examples:

- Thing
- Matter
- Information
- possibly Mind-system / living-organism classes

These are close to the ontology and are likely atomic roots.

## 2.2 Canonical natural Kinds

Kinds whose identity is determined by an objective classification rule that is not conveniently reducible in ordinary casting language.

Examples may include:

- Water
- Iron
- Oak
- Wolf
- Human

A canonical natural-Kind rune can be lexically atomic while its recognition semantics are defined by the world's ontology.

This is **not** an arbitrary alias.

Reality/the formal language recognizes the Kind through a fixed classifier.

## 2.3 Defined semantic Kinds

Kinds defined by a stable predicate structure.

Examples may include:

- Container
- Weapon
- Door
- Medicine
- Sword

Their semantics can reference:

- intrinsic Properties;
- structure/mereology;
- spatial Relations;
- normal function/purpose;
- Process affordances;
- material constraints.

The language may leave such a definition transparent as a compound, or later lexicalize it as a conventional short rune.

## 2.4 Ad-hoc restricted Kinds

Any objective predicate can restrict a Kind for the current expression.

Examples:

`RedMatter`

`SolidMatter`

"Humans currently In this room"

These do not require permanent dictionary entries.

Their identity is exactly the predicate expression written.

## 3. Lexical atomicity does not imply semantic primitiveness

A crucial rule:

> A one-rune lexical item may denote a semantically complex recognized Kind.

Natural languages do this constantly, and Cuspell can do it without sacrificing objectivity because the rune's semantic entry is fixed in the language specification.

For magic:

- writing the accepted root costs one semantic rune;
- reality uses the root's registered meaning;
- the caster does not pay the expanded definitional length.

This is legitimate linguistic compression and is intentionally powerful.

It follows the established principle that knowledge of the language can reduce mana cost.

## 4. Why this does not permit arbitrary aliases

A personal name, abbreviation, or user-defined macro is not automatically a lexical semantic root.

Suppose a caster says:

`Bob = gigantic city-destroying explosion`

The Sign `Bob` may Name that description in ordinary Information semantics, but it does not gain an entry in the magical lexicon.

Magic resolves written semantic roots through the language's registered lexicon, not through arbitrary local definitions.

Therefore:

- Name/alias relation: informational reference only;
- registered semantic root: executable lexical meaning.

Only the second grants mana compression.

## 5. Lexicon registration

For specification purposes, a **registered lexical item** has:

- lexical form/rune identity;
- semantic Category;
- Domain;
- Traits;
- Frames;
- constraints/recognition rule;
- magical-execution status;
- canonical normalization target if derived.

A new conventional rune becomes magical compression only when it is part of the language's recognized lexicon.

The worldbuilding mechanism for how new runes become recognized—discovery, divine origin, ancient formalization, collective standardization, etc.—is deliberately separate from the semantic rule.

## 6. Recognition predicates

A canonical Kind must have an objective recognition predicate.

The predicate may be implemented conceptually at a level inaccessible to ordinary casters.

For example, the language can recognize a substance's microstructure without requiring the caster to write an atomic formula.

This is comparable to a programming language having a primitive type whose implementation is deeper than its source spelling.

Recognition rules belong to the language ontology, not to GM improvisation during casting.

## 7. Material Kinds

Material/substance identity should use **composition/structure identity**, not temporary physical state.

Therefore a canonical Water Kind, if adopted, should denote the substance identity rather than merely "liquid matter."

Conceptually:

`Water(x)`

may remain true when the substance is:

- liquid;
- solid/ice;
- gas/vapor;

provided it still satisfies the language's Water-substance recognition rule.

This immediately explains why:

`LiquidMatter`

is not Water.

Liquid is a phase Property; Water is a material Kind.

Likewise Iron is a material/element Kind, not equivalent to:

`SolidMetalMatter`

which is much broader.

### Mixtures

Mixture handling must be explicit.

A mixed Entity can:

- contain Part material of Kind Water;
- have a composition fraction/ratio;
- fail to be itself pure Water.

The later measurement/composition system will define thresholds and mixture quantities.

Ordinary conversational "water" may tolerate impurities, but magical Water should use the lexicon's explicit purity/composition rule or a mixture construction.

## 8. Biological Kinds

Biological Kinds should not be defined merely by a list of visible Properties.

Tree, Oak, Wolf, Human, etc. are better modeled through a **biological lineage/taxon classifier** in the world's ontology.

A biological Kind can use factors such as:

- developmental organization;
- heredity/lineage;
- organism structure;
- reproductive/genetic/magical inheritance rules appropriate to the setting.

The precise classifier is world-model data, not a caster-written description.

This prevents absurd definitions such as trying to define Human as "two-legged living matter with a mind."

It also leaves room for fantasy biology where species identity may involve souls, magical lineage, transformation, or non-DNA inheritance.

## 9. Taxonomic level must be explicit

There is no universal function:

`KindOf(This)`

because an organism belongs to many nested Kinds.

If the language later supports reference-by-example, the classifier must name its dimension/level.

Examples of possible typed relations:

- SameSpecies(A,B)
- SameGenus(A,B)
- SameLineage(A,B)
- SameSubstance(A,B)
- SameDesign(A,B)

The exact inventory is deferred.

The important rule is that generic "same kind" is not magical shorthand.

## 10. Anatomical Kinds

Anatomical nouns such as Hand are not well captured by generic `PartLifeMatter`.

They should use a canonical anatomical Kind or a stable semantic molecule whose classifier includes:

- organism-relative structural position;
- developmental/homological identity;
- normal functional role;
- relation to neighboring anatomical structures.

A Hand remains a Hand even when injured, because Kind identity is not identical to perfect function.

This argues for lexicalizing common anatomy rather than repeatedly spelling long relational definitions.

## 11. Artifact Kinds

Artifacts such as Sword, Door, House, Container, Clothing, and Tool often depend on **design/function**, not only material composition.

Cuspell therefore permits **relationally defined Kinds**.

A Kind predicate may include facts such as:

- structural Parts and their relations;
- geometry/Form;
- typical permitted Processes;
- intended/recognized function;
- boundary/opening relations;
- material constraints.

### Objective purpose

Purpose cannot mean "whatever someone currently wants to use it for."

A purpose-defined Kind uses an objective **design/function relation**, for example:

> the entity is constructed/organized according to a design whose normal function includes X.

An improvised rock used once as a hammer need not become Kind Hammer.

It can be:

- a rock;
- currently Used as an impact tool.

A deliberately made hammer can satisfy the artifact Kind classifier.

This distinguishes temporary use from design identity.

## 12. Semantic molecules

A **semantic molecule** is a stable reusable meaning assembled from lower-level semantics.

It may exist in three forms:

1. transparent full expression;
2. conventional compound word;
3. registered atomic lexical rune.

All three can normalize to the same semantic definition.

Mana cost follows the written registered form, not the normalized expansion.

This creates exactly the intended progression:

- beginner writes a long transparent definition;
- knowledgeable caster learns a conventional compact word;
- advanced/hidden vocabulary may compress further.

## 13. Lexicalization policy

Do not force every frequently used noun to remain decomposed.

A candidate should be lexicalized when one or more are true:

- its objective definition is long;
- the concept is frequent in ordinary speech;
- the concept is frequent in magic;
- the recognition rule depends on ontology inaccessible to ordinary composition;
- the transparent definition creates repeated ambiguity/verbosity;
- the language plausibly treats it as a conventional unit.

Conversely, keep transparent compounds when the composition is short and semantically useful.

The aim is not minimal rune count.

## 14. Initial treatment of stress-test nouns

## 14.1 Water

Recommended status:

**canonical material Kind**.

Not derived from LiquidMatter.

Recognition uses material/substance identity.

Phase is separate.

Potential root:

`Water : Kind<Material>`

## 14.2 Iron

Recommended status:

**canonical element/material Kind**.

Potential root:

`Iron : Kind<Material/Element>`

Its recognition predicate corresponds to the world's Iron element identity.

## 14.3 Stone

"Stone" is less chemically singular than Iron.

Recommended status:

either:

- a conventional geological Material Kind with a language-defined classifier; or
- a family of more specific mineral/rock Kinds.

Do not define it as SolidMatter.

For game usability, a broad registered Stone Kind is likely worthwhile.

## 14.4 Oak

Recommended status:

**canonical biological taxon Kind**.

The language ontology recognizes Oak lineage/taxon identity.

## 14.5 Tree

Recommended status:

**biological structural/life-form Kind**, possibly a conventional semantic molecule or canonical classifier.

It need not be a primitive semantic concept even if it receives one rune.

## 14.6 Wolf

Recommended status:

**canonical biological taxon Kind**.

## 14.7 Human

Recommended status:

**canonical biological/person taxon Kind**.

Its exact setting-specific classifier must accommodate the world's metaphysics and transformed forms.

## 14.8 Hand

Recommended status:

**canonical anatomical Kind** or registered semantic molecule.

Its classifier uses organism-relative structure/homology/function.

## 14.9 Fire

Recommended status:

do not equate with Heat + Light + Gas.

Fire is better treated as a **Process/phenomenon Kind** with a setting-specific classifier, likely involving a self-sustaining energetic/chemical transformation that produces thermal/light effects.

Fantasy settings may require multiple Fire Kinds:

- ordinary combustion Fire;
- magical Fire;
- other flame-like phenomena.

This remains a world-physics specification task.

## 14.10 House

Recommended status:

registered artifact semantic molecule / Kind.

Classifier includes enclosure, inhabitable structure, access, and design function.

## 14.11 Door

Recommended status:

registered artifact semantic molecule / Kind.

Classifier includes:

- boundary association;
- movable/openable barrier;
- passage-control function.

## 14.12 Sword

Recommended status:

registered artifact Kind/semantic molecule.

Classifier can include:

- elongated blade geometry;
- handle/grip structure;
- hand-held design;
- cutting/thrusting weapon function.

The exact definition should deliberately decide edge cases such as ceremonial swords, broken swords, training swords, energy blades, etc.

Those are lexicon/world-ontology choices, not casting-time interpretation.

## 15. Damaged and transformed members

Kind membership must distinguish **essential identity conditions** from temporary Properties.

Examples:

- a broken sword can remain Sword;
- ice remains Water substance;
- an injured hand remains Hand;
- a dead wolf may remain a Wolf-body/organism-derived Entity even though Life no longer applies.

Each canonical Kind therefore records:

- identity-essential constraints;
- typical/default Properties;
- disqualifying transformations if any.

This avoids defining a Kind so narrowly that damage instantly changes its noun identity.

## 16. Dead organisms and temporal identity

Biological Kind and Life state are separate.

An Entity can cease Life without immediately losing every biological Kind relation.

Therefore:

`NotLife`

does not erase biological history/classification.

A dead wolf can still be classified through a derived body/remains relation.

The exact difference between:

- Wolf organism;
- dead Wolf body;
- former Wolf transformed into another Kind

will be handled by temporal identity rules.

## 17. Reference by example

Reference-by-example is allowed only through a declared comparison classifier.

Valid future patterns may include:

- same MaterialKind as This;
- same Species as This;
- same registered DesignKind as This;
- Equal Form profile to This.

Invalid shortcut:

- "same Kind as This" with no classification dimension.

This preserves objectivity while still enabling useful advanced magic.

## 18. Names do not select Kinds automatically

A Name relation identifies a referent under a naming context.

A Sign named "water" in some human language does not itself become the Cuspell Water semantic root.

Likewise knowing an object's ordinary-language name does not grant magical Kind knowledge unless the caster knows the corresponding registered rune/semantic expression.

This creates a meaningful distinction between:

- mundane vocabulary;
- Cuspell lexical knowledge;
- magical execution vocabulary.

## 19. Dictionary as ontology interface

The Cuspell lexicon should eventually be stored as structured entries.

For Kind roots, useful fields include:

- lexical rune;
- super-Kinds;
- recognition classifier;
- identity-essential constraints;
- default/typical Properties;
- relevant Parts;
- design/function relations;
- whether magical targeting is allowed;
- whether the world supplies deterministic generation/transformation profiles for the Kind;
- known transparent definitions/semantic molecules;
- mana cost of written form.

A later parser/type-checker can use these entries directly.


## Creation and transformation closure

Kind recognition and Kind generation are different capabilities.

A Kind entry may optionally provide:

- a **canonical generation profile** sufficient to create a new member when remaining required parameters are supplied;
- one or more **source-to-target transformation mappings** that deterministically map compatible source attributes into a target member.

A bare Kind does not by itself authorize or fully specify fresh generation/transformation. If a world operation consumes a Kind as a generation/target description, it is closed only when the relevant profile/mapping supplies every otherwise-underdetermined choice.

For example:

- The Water world concept plus amount/Form/location may be generatively sufficient for a future world generation operation if its world profile is deterministic.
- Human-like or animal Kinds usually leave many identity-relevant/appearance/anatomical choices. A bare target Kind is therefore insufficient unless the setting deliberately defines a canonical generation profile.
- A referenced template can supply missing profile information.

This prevents a noun root from hiding arbitrary creation choices while still allowing registered Kinds to provide useful compression.

## 20. World Kinds have explicit classified-value types

Checkpoint 116 resolves the event-category pressure exposed by checkpoint 115 without adding a new rune or semantic root.

A registered **world concept whose semantic type is `Kind`** may optionally declare:

`classifies_types: [ ... ]`

This states which semantic value types can be members of that world category.

If the field is absent, the historical/default behavior remains:

`classifies_types: ["Entity"]`

so all existing ordinary object, organism, artifact, place, role, and institution Kinds keep their previous meaning.

World concepts may instead classify other explicit semantic domains when that is the actual ontology. Current accepted uses include:

- `["EventSpec","Event"]` for ritual, prayer, dance, performance, game/sport, festival/feast, and similar occurrence categories;
- `["Information"]` for story, music composition, song, and similar content categories;
- `["TimeInterval"]` for day, night, season, year, month, and similar calendar-period categories.

The surface predicate remains the same:

`«OldName» value.`

but the parser obtains the allowed subject type from the **registered world concept**, rather than hard-coding every Old Name Kind to Entity.

This is static typed classification, not contextual guessing.

### Why this is better than fake event Entities

A ceremony or battle can have participants, duration, ordering, causes, and consequences as an Event. It should not become a persistent Entity merely because the noun vocabulary system originally classified only Entities.

Likewise a Story or musical composition is Information; its physical book, score, painting, instrument, or performance can be separate Entities/Events.

Typed world-Kind targets preserve those distinctions.

### Built-in lexical Kinds remain frame-typed

Direct productive Kind roots such as `Thing`, `Matter`, `Sign`, and `Group` keep their ordinary registered frames. Checkpoint 116 does **not** make every Kind root polymorphic over every semantic value.

The generalization is specifically for registered world concepts whose classifier metadata says which domain they classify.

### Checkpoint 122 structural audit

The mechanism remains the minimal current solution, but the audit tightens four edges:

1. the default `["Entity"]` rule is centralized and redundant explicit Entity declarations are omitted;
2. named-Kind binders inherit the registered classifier domain when exactly one target type exists, so a Story binder is Information and a Day binder is TimeInterval rather than being hard-coded to Entity;
3. a Kind with multiple incomparable targets such as `["EventSpec","Event"]` is not silently widened to `SemanticValue`; because Cuspell has no union binder type, that named-Kind binder is rejected and the writer must bind an explicit semantic type plus the Kind predicate;
4. core and world-package concepts receive the same validation, including rejection of duplicate targets and broad/meta `Any`, `SemanticValue`, `Binder`, or `Kind` targets.

The audit also scans the full core concept registry. The sixteen explicit non-default declarations are retained. Organizational domains such as `domain: "information"` do not by themselves determine the semantic value type a Kind classifies: Record/Book-like concepts may still classify persistent Entities, and changing Law or another legacy concept to Information requires its own ontology evidence rather than a metadata-name inference.

### New Names

A particular Event, Information value, TimeInterval, or Kind may already receive a New Name through ordinary `Name` facts.

Typed world-Kind classification is separate: it states category membership, while Name states what a community calls a particular semantic value.

## 21. Result

The specific-noun problem does not require one universal trick.

Cuspell uses:

- primitive/general ontology;
- canonical objective Kind roots where appropriate;
- compositional semantic molecules;
- relationally defined artifact/anatomical Kinds;
- ad-hoc predicate restrictions;
- typed reference-by-example.

This permits a large useful vocabulary without sacrificing objective magic or enabling arbitrary alias compression.
