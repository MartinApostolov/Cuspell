# Beginner Spellcraft

_Status: modular beginner progression v0.6 — checkpoint 139_

The first Cuspell lesson is now an **11-sign semantic core**.

Checkpoint 135's 16-sign set was much better than the old 50-sign starter, but stress testing found that its final step still bundled too many new ideas together: measured attributes, an Old Name unit, `@`, a typed binder, bound-variable reuse, fresh creation, a creation profile, and an immediate continuation all arrived at once.

So the progression is now split into:

- **11-sign core** — movement, state change, and simple yes/no discovery;
- **2-sign Light module** — measured attribute change;
- **2-sign Create module** — fresh identity and binder scope;
- **2-sign duration module** — an explicit interval plus active maintenance;
- **1-sign protection module** — block one exact EventSpec over that interval;
- **2-sign shared-representation module** — one explicit sensory channel plus the objective carrier/content relation;
- **1-sign conjunction module** — combine propositions/states explicitly;
- **2-sign event-composition module** — ordered `Sequence` versus simultaneous `Concurrent`;
- **1-sign repetition module** — finite `Repeat`;
- **3-sign multi-target module** — explicit `Collect` + `Member` + `Each`;
- **1-sign watcher module** — simple one-shot `Trigger`.

The progression reaches **28 semantic signs** after all ten modules, but the 11-sign core remains unchanged.

The old 50-sign SRD coverage set remains in `SPELLCRAFT_COVERAGE.md`.

## 1. First six signs

`This There Move Begin End Whole`

A magical command ends in:

`!`

With only these six signs:

`Move This There!`

Move the designated Entity to the designated Location.

`Begin Whole This!`

Begin structural wholeness.

`End Whole This!`

End structural wholeness.

The first lesson therefore teaches only three reusable shapes:

- `Move target destination!`
- `Begin state!`
- `End state!`

No binders, units, collections, timing, or programming are needed.

## 2. Add three reusable words

Add:

`You Locked Magic`

Cumulative total: **9 signs**.

The grammar does not change.

`Move You There!`

`Begin Locked This!`

`End Locked This!`

`Begin Magic This!`

`End Magic This!`

The point of this step is that new state vocabulary reuses the same Begin/End machinery.

`Magic` here means the Entity's magical state. The more advanced EventSpec/Event provenance uses of `Magic` are not part of the beginner lesson.

## 3. Add bounded yes/no discovery

Add:

`Self Find`

Cumulative total: **11 signs**.

The beginner only learns the simple yes/no Find form:

`Find Self This Whole This!`

`Find Self This Locked This!`

`Find Self This Magic This!`

The repeated `This` is deliberate.

The first `This` supplies the explicit information-access scope. The final `This` is the subject inside the queried proposition.

So:

`Find Self This Locked This!`

means:

> within the explicitly designated subject/scope, determine truthfully whether that subject is Locked and make Self know the answer.

Open-query binders and broad searches are later material.

## 4. The complete 11-sign core

`Self This You There`

`Move Begin End Find`

`Whole Locked Magic`

That is the semantic core.

It supports eleven curated first spells:

| Spell idea | Cuspell |
| --- | --- |
| Move something | `Move This There!` |
| Move a person | `Move You There!` |
| Mend | `Begin Whole This!` |
| Break | `End Whole This!` |
| Lock | `Begin Locked This!` |
| Unlock | `End Locked This!` |
| Mark magical | `Begin Magic This!` |
| End selected Magic state | `End Magic This!` |
| Check integrity | `Find Self This Whole This!` |
| Check a lock | `Find Self This Locked This!` |
| Detect Magic state | `Find Self This Magic This!` |

This is intentionally small enough that every semantic sign appears in the first spellbook.

## 5. First follow-on module — Light and measured attributes

Add only:

`Change Light`

Cumulative semantic vocabulary: **13 signs**.

This module also teaches two pieces of notation:

- `@` = the positive unit number 1;
- `«LightUnit»` = the established Light unit Old Name.

Now:

`Change This Light «LightUnit» @!`

sets an already-existing Entity's Light output to one LightUnit.

This module is separate because `Change` has a new three-part pattern:

`Change target attribute value!`

and measured quantities are a new idea even though only two new semantic signs are added.

## 6. Second follow-on module — fresh creation

Add only:

`At Create`

Cumulative semantic vocabulary: **15 signs**.

Creation now introduces the first binder syntax:

`x:Entity`

means “bind a fresh Entity as x,” and:

`$x`

refers to that bound Entity.

The creation example deliberately reuses `There`, `Change`, `Light`, `«LightUnit»`, and `@` instead of introducing more vocabulary at the same time:

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

Meaning:

1. allocate one fresh Entity;
2. establish it at the already-designated Location `There`;
3. keep that fresh identity in scope;
4. immediately set its Light output.

This is the beginner Light creation spell.

The exact visible Form is still a world-realization question. If a setting's generation rules deterministically realize this profile as a glowing orb, it is an orb. Cuspell does not silently invent shape/material details.

