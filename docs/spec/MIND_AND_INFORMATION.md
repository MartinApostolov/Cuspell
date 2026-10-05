# Mind, Perception, and Information

_Status: working specification v0.1_

This specification formalizes Information, Signs, Meaning, language, mental states, perception, memory, questions, and information-acquisition processes.

## 1. Information versus Sign

**Information** is abstract content and is represented directly by the semantic type `Information`; there is no duplicate `Information` Kind root in the minimized core.

A **Sign** is a representation/token capable of carrying Information.

Examples of Signs can include:

- written marks;
- sounds;
- gestures;
- rune inscriptions;
- records.

The same Information can be carried by many different Signs.

## 2. Meaning

`Meaning(sign, information, context/language?) -> Proposition`

relates a Sign to the Information it conveys under a Language/context.

General Meaning is not globally functional because ordinary Signs can be ambiguous, polysemous, or context-sensitive.

`Meaning` survives the root-minimization audit as a primitive semantic relation: Sign interpretation cannot be replaced by topicality, equality, evidence, Purpose, or structural Part without losing those semantics.

For registered Cuspell runes in formal syntax, the parser supplies the unique formal interpretation required by the lexicon.

## 2a. Information topicality

`About(information, topic) -> Proposition`

expresses the subject matter/topic of Information. It is deliberately distinct from `Meaning`: a Sign can mean Information, while that Information can independently be about some Entity, Event, Proposition, or other semantic topic.

`About` therefore also survives the current exact-reduction audit.

## 2b. Objective sensory representation

Checkpoint 132 adds `Represent(carrier, content, channel)` as a persistent StateProposition.

`Represent` states that one Entity presents or depicts semantic content through a named SenseChannel.

It is deliberately distinct from:

- `Meaning` — what a Sign means under a semantic/language context;
- `Sense` — one observer's perceptual EventSpec;
- `ShapeLike` / `Form` — the carrier's actual geometry;
- truth — represented content need not be real.

Multiple observers may independently Sense the same carrier under normal channel/access physics. This makes representation shared by default rather than copying one forced Sense event per observer.

A visual image is an ordinary example of a carrier with a Vision representation. A magical illusion can use a fresh non-Matter Sign/Entity with Magic + Represent states. Tactile solidity, sound, smell, and other channels are separate Represent states and do not arise automatically.

Exact rendered detail must be deterministic enough for the active media/world model. If the written content and carrier Kind do not determine a realizable presentation, magical execution fails rather than inventing aesthetically plausible details.

## 3. Word

`Word` is a Kind of Sign that functions as a lexical unit in a Language.

A Cuspell rune/root is therefore both:

- a physical/written Sign when inscribed;
- a registered lexical semantic item in the Cuspell Language.

The Sign itself and its semantic value remain conceptually distinct.

## 4. Language

A Language is a structured system relating Signs/syntax to Information/semantic structures.

Cuspell is one Language whose magical subset is additionally recognized by the execution engine.

Ordinary human languages may be represented without becoming magical.

## 5. Quotation / mention

The language needs to distinguish using an expression from referring to the expression itself.

Add zero-mana quotation/grouping syntax in transliteration.

Conceptually:

`Quote[expression]`

produces Information/Sign-content describing the written expression rather than evaluating/executing it.

The quotation marks are syntax, but the semantic runes inside remain written content and still count normally if quotation occurs inside a magical Command.

Quoted command text does not execute merely because it is mentioned.

## 6. Proposition and truth

A Proposition is truth-bearing semantic content.

`True(P)`

means Proposition P corresponds to the relevant world state/model.

There is no standalone False root; falsehood of P is represented with `Not P` (or `Not True P` when explicitly talking about the truth-status predicate).

Normally an assertion directly asserts P; users do not need to wrap every sentence in True.

`True` remains available when the truth-status predicate itself is the topic; ordinary negative assertions normally use `Not`.

## 7. Knowledge

Define:

`Know(mind, proposition/information) -> Proposition[state-predicate]`

Knowledge requires:

1. the Mind cognitively represents the content;
2. the relevant propositional content is true under the language's knowledge model.

A false represented belief is not Know.

This lets:

`Begin(Know(A,P))`

represent coming to know P, if the magical system supports direct knowledge change.

## 8. Belief

`Believe(mind, proposition) -> Proposition[state-predicate]`

requires cognitive acceptance/representation but does not require P to be true.

Thus Know and Believe are not synonyms.

