# Second-Pass Primitive Family Map

_Status: active second-pass analysis after foundational ontology/classification audit checkpoint 93_

## Purpose

The first root-minimization pass ended at **210 entries** with **130 semantic primitive candidates**. Second-pass checkpoint 84 consolidates `ChangeRate` and `OccurrenceRate` into one typed `Rate` root, checkpoint 86 folds Duration into Extent, and checkpoint 89 removes Inside/Outside through typed topology composition, so the current inventory is **206 entries** with **126 semantic primitive candidates**, **0 derived candidates**, and **0 unresolved candidates**.

The unresolved bucket being empty does **not** mean the 126 surviving candidates are frozen. It means only that each one currently lacks an exact smaller replacement when considered in isolation.

The second pass therefore changes the question:

> Instead of asking whether one root can be written with the current roots, ask whether several surviving roots are evidence for one missing reusable abstraction.

This document maps all 126 current semantic primitive candidates into primary families, identifies repeated semantic axes, and ranks the families by expected reduction leverage. Checkpoint 84 records the first language change produced by this second-pass analysis.

## Success rule for a second-pass generalization

A proposed abstraction counts as a reduction only if it satisfies all of the following:

1. preserves the exact truth conditions and participant roles of the roots it replaces;
2. preserves typing and command/execution closure;
3. reduces total semantic complexity rather than merely renaming it;
4. does not hide one irreducible old root behind one new closed-domain value with the same meaning;
5. keeps the previously translated book corpora expressible;
6. does not preserve a root merely because a draft Old Name currently uses it.

A design such as `Manner(event, JumpManner)` is **not automatically a reduction** if `JumpManner` is itself an irreducible semantic atom equivalent to the old Jump root. The same warning applies to generic `Attribute(..., MassKind)`, `Attitude(..., LoveKind)`, or similar enum-shaped rewrites.

## Complete primary-family partition

Every one of the 126 semantic primitive candidates appears exactly once below. Cross-family dependencies are discussed later.

### 1. Foundational ontology and classification — 14

`Group`, `Matter`, `Path`, `Region`, `Rule`, `Sign`, `Thing`, `Unit`, `Exist`, `Female`, `Life`, `Magic`, `Whole`, `Member`

These are mostly ontology anchors, membership/classification relations, or foundations used by other families.

**Reduction outlook:** low to medium. These are dangerous targets for aggressive compression because many other analyses depend on their type distinctions. The best opportunity is likely moving some world-specific classifiers out of the core if later world-ontology work proves they are not language-level primitives.

### 2. Measurement, physical descriptors, and fields — 21

`Damage`, `Density`, `DistributionOf`, `Form`, `Heat`, `Hunger`, `Light`, `Loudness`, `Mass`, `Phase`, `TextureOf`, `Volume`, `Area`, `CamouflagedAgainst`, `Rate`, `Distance`, `Extent`, `Length`, `TotalAmount`, `Hard`, `Sharp`

This is the largest clearly structural technical family. Many entries expose a subject and return a typed scalar, profile, region, or descriptor-like value.

Repeated shapes include:

- Entity -> typed Quantity;
- Entity -> ordered EvaluationValue;
- Entity -> profile value;
- Region/Distribution -> aggregate or local measurement;
- contextual threshold properties over an underlying ordered measure.

**Candidate abstraction:** a more explicit typed descriptor/measurement layer, possibly separating:
- the property/attribute descriptor;
- its value domain/dimension;
- the measurement/access operation;
- contextual thresholding.

**Main risk:** false compression. Replacing `Mass(x)` with `Measure(x, Mass)` does not help if `Mass` remains an irreducible semantic token with all of the old root's meaning. This family only reduces if several current roots can be generated from a smaller reusable dimensional/descriptor system.

### 3. Space, topology, and geometry — 14

`At`, `Center`, `Edge`, `In`, `Joined`, `Offset`, `Overlap`, `Part`, `ShapeLike`, `Sides`, `Surface`, `Through`, `Touch`, `Toward`

This family mixes:
- topological containment/contact/overlap predicates;
- occupied-location state;
- boundary/contact relations;
- region selectors;
- direction/location constructors;
- path-through-region relations.

