# Social and Affective Second-Pass Audit

_Status: checkpoint 87 — family-level reduction experiment complete; no net-safe reduction found_

## Scope

This audit tests the next high-leverage family from
`docs/SECOND_PASS_PRIMITIVE_FAMILY_MAP.md`.

Current family:

- affective attitudes/states:
  `Like`, `Love`, `Hate`, `Fear`, `Admire`, `Respect`, `Trust`,
  `JealousOf`, `CompassionFor`, `GratefulTo`, `GrieveFor`,
  `RemorseFor`, `ShameAbout`, `Angry`, `Happy`, `Sad`;
- social/institutional relations:
  `FriendOf`, `EngagedTo`, `ParentOf`, `SpouseOf`, `Have`, `Own`,
  `ResponsibleFor`;
- social evaluation/repair:
  `Evaluate`, `Reputation`, `Forgive`.

The family contains **26 semantic primitive candidates**.

The question is whether repeated experiencer/target structure, positive/negative
valence, social role structure, or evaluation machinery can replace several roots
with a smaller exact semantic basis.

## Reduction rule

A generic wrapper does not count as a reduction if it still requires one atomic
value for every old root.

For example:

`Attitude Self This LoveKind`

does not reduce `Love` if `LoveKind` is an irreducible semantic atom whose whole
meaning is "love". It would preserve the old primitive and add another
meaning-bearing constructor.

The same applies to:

- `Emotion(subject, HappyKind)`;
- `SocialRelation(a,b,SpouseKind)`;
- world-model tags that merely rename the deleted root;
- Old Names whose expansions still contain an equivalent hidden atom.

## Existing general machinery tested

The current language already has reusable machinery around this family:

- `Evaluate(evaluator,target) -> EvaluationValue`;
- `High` / `Low` threshold-property formation over ordered descriptors;
- `More` for ordered comparison;
- `Expect`, `Believe`, `Confidence`, `Want`, and `Intend`;
- `Beneficiary`, `Cause`, `ResponsibleFor`, `Have`, `Control`;
- `Begin` / `End` for persistent-state transitions;
- `Opposite` for declared semantic-axis inversion where an exact axis exists;
- quantification and shared-role composition, already used to remove `SiblingOf`;
- speech composition, already used to remove `Thank` and `Apologize`.

These successful previous reductions are useful controls: this audit should accept a
social reduction only when it is comparably exact.

## Experiment A — one generic Attitude relation

Candidate shape:

`Attitude(experiencer,target,kind)`

The apparent common structure is real, but the distinguishing content remains
irreducible.

At minimum the current family still needs independent distinctions for:

- liking;
- love/affection;
- hatred/hostility;
- fear;
- admiration;
- respect;
- trust;
- jealousy;
- compassion;
- gratitude;
- grief;
- remorse;
- shame.

One `kind` value per distinction preserves thirteen semantic atoms and adds an
`Attitude` root.

**Result: inventory grows. Reject.**

## Experiment B — reduce positive/negative attitudes to Evaluate

The strongest possible reuse candidate is `Evaluate`.

Several social attitudes correlate with positive or negative evaluation, but none is
identical to an ordered evaluation score:

- someone may **like** a flawed thing while evaluating it poorly;
- someone may **admire** skill without liking the person;
- someone may **respect** an opponent while disliking them;
- someone may **love** a person while judging many of their actions negatively;
- someone may **hate** a target while still respecting or admiring some qualities;
- `Trust` concerns reliance, not general approval.

This differs from the successful removal of `Prefer`: preference really is an
ordering between evaluator-relative values, so
`More Evaluate evaluator A Evaluate evaluator B` preserves its truth conditions.
The attitude roots above add different state content.

Likewise `Admire X Y` is not exactly `High Evaluate X Y`, and neither is
`Respect`, `Like`, or `Love`.

**Result: retain these attitudes; Evaluate remains a reusable comparison basis, not
a universal attitude scale.**

## Experiment C — Happy/Sad as one valence axis

A tempting count reduction is:

- introduce one ordered `Valence(subject)` descriptor;
- `Happy subject` -> `High Valence subject`;
- `Sad subject` -> `Low Valence subject`.

Numerically this would appear to replace two roots with one.

It is not exact. Happiness and sadness are not guaranteed to be opposite thresholds
on one scalar. Mixed/bittersweet states can contain both, and low happiness is not
the same proposition as sadness. A one-dimensional valence model would add world
psychology assumptions that the current roots do not entail.

Using separate positive-affect and negative-affect descriptors would preserve more
truth conditions, but then two roots merely become two descriptors and no inventory
reduction occurs.

`Angry` additionally carries an anger state that is not determined by either
positive or negative valence alone.

**Result: retain `Happy`, `Sad`, and `Angry`.**

## Experiment D — use Opposite for Happy/Sad or Love/Hate

`Opposite` is a declared semantic-axis inverse, not a free antonym generator.

Neither pair is exact enough:

- Happy and Sad are not logical complements and need not exclude co-occurrence;
- Love and Hate are not exact inverses and can coexist in complex attitudes;
- absence or reduction of one does not entail the other.

The current `Hate` lexical note already explicitly distinguishes hatred from a
simple Opposite-of-Love analysis.

Generalizing `Opposite` to these pairs would therefore change their truth
conditions rather than remove a redundant rune.

**Result: reject.**

## Experiment E — derive Trust from Expect / Confidence / Believe

`Trust(truster,trusted)` is persistent interpersonal reliance/confidence in an
Entity.

Existing epistemic roots target different objects:

- `Believe` targets a Proposition;
- `Confidence` measures confidence in a Proposition;
- `Expect` targets expected semantic/event content.

