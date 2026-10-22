#!/usr/bin/env python3
"""Check batch 05 source IDs, vector paths, and side-by-side sprites."""
from pathlib import Path
import json, xml.etree.ElementTree as ET
b=Path(__file__).resolve().parent
m=json.loads((b/"manifest.json").read_text(encoding="utf-8"))
d=m["decisions"]
assert len(d)==16 and len({x["id"] for x in d})==16
assert sum(x["id"].startswith("R") for x in d)==8
assert sum(x["id"].startswith("A") for x in d)==8
for x in d:
    root=ET.parse(b/x["adapted_svg"]).getroot()
    assert root.get("viewBox")=="0 0 600 1000"
    for el in root:
        if el.tag.endswith("path"):
            assert el.get("fill")=="none"
            assert el.get("stroke-width")=="66"
            assert el.get("stroke-linecap")=="round"
            assert el.get("stroke-linejoin")=="round"
        elif el.tag.endswith("circle"):
            assert el.get("r")=="71"
        else:
            raise AssertionError("Unexpected SVG geometry")
for s in ("runic_comparison.svg","alchemical_comparison.svg"):
    txt=(b/s).read_text(encoding="utf-8")
    assert txt.count("<use ")==8
    assert "data:image/png;base64" in txt
print("PASS 16 candidate vectors, two comparison sheets, source IDs intact")
