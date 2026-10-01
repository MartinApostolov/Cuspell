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

For registered Cuspell runes in formal syntax, the parser supplies the unique formal interpretation required by the lexicon.

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

`False(P)` can normalize to Not(True(P)) or equivalent.

Normally an assertion directly asserts P; users do not need to wrap every sentence in True.

True/False are useful for talking about propositions as Information.

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

Sense does not automatically mean the perception is perfectly interpreted.

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

Detecting a Sign is not the same as understanding its Meaning.

For example:

- vision can detect written marks;
- Read combines Sign perception with Language/Meaning interpretation.

This distinction matters for unknown runes and foreign languages.

## 16. Read

`Read(reader, sign, language/context?) -> EventSpec :result Information`

Read requires:

- successful perception of the Sign;
- access to the relevant Language mapping;
- successful semantic interpretation.

Unknown vocabulary can therefore block full reading without blocking visual detection.

## 17. Say

`Say(speaker, content, recipient?, medium?) -> EventSpec`

produces Sign(s) intended to convey content.

Say is medium-general.

## 18. Speak

Speak is Say specialized to an audible linguistic Sign medium.

A compact Speak rune may be derived/conventional.

## 19. Write

Write is Say/recording specialized to producing a persistent visual/tactile Sign.

It creates a Sign Entity/Record as a result.

The written Sign can later be Read.

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
- inserting a false Memory -> Create Information + Begin(Remember), subject to magical capability.

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

`Some i:Information And {Know mind $i, AnswerFor $i question}`

`QuestionContent` and `CommandContent` are Information values. Embedding them in `Say` does not activate top-level question or command mood. A separate `Ask` root is unnecessary: addressed questioning is `Say` with `QuestionContent`.

## 28. Magical information acquisition

Magic needs explicit Processes for obtaining otherwise unavailable Information.

Strong candidate:

`Find/Reveal(scope, predicate/attribute) -> EventSpec :result Information/Collection`

Such a Process can be subject to:

- range;
- occlusion;
- protection;
- RequiredPower;
- allowed search domain.

This is the correct layer for detection/divination-like magic.

References themselves are not omniscient search engines.

## 29. Find

Recommended distinction:

- `Collect` constructs a semantic collection from already resolvable domain membership/predicate evaluation;
- `Find` actively acquires Information/references that the caster/command context did not already possess.

Find is therefore an executable information Process, not just set notation.

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
