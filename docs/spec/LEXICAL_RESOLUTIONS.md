# Lexical Semantic Resolutions

_Status: working specification_

This file resolves the highest-risk roots identified by the first full inventory audit. Its purpose is to remove accidental English polysemy before sentence grammar is built on top of it.

The governing rule is:

> One rune may support multiple typed frames only when those frames instantiate one coherent semantic core. If two meanings merely share an English translation, they are separate concepts and should not share a rune.

## 1. `Part`

### Decision

Reserve `Part` for **mereological/structural part-whole semantics**.

Core relation:

`Part(part, whole)`

Meaning:

> the first participant is a constituent portion/component of the second participant under the relevant structural decomposition.

This can apply to physical structure, collections, or other explicitly decomposable objects.

Examples:

- a hand can be Part of a body;
- a room can be Part of a house;
- an element can be Part of a collection.

### Rejected overload

Do not also use `Part` as the numerical ratio operator for color weighting.

The earlier provisional syntax such as:

`RedPart@@@GreenPart@@@@@`

is superseded.

Ratios/weights belong to a dedicated quantity mechanism such as `Ratio`, `Share`, or a later finalized operator.

Reason: structural part-of and numerical weighting can be related philosophically, but they require different argument structures and would create hidden ambiguity in magical expressions.

## 2. `Whole`

### Decision

Reserve `Whole` as an **integrity/completeness Property**, not as the converse noun of `Part`.

Semantic core:

`Whole(x)`

means:

> x satisfies the completeness requirements of its current recognized structure/Kind: required constituent parts are present and related in the required way.

Traits:

- Property
- state-like
- integrity domain

The converse of `Part(part, whole)` is obtained through relation converse or a specifically defined containment relation, not by overloading `Whole`.

This lets:

- `NotWhole` describe incompleteness;
- Damage reduce Whole/completeness;
- Repair restore Whole.

The exact completeness requirements come from the target's structural Kind/profile, not from caster intuition.

## 3. `Kind`

### Decision

Do **not** currently define a general meaning-bearing `Kind` rune that maps an Entity to "its kind."

Reason:

An Entity normally belongs to many Kinds simultaneously:

- Thing
- Matter
- Animal
- Human
- Adult
- local social categories
- function-based categories
- arbitrary restricted Kinds

Therefore `Kind(This)` would not have a unique objective answer.

### Current status

`Kind` remains a semantic Category in the metalanguage/specification.

A lexical rune for "kind/category" may later be introduced only with an explicit taxonomy or classification frame.

Likewise, "same kind as This" is not valid magical shorthand until the language specifies **which classification relation or level** is being compared.

This directly prevents a dangerous hidden-context shortcut in the future specific-noun system.

## 4. `Of`

### Decision

Reject a generic magical `Of` relation.

English "of" collapses many unrelated relations, including:

- Part
- ownership/Have
- material composition
- membership
- location
- origin
- Name
- amount
- topic
- cause

A generic `Of` would reintroduce interpretation by context.

### Full-language status

An ordinary conversational register may eventually have an underspecified linker translated as "of," but such a linker is **not magically executable** and does not substitute for typed relations.

Formal/magical expressions use the actual relation intended.

## 5. `By`

### Decision

Reject a single generic `By` rune.

English "by" conflates:

- agent
- instrument
- means
- cause
- spatial adjacency
- authorship
- measurement difference

Use explicit semantic roles/relations instead.

Sentence grammar may provide dedicated role syntax for agent/instrument/etc. That syntax must not inherit English "by" ambiguity.

## 6. `Begin`, `Start`, and `End`

### Decision

Use **`Begin`** and **`End`** as polymorphic boundary Operators with one coherent semantic core.

Remove `Start` as a separate primitive candidate unless future testing finds a meaning not covered by `Begin`.

### Semantic core

`Begin(X)` refers to the initial boundary/transition of X.

`End(X)` refers to the final boundary/transition of X.

Typed frames determine the output.

#### State/Property frame

For a state-like Property P:

`Begin(P) -> Process`

means transition from NotP to P.

`End(P) -> Process`

means transition from P to NotP.

Example:

`EndLife` = Process that terminates the Life state.

#### Process/Event-description frame

For an Event/Process description E:

`Begin(E)` can denote its onset transition.

`End(E)` can denote its termination transition.

#### Event-reference frame

For a concrete Event reference E:

`Begin(E) -> TimeReference`

`End(E) -> TimeReference`

return its first/final temporal boundary.

These are not unrelated homonyms: all instantiate initial/final boundary semantics.

The parser determines the frame from the input type.

## 7. `Form`

### Decision

Define `Form` as a **functional structural Relation**, not a vague geometric Property.

Conceptual signature:

`Form(Entity) -> GeometryProfile`

