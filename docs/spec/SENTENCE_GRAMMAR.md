# Sentence Grammar and Semantic Roles

_Status: working specification v0.4_

This file defines the first sentence-level grammar for Cuspell. It sits above compound-word semantics.

The goals are:

- every well-formed clause has a unique typed semantic structure;
- complex and multi-action commands remain possible;
- common expressions can be compact;
- omitted information is never silently guessed for magical execution;
- grammatical structure can be represented without adding mana-bearing semantic roots merely to mark syntax.

## 1. Layers

Cuspell now distinguishes four structural layers.

### 1.1 Root

A single meaning-bearing rune such as:

`Red`, `Move`, `Life`, `@`

### 1.2 Word

One or more adjacent roots composed under the lexical type system.

Examples:

`RedMatter`

`OppositeBefore`

`EndLife`

### 1.3 Expression

A Word applied to typed arguments, or an Operator combining expressions.

Expressions may evaluate to:

- Term/value/reference;
- Proposition;
- EventSpec;
- higher structures such as collections or informational values.

### 1.4 Sentence

A top-level expression with sentence mood and final terminator.

Sentence-level products include:

- Assertion;
- Question;
- Command.

## 2. Temporary surface notation

Surface syntax v0.3 uses ordinary spaces as the normal token separator.

- adjacency: lexical compound (`SolidWater`);
- whitespace: ordinary token sequence whose structure is inferred from typed frames;
- `|`: explicit hard application/grouping boundary;
- `(...)`: strongest explicit grouping fallback;
- `.`, `!`, `?`, roles, binders, collections, and quotation retain their existing functions.

Examples:

`Cat Self.`

`!Move This Here.`

`!If Life This EndLife This.`

`All [a:Human] Life $a.`

The detailed algorithm is normative in `SURFACE_SYNTAX.md` and `LINEAR_PARSING.md`.

## 3. Default sentence moods

### 3.1 Assertion

A top-level Proposition followed by `.` is an assertion.

Conceptual example:

`Life|This.`

= assert Life(This).

### 3.2 Question

`?` applied to a Proposition creates a Question speech act.

Conceptual example:

`?Life|This.`

= is Life(This) true?

The detailed Information structure of Question/Answer remains to be expanded later.

### 3.3 Command

`!` applied to an EventSpec creates a Command.

Conceptual example:

`!EndLife|This.`

= execute an event matching EndLife(This).

A magical casting is a Command.

The command marker itself costs 0 mana because imperative mood is grammar, not a meaning-bearing semantic root.

## 4. Terms

A **Term** denotes or resolves to an argument value.

Terms include:

- Entity references;
- Location references;
- Time references;
- Quantities;
- Information values;
- Geometry values;
- collections when explicitly constructed;
- outputs of functional relations.

A Kind by itself denotes a class, not one arbitrary member.

Therefore a Process requiring an Entity cannot silently accept `Human` and choose whichever human the caster intended.

Selection/quantification must be explicit.

## 5. Predicate application

## 5.1 Property

A Property applied to an appropriate Term yields a Proposition.

`Property(term) -> Proposition`

Temporary linear notation:

`Life|This`

`Red|This`

If the Property has incompatible domain/type constraints, the clause is ill-typed.

## 5.2 Relation

A non-functional Relation applied to all required participants yields a Proposition.

Example abstract structures:

`Same(A,B)`

`In(A,B)`

`Before(EventA,EventB)`

Temporary canonical linear form places the Relation first, followed by arguments in its declared frame order.

Example:

`In|This|That`

The exact reference root for "That" is not yet fixed; the example shows structure only.

## 5.3 Functional relation

A Relation with `functional(inputs -> output)` can be invoked with its input roles to produce a Term/value.

Examples:

`Center(X) -> Location`

`Surface(X) -> SurfaceRegion`

`Form(X) -> GeometryProfile`

