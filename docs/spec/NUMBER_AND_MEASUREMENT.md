# Number, Quantity, and Measurement System

_Status: working specification v0.1_

This specification formalizes number values, arithmetic compression, dimensions, units, scalar attributes, ratios, and vectors while preserving the rule that a shorter valid expression can cost less mana.

## Core quantity model

A Quantity carries a numeric value and a dimension. Pure numbers are dimensionless. Measured quantities use dimensions such as Length, Time, Mass, Mana, Charge, thermal level, and light intensity.

`@` is the primitive positive unit number:

- `@` = 1
- `@@` = 2
- `@@@` = 3

Each written `@` costs one mana.

`Zero` is a one-rune Quantity with value 0.

`Opposite` applied to a Quantity reverses its sign, so `Opposite@@` normalizes to -2. There is no free minus sign.

## Arithmetic

Meaning-bearing arithmetic operators include:

- Multiply (`x`)
- Divide
- Add
- Power
- Root

Subtraction can be derived as Add(A, Opposite(B)).

The existing compression rule is retained: `@@@@x@@@@` represents 16 and costs only the runes actually written.

Arithmetic is dimension-typed:

- Add requires compatible identical dimensions.
- Opposite preserves dimension.
- Multiply combines dimensions.
- Divide subtracts dimension exponents.
- Power transforms dimension exponents.
- Root is legal only when the resulting dimension is valid.

For Power/Root on a dimensionful quantity, the exponent/root degree must be an exact statically known dimensionless number so the output dimension can be checked before execution. Runtime-variable exponents/degrees are allowed only for dimensionless `Quantity:Number` bases/radicands. In the current integer-exponent dimension model, Root is valid only when dividing the input dimension exponents by the degree leaves integral exponents; degree zero is invalid.

Examples of derived dimensions can include:

- Area = Length^2
- Volume = Length^3
- Speed = Length / Time
- Frequency = 1 / Time
- Density = Mass / Volume
- Pressure = Force / Area

Equivalent expressions normalize to the same value/dimension but keep their different written mana costs.

Because Frequency has dimension Time^-1, recurrence period is compositional rather than lexical:

`Divide @ OccurrenceRate E`

has Time dimension and replaces a standalone Period root. An explicit interval may be supplied to OccurrenceRate when the measurement scope must be fixed.

## Exactness

Integer and rational arithmetic should remain exact. Irrational results may remain symbolic. Approximation or tolerance must be explicit; magical execution never silently chooses a rounding precision.

## Units

A Unit is a registered scale constructor for a dimension, not a new core Category.

Conceptually:

`Unit<D>(number) -> Quantity<D>`

A measured quantity must have either an explicit registered Unit or occur in a frame whose unit is explicitly fixed by the rules. No command may rely on the GM choosing an unstated unit.

Units normalize to a canonical internal scale for comparison.

## Scalar attributes

The earlier draft treated Heat, Light, Length, Mass, and similar concepts too loosely as Boolean Properties. Refine them as scalar measurement functions.

A scalar attribute has the form:

`Attribute(subject...) -> Quantity<D>`

and carries trait `scalar-attribute(D)`.

Examples:

- Length(Entity) -> Quantity<Length>
- Mass(Entity) -> Quantity<Mass>
- Duration(Event) -> Quantity<Time>
- Light(subject) -> Quantity<LightIntensity>
- Heat(subject) -> Quantity<ThermalLevel>
- Distance(A,B) -> Quantity<Length>

This makes the distinction between an attribute and a predicate precise.

## Measured-property shorthand

To preserve useful compact constructions such as `ZeroLight`, add:

`Quantity + ScalarAttribute<D> -> Property`

The result means that the subject's attribute equals the specified quantity after unit normalization.

Thus `ZeroLight` means Light magnitude equals zero.

A bare scalar attribute names/measures the attribute; it does not silently mean "greater than zero."

## Comparisons

`Equal(A,B)` compares compatible typed values.

`Same(A,B)` remains object/reference identity and is different from Equal.

`More(A,B)` and `Less(A,B)` compare ordered compatible scalars. Less may be the formal reversible counterpart of More.

Qualitative threshold meanings should reuse productive comparison machinery where possible. Magical use requires either a fixed lexical threshold or an explicit comparison standard.

## Contextual High and Low thresholds

`High(value)` means that an ordered value is above the relevant contextual standard. It is contextual and therefore is not enough by itself for objective magical execution.

When combined lexically with an AttributeDescriptor, High produces a first-class PropertyDescriptor. Examples:

- `HighLength X` for the former Long meaning;
- `HighHunger X` for the former Hungry meaning.

Because the result is still a PropertyDescriptor, higher-order forms such as `Almost HighHunger X` remain well typed.

For event frequency, `High OccurrenceRate E I` replaces the former Often root. The symmetric `Low` operator means below the relevant contextual standard and is deliberately not equivalent to `Not High`; an intermediate band can exist.

When combined with an AttributeDescriptor, Low also produces a first-class PropertyDescriptor. `LowHunger X` is therefore the contextual satiated/full-enough state without claiming that every non-high hunger value is sated.

`Low OccurrenceRate E I` replaces the former Rarely root. OccurrenceRate also has a contextual-interval frame for ordinary discourse when the interval is omitted.

## Normalized Confidence endpoints

