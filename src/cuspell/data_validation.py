from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ALLOWED_CATEGORIES={
    "Entity","Kind","Property","Relation","Process","Quantity","Reference","Operator"
}
ALLOWED_COMPOUND_RESULTS={
    "restricted_kind","property_conjunction","not_property","trait_alias","state_boundary_process"
}


def validate_language_data(root: str|Path) -> list[str]:
    root=Path(root)
    with (root/"language/core/types.json").open(encoding="utf-8") as f:
        types=json.load(f)
    with (root/"language/core/lexicon.json").open(encoding="utf-8") as f:
        lex=json.load(f)
    with (root/"language/core/compounds.json").open(encoding="utf-8") as f:
        compounds=json.load(f)

    errors:list[str]=[]
    parents:dict[str,str|None]=types.get("parents",{})
    known_types=set(parents)
    entries=lex.get("entries",[])

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
            strategies=sum(key in frame for key in ("output","output_from_arg","output_member_of_arg"))
            if strategies!=1:
                errors.append(f"{frame_label}: expected exactly one output strategy")
            if "output" in frame and not _known_type(frame["output"],known_types):
                errors.append(f"{frame_label}: unknown output type {frame['output']}")
            for slot in frame.get("slots",[]):
                if not slot.get("name"):
                    errors.append(f"{frame_label}: slot without name")
                spec=slot.get("type")
                if not spec:
                    errors.append(f"{frame_label}: slot {slot.get('name')} lacks type")
                elif not _known_type_spec(spec,known_types):
                    errors.append(f"{frame_label}: slot {slot.get('name')} has unknown type spec {spec}")

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
    if name.startswith("Collection:"):
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
