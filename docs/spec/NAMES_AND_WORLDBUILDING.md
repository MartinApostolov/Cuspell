# Old Names, New Names, and World Concepts

_Status: working specification v0.2_

This specification separates semantic language machinery, world concepts, and names.

The goal is to let ordinary vocabulary develop historically and socially without turning every familiar noun into a primitive semantic rune.

## 1. Three layers

Cuspell now distinguishes:

1. **semantic roots and grammar** — meanings such as Life, Move, Cause, Before, Change, Part, etc.;
2. **world concepts** — stable semantic/world identities such as a particular artifact Kind, species Kind, Skill, place, person, or frozen spell structure;
3. **names/signs** — exact socially used Signs written inside `« »`.

A name points at or historically denotes something. It is not the identity of that thing.

## 2. Exact quoted Signs

`«... »` writes an exact Sign.

Everything inside the outer quote is orthographic/sign content, not active sentence grammar.

Therefore:

`«SharpStick»`

and

`«Sharp!Stick»`

are distinct Signs.

The `!` inside the quote is not command mood.

Quoted Signs may nest:

`«Yona's«SharpStick»»`

The outer Sign remains one exact name. The inner quotation is part of its spelling/structure.

Pipe spacing, punctuation, spaces, and nested quotations inside a Sign are preserved exactly.

## 3. World concepts

A world concept has a stable ID independent of its description and independent of what anyone calls it.

Two concepts may currently have identical descriptions and still be distinct.

For example:

- concept A and concept B may both be described by the same current classifier/profile;
- `«SharpStick»` may historically name A;
- `«Sharp!Stick»` may historically name B.

Description does not create identity.

World concepts live in:

`world/core/concepts.json`

The registry is intentionally empty until worldbuilding supplies actual concepts.

## 4. New Names

A **New Name** is an ordinary Name relation/reference established after the magical historical cutoff or otherwise not privileged as frozen magical vocabulary.

Examples include:

- a person's name such as `«Yona»`;
- the proper name of one particular sword;
- a newly coined Skill name;
- a compound reference such as `«Yona's«SharpStick»»`.

New Names are reference data.

They do not substitute their referent's semantic definition into a spell.

Naming a ten-rune spell `«Bob»` does not make it a one-mana spell.

New Name world data lives in:

`world/core/new_names.json`

The parser loads this registry for later reference-resolution/world-execution work. A quoted New Name remains a `Sign` at the language layer; the world/name registry supplies the corresponding `Name(sign, referent, context?)` facts.

Checkpoint 101 removes the old one-argument `Name(Sign) -> Entity` shortcut. Reference resolution now uses the same explicit typed selection machinery as any other inverse relation lookup. For example:

`Unique Collect e:Entity Name «Yona» $e`

selects an Entity only when the active naming facts and context leave exactly one Entity named `«Yona»`. When a naming context must be stated explicitly, write it as the named-only role `:context value` inside the `Name` predicate.

Because `Collect` preserves binder type, the same mechanism also works for non-Entity New Names, for example:

`Unique Collect r:Region Name «Oakville» $r`

This is important because world New Names may refer to Entities, Regions, Kinds, and other semantic values. `Unique` does not make `Name` globally functional: zero or multiple matches remain a failed/non-unique selection until more constraints or naming context are supplied.

### 4.1 Reused spelling does not inherit Old-Name privilege

A later technical community may reuse an older ordinary word while assigning it a new specialized denotation.

That does **not** make the new denotation an Old Name.

For example, a pre-magic language may already have an ordinary concept roughly corresponding to skill, class, profession, level, or trait. A later System may then define capitalized technical categories with precise progression/unlock rules and use similar-looking Signs for them.

Those technical referents are New Names unless their exact specialized denotations were already established before the magical cutoff.

Old-Name magical compression belongs to the historical denotation, not automatically to every later homonym or semantic reuse.

### 4.2 World-specific New Name packages

New Names and world concepts may be package-specific.

Generic Cuspell can load only the core world, while a corpus/setting package can add its own current names and concepts.

