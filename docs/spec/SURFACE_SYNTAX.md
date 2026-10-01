# Canonical Surface Syntax and Parsing

_Status: normative transliteration syntax v0.7_

This file defines the **current** Latin/ASCII transliteration used before final rune glyphs are designed. Historical v0.2-v0.6 snapshots live under `archive/syntax/`.

The semantic AST remains normative beneath the surface form.

## 1. Design target

Normal Cuspell should look like a flat foreign-language sentence, not a printed syntax tree or programming language.

Canonical writing prefers:

- ordinary whitespace between larger units;
- tight adjacency for short local units;
- sentence-final mood punctuation;
- linear grammatical boundary markers where a flat list needs to close before later material.

Parentheses and pipe remain legal fallback/debug grouping, not the normal style.

## 2. Sentence mood and termination

A complete sentence ends with exactly one canonical mood mark:

- `.` — assertion;
- `?` — question;
- `!` — command.

Examples:

`MatterSelf.`

`LifeThis?`

`Move This Here!`

The final mark both gives the sentence mood and terminates it. These punctuation marks cost no mana.

Legacy leading `!` / `?` with a final period may remain parser-compatible for old tests/documents, but it is **not current Cuspell**.

## 3. Whitespace and the flat token stream

Whitespace separates larger written units:

`Move This Here!`

`If LifeThis EndLifeThis!`

Whitespace itself contributes no semantic relation. It does not mean application, And, Sequence, or anything else.

The typed parser determines how the stream attaches.

## 4. Typed prefix parsing

The ordinary rule is:

> write the head first, then its arguments in the head's declared frame order.

Example:

`Move This Here!`

The parser selects a registered frame and recursively consumes arguments left-to-right according to required types.

Example:

`Equal Extent ThisEvent @@.`

may normalize to equality between the Event's temporal Extent and the number 2 when the types are compatible.

No grouping marks are required when one complete typed reading exists.

## 5. Tight adjacency

Direct adjacency is the preferred local-binding mechanism.

Resolution order is:

1. exact registered root label;
2. licensed registered lexical compound;
3. otherwise one uniquely typed tight local application.

Examples:

`MatterSelf` = local application of Matter to Self.

`LifeThis` = Life applied to This.

`DensityThis` = Density applied to This.

`NotLifeThis` = Not applied to Life(This).

`SolidMatter` is a licensed lexical restriction compound.

If adjacency produces several distinct semantic normal forms, the form is ambiguous and invalid until rewritten.

## 6. Full consumption and ambiguity

A complete sentence must consume every top-level unit.

- zero complete typed readings -> invalid;
- one semantic normal form -> valid;
- several parses with the same normal form -> valid;
- several distinct semantic normal forms -> ambiguous and invalid.

The parser never chooses the interpretation that merely sounds most plausible.

## 7. Frame order, omitted roles, and named roles

Relations and Processes declare ordered frames.

Required roles must be supplied.

Optional roles may be omitted, but omission means **unspecified/unconstrained**, not "infer what the writer intended."

A named role may explicitly fill a role or skip earlier optional positions:

`Move This :path ThisPath!`

`Move This Here :source There!`

`Permitted You MoveYouHere :authority Self.`

The `:role` mark is zero-mana grammar.

## 8. And / Or

Canonical proposition conjunction and disjunction use spoken-order infix form:

`LifeThis And MagicThis.`

`LifeThis Or MagicThis.`

Same-operator chains remain flat:

`LifeThis And MagicThis And WholeThis.`

Mixed bare And/Or has no hidden precedence. Grouping must make scope explicit when both occur in one logical expression.

Older prefix/collection-backed forms may remain parser-compatible, but they are not canonical prose.

## 9. Sequence / Concurrent

Ordered and concurrent event groups use flat event lists:

`Sequence MoveSelfHere MoveSelfThere!`

`Concurrent MoveSelfHere MoveYouThere!`

If the group reaches sentence end, the final mood mark closes it automatically.

When later material must follow in the same sentence, use the matching zero-mana grammatical closer:

`SequenceEnd`

`ConcurrentEnd`

Example:

`Permitted You Sequence MoveYouHere MoveYouThere SequenceEnd :authority Self.`

These closers are canonical language-like boundary markers. They exist specifically so ordinary Cuspell does not have to expose a visible tree with braces or parentheses.

## 10. True Collection values

Collections remain real semantic values:

`{This,Self,You}`

Use collection punctuation when the meaning genuinely is a Collection consumed by Count, Filter, Partition, selectors, and similar operations.

Ordinary And/Or and Sequence/Concurrent do not require visible Collection syntax.

Collection punctuation costs no mana.

## 11. Binders and variables

Canonical binder declaration:

`a:Entity`

Reference:

`$a`

A named Kind may be the domain:

`a:«Know«MoveLifeThing»»`

Example:

`All a:«Know«MoveLifeThing»» Life $a.`

Binder labels and `$` references are zero-mana grammar. The semantic domain still carries its normal meaning/cost.

The older bracketed form `[a:Domain]` may remain parser-compatible but is not canonical.

### Open questions

A question may introduce one or more unknown values before the query:

`p:Entity ParentOf $p Self?`

Read: which Entity `p` is a parent of Self?

`g:Location At This $g?`

Read: at which Location `g` is This?

The declaration appears before the variable reference so its domain/type is known.

## 12. Quotation and exact Signs

Quotation uses:

`«... »`

The enclosed material is exact Sign content rather than active sentence grammar.

Quoted Signs may nest. Punctuation, whitespace, and other marks inside the quote are literal.

A registered Old Name may additionally have its recorded semantic reading. New Names remain ordinary name/reference data and do not gain magical macro expansion.

Quotation delimiters cost no mana; Old Name mana follows the registered historical name units.

## 13. Explicit grouping fallback

### Parentheses

Parentheses force a grouped subexpression containing spaces.

They are legal zero-mana grammar but should be uncommon in ordinary prose.

### Pipe

Pipe hard-binds a connected group before the surrounding stream is parsed:

`Move|This|Here!`

When unambiguous this is equivalent to:

`Move This Here!`

Pipe is currently legal fallback/debug syntax and zero mana. Whether it remains an advanced player-facing device or becomes debug-only is still an open stabilization decision.

Neither parentheses nor pipe is the canonical visual style.

## 14. Transliteration-only exact-root rule

Latin transliteration can create an artifact the future rune script will not have: one registered root label may contain text that could also be segmented into shorter root labels.

Therefore an exact registered root wins before dynamic segmentation.

Final rune glyphs will distinguish one rune from several adjacent runes physically.

## 15. Mana cost of grammar

Current zero-mana grammar includes:

- whitespace;
- sentence punctuation;
- role markers;
- binder/reference marks;
- collection punctuation;
- quotation delimiters;
- SequenceEnd / ConcurrentEnd;
- fallback grouping marks.

Meaning-bearing registered signs still pay their written rune cost.

Normalization never refunds cost.

## 16. Canonical player style

Prefer:

`MatterSelf.`

`LifeThis?`

`Move This Here!`

`More Evaluate MatterSelf Evaluate ThingSelf.`

`LifeThis Or MagicThis.`

`Sequence MoveSelfHere MoveSelfThere!`

`If LifeThis EndLifeThis!`

Use explicit grouping only when the flat form cannot state one unique meaning.

## 17. Legacy compatibility boundary

The parser may intentionally continue accepting some historical forms so old tests and archived material remain reproducible.

Legacy compatibility is **not** part of the grammar a new player must learn.

Current player-facing rules live in `player/RULES.md`; historical syntax snapshots live in `archive/syntax/`.
