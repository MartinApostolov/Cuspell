# Multi-Frame Lexical and Grammar Audit

_Status: checkpoint 99 — all 51 checkpoint-98 multi-frame entries audited_

## Purpose

Checkpoint 97 established that Cuspell does not have one grammar rule per rune. This audit asks the narrower learner-facing question:

> When one surface root has several semantic frames, are those frames one coherent typed operation, a contextual shorthand, or genuinely different lexical senses?

The audit started from the **51 multi-frame entries** present at checkpoint 98.

Classification:

1. **typed generalization** — one semantic core applied to related input/output types;
2. **contextual/shorthand form** — same core with an omitted/context-provided value or a lifted/convenience form that should remain explicit in advanced documentation;
3. **genuinely different lexical sense** — one surface label currently hides more than one operation and should be redesigned, split, or made compositional.

For root-level counting, a root is placed in category 2 if any frame is shorthand but none is category 3. A root is placed in category 3 if any frame crosses the semantic-core boundary.

## Result

Across the 51 checkpoint-98 multi-frame roots:

- **33** are category 1 only;
- **15** contain category 2 shorthand/contextual lifting but no genuine lexical split;
- **3** contain category 3 hidden lexical irregularity: **Distance, Sense, Name**.

One purely mechanical overload was removed during the audit: GratefulTo(experiencer, benefactor) and GratefulTo(experiencer, benefactor, :basis basis) are now one frame with an optional named-only :basis role.

After that standardization, the live registry has:

- **205 entries**;
- **258 semantic frames**;
- **50 multi-frame entries**;
- 22 entries with no callable frame;
- 133 with exactly one frame;
- 37 with exactly two frames;
- 13 with three or more frames.

No rune was added or removed.

## Whole-registry classification