The reference loader supports:

`Language.load(root, world_package="yona")`

which adds `world/yona/concepts.json` and `world/yona/new_names.json` on top of core world data.

Historical Cuspell Old Names remain language data and are shared across packages.

## 5. Old Names

An **Old Name** is a historically established Sign whose conventional meaning existed before the language became magical.

Old status is historical, not something a current speaker can create.

An Old Name has:

- an exact Sign;
- historical name units;
- evidence/metadata that it was established before magic;
- a frozen semantic meaning;
- a frozen mana cost derived from its historical name units.

Old Names live in:

`language/names/old_names.json`

## 6. Ordinary object names should begin as descriptions

For common pre-magic objects and concepts, do **not** invent a one-word primitive just because modern English has one.

Instead:

1. identify semantic roots that already existed at that historical point;
2. make a plausible short description from those roots;
3. let repeated social use fossilize that description into the conventional name;
4. register the resulting exact Sign as the Old Name of the world concept.

The description does not need to be an exhaustive definition.

Natural names may be:

- incomplete;
- based on a salient feature;
- based on use;
- historically misleading;
- shared by multiple possible literal descriptions.

Once conventionalized, the quoted Old Name points at its frozen concept rather than re-evaluating its spelling as a fresh description.

The worldbuilding question is therefore not:

> What is the perfect modern formal definition of this object?

It is:

> What short description could speakers with the roots available at that time plausibly have started calling it?

## 7. Root-derived and historical name units

Each Old Name records `name_units`.

A unit may be a semantic root:

```json
{"root": "Life"}
```

Its mana cost is the registered written cost of that root.

A culturally historical lexical/sign unit that is not a current semantic root may instead record an explicit historical sign unit:

```json
{"sign": "Bob", "mana_cost": 1}
```

This permits culturally important historical names such as a famous pre-magic spell name without pretending every proper name is a semantic primitive.

An Old Name may also use an **earlier Old Name** as one of its historical name units:

```json
{"old_name": "old.example.boat"}
```

This represents genuine vocabulary growth. Once a society already has an established Old Name for one concept, later descriptions can reuse that name rather than rebuilding the concept from first principles.

Illustratively, if:

`«MoveInLiquidThing»` = Boat

then a later society could coin something structurally like:

`«HighExtent«MoveInLiquidThing»»` = Ship

once the relevant High + Extent description is available.

The inner quoted Old Name is part of the exact outer Sign and also appears as an `old_name` dependency in the outer entry's `name_units`.

### 7.1 Recursive mana cost

A nested Old Name contributes its **full frozen Old Name cost**, not a new one-mana shortcut merely because it is nested.

If:

- `«MoveInLiquidThing»` costs 4 mana;
- `High` + `Extent` cost 2 mana;

then:

`«HighExtent«MoveInLiquidThing»»`

costs 6 mana.

Quotation punctuation itself still costs zero.

This rule prevents free recursive compression from repeatedly wrapping an existing Old Name in new quotation.

### 7.2 Historical dependency order

An Old Name may depend only on vocabulary that already existed earlier in its naming history.

The machine-readable dependency graph therefore represents an implicit historical ordering:

earlier Old Name -> later Old Name.

The graph must be acyclic.

A pair of entries where A uses B as a name unit and B uses A is invalid, because neither name could historically have been available first.

This gives Cuspell vocabulary an etymological dependency structure without requiring exact calendar dates for every word.

All entries sharing the same exact Old Name Sign must have the same written mana cost.

### 7.3 Etymology is not a live classifier

The roots and earlier Old Names recorded in `name_units` explain historical formation and mana cost. They do **not** remain a live conjunction that reclassifies the concept every time the Old Name is used.

For example, if Ship historically fossilizes from something structurally like:

`«HighExtent«MoveInLiquidThing»»`

a particular Ship does not stop being a Ship merely because it is small relative to some later comparison standard. The frozen Old Name points to the Ship world concept; the world classifier defines membership.

