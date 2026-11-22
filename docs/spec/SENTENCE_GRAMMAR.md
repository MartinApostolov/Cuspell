# Sentence Grammar and Semantic Roles

_Status: current working specification aligned with surface syntax v0.10_

This file defines sentence-level semantic grammar. Player-facing spelling rules are summarized in `player/RULES.md`; the detailed surface parser is specified in `SURFACE_SYNTAX.md` and `LINEAR_PARSING.md`.

## 1. Structural layers

### Root

A single meaning-bearing sign such as `Move`, `Life`, `Not`, or `@`.

### Word / tight local unit

One or more adjacent signs composed under the lexical/type system.

Examples:

`SolidMatter`

`EndLife`

`LifeThis`

### Expression

A head applied to typed arguments, or an Operator combining expressions.

Expressions may evaluate to Terms/values, Propositions, EventSpecs, Collections, Information, and other typed semantic values.

### Sentence

A top-level expression plus final sentence mood.

- Proposition + `.` -> Assertion
- Proposition/open query + `?` -> Question
- EventSpec + `!` -> Command

## 2. Canonical surface summary

Current surface syntax is v0.10.

- normal prose is flat;
- heads normally precede arguments;
- typed frames determine attachment;
- adjacency may form a registered lexical compound or uniquely typed local application;
- final punctuation supplies sentence mood;
- `And` / `Or` use canonical infix spoken order;
- `Sequence` / `Concurrent` use flat event lists;
- a standalone `:` closes either flat event list before later sentence material;
- binders use rune-native declarations like `:«This»:This` (Cuspell type witness), or `:«This»` when the frame supplies a type; references use `$«This»`;
- optional positions are skipped with the meaning-free `_` omission marker;
- explicit grouping is fallback/debug syntax.

Legacy leading mood and bracketed binders may remain parser-compatible but are not canonical.

## 3. Terms and Kinds

A **Term** denotes or resolves to an argument value.

Terms include:

- Entity references;
- Locations, Regions, Paths, and Times;
- Quantities;
- Information and Sign values;
- Geometry/profile values;
- Collections;
- outputs of functional relations.

A Kind denotes a class, not one arbitrary member.

A Process requiring an Entity therefore cannot accept a Kind and silently choose a member. Selection, binding, or reference must be explicit.

## 4. Property application

A Property applied to an appropriate subject yields a Proposition.

Conceptual signature:

`Property(subject) -> Proposition`

Canonical surface examples:

`LifeThis.`

`WholeThis.`

Type/domain constraints determine whether the application is legal.

## 5. Relation application

A non-functional Relation applied to its required participants yields a Proposition.

Conceptual signatures:

`In(item, region) -> Proposition`

`ParentOf(parent, child) -> Proposition`

Canonical linear order places the Relation first, then arguments in declared frame order:

`In This ThisRegion.`

## 6. Functional relations / Attributes

A functional Relation or Attribute can return a typed value.

Examples:

`Center ThisRegion` -> Location

`Surface This` -> Region

`Form This` -> GeometryProfile

`Extent ThisEvent` -> Quantity:Time

To compare the returned value, use the general comparison/equality machinery rather than a hidden output slot.

## 7. Process application

A Process applied to its required roles yields an **EventSpec**.

An EventSpec is a description/template of an event, not a claim that the event occurred.

Example:

`Move This Here` -> EventSpec

A Command asks magic to realize an EventSpec:

`Move This Here!`

The caster is the issuer of the Command, not automatically an Agent participant.

## 8. EventSpec versus Event

### EventSpec

A typed description of a possible event.

Examples:

- Move(This, Here)
- End(Life(This))
- Attempt(Self, Move(Self, Here))

### Event

A concrete occurrence with actual participants, timing, location, causes, and results.

`Happen` connects an EventSpec to occurrence:

`Happen EventSpec interval?` -> Proposition

This prevents a verb phrase from simultaneously meaning an action description, an occurrence claim, and a command.

## 9. Frames and argument order

Each Relation/Process declares one or more typed frames.

Default surface order is the declared slot order.

Required roles must be supplied.

Optional roles may be omitted. Omission means **unspecified/unconstrained**, not “infer what the writer wanted.”

Example working Move family:

`Move(theme, goal?, source?, path?)`

Common form:

`Move This Here!`

Skipping goal while giving a path:

`Move This _ _ ThisPath!`

## 10. Optional arguments and explicit omission

Frame slots remain ordered and positional.

A trailing optional slot may simply be absent. If a writer must skip an optional slot to reach a later one, `_` advances over exactly one optional position without binding a value.

Examples:

`Move This Here There!`

supplies goal `Here` and source `There`.

`Move This _ _ ThisPath!`

omits goal and source, then supplies path.

`Transfer DistributionOf This Self ThisRegion ThisRegion _ DistributionOf You Self!`

omits the optional amount before supplying the optional destination-distribution profile.

An omitted broad tail can also be closed explicitly before an outer argument:

`Say Self Obligated Self MoveSelfHere _ You!`

The omission marker is legal only at an optional current slot. It carries no semantic role identity and costs no mana. Internal slot names such as `source`, `authority`, or `context` are specification metadata, not Cuspell words.

## 11. Core semantic roles

Common grammatical roles include:

- **theme** — centrally affected/moved/changed value;
- **agent** — intentional performer where semantically required;
- **experiencer** — mind/living experiencer;
- **stimulus** — sensed input;
- **content** — proposition/information/sign content;
- **source** — origin/initial participant;
- **goal** — destination/target state;
- **recipient** — receiver;
- **instrument** — means/tool;
- **beneficiary** — entity benefiting from an event;
- **result** — explicit result value/entity;
- **location** — spatial setting;
- **time** — temporal reference;
- **cause** — causal source/context.

