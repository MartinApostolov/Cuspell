# Advanced Player Grammar

## Optional arguments and the omission marker

Most arguments are positional. A trailing optional argument may simply be left out.

To skip one optional position while supplying a later one, write `_` in the skipped position:

`Move This _ _ ThisPath!`

This means: Move `This`, leave goal unspecified, leave source unspecified, and supply `ThisPath` as the path.

The same marker can explicitly end an omitted broad optional tail before an outer expression continues:

`Say Self Obligated Self MoveSelfHere _ You!`

Here `_` says only that the optional obligation context is absent, so `You` belongs to `Say` as its recipient.

`_` is grammar and costs no mana. It does **not** name a semantic role; frame order determines which optional position is omitted. It is invalid for required arguments.

## Collections

Use `{A,B,C}` only when the meaning is genuinely a Collection value.

`{This,Self,You}`

Ordinary And, Or, Sequence, and Concurrent do not need visible collection braces.

## Binders and variables

A binder introduces a temporary unknown or quantified value:

`a:Entity`

Use it later as:

`$a`

Example:

`All a:Entity Life $a.`

The variable label is grammar, not a mana-bearing rune.

## Open questions: asking for an unknown value

A yes/no question has no binder:

`LifeThis?`

An open question introduces what is unknown and then asks for values that make the query true:

`p:Entity ParentOf $p Self?`

Read it as: **which Entity p is a parent of Self?**

Another example:

`g:Location At This $g?`

Read it as: **at which Location g is This?**

The binder appears before `$p` or `$g` so the language already knows what kind of unknown the variable represents.

## Quotation and names

`«... »` is an exact Sign. Registered Old Names may additionally have a historical semantic reading. New Names remain normal names and never gain free magical macro behavior.

## Typed shorthand worth knowing

Most roots use one frame or several frames with the same operation over different types. A few advanced forms omit context that an objective spell may need to state explicitly:

- `BeforeValue value` and `AfterValue value` use the enclosing Change event; the two-argument forms state the Event explicitly.
- `End event` can mean the event's final TimePoint when a TimePoint is required, or an EventSpec that stops that ongoing Event when an EventSpec is required.
- `Before` and `During` can apply to EventSpecs or propositions by talking about matching occurrences or when the proposition holds.
- `Evaluate target`, `Rate event`, `First event`, and `RemorseFor experiencer` have contextual short forms whose omitted evaluator, interval, occurrence domain, or basis must be objectively fixed for magical use.
- `Extent subject axis` may use a context-provided CoordinateFrame; explicit `Extent subject frame axis` is preferred when geometry must be exact.
- `Through event region` lifts the ordinary path-through-region relation to the event.

`Sense` has only sensory meaning. Write an explicit channel, for example `Sense Self Vision «mark»`.

Sign interpretation is compositional rather than a separate rune. `Meaning sign content` states the real Sign-to-content relation, while `Understand mind (Meaning sign content)` states comprehension of that mapping. A familiar reading can therefore be a `Sense` event conditioned on the actual mapping being understood; learning a previously unknown mapping uses the separate `Begin Understand` transition.

### Selecting the value of a relation

`Collect` preserves the type declared by its binder. Combine it with `Unique` when a relation objectively has exactly one value under the stated constraints:

`Unique Collect e:Entity Name «Yona» $e`

`Unique Collect i:Information Meaning «mark» $i`

This is the general inverse-relation mechanism. It does not make `Name` or `Meaning` globally functional: if zero or several values satisfy the relation, `Unique` cannot supply a valid unique value.

Only one genuine multi-frame lexical irregularity remains under redesign: boundary-style `Distance`.

## Explicit grouping

Parentheses are the player-facing fallback when flat Cuspell plus tight adjacency cannot state one unique structure.

Use them sparingly: normal Cuspell should remain flat, and short local expressions should prefer tight adjacency.