Successful deception no longer needs a separate `Deceive` Process. For deceiver D, target T, and content P:

`If (Not P) (Cause D (Believe T P))`

states both required conditions: P is false and D successfully causes T's belief state. The method—speech, omission, appearance, forged Sign, and so on—can be represented separately when relevant.

## 9. Think

`Think(mind, content) -> EventSpec`

is a mental Process involving active thought about Information/Proposition.

Think is event-like; Know/Believe are persistent state Relations.

## 10. Want

`Want(mind, desired-content) -> Proposition[state-predicate]`

The desired content can be:

- a State/Proposition;
- an EventSpec;
- possession/relationship;
- other typed goal representation.

Want does not automatically cause the desired Event.

## 11. Feel

The English word "feel" is too broad to be one magical semantic root without typed frames.

Possible distinct concepts include:

- perceive via a Sense channel;
- experience emotion;
- experience internal bodily sensation;
- hold an evaluative state.

Recommendation:

retain Feel for ordinary language as a family/umbrella, but magical semantics should use specific typed perception/emotion roots.

## 12. Sense

There is no separate `Detected` root in the minimized core. Channel-specific detection is `Happen Sense experiencer channel stimulus`; channel-unspecified detection existentially quantifies a SenseChannel.

Sense is an information-acquisition Process.

Working frame:

`Sense(experiencer: Mind, channel, stimulus/scope) -> EventSpec :result Information`

A successful Sense Event produces/updates perceptual Information available to the experiencer.

Sense does not automatically mean the perception is interpreted or understood.

Checkpoint 100 removed the former hidden interpreted-Sign overload. Checkpoint 101 keeps that correction but supersedes the temporary `Interpret` root: semantic interpretation is built from the actual `Meaning` relation plus the interpreter's `Understand` state, while `Sense` remains strictly sensory.

For a known candidate content `I`, successful comprehension of the mapping requires both:

- `Meaning S I` — the Sign actually has that meaning in the applicable context;
- `Understand A (Meaning S I)` — A comprehends that Sign-to-content mapping.

If the content itself must be obtained rather than stated, use typed inverse selection, for example:

`Unique Collect i:Information Meaning S $i`

This does not make `Meaning` globally functional. `Unique` succeeds only when the stated constraints leave exactly one value.

## 13. SenseChannel

A SenseChannel declares:

- stimulus domain;
- required interaction;
- medium if relevant;
- information produced.

This generalizes the earlier `perceptible + Sense` rule.

Examples:

### Vision

Light-based channel; requires appropriate optical relation.

### Hearing

Sound-based channel.

### Touch

contact/force interaction channel.

### Smell

material/chemical airborne interaction channel.

### Taste

material/chemical contact channel.

Registered compounds such as LightSense and SoundSense can lexicalize common channels.

## 14. Channel-specific sensing

The minimized core does not keep separate See/Hear/Smell/Taste roots.

Write the general Process with an explicit channel:

- `Sense(experiencer, Vision, stimulus)`;
- `Sense(experiencer, Hearing, stimulus)`;
- `Sense(experiencer, Olfaction, stimulus)`;
- `Sense(experiencer, Gustation, stimulus)`.

This keeps the sensory distinction while using one productive Process.

## 15. Sign perception versus understanding

Detecting a Sign, knowing its actual Meaning, and understanding that mapping are separate facts.

For example:

- `Sense(reader, Vision, sign)` can detect written marks without interpreting them;
- `Meaning(sign, information)` states the objective/contextual Sign-to-content relation;
- `Understand(reader, Meaning(sign, information))` states comprehension of that mapping.

This distinction matters for unknown runes and foreign languages. A reader may successfully Sense a Sign while lacking the relevant mapping entirely, or may understand a proposed content while that content is not in fact the Sign's Meaning.

## 16. Reading

There is no separate `Read` or `Interpret` root in the minimized core.

Reading separates the sensory event from the semantic conditions that make it a successful reading.

For a familiar mapping, the core pieces are:

- the Sign actually has content I: `Meaning S I`;
- the reader understands that mapping: `Understand A (Meaning S I)`;
- the reader senses the Sign through the relevant channel: `Sense A channel S`.

One executable EventSpec shape is a `Sense` event conditioned on the real mapping being understood:

`If (Meaning S I And Understand A (Meaning S I)) (Sense A channel S)`

For an unfamiliar mapping, successful decoding genuinely changes mental state. That case uses the distinct `Begin Understand` transition rather than pretending an already-known reading and new learning are the same event.