## 7. Third follow-on module — duration and active maintenance

Add:

`ThisInterval Persist`

Cumulative semantic vocabulary: **17 signs**.

`ThisInterval` is a typed reference to **one objectively designated TimeInterval** supplied by the command/casting environment.

It does not mean “some duration,” and it does not mean “forever.”

Now the already-known state vocabulary can be maintained:

`Persist Whole This ThisInterval!`

`Persist Locked This ThisInterval!`

`Persist Magic This ThisInterval!`

The new pattern is:

`Persist state interval!`

`Persist` means actively maintain the specified state against ordinary evolution over the interval. It is not taught as another spelling of `Begin`.

So `Persist Whole This ThisInterval!` means “keep this Whole during the designated interval,” not automatically “repair this and then keep it Whole.” Establishing a missing state and maintaining it are distinct meanings.

No duration is silently omitted. A permanent enchantment therefore does not come from leaving `ThisInterval` out.

## 8. Fourth follow-on module — exact-event protection

Add only:

`Prevent`

Cumulative semantic vocabulary: **18 signs**.

The beginner learns only the simple form:

`Prevent event interval!`

Examples:

`Prevent Move This There ThisInterval!`

blocks that exact movement EventSpec over the designated interval.

`Prevent End Whole This ThisInterval!`

blocks the exact `End Whole This` transition over that interval.

`Prevent Begin Locked This ThisInterval!`

blocks the exact `Begin Locked This` transition over that interval.

This is intentionally **exact protection**, not “prevent anything bad.”

It also does not automatically cover every physical process that could produce a similar final state. For example, preventing the written `End Whole This` EventSpec is not a hidden universal ban on every conceivable way the object might be damaged.

Full antimagic-style interception is later material. Cuspell already supports the advanced bound form:

`Prevent e:EventSpec Magic $e _ ThisInterval!`

but that introduces an EventSpec binder, a predicate matcher, the omission marker, and execution-interception semantics, so it is not part of this beginner module.

## 9. Fifth follow-on module — shared visual representation

Add only:

`Vision Represent`

Cumulative semantic vocabulary: **20 signs**.

`Vision` is the first explicit `SenseChannel` taught in the progression.

`Represent` states:

`Represent carrier content channel`

The carrier and the represented content are different things.

For example:

`Begin Represent This You Vision!`

means the designated carrier `This` begins visually depicting `You`.

The reverse transition is:

`End Represent This You Vision!`

If an already-established representation must be actively maintained:

`Persist Represent This You Vision ThisInterval!`

This reuses `Begin`, `End`, `Persist`, and `ThisInterval` instead of introducing new control grammar.

### Shared does not mean forced perception

`Represent` is an objective state of the carrier.

It does **not** mean:

- every observer is forced to see it;
- an observer believes it;
- an observer understands it;
- the represented thing is physically present;
- the represented content is true.

Observers perceive the same carrier through ordinary channel/access rules. That is what makes the representation shared without enumerating observers.

### Fresh visual representation carrier

The previous Create lesson can now be reused without adding `And` or `Sign`:

`Create i:Entity At $i There Begin Represent $i This Vision!`

This means:

1. allocate a fresh Entity;
2. place it at the designated destination `There`;
3. keep the fresh binder in scope;
4. make that carrier begin visually representing `This`.

The carrier need not automatically be Matter or solid.

Its exact visible realization still depends on deterministic world/media rules. If the active world cannot realize the written carrier/content/channel profile precisely enough, execution fails rather than inventing artistic details.

### Other channels are vocabulary expansion

After `Vision` is understood, other channels can be learned independently.

For example:

`Begin Represent This You Hearing!`

or:

`Begin Represent This You TouchChannel!`

Those do not belong to the required 20-sign path.

A tactile representation also does not silently gain mass, collision, damage, or other physical properties.

## 10. Sixth follow-on module — explicit conjunction

Add only:

`And`

Cumulative semantic vocabulary: **21 signs**.

Canonical Cuspell uses spoken-order infix conjunction:

`Whole This And Magic This`

The beginner first uses `And` to combine propositions/state propositions, not to learn its more advanced EventSpec transaction semantics.

For example, a bounded query can ask about two facts in one Proposition:

`Find Self This Whole This And Magic This!`

A Create profile can likewise conjoin two facts before its continuation:

`Create i:Entity At $i There And Magic $i Begin Represent $i This Vision!`

Here `At $i There And Magic $i` is the fresh Entity's profile, while `Begin Represent ...` is the already-known continuation.

Same-operator chains remain flat. Mixed `And` / `Or` grouping is later material.

## 11. Seventh follow-on module — ordered versus concurrent events

Add:

`Sequence Concurrent`

Cumulative semantic vocabulary: **23 signs**.

This repairs one omission in the earlier programming candidate list: it mentioned `Concurrent` but not `Sequence`.

General programming needs both.