**Candidate abstraction:** a small exact topological basis plus reusable selectors/derived predicates.

**Checkpoint 89 result:** the earlier warning remains correct—Inside is not plain In and Outside is not Not In—but typed Region support on Touch and Overlap now preserves the missing boundary distinctions compositionally. See `docs/SPACE_TOPOLOGY_AUDIT.md`.

### 4. Time and event occurrence — 4

`Before`, `During`, `Happen`, `Simultaneous`

These are already a compact foundation after Past/Future/Present/Always/Ongoing/Completed and related conveniences were removed.

**Reduction outlook:** low. This family is more useful as dependency infrastructure for other reductions than as a likely source of large savings.

### 5. Motion and action manner — 12

`Attack`, `Bite`, `Climb`, `Dodge`, `Eat`, `Fall`, `Jump`, `Limp`, `Move`, `Stab`, `Use`, `Worship`

This is the clearest repeated signal from the final unresolved audit.

Seven entries were retained for essentially the same structural reason: the language has no general way to express an event's **manner/mode of realization** without replacing the missing distinction with another equally primitive label.

The strongest evidence is:

- `Bite` — oral action manner;
- `Climb` — supported/contact locomotion manner;
- `Dodge` — evasive threat-avoidance manner/goal;
- `Fall` — non-agentive gravity/context-governed motion manner;
- `Jump` — launch/airborne locomotion manner;
- `Limp` — asymmetric/impaired gait manner;
- `Stab` — directed puncturing/thrust manner.

`Attack`, `Eat`, `Use`, and `Worship` are useful boundary cases because they combine manner with goal, social interpretation, participant roles, or conventional activity type.

**Candidate abstraction:** an event-manner/action-schema system that can state reusable features such as:
- locomotion vs contact action;
- agency/control mode;
- body-part or instrument role;
- support/contact profile;
- trajectory profile;
- goal/evasion orientation;
- puncture/bite/ingest-style physical interaction.

**Main test:** whether this can define several roots from a genuinely smaller feature basis rather than introducing `JumpManner`, `LimpManner`, `StabManner`, etc. as disguised replacements.

### 6. Change, causation, transfer, and control — 5

`Change`, `Cause`, `Give`, `Transfer`, `Control`

These are broad event-structure mechanisms already reused by many deleted roots.

**Reduction outlook:** low as deletion targets, high as supporting machinery. They are more likely to help reduce other families than to disappear themselves.

### 7. Agency, goals, deontics, and event roles — 11

`Attempt`, `Reflexive`, `Beneficiary`, `Can`, `Expect`, `Intend`, `Obligated`, `Permitted`, `Plan`, `Purpose`, `Want`

Repeated axes include:
- actual effort vs mental stance;
- intention vs desire vs expectation;
- ability vs permission vs obligation;
- event participant role;
- voluntary vs reflex execution;
- persistent goal/function.

**Candidate abstraction:** a typed event-stance/agency layer with orthogonal features for:
- holder/agent;
- target EventSpec;
- modal force;
- control/volition;
- social authority;
- commitment;
- intended function.

**Main risk:** these distinctions have different truth conditions. A single generic `Stance(kind,...)` with one irreducible kind value per old root would only move the inventory, not reduce it.

### 8. Communication, information, epistemics, and discourse — 15

`Assert`, `Infer`, `Say`, `Sense`, `About`, `AnswerFor`, `Believe`, `Confidence`, `Contrast`, `EvidenceFor`, `Explains`, `Know`, `Meaning`, `Remember`, `Understand`

This family contains several distinct but interacting layers:
- information/sign interpretation;
- speech acts;
- perception;
- propositional attitudes;
- evidence/inference;
- discourse coherence.

**Candidate abstraction:** carefully factor shared roles such as source, content, mind, proposition, Sign, evidence, and discourse relation while preserving factivity and directionality.

**Known hard boundaries:** `Meaning`, `About`, and `Contrast` already survived exact-reduction review. `Know`, `Believe`, `Remember`, and `Understand` also differ in factivity and mental-state content. This is likely a later family, not the first experimental target.

### 9. Social, affective, and institutional relations — 26

