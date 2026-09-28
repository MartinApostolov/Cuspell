# Temporary Surface Syntax and Parsing

_Status: canonical transliteration syntax v0.7_

This file defines the current ASCII/Latin notation used before final rune glyphs are designed.

The semantic AST remains normative.

## 1. The three visible joins

Cuspell now distinguishes three increasingly explicit ways for written material to relate.

### Adjacency: lexical composition or tight local application

Direct adjacency is the preferred way to make short, language-like local units.

It has two typed uses.

**Registered lexical composition** creates a derived lexical meaning:

`SolidWater`

`NotLife`

`OppositeBefore`

`EndLife`

**Tight local application** binds adjacent registered roots into one complete typed expression when no registered lexical compound claims that form:

`CatSelf` = `Cat Self`

`LifeThis` = `Life This`

`DensityThis` = `Density This`

`NotLifeThis` = `Not Life This`

Resolution order is: exact registered root label, licensed lexical compound, then one uniquely typed tight application. Several distinct surviving meanings are ambiguous and invalid.

Tight adjacency is the normal prose tool for small predicate/reference or attribute/reference units. It does not require the writer to expose the semantic AST.

### Whitespace: ordinary token separation

Whitespace is the normal way to write successive Cuspell words/runes.

Examples:

`SolidWater This.`

`Move This Here.`

`If Life This EndLife This.`

Whitespace does not itself mean application, And, Sequence, or any other semantic relation. The typed parser uses registered frames and result types to determine how the token stream composes.

### Pipe: hard application binding

`|` explicitly binds the connected tokens into one complete subexpression before the surrounding token stream is parsed.

Examples:

`Move|This|Here.`

is an explicit form of:

`Move This Here.`

while:

`Move|A|B C`

first creates the hard-bound subexpression `Move(A,B)`; `C` remains outside that group.

A pipe group must be complete by itself for the type expected at that location. The parser never lets later whitespace-separated tokens leak back inside it.

## 2. Typed prefix parsing

The ordinary whitespace stream uses typed prefix parsing.

A head selects one of its registered frames. Its arguments are recursively consumed from left to right according to each slot's required type.

Example:

`Equal Duration ThisEvent @@.`

can normalize to:

`Equal(Duration(ThisEvent), 2)`

when the types and dimensions are compatible.

Example:

`If Life This EndLife This!`

normalizes to:

`Command(If(Life(This), End(Life(This))))`.

No parentheses or pipes are required when exactly one full type-correct parse exists.

## 3. Full-consumption and ambiguity rules

A complete sentence must have a parse that consumes every top-level token.

- zero full parses -> invalid;
- one semantic normal form -> valid;
- several parses with the same normal form -> valid;
- several distinct semantic normal forms -> ambiguous and invalid until rewritten.

The parser never chooses the most plausible interpretation.

Whitespace therefore gives no free conjunction or sequencing. For example, a complete Move followed by an unrelated EventSpec is invalid unless an explicit semantic structure such as Sequence consumes both.

## 4. Hard binding with pipe

A maximal pipe-connected group is parsed independently as one expression.

Equivalent when unambiguous:

`Move This Here`

`Move|This|Here`

Mixed form is allowed:

`If Life|This EndLife|This`

The two pipe groups are parsed first and then supplied to If.

A hard-bound group is useful when:

- the ordinary token stream would have more than one parse;
- the writer wants to force a boundary;
- a complex expression is easier to inspect with explicit structure.

Pipe is zero-mana syntax.

Spaces around a pipe are ignored:

`Move | This | Here`

is the same hard group as:

`Move|This|Here`.

## 5. Parentheses

Parentheses remain the strongest explicit grouping escape hatch.

They are useful when a desired group contains spaces or when flat/tight syntax would otherwise be ambiguous. They are not normal player-facing prose.

Example:

`If (Life This) (EndLife This)`

Parentheses are zero-mana syntax and do not alter semantic cost.

Canonical player-facing style should prefer tight local adjacency plus ordinary spaces. Pipe and parentheses are fallback/debugging tools for ambiguity or unusually difficult structures.

## 6. Sentence mood and termination

Sentence-final punctuation carries both termination and mood.

Assertion:

`Cat Self.`

Question:

`Life This?`

Command:

`Move This Here!`

Thus `.`, `?`, and `!` each mark both the end of the sentence and its mood. There is no canonical leading mood mark.

All three punctuation marks cost zero mana.

The reference parser temporarily accepts the pre-v0.5 forms `?Life This.` and `Move This Here!` for compatibility with older tests/documents, but they are not canonical surface Cuspell.

## 7. Role markers

Temporary role syntax remains:

`:role`

A role marker assigns the following expression to a named role in the currently active frame.

Examples:

`Move This Here :source There`

`Move This :path ThisPath`

This lets a writer skip optional positional roles without ambiguity.

Role markers are zero-mana grammar.

## 8. Collections

Finite structural collections remain:

`{A,B,C}`

Each item is a complete expression and may use ordinary space syntax:

`Sequence {Move This Here,EndLife Self}`

Braces and commas cost zero mana.

Variadic heads should prefer a collection when an unbounded whitespace stream would make the stopping point unclear.

## 9. Binders

