#!/usr/bin/env python3
"""Apply verified v0.14 Revision 1 artwork to the recovered 150-glyph source.

Idempotent: only replaces description-based approximations. Later hand-reviewed
artwork is not overwritten. The uploaded ZIP is the evidence; its SHA256 is
recorded in the compressed evidence pack for external verification.
"""
from pathlib import Path
import base64
import brotli
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source_geometry.json"
EVIDENCE = ROOT / "evidence" / "v0.14_R1_confirmed_source.br.b64"
IDS = [f"G{i:03d}" for i in (*range(81, 87), *range(91, 101))]


def read_evidence():
    data = json.loads(brotli.decompress(base64.b64decode(EVIDENCE.read_text().strip())))
    assert data["pack"] == "v0.14_R1"
    assert len(data["original_pack_sha256"]) == 64
    for name in IDS:
        assert f"glyphs/{name}.svg" in data["contents"]
        assert f"gesture_guides/{name}.svg" in data["contents"]
        assert "<svg" in data["contents"][f"glyphs/{name}.svg"]
    return data


def main():
    data = read_evidence()
    source = json.loads(SOURCE.read_text())
    assert len(source["glyphs"]) == 150
    updated = []
    for name in IDS:
        glyph = source["glyphs"][name]
        if glyph["confidence"] == "EXACT_V014_R1":
            assert glyph["svg"].strip() == data["contents"][f"glyphs/{name}.svg"].strip(), name
            continue
        if glyph["confidence"] != "DESCRIPTION_APPROX":
            print(f"Preserving later-reviewed {name} ({glyph['confidence']})")
            continue
        glyph["svg"] = data["contents"][f"glyphs/{name}.svg"].strip()
        glyph["source"] = "original_v0.14_R1_uploaded_archive"
        glyph["confidence"] = "EXACT_V014_R1"
        # These were candidates when archived; do not manufacture approval.
        glyph["approval"] = "review_requested"
        updated.append(name)
    source["version"] = "0.19-recovered-v2-v014R1-evidence"
    source["evidence_v014_r1_sha256"] = data["original_pack_sha256"]
    source["source_caveats"] = [
        note for note in source["source_caveats"]
        if not note.startswith("G081-G086 are approximations")
        and not note.startswith("G091-G110,")
    ]
    for note in [
        "G081-G086 and G091-G100 are exact original v0.14 Revision 1 SVGs, not proof that their later revisions were identical or formally approved.",
        "G101-G110 and G133-G150 are still description-based approximations (G137/G138 visually accepted previously but not geometrically exact).",
        "Authentic v0.14 R1 gesture-guide markup is preserved for the 16 newly recovered candidates; other generated guide files are NOT authentic gesture order.",
        "G001-G080 and G087-G090 were unchanged between v0.13 and v0.14 R1, per uploaded original pack.",
    ]:
        if note not in source["source_caveats"]:
            source["source_caveats"].append(note)
    SOURCE.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n")
    print(f"Applied {len(updated)} exact v0.14 R1 SVG sources: {', '.join(updated) or '(already present)'}")


if __name__ == "__main__":
    main()