`Forgive`, `Angry`, `Happy`, `Sad`, `Admire`, `CompassionFor`, `EngagedTo`, `Evaluate`, `Fear`, `FriendOf`, `GratefulTo`, `GrieveFor`, `Hate`, `Have`, `JealousOf`, `Like`, `Love`, `Own`, `ParentOf`, `RemorseFor`, `Reputation`, `Respect`, `ResponsibleFor`, `ShameAbout`, `SpouseOf`, `Trust`

This is numerically the largest family. It contains at least three subfamilies:

- **affective attitudes/states:** Like, Love, Hate, Fear, Admire, Respect, Trust, JealousOf, CompassionFor, GratefulTo, GrieveFor, RemorseFor, ShameAbout, Angry, Happy, Sad;
- **social/institutional relations:** FriendOf, EngagedTo, ParentOf, SpouseOf, Own, Have, ResponsibleFor;
- **social evaluation/repair:** Evaluate, Reputation, Forgive.

**Candidate abstraction:** a general attitude/relationship framework may reduce repeated experiencer-target structure; institutional relations may instead belong partly to world ontology.

**Main risk:** this family is extremely vulnerable to enum-shaped fake reduction. `Attitude(Self,This,Love)` is not simpler if Love remains an irreducible atom. A valid reduction would need a smaller semantic basis that actually predicts multiple current relations.

### 10. Operational and body states — 4

`Awake`, `Sleep`, `Open`, `Locked`

These are compact persistent state predicates with strong world-model dependence.

**Candidate abstraction:** state families with explicit state dimensions or mutually constrained values.

**Reduction outlook:** small but potentially clean. The key question is whether the values are genuinely generated from a reusable state dimension or merely renamed as `AwakeState`, `SleepState`, etc.

## Cross-family dependency map

The primary partition above is for audit organization, not a claim that the families are independent.

The most important cross-family dependencies are:

- **motion/action manner -> agency + geometry + contact + physical descriptors**  
  Climb, Dodge, Fall, Jump, Limp, Bite, and Stab depend on combinations of trajectory, contact, support, volition, body/instrument role, and physical interaction.

- **agency/deontic -> information/social**  
  Expect, Intend, Plan, Want, Permitted, and Obligated all target semantic/event content but differ by mental, social, and normative force.

- **epistemic/discourse -> Sign/Information foundations**  
  Meaning, About, AnswerFor, EvidenceFor, Explains, Believe, Know, Infer, Remember, and Understand depend on the existing semantic-content type system.

- **social/affective -> evaluation + event history + institutional world rules**  
  Gratitude, remorse, shame, forgiveness, responsibility, ownership, engagement, and marriage depend on causes, events, social context, and sometimes world-defined institutions.

- **measurement -> change + world ontology**  
  Rate, Density, Damage, Hunger, Reputation, Loudness, Hard, Sharp, and camouflage all rely on an underlying measure/classifier supplied partly by the world model.

- **space/topology -> motion/action**  
  Move, Climb, Dodge, Through, Touch, Joined, Surface, and Offset share geometry that may become reusable if the spatial basis is made more explicit.

## Ranked second-pass opportunities

This ranking is based on repeated evidence of a missing abstraction, likely reuse across multiple roots, and risk of merely hiding the same semantics elsewhere.

### Priority 1 — motion/action manner

**Why first:** the final unresolved audit repeatedly reached the same conclusion independently for Bite, Climb, Dodge, Fall, Jump, Limp, and Stab.

This is the strongest evidence that the current root set may be missing a real reusable abstraction rather than seven unrelated atoms.

**First experiment:** try to define a minimal event-manner feature basis and see whether at least **three** of those seven roots become exact compositions while the new basis uses fewer irreducible distinctions than it removes.

If the experiment requires one unique primitive manner value for each old root, reject it.

### Priority 2 — measurement/descriptor architecture

**Why second:** 21 roots remain in this family after Rate consolidation and folding temporal Duration into Extent. Their typed-access patterns are still strongly regular, and prior successful reductions already came from generalizing Extent, Rate, Density, Unit, High/Low, and axis selection.

**First experiment:** separate descriptor identity, value domain/dimension, access, and contextual thresholding, then test Mass/Heat/Light/Volume/Damage/Hunger/Loudness as representative cases.

