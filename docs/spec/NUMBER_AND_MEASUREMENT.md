# Number, Quantity, and Measurement System

_Status: current working specification aligned with executable data_

This specification defines exact numbers, dimensions, Units, arithmetic, comparison, thresholds, ratios, and Rate.

## 1. Numbers

`@` is the positive unit number:

- `@` = 1
- `@@` = 2
- `@@@` = 3

Each written `@` costs one mana.

`Zero` is exact numeric zero.

`Opposite` applied to a Quantity reverses sign; there is no free minus sign.

## 2. Current dimensions

Machine truth lives in `language/core/dimensions.json`.

Current named dimensions include:

- Number
- Length
- Area
- Volume
- Time
- Mass
- Density
- Heat
- Light
- Confidence
- Frequency

Equivalent derived vectors normalize to registered aliases where available.

## 3. Arithmetic

Current arithmetic operators include:

- Add
- Multiply
- Divide
- Power
- Root

Subtraction is `Add A Opposite B`.

Dimension rules are checked:

- Add requires compatible dimensions;
- Opposite preserves dimension;
- Multiply combines dimension exponents;
- Divide subtracts them;
- Power/Root require valid dimension transformations.

Mathematical compression is intentional: equivalent values may have different written mana costs.

## 4. Units

`Unit` is the single productive Unit root.

Canonical typed units are Old Names:

- `«LengthUnit»`
- `«DurationUnit»` for Time
- `«MassUnit»`
- `«HeatUnit»`
- `«LightUnit»`
- `«ConfidenceUnit»`

Unit spelling/cost comes from the Old Name registry. Scale/dimension comes from `language/core/units.json`.

Example:

`«LengthUnit» @@`

constructs a Length quantity of two canonical length units.

## 5. Scalar Attributes

A scalar Attribute is a functional typed relation from a subject to an ordered value/Quantity.

Current examples include:

- Length
- Mass
- Volume
- Density
- Heat
- Light
- Confidence
- Rate-derived quantities

A bare Attribute retrieves/measures its value; it does not silently assert that the value is nonzero or high.

## 6. Measured-property compounds

The productive compound system can combine a Quantity with a compatible scalar Attribute descriptor to form an equality Property.

Example:

`ZeroLight`

means a subject's Light value equals Zero after typed normalization.

## 7. Equality and ordering

`Equal A B` compares compatible typed values.

For Entity inputs, the dedicated Entity frame means identity equality.

`More A B` means A is greater than B on their shared ordered scale.

The former Less meaning is written by reversing More's arguments.

## 8. High and Low

`High value` and `Low value` are contextual threshold predicates over supported ordered values.

They are not exact complements: an intermediate band may exist.

With an AttributeDescriptor they can form reusable threshold Properties:

- `HighLength X`
- `HighHunger X`
- `LowHunger X`
- `HighDamage X`

Objective magical use must supply or inherit an objectively registered threshold rather than rely on vague context.

## 9. Confidence endpoints

Confidence uses a canonical normalized scale:

- `Zero` = complete rejection;
- `«ConfidenceUnit» @` = complete confidence.

World/mind models may calculate evidence/probability differently internally, but exposed Confidence normalizes to this language scale.

## 10. Value domains

Dimensions alone do not determine sign restrictions.

Examples:

- Length and temporal Extent are nonnegative;
- repeat/group sizes use integer-domain constraints;
- dynamic target expressions may carry runtime nonnegative constraints.

Value-domain metadata belongs to the registered frame/attribute and is validated separately from dimensions.

## 11. Extent and geometry

`Extent` is generalized:

- Entity -> occupied Region when Region is expected;
- Entity -> contextual holistic EvaluationValue when an extent/size evaluation is expected;
- Entity/Region + CoordinateFrame + axis number -> projected Length;
- contextual frame + axis number is available only where context resolves the frame;
- Event -> Quantity:Time.

The former Height/Width roots are axis selections of Extent rather than separate primitives.

Objective geometry should use explicit frame/axis or another exact measure when context is insufficient.

## 12. Temporal order versus temporal extent

Temporal ordering uses `Before`.

The former “after” meaning is the same ordering relation with reversed arguments.

Duration is not a separate root: temporal duration of an Event is:

`Extent event`

when a Time quantity is expected.

## 13. Ratio

`Ratio` represents component proportions and is distinct from `Divide`, which returns a quotient Quantity/value.

Ratio can be built from a pair of numbers or a numeric Collection according to the registered frames.

## 14. Rate

`Rate` is the generalized per-Time operator.

Current frames include:

- Quantity + TimeInterval -> input dimension / Time;
- EventSpec + TimeInterval -> Frequency;
- contextual EventSpec shorthand -> Frequency.

Examples of former convenience meanings:

- increasing -> `More Rate value interval Zero`;
- decreasing -> `More Opposite Rate value interval Zero`;
- exact stability -> `Equal Rate value interval Zero`;
- high habitual frequency -> `High Rate event interval`;
- low/rare frequency -> `Low Rate event interval`.

There are no separate ChangeRate or OccurrenceRate roots.

## 15. Approximate equality and ranges

Exact equality remains exact.

A tolerance is written explicitly. One two-sided numeric pattern is:

`Not More Add A Opposite B T And Not More Add B Opposite A T.`

There is no standalone ApproxEqual root.

Likewise at-least/at-most meanings use ordinary More/Equal compositions rather than dedicated base roots.

## 16. Mana and normalization

Mana is based on written meaning-bearing signs.

Equivalent arithmetic may normalize to the same value while costing different amounts because the written form differs. This is intentional: mathematical knowledge can create real linguistic efficiency.

Normalization never refunds already written cost.

## 17. Result

The measurement system separates:

- numeric value;
- dimension;
- Unit;
- Attribute;
- exact comparison;
- contextual threshold;
- Ratio;
- Rate.

That keeps physical/magical quantities typeable without proliferating one rune for every English measurement phrase.