Binder declaration:

`[a:Human]`

Reference:

`$a`

Example:

`All [a:Human] Life $a.`

Binder marks and variable labels are grammar and cost zero mana. Semantic Kind roots written in binder domains still cost normally.

Derived compound Kinds may appear as binder domains:

`All [a:SolidWater] ...`

when the compound is legal.

## 10. Quotation and exact names

Quotation remains:

`« ... »`

Quotation produces an exact Sign rather than evaluating the enclosed writing as active sentence grammar.

Quoted Signs may nest:

`«Yona's«SharpStick»»`

Punctuation, spaces, pipe characters, and nested quotation inside the outer Sign are preserved exactly. Thus `«SharpStick»` and `«Sharp!Stick»` are distinct Signs, and the internal `!` is not command mood.

A quoted Sign may additionally have a registered **Old Name** semantic reading. Only entries historically registered in `language/names/old_names.json` receive that reading. Ordinary/New Names remain Signs used through Name/reference semantics and do not become magical macros.

Quotation marks themselves cost zero mana. A registered Old Name pays the frozen cost of its historical name units. Otherwise semantic roots physically written inside a quoted Sign retain their normal written cost without gaining macro expansion.

See `NAMES_AND_WORLDBUILDING.md`.

## 11. Lexical compounds versus syntactic grouping

These must not be confused.

`SolidWater`

is one lexical compound expression built from adjacent meaning-bearing roots.

`Solid|Water`

is a hard syntactic application group and is not automatically the same thing.

Only registered lexical compound rules license adjacency meanings such as Property + Kind restriction.

This distinction will eventually be visible directly in the rune script.

## 12. Exact registered roots in transliteration

The temporary Latin spelling has one limitation the final rune script will not have: an exact registered root label can happen to contain text that could also be segmented into shorter root labels.

For transliteration, an exact registered root label wins before dynamic segmentation.

The final glyph system will distinguish one lexical rune from several adjacent runes physically, removing this textual artifact.

## 13. Mana cost

Current zero-mana syntax includes:

- whitespace;
- pipe;
- period;
- mood marks;
- parentheses;
- collection punctuation;
- role markers;
- binder/reference marks;
- quotation delimiters.

Meaning-bearing registered root occurrences still cost mana.

Normalization never refunds cost.

Thus `NotNotLife This.` may normalize semantically to `Life(This)` while still charging for both written Not roots and Life.

## 14. Canonical writing style

Normal Cuspell should look like a flat foreign sentence, not a printed syntax tree.

Use tight adjacency for short local units and whitespace between larger phrase units.

Preferred:

`CatSelf.`

`LifeThis.`

`SolidWater This.`

`Move This Here!`

`More Evaluate CatSelf Evaluate HumanSelf.`

`If LifeThis EndLifeThis!`

The contextual one-argument Evaluate form uses the discourse evaluator; the explicit form remains available when the evaluator must be named.

Pipe is available when clarity or ambiguity requires it:

`!If Life|This EndLife|This.`

Parentheses are the final explicit grouping tool and should be uncommon in ordinary prose.

## 15. Future rune script

The final rune writing system can map these distinctions naturally:

- physically adjacent distinct glyphs -> lexical compound or tight local application, resolved by registered lexical rules and types;
- ordinary spacing -> separation between larger phrase units;
- connecting stroke/attachment mark -> pipe-like hard binding;
- enclosure -> parenthesized grouping;
- small case/role marks -> `:role`.

This keeps the current transliteration useful without forcing the final writing system to resemble source code.


## 10. Infix And/Or and flat Sequence/Concurrent

Canonical proposition conjunction and disjunction follow the spoken order:

`LifeThis And MagicThis.`

`LifeThis Or MagicThis.`

rather than requiring prefix And/Or over visible collection values.

Same-operator chains remain linear:

`LifeThis And MagicThis And WholeThis.`

`LifeThis Or MagicThis Or WholeThis.`

Mixed bare And/Or deliberately has **no implicit precedence**. If both occur in one logical expression, grouping must make scope explicit:

`(LifeThis And MagicThis) Or WholeThis.`

This avoids importing an invisible programming/mathematical precedence convention into ordinary Cuspell.

Ordered and concurrent event groups are both variadic and flat:

`Sequence MoveSelfHere MoveSelfThere!`

`Concurrent MoveSelfHere MoveYouThere!`

A sentence-final mood mark closes either flat event group automatically, even when it is the final nested expression of the sentence.

When later material must follow the group, a zero-mana grammar marker closes it explicitly:

`Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd :authority Self.`

`Permitted You Concurrent MoveYouHere MoveYouThere ConcurrentEnd :authority Self.`

`SequenceEnd` and `ConcurrentEnd` have no semantic AST nodes of their own; they are only surface boundary markers.

Collections remain semantic values for operations that genuinely consume a Collection. Removing braces from ordinary And/Or/Sequence/Concurrent does not remove Collection<T> from the language.

## 11. Bare binder declarations

Canonical binder declaration is:

`a:Human`

and reference remains:

`$a`

Example:

`All a:Human Life $a.`

The older bracketed spelling `[a:Human]` may remain parser-compatible during migration, but brackets are not part of canonical v0.7 prose.
