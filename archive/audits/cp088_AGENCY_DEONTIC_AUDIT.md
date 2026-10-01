# Agency, Mental Stance, Deontic, and Event-Role Second-Pass Audit

_Status: checkpoint 88 — family-level reduction experiment complete; no net-safe reduction found_

## Scope

This audit tests the next high-leverage family from
`docs/SECOND_PASS_PRIMITIVE_FAMILY_MAP.md`.

Current family:

- `Attempt`
- `Reflexive`
- `Beneficiary`
- `Can`
- `Expect`
- `Intend`
- `Obligated`
- `Permitted`
- `Plan`
- `Purpose`
- `Want`

The family contains **11 semantic primitive candidates**.

The repeated surface shape is strong: several roots relate an Entity or other
SemanticValue to an EventSpec or Proposition. The audit asks whether that repetition
reflects one smaller semantic system or merely similar argument structure.

## Reduction rule

A generic wrapper does not count as a reduction if each old meaning survives as one
new atomic mode value.

For example,

`Stance Self MoveSelfHere IntentionKind`

does not reduce `Intend` if `IntentionKind` is an irreducible atom whose entire
meaning is "intention". Replacing eleven roots with a Stance/Role/Modal constructor
plus eleven kind values grows the semantic alphabet.

The same rule applies to hiding the distinctions in world-model tags, zero-cost
grammar, or Old Names.

## Existing machinery tested

Relevant current mechanisms include:

- `Believe`, `Confidence`, `Evaluate`, `Know`, `Understand`;
- `Happen`, `Cause`, `Prevent`, `Begin`, `End`;
- `Say` and addressed speech composition;
- `Purpose`, `Use`, `Beneficiary`, `ResponsibleFor`;
- `Not`, `And`, quantification, and contextual role marks;
- EventSpec structure such as `Sequence`, `Concurrent`, `When`, and conditions.

Several previous reductions already demonstrate where this machinery is exact:

- `PossibleTo` / `ProbableTo` / `CertainTo` reduce through `Confidence`;
- `Learn` reduces to `Begin Know`, `Begin Can`, or `Begin Understand`;
- `Promise` reduces to addressed `Say` plus `Begin Obligated`;
- `Consent` / `Refuse` reduce to addressed assertion/denial of `Permitted`;
- `DesignedFor` / `MethodFor` reduce to `Purpose`.

The remaining roots must preserve more than those removed conveniences.

## Experiment A — generic mental Stance

Candidate shape:

`Stance(holder,content,mode)`

The obvious candidates are `Want`, `Expect`, `Intend`, and `Plan`.

They are not one relation with interchangeable labels:

- `Want` can target either an EventSpec or Proposition and expresses desire;
- `Expect` can target either an EventSpec or Proposition and expresses anticipated
  occurrence/truth;
- `Intend` targets an EventSpec and expresses an agent's committed intended action;
- `Plan` targets an EventSpec but represents having a plan/course of action, often
  structured.

Pairwise entailments do not hold generally:

- wanting an event does not imply intending to perform it;
- intending an event does not imply expecting it to succeed;
- expecting an event does not imply wanting it;
- planning for an event does not by itself imply that the agent wants every
  consequence encoded in the plan;
- an intention can exist without a developed plan;
- a contingency plan can exist without asserting that its trigger will occur.

A generic Stance root therefore still needs independent desire, expectation,
intention, and planning distinctions.

**Result: no reduction.**

## Experiment B — Plan into Intend

This is the closest-looking pair because both currently relate an Entity to an
EventSpec.

The distinction is semantic rather than merely lexical:

- `Intend(agent,E)` states an intention toward E;
- `Plan(agent,E)` states that E is the represented/planned course of action.

A plan may be conditional or contingency-oriented and can encode structure beyond
the bare intended result. Conversely, an agent can intend a simple action without
having a plan for how to accomplish it.

Replacing Plan with Intend would therefore strengthen some plans into intentions and
erase the difference between goal commitment and represented course structure.

Requiring `Sequence` under Plan does not fix the issue: not every plan is a flat
Sequence, and an intended Sequence is still not equivalent to having a plan.

**Result: retain both.**

## Experiment C — Want into Intend or Evaluate

`Want` is broader than intention because it also targets Propositions and does not
require agentive commitment or action.

`Evaluate` supplies an ordered appraisal value, but positive evaluation is not
desire. A mind may evaluate an outcome positively without wanting it, and may want
an outcome despite evaluating aspects of it negatively.

**Result: retain Want.**

## Experiment D — Expect into Believe / Confidence

Expectation overlaps epistemic belief but is not identical to it.

A mind can:

- believe that an event is possible without expecting it;
- expect an event while assigning less than certainty to its occurrence;
- believe a standing proposition that has no expectation/future-event reading.

`Confidence` measures degree assigned to a Proposition. It does not by itself say
that the proposition/event is what the mind expects, and the current language has no
single objective confidence threshold that exactly defines Expect across contexts.