### Ordered execution

`Sequence Move This There Begin Magic This!`

means:

1. attempt `Move This There`;
2. only if that succeeds, evaluate/attempt `Begin Magic This` against the resulting world state.

There is no free rollback of already-completed earlier steps if a later step fails.

### Concurrent execution

`Concurrent Move This There Begin Magic You!`

requests those component EventSpecs concurrently.

`Sequence` and `Concurrent` both use flat event lists. When the list reaches the sentence end, `!` closes it automatically.

The zero-mana grammatical markers `SequenceEnd` and `ConcurrentEnd` are only needed when later material must follow in the same sentence; the first examples do not require them.

The special continuation inside `Create` does not replace general `Sequence`. It exists only to keep one fresh result binder in lexical scope for an immediate follow-on EventSpec.

## 12. Eighth follow-on module — finite repetition

Add only:

`Repeat`

Cumulative semantic vocabulary: **24 signs**.

The beginner learns only finite count-based repetition:

`Repeat count event!`

For example:

`Repeat @@@ Create x:Entity At $x There Change $x Light «LightUnit» @!`

repeats the whole fresh-creation EventSpec three times.

Because each `Create` invocation allocates a new identity, this requests three distinct fresh light sources.

`Repeat` does not imply an infinite loop. The count must be an explicit nonnegative integer quantity.

## 13. Ninth follow-on module — bounded multi-target magic

Add:

`Collect Member Each`

Cumulative semantic vocabulary: **27 signs**.

Cuspell never silently distributes a singular Process across a group.

The learner therefore sees all three pieces together:

1. `Member` states objective group membership;
2. `Collect` builds the typed collection;
3. `Each` instantiates an EventSpec once for every resolved member.

Example:

`Each Collect x:Entity Member $x This y:Entity Begin Magic $y!`

Read it as:

1. collect every Entity `x` that is a Member of the designated group `This`;
2. take each resolved member as `y`;
3. perform `Begin Magic $y` for each member.

The same pattern can reuse the earlier Light module:

`Each Collect x:Entity Member $x This y:Entity Change $y Light «LightUnit» @!`

### This is not omniscient search

For these examples, `This` must designate a group whose membership is objectively resolvable in the active context.

`Collect` does not search the entire world just because the binder says `Entity`.

If the group/domain cannot be resolved, the multi-target command cannot guess.

`Each` also does not imply a hidden ordering between member events.

## 14. Tenth follow-on module — simple reactive programming

Add only:

`Trigger`

Cumulative semantic vocabulary: **28 signs**.

The first form is:

`Trigger condition action lifetime!`

For example:

`Trigger Locked This End Locked This ThisInterval!`

creates a watcher over the designated interval. When the Locked condition fires under Trigger semantics, it attempts:

`End Locked This!`

Another example:

`Trigger Magic This End Magic This ThisInterval!`

This watches the selected Entity's Magic state and attempts to end it when the trigger fires.

The beginner Trigger is:

- one-shot by default;
- finite-lifetime;
- explicit about both condition and action;
- not allowed to invent a hidden matching target.

Cuspell also has a bound-witness Trigger form, where a matched binder can be exported into the action, but that is later material.

## 15. Why `Here` and `Ill` left the required set

Checkpoint 135 required both.

The stress test found neither was a prerequisite.

### `Here`

Creation can reuse the already-known `There`:

`Create x:Entity At $x There Change $x Light «LightUnit» @!`

So `Here` is useful convenience vocabulary, not a required teaching sign.

If learned later:

`Create x:Entity At $x Here Change $x Light «LightUnit» @!`

is the caster-local version.

### `Ill`

`Ill` adds useful vocabulary, but no new grammar.

Once Begin/End/Find are understood, adding `Ill` immediately gives:

`Begin Ill You!`

`End Ill You!`

`Find Self You Ill You!`

That makes it a good example of **ordinary vocabulary expansion**, not a sign everyone must memorize in the core.

`Magic` replaces it in the core because the same single sign supports Begin/End/Find while being more central to spellcraft.

## 16. What remains deferred

The core and first ten modules still do **not** require:

`TimeFlow`

The remaining required module introduces altered temporal progression through `TimeFlow`.

Several **advanced uses of already-known signs** also remain deferred: event-level transactional `And`, mixed logical grouping, bound-witness `Trigger`, general collection selectors, bound antimagic/interception `Prevent`, and richer multi-channel/programmed illusion profiles.

## 17. Teaching rule

Count semantic signs separately from syntax.

The 11-sign core really does use only 11 registered semantic signs, but the later modules also teach grammar/notation such as:

- `@`;
- Old Names;
- `name:Type` binders;
- `$name` variables;
- Create profile/continuation scope.

Those are genuine things a learner must understand even though they are not additional semantic rune entries.

That distinction is why the old 16-sign count understated the difficulty of its final tier.

For the broader 50-sign SRD stress test, see `SPELLCRAFT_COVERAGE.md`.