To reconstruct general interpersonal trust, a composition would need to quantify
over an open set of propositions or actions on which the truster relies. That
selection itself is contextual and does not equal the existing binary Trust state.

Trust in one specific proposition remains expressible through Believe/Confidence,
but that does not make the interpersonal relation redundant.

**Result: retain `Trust`.**

## Experiment F — derive Fear, Jealousy, Compassion, Gratitude, Grief, Remorse, Shame

These relations have useful connections to other states but not equivalences.

### Fear

Fear is not simply `Want Not target`, negative Evaluate, or low Confidence.
A feared Entity is not itself a Proposition/EventSpec whose negation can stand in
for the fear state.

### JealousOf

Jealousy can involve Want, Fear, Have/Own, Love, or competition, but no fixed
conjunction of those is necessary and sufficient for jealousy.

### CompassionFor

Compassion often involves awareness of suffering and a prosocial orientation, but it
does not reduce exactly to Sad + Want. The core also deliberately has no generic
"suffering" proposition whose presence would close such a definition.

### GratefulTo

Gratitude toward a benefactor is not just positive evaluation plus having benefited.
A person can acknowledge benefit without gratitude, or feel gratitude for a basis
that is not captured by one generic Beneficiary proposition.

The optional `:basis` role therefore remains part of GratefulTo rather than making
the relation derivable.

### GrieveFor

Grief is a directed/persistent response to loss or suffering, not generic Sadness.
A grieving person can have moments of happiness while still grieving.

### RemorseFor vs ShameAbout vs ResponsibleFor

These three are independent:

- responsibility may be attributed without remorse or shame;
- remorse can concern one's action/consequence without requiring a shame state;
- shame can concern a property or social fact not represented as an outcome for
  which the subject is ResponsibleFor.

Therefore neither
`And {ShameAbout X Y,ResponsibleFor X Y}`
nor any subset is equivalent to RemorseFor.

**Result: retain all seven distinctions.**

## Experiment G — generic SocialRelation for institutional relations

`FriendOf`, `ParentOf`, `SpouseOf`, `EngagedTo`, `Have`, `Own`, and
`ResponsibleFor` all have Entity-related frames, but the shared arity does not
supply shared semantics.

A generic:

`SocialRelation A B relation-kind`

would require one irreducible relation-kind value per current relation and would
therefore increase the inventory.

The roots also fail pairwise reductions:

- `ParentOf` is not Cause, Have, Own, or Control;
- `SpouseOf` is not FriendOf and is distinct from `EngagedTo`;
- `Own` is a property-right relation, while `Have` is broader holding/possession;
- `Control` is intentionally distinct from Have and Own;
- `ResponsibleFor` is not Cause: responsibility may be institutional/moral/legal,
  and causal contribution does not automatically imply responsibility.

The world model may decide when a marriage, engagement, ownership claim, or
responsibility attribution is valid. That does not remove the semantic identity of
the relation from the language.

**Result: retain the seven relations.**

## Experiment H — Reputation as aggregate Evaluate

A person's reputation often depends on other people's evaluations, making this a
promising structural idea.

But current `Reputation(subject,:community?) -> EvaluationValue` denotes public or
community standing. It is not defined as a simple arithmetic total/mean of
`Evaluate(member,subject)` values.

An exact reduction would require at least:

- selecting the relevant community;
- selecting which evaluations count;
- weighting/aggregation rules;
- handling institutional reputation not reducible to current individual opinions.

Adding a generic aggregation mechanism may be useful later, but without those rules
it would not make Reputation equivalent to Evaluate.

**Result: retain `Reputation`.**

## Experiment I — Forgive from ending negative states

This was already tested in the first exact-reduction audit and remains unchanged.

`Forgive(forgiver,offender,:offense?)` can coexist with:

- continued anger;
- memory of the offense;
- continued attribution of responsibility;
- lack of Love or Like.

Therefore it is not `End Hate`, `End Angry`, `Not ResponsibleFor`, or a
conjunction of those transitions.

**Result: retain `Forgive`.**

## Boundary roots that are already good abstractions

### Evaluate

`Evaluate` is already productive enough to remove:

- `Prefer` through ordered comparison;
- `Should` through contextual High evaluation;
- `ImportantTo` through contextual High evaluation.

That is evidence that the root captures a real reusable semantic axis. It should not
be stretched until unrelated affective states become synonyms of evaluation.

### ParentOf

`ParentOf` already supports the exact removal of `SiblingOf` through shared-parent
quantification. That is a successful relational decomposition without inventing a
generic Kinship enum.

### GratefulTo and RemorseFor

These support removal of the speech-act conveniences `Thank` and `Apologize`
through addressed `Say`. The surviving roots are the underlying sincere state
content, not redundant speech wrappers.

## Count result

No social/affective root is removed and no new attitude/social-relation wrapper is
added.

Current inventory remains:

- **208 registered base entries**;
- **128 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The social/affective family remains **26 semantic primitive candidates**.

## Design conclusion

The repeated structure in this family is mostly **argument shape**, not duplicated
meaning.

Several current roots are already productive abstraction points—especially
`Evaluate`, `ParentOf`, `GratefulTo`, and `RemorseFor`—and have already
eliminated more superficial vocabulary. The remaining attitude and social-relation
roots cannot currently be compressed without either changing truth conditions or
moving each old distinction into one new enum/tag.

The family should be revisited only if Cuspell later gains independently motivated
machinery such as:

- a rigorous multi-dimensional affect model;
- a generic social-role/institution ontology whose relation values are themselves
  compositionally defined;
- a community aggregation model that makes Reputation derivable;
- reusable causal/appraisal semantics for gratitude, grief, remorse, shame, or
  jealousy.

The next second-pass family should therefore be **agency, mental stance, deontics,
and event roles**.
