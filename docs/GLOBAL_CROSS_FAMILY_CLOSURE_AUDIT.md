# Global Cross-Family Closure Audit

_Status: checkpoint 95 — global second-pass closure complete; no further exact reduction found_

## Purpose

Checkpoint 94 finished the family-by-family second pass with **205 registered base
entries** and **125 semantic primitive candidates**.

This pass asks a different question:

> Do any of the 125 survivors become exactly reducible only when machinery from
> different semantic families is combined?

The audit therefore tests the strongest cross-family bridges created by the
reduction work rather than repeating the ten family audits independently.

The reusable bridge mechanisms now available include:

- `Begin` / `End` over persistent Properties and Relations;
- agentive `Cause`, including optional instrument;
- generic `Transfer`;
- generalized `Rate`;
- spatial/temporal `Extent`;
- typed Region `Touch` and `Overlap`;
- `High` / `Low` threshold Properties;
- `MinBy` / `MaxBy`;
- collection/binder logic;
- exact arithmetic and dimensional normalization;
- contextual `Evaluate`;
- world-backed Kind and state classifiers.

A reduction is accepted only if the old meaning is fully generated from surviving
semantics. Moving the same distinction into a world classifier, enum value,
descriptor-kind token, hidden tolerance rule, or parser special case does not count.

## Cross-family candidates tested

### 1. Density from Mass / Volume / TotalAmount

For a homogeneous physical entity,

`Divide Mass X Volume X`

has the Density dimension and often computes ordinary physical density.

That is not sufficient to remove `Density`.

The current root also provides:

`Density(distribution, region)`

for local field/resource density. `DistributionOf` can represent general resource
dimensions, and `TotalAmount` is an aggregate whose output dimension depends on the
resource/world model. The language still lacks a general region-measure/integration
scheme that turns every registered Distribution density into an exact
`TotalAmount / Volume` expression with the existing type guarantees.

**Result: retain Density.**

### 2. Hard / Sharp from High + Evaluate or generic measurement

`High` now supplies a reusable contextual threshold operator, and `Evaluate`
supplies a general ordered evaluation.

Neither provides the missing physical descriptor identity:

- hardness is resistance to indentation/deformation;
- sharpness is edge/point concentration.

`High Evaluate X` is a generic/contextual evaluation, not either physical property.
Introducing Hardness/Sharpness descriptor values would only relocate the two atoms.

**Result: retain Hard and Sharp.**

### 3. CamouflagedAgainst from Form / TextureOf / Sense / Distance

The language now exposes geometry, texture, sensing, and contextual boundary
distance.

Camouflage nevertheless requires observer/background-relative perceptual similarity
or detectability. There is no registered appearance metric that makes:

`CamouflagedAgainst(subject, background, observer?)`

equivalent to a fixed combination of Form, TextureOf, Sense, or Distance.

Adding a camouflage-specific metric/profile value would preserve the old primitive
under another name.

**Result: retain CamouflagedAgainst.**

### 4. At from In + Extent/topology

`In(X,R)` constrains the spatial extent of X to a Region. `At(X,L)` states that
X's declared anchor position coincides with a Location.

An extended Entity can be At a Location without its full extent being contained in
a zero-sized region at that point. Region topology therefore does not reconstruct
anchor-position semantics.

**Result: retain At.**

### 5. Toward from Offset / Move / Opposite

`Toward(reference)` produces a Direction from a reference relation. `Offset`
consumes an already resolved Direction plus an origin and distance; `Move` consumes
a goal/path; `Opposite` can reverse a Direction only after one exists.

None generates the original direction from the reference alone.

**Result: retain Toward.**

### 6. ShapeLike from Form + Equal

`Form(subject)` returns a GeometryProfile, but `ShapeLike(subject, Kind)` compares
against a Kind/template under registered resemblance semantics.

Exact `Equal Form A Form B` is stronger and also requires an Entity/template value,
not merely a Kind. A new tolerance/resemblance atom would be the same missing
distinction.

**Result: retain ShapeLike.**

### 7. Use from Cause + :instrument

This is a particularly strong cross-family near miss.

`Cause agent effect :instrument I`

states successful causation of the effect with I as instrument.

`Use agent I goal` states intentional employment of I toward a goal EventSpec.
Use does **not** require that the goal succeeds.

Replacing Use with Cause would therefore strengthen ordinary use into successful
causation. The two-argument Use frames also remain participant-role propositions over
Event/EventSpec + instrument.

**Result: retain Use.**

### 8. Attack from Attempt / Cause / Damage

Attack can fail to cause Damage. `Cause ... Change Damage ...` is therefore too
strong.

`Attempt agent goal` supplies effort toward an explicit EventSpec goal, but the
current core has no smaller "harm/hostile attack realization" predicate that turns
Attempt into Attack without reintroducing the same action distinction.

**Result: retain Attack.**