| Root | Frames at audit start | Class | Audit result |
| --- | ---: | --- | --- |
| Density | 2 | 1 | Entity density and Distribution-within-Region density are the same density measure over different carriers. |
| AfterValue | 2 | 2 | Explicit Event and event-local forms are the same boundary-value operation; the one-argument form supplies the enclosing Change event. |
| And | 3 | 1 | StateProposition, Proposition, and EventSpec conjunction share one conjunction core. Infix spelling is a reusable structural rule, not a lexical exception. |
| BeforeValue | 2 | 2 | Explicit Event and event-local forms are the same boundary-value operation; the one-argument form supplies the enclosing Change event. |
| Begin | 2 | 1 | State onset and concrete Event begin-point are one initial-boundary core, selected by type. |
| End | 3 | 2 | Final state transition and final Event boundary share one boundary core. End(Event) is output-context-sensitive: TimePoint means final boundary; EventSpec means stop that ongoing event. |
| Equal | 2 | 1 | Generic typed equality and Entity identity are the same equality core; Entity specialization preserves StateProposition typing. |
| Opposite | 2 | 1 | Quantity sign reversal and Direction reversal are the same typed opposite operation. |
| Sequence | 2 | 1 | EventSpec sequence and generic ordered value Sequence share one ordering constructor. Flat event-list spelling is reusable grammar. |
| Some | 2 | 1 | Existential quantification is identical; StateProposition specialization preserves state typing. |
| Trigger | 2 | 1 | Bound and unbound trigger forms are one trigger construction; the binder only introduces a scoped variable. |
| When | 2 | 1 | TimePoint and TimeInterval attachment are one temporal scheduling/attachment operation. |
| Change | 3 | 2 | Exact target and constraint forms are one Change event. Family-member input is a normalized convenience for the corresponding Attribute plus target value. |
| Exist | 2 | 1 | Entity and general SemanticValue existence are one existence state; Entity is the more specific type. |
| Before | 7 | 2 | Concrete Event/TimePoint frames are ordinary temporal precedence. EventSpec/StateProposition forms lift the same ordering relation over matching occurrences or holding states. |
| Distance | 3 | 3 | Physical/metric Distance returns Length, while Property/EventSpec boundary-distance returns contextual EvaluationValue. These use different spaces, arity, result types, and closure rules. |
| During | 6 | 2 | Concrete Event/point containment is the core. EventSpec and Proposition forms lift containment over matching occurrences or proposition-holding through an interval. |
| Evaluate | 2 | 2 | Explicit evaluator and omitted contextual evaluator are the same evaluation operation; the one-argument form supplies evaluator from context. |
| Explains | 2 | 2 | Explanation-object relation is core; Proposition-as-reason is contextual discourse shorthand for a represented explanation. |
| Know | 2 | 1 | Knowing Proposition or Information is one epistemic relation generalized over content type. |
| Member | 2 | 1 | Collection membership and world/group membership are the same membership core over different container representations. |
| More | 2 | 1 | EvaluationValue and other OrderedValue comparisons are one strict ordering relation. |
| Overlap | 4 | 1 | Entity, Region, Event, and TimeInterval overlap are one nontrivial shared-extent/topological core specialized by domain. |
| Permitted | 2 | 1 | Both frames express deontic permission of an EventSpec, with either explicit agent scope or event-level permission plus authority. |
| Simultaneous | 2 | 1 | Concrete Events and TimePoints use the same simultaneity relation. |
| Touch | 2 | 1 | Entity contact and Region boundary contact are one topological contact core; the output state/proposition distinction follows persistence typing. |
| Rate | 3 | 2 | Quantity/time and EventSpec frequency share one per-Time core. EventSpec without interval is contextual interval omission. |
| Requires | 2 | 1 | Proposition and EventSpec outcomes use the same prerequisite relation. |
| Sense | 2 | 3 | Explicit-channel Sense is raw perceptual acquisition, while the two-argument Sign form additionally guarantees semantic interpretation, the former Read meaning. |
| Purpose | 2 | 1 | EventSpec and Proposition goals are one persistent purpose/function relation over different goal content types. |
| Ratio | 2 | 2 | Pair and Collection forms construct the same Ratio; the pair form is a convenience arity rather than a distinct meaning. |
| Name | 2 | 3 | Name(sign,referent,context?) is a nonfunctional naming relation, while Name(sign) -> Entity is contextual inverse reference resolution. |
| First | 2 | 2 | Sequence-first is the core selector. EventSpec form contextually supplies the ordered sequence/domain of matching occurrences and selects its next/first member. |
| SufficientFor | 2 | 1 | Proposition and EventSpec outcomes share one sufficiency relation. |
| Cause | 3 | 1 | Event-to-Event causation and Entity-caused EventSpec/State transition share one causality core; optional :instrument is an ordinary named role. |
| Use | 3 | 1 | The three-argument Process constructs intentional instrument use; Event/EventSpec plus instrument frames expose the same instrument-participant relation on an event. |
| Beneficiary | 2 | 1 | Event and EventSpec beneficiary roles are one thematic relation. |
| Meaning | 2 | 1 | Sign-to-Information and Sign-to-Proposition are one interpretation relation generalized over content type. |
| Say | 3 | 1 | Proposition, Information, and Sign content are one speech/utterance Process generalized over content type. |
| Want | 2 | 1 | Desired EventSpec or Proposition are one desire relation over content type. |
| Expect | 2 | 1 | Expected EventSpec or Proposition are one expectation relation over content type. |
| Extent | 7 | 2 | Region, axis Length, and temporal extent share an extent/size core; unary holistic EvaluationValue and omitted CoordinateFrame forms are contextual projections/shorthands. |
| Length | 2 | 1 | Entity and Path length are one Length measurement over different carriers. |
| Through | 2 | 2 | Path-through-Region is core; EventSpec-through-Region is a lifted event/path convenience. |
| Edge | 2 | 1 | Entity and Region edge extraction are the same boundary-feature operation. |
| Contrast | 2 | 1 | Proposition and EventSpec discourse contrast share one represented-content contrast relation. |
| Question | 2 | 1 | Yes/no and binder-open questions share one QuestionContent construction; binder scope is a reusable grammar mechanism. |
| GratefulTo | 2 -> 1 | 2 | The second frame only added named :basis; standardized to one frame with an optional named-only role. |
| RemorseFor | 2 | 2 | Explicit basis is core; one-argument form contextually omits the basis. Objective use should state it. |
| High | 3 | 1 | EvaluationValue, Quantity, and Ratio all use the same contextual upper-threshold predicate over ordered values. |
| Low | 2 | 1 | EvaluationValue and Quantity use the same contextual lower-threshold predicate. |

## Highest-frame roots

### Before — 7 frames

Before has one temporal-precedence core. Concrete Event/Event and TimePoint/TimePoint forms are direct ordering. EventSpec and StateProposition forms are lifted readings over matching occurrences or times at which a state holds. They remain category 2 because context supplies occurrence/holding interpretation, but they do not change argument order and require no parser special case.

Player consequence: advanced documentation should say that pattern/state forms talk about matching occurrence/holding relative to the supplied temporal reference.

### Extent — 7 frames

Extent is coherent enough to remain one family, but it is the most context-sensitive non-irregular root.

Direct forms cover occupied Region of an Entity, projected Length of Entity/Region in an explicit CoordinateFrame axis, and temporal extent of an Event. Contextual forms cover holistic ordered size EvaluationValue and omitted CoordinateFrame for axis measurement.

The two unary Entity readings are distinguished partly by expected output type rather than input type alone. This is acceptable as advanced typed shorthand, but objective magic should use explicit physical measures/frame where execution depends on geometry.

### During — 6 frames

All forms preserve temporal inclusion/holding: Event within Event, Event within TimeInterval, TimePoint within TimeInterval, matching EventSpec active at/across a temporal reference, and Proposition holding throughout a TimeInterval.

The EventSpec/Proposition frames are semantic lifting, not new word order.

