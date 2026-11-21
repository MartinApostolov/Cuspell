#!/usr/bin/env python3
"""Validate R166–R181 source variants, approved-vector equality and source comparisons."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
P=Path(__file__).resolve().parent
M=json.loads((P/"manifest.json").read_text(encoding="utf-8"))
assert M["batch"]==16 and M["external_source_ids_stylized"]==256
assert M["remaining_external_source_ids"]==43 and M["canonical_registry_changed"] is False
rows=M["glyphs"]
assert [r["id"] for r in rows]==[f"R{i:03d}" for i in range(166,182)]
for r in rows:
    assert int(r["id"][1:])-int(r["alternate_ink_partner"][1:])==112
    a=ET.parse(P/r["candidate_svg"]).getroot()
    b=ET.parse(P/r["geometry_shared_from"]).getroot()
    assert a.get("viewBox")==b.get("viewBox")=="0 0 600 1000"
    assert ET.tostring(a)==ET.tostring(b),r["id"]
    assert r["style_review"]=="AWAITING_USER_REVIEW" and r["final_inventory_selection"]=="UNDECIDED"
for name,n in (("runic_comparison.svg",16),("variant_pair_check.svg",32)):
    s=(P/name).read_text(encoding="utf-8")
    ET.fromstring(s)
    assert s.count('href="#source"')==n and "data:image/png;base64," in s
ET.parse(P/"batch16_adapted.svg")
assert len(list((P/"svgs").glob("R*.svg")))==16
print("PASS: 16 Runic alternate IDs, source pixels, exact approved contours")
