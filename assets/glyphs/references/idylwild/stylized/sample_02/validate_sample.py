#!/usr/bin/env python3
"""Check batch 02 editable SVG candidates without touching canonical Cuspell."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET
base=Path(__file__).resolve().parent
m=json.loads((base/"manifest.json").read_text(encoding="utf-8"))
items=m["samples"]
assert len(items)==16 and len({s["id"] for s in items})==16
assert sum(s["id"].startswith("R") for s in items)==8
assert sum(s["id"].startswith("A") for s in items)==8
for s in items:
    root=ET.parse(base/s["svg"]).getroot()
    assert root.attrib["viewBox"]=="0 0 600 1000"
    paths=[x for x in root if x.tag.endswith("path")]
    assert paths
    for p in paths:
        assert p.get("stroke-width")=="66" and p.get("stroke-linecap")=="round"
        assert p.get("fill")=="none" and p.get("d","").startswith("M ")
assert (base/"runic_comparison.svg").exists()
assert (base/"alchemical_comparison.svg").exists()
print("PASS: 16 noncanonical candidate SVGs, provenance IDs, layout and stroke attributes.")