Confidence is a bounded ordered quantity whose canonical Cuspell representation fixes two semantic endpoints:

- `Zero` is complete rejection;
- `«ConfidenceUnit» @` is complete confidence/certainty.

Intermediate world-model confidence systems normalize into that interval. This allows exact certainty to be written as equality with one ConfidenceUnit while keeping ordinary probability terms contextual through `High Confidence ...`.

## Value-domain restrictions

A dimension does not by itself determine whether negative values are allowed.

Examples:

- Duration is nonnegative.
- absolute Length is nonnegative.
- Charge may be signed.
- displacement coordinates may be signed.

Every attribute/frame declares its allowed value domain.

## Geometry measurements

`Volume` is reserved for measured three-dimensional spatial extent. A 3D region is represented as a Region/Space entity, not the same rune.

`Size` should not initially be one scalar because objects have several extents. Magical changes should identify Length, Width, Height, Volume, or another explicit measure unless a uniform-scale operation is defined.

Height and Width require a resolved CoordinateFrame. No command may infer an "obvious" orientation.

Area is a Quantity<Length^2>; an Area amount does not by itself specify the shape or location of the affected region.

## Time measurements

`Duration(Event) -> Quantity<Time>`.

`Now` is a TimeReference, not a Duration.

Temporal order (Before/After) and temporal extent (Duration) remain separate.

## Mana

Mana is a scalar resource dimension. Rune-cost rules consume a Mana quantity at execution level; casters do not need to write the word Mana merely to pay a spell's cost.

## Ratios

`Ratio` is a dedicated Operator and replaces the earlier numerical use of `Part`.

A Ratio preserves component proportions, unlike Divide which returns one scalar quotient.

Common scaling normalizes:

3:5 = 6:10 as the same Ratio.

Blending families can consume labeled ratios. For color, the semantic model can combine a normalized Red/Green/Blue ratio with separate total Light intensity.

Accidental repetition of a color root does not encode weight.

## Vectors

Some values require magnitude and direction.

A VectorQuantity contains:

- a typed magnitude;
- direction in a resolved CoordinateFrame.

Candidates include Force, displacement, velocity, and field quantities.

Direction may use spatial semantics such as To, From, Up, and Down, but the frame must resolve objectively.

Force should therefore be vector-valued rather than a simple scalar Property.

## Thermal terminology

For game semantics, `Heat` may remain the primary scalar thermal attribute. Its formal definition is the setting's registered thermal-level measure, not necessarily the strict real-world physics meaning of the English word.

Cold is lower Heat/thermal level, not an independent substance and not automatically OppositeHeat.

## Precision ranges

Future comparison constructors should include concepts equivalent to:

- AtLeast
- AtMost
- strict ordered range: `More value lower And More upper value`
- explicit tolerance

Exact equality stays exact unless such a range/tolerance is written.

Approximate equality is also compositional. For same-dimension A, B, tolerance T: `And {Not More Add A Opposite B T, Not More Add B Opposite A T}`. There is no separate `ApproxEqual` root.

## Numeric parsing

The expression tree is normative. If compact infix notation is used, precedence must be fixed:

1. grouping
2. Opposite prefix
3. Power / Root
4. Multiply / Divide
5. Add

Grouping punctuation is zero-mana syntax.

## Cost and normalization

Normalization never refunds cost.

Long and short expressions may denote the same number while costing different amounts. This is intentional and preserves mathematical knowledge as a source of magical efficiency.

Ordinary Names or aliases for large numbers do not become cheap literals unless they are registered numeric lexical items in Cuspell.

## Result

The measurement layer now separates:

- numeric value;
- dimension;
- unit;
- scalar attribute;
- comparison;
- ratio;
- vector direction/frame.

This gives physical and magical quantities objective typing while preserving arithmetic compression.


## Rate and trend

A Rate is a typed quantity expressing change or occurrence per unit of another dimension, commonly Time.

Examples:

- occurrence rate of an EventSpec;
- flow rate;
- change in an Attribute per Time;
- spawn/appearance rate.

General dimensional form:

Rate = numerator-dimension / denominator-dimension.

Useful functional forms include:

OccurrenceRate(EventSpec, interval/scope) -> Quantity<Count/Time>.

ChangeRate(value: Quantity, interval) -> Quantity<ValueDimension/Time>.

An Attribute value can be supplied directly, for example `ChangeRate Density subject interval`.

There are no separate `Increasing` or `Decreasing` roots in the minimized core. With typed zero:

- increasing -> `More ChangeRate value interval Zero`;
- decreasing -> `More Opposite ChangeRate value interval Zero`.

There is no separate `Stable` root in the minimized core. Exact stability is:

`Equal ChangeRate value interval Zero`

and tolerance-bounded stability is:

`And {Not More ChangeRate value interval tolerance,Not More Opposite ChangeRate value interval tolerance}`.

The tolerance form is the two-sided bound `-T <= rate <= T`; objective magical use must supply or register T.

These predicates describe trend across an interval rather than one instantaneous comparison.

An expression equivalent to "the spawn rate has been decreasing" can therefore combine:

- OccurrenceRate for the relevant creature-appearance EventSpec;
- comparison of the occurrence-rate ChangeRate against typed zero over the recent interval.

Exact magical use requires the measured EventSpec, interval, and Units/tolerance to be resolved. Ordinary discourse may inherit them from context.