`Extent(E) -> Quantity[Time]` for concrete Event E

The function-like use is the normal compact form.

To assert equality with an expected value, use the general equality relation rather than supplying a hidden extra output slot:

`Equal|Extent|E|Q`

This avoids one expression having an ambiguous choice between "return value" and "assert relation."

## 6. Process application

A Process applied to its required roles yields an **EventSpec**.

An EventSpec is a description/template for an event, not a claim that the event actually occurs.

Example conceptual frame:

`Move(theme, goal?) -> EventSpec`

A magical command can execute an EventSpec:

`!Move|This|Here.`

Ordinary discourse can refer to or assert occurrence of EventSpecs through Event semantics rather than treating every Process phrase as automatically true.

## 7. EventSpec versus Event

This distinction is fundamental.

### EventSpec

A typed description of an event that could occur.

Examples:

- Move(This, Here)
- EndLife(This)
- Begin(Joined(A,B))

### Event

A concrete occurrence satisfying an EventSpec, with facts such as:

- actual participants;
- time;
- location;
- duration;
- causes;
- results.

Magic primarily takes an EventSpec in a Command and attempts to realize it as an Event.

This prevents a verb phrase from simultaneously meaning "an action description," "an actual event," and "a command."

## 8. `Happen`

Reclassify `Happen` as an Event-realization/existence Operator.

Conceptual signature:

`Happen(EventSpec, interval/context?) -> Proposition`

Meaning:

> at least one actual Event matching the EventSpec occurs in the supplied temporal scope.

Ordinary conversation may use a discourse-default temporal scope.

Magical conditions must not rely on an unstated ambiguous time interval. A Trigger or command environment may provide an explicit evaluation interval.

This makes it possible to say that an event occurs without confusing EventSpec with Proposition.

## 9. Process participant philosophy

A Process frame contains only participants required by the event's semantic structure.

Do **not** automatically add the caster as Agent.

For magical execution:

> the caster is the issuer of the Command, not automatically a participant in the commanded Event.

Example:

`!Move|This|Here.`

commands reality to realize Move(This, Here).

It does not semantically mean:

"the caster physically moves This."

If agentive causation matters, it must be represented explicitly through causation or an agentive Process.

This avoids hidden role assumptions and makes remote magic natural.

## 10. Canonical frame order

Every Relation and Process declares an ordered frame.

Compact syntax supplies arguments in that order.

Example frame:

`Move(theme, goal?, source?, path?)`

A compact expression may use only the initial required/core positions.

Optional trailing roles may be omitted.

Omission means **unconstrained/not specified**, not "infer what the caster wants."

No required role may be omitted in a magical Command.

## 11. Explicit role marking

For noncanonical order, skipped optional slots, or clarity, a grammatical case marker may name a frame role.

Temporary notation:

`:goal Here`

`:source This`

These labels are metalanguage names for case markers; final glyphs will be language-specific.

A role marker is legal only if the head's frame contains that role and the supplied argument has the required type.

Example conceptual form:

`Move|Rock|:goal|Here|:source|There`

This is semantically equivalent to the corresponding fully positional frame.

The role markers cost 0 mana because they disambiguate grammatical attachment; they do not introduce new world concepts.

## 12. Core semantic roles

These are grammatical role types, not necessarily meaning-bearing roots.

### theme

Entity whose state/location/possession changes or which is centrally affected.

### agent

Entity intentionally performing an event, where a Process semantically requires agency.

### experiencer

Mind/Life entity experiencing perception, feeling, knowledge, etc.

### stimulus

Entity/phenomenon/input being sensed.

### content

Information/Proposition serving as mental or communicative content.

### source

Initial location, possessor, state, or origin.

### goal

Destination/final location or target state.

### recipient

Entity receiving transferred possession/information.

### instrument

Entity/process used as means.

### beneficiary

Entity for whose purpose/benefit the event is performed.

### result

