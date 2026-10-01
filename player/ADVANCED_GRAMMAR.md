# Advanced Player Grammar

## Named roles

Most roles are positional. To skip an optional role or state one explicitly, use `:role value`.

`Move This :path ThisPath!`

`Permitted You MoveYouHere :authority Self.`

The role marker is grammar and costs no mana.

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

Three current advanced overloads are still under language redesign because they cross a semantic boundary rather than merely omitting context: boundary-style `Distance`, interpreted-Sign `Sense`, and one-argument reference-resolving `Name`. They remain valid current forms, but they are not part of the beginner grammar and objective writing should prefer the more explicit relation/process forms when possible.

## Explicit grouping

Parentheses and pipe hard-binding remain legal escape/debug tools when a flat phrase cannot otherwise state one unique structure. They are not the normal visual style of player-facing Cuspell.
