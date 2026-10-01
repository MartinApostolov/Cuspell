# Magical Execution Semantics

_Status: working specification v0.1_

This file defines what happens when a grammatically valid Cuspell expression is used as magic.

The language and the magic engine remain separate:

- language determines meaning;
- the magic engine determines whether that meaning can be realized in the current world state.

## 1. A spell is a Command

A magical spell is a sentence in command mood:

`! EventSpec .`

The EventSpec may be simple or structurally complex.

Complex commands, conjunctions, sequences, and conditionals are legal when their semantic structures are valid and executable.

Magic does not impose a one-action-per-spell restriction.

## 2. Execution pipeline

A magical command is processed in ordered stages.

### Stage 1 — lexical parse

Every root/compound must exist and have one valid semantic parse.

Failure: lexical/grammatical invalidity.

### Stage 2 — type/frame check

All arguments, roles, Operators, dimensions, and nested structures must type-check.

Required roles must be present.

Failure: ill-typed Command.

### Stage 3 — semantic closure

The Command must constrain every execution-relevant degree of freedom or invoke an explicit deterministic default.

Magic does not fill gaps with caster intent.

Failure: semantically incomplete Command.

### Stage 4 — reference resolution

Every Reference must resolve according to its formal rule.

A singular role requiring one Entity fails if the reference resolves to zero or multiple Entities.

A collection role may resolve to a collection only when the frame accepts it.

Failure: reference-resolution failure.

### Stage 5 — constraint check

Accumulated Properties/Relations must be mutually satisfiable.

Failure: contradiction.

### Stage 6 — capability check

The requested event must be a kind of change the magical system is allowed to realize.

Language can describe things that magic cannot necessarily perform.

Failure: unsupported/impossible execution.

### Stage 7 — required-power evaluation

The engine computes the objective execution difficulty/power required by the requested change in the current world state.

### Stage 8 — resource payment

The caster must be able to pay the written mana cost and meet any system-level casting requirements.

### Stage 9 — commit

The magic attempts to realize the EventSpec under the composite-command rules below.

This staged model lets the implementation report exactly why a spell failed.

## 3. Mana cost

Base linguistic mana cost is:

> one mana per written meaning-bearing rune occurrence.

Examples of meaning-bearing runes:

- semantic roots;
- each `@`;
- Opposite;
- arithmetic operators;
- registered lexical noun roots;
- logical operators such as If/And when written.

Zero-mana syntax includes:

- word separators;
- grouping marks;
- sentence terminator;
- mood marks;
- grammatical case/role markers.

The cost is calculated from the written spell before semantic normalization.

Equivalent meanings can therefore cost different amounts.

## 4. Registered lexical compression

A registered one-rune word costs one rune even when its semantic definition is complex.

A long transparent expression costs every written semantic rune.

This is deliberate.

Personal aliases, Names, abbreviations, or temporary macros do not become magical lexical entries and do not grant compression.

## 5. Command power

Rune-count mana and execution strength must not be confused.

Introduce a command-level **Power** parameter.

Power is a typed magical execution quantity indicating how strongly reality is instructed to realize the EventSpec.

Temporary notation uses a grammatical role:

`:power <Quantity>`

When a Quantity appears in the Power slot, its unit/dimension is supplied by the magical frame.

A command with no explicit Power uses the system-defined minimum Power value of 1.

The exact surface glyph for Power is not finalized.

### Why Power exists

Some binary semantic requests can be extremely difficult despite being linguistically short.

For example:

`EndLife(target)`

is semantically precise, but ending the Life state of a tiny insect and a magically protected giant need not require equal execution strength.

The language describes the requested change; Power specifies the strength available to impose it.

## 6. Power preserves linguistic compression

Power values use the normal Quantity language.

Therefore a knowledgeable caster may express a large Power value using arithmetic compression.

The engine does **not** charge the expanded numeric value as extra linguistic mana.

This preserves the earlier design choice that mathematical knowledge can produce dramatically more power for fewer written runes.

## 7. RequiredPower

The magical engine defines an objective function conceptually:

`RequiredPower(EventSpec, resolved-world-state) -> Quantity<MagicPower>`

Factors can include, depending on the Event:

- affected mass/extent;
- distance;
- degree of state change;
- structural complexity;
- number of independently affected targets;
- target magical resistance/stability;
- persistence duration;
- rate of change;
- competing magical effects.

