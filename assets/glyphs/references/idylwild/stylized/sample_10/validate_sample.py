#!/usr/bin/env python3
"""Validate batch 10 (13 Runic, last 3 Alchemical candidates)."""
import json
from pathlib import Path
from xml.etree import ElementTree as ET
root=Path(__file__).resolve().parent
m=json.loads((root/"manifest.json").read_text(encoding="utf-8"))
d=m["candidates"]
assert len(d)==16 and len({x["id"] for x in d})==16
assert sum(x["id"].startswith("R") for x in d)==13
assert sum(x["id"].startswith("A") for x in d)==3
assert {x["id"] for x in d if x["id"].startswith("A")}=={"A044","A053","A075"}
for x in d:
    v=ET.parse(root/x["vector"]).getroot()
    assert v.attrib["viewBox"]=="0 0 600 1000"
    assert list(v) and all(e.tag.endswith("path") and e.attrib["stroke-width"]=="66" and e.attrib["stroke-linecap"]=="round" for e in v)
for sheet,n in (("runic_comparison.svg",13),("alchemical_comparison.svg",3)):
    text=(root/sheet).read_text(encoding="utf-8")
    assert text.count("<use ")==n
    assert "data:image/png;base64" in text
print("PASS: 16 candidate SVGs and 13+3 true-source image comparisons")