A GeometryProfile is a structured semantic value containing geometric facts relevant to the entity, such as topology, dimensions, curvature, boundaries, orientation-relative measures, etc.

It is not a new top-level lexical Category; it is a structured value in the geometry domain.

This permits future constructions such as:

- compare Form values;
- preserve Form during another Change;
- change selected parts of Form;
- Copy an informational representation of Form.

Properties such as Round, Flat, Straight, and dimensions such as Length remain independently usable; `Form` does not replace them.

## 8. `Surface`

### Decision

Use `Surface` as a **functional geometry relation**.

Conceptual signature:

`Surface(Entity/Region) -> SurfaceRegion`

The output is a spatial/geometric Entity/Region corresponding to the boundary surface of the input under the selected geometric model.

A generic "surface" can therefore be represented as a SurfaceRegion Kind if needed, but the rune itself is not overloaded between noun and relation.

This aligns Surface with Center and Edge:

- `Center(X) -> Location/Region`
- `Edge(X) -> BoundaryRegion`
- `Surface(X) -> SurfaceRegion`

## 9. `Volume`

### Decision

Reserve `Volume` for **measured three-dimensional spatial extent**.

Traits:

- scalar
- dimension(Volume)
- geometry/spatial domain

A three-dimensional region is represented by a Region/Space Kind, not by the same rune.

This avoids the English ambiguity between:

- "the volume is 3 cubic units";
- "a volume of space."

## 10. `Magic`

### Decision

Define `Magic` as a **state Property marking an actively magical condition/effect**, not as a catch-all noun for every magical concept.

Semantic core:

`Magic(x)`

means:

> x currently depends on, carries, or instantiates an active magical alteration/effect recognized by the magical execution layer.

Traits:

- Property
- state
- magical domain

This supports:

`EndMagic`

as the semantic core of dispelling: terminate the active Magic state on a target/effect, subject to later execution/resistance rules.

Important distinction:

A historical event caused by magic need not continue satisfying Magic after the active magical state has ended.

`Mana` remains a distinct scalar resource/measurement concept.

## 11. `Copy`

### Decision

Do not define a universal physical `Copy` Process.

A universal "copy this thing" hides the crucial question: copy which properties, relations, history, identity, contents, magic, memories, etc.?

### Current primitive scope

`Copy` is provisionally restricted to **Information/Sign structures** whose identity-independent content has a defined exact representation.

Conceptual signature:

`Copy(Information source) -> Process producing Information with equivalent content`

The output is a distinct token/record but the copied content normalizes to the same informational value.

Copying a physical Entity requires explicit creation plus a specified profile of properties/structure and is not granted by the Information Copy rune.

Repeating a Command or magical effect uses `Repeat`/Command semantics, not physical Copy.

## 12. `Disease`

### Decision

Reserve `Disease` as a **biological pathological state Property** for the initial magical language.

`Disease(x)`

means:

> x is in a biologically pathological state according to the language's objective biological model.

Traits:

- Property
- state
- biological
- potentially structured/severity-bearing

This supports:

- `BeginDisease`
- `EndDisease`
- Disease-specialized Damage/Repair interactions

Specific diseases can later be represented as Kinds of pathological process/condition, infectious agents, or semantic molecules as appropriate.

If ordinary language needs the noun "a disease" as distinct from the state "diseased," it receives a distinct lexical construction rather than overloading this rune.

## 13. `Memory`

### Decision

Define `Memory` as a **Kind of Information**, not the mental state of remembering.

A Memory is an Information structure encoded/retained by a Mind and associated with source/experience/time metadata when known.

`Remember` is the Mind-to-Information/Memory relation or state.

This separates:

- the stored/retrievable informational content;
- the mental condition of currently retaining/accessing it.

It also makes future memory manipulation typeable as Information manipulation while allowing `Remember` and `Forget` to describe changes in the Mind's relation to that information.

## 14. `Name`

### Decision

Define `Name` as a **Relation**, not a functional Entity-to-Sign mapping.

Core relation:

`Name(sign, referent, :context naming-context?)`

means:

> the Sign is recognized as a name for the referent in the applicable naming system/context.

This is intentionally not globally functional:

- one entity can have multiple names;
- multiple entities can share a name;
- names depend on language/community/context.

When the naming context is omitted in ordinary language it may come from discourse context. When written explicitly, it uses the named-only `:context` role so it cannot greedily consume an outer expression's next argument.

For magical execution, the context must be explicit or uniquely fixed by the command environment.

Checkpoint 101 removes the former contextual one-argument `Name(Sign) -> Entity` frame. It was inverse selection over a relation that is intentionally not globally functional and was also too narrow for New Names whose referents are Regions, Kinds, or other semantic types.

Inverse lookup is now explicit and general:

`Unique Collect x:Type Name sign $x`

