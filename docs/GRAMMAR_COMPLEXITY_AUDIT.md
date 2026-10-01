# Grammar and Learning-Complexity Audit

_Status: checkpoint 97 — canonical writing-rule inventory complete; no grammar change yet_

## Purpose

The semantic inventory has already reached practical reduction closure. This audit asks a different question:

> Is Cuspell's **writing grammar** small and regular, or did root reduction merely move
> complexity into a large collection of special rules?

The answer is encouraging: the current parser is overwhelmingly driven by one
typed-frame mechanism rather than one grammar rule per rune. The main complexity
problem is now **presentation/documentation drift**, plus a small number of deliberate
surface constructions.

This checkpoint does **not** redesign syntax. In particular, it preserves the
flat-language goal and the canonical `SequenceEnd` / `ConcurrentEnd` closure rule.

## 1. Machine-readable complexity snapshot

Current registry:

- **205 registered signs**;
- **125 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**.

The 205 lexicon entries expose **259 semantic frames**.

Frame distribution:

- **22 entries** have no callable frame and behave as literals/references/domain values;
- **132 entries** have exactly **1 frame**;
- **38 entries** have exactly **2 frames**;
- **13 entries** have **3 or more frames**.

Therefore **154 of 205 entries (75.1%) have zero or one frame**.

Only three entries have more than four frames:

- `Before` — **7**;
- `During` — **6**;
- `Extent` — **7**.

There are **51 multi-frame entries** in total. Their overloads still use the same
generic head-first typed parser; they do not each introduce new punctuation or
word-order rules.

Optional-role pressure is also limited:

- **20 entries** have at least one optional positional role;
- **23 frames** contain an optional role;
- only **9 slots** are explicitly `named_only`, spread across **7 roots**:
  `Obligated`, `Permitted`, `Transfer`, `Cause`, `GratefulTo`,
  `Reputation`, and `Forgive`.

The lexical compound system has only **9 productive compound rules**, based on
category/trait patterns such as Property+Kind, Not+Property, Begin/End+state,
quantity+scalar attribute, and High/Low+attribute. It is not a dictionary of
hundreds of special compound cases.

## 2. Canonical writing rules: the universal core

The current surface system can be described by **seven general rules** that apply
across almost the whole language.

### G1 — sentence end carries mood

A complete sentence ends in exactly one of:

- `.` — assertion;
- `?` — question;
- `!` — command.

The same mark also terminates the sentence.

### G2 — normal prose is a flat token stream

Whitespace separates larger written units. Whitespace itself means nothing:
it is not And, Sequence, application, or a semantic relation.

### G3 — heads precede arguments

The default order is typed prefix order:

`Move This Here!`

The head comes first; its arguments follow.

### G4 — arguments follow one declared frame order and are selected by type

Frames declare participant order. Arguments are consumed left-to-right.

When a root has several frames, input/output types select among them. This is the
central standardization mechanism: overload is ordinarily **vocabulary typing**, not a
new grammar rule.

### G5 — tight adjacency forms one local unit

Direct adjacency first checks:

1. exact registered root;
2. licensed lexical compound;
3. otherwise one uniquely typed tight local application.

Examples such as `LifeThis` and `EndLifeThis` therefore use the same typed system
rather than a separate phrase grammar.

### G6 — the whole expression must parse completely and uniquely

A sentence is valid only when all material is consumed.

- no complete typed reading -> invalid;
- one semantic normal form -> valid;
- several surface parses with the same normal form -> valid;
- several distinct semantic normal forms -> ambiguous and invalid.

The parser never chooses the most plausible reading.

### G7 — omission never means "guess"

Required roles must be supplied. Optional roles may be omitted, but omission means
unspecified/unconstrained rather than "infer what the writer probably wanted."

These seven rules account for the ordinary behavior of the great majority of the
205 registered signs.

## 3. Reusable structural constructions

On top of the seven universal rules, current Cuspell has a small set of reusable
constructions. These are grammatical tools, not one-off rune exceptions.