### Overlap — 4 frames

No learner exception was found. Entity, Region, Event, and TimeInterval frames all mean nontrivial shared extent in the relevant topology/domain. Types alone select the frame.

## Category-2 shorthand that deserves advanced documentation

The following roots do not need redesign, but their short forms should not be left as surprises:

- BeforeValue / AfterValue — one-argument form means the enclosing Change event;
- End — concrete Event input can yield its final TimePoint or an EventSpec that stops the ongoing Event, according to expected output type;
- Change — family-value shorthand normalizes to Attribute plus target;
- Before / During — EventSpec/state/proposition forms are temporal lifting;
- Evaluate — omitted evaluator is contextual;
- Explains — Proposition-as-reason is contextual explanation shorthand;
- Rate — omitted interval is contextual;
- Ratio — pair spelling is a convenience for ratio construction;
- First — EventSpec form uses a context-provided occurrence ordering/domain;
- Extent — holistic size and omitted frame are contextual;
- Through — EventSpec form lifts the path relation;
- RemorseFor — omitted basis is contextual.

GratefulTo no longer needs a separate overload for :basis; named-role syntax now handles it directly.

## Category-3 lexical irregularities

### Distance

Current frames combine physical/general metric distance between two values, returning Quantity:Length, with distance from a Property or EventSpec satisfaction boundary, returning EvaluationValue.

The boundary forms are not just omitted arguments to the spatial Length operation. They depend on a different abstract state/evaluation metric.

**Recommendation:** keep current behavior for compatibility at checkpoint 99, but redesign before beginner freeze. Either separate the boundary operation under a distinct lexical root/constructor, or formalize one explicit generic metric-distance abstraction that makes the metric space/boundary an argument instead of hiding it contextually.

### Sense

The explicit channel frame means perceptual acquisition.

The two-argument contextual Sign frame means successful perception **plus semantic interpretation**. That extra interpretation is exactly the distinction the current mind spec otherwise preserves between sensing and Meaning/understanding.

**Recommendation:** redesign. Most likely either restore a distinct compact Read-like construction or make interpreted reading an explicit composition of Sense with Meaning/Understand machinery. Do not teach the interpreted frame as if it were merely a missing channel argument.

### Name

The core naming relation is intentionally nonfunctional: Name(sign, referent, context?).

The one-argument resolver Name(sign) -> Entity runs in the inverse direction and selects one contextual referent even though the relation may have multiple referents.

**Recommendation:** move reference resolution to an explicit reference constructor/selector before final player freeze. New Names currently depend on this lookup behavior, so it should not simply be deleted without replacement.

## Parser-behavior audit

The 51 roots do **not** introduce 51 parser branches.

Reusable surface handlers remain infix And/Or, flat Sequence/Concurrent, and open-question binder placement.

Among audited roots, root-specific semantic normalization is limited to event-local BeforeValue, event-local AfterValue, and Change family-member normalization. These normalize semantics after ordinary typed parsing; they do not create new punctuation or argument-order grammars.

End and Extent contain same-input frames that can rely on expected output type. That is a learner-facing typed-overload issue, not special parser syntax.

Named roles remain general grammar. The audit found no need for a new named-role rule. The redundant GratefulTo basis frame was collapsed specifically so ordinary optional named-role machinery represents it directly.

## Argument-order audit

No category-1 root requires arbitrary frame-specific word order that cannot be explained by its semantic roles.

Some roots change role shape by type:

- Use(agent,instrument,goal) versus Use(event,instrument);
- Permitted(agent,event,:authority ...) versus Permitted(event,:authority ...);
- Cause(event,event) versus Cause(entity,effect,:instrument ...).

These are type-distinguished valence differences, not parser exceptions. They should be shown in dictionary examples where commonly used, but they do not add a grammar rule.

## Player-learning result

The checkpoint-97 structural count still stands:

- **7 universal writing rules**;
- **8 reusable structural constructions** while pipe remains counted;
- **3 canonical surface-special families** inside those constructions.

Checkpoint 99 adds the lexical result:

- **3 genuinely irregular multi-frame lexical cases** still need redesign;
- category-2 contextual shorthand exists, but it is concentrated in a small, documentable set and uses the same typed parser.

Therefore the current best learning-complexity summary is:

> **Cuspell has 7 universal writing rules, 8 reusable structural constructions, and 3 genuinely irregular multi-frame lexical cases.**

If pipe becomes debug-only, the player-facing structural count drops from 8 to 7 without changing the lexical result.

## Checkpoint decision

Do **not** start another global root-reduction sweep.

Next lexical work should be targeted at the three category-3 cases:

1. Sense;
2. Name;
3. Distance.

Sense and Name are higher priority because their current overloads cross explicit semantic boundaries already stated in current specs. Distance needs a deliberate choice between a generic metric abstraction and a split boundary-distance operation.

All other audited multi-frame roots are considered learner-regular enough for now, subject to future evidence.
