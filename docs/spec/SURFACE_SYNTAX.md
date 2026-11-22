# Canonical Surface Syntax and Parsing

_Status: normative transliteration syntax v0.10_

This file defines the **current** Latin/ASCII transliteration of Cuspell's approved rune script. All 217 root meanings plus numeric-one `@` have assigned glyph designs, and the [offline keyboard](../../assets/glyphs/references/idylwild/keyboard_kit/meaning_keyboard.html) provides reversible typography. Transliteration remains the normative parser surface. Historical v0.2-v0.7 snapshots live under `archive/syntax/`.

The semantic AST remains normative beneath the surface form.

## 1. Design target

Normal Cuspell should look like a flat foreign-language sentence, not a printed syntax tree or programming language.

Canonical writing prefers:

- ordinary whitespace between larger units;
- tight adjacency for short local units;
- sentence-final mood punctuation;
- linear grammatical boundary markers where a flat list needs to close before later material.

Parentheses remain the explicit player-facing fallback for difficult grouping. Pipe hard-binding is parser/debug compatibility only, not player-facing Cuspell.

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

## 7. Frame order and omitted optional positions

Relations and Processes declare ordered frames.

Required roles must be supplied.

Optional roles may be omitted, but omission means **unspecified/unconstrained**, not "infer what the writer intended."

A trailing optional role may simply be absent. To skip an optional position while supplying a later position, write one `_` for each skipped slot:

`Move This _ _ ThisPath!`

The same marker can close an omitted broad optional tail before an outer expression continues:

`Say Self Obligated Self MoveSelfHere _ You!`

The marker has no semantic role identity. It means only "no value in this optional position," so it is zero-mana grammar. It is invalid where the current frame slot is required.

English/internal slot labels are not surface Cuspell and cannot be written as zero-mana `:role` selectors.

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

When later material must follow in the same sentence, use the standalone approved colon punctuation `:` (zero mana), whether the group is Sequence or Concurrent:

Example:

`Permitted You Sequence MoveYouHere MoveYouThere : Self.`

This closer is canonical approved punctuation. They exist specifically so ordinary Cuspell does not have to expose a visible tree with braces or parentheses.

## 10. True Collection values

Collections remain real semantic values:

`{This,Self,You}`

Use collection punctuation when the meaning genuinely is a Collection consumed by Count, Filter, Partition, selectors, and similar operations.

Ordinary And/Or and Sequence/Concurrent do not require visible Collection syntax.

Collection punctuation costs no mana.

## 11. Binders and variables

Canonical binder declaration:

`:«This»:This`

The label `«This»` is spelled with an existing rune and means only a grammatical handle in this position. The witness `This` has semantic type Entity; this replaces the non-Cuspell word `Entity` in written syntax. Frames such as Create already specify the binder type, so their declarations need no witness: `Create :«This» ... $«This» ...!`.

Reference:

`$«This»`

A named Kind may be the domain:

`:«This»:«Know«MoveLifeThing»»`

Example:

`All :«This»:«Know«MoveLifeThing»» Life $«This».`