### S1 — named roles

`:role value` explicitly fills a frame role, especially when skipping another
optional role.

Example:

`Move This :path ThisPath!`

### S2 — infix And / Or

Canonical proposition conjunction/disjunction follows spoken order:

`LifeThis And MagicThis.`

`LifeThis Or MagicThis.`

Same-operator chains remain flat. Mixed bare And/Or has no hidden precedence and must
be grouped.

This is one deliberate departure from default head-first order.

### S3 — flat Sequence / Concurrent groups

Ordered and concurrent event groups are written as linear event lists:

`Sequence MoveSelfHere MoveSelfThere!`

`Concurrent MoveSelfHere MoveYouThere!`

Sentence end closes the group when it reaches the sentence boundary.

When later material must follow, the matching grammatical closer is used:

`SequenceEnd`

`ConcurrentEnd`

Example:

`Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd :authority Self.`

These end markers are **canonical language-like boundary markers**, not pseudocode
grouping and not candidates for removal merely because parentheses could express the
same tree.

### S4 — true Collection values

Braces/commas create an actual Collection when the semantic meaning is a collection
value:

`{This,Self,You}`

Collections remain important for selectors, Count, Filter, Partition, and related
operations. They are not required merely to write ordinary And/Or or Sequence.

### S5 — binders and variables

Canonical binder:

`a:Domain`

Reference:

`$a`

This supplies quantification, selectors, and open questions without adding a
meaning-bearing rune for each variable.

### S6 — quotation / exact Signs / Names

`«... »` protects exact sign content and supports the Old Name / New Name system.

This is a general quotation mechanism, not a special syntax for each named concept.

### S7 — explicit grouping fallback

Parentheses can force a group when ordinary flat typed parsing would otherwise be
ambiguous.

They are legal zero-mana grammar but should remain uncommon in normal prose.

### S8 — hard-binding pipe

Pipe currently remains a legal hard-binding/debug mechanism.

Unlike SequenceEnd/ConcurrentEnd, pipe is **not required for normal canonical prose**.
The current documents describe it both as legal fallback syntax and as a possible
future connecting mark in the rune script.

That status should be made explicit in the next simplification pass: either keep it
as an advanced/debug escape hatch or remove it from the player-facing grammar while
retaining parser compatibility. No decision is made at checkpoint 97.

## 4. Genuine surface special cases

The parser does **not** contain one special word-order rule for every root.

The canonical surface departures from the generic typed-prefix mechanism are
concentrated in only three families:

1. **And / Or** use infix spoken order instead of head-first order.
2. **Sequence / Concurrent** accept variadic flat event lists and use sentence end or
   their matching End marker as the stopping rule.
3. **Open questions** may place one or more binder declarations before the query
   expression so the variables are in scope for the question.

Everything else that looks "special" in most lexical entries is primarily a typed
frame, semantic normalization, contextual meaning, or value-domain restriction—not
a new writing grammar.

There are also implementation-specific semantic normalizations for roots such as
Not and arithmetic operators, but those do not create additional surface word-order
or punctuation rules for a player.

## 5. Multi-frame roots are the next place to inspect

The language has **51 multi-frame entries**, but most are modest overloads:

- **38** have exactly two frames;
- **9** have three;
- **1** has four;
- only **3** have five or more.

The highest-complexity roots are therefore a small, inspectable set rather than the
entire vocabulary.

Priority review:

- `Before` — 7 frames;
- `Extent` — 7 frames;
- `During` — 6 frames;
- `Overlap` — 4 frames;
- then the 3-frame group:
  `And`, `End`, `Change`, `Distance`, `Rate`, `Cause`, `Use`,
  `Say`, and `High`.

The next audit should ask whether each overload is:

1. the same operation generalized across input types;
2. an explicit/contextual short form of the same operation;
3. a genuinely different lexical sense that the learner must memorize.

Only category 3 represents hidden vocabulary irregularity.