`Collect` preserves the binder's declared type; `Unique` extracts a value only when exactly one candidate satisfies the relation under the active constraints/context. Supplying a naming context or other predicates narrows the candidate set rather than changing `Name` into a function.

A "name" as an object is simply a Sign participating in the Name relation.

## 15. Consequences for the inventory

The following provisional candidates are changed:

- `Part` -> structural mereology only.
- ratio use of `Part` -> removed; use dedicated ratio/weight machinery.
- `Whole` -> completeness/integrity Property.
- lexical generic `Kind` -> deferred/rejected until classification is explicit.
- generic magical `Of` -> rejected.
- generic `By` -> rejected.
- `Start` -> folded into `Begin`.
- `Begin`/`End` -> typed boundary Operators.
- `Form` -> functional Entity -> GeometryProfile relation.
- `Surface` -> functional boundary-surface relation.
- `Volume` -> scalar measured spatial extent only.
- `Magic` -> active magical-state Property.
- `Copy` -> Information-only primitive for now.
- `Disease` -> pathological biological state Property.
- `Memory` -> Information Kind.
- `Name` -> naming Relation.

These choices reduce polysemy before sentence grammar is introduced.

## 16. Residual role/action distinctions retained by exact-reduction audit

Four previously unresolved entries survive the current reduction pass because nearby roots describe consequences, participants, or components rather than the same truth conditions.

### `Beneficiary`

`Beneficiary(event, entity)` is the role of an entity that benefits from an Event/EventSpec. It is distinct from recipient, possession, transfer, and intended `Purpose`; benefit may be indirect or unintended.

### `Bite`

`Bite(agent, target)` denotes an oral biting action. `Attack`, `Eat`, `Touch`, and `Damage` can overlap with individual bites but do not encode the action manner itself. A later general manner/body-part system could justify revisiting this root.

### `CamouflagedAgainst`

`CamouflagedAgainst(subject, background, observer?)` is a contextual perceptual relation. `ColorOf` and `TextureOf` expose components that may contribute to camouflage, but there is no current general observer-relative similarity/visibility metric that makes those components an exact replacement. The registered `Contrast` relation is discourse contrast, not visual contrast.

### `Climb`

`Climb(agent, target)` denotes a supported/contact locomotion manner relative to a target. It is not equivalent to upward `Move`: climbing can proceed up, down, across, or over, and generic `Move` does not encode the characteristic manner.

## 17. Additional unresolved distinctions retained by exact-reduction audit

The next four unresolved entries likewise survive because their nearest compositions lose part of the represented meaning.

### `Contrast`

`Contrast(a, b)` is a contextual discourse concession/contrast relation. `And` states both represented sides, but does not state that they stand in a noteworthy tension, violated expectation, or concession relation. Until Cuspell has a general discourse-coherence relation family, Contrast remains distinct.

### `Dodge`

`Dodge(agent, threat?)` is evasive action intended to avoid a threat. It is not equivalent to `Move`: the path can vary and avoidance is central. It is not equivalent to `Prevent threat`, because a dodge can let the threatening event occur while avoiding its contact/effect on the agent. `Attempt` can represent effort toward a goal but does not itself encode evasive action.

### `Fall`

`Fall(theme)` is a non-agentive/context-governed motion manner. The relevant downward/gravity direction is determined by the physical/world frame; generic `Move` neither carries that manner nor provides a direction-only frame, and objective Move execution requires a goal or Path.

### `Forgive`

`Forgive(forgiver, offender, :offense?)` is a social/affective transition that relinquishes blame or resentment toward an offender. It does not entail forgetting the offense, denying the offender's responsibility, ending every anger state, beginning Love/Like, or granting legal pardon.

## 18. Final unresolved distinctions retained by exact-reduction audit

The remaining four unresolved entries also survive. This empties the explicit unresolved-candidate bucket without freezing any retained primitive permanently.

### `Reflexive`

`Reflexive(event)` marks involuntary/reflex execution. It is not equivalent to `Not Intend`: many accidental, coerced, habitual, or intention-unknown events are non-intentional without being reflexes. `Cause` addresses causal dependence rather than agency/control mode.

### `Jump`

`Jump(agent, goal?)` denotes launch/airborne locomotion manner. `Move` can express displacement and destination but not the jumping manner itself, and the current core has no general motion-manner constructor that would make the replacement exact.

### `Limp`

`Limp(agent)` denotes asymmetric/impaired gait. `Damage` is a graded condition rather than a gait description: damaged entities need not limp, and limping can arise from multiple causes. Generic `Move` likewise lacks gait manner.

### `Stab`

`Stab(agent, target, instrument?)` denotes a directed puncturing/thrust action. `Attack`, `Damage`, `Touch`, and `Use` may all describe aspects of a particular stabbing but do not encode the same event type.

The unresolved-candidate inventory is now empty. Further reduction should audit the retained semantic primitive candidates by reusable families as stronger abstractions become available.