Binder labels, `# Canonical Surface Syntax and Parsing

_Status: normative transliteration syntax v0.10_

This file defines the **current** Latin/ASCII transliteration of Cuspell's approved rune script. All 217 root meanings plus numeric-one `@` have assigned glyph designs, and the [offline keyboard](../../assets/glyphs/references/idylwild/keyboard_kit/meaning_keyboard.html) provides reversible typography. Transliteration remains the normative parser surface. Historical v0.2-v0.7 snapshots live under `archive/syntax/`.

The semantic AST remains normative beneath the surface form.

## 1. Design target

Normal Cuspell should look like a flat foreign-language sentence, not a printed syntax tree or programming language.

Canonical writing prefers:

- ordinary whitespace between larger units;
- tight adjacency for short local units;
- sentence-final mood punctuation;
- linear grammatical boundary markers where a flat list needs to close before later material.

Parentheses remain the explicit player-facing fallback for difficult grouping. Pipe hard-binding is parser/debug compatibility only, not player-facing Cuspell.

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

## 7. Frame order and omitted optional positions

Relations and Processes declare ordered frames.

Required roles must be supplied.

Optional roles may be omitted, but omission means **unspecified/unconstrained**, not "infer what the writer intended."

A trailing optional role may simply be absent. To skip an optional position while supplying a later position, write one `_` for each skipped slot:

`Move This _ _ ThisPath!`

The same marker can close an omitted broad optional tail before an outer expression continues:

`Say Self Obligated Self MoveSelfHere _ You!`

The marker has no semantic role identity. It means only "no value in this optional position," so it is zero-mana grammar. It is invalid where the current frame slot is required.

English/internal slot labels are not surface Cuspell and cannot be written as zero-mana `:role` selectors.

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

When later material must follow in the same sentence, use the standalone approved colon punctuation `:` (zero mana), whether the group is Sequence or Concurrent:

Example:

`Permitted You Sequence MoveYouHere MoveYouThere : Self.`

This closer is canonical approved punctuation. They exist specifically so ordinary Cuspell does not have to expose a visible tree with braces or parentheses.

## 10. True Collection values

Collections remain real semantic values:

`{This,Self,You}`

Use collection punctuation when the meaning genuinely is a Collection consumed by Count, Filter, Partition, selectors, and similar operations.

Ordinary And/Or and Sequence/Concurrent do not require visible Collection syntax.

Collection punctuation costs no mana.

## 11. Binders and variables

Canonical binder declaration:

`:«This»:This`

The label `«This»` is spelled with an existing rune and means only a grammatical handle in this position. The witness `This` has semantic type Entity; this replaces the non-Cuspell word `Entity` in written syntax. Frames such as Create already specify the binder type, so their declarations need no witness: `Create :«This» ... $«This» ...!`.

Reference:

`$«This»`

A named Kind may be the domain:

`:«This»:«Know«MoveLifeThing»»`

Example:

`All :«This»:«Know«MoveLifeThing»» Life $«This».`

 references, and type witnesses are zero-mana grammar (the witness specifies type but is not invoked as a semantic claim). Meaning-bearing runes in the actual sentence still pay their usual costs.

The older bracketed form `[a:Domain]` may remain parser-compatible but is not canonical.

### Open questions

A question may introduce one or more unknown values before the query:

`:«This»:This ParentOf $«This» Self?`

Read: which Entity bound under the rune label `«This»` is a parent of Self?

`:«Here»:Here At This $«Here»?`

Read: at which Location bound under the rune label `«Here»` is This?

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

They are legal zero-mana player-facing grammar, but should be uncommon in ordinary prose. Prefer tight adjacency for short local units and ordinary flat typing when the structure is already unique.

### Pipe compatibility

The reference parser still accepts pipe hard-binding, for example `Move|This|Here!`, so historical tests and debugging tools can force a hard token group.

Pipe is **not current player-facing Cuspell**. New player material must not teach or require it. It remains zero-cost only because it is parser/debug punctuation rather than semantic content.

## 14. Transliteration-only exact-root rule

Latin transliteration can create an artifact the approved rune script does not have: one registered root label may contain text that could also be segmented into shorter root labels.

Therefore an exact registered root wins before dynamic segmentation.

The actual glyphs distinguish one registered rune from several adjacent signs physically. The orthographic converter prefers a whole registered rune and otherwise converts only one unambiguous decomposition of tightly joined roots. For glyph-origin text, decoding may insert the minimum locally necessary **word boundary** to retain that physical distinction on re-encoding: separate `This` + `Interval` glyphs become `This Interval`, whereas the dedicated `ThisInterval` glyph remains `ThisInterval`. The same exact-root conflict exists for `ThisPath` and `ThisRegion`. These disambiguating spaces are transliteration aids, not semantic operators.

## 15. Mana cost of grammar

Current zero-mana grammar includes:

- whitespace;
- sentence punctuation;
- the `_` omission marker;
- binder/reference marks;
- collection punctuation;
- quotation delimiters;
- the standalone `:` flat event-list closer;
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


## Surface v0.10 — inferred rune-native binders

A binder can omit a type witness when its typed uses uniquely determine its type:

- `All :«This» Life $«This».` — Life takes Entity, so the variable is inferred as Entity
- `:«This» At Self $«This»?` — At needs Location in its second argument
- `Collect :«This» Life $«This»` — produces a typed Collection:Entity after inference

Inference uses all typed constraints from the complete local predicate. Generic Any/SemanticValue slots supply no type evidence, conflicting constraints fail, and genuinely distinct overloaded parses remain ambiguous instead of picking an arbitrary type.

If no unique type is known, use a Cuspell type witness. The ordinary tight Cuspell expression `MassSelf` has output type Quantity:Mass, so `:«This»:MassSelf` is a valid witness without parentheses or English type words. The witness supplies its type rather than evaluating Self's mass; binder syntax and witness usage cost zero mana.

One rune-native label may be declared only once while that label is visible. Duplicate declarations (including nested active shadowing) fail with DuplicateBinder; independent sentences or completed scopes can reuse the name. Historical Latin binders remain compatibility input, not canonical writing.
