#!/usr/bin/env python3
"""Validate Batch 17 source variants, prior contour identity and original pixels."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
P=Path(__file__).resolve().parent
M=json.loads((P/"manifest.json").read_text(encoding="utf-8"))
assert M["batch"]==17 and M["external_source_ids_covered"]==272
assert M["remaining_external_source_ids"]==27 and M["no_canonical_registry_changes"]
rows=M["glyphs"]
assert [r["id"] for r in rows]==[f"R{i:03d}" for i in range(182,198)]
for row in rows:
    assert int(row["id"][1:])-int(row["alternate_ink_partner"][1:])==112
    a=ET.parse(P/row["candidate_svg"]).getroot()
    b=ET.parse(P/row["geometry_shared_from"]).getroot()
    assert a.get("viewBox")==b.get("viewBox")=="0 0 600 1000"
    assert ET.tostring(a)==ET.tostring(b),row["id"]
    assert row["style_review"]=="AWAITING_USER_REVIEW"
    assert row["final_inventory_selection"]=="UNDECIDED"
for name,count in (("runic_comparison.svg",16),("variant_pair_check.svg",32)):
    svg=(P/name).read_text(encoding="utf-8")
    ET.fromstring(svg)
    assert svg.count('href="#source"')==count and "data:image/png;base64," in svg
ET.parse(P/"batch17_adapted.svg")
assert len(list((P/"svgs").glob("R*.svg")))==16
print("PASS: Batch 17, 16 CC0 sources, SVG contour equality and comparisons")