If the conveyed content is not already named in the sentence, typed `Collect` + `Unique` can select it when the contextual Meaning relation has exactly one matching value.

## 17. Say

`Say(speaker, content, recipient?, medium?) -> EventSpec`

produces Sign(s) intended to convey content.

Say is medium-general.

## 18. Speak

Speak is Say specialized to an audible linguistic Sign medium.

A compact Speak rune may be derived/conventional.

## 19. Writing

There is no separate `Write` root in the minimized core.

For a Sign token S:

`Cause writer Begin Exist S`

means the writer causes that Sign's existence state to begin. Because `Begin Exist` starts a persistent state, the Sign remains extant until separately ended. Visual/tactile medium details can be represented separately where needed.

The written Sign can later be sensed through `Sense`; its semantic mapping is represented with `Meaning`, and comprehension of that mapping with `Understand`.

## 20. Record

A Record is a persistent Sign/Information-bearing Entity.

A Record's physical identity and its Information content are separate.

Two records can contain Equal Information while being distinct Entities.

## 21. Memory

Per lexical resolution:

`Memory` is a Kind of Information associated with retained mental encoding.

A Memory can contain:

- represented event/content;
- source association;
- temporal metadata;
- confidence/interpretive metadata if the mind model includes it.

It need not be objectively true; remembered content can be inaccurate.

## 22. Remember

`Remember(mind, memory/content) -> Proposition[state-predicate]`

means the information is retained/retrievable under the mind model.

`Forget` may lexicalize:

`End(Remember(...))`

## 23. Memory manipulation

Editing Information content and changing Remember relations are distinct.

Examples:

- removing access to a Memory -> End(Remember).
- altering stored Memory content -> Change/Information manipulation.
- inserting fabricated/false remembered content -> provide/construct the relevant Information through world-supported means, then `Begin Remember` for that content, subject to magical capability.

The language does not collapse these into one vague "memory spell."

## 24. Name

Per lexical resolution:

`Name(sign, referent, naming-context?)`

is a Relation.

A Name is a Sign participating in that relation.

Names are not globally unique and do not replace Entity identity.

A Name in another Language is Information/reference data, not automatically a Cuspell semantic rune.

## 25. Number as Information

A Quantity value and a numeral Sign are different.

A `Number` can be modeled as a Sign/Information representation of a Quantity.

Useful relation/function:

`NumericValue(number-sign, language) -> Quantity`

This prevents written digits from being confused with the abstract number they denote.

## 26. Question

Question mood `?` turns a Proposition/open-value query into a Question speech act/Information structure.

A Question does not automatically retrieve truth from reality.

Someone/something must have an information source capable of answering it.

This prevents ordinary grammar from becoming free divination.

## 27. Answer

An Answer is Information that satisfies the response requirements of a Question under the Language/context.

Truthful Answer and merely supplied response are distinguishable if needed.

Executable embedded forms:

- `Question(Proposition) -> QuestionContent`
- `Question(Binder, Proposition) -> QuestionContent`
- `Directive(EventSpec) -> CommandContent`
- `AnswerFor(Information, QuestionContent) -> Proposition`
- `Know(mind, Information) -> state-predicate Proposition`

Knowing an answer is compositional rather than a separate root:

`Some i:Information (Know mind $i And AnswerFor $i question)`

`QuestionContent` and `CommandContent` are Information values. Embedding them in `Say` does not activate top-level question or command mood. A separate `Ask` root is unnecessary: addressed questioning is `Say` with `QuestionContent`.

## 28. Magical information acquisition

Magic needs an explicit Process for obtaining otherwise unavailable truthful Information.

Checkpoint 131 adds:

`Find`

with two surface frames:

`Find mind scope proposition`

`Find mind scope answer-binder proposition`

Both return an EventSpec.

Examples:

`Find Self This Magic This!`

means: determine whether the explicitly designated subject is magical and make Self know the truthful yes/no answer.

`Find Self This l:Location At This $l!`

means: determine the complete satisfying Location binding(s) for the explicitly designated subject and make Self know that answer.

A region search states the bounding relation in the query itself:

`Find Self ThisRegion x:Entity In $x ThisRegion And Magic $x!`

The `scope` is an explicit information-access boundary. It is not a hidden relation or target selector. The query must explicitly mention/relate to that same scope, and an open query must explicitly use its answer binder.

