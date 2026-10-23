#!/usr/bin/env python3
"""Validate batch 09 candidate graphics and source comparisons."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
b=Path(__file__).resolve().parent
arr=json.loads((b/"manifest.json").read_text(encoding="utf8"))["candidates"]
assert len(arr)==16 and len({g["id"] for g in arr})==16
assert sum(x["id"].startswith("R") for x in arr)==8
assert sum(x["id"].startswith("A") for x in arr)==8
for g in arr:
    r=ET.parse(b/g["stylized_vector"]).getroot()
    assert r.attrib["viewBox"]=="0 0 600 1000"
    paths=list(r)
    assert paths and all(x.tag.endswith("path") for x in paths)
    assert all(x.attrib["stroke-width"]=="66" and x.attrib["stroke-linecap"]=="round" and x.attrib["stroke-linejoin"]=="round" for x in paths)
for name in ["runic_comparison.svg","alchemical_comparison.svg"]:
    txt=(b/name).read_text(encoding="utf8")
    assert txt.count("<use ")==8 and "data:image/png;base64," in txt
print("PASS: 16 noncanonical SVGs and two original/adapted/Cuspell comparison sheets")