Not every frame supports every role.

## 12. State boundaries and Change

Persistent state predicates use `Begin` / `End`.

Examples:

`EndLifeThis!`

`Begin Open This!`

`Concurrent EndHave Self This BeginHave You This!`

Value-bearing Attributes use `Change`:

`Change This Mass «MassUnit» @@!`

This keeps state truth transitions separate from value-setting transitions.

## 13. Causation and Attempt

`Cause` is not a generic synonym for performing an action.

It represents actual causal dependence or an agentive causative EventSpec.

`Attempt(agent, goal)` represents a real effort episode aimed at a goal EventSpec and **does not entail success**.

Therefore:

- Intend != Attempt;
- Attempt != goal occurrence;
- Cause is stronger than mere Attempt when causation succeeds.

## 14. Logical operators

### Not

`Not Proposition` -> Proposition

### And

Canonical surface:

`LifeThis And MagicThis.`

For EventSpecs, And requires joint realization but imposes no order.

### Or

Canonical proposition surface:

`LifeThis Or MagicThis.`

Repeated same-operator chains remain flat.

Mixed bare And/Or has no hidden precedence; grouping must state scope.

### If

`If condition consequent alternative?`

The output type follows the consequent/alternative family.

Example:

`If LifeThis EndLifeThis!`

### Counterfactual

`Counterfactual antecedent consequent` is a discourse-level contrary-to-actual relation, not ordinary actual-world `If`.

It remains contextual and is not magically executable until the relevant hypothetical-world assumptions are objectively supplied.

## 15. Multi-action commands

### Unordered conjunction

`E1 And E2!`

requires both EventSpecs without imposing order.

### Ordered sequence

`Sequence E1 E2 E3!`

requires listed order.

Sentence end closes the Sequence. If later sentence material follows:

`Sequence E1 E2 : ...`

### Concurrent group

`Concurrent E1 E2!`

requires the registered concurrency/overlap relation.

If later material follows:

`Concurrent E1 E2 : ...`

Sequence/Concurrent are deliberately flat language constructions rather than visible AST containers.

## 16. Time and occurrence

Cuspell avoids hidden grammatical tense when explicit temporal relations can state the meaning.

Core tools include:

- `Now`;
- `Before`;
- `During`;
- `Simultaneous`;
- typed `Overlap`;
- `Happen`;
- temporal `Extent(Event)`.

Past/future meanings are expressed compositionally through `Before` and the relevant reference time.

## 17. Quantification and binding

Quantification requires an explicit binder.

Canonical binder declaration:

`:«This»:This` (type witness `This`), or `:«This»` when the operator supplies the bound type

Reference:

`$«This»`

Examples:

`All :«This»:This Exist $«This».`

`Some :«This»:«LowExtent«MoveLifeThing»» At $«This» Here.`

A binder may use an existing Cuspell type witness or a named Kind domain; English type labels are no longer canonical written syntax.

Magically executable selection must still satisfy scope/reference/execution rules; quantification does not provide free universal targeting.

## 18. Open questions

A yes/no question asks whether a Proposition holds:

`LifeThis?`

An open question introduces an unknown value before the query:

`:«This»:This ParentOf $«This» Self?`

Meaning: which Entity labeled by `«This»` is a parent of Self?

`:«Here»:Here At This $«Here»?`

Meaning: at which Location labeled by `«Here»` is This?

The binder appears first so the variable's domain is known before `$«This»` / `$«Here»` is used.

## 19. References

References are typed and must resolve under formal rules.

Examples:

- `Self` — speaker/caster Entity;
- `You` — addressee Entity;
- `Here` — contextual Location;
- `Now` — contextual TimePoint;
- `This`, `That`, `They` — discourse/deictic references;
- `ThisEvent`, `ThisRegion`, etc. — typed contextual references.

A magical Reference that does not resolve uniquely enough for execution remains incomplete rather than inviting a plausibility guess.

## 20. Contextual expressions

Some ordinary-language expressions depend on discourse standards or context.

Examples include contextual evaluation thresholds, deictics, and some social/discourse relations.

Ordinary language may use such context.

Magical execution requires the relevant contextual value to resolve objectively through an explicit argument, fixed language/world default, or defined command environment.

## 21. Equality and identity

`Equal` is typed equality.

For Entity inputs, the current Entity frame of `Equal` means identity equality.

For quantities/profiles/other compatible values, it means equality under the registered typed comparison.

Do not reintroduce the removed `Same` root merely to express Entity identity.

## 22. Sentence validation stages

Current checking separates:

1. lexical recognition/compound parsing;
2. expression typing;
3. frame completion;
4. semantic closure;
5. reference/context resolution;
6. consistency/constraint validation;
7. magical executability;
8. world/Power/resource resolution.

A sentence may be valid Cuspell without being executable magic.

## 23. Grammar status and future scope

The current canonical transliteration is **surface v0.10** and the ordinary grammar has been reconciled with the maintained parser, player guide, and current surface snapshot. The pipe is **debug/legacy compatibility only**, not player-facing Cuspell. The completed multi-frame audit found **zero genuine lexical irregularities** in the live 53 multi-frame entries (276 total semantic frames); the historical 51-entry checkpoint-99 audit is not an open release task.

Discourse/anaphora refinements and the exact execution policy for EventSpec-Or can still be extended when future language/world evidence requires it. Those are not permission to infer missing arguments or silently change the canonical parser. Keep grammar and frame rules data-driven rather than adding root-specific exceptions.

Historical surface forms and superseded grammar experiments remain under `archive/`, not in this specification.