The exact gameplay calibration belongs in a later balance/rules table.

The important semantic rule is:

> RequiredPower is computed from defined rules, not improvised from how impressive the GM thinks the spell sounds.

## 8. Underpowered commands

If supplied Power is lower than RequiredPower, the default result is:

**no realization of that EventSpec.**

Magic does not automatically perform an arbitrary weaker version.

This prevents outcomes such as:

- half of an unspecified transformation;
- moving an object in an unintended direction;
- damaging a random subset of targets;
- partially satisfying an exact identity change.

## 9. Explicit scalable effects

Some Processes can declare a `scalable` execution trait.

A scalable EventSpec may accept an explicit construct equivalent to:

`UpTo(power/amount)`

or another bounded range.

Only then may the engine realize the greatest objectively defined effect within the supplied bound.

Partial execution must be requested by semantics; it is never the fallback for insufficient Power.

The exact rune for UpTo remains to be chosen.

## 10. Oversupplied Power

Supplying more Power than required does not automatically amplify the semantic effect.

An exact request remains exact.

Example:

if a command requests an exact destination, excess Power does not throw the target past the destination.

Extra Power can instead provide margin against resistance/competition where the execution model allows it.

To request a larger result, write a larger result.

## 11. Semantic closure

A magical Command must be **closed for execution**.

Examples:

- Move(This) with no destination/path/change amount may be a valid EventSpec description but is not executable if the Move frame leaves outcome location unconstrained.
- Change(This) without naming the attribute/result is not executable.
- "Make it hot" is not executable if Hot has no fixed threshold or explicit standard.
- LiquidMatter is a valid Kind but does not select a unique Entity.

The engine never chooses an aesthetically or narratively reasonable completion.

## 12. Contradictory commands

A well-typed but contradictory Command fails before world modification.

Example:

requiring one target simultaneously to satisfy mutually exclusive Phase values without a special mixed-phase model.

Contradiction is different from a type error and should be reported separately by a reference implementation.

## 13. Impossible or unsupported commands

The formal language may describe situations outside magical capability.

Examples could include setting-dependent prohibitions such as:

- creating certain protected substances;
- changing fundamental constants;
- affecting entities outside accessible reality;
- modifying protected identity/soul structures.

Such a sentence remains meaningful language but is non-executable magic.

This is how the system preserves a real language larger than the spell engine.

## 14. Parse-time versus run-time failure

Failures before a valid Command exists are **formulation failures**.

Failures after a valid Command is issued are **execution failures**.

Recommended gameplay rule:

- formulation failures do not activate the spell engine;
- execution failures consume the spell's written mana cost because the caster successfully issued a command that reality could not realize.

This prevents cost-free probing for hidden targets/resistance while avoiding punishment for a parser-invalid inscription.

Campaign rules may add mishaps, but they are not part of base semantics.

## 15. Reference failures

A magical Reference must resolve uniquely for a singular slot.

Cases:

- zero matches -> failure;
- multiple matches -> failure;
- wrong type -> failure;
- inaccessible reference context -> failure.

A command may explicitly operate on a collection if its frame/quantifier construction allows one.

Magic does not select the nearest, most dangerous, or most likely target unless that selection rule is written or built into the reference root.

## 16. Visibility and knowledge

Reference resolution is not automatically omniscient search.

Each Reference/selection operator declares what information it is allowed to use.

For example:

- This can use an explicitly designated referent;
- Self is inherently known;
- a Kind query inside a bounded region may use magical detection only if the selection mechanism grants it.

This prevents "target the assassin I do not know exists" from being smuggled into ordinary reference semantics.

Detection/search capabilities are explicit magical semantics.

## 17. Immediate Event atomicity

A single simple EventSpec is atomic at its semantic result boundary by default.

It either realizes the requested state transition or does not.

Internal physical microsteps do not count as partial success.

This is especially important for transformation/identity changes.

## 18. And-composites

`And(E1,E2,...)`

defines one composite request requiring all component EventSpecs without ordering.

Default execution rule:

- preflight all components against the same activation state where possible;
- if the composite cannot be jointly satisfied, the composite fails;
- compatible state changes may commit together.

Thus And behaves transactionally as a simultaneous composite, not as a sequence that may stop halfway.