This is especially important for contextual descriptive constructions such as High/Low Extent, Hard, Sharp, or Sleep. Their contextuality matters when they are used compositionally as active language, but not when they merely survive inside the etymology of an already-frozen Old Name.

## 8. Frozen meanings

An Old Name may freeze either:

### 8.1 A world concept

Example abstract structure:

```json
{
  "meaning": {
    "kind": "concept",
    "concept_id": "world.kind.example",
    "type": "Kind"
  }
}
```

When a Kind-valued Old Name is used as a predicate:

`«OldName» This.`

it normalizes to membership in that named Kind.

### 8.2 A semantic expression

A culturally important historical construction may freeze an expression:

```json
{
  "meaning": {
    "kind": "expression",
    "type": "EventSpec",
    "source": "..."
  }
}
```

Using the Old Name in a compatible semantic slot expands to that frozen meaning.

The semantic expansion is validated normally.

Recursive Old Name expansion is invalid.

## 9. Magical compression

Old Names are genuine historical lexical compression.

Their mana cost is the cost of the historically written name units, not the cost of the frozen semantic expansion.

Therefore a three-unit ancient name may legitimately cost 3 mana even if its frozen spell meaning would require 10 mana when written compositionally.

This is not available to New Names.

The cutoff prevents a modern caster from inventing arbitrarily cheap aliases.

## 10. Semantic drift

An Old Name's magical denotation is frozen at the magical historical cutoff.

Later society may:

- broaden the everyday use of the word;
- narrow it;
- turn it into slang;
- forget its original reason;
- use a newer synonym.

Those changes do not silently rewrite the magical meaning of the Old Name.

Current Name relations and historical Old Name semantics may therefore diverge.

## 11. Foreign names

A New Name from another language need not be reconstructed from Cuspell roots.

For example:

`«Yona»`

may remain exactly the foreign Sign used for that person.

This is ordinary reference, not Old Name magical compression.

## 12. Ambiguity

The same exact Sign may name multiple things in ordinary language.

Ordinary discourse may resolve a New Name through context.

Magic may not guess.

Old Name semantic use must have a unique type-compatible frozen meaning at the use site or the expression is ambiguous.

## 13. Mana inside quoted Signs

Quotation punctuation costs zero mana.

For a registered Old Name, the frozen historical `name_units` determine the name's cost.

A `root` name unit contributes that root's written cost. A historical `sign` unit contributes its recorded historical cost. An `old_name` unit contributes the referenced earlier Old Name's complete frozen cost recursively.

For an unregistered/New quoted Sign, semantic roots physically written inside the Sign retain their normal written cost, but the Sign gains no semantic macro expansion.

Nested quoted material is handled recursively for written-cost accounting, and Old Name dependency cycles are invalid.

## 14. Current machine-readable files

- `language/names/old_names.json` — frozen Old Name vocabulary;
- `world/core/concepts.json` — stable world concept identities/descriptions;
- `world/core/new_names.json` — current New Name/reference relations.

These files are intentionally empty at this checkpoint.

The next corpus/worldbuilding pass should populate them from actual needs rather than inventing a speculative dictionary in advance.

## 15. Migration rule for existing noun roots

Earlier Cuspell work allowed common nouns such as Water, Human, Hand, Wolf, Sword, etc. to become registered Kind roots.

That policy is superseded as the default for culturally ordinary vocabulary.

Do not delete/migrate existing executable roots piecemeal before their replacements exist.

During the next corpus pass:

1. identify each ordinary/world noun currently used or missing;
2. decide whether it is a true semantic root or a world concept with an Old/New Name;
3. for ordinary pre-magic concepts, construct a plausible historical descriptive Old Name from roots already available at that historical stage;
4. create the world concept;
5. register the Old Name;
6. add regression tests;
7. only then retire a redundant noun root if safe.

## 16. Design boundary

Old Names solve vocabulary and historical lexical compression.

They do not replace:

- semantic roots;
- world classifiers;
- concept identity;
- New Name relations;
- ordinary reference resolution;
- spell validation.

A name can tell the language **which concept** is meant. The world package still determines what that concept objectively is.