### 9. Dodge from Attempt + Prevent + Move

`Prevent threat interval` suppresses the threatening event itself. A dodge may
succeed while the threat still occurs but misses the agent.

`Attempt` adds effort but not evasive realization, while `Move` adds displacement
without threat-relative evasion.

**Result: retain Dodge.**

### 10. ResponsibleFor from Cause / Obligated

Responsibility can be grounded causally, legally, institutionally, or morally.

`Cause A E` is too narrow for non-causal responsibility. `Obligated A E` is a
duty state rather than attribution for an outcome. Combining the two still does not
cover every current ResponsibleFor truth condition.

**Result: retain ResponsibleFor.**

### 11. Reputation from Evaluate + Group/Member + aggregation

The collection system can obtain members of a Group and `Evaluate` can produce
ordered evaluations.

The core still has no registered community aggregation semantics that makes
Reputation definitionally an average, majority, maximum, or other fixed statistic of
individual Evaluate values. Different world/social models can define standing
differently.

A new ReputationAggregation rule would simply move the missing semantic distinction.

**Result: retain Reputation.**

### 12. Trust from Confidence / Believe / Know

Confidence and Believe target Propositions. Trust is a persistent interpersonal
reliance relation between Entities.

Turning Trust into "high confidence in some proposition about the trusted entity"
requires choosing that proposition/reliance criterion, which the current root does
not leave as a hidden free variable.

**Result: retain Trust.**

### 13. Assert from Say + Proposition content

`Say` is a general utterance Process and can carry Proposition content.

`Assert` additionally marks assertion force: the speaker presents the proposition
as asserted, without making it objectively true and without requiring belief.

A bare Proposition-valued Say does not carry that force in the current semantics.

**Result: retain Assert.**

### 14. AnswerFor from About / EvidenceFor / Question

An answer can be about the same topic without answering the question, and evidence
for a proposition is not necessarily an answer to a QuestionContent value.

The Question constructor creates QuestionContent but does not itself provide the
answerhood relation.

**Result: retain AnswerFor.**

### 15. Simultaneous from Equal / Begin / End / Overlap

The TimePoint frame alone can be represented by `Equal`.

The Event frame still uses relevant event timing under a declared temporal
tolerance/profile:

- equal starts can allow different durations;
- equal start + end is stronger than relevant simultaneity;
- Overlap is weaker.

No general tolerance relation introduced elsewhere in the second pass closes this
gap.

**Result: retain Simultaneous.**

### 16. Whole from Damage + Form / Part

`Whole` is profile-relative structural integrity. Low Damage does not guarantee all
required Parts/relations exist, and complete Form similarity does not necessarily
encode required internal structure.

A registered structural profile may use Part, Joined, Form, and Damage as evidence,
but those inputs do not definitionally replace the Whole predicate.

**Result: retain Whole.**

### 17. Foundational/social classifiers through world ontology

Several remaining roots have exact membership supplied partly or wholly by world
ontology: Female, ParentOf, SpouseOf, EngagedTo, Own, Group, Matter, Rule, Sign, Unit,
and similar classifications/relations.

Moving any one of them into a single world-model classifier with the same meaning is
not a reduction. The semantic distinction remains atomic; only its storage location
changes.

**Result: no classifier relocation is counted as root reduction.**

## Global dependency conclusion

The cross-family graph exposes three broad kinds of near-reduction:

1. **one frame is derivable but another frame keeps the root**  
   Examples: simple Entity Density versus Distribution Density; TimePoint
   Simultaneous versus Event Simultaneous.

2. **the composition is stronger or weaker than the root**  
   Examples: Cause-with-instrument versus Use; Prevent versus Dodge; Equal Form
   versus ShapeLike.

3. **the composition still needs one missing semantic selector/metric/classifier**  
   Examples: camouflage metric, reputation aggregation, attack/harm realization,
   Hardness/Sharpness descriptors.

None produces a net smaller semantic alphabet.

## Closure result

No root is removed at checkpoint 95.

Current inventory remains:

- **205 registered base entries**;
- **125 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The important conclusion is stronger than "nothing obvious was found":

> Every remaining candidate has now survived both its local family audit and a
> global cross-family composition pass against the reusable machinery produced by
> the minimization work.

This does **not** freeze the inventory permanently. A future genuinely new reusable
abstraction, world-ontology basis, or corpus pressure can reopen a candidate. But
with the current semantic architecture, the reduction pass has reached a practical
closure.

## Next step

Do **not** start another blind deletion sweep immediately.

The next useful phase is a stabilization/regression phase:

1. run the translated-book/cross-genre corpus again against the 205/125 inventory;
2. check all provisional Old Names whose spellings changed during minimization;
3. audit the 125 surviving roots against the canonical rune visual constraints;
4. only reopen semantic reduction when one of those checks exposes a concrete
   redundancy, gap, or awkward distinction.