This is why Possible/Probable/Certain could be reduced through explicit confidence
threshold/endpoints while Expect cannot.

**Result: retain Expect.**

## Experiment E — Can into Permitted or Confidence

`Can(agent,E)` is capability.

`Permitted(agent,E,...)` is authorization.

The two are independent:

- an agent may be capable of an action but forbidden to perform it;
- an agent may be permitted to perform an action but physically unable to do it.

Epistemic possibility also does not replace capability. Earlier `PossibleTo`
reduced to positive Confidence because it concerned epistemic possibility, while
`Can` is deliberately the persistent skill/capability state used by `Begin Can`
for learning-to-do.

**Result: retain Can and Permitted separately.**

## Experiment F — Permitted and Obligated as deontic duals

A classical deontic system can sometimes define permission using obligation over the
negated action, but the current Cuspell semantics do not license that collapse.

Reasons:

1. EventSpec negation is not the same object as propositional `Not`; Cuspell does
   not currently have a general "not-do-E" EventSpec constructor that would make
   `Obligated(agent, not-E)` exact.
2. Permission and obligation carry potentially different authority/context roles.
3. A world/institution may represent explicit permission independently of absence of
   prohibition or obligation.
4. `Permitted(E :authority A)` is also used as the semantic content of consent,
   whereas `Obligated` represents a persistent duty/commitment state.

Defining one as the logical dual of the other would add normative-system assumptions
that are not currently part of the language.

**Result: retain both.**

## Experiment G — Purpose into Intend / Plan

`Purpose(subject,goal)` applies to any SemanticValue, not only a mind/agent.

It covers:

- artifact design/function;
- method goal;
- persistent intended function/goal of a process or semantic object.

A hammer's Purpose can exist without the hammer intending anything. Likewise a
Method can have a Purpose without being an agent.

Therefore Purpose cannot reduce to Intend or Plan. Conversely, an agent's current
intention or plan does not establish a persistent artifact/function Purpose.

**Result: retain Purpose.**

## Experiment H — Beneficiary into Purpose / Give / Transfer / Have

This was already tested in the first exact-reduction audit and still fails.

`Beneficiary(event,entity)` states who benefits from an Event or EventSpec.

Benefit may be:

- unintended;
- indirect;
- unaccompanied by receipt;
- unaccompanied by possession;
- different from the event's explicit Purpose.

Thus neither recipient/Transfer, possession/Have, nor intended Purpose is
equivalent.

**Result: retain Beneficiary.**

## Experiment I — Attempt into Intend + event occurrence

`Attempt(agent,goal)` is an actual goal-directed effort EventSpec.

It differs from intention:

- an agent can intend without making an attempt;
- an attempt can fail, so it cannot be replaced by the goal EventSpec;
- `Happen goal` would assert success rather than effort;
- `Cause goal` would assert successful causation;
- `Intend + Happen some generic action` still lacks the relation saying that the
  action is an effort toward the embedded goal.

This is already encoded by D-073 and remains exact after the second-pass audit.

**Result: retain Attempt.**

## Experiment J — Reflexive into Not Intend / Cause

This was also tested previously and remains distinct.

`Reflexive(E)` states involuntary/reflex realization.

`Not Intend` is too broad: accidents, coercion, habitual action, and unknown
intention can all be non-intended without being reflexes.

`Cause` addresses causal dependence, not the control/volition mode of execution.

A generic control-mode system could revisit this later, but one
`ReflexiveMode` value would merely rename the current primitive.

**Result: retain Reflexive.**

## Shared-axis count test

A plausible generalized system might introduce axes such as:

- epistemic stance;
- motivational stance;
- commitment;
- capability;
- deontic force;
- control/volition;
- event participant role;
- persistent function.

However, exact reconstruction still requires root-specific distinctions:

- desire;
- expectation;
- intention;
- planning;
- capability;
- permission;
- obligation;
- reflex execution;
- actual attempting;
- beneficiary role;
- purpose/function.

That is already eleven distinctions before adding the generic operators that would
host them.

The apparent commonality is therefore mostly typing/argument structure, not duplicate
semantic atoms.

**Result: generic Stance/Modal/Role architecture would not currently lower the rune
count.**

## Count result

No root is removed and no new stance/deontic wrapper is added.

Current inventory remains:

- **208 registered base entries**;
- **128 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The agency/mental-stance/deontic/event-role family remains **11 semantic primitive
candidates**.

## Design conclusion

The family contains several strong reusable roots, but they occupy genuinely
different semantic axes.

The successful earlier reductions are informative: Confidence removed epistemic
possibility conveniences, Purpose removed design/method aliases, Obligated absorbed
commitment, Permitted absorbed consent/refusal content, and Can supports typed skill
acquisition. Those reductions have already stripped away much of the easy overlap.

The remaining eleven roots should stay until independently motivated machinery can
remove more than it adds.

The next second-pass family should be **space, topology, and geometry**, where exact
boundary/contact relations may admit a smaller topological basis.