## 6. Compatibility syntax is inflating the apparent grammar

Several older surface forms remain accepted so existing tests/documents do not
break. They should not be counted as rules a new player must learn.

Current compatibility/noncanonical families include:

- leading `!` / `?` mood with a final period;
- bracketed binders such as `[a:Human]`;
- older prefix/collection-backed And/Or forms;
- older brace-backed Sequence/Concurrent forms;
- pipe-heavy tree-like spellings used by older documentation/tests.

The parser can continue accepting these during migration, but the player grammar
should teach one canonical form for each meaning.

## 7. Documentation drift found by the audit

The written specifications currently make the grammar look more complicated than the
actual canonical system because different generations of surface syntax remain mixed
inside normative-looking documents.

Concrete drift:

- `SURFACE_SYNTAX.md` is marked v0.7 but contains an earlier bracketed-binder section
  and then a later bare-binder section;
- its section numbering restarts after section 15;
- several examples still use migrated direct noun roots such as Cat/Human/Water;
- one pipe example still uses legacy leading command mood;
- `SENTENCE_GRAMMAR.md` still describes surface syntax v0.3, leading command/question
  marks, and bracketed binders in sections that read as current grammar;
- `LINEAR_PARSING.md` still labels itself as a v0.3 algorithm for surface v0.4 even
  though canonical surface syntax is v0.7;
- historical parser-compatible forms are often shown beside canonical forms without a
  single clear "players learn this / parser also accepts this" boundary.

This is documentation debt, not evidence that the language itself needs all of those
rules.

## 8. Current complexity result

Using the categories above, current Cuspell has:

- **7 universal writing rules**;
- **8 reusable structural mechanisms** if pipe is counted;
- **3 notable canonical surface special-case families** inside those mechanisms;
- **0 evidence of one writing rule per rune**;
- **51 multi-frame lexical entries** to inspect for hidden semantic irregularity;
- **4+ legacy/noncanonical surface families** that should be pushed out of the
  beginner-facing grammar.

The most important result is that **semantic-frame count is not grammar-rule count**.
The 259 frames are mostly data consumed by one parser rule.

## 9. Beginner-learning implications

A basic caster does not need the whole grammar.

A first-use subset can omit:

- binders/variables;
- open questions;
- Collection values;
- quotation/name mechanics;
- named optional roles;
- pipe;
- mixed And/Or grouping;
- nested Sequence/Concurrent closure.

A beginner can therefore work with a smaller teaching core:

1. final mood punctuation;
2. flat head-first expressions;
3. left-to-right typed arguments;
4. tight local adjacency;
5. ambiguity is never guessed;
6. simple And and/or top-level Sequence/Concurrent as needed.

This is a plausible one-page grammar target. Actual learning time should be tested
with people rather than inferred from rule count alone.

## 10. Standardization opportunities

The audit recommends **no semantic or syntax deletion yet**. The next cleanup should
first make the canonical grammar unambiguous in the documentation.

Highest-value standardizations:

1. create one authoritative player-facing canonical grammar section;
2. move legacy syntax into a clearly labeled compatibility appendix;
3. keep `SequenceEnd` / `ConcurrentEnd` as the canonical linear closure rule;
4. update all canonical examples to current roots/Old Names;
5. fix version/section-number drift across SURFACE_SYNTAX, SENTENCE_GRAMMAR, and
   LINEAR_PARSING;
6. explicitly decide whether pipe is player-facing advanced grammar or debug-only;
7. then audit the 51 multi-frame roots, beginning with Before/During/Extent.

## Checkpoint result

No language behavior changes at checkpoint 97.

Inventory remains:

- **205 registered base entries**;
- **125 semantic primitive candidates**;
- **54 formal constructors**;
- **16 reference forms**;
- **10 domain values**;
- **0 unresolved candidates**;
- **0 derived candidates**.

The next concrete step is a **canonical grammar documentation consolidation**, followed
by the targeted multi-frame overload audit.
