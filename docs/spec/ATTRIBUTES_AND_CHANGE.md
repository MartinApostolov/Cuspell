# Attributes, Property Families, and Change

_Status: working specification v0.1_

This file refines how scalar attributes, mutually exclusive Properties, structured values, and the generic Change Process interact.

## 1. Why an attribute layer is needed

A Boolean Property is sufficient for concepts such as:

- Life
- Whole
- Ill

but many features are better represented as values of an attribute:

- Phase = Solid/Liquid/Gas/Plasma
- Heat = measured thermal value
- Mass = measured quantity
- Pressure = measured scalar mechanical pressure
- Health = ordered biological functional condition
- Pain = ordered experienced pain intensity
- Form = GeometryProfile
- Color = ColorProfile
- Location = spatial value

The language should not treat all of these as unrelated Boolean flags.

## 2. Attribute

An **Attribute** is a functional semantic relation:

`Attribute(subject) -> ValueType`

It may be represented by a Relation carrying:

- `functional`
- `attribute`
- output type/domain

Examples:

- Heat(Entity) -> Quantity<Thermal>
- Mass(Entity) -> Quantity<Mass>
- Pressure(Entity) -> Quantity<Pressure>
- Pressure(Location) -> Quantity<Pressure>
- Health(Entity) -> EvaluationValue
- Pain(Entity) -> EvaluationValue
- Form(Entity) -> GeometryProfile
- Phase(MaterialPortion) -> PhaseValue
- Color(Entity/Surface/Light) -> ColorProfile

No new top-level lexical Category is required.

## 3. Property family members

Some familiar Property roots are convenient predicates corresponding to attribute values.

Register `Phase` as a physical-state Attribute:

`Phase(MaterialPortion) -> PhaseValue`

Example:

`Solid(x)`

normalizes to:

`Equal(Phase(x), SolidValue)`

The written rune Solid can remain a Property root with metadata:

- `family=Phase`
- `family-value=Solid`

Likewise Liquid/Gas/Plasma.

This lets the player write compact Properties without exposing an internal value object.

## 4. Exclusive families

An exclusive-family declaration belongs to the underlying Attribute.

If Phase is single-valued for the selected homogeneous subject, then:

- Solid
- Liquid
- Gas
- Plasma

are mutually exclusive family-member predicates.

A composite Entity can still contain Parts whose Phase values differ.

## 5. Structured attributes

An Attribute output does not have to be a scalar.

Examples:

- Form -> GeometryProfile
- Color -> ColorProfile
- group membership collection -> `Collect x:Entity Member $x group`

Change semantics can operate on structured values when the target value/profile is fully specified.

## 6. Change

Refine `Change` to an explicit attribute-setting Process.

Primary frame:

`Change(subject, attribute, target-value-or-profile) -> EventSpec`

Meaning:

> change the selected Attribute of subject until its value Equals/satisfies the target value/profile.

Only the selected Attribute and changes necessarily entailed by consistency/world law are directly commanded.

This is much more objective than bare `Change(subject)`.

## 7. Family-member shorthand

For a registered family-member Property, a shorter Change frame can infer the Attribute from the family:

`Change(subject, Solid)`

normalizes to:

`Change(subject, Phase, SolidValue)`

Likewise for other uniquely registered family members.

This is legitimate semantic compression because Solid's lexicon entry names its family.

## 8. Scalar Change

For scalar attributes:

`Change(subject, Heat, Quantity<Thermal>)`

sets the target thermal value.

`Change(subject, Mass, Quantity<Mass>)`

sets Mass if the magic engine permits it.

`Change(subject, Pressure, Quantity<Pressure>)`

sets the subject's registered scalar Pressure target if the world/execution model permits such a change. The separate `Pressure(Location)` query frame is not itself a command to mutate space; Change continues to select an Entity theme.

Units/dimensions must match.

## 9. Structured Change

Examples:

`Change(subject, Form, GeometryProfile)`

`Change(subject, Color, ColorProfile)`

The profile must be closed enough for execution.

If a profile leaves execution-relevant choices unresolved, the Command is incomplete.

## 10. Begin/End versus Change

Use Begin/End primarily for truth-valued state predicates and Relations.

Examples:

- Begin(Life(x))
- End(Life(x))
- Begin(Have(a,b))
- End(Remember(m,info))

Use Change for value-bearing Attributes.

Examples:

- Change Phase
- Change Heat
- Change Form
- Change Color

This division reduces overlap.

## 11. Change by delta

Relative change does **not** need a separate ChangeBy root.

Write the exact target value compositionally:

`Change(subject, attribute, Add(BeforeValue(attribute(subject)), delta))`

with normal dimension/value-domain checks.

This remains distinct from a simple Change-to-literal-value because the target explicitly depends on the event's pre-state snapshot.

## 12. Increase and decrease

Increase/decrease are relative Change constructions on ordered scalar attributes.

Decrease can use Opposite on a positive delta.

Example conceptually:

`Change(x, Heat, Add(BeforeValue(Heat(x)), Opposite(q)))`

lowers Heat by q.

This avoids treating OppositeHeat as Cold.

## 13. Preservation rule

Direct Change commands preserve other independent Attributes unless:

- the target profile explicitly changes them;
- consistency constraints require change;
- world laws produce downstream consequences after the commanded event.

This is the default minimal semantic scope of Change.

It does not mean the physical world freezes every other variable.

## 14. Entailed changes

If world rules say one change necessarily entails another, the resulting Event may include consequences.

Example:

changing Heat enough may naturally alter Phase. Pressure may also affect Phase or other material behavior, but those causal laws belong to the active world physics rather than to the lexical meaning of `Pressure`.

Those are world-model consequences unless the Command explicitly constrains Phase to remain unchanged.

If requested constraints conflict with unavoidable consequences, execution may become impossible or require Persist/extra Power.

## 15. Color profile

Define Color as a structured Attribute.

A ColorProfile contains at least:

- normalized Red/Green/Blue channel relation;
- total visible Light/intensity component.

Unquantified compounds such as RedGreen can denote equal included chromatic components.

Weighted colors use Ratio.

White/gray/black are then registered regions/profiles of this structure rather than mere English labels.

## 16. Black

The earlier `ZeroLight` intuition can be retained as the zero-intensity ColorProfile/visible-light condition.

At zero intensity, chromatic ratio is irrelevant/undefined.

For material optics, the world's Color/appearance model may later distinguish emitted, reflected, and transmitted light; that refinement belongs to the physics ontology.

## 17. Damage and integrity attributes

Damage may eventually be a structured Attribute rather than one Boolean Property.

A DamageProfile can contain:

- magnitude;
- location/Part;
- type;
- topology.

Whole remains a predicate computed against the structural profile.

Repair changes the Damage/structure profile toward a selected intact reference.

## 18. State transitions remain Events

Attribute Change produces EventSpecs and therefore supports:

- Sequence;
- Cause;
- Repeat;
- Persisting a target attribute value;
- Triggering on comparisons.

Example conceptually:

`Persist(Equal(Heat(x), q), duration)`

actively maintains the thermal value.

## 19. Result

The language now has a clean split:

- Property = truth-valued predicate;
- Attribute = functional value relation;
- family-member Property = convenient predicate over an Attribute value;
- Change = explicit attribute value transition;
- Begin/End = boundary transition of state predicates.

This resolves several ambiguities in Phase, Heat, Form, Color, and measurement.
