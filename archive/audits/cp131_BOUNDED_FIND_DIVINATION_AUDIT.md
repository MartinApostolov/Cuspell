# Checkpoint 131 — Bounded Unknown-Information Acquisition / Find Audit

_Status: advanced spellcraft gap audit 2_

## Trigger

Checkpoint 128 identified controlled unknown-information acquisition as a recurring gap across low- and high-level divination pressure.

Checkpoint 129 closed fresh Entity generation with `Create`; checkpoint 130 then fed Create back through the beginner spell corpus.

The next question is whether current Cuspell can safely express:

> acquire a truthful answer that the caster/execution context did not already possess,

without turning ordinary Questions, References, Sense, Collect, If, or Trigger into omniscient world search.

## Pressure examples

The recurring family includes effects analogous to:

- Detect Magic;
- Locate Object;
- Locate Creature;
- Find Traps;
- Identify;
- Detect Thoughts;
- Legend Lore;
- Commune / Contact Other Plane;
- Scrying/Clairvoyance when an unknown location/fact must first be resolved;
- Find the Path;
- some future/predictive divinations.

Not every spell in that list should use one mechanism for every part of its effect.

Remote seeing remains Sense pressure. Asking another being remains Question/Say/AnswerFor pressure. Future knowledge depends on setting metaphysics.

The narrow missing operation is factual acquisition itself.

## Candidate A — Question

Question mood and the `Question` operator can represent:

- yes/no queries;
- open binder queries;
- addressed questions as Information.

They do not obtain an answer from reality.

If Question itself performed world lookup, ordinary language would become free divination.

**Result: Question is not acquisition.**

## Candidate B — Sense

`Sense` acquires perceptual Information through an explicit SenseChannel.

It is correct for vision, hearing, touch, etc., including magically extended sensing where world capability permits.

But many divinations request facts that are not sensory stimuli:

- whether an object is magical;
- an unknown Location;
- the satisfying members of a bounded predicate;
- what proposition a mind believes;
- historical/factual Information.

Making Sense answer those without a channel would restore the hidden interpretation/search overload removed earlier.

**Result: Sense is not general factual acquisition.**

## Candidate C — Collect / Unique

`Collect` constructs a typed collection from values whose membership/predicate evaluation is already resolvable under the current access rules.

`Unique` can select one result when exactly one exists.

Neither operation grants access to hidden facts.

Otherwise expressions such as broad Kind collections would become universal world databases.

**Result: selection is not acquisition.**

## Candidate D — Infer

`Infer mind evidence conclusion` requires supplied evidence.

Inference may be wrong; it is not automatically factive.

A divination that directly obtains a truthful fact without prior evidence therefore cannot be reduced to Infer.

**Result: inference is not acquisition.**

## Candidate E — Know / Begin Know

`Know mind P` describes a factive epistemic state.

`Begin Know mind P!` can request acquisition of the already-written true content P.

That does not solve unknown-answer discovery:

- it cannot bind an unknown value that was not already supplied;
- if P is false, it does not yield knowledge of Not P;
- the content to be acquired is already written into the spell.

Two worlds can agree on every written P while differing on what unknown binding satisfies a query.

**Result: Know is the result state, not the bounded search operation.**

## Candidate F — If / Trigger as hidden tests

A tempting reduction is to branch on a hidden proposition and make the branch observable.

Current execution rules already block that shortcut.

`If P E` can evaluate P only when the information needed to evaluate P is available to the execution context.

Likewise Trigger does not receive hidden universal witness/search power.

Using an unavailable hidden fact as a condition therefore presupposes the information-access capability being audited.

**Result: conditionals do not reduce acquisition.**

## Accepted result — Find

Checkpoint 131 adds:

`Find`

as a semantic primitive candidate.

Two frames:

`Find(mind:Entity, scope:SemanticValue, query:Proposition) -> EventSpec`

`Find(mind:Entity, scope:SemanticValue, answer:Binder, query:Proposition) -> EventSpec`

### Yes/no form

Example:

`Find Self This Magic This!`

Meaning:

> within the explicitly designated information-access scope This, determine the true polarity of Magic This and make Self know that truthful answer.

If Magic This is true, successful execution yields knowledge of that fact.

If it is false, successful execution yields knowledge of the negative answer.

False is not failure.

### Open form

Example:

`Find Self This l:Location At This $l!`

Meaning:

> determine the complete satisfying Location binding(s) for the designated subject under scope This and make Self know that answer.

Region example:

`Find Self ThisRegion x:Entity In $x ThisRegion And Magic $x!`

Meaning:

> acquire the complete set of magical Entities in the designated Region, subject to world access rules.

The answer binder is lexical to the query. It is not exported into later EventSpecs.

## Explicit scope rule

The Find scope is an information-access boundary.

It does not silently mean:

- In;
- About;
- At;
- Member;
- source-of;
- temporal containment;
- ownership;
- sensory visibility.

The query states the relevant relationship itself.

Static validation requires the supplied scope to occur in the query so a decorative scope cannot license an unrelated global search.

Open Find additionally requires the answer binder to occur in the query.

Runtime execution must ensure that every otherwise unavailable fact needed to answer is licensed by the scope/world capability.

## Complete-answer rule

A successful Find is factive and complete for its declared query/scope.

Therefore:

- a yes/no success returns the true polarity;
- an open-query success returns the complete satisfying binding set;
- zero satisfying bindings is a valid answer;
- blocked/incomplete access is execution failure.

A ward must never masquerade as “no target.”

This is important for gameplay: otherwise protected targets would be indistinguishable from absent targets in an uncontrolled way.

## World/execution boundary

Well-formed Find does not guarantee executable Find.

World rules may restrict:

- maximum range;
- line/plane/reality access;
- occlusion;
- anti-divination wards;
- mind/privacy protection;
- temporal reach;
- accessible information domains;
- information volume;
- RequiredPower;
- source reliability/capability where applicable.

The language states the exact bounded information request.

The world decides whether magic can satisfy it.

## Spell-family consequences

### Detect Magic

Selected subject:

`Find Self This Magic This!`

Bounded area search:

`Find Self ThisRegion x:Entity In $x ThisRegion And Magic $x!`

### Locate Object / Locate Creature

For an already designated target:

`Find Self This l:Location At This $l!`

Searching by Kind/description still requires an explicit bounded scope and objective predicate.

### Identify

Find can acquire explicitly queried facts about an item.

A request equivalent to “tell me everything about this” can still fail because the answer domain/information volume is not sufficiently bounded.

### Detect Thoughts

Find may query objective epistemic states where the mind model exposes them, for example beliefs/knowledge/wants.

That does not automatically grant access through mind protection; such access is world capability.

### Commune / Contact Other Plane

If the fiction is literally asking another information-bearing entity, ordinary communication remains relevant.

Find can query what that source knows only when the query explicitly relates to that source and access is permitted.

### Clairvoyance / Scrying

Remote sensory observation remains Sense.

Find may be needed only to resolve an otherwise unknown target/location before sensing.

### True Seeing

Primarily a Sense/capability issue, not general Find.

### Foresight / Augury

Find can acquire future-oriented Information only when the world model exposes an objective future/predictive source.

Find does not make an undetermined future determinate.

## Beginner-design consequence

This audit supports the user's plan to separate:

1. a **small actual starting vocabulary**, and
2. a broader spellcraft coverage set.

Find is a good candidate for an early optional module because simple useful spells can be written without collections, triggers, or advanced transformation.

For example:

`Find Self This Magic This!`

is structurally simpler than many current 50-sign coverage examples.

Checkpoint 131 does **not** yet rewrite the beginner subset. That redesign should compare Create-, Find-, movement-, state-change-, and simple sensing spells together rather than incrementally bloating the existing starter.

## Drift repair

The lexicon's Sense note still mentioned a separate Interpret process even though checkpoint 101 removed that temporary root.

Checkpoint 131 corrects the note: semantic decoding uses Meaning + Understand; Sense remains strictly sensory.

## Regression additions

Eight tests cover:

1. yes/no Find;
2. open Location Find;
3. bounded Region search;
4. scope must occur in the query;
5. open answer binder must occur in the query;
6. a decorative Region scope cannot license a global search;
7. Begin Know remains structurally distinct;
8. ordinary Question mood remains non-command query.

Suite total:

- **700 -> 708 tests**.

## Inventory effect

Checkpoint 131 adds:

- 1 registered base entry: `Find`;
- 1 semantic primitive candidate;
- 2 semantic frames.

New totals:

- **215 registered base entries**;
- **134 semantic primitive candidates**;
- **55 formal constructors**;
- **270 semantic frames**;
- **50 multi-frame entries**;
- **204 Old Names**;
- **197 core world concepts**.

## Decision

**ADD Find as explicit bounded factive unknown-information acquisition.**

Do not reduce it to:

- Question;
- Sense;
- Collect/Unique;
- Infer;
- Know/Begin Know;
- AnswerFor;
- If/Trigger;
- ordinary Reference resolution.

The canonical semantic shapes are:

`Find mind scope proposition`

`Find mind scope binder proposition`

The scope must participate in the query. Hidden facts outside the permitted access domain remain unavailable.

## Next work

Before finalizing the beginner teaching set, compare the newly stabilized `Create` and `Find` families with the existing simple movement/state/sensing spells and design a genuinely small first lesson.

The remaining advanced spellcraft pressure families are:

1. persistent shared illusion/representation;
2. generic magical-execution interception/suppression;
3. time-flow manipulation.
