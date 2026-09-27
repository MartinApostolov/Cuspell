# Discourse, Narrative, Modality, and Questions

_Status: working specification v0.1_

This specification is the first major result of the prose-corpus test. It extends Cuspell beyond isolated propositions and magical commands into connected ordinary discourse.

## 1. Kind predication

A Kind can be used predicatively of an Entity.

Abstract rule:

InstanceOf(entity, Kind) -> Proposition.

Compact surface shorthand permits a Kind as the head of an Entity argument:

Cat|Self

normalizes to:

InstanceOf(Self, Cat).

This is distinct from Property + Kind restriction such as RedMatter.

Binder domains also imply Kind membership.

[a:Human]

means the binder ranges over Entities satisfying InstanceOf(a, Human).

## 2. Utterance context

Every ordinary utterance/discourse segment has a typed UtteranceContext containing at least:

- speaker;
- addressee set;
- utterance time;
- utterance location;
- discourse reference time;
- discourse referents/salience state;
- relevant Language/context.

Contextual References are interpreted against this structure.

Self = current utterance speaker.

You = current addressed participant when unique or explicitly selected.

Here = current utterance/casting location rule.

Now = current utterance/evaluation TimePoint.

For magical Commands, the casting context is a stricter form of UtteranceContext.

## 3. Nested speech contexts

Quoted/direct speech creates a nested UtteranceContext.

When Sally says a sentence:

- Self inside the quoted content resolves to Sally;
- You resolves to the quoted addressee;
- Here/Now resolve to the quoted utterance context unless explicitly preserved from an outer context.

This prevents a quoted "I" from accidentally referring to the narrator/outer speaker.

Say/Tell can take semantic speech-act content as well as quoted Sign content.

## 4. Quotation versus reported content

Distinguish:

- quotation: preserves the Sign/wording;
- reported content: preserves semantic content without requiring exact wording.

A quotation is Information about Signs.

Reported speech embeds a Proposition, Question, Command-content, or other Information structure.

This matters for translation because a novel often gives exact dialogue while ordinary paraphrase may not.

## 5. Discourse referents

Ordinary discourse can introduce persistent discourse referents that survive sentence boundaries.

A referent record contains:

- Entity/value identity when resolved;
- semantic type;
- descriptive predicates;
- Name relations;
- salience;
- number/group information.

Pronouns and definite descriptions can resolve to these discourse referents.

This is a discourse mechanism, not a magical search capability.

## 6. Anaphora

An anaphoric Reference means roughly:

resolve to the sufficiently salient compatible discourse referent required by the grammatical features/context.

If zero or multiple equally compatible antecedents remain, the ordinary expression is ambiguous.

For magical execution, an anaphoric target is accepted only when its antecedent has already resolved uniquely and is frozen into the Command context.

Magic never chooses an antecedent from narrative salience at execution time.

## 7. Proper names

Name remains a many-to-many Relation between Sign and referent under a naming context.

Ordinary discourse may use a proper-name Reference as shorthand for:

select the salient/accessibly named referent under the current naming context.

If more than one candidate remains, the Reference is ambiguous unless additional description/selection resolves it.

This is not a globally unique ID system.

## 8. Definite descriptions

Ordinary discourse needs constructions corresponding to "the X."

A Definite description selects the uniquely salient/resolvable member satisfying a description in the current discourse domain.

It is contextual.

For magical language, the same semantic request must normalize to explicit Unique(collection/filter) or another deterministic selector.

Thus conversational convenience does not weaken magical targeting rules.

## 9. Narrative reference time

Connected narrative maintains a DiscourseReferenceTime distinct from utterance Now.

A clause can update or inherit that reference time.

This lets a paragraph describe past events without spelling a full absolute interval in every sentence.

The normalized semantics still records explicit temporal relations.

Magical Commands do not receive an implicit narrative reference time unless a control structure explicitly supplies one.

## 10. Tense operators

Cuspell may lexicalize compact temporal operators:

Past(X): the relevant time of X precedes the reference/utterance time.

Present(X): X holds/occurs overlapping the reference/utterance time.

Future(X): X follows the reference/utterance time.

These are meaning-bearing temporal operators/morphemes, not zero-mana punctuation.

When used in magic, they therefore cost as semantic material unless a more explicit time expression is written instead.

## 11. Aspect

Working ordinary-language aspect operators:

### Ongoing

Ongoing(EventSpec, reference-time) -> Proposition

At least one matching Event is active across the reference TimePoint/interval.

### Completed

Completed(EventSpec, reference-time) -> Proposition

A matching Event ended before the reference time within the supplied discourse scope.

### Continue

Continue(EventRef or uniquely resolved ongoing EventSpec) -> EventSpec

The current Event continues rather than ending at the present boundary.

### Habitual

Habitual(EventSpec/predicate, interval/context) -> Proposition

The pattern recurs with contextually normal frequency across the interval.

Habitual is contextual ordinary-language semantics unless a frequency rule/threshold is supplied.

### Whenever

Whenever(condition-pattern, consequence-pattern, interval/context) -> Proposition

For matching condition episodes in the relevant discourse domain, the consequence relation/pattern holds.

For magical control, Trigger/Repeat remains the precise executable mechanism.

## 12. Generic statements

Natural-language generics such as "cats are cute" are not equivalent to strict All.

Introduce:

Generic(Kind/domain, predicate, context) -> Proposition.

Generic means the predicate is presented as characteristic/normal for the domain under the discourse/world knowledge standard.

Generic is intentionally contextual and ordinarily non-magical.

Objective magic should instead use:

