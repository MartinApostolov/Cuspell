# Cross-Genre Corpus Pass — Pride and Prejudice + Frankenstein (1818)

_Status: 2026-09-29 anti-overfitting corpus pass after the Yona full-published audit_

## Purpose

Yona is a strong stress corpus for combat, explicit magic, progression systems, objective state change, technical explanation, and action-heavy dialogue.

That creates a risk: Cuspell might be structurally adequate while still being unusually shaped around Yona's genres.

This pass deliberately uses two public-domain novels with very different pressure profiles:

1. **Jane Austen, _Pride and Prejudice_** — Project Gutenberg #1342, 61 chapters.
   - Source: https://www.gutenberg.org/ebooks/1342
2. **Mary Wollstonecraft Shelley, _Frankenstein; Or, The Modern Prometheus_ (1818 edition)** — Project Gutenberg #41445.
   - Source: https://www.gutenberg.org/ebooks/41445

The goal is not to create Austen- or Shelley-specific vocabulary packages. Proper names and historically specific institutions are treated as corpus/world data. Only genuinely reusable general-language pressure may alter core Cuspell.

## Overall result

**No G17/new grammar or semantic-type gap was found in either novel.**

Both books heavily stress meanings that are rare in Yona:

- social inference and reputation;
- courtship, proposals, consent, refusal and promises;
- affection, friendship, family and marriage;
- politeness, gratitude, apology, forgiveness and resentment;
- nested belief, deception, misunderstanding and belief revision;
- responsibility, guilt, remorse and moral judgment;
- teaching, learning, language acquisition and memory;
- nested letters, testimony and stories-within-stories;
- long causal chains and indirect consequences;
- creation, identity, body/part relations and hypothetical descendants.

The existing G1–G16 architecture can preserve these meanings compositionally.

The important failure was instead **lexical balance**:

> core Cuspell had strong formal/magical/action vocabulary but an unusually thin executable social, emotional and ordinary-cognitive layer.

That weakness is visible in both novels independently, so it is not an Austen-specific patch.

This pass therefore adds **33 general core entries** without changing grammar.

## Pride and Prejudice — full-novel findings

### Chapters 1–12 — PASS / SOCIAL LEXICON / DISCOURSE

Pressure includes:

- gossip and second-hand reports;
- expectations about unknown people's intentions;
- attraction/liking inferred from behaviour;
- visits, invitations and social obligation;
- illness, care, family concern and embarrassment;
- evaluation of manners and character;
- strategic politeness and indirect criticism.

Existing Say/Tell, Believe, Infer, EvidenceFor/Against, Expect, Want, Prefer, Should, Obligated, Cause and contextual discourse mechanisms are structurally sufficient.

The weak point is ordinary vocabulary for affection, friendship, respect, trust and emotional state.

### Chapters 13–23 — PASS / SOCIAL ACTS

Mr. Collins' arrival, courtship and proposal material strongly stresses:

- kinship;
- inheritance/property institutions;
- proposals;
- explicit refusal;
- mistaken belief that refusal is insincere;
- parental/social pressure;
- another person's later consent/acceptance;
- marriage engagement as a persistent social relation.

No new grammar is needed.

The corpus does, however, justify general semantic molecules for:

- Consent;
- Refuse;
- EngagedTo;
- SpouseOf;
- ParentOf/SiblingOf;
- Own.

Regency inheritance/entail law itself remains world/institution data rather than a Cuspell primitive.

### Chapters 24–36 — PASS / EPISTEMIC + SOCIAL EVALUATION

Pressure includes:

- self-deception;
- reputation and rank;
- changing beliefs after new evidence;
- inference about motives;
- advice about whether information should be disclosed;
- social duty versus personal preference;
- Darcy's first proposal and Elizabeth's refusal;
- nested claims about what one person believed another person felt.

Current proposition embedding and epistemic relations remain sufficient.

The reusable lexical need is especially clear for:

- Reputation;
- Trust;
- Respect;
- Admire;
- Deceive.

### Chapters 37–50 — PASS / BELIEF REVISION / SHAME / GRATITUDE

Darcy's letter, Pemberley, Lydia's elopement and the response to it stress:

- belief revision;
- reinterpretation of prior evidence;
- shame/disgrace/reputation;
- gratitude;
- forgiveness;
- responsibility/blame;
- counterfactual reflection;
- concealment and selective disclosure.

No new tense, evidential or counterfactual architecture is required.

### Chapters 51–61 — PASS / CONSENT / LOVE / SOCIAL COMMITMENT

The conclusion stresses:

- changing affection;
- second proposals;
- engagement and marriage;
- parental consent;
- refusal to promise;
- social approval/disapproval;
- love distinguished from mere liking;
- forgiveness and restored friendship;
- reputation after marriage.

Again, the structure is already expressible. The core dictionary was the limiting factor.

## Frankenstein (1818) — full-novel findings

The 1818 edition uses Walton's four opening letters followed by three volumes whose chapter numbering restarts.

### Walton letters — PASS / NESTED COMMUNICATION / GOALS

Pressure includes:

- letters as durable communication;
- uncertain future plans;
- hopes and fears;
- conditional success/failure;
- friendship as a desired social relation;
- comparing possible futures;
- testimony recorded for another reader.

Existing Sign/Information, Say/Tell/Ask, Intend/Plan/Attempt, PossibleTo/ProbableTo, conditional and temporal architecture is sufficient.

The general lexical weakness is friendship, trust, fear, hope-like emotional language and learning.

### Volume I — PASS / CAUSATION / LEGAL-EPISTEMIC / RESPONSIBILITY

Pressure includes:

- family/kinship;
- education and knowledge acquisition;
- scientific discovery;
- assembling/animating a new being;
- causal responsibility for downstream deaths;
- testimony and circumstantial evidence;
- guilt/innocence claims;
- coerced false confession;
- grief, remorse and self-blame.

Creation/animation itself belongs to world ontology: the language can describe parts, joining, life/state change and causation, while a real world package must define what operations actually produce a living entity.

Legal guilt and court procedure also remain institutional world data.

The reusable general semantics are:

- Learn / Teach / Understand / Remember;
- ResponsibleFor;
- GrieveFor / RemorseFor / ShameAbout;
- Trust.

### Volume II — PASS / LANGUAGE LEARNING / SOCIAL EXCLUSION / MORAL EVALUATION

The creature's narrative stresses:

- observation-based learning;
- language acquisition;
- reading;
- learning social institutions;
- friendship/companionship;
- admiration, compassion, gratitude and hatred;
- rejection based on appearance;
- revenge motives;
- moral self-evaluation;
- claims about creator duties;
- request for a companion;
- consent/refusal bargaining.

This is excellent anti-Yona pressure because much of the novel is about social/cognitive development rather than combat mechanics.

No new grammar is required.

### Volume III — PASS / PROMISE / REFUSAL / HYPOTHETICAL DESCENDANTS

Pressure includes:

- a promise to create a companion;
- revoking/breaking that promise;
- explicit refusal and consent;
- hypothetical reproduction and future generations;
- risk to an entire species;
- marriage;
- threats and revenge;
- responsibility for indirect consequences;
- grief and remorse;
- testimony after Victor's death.

Counterfactual, Future, PossibleTo, Cause, Promise, Intend and collection/Kind semantics remain sufficient.

The refusal/consent family is again independently confirmed as ordinary reusable vocabulary.

## New general core entries

### Social/affective Relations

- Love
- Hate
- Trust
- Respect
- Admire
- GratefulTo
- CompassionFor
- JealousOf
- Fear
- GrieveFor
- RemorseFor
- ShameAbout

### Social/kinship/property Relations

- FriendOf
- ParentOf
- SiblingOf
- SpouseOf
- EngagedTo
- Own
- ResponsibleFor

### Cognitive Relations

- Understand
- Remember

### Ordered social Attribute

- Reputation

### Social/cognitive Processes

- Consent
- Refuse
- Forgive
- Deceive
- Learn
- Teach
- Apologize
- Thank

### Ordinary emotional Properties

- Happy
- Sad
- Angry

All are ordinary productive semantics, not book-specific names or magical macros.

## Deliberately not added

The books also contain many important concepts that do **not** justify new core roots yet.

### World/institution data

- Regency entail/inheritance law;
- specific social ranks and titles;
- legal courts, trial procedure and criminal guilt;
- currencies/wealth systems;
- marriage law;
- specific educational/scientific institutions;
- Frankenstein's physical method for constructing/animating life.

These belong in world/history packages when objective use requires them.

### Still-compositional convenience vocabulary

No primitive is required yet for:

- Accept — often decomposes into Consent/Promise/Intend depending on the object accepted;
- Misunderstand — represent the mistaken belief/interpretation explicitly;
- Lie — represent Say plus deceptive intent/content, or use Deceive when successful deception matters;
- Hope — often Want plus possibility/expectation;
- Regret — counterfactual preference/remorse can be represented compositionally;
- Guilt/Innocence — legal/moral responsibility depends on a normative world/institution context;
- Revenge — Intend/Plan/Cause/Harm with motive/history;
- Invitation/Offer — Ask/Say plus proposed EventSpec and social context;
- reputation loss/gain — Change/ChangeBy over Reputation.

These may later become compression vocabulary if repeated corpus pressure shows that readability warrants them.

## Anti-overfitting conclusion

The two novels give a useful mixed result:

1. **Cuspell's semantic architecture generalizes well outside Yona.**
   No new grammar/type-system gap appeared across a 61-chapter social novel and the full 1818 _Frankenstein_.

2. **The executable core dictionary was over-specialized in vocabulary coverage.**
   It had extensive action/magic/system-oriented semantics but almost no explicit social-emotional layer.

3. **The correct response is vocabulary expansion, not grammar redesign.**
   The 33 added entries address meanings independently required by both corpora.

4. **World ontology remains the next major engineering frontier.**
   Both novels reinforce that institutional/social facts and physical creation/identity need objective world models if spells are ever to act on them.

Future corpus testing should continue to distinguish:
- structural failure;
- reusable ordinary semantic vocabulary;
- historical Old Names;
- setting/institution/world ontology;
- style/pragmatics.