## 19. Sequence

`Sequence(E1,E2,...)`

defines ordered execution.

Default rule:

- execute E1;
- if successful, evaluate/execute E2 against the resulting world state;
- continue in order;
- if a later step fails, already completed earlier steps remain.

There is no free rollback.

A future advanced `Atomic`/transaction Operator could request rollback semantics if the magic system supports it; such a capability should be meaning-bearing and costly.

## 20. Conditional commands

`If(condition, EventSpec)`

evaluates the Proposition at the defined activation time.

- true -> attempt the EventSpec;
- false -> no Event is requested.

A false condition is not an execution failure.

If the condition itself cannot be evaluated because references are unresolved or required information is unavailable, the conditional cannot activate successfully.

## 21. Or in commands

A disjunctive EventSpec is semantically meaningful but dangerous because "either branch" does not specify a selection policy.

Base magical rule:

> `Or(E1,E2)` is not executable as a Command unless a selection rule is present.

Possible future selectors include:

- FirstPossible;
- Cheapest;
- explicit priority order;
- Random;
- caster-selected branch before activation.

This prevents reality from choosing whichever result is most convenient to interpretation.

## 22. Natural persistence versus magical persistence

A completed Event may leave a normal world state that persists naturally.

Examples:

- a moved stone remains where normal physics leaves it;
- a cut remains until healed;
- heated material cools under normal laws.

No `Persist` rune is required merely for consequences to continue naturally.

## 23. `Persist`

`Persist` means:

> actively maintain a specified State/Relation/Process against ordinary evolution for a specified temporal condition.

Persist therefore creates an ongoing active `Magic` state.

It requires:

- the condition/state to maintain;
- duration or end condition;
- sufficient Power for maintenance.

No omitted duration means "forever."

A permanent or indefinite enchantment requires explicit advanced semantics.

## 24. Persistence power

RequiredPower for Persist may depend on:

- duration;
- target resistance;
- magnitude of maintained deviation from natural evolution;
- area/number of targets;
- external attempts to change the state.

How long durations scale numerically is a balance rule, but the inputs are explicit and objective.

## 25. Trigger

A simple Trigger has the form:

`Trigger(condition, action, lifetime, rearm?)`

and creates a persistent magical watcher that evaluates a Proposition and attempts an action when the trigger transition occurs.

When the action must use the participant that caused/matched the condition, Trigger uses an explicit pattern binder:

`Trigger(x:Domain, condition($x), action($x), lifetime, rearm?)`

The binder ranges over the declared Domain. Each trigger match binds the witness deterministically into the action. This is different from `Some`: existential quantification proves that a witness exists but does not export one.

Base defaults:

- one-shot;
- finite explicit lifetime required;
- condition scope/reference context frozen or formally defined at creation;
- action uses the Power/resource parameters stored in the Trigger;
- no hidden witness/target selection.

A Trigger therefore carries an active Magic state until fired, expired, or dispelled.

## 26. Repeat

Finite Repeat is defined as:

`Repeat(count, EventSpec)`

where count is a nonnegative integer Quantity.

It expands semantically to an ordered repetition structure but retains the written cost of the compressed Repeat expression.

This is another legitimate language-compression mechanism.

Whether iterations are simultaneous or sequential must be declared by Repeat's frame; default is sequential recurrence.

## 27. Infinite repetition

An unbounded loop is not implied by Repeat.

Indefinite recurrence requires explicit lifetime/condition semantics and active persistence.

This avoids a one-rune accidental infinite loop.

Advanced forms may include:

- RepeatUntil(condition)
- Trigger with rearm
- persistent periodic Events

All remain valid directions because program-like complexity is not banned; they simply require complete semantics.

### Temporal well-foundedness

Control structures may not require an infinite number of Event activations at the same TimePoint.

The execution engine detects zero-time recursive cycles such as a Trigger whose action immediately recreates/re-fires the same Trigger without temporal progress.

Such a structure is non-executable unless the specification includes a positive temporal step or another rule that proves finite activation at each TimePoint.

This is an execution-safety/consistency rule, not a ban on loops.

## 28. Dispel

With Magic defined as an active magical-state Property:

`EndMagic(target)`

is the semantic core of dispelling.

The target must identify the active magical state/effect to terminate.

If several distinct magical states exist and the reference does not select which, a singular dispel is unresolved.