Explicit resulting Entity/state/value when a Process frame exposes one.

### location

Spatial setting of Event.

### time

Temporal location/boundary.

### duration

Measured temporal extent.

### cause

Event/Entity relation specifying causal source when semantically represented.

Not every Process supports every role.

## 13. Core frame sketches

These are provisional but now constrain later lexicon work.

### Move

`Move(theme: Entity, goal?: Location, source?: Location, path?: SpatialPath) -> EventSpec`

Core meaning: spatial location of theme changes along a permitted path.

Move itself does not assert an Agent.

### Beginning a Joined state

The minimized core has no separate Join Process. Use:

`Begin(Joined(A,B)) -> EventSpec`

for the structural state transition. Any stronger fusion/composite-identity operation must state its additional semantics explicitly.

The exact physical/result identity rules belong to execution semantics.

### End

When applied as the lexical compound `EndX`, End's boundary semantics create a termination Process/EventSpec as defined in LEXICAL_RESOLUTIONS.

### Change

`Change(theme, attribute/function, target-value) -> EventSpec`

Core meaning: a selected attribute/property value of theme changes to the target value.

Do not allow bare `Change(theme)` in magic; it is underspecified about what changes.

### Giving

There is no standalone `Give` root in the minimized core.

Giving is the coordinated possession transition:

`Concurrent EndHave source theme BeginHave recipient theme`

This explicitly ends the source holder's `Have` state and begins the recipient holder's `Have` state. Generic `Transfer` remains distinct because its source/destination roles do not inherently assert possession.

### Sense

`Sense(experiencer, stimulus/channel-content) -> EventSpec`

Specialized Sense compounds constrain the channel.

### Say

`Say(speaker/agent, content, recipient?) -> EventSpec`

Output medium may be added through a Sign/channel specialization.

### Attempt

`Attempt(agent: Entity, goal: EventSpec) -> EventSpec`

Meaning: the agent undertakes a real goal-directed effort episode aimed at realizing the goal EventSpec.

Attempt is deliberately distinct from:

- `Intend(agent, goal)` — a standing intention can exist without any effort episode;
- `Plan(agent, goal)` — a plan can exist without being attempted;
- the goal EventSpec itself — attempting the goal does **not** entail that the goal occurs;
- `Cause(agent, goal)` — successful causation entails the effect rather than merely trying to produce it.

This distinction is required by ordinary prose such as "tried to grab," "tried and failed," and "tried it and it worked."

Success/failure can be represented compositionally by relating the salient Attempt Event to occurrence/non-occurrence of its embedded goal in the relevant attempt interval. Compact Succeed/Fail/Manage molecules may be added later, but are not required for the semantic core.

In magic, commanding `Attempt A Goal!` commands the attempt EventSpec only. It does not silently upgrade into a command that Goal succeed.

### Use

`Use(agent, instrument, goal/EventSpec) -> EventSpec`

This Process intrinsically contains an agentive role because "use" semantically requires an intentional user.

## 14. Causation

`Cause` is not a vague synonym for doing an action.

Working semantic relation/operator:

`Cause(cause-event-or-agent, effect: EventSpec/Event) -> causal structure`

For propositions about actual events it can yield a Proposition.

For Commands, a causative event specification can explicitly require one event/agent to cause another.

Magic does not need to wrap every commanded action in Cause; command execution already asks reality to realize the EventSpec.

## 15. Logical operators

## 15.1 Not

At sentence level:

`Not(Proposition) -> Proposition`

At lexical/property level, existing typed complement rules remain.

## 15.2 And

`And` is type-preserving conjunction when all operands share a compatible semantic level.

- Proposition + Proposition -> Proposition conjunction.
- EventSpec + EventSpec -> CompositeEventSpec requiring both component events.

For EventSpecs, And does **not** impose an order.

## 15.3 Or