### Priority 3 — social/affective structure

**Why third:** 26 roots give large theoretical leverage, and the cross-genre books prove the family is genuinely needed.

**First experiment:** test whether a smaller combination of valence, target/basis, social orientation, and persistence can reconstruct several attitudes exactly. Do not accept a one-value-per-old-root attitude enum.

### Priority 4 — agency/mental stance/deontic structure

This family may eventually connect with both epistemic attitudes and event manner/control. The likely reusable axes are volition, ability, desire, expectation, intention, obligation, permission, and commitment.

It should be tested after manner because Reflexive and Dodge may reveal what the control/volition layer actually needs.

### Priority 5 — space/topology

A formal topological basis could potentially unify several relations and selectors, but boundary semantics are subtle and the existing spatial core is already fairly compressed.

### Priority 6 — communication/epistemic/discourse

High semantic importance, but several members have already survived direct exact-reduction review. This family should be revisited only after more general content/stance machinery exists.

### Priority 7 — operational state dimensions

Small possible savings. Useful as a clean test of the general "state dimension" idea, but not a major inventory reduction by itself.

### Priority 8 — foundational ontology, time/event occurrence, and broad change/causation

These are currently more valuable as support machinery than as likely reduction targets.

## Second-pass checkpoint 84 — repeated-label audit finds a real Rate abstraction

A focused audit of multiword English glosses found that most repeated pieces such as `Of`, `For`, and `To` are translation/preposition artifacts rather than shared Cuspell semantics. They do not justify generic roots.

`ChangeRate` and `OccurrenceRate` are different: both apply the same semantic operation, measurement per Time, and their input types distinguish the cases exactly.

They are replaced by one root:

- `Rate(value: Quantity, interval: TimeInterval)` -> Quantity<value-dimension/Time>;
- `Rate(event: EventSpec, interval: TimeInterval)` -> Quantity<Frequency>;
- `Rate(event: EventSpec)` -> contextual Quantity<Frequency>.

No new enum or hidden one-value-per-old-root distinction is introduced. This is therefore a genuine **2 roots -> 1 root** reduction.

Registered base inventory **210 -> 209**. Semantic primitive candidates **130 -> 129**.

## Second-pass checkpoint 85 — motion/action manner does not yet reduce

The full family experiment is recorded in `docs/MOTION_ACTION_MANNER_AUDIT.md`.

The attempted shared feature basis does **not** produce a net reduction yet. The existing general machinery handles surrounding facts—Move, Touch, Through, Use, Attack, Damage, Attempt, Prevent, Reflexive, Cause—but each target still needs a distinct missing semantic component:

- Bite -> oral/teeth-closing interaction;
- Climb -> supported surface traversal;
- Dodge -> evasive realization relative to a threat;
- Fall -> gravity/world-force-driven uncontrolled motion;
- Jump -> self-launch plus unsupported/airborne phase;
- Limp -> asymmetric/impaired gait;
- Stab -> directed puncturing/thrust interaction.

A generic `Manner` constructor plus one atomic manner value per old root would make the inventory larger. Factoring apparent overlaps such as Jump/Fall airborne motion or Bite/Stab penetration also requires additional root-specific distinctions and still loses the count test.

No roots are removed. Registered inventory remains **209** and semantic primitive candidates remain **129**.

## Second-pass checkpoint 86 — Duration folds into Extent

The full family audit is recorded in `docs/MEASUREMENT_DESCRIPTOR_AUDIT.md`.

One exact reduction is available:

- `Duration(Event)` -> `Extent(Event)` where a Time Quantity is expected.

This extends the already-general Extent family from spatial/holistic extent to the type-distinct temporal extent of a concrete Event. No new selector, enum, or descriptor-kind value is introduced.

The other measurement candidates remain distinct for now. In particular, Mass/Heat/Light/Volume/Length carry AttributeDescriptor identity; Area/Volume are not derivable from one axis for arbitrary shapes; Density still has Distribution-field semantics; Damage/Hunger/Loudness are independent scales; Hard/Sharp lack reusable underlying scalar descriptors; and Form/TextureOf remain different profile types.

Registered inventory **209 -> 208**. Semantic primitive candidates **129 -> 128**.

