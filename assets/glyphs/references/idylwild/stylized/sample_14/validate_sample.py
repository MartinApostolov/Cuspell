#!/usr/bin/env python3
"""Validate source variant glyphs and source-image comparison (batch 14)."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
p=Path(__file__).resolve().parent
a=json.loads((p/"manifest.json").read_text(encoding="utf-8"))["glyphs"]
assert [x["id"] for x in a]==[f"R{i:03d}" for i in range(134,150)]
for x in a:
    mine=ET.parse(p/x["candidate_svg"]).getroot()
    other=ET.parse(p/x["geometry_shared_from"]).getroot()
    assert mine.get("viewBox")=="0 0 600 1000"
    assert [(e.tag,e.attrib) for e in mine]==[(e.tag,e.attrib) for e in other],x["id"]
sheet=(p/"runic_comparison.svg").read_text(encoding="utf-8")
assert sheet.count("<use ")==16 and "data:image/png;base64," in sheet
print("PASS: 16 sources, existing approved contours, comparison sprites")