- All;
- Most;
- an explicit ratio/frequency;
- a registered Kind classifier/default.

This preserves natural prose without smuggling vague generalizations into spell conditions.

## 13. Most

Add exact quantifier:

Most(domain, predicate) -> Proposition

for a finite/resolved domain where strictly more than half of the members satisfy the predicate.

Other proportional quantifiers can be expressed with Count/Ratio/comparison.

"Almost all" remains contextual unless a threshold is given.

## 14. Free-choice any

Ordinary "any/anywhere/anyone" often combines universal quantification with modality.

Its normalized form should expose that structure.

Example meaning:

"I can sleep anywhere"

can normalize conceptually to:

for every relevant Place p in the contextual domain, Can(Self, SleepAt(p)).

A compact Any semantic molecule may exist for ordinary language, but magical use must expose/bound the domain.

## 15. Subjective evaluation

Evaluation must identify an evaluator/experiencer when the judgment is not objective.

Introduce a family around:

Evaluate(evaluator, target/situation, dimension/context) -> EvaluationValue.

Useful conventional Relations/Properties can normalize against that structure:

- GoodFor(target, evaluator);
- BadFor(target, evaluator);
- ImportantTo(target/proposition, evaluator);
- Like(evaluator, target);
- Prefer(evaluator, A, B).

Good/Bad without an evaluator remain contextual ordinary-language shortcuts.

This lets the language distinguish:

"fish tastes good to me"

from:

"fish satisfies some externally defined quality standard."

## 16. Sensory evaluation

Perceptual Processes return Information/experience structures.

Evaluation can target that result.

Thus "delicious to X" can be represented as a positive evaluation of a Taste experience by X.

A conventional DeliciousTo(food, experiencer) Relation may lexicalize that common structure.

## 17. Modality

### Can

Can(entity, EventSpec/type) means the entity has capability/permission-as-defined to realize the event under the supplied context.

Capability and permission should be split if the world/social model needs both.

### Intend

Intend(agent, EventSpec/goal) -> state-predicate Proposition.

The agent currently has the event/goal as an intention.

### Plan

Plan(agent, structured EventSpec/Sequence) -> state/Information relation.

A Plan can contain ordered intended actions.

### Obligated

Obligated(entity, EventSpec/state, authority/context) -> state-predicate Proposition.

This represents social/deontic responsibility.

### Permitted

Permitted(entity, EventSpec, authority/context) -> Proposition.

### Should

Should is a weaker/contextual normative recommendation and is best treated as ordinary-language modality derived from evaluation/obligation standards rather than a core magical predicate.

These distinctions prevent Want, Can, Intend, and obligation from collapsing into one verb.

## 18. Open questions

Yes/no questions remain:

? Proposition .

Open questions use one or more typed interrogative binders.

Temporary abstract syntax:

?[x:Type] Proposition($x).

The Question asks for values of x that satisfy the open Proposition under the intended information source/addressee.

Example structure for "Where are you going?":

?[g:Location] Intend(You, Move(You,$g)).

This is an ordinary semantic paraphrase; the source may instead ask about an already ongoing movement goal.

Question itself still does not perform magical Find/Reveal.

For embedded/narrated speech, executable constructors are:

- `Question(Proposition) -> QuestionContent`
- `Question(Binder, Proposition) -> QuestionContent`
- `Directive(EventSpec) -> CommandContent`
- `Ask(speaker, QuestionContent, addressee?) -> EventSpec`
- `Tell(speaker, Information, addressee) -> EventSpec`

`Almost(EventSpec) -> contextual Proposition` covers near occurrence of an event without asserting that the event occurred.

## 19. Answers

An Answer to an open Question supplies bindings for the interrogative variables plus optional explanatory Information.

A yes/no Answer supplies truth commitment/content.

Answer correctness/truth remains separate from merely responding.

## 20. Ongoing-event cessation

Add:

Stop(target-event-pattern/ref) -> EventSpec.

If given an EventRef, Stop ends that ongoing Event at the earliest valid boundary.

If given an EventSpec pattern, the pattern must resolve to the intended ongoing Event or explicit Collection of Events.

Stop does not mean "prevent every future event of this type."

For ongoing speech, a command equivalent to Stop(Speaking(You)) can represent "shut up."

## 21. Prevention

Add distinct:

Prevent(EventSpec pattern, interval/scope) -> state/control EventSpec.

Meaning:

establish/maintain that no matching Event occurs during the interval/scope.

For magic, Prevent is persistence-like and requires explicit scope/duration and Power.

This distinguishes stopping something already happening from preventing future occurrence.

## 22. Concurrency

Add:

Concurrent({EventSpecs...}) -> CompositeEventSpec.

It requires all component Events and adds temporal-overlap constraints rather than only unordered conjunction.

This differs from:

- And: all occur, no required order/overlap;
- Sequence: ordered occurrence;
- Concurrent: occurrence with overlap.

"Yawn while stretching" can therefore normalize to Concurrent or to explicit During constraints after Event binding.

## 23. Discourse versus magical strictness

Ordinary discourse may use:

- anaphora;
- generics;
- Habitual;
- contextual evaluation;
- discourse reference time;
- proper-name shorthand;
- definite descriptions.

Before any such expression participates in magical execution, it must normalize to a closed objective structure or be rejected as non-executable.

This maintains one broad language while keeping magic deterministic.

## 24. Corpus consequence

The first prose pass demonstrates that the spell grammar was not yet a complete discourse grammar.

The additions above are language-level features rather than exceptions for one book.

They should be stress-tested against later chapters and then represented in the reference AST/parser.