## Second-pass checkpoint 87 — social/affective structure does not yet reduce

The full family audit is recorded in `docs/SOCIAL_AFFECTIVE_AUDIT.md`.

The 26 social/affective roots share substantial argument structure, but the audit does not find a smaller exact semantic basis:

- a generic `Attitude(...,kind)` or `SocialRelation(...,kind)` needs one atomic kind per old root and grows the inventory;
- Like/Love/Hate/Admire/Respect/Trust are not equivalent to evaluator-relative `Evaluate`;
- Happy/Sad are not exact opposite thresholds on one scalar valence axis, and Love/Hate are not exact Opposite pairs;
- Trust is not one proposition-level Expect/Confidence state;
- Fear, jealousy, compassion, gratitude, grief, remorse, and shame each preserve different appraisal/target/basis semantics;
- FriendOf/ParentOf/SpouseOf/EngagedTo/Have/Own/ResponsibleFor remain different social or institutional relations;
- Reputation is not currently a simple aggregate of individual Evaluate values;
- Forgive remains distinct from ending anger/hate or denying responsibility.

No roots are removed. Registered inventory remains **208** and semantic primitive candidates remain **128**.

## Second-pass checkpoint 88 — agency/deontic structure does not yet reduce

The full family audit is recorded in `docs/AGENCY_DEONTIC_AUDIT.md`.

The 11 roots share typed holder/content/event-role shapes but not duplicate truth conditions:

- Want, Expect, Intend, and Plan are different motivational/epistemic/commitment states;
- Plan cannot collapse into Intend because represented course structure and intention are not equivalent;
- Can is capability, while Permitted is authorization;
- Permitted and Obligated are not currently licensed as logical deontic duals;
- Purpose applies to artifacts/methods/non-agents and therefore cannot reduce to Intend/Plan;
- Beneficiary is an event role independent of Purpose, transfer, receipt, or possession;
- Attempt is an actual effort EventSpec, not a mental stance;
- Reflexive is an execution/control mode, not merely Not Intend.

A generic Stance/Modal/Role wrapper would still require the same eleven irreducible mode values and would therefore increase the semantic inventory.

No roots are removed. Registered inventory remains **208** and semantic primitive candidates remain **128**.

## Second-pass checkpoint 89 — strict containment reduces to topology

The full family audit is recorded in `docs/SPACE_TOPOLOGY_AUDIT.md`.

Typed Region frames on the existing topological roots close the gap that forced Inside/Outside to survive the first pass:

- `Touch(Region,Region)` = boundary contact;
- `Overlap(Region,Region)` = nontrivial shared interior extent.

Therefore:

- strict inside -> `And {In A R,Not Touch Extent A R}`;
- outside -> `Not Overlap Extent A R`.

This preserves the exact distinction from plain In / Not In: partial overlap still fails Outside, while boundary-only contact still counts as outside; boundary-inclusive In is narrowed to strict inside by explicitly excluding boundary contact.

Inside and Outside are removed. The remaining 14 spatial roots retain distinct anchor, structural, geometry-selection, path, profile, contact/overlap, or direction semantics.

Registered inventory **208 -> 206**. Semantic primitive candidates **128 -> 126**.

## Second-pass checkpoint 90 — communication/epistemic/discourse does not yet reduce

The full family audit is recorded in `docs/EPISTEMIC_DISCOURSE_AUDIT.md`.

The 15 roots interact heavily but occupy different semantic layers:

- Say is general utterance while Assert adds assertion force;
- Sense is a perceptual event while Meaning is sign interpretation;
- About is topicality, EvidenceFor is epistemic support, and Explains is explanatory relation;
- Infer is an actual reasoning EventSpec rather than a static support or belief relation;
- Believe is a persistent belief state, Confidence is an ordered degree, and Know remains factive rather than "true belief";
- Remember is memory/retention and Understand is comprehension;
- AnswerFor supplies typed answerhood for QuestionContent;
- Contrast is discourse tension/concession rather than And or an explicit mind's Expect state.

The strongest apparent reduction, Believe -> High Confidence, is rejected for now. Current Believe is a persistent StateProposition selecting the mind-model's belief state, while High Confidence is a contextual Quantity threshold Proposition also used for probability-standard language. Making them identical would either collapse distinct contextual thresholds or require a new belief-threshold atom.

