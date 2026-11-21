#!/usr/bin/env python3
"""Validate Batch 15 SVG matching, variant IDs, and original PNG comparison sprites."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
P=Path(__file__).resolve().parent
M=json.loads((P/"manifest.json").read_text(encoding="utf-8"))
items=M["glyphs"]
assert [r["id"] for r in items]==[f"R{n:03d}" for n in range(150,166)]
assert M["external_source_ids_stylized"]==240 and M["remaining_external_source_ids"]==59
assert M["canonical_registry_changed"] is False
for row in items:
    assert int(row["id"][1:])-int(row["alternate_ink_partner"][1:])==112
    a=ET.parse(P/row["candidate_svg"]).getroot()
    b=ET.parse(P/row["geometry_shared_from"]).getroot()
    assert a.get("viewBox")==b.get("viewBox")=="0 0 600 1000"
    assert ET.tostring(a)==ET.tostring(b),row["id"]
    assert row["style_review"]=="AWAITING_USER_REVIEW" and row["final_inventory_selection"]=="UNDECIDED"
for name,uses in (("runic_comparison.svg",16),("variant_pair_check.svg",32)):
    raw=(P/name).read_text(encoding="utf-8")
    ET.fromstring(raw)
    assert raw.count('href="#source"')==uses
    assert "data:image/png;base64," in raw
ET.parse(P/"batch15_adapted.svg")
assert len(list((P/"svgs").glob("R*.svg")))==16
print("PASS: Batch 15; exact approved contours, source IDs and source PNGs")
