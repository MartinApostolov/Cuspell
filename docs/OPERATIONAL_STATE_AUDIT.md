# Operational and Body-State Second-Pass Audit

_Status: checkpoint 92 — family-level reduction experiment complete; no net-safe reduction found_

## Scope

This audit tests the four-root operational/body-state family:

- `Awake`
- `Sleep`
- `Open`
- `Locked`

All four are persistent StateProposition-producing Properties and therefore already
share the general `Begin` / `End` transition machinery.

The question is whether the state predicates themselves are duplicate values of a
smaller reusable state axis.

## Reduction rule

A state-axis refactor counts only if it reduces irreducible semantic distinctions.

For example,

`State subject SleepKind`

does not reduce `Sleep` if `SleepKind` is a new atomic value whose entire meaning
is "sleeping". Likewise, replacing Awake/Open/Locked with one value each under a
generic State operator would increase the inventory.

Negation is acceptable only when two predicates are exact complements under the
current semantics, not merely common antonyms in English.

## Experiment A — Sleep = Not Awake

This is not exact.

`Awake(subject)` means a persistent wakefulness state.

`Sleep(subject)` means a persistent sleep state.

The complement of awake is broader than sleep. A subject can be non-awake because
of, for example:

- unconsciousness;
- anesthesia;
- coma;
- incapacitation;
- other world-defined inactive/altered states.

Those possibilities need not satisfy Sleep.

Conversely, making Sleep exactly Not Awake would force every non-awake state into the
sleep category and erase distinctions that a world model may need.

The existing `Sleep` entry is also explicitly contextual, while `Awake` is the
more direct wakefulness state; this is further evidence that they are not currently
declared Boolean complements.

**Result: retain both.**

## Experiment B — Awake = Not Sleep

This fails for the same reason in the other direction.

Not sleeping does not imply wakefulness. A subject may be unconscious, anesthetized,
or otherwise neither sleeping nor awake under the active world model.

Therefore the pair is mutually constraining in many ordinary worlds but not an
exhaustive two-value partition in the language.

**Result: retain both.**

## Experiment C — one consciousness-state dimension

A more general design could introduce something like:

`ConsciousnessState(subject) -> value`

with values for awake, sleep, coma, anesthesia, and so on.

That can be useful world modeling, but it does not currently reduce the semantic
alphabet. At minimum Awake and Sleep would still require two distinct values, plus
the new descriptor/state relation.

Unless the values themselves become compositionally generated from a smaller
independently useful basis, this is enum-shaped fake compression.

**Result: reject for root minimization.**

## Experiment D — Locked = Not Open

This is also not exact.

`Open(subject)` is the object's contextual open-state relative to its
closure/design.

`Locked(subject)` is a persistent lock/seal state supplied by the world model.

The two axes differ:

- an object can be closed but unlocked;
- an object can be locked because a locking mechanism is engaged, which says more
  than merely "not open";
- some designs can be open while a separate lock is engaged on another moving or
  access component;
- "not locked" does not imply open.

Thus `Locked` is not the negation of `Open`, and `Open` is not the negation of
`Locked`.

**Result: retain both.**

## Experiment E — Open and Locked as one accessibility scale

A candidate abstraction such as:

`Accessibility(subject) -> EvaluationValue`

would not preserve the current meanings.

Open is a structural/configuration state. Locked is a mechanism/security state.
Neither is merely high or low accessibility:

- an unlocked but closed door may still have low immediate access;
- an open but guarded aperture can be accessible geometrically but not permitted;
- a locked mechanism can coexist with openings elsewhere on the same entity.

A scalar would conflate geometry, mechanism state, and permission/access control.

**Result: reject.**

## Experiment F — derive Locked from Control / Can / Permitted

Locking often affects capability, control, or permission, but none is equivalent to
the lock state.

- `Can A Open X` is agent-relative capability;
- `Permitted A Open X` is authorization;
- `Control A X` is controller/target relation;
- `Locked X` is a state of X or its lock mechanism.

A lock may exist even when a particular agent can bypass it, has permission to open
it, or controls the object.

**Result: retain Locked.**

## Existing transition abstraction is already the useful compression

The family does share one real abstraction, but it already exists:

- waking -> `Begin Awake X`;
- becoming asleep -> `Begin Sleep X`;
- opening -> `Begin Open X`;
- closing -> `End Open X`;
- locking -> `Begin Locked X`;
- unlocking -> `End Locked X`.

This avoids separate Wake/Open-as-Process/Close/Lock/Unlock roots where the ordinary
meaning is exactly state onset or cessation.

The remaining Properties are therefore the underlying state content, not redundant
transition verbs.

## Old Name check

Draft Old Names do not protect these roots.

Current historical compounds include:

- `«SleepThing»`;
- `«AwakeSleep»`.

The latter is explicitly fossilized historical wording for meditation, not a live
logical conjunction that proves Awake and Sleep are simultaneous or complementary.

If either root were later removed by a stronger exact analysis, the Old Names could
be rebuilt. No such exact analysis exists here.

## Count result

No root is removed and no generic state-axis wrapper is added.

Current inventory remains:

- **206 registered base entries**;
- **126 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The operational/body-state family remains **4 semantic primitive candidates**.

## Design conclusion

These four roots divide into two pairs that look antonymic in ordinary English but
are not exact logical complements in the current semantics:

- Awake / Sleep are different biological/mental states, with room for states that
  are neither;
- Open / Locked describe different physical axes, configuration vs locking
  mechanism.

The useful generalization is already `Begin` / `End`, which removes transition
verbs without erasing the persistent state distinctions.

The next second-pass target should be the **foundational ontology and
classification** family, followed by the small **change/causation/transfer/control**
family if no ontology reduction appears.