- Proposition + Proposition -> Proposition disjunction.
- Canonical proposition surface syntax is infix: `A Or B`.
- Repeated Or chains are associative and remain linear.
- Mixed ungrouped And/Or is rejected; explicit grouping must state scope.
- EventSpec alternatives remain a separate unresolved execution problem: ordinary proposition disjunction does not silently choose one executable event branch.

The current executable lexicon therefore supports proposition Or directly while an executable EventSpec-Or branch policy remains deferred.

## 15.4 If

Conditional core:

`If(condition: Proposition, consequent: X, alternative?: X) -> X`

where X may be Proposition or EventSpec/Command-compatible structure.

This is one coherent conditional meaning with typed output.

Example:

`!If Life This EndLife This.`

means: if Life(This) is true when the condition is evaluated, execute EndLife(This).

The flat phrase is legal only because the typed frames produce one unique full-consumption parse. Parentheses remain available when needed.

## 15.5 Counterfactual

`Counterfactual(antecedent: Proposition, consequent: Proposition) -> Proposition`

Counterfactual is **not** another spelling of If.

Meaning:

> in the discourse-selected relevant admissible alternative history in which the contrary-to-actual antecedent holds, the consequent holds.

It does not assert either antecedent or consequent in the actual history.

Examples of meanings that require this distinction include:

- "If I had acted earlier, he would still be alive."
- "If I had chosen that evolution, I would have been able to return."
- "My earlier self would not have heard that sound."

Past/Present/Future may occur inside either clause when temporal location matters. Counterfactual itself supplies the alternate-history relation, not tense.

The current root is contextual ordinary-language semantics because selecting the relevant minimally changed alternative history depends on discourse/world assumptions. Therefore a Counterfactual nested inside a magical Command is SemanticallyIncomplete until a future explicit objective hypothetical-history/world construction is supplied.

Actual-world conditional control remains `If`; do not weaken If to absorb counterfactual reasoning.

## 16. Multi-action commands

Multiple actions are explicitly legal.

There are at least two different structures.

### 16.1 Unordered conjunction

`And(E1,E2,...)`

requires all component EventSpecs to be realized, with no semantic ordering unless their constraints imply one.

### 16.2 Ordered sequence

`Sequence(E1,E2,...)`

requires E1 before E2 before ... in listed order.

Canonical surface form is flat: `Sequence E1 E2 ...`. Sentence end closes the group unless `SequenceEnd` closes it earlier.

This resolves an important ambiguity: "do both" is not automatically the same as "do this, then that."

Sequence is therefore retained as a useful structural Operator/Kind-like construct rather than only a mathematical list.

Later execution semantics must define failure/rollback behavior for multi-step commands.

### 16.3 Concurrent group

`Concurrent(E1,E2,...)`

requires all component events to occur with the concurrency/overlap constraints defined in the discourse/time specification.

Canonical surface form is flat: `Concurrent E1 E2 ...`. Sentence end closes the group unless `ConcurrentEnd` closes it earlier.

Concurrent remains distinct from unordered And: And requires joint realization but does not itself require temporal overlap.

## 17. Begin and End in event grammar

Because Begin/End are boundary Operators, they can interact cleanly with EventSpec/Event.

- `Begin(StateProperty)` -> transition EventSpec/Process
- `End(StateProperty)` -> transition EventSpec/Process
- `Begin(EventRef)` -> TimeReference
- `End(EventRef)` -> TimeReference

The parser selects the frame from input type; no English ambiguity remains.

## 18. Tense and temporal assertion

Cuspell should avoid grammatical tense that silently depends on speaker perspective when objective time can be represented directly.

Initial approach:

- `Now` is Reference<Time>.
- `Before` and `During` relate Events/Times; after-meaning uses `Before` with reversed arguments.
- `Happen(EventSpec, interval)` asserts occurrence.
- `Former(P)` can later be defined through a past interval plus current NotP if useful.