No roots are removed. Registered inventory remains **206** and semantic primitive candidates remain **126**.

## Second-pass checkpoint 91 — time/event occurrence is already a compact basis

The full family audit is recorded in `docs/TIME_EVENT_AUDIT.md`.

No exact net reduction is available:

- `Before` is the primitive strict temporal ordering relation; expressing Event Before through End/Begin still requires TimePoint Before;
- `During` supplies temporal containment/holding and EventSpec activity across a point/interval, not mere overlap or occurrence;
- `Happen` is the existential EventSpec-to-concrete-occurrence bridge, distinct from an occurrence being active throughout a target;
- `Simultaneous` is stronger than Overlap. Its TimePoint frame can individually be written as Equal, but the Event frame retains timing/tolerance semantics not reconstructible from Equal Begin, exact coextensive boundaries, or overlap without new temporal-tolerance machinery.

No roots are removed. Registered inventory remains **206** and semantic primitive candidates remain **126**.

## Second-pass checkpoint 92 — operational/body states remain distinct

The full family audit is recorded in `docs/OPERATIONAL_STATE_AUDIT.md`.

No exact net reduction is available:

- Awake and Sleep are not logical complements; non-awake includes coma, anesthesia, unconsciousness, and other possible states that are not sleep;
- Open and Locked are different physical axes; closed can be unlocked, and not locked does not imply open;
- one consciousness-state or accessibility-state descriptor would still need one atomic value per old distinction and would add a wrapper rather than reduce the alphabet;
- Can, Control, and Permitted describe capability, control, and authorization, not the Locked state.

The useful shared abstraction already exists in `Begin` / `End`, which supplies waking, sleeping, opening, closing, locking, and unlocking transitions without separate transition roots.

No roots are removed. Registered inventory remains **206** and semantic primitive candidates remain **126**.

## Second-pass checkpoint 93 — foundational ontology/classification remains distinct

The full family audit is recorded in `docs/FOUNDATIONAL_ONTOLOGY_AUDIT.md`.

No exact net reduction is available:

- semantic type names are implementation/typing machinery rather than free language-level substitutes for Thing/Path/Region/Sign/Unit;
- Group is not a semantic Collection, and Member is not Part/In/Have;
- Path and Region retain ordered-trajectory versus spatial-subset semantics;
- Sign is not reducible to a current Meaning relation, and Rule remains narrower than generic Information;
- Matter and Unit retain independent foundational classification content;
- Exist, Life, Magic, and Whole are independent state predicates;
- Female cannot simply be moved to one atomic world classifier without preserving the same semantic atom and changing its current Property behavior if retyped as a Kind.

No roots are removed. Registered inventory remains **206** and semantic primitive candidates remain **126**.

## Recommended next concrete experiment

Move to **change, causation, transfer, and control**: `Change`, `Cause`, `Give`, `Transfer`, and `Control`.

The strongest question is whether `Give` is an exact specialization of `Transfer` or whether it additionally fixes entity transfer/possession semantics that generic resource/value Transfer does not. Also test whether `Control` can be reconstructed from capability/prevention/state machinery without losing the actual controller-target relation, and whether any typed-overload sharing between Change/Cause/Transfer is a genuine common operation rather than a wrapper around distinct atoms.

`Cause` and `Change` are already broad supporting mechanisms, so removal should be accepted only if their full event/state semantics survive without introducing an equivalent new operator.

## Checkpoint

The second-pass family map covers **all 126 semantic primitive candidates**.

Checkpoint 84 reduced ChangeRate + OccurrenceRate to Rate. Checkpoint 85 retained motion/action manner. Checkpoint 86 removed Duration through temporal Extent. Checkpoint 87 retained social/affective structure. Checkpoint 88 retained agency/deontics. Checkpoint 89 removed Inside/Outside through typed Region topology. Checkpoint 90 retained communication/information/epistemic/discourse. Checkpoint 91 retained time/event occurrence. Checkpoint 92 retained Awake, Sleep, Open, and Locked. Checkpoint 93 retains the fourteen foundational ontology/classification roots after exact family-level testing.