RequiredPower can depend on the target effect's persistence Power/stability.

## 29. Enchantment

An enchantment is not a separate ontological mystery.

Working analysis:

- a target Entity;
- an actively maintained Magic state;
- one or more persisted Properties/Relations/Trigger structures;
- duration/end condition.

A conventional Enchant rune may later lexicalize this common semantic molecule.

## 30. Existence transitions and fresh generation

Existence is a state predicate.

- `Begin Exist X` can reinstate an already identifiable non-active subject when the world ontology permits it.
- `End Exist X` is the compositional destruction meaning for an identifiable subject.
- the minimized base lexicon has no universal Create root that can allocate a fresh Entity from an underspecified Kind.

Fresh Entity generation therefore requires explicit future/world generation machinery with a deterministic profile, result identity/cardinality, and capability rules. It must not be inferred merely from a Kind name.

## 31. Transformation

`Change` modifies specified attributes/structure.

A transformation Command must state enough target-state constraints to be closed.

A destination Kind by itself is sufficient only if that Kind entry supplies a deterministic generation profile or a registered source-to-target mapping.

Otherwise additional target profile/template data is required.

Transformation preserves compatible source properties only where the registered mapping says to preserve them. It may not invent arbitrary optional features merely because many outputs would satisfy the destination Kind.

If multiple valid target realizations remain after all registered rules apply, the transformation is semantically incomplete.

## 32. Restoration and repair

Repair can use a recognized prior/Kind structural profile to reduce Damage and restore Whole.

It must specify which restoration reference is used when several are possible:

- current Kind's canonical healthy structure;
- a recorded former state;
- an explicitly referenced template.

Magic does not assume "how it looked before" unless a former-state reference is semantically available.

## 33. Detection as execution

Queries/questions are not automatically spells.

A magical detection spell must explicitly create/access Information.

This prevents ordinary logical expressions from granting omniscience.

Question mood asks; magic must have an Information-acquisition Process to answer from reality.

Future roots such as Sense, Find, Know, or Reveal can provide this capability under defined scopes.

## 34. Competing simultaneous magic

When multiple magical Commands attempt incompatible state changes at the same effective time, the engine needs an objective contest rule.

Working model:

1. compatible constraints merge;
2. incompatible active commands compare effective Power after resistance/modifiers;
3. higher effective Power takes precedence for the contested constraint;
4. exact ties do not choose arbitrarily: the contested change fails/stalls unless another rule breaks the tie.

The precise tabletop formula can include system modifiers, but the semantic outcome must not depend on narrative preference.

## 35. Existing magic as resistance

An active Persist/Magic state can contribute resistance to contrary changes.

This makes enchantments and dispels interact through the same general Power mechanism rather than bespoke exceptions.

## 36. Collection targets

A command over many targets must use an explicit collection/distribution structure.

RequiredPower may scale with the actual resolved collection according to the game rule.

The selection scope must be bounded/defined.

A singular Process does not silently distribute over a Collection.

`Each` creates a distributed CompositeEventSpec with explicit collection/binder semantics.

## 37. Caster ignorance and hidden RequiredPower

The caster need not know the exact RequiredPower.

They may supply a value and risk execution failure.

Because runic arithmetic allows compression, experienced casters can economically overprovision Power.

This creates useful uncertainty without semantic ambiguity.

## 38. Command result records

For implementation, execution should return a structured result such as:

- Parsed
- TypeValid
- Closed
- ReferencesResolved
- ConstraintsSatisfiable
- CapabilitySupported
- RequiredPower
- SuppliedPower
- ManaCost
- Outcome
- FailureReason
- ResultingEvent IDs

This makes the system testable and removes GM-only hidden categories of failure.

## 39. Open balance layer

This specification intentionally does not yet choose numeric formulas for:

- RequiredPower by mass/distance;
- biological resistance;
- transformation complexity;
- duration scaling;
- collection scaling;
- contest modifiers.

Those are balance constants/functions, not language semantics.

They should later live in a separate game-rules specification so semantic language changes do not require rebalance and vice versa.

## 40. Execution principle

The core rule is:

> Magic executes the exact closed semantic structure that was written, if the structure is supported, references resolve, constraints are satisfiable, resources are paid, and supplied Power meets the objectively computed requirement.

It never executes "what the caster meant."