At execution time, every otherwise unavailable fact needed to answer the query must be licensed by the stated scope and world capability. Range, occlusion, wards, mind protection, temporal access, information volume, RequiredPower, and setting metaphysics may therefore make a well-formed Find fail.

A successful yes/no Find makes the mind know the true polarity of the proposition. A successful open Find makes the mind know the complete satisfying binding set within the permitted scope. A complete empty result is legitimate Information and is distinct from inability to access/evaluate the query.

Failure or blocked access must never be reported as “false” or “no matches.”

References themselves remain non-omniscient.

## 29. Find is distinct from existing epistemic machinery

Keep these operations separate:

- `Question` constructs/asks a query but does not obtain its answer from reality;
- `Sense` acquires sensory Information through an explicit SenseChannel;
- `Collect` constructs a collection only from membership/predicates already resolvable under its current access rules;
- `Infer` derives a conclusion from supplied evidence and is not automatically factive;
- `Know` describes a factive epistemic state;
- `Begin Know mind P` can request acquisition of the already-written true content P, but it cannot discover an unknown binding or return the false branch of a yes/no test;
- `AnswerFor` relates Information to a QuestionContent but does not source that Information.

`Find` is therefore the distinct executable operation that grants bounded access to an otherwise unavailable truthful answer.

Conditional magic does not reduce Find either. `If P E` can evaluate P only when the information needed for P is already available to the execution context. Using an unavailable hidden P as the condition therefore presupposes exactly the access capability Find supplies.

Find does not automatically export an answer binder into later EventSpecs. Its semantic result is acquired knowledge. If later spell programming needs result-driven branching/export, that is a separate control/data-flow question rather than hidden global-variable behavior.

## 30. Rule

A Rule is a Kind of Information expressing a conditional/normative/general relation.

Formal rules can contain Propositions and variable binders.

A Rule does not execute simply by being stated.

A magical Trigger/Command can use rule-like content through explicit control semantics.

## 31. Command as Information versus active Command

Distinguish:

- **Command-content** — Information encoding a directive/EventSpec;
- **active magical Command** — sentence-mood structure submitted to the execution engine.

A written Record can contain command-content without executing it.

Activation/command mood is separate.

This allows spellbooks to exist safely as Information.

## 32. Copy

Per lexical resolution, primitive Copy initially applies to Information/Sign content.

`Copy(source Information/Record) -> EventSpec :result Information/Record`

The result is a distinct token/record with Equal copied content as specified.

Physical Entity copying remains a different problem.

## 33. Say and teaching

Addressed information transfer uses Say with a recipient rather than a separate Tell root.

Teaching is stronger than saying, but it does not need a separate root. Successful teaching is represented as agentive causation of the appropriate learner-state transition:

- fact/Information: `Cause teacher Begin Know learner content`;
- skill/EventSpec: `Cause teacher Begin Can learner event`;
- other semantic comprehension: `Cause teacher Begin Understand learner content`.

This preserves the distinction that merely telling someone something does not guarantee acquisition.

## 34. Learning

There is no separate `Learn` root in the minimized core. Learning is the transition into the state actually acquired:

- `Begin Know` for factive knowledge/Information;
- `Begin Can` for capability/skill;
- `Begin Understand` for other semantic comprehension.

## 35. Can

`Can(entity, EventSpec/type) -> StateProposition`

means the entity has the capability to realize the specified Process under the model's conditions.

Can is not the same as the Event actually happening.

## 36. Information equality

Information can be compared by content equality.

This differs from Entity `Equal` identity of the Sign/Record carrying it.

A copied book can contain Equal Information while the two physical books are not Entity-Equal.


## Visibility

"Invisible" should not be an unexplained unary Property.

Introduce an objective visual-access relation or derive it from the optical world model.

Working relation:

`VisibleTo(target, observer, conditions?) -> Proposition[state-predicate]`

It is true when the observer can receive sufficient visual Information about the target through the registered Vision channel under the supplied environmental/optical conditions.

A magical invisibility effect can therefore maintain:

`Not(VisibleTo(target, observer,...))`

for an explicitly quantified observer set, or alter the underlying optical interactions that determine visibility.

This keeps invisibility observer/condition-sensitive and avoids treating it as a mystical Boolean label with no perception semantics.

## 37. Result

Mind/information semantics now distinguish:

- content from representation;
- perception from interpretation;
- belief from knowledge;
- memory content from remembering;
- questions from information acquisition;
- command text from command activation;
- names from identity.

This closes several routes by which ordinary language ambiguity could otherwise leak into magic.