Ordinary conversation may gain compact tense morphology later, but magical semantics should normalize it to explicit time relations.

## 19. Quantification: semantic model

Quantification requires binding, so it cannot be treated as a simple adjective.

Working semantics:

`All(domain: Kind/Collection, predicate) -> Proposition`

`Some(domain: Kind/Collection, predicate) -> Proposition`

`None(domain, predicate) -> Proposition`

A binder connects occurrences of the quantified participant inside the predicate.

For magical Commands, targeting a quantified set must be distinct from asserting a quantified Proposition.

A later `Each`/distribution construction is likely required:

`Each(collection, EventSpec-template) -> CompositeEventSpec`

This prevents `AllHuman` from silently becoming "all humans everywhere" and then being accepted as an Entity argument.

### Scope requirement

A magically executable collection selection must have a bounded selection scope unless the command environment supplies one explicitly.

Examples of scopes may include:

- In(region)
- Near(reference, distance)
- a previously bound Collection
- an explicitly named finite Kind set

This protects objectivity and prevents hidden universal targeting.

### Surface binder notation

The temporary transliteration is now fixed for testing:

- `[a:Domain]` introduces a typed binder.
- `$a` refers to that bound value.
- binder labels/references are zero-mana grammar.

The flat preferred form is:

`All [a:Human] Life $a`

when that phrase has a unique typed parse.

Detailed scoping, collection construction, and distribution rules live in `COLLECTIONS_AND_BINDING.md`, `SURFACE_SYNTAX.md`, and `LINEAR_PARSING.md`.

A magical spell may never rely on an implicit or unspecified binder interpretation.

## 20. References

References remain typed.

A reference either:

1. resolves uniquely under its formal rule;
2. resolves to an explicitly typed collection;
3. fails to resolve.

It does not pick the "most reasonable" object.

Examples:

- Self -> caster Entity
- Here -> command-origin/reference Location under a defined casting-context rule
- Now -> evaluation Time
- This -> only valid when an explicit deictic/selected referent exists and its type is known

A failed or multiply-resolving magical Reference is a resolution failure, not an invitation for GM interpretation.

## 21. Contextual expressions

Expressions with the `contextual` trait can occur in ordinary language with discourse-supplied standards.

Examples:

- Near
- Far
- Many
- Few
- Hot
- Cold
- Good
- Bad

Magical execution requires one of:

1. an explicit comparison standard/threshold;
2. a fixed magical-language default defined in the lexicon;
3. a command-environment parameter whose semantics are defined.

Otherwise the Command is semantically incomplete.

## 22. Identity versus equality

Maintain the distinction:

`Same(A,B)`

= A and B resolve to the same identity.

`Equal(valueA,valueB)`

= values are equal under a typed comparison/dimension.

Two rods can have Equal Length without being Same.

## 23. Validity stages

Sentence checking occurs in stages.

1. **Lexical parse** — roots/compounds valid?
2. **Expression typing** — heads and arguments compatible?
3. **Frame completion** — required roles bound?
4. **Reference resolution** — references unique and typed?
5. **Constraint consistency** — contradictions?
6. **Command executability** — magical layer supports the semantic structure?
7. **Resource/effect resolution** — mana/power/range/etc.

A sentence can be grammatically valid but not magically executable.

This preserves the distinction between language and magic.

## 24. Current unresolved grammar work

Before sentence grammar can be considered stable, remaining work includes:

- completing argument frames for the full Process/Relation inventory;
- stress-testing v0.2 flat pipe parsing against the whole corpus;
- resolving any phrases with multiple valid typed parses;
- deciding which role markers become case marks versus glyph placement;
- refining ordinary-language pronouns/anaphora beyond the current discourse layer;
- finalizing a small number of control/discourse constructions such as executable Or selection policy.

Collection/binder syntax, open questions, quotation, narrative tense/aspect, and cross-sentence discourse now have working specifications elsewhere in the project.
