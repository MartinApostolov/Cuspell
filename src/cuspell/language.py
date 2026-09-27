from __future__ import annotations

import json
import os
from dataclasses import dataclass
from functools import lru_cache
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
    def __init__(self, root: Path, types: dict[str, Any], lexicon: dict[str, Any], compounds: dict[str, Any] | None = None):
        self.root = root
        self.parents: dict[str, str | None] = types["parents"]
        self.entries = {item["surface"]: Entry(item) for item in lexicon["entries"]}
        self.compound_rules = list((compounds or {}).get("rules", []))
        self._root_surfaces = tuple(sorted((s for s in self.entries if s and s[0].isalpha()), key=lambda s: (-len(s), s)))

    @classmethod
    def load(cls, root: str | Path | None = None) -> "Language":
        root_path = cls._find_root(root)
        types_path = root_path / "language" / "core" / "types.json"
        lexicon_path = root_path / "language" / "core" / "lexicon.json"
        compounds_path = root_path / "language" / "core" / "compounds.json"
        with types_path.open("r", encoding="utf-8") as f: types = json.load(f)
        with lexicon_path.open("r", encoding="utf-8") as f: lexicon = json.load(f)
        compounds: dict[str, Any] = {"rules": []}
        if compounds_path.exists():
            with compounds_path.open("r", encoding="utf-8") as f: compounds = json.load(f)
        return cls(root_path, types, lexicon, compounds)

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

    def is_assignable(self,actual:str,expected:str)->bool:
        if expected in {"Any","SemanticValue"}: return True
        if actual==expected: return True
        if actual.startswith("Collection:") and expected=="Collection": return True
        if actual.startswith("Collection:") and expected.startswith("Collection:"):
            return self.is_assignable(actual.split(":",1)[1], expected.split(":",1)[1])
        current=actual;visited:set[str]=set()
        while current and current not in visited:
            visited.add(current);current=self.parents.get(current)
            if current==expected: return True
        return False
