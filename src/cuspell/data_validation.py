from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ALLOWED_CATEGORIES={
    "Entity","Kind","Property","Relation","Process","Quantity","Reference","Operator"
}
ALLOWED_COMPOUND_RESULTS={
    "restricted_kind","property_conjunction","not_property","trait_alias","state_boundary_process","measured_property"
}


def validate_language_data(root: str|Path) -> list[str]:
    root=Path(root)
    with (root/"language/core/types.json").open(encoding="utf-8") as f:
        types=json.load(f)
    with (root/"language/core/lexicon.json").open(encoding="utf-8") as f:
        lex=json.load(f)
    with (root/"language/core/compounds.json").open(encoding="utf-8") as f:
        compounds=json.load(f)
    dimensions_path=root/"language/core/dimensions.json"
    dimensions={"base_dimensions":[],"dimensions":{}}
    if dimensions_path.exists():
        with dimensions_path.open(encoding="utf-8") as f:
            dimensions=json.load(f)
    units_path=root/"language/core/units.json"
    units={"units":[]}
    if units_path.exists():
        with units_path.open(encoding="utf-8") as f:
            units=json.load(f)
    old_names_path=root/"language/names/old_names.json"
    old_names={"entries":[]}
    if old_names_path.exists():
        with old_names_path.open(encoding="utf-8") as f:
            old_names=json.load(f)
    concepts_path=root/"world/core/concepts.json"
    concepts={"concepts":[]}
    if concepts_path.exists():
        with concepts_path.open(encoding="utf-8") as f:
            concepts=json.load(f)
    new_names_path=root/"world/core/new_names.json"
    new_names={"entries":[]}
    if new_names_path.exists():
        with new_names_path.open(encoding="utf-8") as f:
            new_names=json.load(f)

    errors:list[str]=[]
    parents:dict[str,str|None]=types.get("parents",{})
    known_types=set(parents)
    entries=lex.get("entries",[])

    base_dimensions=dimensions.get("base_dimensions",[])
    _duplicates(base_dimensions,"base dimension",errors)
    dimension_vectors=dimensions.get("dimensions",{})
    for dimension_name, vector in dimension_vectors.items():
        if not isinstance(vector,dict):
            errors.append(f"dimension {dimension_name}: vector must be an object")
            continue
        for base, exponent in vector.items():
            if base not in base_dimensions:
                errors.append(f"dimension {dimension_name}: unknown base dimension {base!r}")
            if not isinstance(exponent,int):
                errors.append(f"dimension {dimension_name}: exponent for {base} must be an integer")

    registered_quantity_dimensions={
        name.split(":",1)[1]
        for name,parent in parents.items()
        if name.startswith("Quantity:") and parent=="Quantity"
    }
    for dimension_name in sorted(registered_quantity_dimensions):
        if dimension_name not in dimension_vectors:
            errors.append(f"quantity type Quantity:{dimension_name} lacks a registered dimension vector")
    for dimension_name in sorted(dimension_vectors):
        if f"Quantity:{dimension_name}" not in parents:
            errors.append(f"dimension {dimension_name} lacks registered type Quantity:{dimension_name}")

    unit_entries=units.get("units",[])
    unit_ids=[u.get("id") for u in unit_entries]
    unit_old_name_ids=[u.get("old_name_id") for u in unit_entries]
    _duplicates(unit_ids,"unit id",errors)
    _duplicates(unit_old_name_ids,"unit old_name_id",errors)
    unit_by_id={
        str(u.get("id")):u
        for u in unit_entries
        if u.get("id")
    }
    raw_old_ids={
        str(item.get("id"))
        for item in old_names.get("entries",[])
        if item.get("id")
    }
    canonical_by_dimension:dict[str,int]={}
    for unit in unit_entries:
        label=unit.get("id") or "<unit>"
        old_name_id=unit.get("old_name_id")
        if not isinstance(old_name_id,str) or not old_name_id:
            errors.append(f"{label}: unit needs an old_name_id")
        elif old_name_id not in raw_old_ids:
            errors.append(f"{label}: unknown unit Old Name {old_name_id!r}")
        dimension=unit.get("dimension")
        if dimension not in dimension_vectors:
            errors.append(f"{label}: unknown unit dimension {dimension!r}")
        elif f"Quantity:{dimension}" not in parents:
            errors.append(f"{label}: unit dimension {dimension} lacks registered quantity type")
        scale=unit.get("scale")
        if not isinstance(scale,dict):
            errors.append(f"{label}: unit scale must be an object")
        else:
            numerator=scale.get("numerator")
            denominator=scale.get("denominator")
            if not isinstance(numerator,int) or not isinstance(denominator,int):
                errors.append(f"{label}: unit scale numerator/denominator must be integers")
            elif denominator==0:
                errors.append(f"{label}: unit scale denominator cannot be zero")
        if unit.get("canonical"):
            canonical_by_dimension[str(dimension)]=canonical_by_dimension.get(str(dimension),0)+1
            if isinstance(scale,dict) and scale.get("numerator")==1 and scale.get("denominator")==1:
                pass
            else:
                errors.append(f"{label}: canonical unit must have scale 1/1")
    for dimension,count in canonical_by_dimension.items():
        if count>1:
            errors.append(f"dimension {dimension}: multiple canonical units")

    ids=[e.get("id") for e in entries]
    surfaces=[e.get("surface") for e in entries]
    _duplicates(ids,"entry id",errors)
    _duplicates(surfaces,"surface",errors)

    by_surface={e.get("surface"):e for e in entries if e.get("surface")}
    frame_ids:list[str]=[]

    for entry in entries:
        label=entry.get("surface") or entry.get("id") or "<entry>"
        category=entry.get("category")
        if category not in ALLOWED_CATEGORIES:
            errors.append(f"{label}: unknown category {category!r}")

        atom=entry.get("atom_type")
        if atom and not _known_type(atom,known_types):
            errors.append(f"{label}: unknown atom_type {atom}")

        descriptor_type=entry.get("descriptor_value_type")
        if descriptor_type and not _known_type(descriptor_type,known_types):
            errors.append(f"{label}: unknown descriptor_value_type {descriptor_type}")
        if atom=="AttributeDescriptor" and not descriptor_type:
            errors.append(f"{label}: AttributeDescriptor lacks descriptor_value_type")

        for trait in ("reversible_to","converse_to"):
            target=entry.get(trait)
            if target and target not in by_surface:
                errors.append(f"{label}: {trait} target {target!r} is not a registered root")

        frames=entry.get("frames",[])
        if entry.get("state_predicate") and frames:
            for frame in frames:
                if frame.get("output") not in {"StateProposition",None}:
                    errors.append(f"{label}/{frame.get('id')}: state_predicate frame should output StateProposition")

        for frame in frames:
            frame_label=f"{label}/{frame.get('id','<frame>')}"
            if frame.get("id"):
                frame_ids.append(frame["id"])
            strategies=sum(key in frame for key in ("output","output_from_arg","output_member_of_arg","output_dimension_op","output_attribute_dimension_op","output_quantity_dimension_op","output_partition_of_arg","output_sequence_of_arg"))
            if strategies!=1:
                errors.append(f"{frame_label}: expected exactly one output strategy")
            if "output" in frame and not _known_type(frame["output"],known_types):
                errors.append(f"{frame_label}: unknown output type {frame['output']}")
            slots=frame.get("slots",[])
            utterance_context=frame.get("utterance_context")
            if utterance_context is not None:
                if not isinstance(utterance_context,dict):
                    errors.append(f"{frame_label}: utterance_context must be an object")
                else:
                    slot_names={slot.get("name") for slot in frame.get("slots",[])}
                    for key in ("speaker_role","content_role","addressee_role"):
                        role=utterance_context.get(key)
                        if role is not None and role not in slot_names:
                            errors.append(f"{frame_label}: utterance_context {key} references missing role {role!r}")
            for slot_index, slot in enumerate(slots):
                if not slot.get("name"):
                    errors.append(f"{frame_label}: slot without name")
                spec=slot.get("type")
                if not spec:
                    errors.append(f"{frame_label}: slot {slot.get('name')} lacks type")
                elif not _known_type_spec(spec,known_types):
                    errors.append(f"{frame_label}: slot {slot.get('name')} has unknown type spec {spec}")
                named_only=slot.get("named_only")
                if named_only is not None and not isinstance(named_only,bool):
                    errors.append(f"{frame_label}: slot {slot.get('name')} named_only must be boolean")
                value_domain=slot.get("value_domain")
                if value_domain is not None and value_domain not in {"nonnegative","positive","positive_integer","nonnegative_integer"}:
                    errors.append(f"{frame_label}: slot {slot.get('name')} has unsupported value_domain {value_domain!r}")
                domain_role=slot.get("value_domain_from_role")
                if domain_role is not None and not any(s.get("name")==domain_role for s in slots):
                    errors.append(f"{frame_label}: slot {slot.get('name')} references unknown value-domain role {domain_role!r}")
                source_role=slot.get("binds_member_of_role")
                if source_role:
                    if spec!="Binder":
                        errors.append(f"{frame_label}: slot {slot.get('name')} uses binds_member_of_role but is not a Binder")
                    source_index=next((i for i,s in enumerate(slots) if s.get("name")==source_role),None)
                    if source_index is None:
                        errors.append(f"{frame_label}: slot {slot.get('name')} references unknown collection role {source_role!r}")
                    else:
                        source_spec=slots[source_index].get("type","")
                        if source_spec!="Collection" and not source_spec.startswith("Collection:"):
                            errors.append(f"{frame_label}: role {source_role} is not collection-typed")
                        if source_index>=slot_index:
                            errors.append(f"{frame_label}: collection role {source_role} must precede binder slot {slot.get('name')}")

            sequence_arg=frame.get("output_sequence_of_arg")
            if sequence_arg is not None:
                if not isinstance(sequence_arg,int) or sequence_arg<0 or sequence_arg>=len(slots):
                    errors.append(f"{frame_label}: output_sequence_of_arg references a missing slot")
                else:
                    spec=slots[sequence_arg].get("type","")
                    if spec!="Collection" and not spec.startswith("Collection:"):
                        errors.append(f"{frame_label}: sequence source slot is not Collection-typed")

            partition_arg=frame.get("output_partition_of_arg")
            if partition_arg is not None:
                if not isinstance(partition_arg,int) or partition_arg<0 or partition_arg>=len(slots):
                    errors.append(f"{frame_label}: output_partition_of_arg references a missing slot")
                else:
                    spec=slots[partition_arg].get("type","")
                    if spec!="Collection" and not spec.startswith("Collection:"):
                        errors.append(f"{frame_label}: partition source slot is not Collection-typed")

            quantity_dimension_op=frame.get("output_quantity_dimension_op")
            if quantity_dimension_op is not None:
                if not isinstance(quantity_dimension_op,dict):
                    errors.append(f"{frame_label}: output_quantity_dimension_op must be an object")
                else:
                    operation=quantity_dimension_op.get("op")
                    if operation!="divide_time":
                        errors.append(f"{frame_label}: unsupported quantity dimension operation {operation!r}")
                    value_arg=quantity_dimension_op.get("arg",0)
                    if not isinstance(value_arg,int) or value_arg<0 or value_arg>=len(slots):
                        errors.append(f"{frame_label}: output_quantity_dimension_op references a missing quantity slot")
                    else:
                        spec=slots[value_arg].get("type","")
                        if spec!="Quantity" and not spec.startswith("Quantity:") and not spec.startswith("$"):
                            errors.append(f"{frame_label}: output_quantity_dimension_op source slot must be quantity-typed")

            attribute_dimension_op=frame.get("output_attribute_dimension_op")
            if attribute_dimension_op is not None:
                if not isinstance(attribute_dimension_op,dict):
                    errors.append(f"{frame_label}: output_attribute_dimension_op must be an object")
                else:
                    operation=attribute_dimension_op.get("op")
                    if operation!="divide_time":
                        errors.append(f"{frame_label}: unsupported attribute dimension operation {operation!r}")
                    attribute_arg=attribute_dimension_op.get("attribute_arg",0)
                    if not isinstance(attribute_arg,int) or attribute_arg<0 or attribute_arg>=len(slots):
                        errors.append(f"{frame_label}: output_attribute_dimension_op references a missing attribute slot")
                    elif slots[attribute_arg].get("type")!="AttributeDescriptor":
                        errors.append(f"{frame_label}: output_attribute_dimension_op attribute slot must be AttributeDescriptor")

            dimension_op=frame.get("output_dimension_op")
            if dimension_op is not None:
                if not isinstance(dimension_op,dict):
                    errors.append(f"{frame_label}: output_dimension_op must be an object")
                else:
                    operation=dimension_op.get("op")
                    if operation not in {"multiply","divide","power","root"}:
                        errors.append(f"{frame_label}: unsupported dimension operation {operation!r}")
                    arg_indices=dimension_op.get("args")
                    if not isinstance(arg_indices,list) or len(arg_indices)!=2 or not all(isinstance(i,int) for i in arg_indices):
                        errors.append(f"{frame_label}: output_dimension_op args must be two integer slot indices")
                    elif any(i<0 or i>=len(slots) for i in arg_indices):
                        errors.append(f"{frame_label}: output_dimension_op references a missing slot")
                    else:
                        for i in arg_indices:
                            spec=slots[i].get("type","")
                            if spec!="Quantity" and not spec.startswith("Quantity:") and not spec.startswith("$"):
                                errors.append(f"{frame_label}: dimension operation slot {slots[i].get('name')} is not quantity-typed")

    _duplicates(frame_ids,"frame id",errors)

    for rule in compounds.get("rules",[]):
        rid=rule.get("id","<rule>")
        result=rule.get("result")
        if result not in ALLOWED_COMPOUND_RESULTS:
            errors.append(f"compound {rid}: unsupported result {result!r}")
        left=rule.get("left_surface")
        right=rule.get("right_surface")
        if left and left not in by_surface:
            errors.append(f"compound {rid}: unknown left_surface {left!r}")
        if right and right not in by_surface:
            errors.append(f"compound {rid}: unknown right_surface {right!r}")
        for key in ("left_category","right_category"):
            if rule.get(key) and rule[key] not in ALLOWED_CATEGORIES:
                errors.append(f"compound {rid}: unknown {key} {rule[key]!r}")

    # World concepts and historical/current naming data.
    concept_entries=concepts.get("concepts",[])
    concept_ids=[item.get("id") for item in concept_entries]
    _duplicates(concept_ids,"world concept id",errors)
    concept_by_id={item.get("id"):item for item in concept_entries if item.get("id")}
    for concept in concept_entries:
        label=concept.get("id") or "<concept>"
        semantic_type=concept.get("semantic_type")
        if not semantic_type or not _known_type(str(semantic_type),known_types):
            errors.append(f"{label}: unknown or missing semantic_type {semantic_type!r}")

    old_entries=old_names.get("entries",[])
    _duplicates([item.get("id") for item in old_entries],"Old Name id",errors)
    old_by_id={
        str(item.get("id")):item
        for item in old_entries
        if item.get("id")
    }

    for item in old_entries:
        label=item.get("id") or item.get("sign") or "<Old Name>"
        sign=item.get("sign")
        if not isinstance(sign,str) or not sign:
            errors.append(f"{label}: Old Name sign must be a non-empty string")
            continue
        if item.get("established_before_magic") is not True:
            errors.append(f"{label}: Old Name must be established_before_magic=true")

        units_list=item.get("name_units")
        if not isinstance(units_list,list) or not units_list:
            errors.append(f"{label}: Old Name needs at least one name_unit")
            units_list=[]
        for unit in units_list:
            if not isinstance(unit,dict):
                errors.append(f"{label}: name_unit must be an object")
                continue
            unit_kinds=[key for key in ("root","sign","old_name") if key in unit]
            if len(unit_kinds)!=1:
                errors.append(
                    f"{label}: each name_unit needs exactly one of "
                    "root/sign/old_name"
                )
                continue
            kind=unit_kinds[0]
            if kind=="root":
                root_surface=unit.get("root")
                if root_surface not in by_surface:
                    errors.append(f"{label}: unknown root name_unit {root_surface!r}")
            elif kind=="sign":
                mana_cost=unit.get("mana_cost",1)
                if not isinstance(mana_cost,int) or mana_cost<=0:
                    errors.append(
                        f"{label}: historical sign name_unit mana_cost "
                        "must be positive integer"
                    )
            else:
                dependency_id=unit.get("old_name")
                if not isinstance(dependency_id,str) or not dependency_id:
                    errors.append(f"{label}: old_name name_unit needs an Old Name id")
                elif dependency_id not in old_by_id:
                    errors.append(
                        f"{label}: unknown nested Old Name {dependency_id!r}"
                    )

        meaning=item.get("meaning")
        if not isinstance(meaning,dict):
            errors.append(f"{label}: Old Name meaning must be an object")
            continue
        meaning_kind=meaning.get("kind")
        semantic_type=meaning.get("type")
        if not semantic_type or not _known_type(str(semantic_type),known_types):
            errors.append(f"{label}: Old Name has unknown meaning type {semantic_type!r}")
        if meaning_kind=="concept":
            concept_id=meaning.get("concept_id")
            concept=concept_by_id.get(concept_id)
            if concept is None:
                errors.append(f"{label}: unknown world concept {concept_id!r}")
            elif semantic_type and concept.get("semantic_type")!=semantic_type:
                errors.append(
                    f"{label}: meaning type {semantic_type} does not match concept "
                    f"type {concept.get('semantic_type')}"
                )
        elif meaning_kind=="expression":
            if not isinstance(meaning.get("source"),str) or not meaning.get("source","").strip():
                errors.append(f"{label}: expression Old Name needs non-empty source")
        elif meaning_kind=="unit":
            if semantic_type!="Unit":
                errors.append(f"{label}: Unit Old Name must have meaning type 'Unit'")
            unit_id=meaning.get("unit_id")
            unit=unit_by_id.get(str(unit_id)) if unit_id is not None else None
            if unit is None:
                errors.append(f"{label}: unknown Unit definition {unit_id!r}")
            elif unit.get("old_name_id")!=item.get("id"):
                errors.append(
                    f"{label}: Unit definition {unit_id!r} points to "
                    f"{unit.get('old_name_id')!r}, not this Old Name"
                )
        else:
            errors.append(f"{label}: unsupported Old Name meaning kind {meaning_kind!r}")

    old_cost_cache:dict[str,int|None]={}
    old_cycle_reports:set[tuple[str,...]]=set()

    def old_name_cost(old_id:str,stack:tuple[str,...]=())->int|None:
        if old_id in old_cost_cache:
            return old_cost_cache[old_id]
        if old_id in stack:
            cycle=(*stack[stack.index(old_id):],old_id)
            if cycle not in old_cycle_reports:
                old_cycle_reports.add(cycle)
                errors.append(
                    "Old Name dependency cycle: " + " -> ".join(cycle)
                )
            return None
        item=old_by_id.get(old_id)
        if item is None:
            return None
        total=0
        valid=True
        next_stack=(*stack,old_id)
        units_list=item.get("name_units")
        if not isinstance(units_list,list):
            old_cost_cache[old_id]=None
            return None
        for unit in units_list:
            if not isinstance(unit,dict):
                valid=False
                continue
            if "root" in unit and len([k for k in ("root","sign","old_name") if k in unit])==1:
                root_surface=unit.get("root")
                root_entry=by_surface.get(root_surface)
                if root_entry is None:
                    valid=False
                else:
                    total+=int(root_entry.get("rune_cost",1))
            elif "sign" in unit and len([k for k in ("root","sign","old_name") if k in unit])==1:
                mana_cost=unit.get("mana_cost",1)
                if not isinstance(mana_cost,int) or mana_cost<=0:
                    valid=False
                else:
                    total+=mana_cost
            elif "old_name" in unit and len([k for k in ("root","sign","old_name") if k in unit])==1:
                dependency_id=unit.get("old_name")
                if not isinstance(dependency_id,str) or dependency_id not in old_by_id:
                    valid=False
                else:
                    nested=old_name_cost(dependency_id,next_stack)
                    if nested is None:
                        valid=False
                    else:
                        total+=nested
            else:
                valid=False
        old_cost_cache[old_id]=total if valid else None
        return old_cost_cache[old_id]

    old_cost_by_sign:dict[str,set[int]]={}
    for item in old_entries:
        old_id=item.get("id")
        sign=item.get("sign")
        if not old_id or not isinstance(sign,str) or not sign:
            continue
        cost=old_name_cost(str(old_id))
        if cost is not None:
            old_cost_by_sign.setdefault(sign,set()).add(cost)

    for sign,costs in old_cost_by_sign.items():
        if len(costs)>1:
            errors.append(f"Old Name sign {sign!r} has inconsistent mana costs {sorted(costs)}")

    new_entries=new_names.get("entries",[])
    _duplicates([item.get("id") for item in new_entries],"New Name id",errors)
    for item in new_entries:
        label=item.get("id") or item.get("sign") or "<New Name>"
        sign=item.get("sign")
        if not isinstance(sign,str) or not sign:
            errors.append(f"{label}: New Name sign must be a non-empty string")
        referent_type=item.get("referent_type")
        if not referent_type or not _known_type(str(referent_type),known_types):
            errors.append(f"{label}: New Name has unknown referent_type {referent_type!r}")
        if not isinstance(item.get("referent_id"),str) or not item.get("referent_id"):
            errors.append(f"{label}: New Name needs a referent_id")

    # Validate optional world-specific packages (for example world/yona)
    # against the same type system without merging them into the default world.
    world_root=root/"world"
    if world_root.exists():
        core_concept_ids=set(concept_by_id)
        core_new_ids={item.get("id") for item in new_entries if item.get("id")}
        for package_dir in sorted(
            (p for p in world_root.iterdir() if p.is_dir() and p.name!="core"),
            key=lambda p:p.name,
        ):
            package_concepts_path=package_dir/"concepts.json"
            package_names_path=package_dir/"new_names.json"
            package_concepts={"concepts":[]}
            package_names={"entries":[]}
            if package_concepts_path.exists():
                with package_concepts_path.open(encoding="utf-8") as f:
                    package_concepts=json.load(f)
            if package_names_path.exists():
                with package_names_path.open(encoding="utf-8") as f:
                    package_names=json.load(f)

            package_label=f"world/{package_dir.name}"
            package_concept_entries=package_concepts.get("concepts",[])
            package_concept_ids=[item.get("id") for item in package_concept_entries]
            _duplicates(package_concept_ids,f"{package_label} concept id",errors)
            for concept_id in package_concept_ids:
                if concept_id in core_concept_ids:
                    errors.append(
                        f"{package_label}: concept id {concept_id!r} collides with core world concept"
                    )
            package_concept_by_id={
                item.get("id"):item
                for item in package_concept_entries
                if item.get("id")
            }
            for concept in package_concept_entries:
                label=concept.get("id") or f"{package_label}/<concept>"
                semantic_type=concept.get("semantic_type")
                if not semantic_type or not _known_type(str(semantic_type),known_types):
                    errors.append(
                        f"{label}: unknown or missing semantic_type {semantic_type!r}"
                    )

            package_new_entries=package_names.get("entries",[])
            _duplicates(
                [item.get("id") for item in package_new_entries],
                f"{package_label} New Name id",
                errors,
            )
            known_referents={**concept_by_id,**package_concept_by_id}
            for item in package_new_entries:
                label=item.get("id") or item.get("sign") or f"{package_label}/<New Name>"
                if item.get("id") in core_new_ids:
                    errors.append(
                        f"{package_label}: New Name id {item.get('id')!r} collides with core"
                    )
                sign=item.get("sign")
                if not isinstance(sign,str) or not sign:
                    errors.append(f"{label}: New Name sign must be a non-empty string")
                referent_type=item.get("referent_type")
                if not referent_type or not _known_type(str(referent_type),known_types):
                    errors.append(
                        f"{label}: New Name has unknown referent_type {referent_type!r}"
                    )
                referent_id=item.get("referent_id")
                if not isinstance(referent_id,str) or not referent_id:
                    errors.append(f"{label}: New Name needs a referent_id")
                    continue
                referent=known_referents.get(referent_id)
                if referent is None:
                    errors.append(
                        f"{label}: New Name referent {referent_id!r} is not a registered "
                        f"core/{package_dir.name} concept"
                    )
                elif referent_type and referent.get("semantic_type")!=referent_type:
                    errors.append(
                        f"{label}: referent_type {referent_type} does not match "
                        f"{referent_id} type {referent.get('semantic_type')}"
                    )

    return errors


def _duplicates(values:list[Any],label:str,errors:list[str])->None:
    seen=set()
    duplicates=set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    for value in sorted((x for x in duplicates if x is not None),key=str):
        errors.append(f"duplicate {label}: {value}")


def _known_type(name:str,known:set[str])->bool:
    if name in known:
        return True
    if name.startswith("Collection:") or name.startswith("Sequence:"):
        return _known_type(name.split(":",1)[1],known)
    return False


def _known_type_spec(spec:str,known:set[str])->bool:
    if spec in {"$output"}:
        return True
    if spec.startswith("$attribute:"):
        return spec.split(":",1)[1].isdigit()
    if spec.startswith("$") and spec[1:].isdigit():
        return True
    return _known_type(spec,known)
