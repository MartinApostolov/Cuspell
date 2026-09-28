from __future__ import annotations

import json
import os
from dataclasses import dataclass
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Entry:
    data: dict[str, Any]

    @property
    def surface(self) -> str:
        return self.data["surface"]

    @property
    def rune_cost(self) -> int:
        return int(self.data.get("rune_cost", 1))

    @property
    def atom_type(self) -> str | None:
        return self.data.get("atom_type")

    @property
    def frames(self) -> list[dict[str, Any]]:
        return list(self.data.get("frames", []))

    @property
    def category(self) -> str | None:
        return self.data.get("category")


class Language:
    def __init__(
        self,
        root: Path,
        types: dict[str, Any],
        lexicon: dict[str, Any],
        compounds: dict[str, Any] | None = None,
        dimensions: dict[str, Any] | None = None,
        units: dict[str, Any] | None = None,
        old_names: dict[str, Any] | None = None,
        concepts: dict[str, Any] | None = None,
        new_names: dict[str, Any] | None = None,
    ):
        self.root = root
        self.parents: dict[str, str | None] = types["parents"]
        self.entries = {item["surface"]: Entry(item) for item in lexicon["entries"]}
        self.compound_rules = list((compounds or {}).get("rules", []))
        dimension_data = dimensions or {}
        self.base_dimensions = tuple(dimension_data.get("base_dimensions", ()))
        self.dimension_vectors: dict[str, dict[str, int]] = {
            name: {base: int(exp) for base, exp in vector.items() if int(exp) != 0}
            for name, vector in dimension_data.get("dimensions", {}).items()
        }
        self._dimension_aliases: dict[tuple[tuple[str, int], ...], str] = {}
        for name, vector in self.dimension_vectors.items():
            self._dimension_aliases.setdefault(self._dimension_signature(vector), name)
        self._derived_quantity_vectors: dict[str, dict[str, int]] = {}
        self.unit_definitions: dict[str, dict[str, Any]] = {}
        for unit in (units or {}).get("units", []):
            surface = unit["surface"]
            if surface in self.entries:
                raise ValueError(f"Unit surface collides with lexicon root: {surface}")
            definition = dict(unit)
            self.unit_definitions[surface] = definition
            dimension = definition["dimension"]
            scale = definition.get("scale", {"numerator": 1, "denominator": 1})
            self.entries[surface] = Entry({
                "id": definition["id"],
                "surface": surface,
                "category": "Operator",
                "rune_cost": int(definition.get("rune_cost", 1)),
                "unit_constructor": {
                    "dimension": dimension,
                    "scale_numerator": int(scale.get("numerator", 1)),
                    "scale_denominator": int(scale.get("denominator", 1)),
                    "canonical": bool(definition.get("canonical", False)),
                },
                "frames": [{
                    "id": f"{definition['id']}.construct",
                    "normalize": "unit_quantity",
                    "output": f"Quantity:{dimension}",
                    "slots": [{"name": "amount", "type": "Quantity:Number", "required": True}],
                }],
            })
        self._root_surfaces = tuple(sorted((s for s in self.entries if s and s[0].isalpha()), key=lambda s: (-len(s), s)))

        self.world_concepts: dict[str, dict[str, Any]] = {
            item["id"]: dict(item)
            for item in (concepts or {}).get("concepts", [])
            if item.get("id")
        }
        self.old_names_by_sign: dict[str, list[dict[str, Any]]] = {}
        self.old_names_by_id: dict[str, dict[str, Any]] = {}
        for item in (old_names or {}).get("entries", []):
            copied = dict(item)
            old_id = copied.get("id")
            if old_id:
                self.old_names_by_id[str(old_id)] = copied
            sign = copied.get("sign")
            if sign:
                self.old_names_by_sign.setdefault(sign, []).append(copied)
        self.new_names_by_sign: dict[str, list[dict[str, Any]]] = {}
        for item in (new_names or {}).get("entries", []):
            sign = item.get("sign")
            if sign:
                self.new_names_by_sign.setdefault(sign, []).append(dict(item))

    @classmethod
    def load(cls, root: str | Path | None = None) -> "Language":
        root_path = cls._find_root(root)
        types_path = root_path / "language" / "core" / "types.json"
        lexicon_path = root_path / "language" / "core" / "lexicon.json"
        compounds_path = root_path / "language" / "core" / "compounds.json"
        dimensions_path = root_path / "language" / "core" / "dimensions.json"
        units_path = root_path / "language" / "core" / "units.json"
        old_names_path = root_path / "language" / "names" / "old_names.json"
        concepts_path = root_path / "world" / "core" / "concepts.json"
        new_names_path = root_path / "world" / "core" / "new_names.json"
        with types_path.open("r", encoding="utf-8") as f: types = json.load(f)
        with lexicon_path.open("r", encoding="utf-8") as f: lexicon = json.load(f)
        compounds: dict[str, Any] = {"rules": []}
        if compounds_path.exists():
            with compounds_path.open("r", encoding="utf-8") as f: compounds = json.load(f)
        dimensions: dict[str, Any] = {"base_dimensions": [], "dimensions": {}}
        if dimensions_path.exists():
            with dimensions_path.open("r", encoding="utf-8") as f: dimensions = json.load(f)
        units: dict[str, Any] = {"units": []}
        if units_path.exists():
            with units_path.open("r", encoding="utf-8") as f: units = json.load(f)
        old_names: dict[str, Any] = {"entries": []}
        if old_names_path.exists():
            with old_names_path.open("r", encoding="utf-8") as f: old_names = json.load(f)
        concepts: dict[str, Any] = {"concepts": []}
        if concepts_path.exists():
            with concepts_path.open("r", encoding="utf-8") as f: concepts = json.load(f)
        new_names: dict[str, Any] = {"entries": []}
        if new_names_path.exists():
            with new_names_path.open("r", encoding="utf-8") as f: new_names = json.load(f)
        return cls(
            root_path,
            types,
            lexicon,
            compounds,
            dimensions,
            units,
            old_names,
            concepts,
            new_names,
        )

    @staticmethod
    def _find_root(explicit: str | Path | None) -> Path:
        candidates: list[Path] = []
        if explicit is not None: candidates.append(Path(explicit).resolve())
        env = os.getenv("CUSPELL_ROOT")
        if env: candidates.append(Path(env).resolve())
        cwd = Path.cwd().resolve()
        candidates.extend([cwd, *cwd.parents]); candidates.extend(Path(__file__).resolve().parents)
        seen: set[Path] = set()
        for candidate in candidates:
            if candidate in seen: continue
            seen.add(candidate)
            if (candidate / "language" / "core" / "lexicon.json").exists(): return candidate
        raise FileNotFoundError("Could not locate Cuspell language data. Run from the repository root or set CUSPELL_ROOT.")

    def entry(self, surface: str) -> Entry | None:
        return self.entries.get(surface)

    def old_name_entries(self, sign: str) -> tuple[dict[str, Any], ...]:
        return tuple(self.old_names_by_sign.get(sign, ()))

    def new_name_entries(self, sign: str) -> tuple[dict[str, Any], ...]:
        return tuple(self.new_names_by_sign.get(sign, ()))

    def world_concept(self, concept_id: str) -> dict[str, Any] | None:
        concept = self.world_concepts.get(concept_id)
        return dict(concept) if concept is not None else None

    def old_name_cost(self, sign: str) -> int | None:
        entries = self.old_name_entries(sign)
        if not entries:
            return None
        costs = {self._old_name_entry_cost(entry) for entry in entries}
        if len(costs) != 1:
            raise ValueError(
                f"Old Name {sign!r} has inconsistent mana costs: {sorted(costs)}"
            )
        return next(iter(costs))

    def _old_name_entry_cost(
        self,
        entry: dict[str, Any],
        stack: tuple[str, ...] = (),
    ) -> int:
        old_id = str(entry.get("id", entry.get("sign", "<old-name>")))
        if old_id in stack:
            chain = " -> ".join((*stack, old_id))
            raise ValueError(f"Recursive Old Name cost dependency: {chain}")

        total = 0
        next_stack = (*stack, old_id)
        for unit in entry.get("name_units", []):
            if "root" in unit:
                root = str(unit["root"])
                cost = self.written_rune_cost(root)
                if cost is None:
                    raise ValueError(
                        f"Old Name {old_id}: unknown root unit {root!r}"
                    )
                total += cost
            elif "old_name" in unit:
                dependency_id = str(unit["old_name"])
                dependency = self.old_names_by_id.get(dependency_id)
                if dependency is None:
                    raise ValueError(
                        f"Old Name {old_id}: unknown nested Old Name "
                        f"{dependency_id!r}"
                    )
                total += self._old_name_entry_cost(dependency, next_stack)
            else:
                total += int(unit.get("mana_cost", 1))
        return total

    def resolve_entries(self, surface: str) -> list[Entry]:
        exact = self.entry(surface)
        if exact is not None: return [exact]
        return list(self.resolve_compounds(surface))

    @lru_cache(maxsize=4096)
    def known_segmentations(self, surface: str) -> tuple[tuple[str, ...], ...]:
        if not surface: return ()
        @lru_cache(maxsize=None)
        def rec(pos: int) -> tuple[tuple[str, ...], ...]:
            if pos == len(surface): return ((),)
            out: list[tuple[str, ...]] = []
            for root in self._root_surfaces:
                if surface.startswith(root, pos):
                    for tail in rec(pos + len(root)): out.append((root, *tail))
            return tuple(out)
        return tuple(seg for seg in rec(0) if len(seg) >= 2)

    @lru_cache(maxsize=4096)
    def resolve_compounds(self, surface: str) -> tuple[Entry, ...]:
        derived: dict[str, Entry] = {}
        for segmentation in self.known_segmentations(surface):
            base = tuple(self.entries[s] for s in segmentation)
            for entry in self._derive_sequence(base): derived[self._entry_signature(entry)] = entry
        return tuple(derived.values())

    def has_known_segmentation(self, surface: str) -> bool:
        return bool(self.known_segmentations(surface))

    def written_rune_cost(self, surface: str) -> int | None:
        exact = self.entry(surface)
        if exact is not None: return exact.rune_cost
        segs = self.known_segmentations(surface)
        if not segs: return None
        costs = {sum(self.entries[root].rune_cost for root in seg) for seg in segs}
        return next(iter(costs)) if len(costs)==1 else min(costs)

    def _derive_sequence(self, parts: tuple[Entry, ...]) -> tuple[Entry, ...]:
        if len(parts)==1: return parts
        out: dict[str, Entry] = {}
        for split in range(1,len(parts)):
            for left in self._derive_sequence(parts[:split]):
                for right in self._derive_sequence(parts[split:]):
                    for result in self._apply_compound_rules(left,right): out[self._entry_signature(result)] = result
        return tuple(out.values())

    def _apply_compound_rules(self,left:Entry,right:Entry)->list[Entry]:
        surface=left.surface+right.surface;out:list[Entry]=[]
        for rule in self.compound_rules:
            if not self._rule_matches(rule,left,right): continue
            result=rule.get("result")
            if result=="restricted_kind": out.append(self._make_restricted_kind(surface,left,right,rule))
            elif result=="property_conjunction": out.append(self._make_property_conjunction(surface,left,right,rule))
            elif result=="not_property": out.append(self._make_not_property(surface,left,right,rule))
            elif result=="trait_alias":
                alias=self._make_trait_alias(surface,left,right,rule)
                if alias is not None: out.append(alias)
            elif result=="state_boundary_process": out.append(self._make_state_boundary(surface,left,right,rule))
            elif result=="measured_property": out.append(self._make_measured_property(surface,left,right,rule))
        return out

    @staticmethod
    def _rule_matches(rule:dict[str,Any],left:Entry,right:Entry)->bool:
        if rule.get("left_surface") and left.surface!=rule["left_surface"]: return False
        if rule.get("right_surface") and right.surface!=rule["right_surface"]: return False
        if rule.get("left_category") and left.category!=rule["left_category"]: return False
        if rule.get("right_category") and right.category!=rule["right_category"]: return False
        trait=rule.get("right_trait")
        return not trait or bool(right.data.get(trait))

    def _make_restricted_kind(self,surface:str,left:Entry,right:Entry,rule:dict[str,Any])->Entry:
        left_expr=self.property_expr(left);right_kind=self.kind_expr(right)
        if right_kind.get("op")=="restrict_kind":
            kind_expr={"op":"restrict_kind","base":right_kind["base"],"property":self._and_property_expr(left_expr,right_kind["property"])}
        else: kind_expr={"op":"restrict_kind","base":right_kind,"property":left_expr}
        return Entry({"id":f"compound.{rule['id']}.{surface}","surface":surface,"category":"Kind","rune_cost":left.rune_cost+right.rune_cost,
          "atom_type":"Kind","derived_kind":kind_expr,"source_components":[left.surface,right.surface],
          "frames":[{"id":f"{surface}.instance","normalize":"kind_predication","output":"Proposition","slots":[{"name":"subject","type":"Entity","required":True}]}]})

    def _make_property_conjunction(self,surface:str,left:Entry,right:Entry,rule:dict[str,Any])->Entry:
        expr=self._and_property_expr(self.property_expr(left),self.property_expr(right))
        is_state=bool(left.data.get("state_predicate") and right.data.get("state_predicate"))
        data={"id":f"compound.{rule['id']}.{surface}","surface":surface,"category":"Property","rune_cost":left.rune_cost+right.rune_cost,
          "atom_type":"PropertyDescriptor","property_expr":expr,"source_components":[left.surface,right.surface],
          "frames":[{"id":f"{surface}.apply","normalize":"compound_property_apply","output":"StateProposition" if is_state else "Proposition","slots":[{"name":"subject","type":"Entity","required":True}]}]}
        if is_state: data["state_predicate"]=True
        return Entry(data)

    def _make_not_property(self,surface:str,left:Entry,right:Entry,rule:dict[str,Any])->Entry:
        expr=self._not_property_expr(self.property_expr(right))
        is_state=bool(right.data.get("state_predicate"))
        data={"id":f"compound.{rule['id']}.{surface}","surface":surface,"category":"Property","rune_cost":left.rune_cost+right.rune_cost,
          "atom_type":"PropertyDescriptor","property_expr":expr,"source_components":[left.surface,right.surface],
          "frames":[{"id":f"{surface}.apply","normalize":"compound_property_apply","output":"StateProposition" if is_state else "Proposition","slots":[{"name":"subject","type":"Entity","required":True}]}]}
        if is_state: data["state_predicate"]=True
        return Entry(data)

    def _make_trait_alias(self,surface:str,left:Entry,right:Entry,rule:dict[str,Any])->Entry|None:
        target_surface=right.data.get(rule["trait"])
        if not target_surface: return None
        target=self.entry(target_surface)
        if target is None: return None
        data=dict(target.data);data.update({"id":f"compound.{rule['id']}.{surface}","surface":surface,"rune_cost":left.rune_cost+right.rune_cost,
          "normalized_surface":target.surface,"source_components":[left.surface,right.surface]})
        return Entry(data)

    def _make_state_boundary(self,surface:str,left:Entry,right:Entry,rule:dict[str,Any])->Entry:
        state_frame=right.frames[0] if right.frames else {"slots":[{"name":"subject","type":"Entity","required":True}]}
        data={"id":f"compound.{rule['id']}.{surface}","surface":surface,"category":"Process","rune_cost":left.rune_cost+right.rune_cost,
          "boundary":rule["boundary"],"source_components":[left.surface,right.surface],
          "frames":[{"id":f"{surface}.boundary","normalize":"state_boundary","boundary":rule["boundary"],"output":"EventSpec","event_context":True,
            "slots":list(state_frame.get("slots",[]))}]}
        if right.category=="Relation":
            data["state_relation_surface"]=right.data.get("normalized_surface",right.surface)
            data["state_relation_roles"]=[slot["name"] for slot in state_frame.get("slots",[])]
        else:
            data["state_property_expr"]=self.property_expr(right)
        return Entry(data)

    def _make_measured_property(self,surface:str,left:Entry,right:Entry,rule:dict[str,Any])->Entry:
        value_type=right.data.get("descriptor_value_type")
        if not value_type:
            return Entry({"id":f"invalid.{surface}","surface":surface,"category":"Property","rune_cost":left.rune_cost+right.rune_cost})
        literal=left.data.get("literal_number")
        measured={"attribute":right.data.get("normalized_surface",right.surface),"value_type":value_type,"literal_number":literal}
        return Entry({"id":f"compound.{rule['id']}.{surface}","surface":surface,"category":"Property",
          "rune_cost":left.rune_cost+right.rune_cost,"atom_type":"PropertyDescriptor","measured_property":measured,
          "source_components":[left.surface,right.surface],
          "frames":[{"id":f"{surface}.apply","normalize":"measured_property_apply","output":"Proposition",
            "slots":[{"name":"subject","type":"Entity","required":True}]}]})

    @staticmethod
    def _entry_signature(entry:Entry)->str:
        semantic={k:entry.data.get(k) for k in ["category","atom_type","normalized_surface","property_expr","measured_property","derived_kind","boundary","state_property_expr","state_relation_surface","state_relation_roles","frames"]}
        return json.dumps(semantic,sort_keys=True,separators=(",",":"))

    def property_expr(self,entry:Entry)->dict[str,Any]:
        if "property_expr" in entry.data: return entry.data["property_expr"]
        literal=dict(entry.data.get("property_literal") or {});literal.setdefault("surface",entry.data.get("normalized_surface",entry.surface))
        return {"op":"atom",**literal}

    def kind_expr(self,entry:Entry)->dict[str,Any]:
        if "derived_kind" in entry.data: return entry.data["derived_kind"]
        return {"op":"kind","surface":entry.data.get("normalized_surface",entry.surface)}

    def _and_property_expr(self,a:dict[str,Any],b:dict[str,Any])->dict[str,Any]:
        items=[]
        for value in (a,b):
            if value.get("op")=="and": items.extend(value["args"])
            else: items.append(value)
        items.sort(key=lambda x:json.dumps(x,sort_keys=True,separators=(",",":")))
        return {"op":"and","args":items}

    def _not_property_expr(self,expr:dict[str,Any])->dict[str,Any]:
        return expr["arg"] if expr.get("op")=="not" else {"op":"not","arg":expr}

    @staticmethod
    def _dimension_signature(vector: dict[str, int]) -> tuple[tuple[str, int], ...]:
        return tuple(sorted((name, int(exp)) for name, exp in vector.items() if int(exp) != 0))

    def quantity_dimension_vector(self, quantity_type: str) -> dict[str, int] | None:
        if not quantity_type.startswith("Quantity:"):
            return None
        name = quantity_type.split(":", 1)[1]
        registered = self.dimension_vectors.get(name)
        if registered is not None:
            return dict(registered)
        derived = self._derived_quantity_vectors.get(quantity_type)
        return dict(derived) if derived is not None else None

    def quantity_type_for_vector(self, vector: dict[str, int]) -> str:
        normalized = {name: int(exp) for name, exp in vector.items() if int(exp) != 0}
        signature = self._dimension_signature(normalized)
        alias = self._dimension_aliases.get(signature)
        if alias is not None:
            return f"Quantity:{alias}"

        order = {name: index for index, name in enumerate(self.base_dimensions)}
        names = sorted(normalized, key=lambda name: (order.get(name, len(order)), name))
        encoded = "_".join(
            f"{name}{'P' if normalized[name] > 0 else 'N'}{abs(normalized[name])}"
            for name in names
        )
        quantity_type = f"Quantity:Dim_{encoded or 'Number'}"
        self._derived_quantity_vectors[quantity_type] = normalized
        return quantity_type

    def combine_quantity_types(self, left: str, right: str, operation: str) -> str:
        left_vector = self.quantity_dimension_vector(left)
        right_vector = self.quantity_dimension_vector(right)
        if left_vector is None or right_vector is None:
            return "Quantity"

        result = dict(left_vector)
        sign = 1 if operation == "multiply" else -1 if operation == "divide" else None
        if sign is None:
            raise ValueError(f"Unsupported dimension operation: {operation}")
        for name, exponent in right_vector.items():
            result[name] = result.get(name, 0) + sign * exponent
            if result[name] == 0:
                del result[name]
        return self.quantity_type_for_vector(result)

    def scale_quantity_dimension(
        self,
        quantity_type: str,
        factor: Fraction,
    ) -> str | None:
        vector = self.quantity_dimension_vector(quantity_type)
        if vector is None:
            return "Quantity"
        result: dict[str, int] = {}
        for name, exponent in vector.items():
            scaled = Fraction(exponent) * factor
            if scaled.denominator != 1:
                return None
            if scaled.numerator:
                result[name] = scaled.numerator
        return self.quantity_type_for_vector(result)

    def is_assignable(self,actual:str,expected:str)->bool:
        if expected in {"Any","SemanticValue"}: return True
        if actual==expected: return True
        if expected=="Quantity" and (actual=="Quantity" or actual.startswith("Quantity:")): return True
        if actual.startswith("Quantity:") and expected.startswith("Quantity:"):
            actual_vector=self.quantity_dimension_vector(actual)
            expected_vector=self.quantity_dimension_vector(expected)
            if actual_vector is not None and expected_vector is not None:
                return self._dimension_signature(actual_vector)==self._dimension_signature(expected_vector)
        if actual.startswith("Collection:") and expected=="Collection": return True
        if actual.startswith("Collection:") and expected.startswith("Collection:"):
            return self.is_assignable(actual.split(":",1)[1], expected.split(":",1)[1])
        if actual.startswith("Sequence:") and expected in {"Sequence","Collection"}: return True
        if actual.startswith("Sequence:") and expected.startswith("Sequence:"):
            return self.is_assignable(actual.split(":",1)[1], expected.split(":",1)[1])
        if actual.startswith("Sequence:") and expected.startswith("Collection:"):
            return self.is_assignable(actual.split(":",1)[1], expected.split(":",1)[1])
        current=actual;visited:set[str]=set()
        while current and current not in visited:
            visited.add(current);current=self.parents.get(current)
            if current==expected: return True
        return False
