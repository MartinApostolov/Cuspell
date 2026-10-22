#!/usr/bin/env python3
"""Reproducible visual audit for the Cuspell 150-glyph recovery collection.

Read-only with respect to canonical artwork: writes only generated/audit/.
Dependencies already installed in the recovery workflow: pillow, cairosvg,
fonttools, shapely, plus numpy (normally installed as a transitive dependency).

Similarity scores are triage suggestions, NOT visual approvals or automatic
rejections. Mirrored partners are tested separately, and excluded from the
unrelated-glyph similarity ranking.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from itertools import combinations
from pathlib import Path
import io
import json
import math
import re
import xml.etree.ElementTree as ET

import cairosvg
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source_geometry.json"
GENERATED = ROOT / "generated"
OUT = GENERATED / "audit"
OUT.mkdir(parents=True, exist_ok=True)
DATA = json.loads(SOURCE.read_text(encoding="utf-8"))
GLYPHS = DATA["glyphs"]
NAMES = [f"G{i:03}" for i in range(1, 151)]
assert list(sorted(GLYPHS)) == NAMES, "Audit requires G001–G150 in canonical source"
assert all(isinstance(GLYPHS[g].get("svg"), str) and "<svg" in GLYPHS[g]["svg"] for g in NAMES), "Pending or empty glyphs: audit only complete active inventory"

# Render in the same fixed 600x1000 cell. A 16px em displays 9.6px width.
# Small-size scores therefore check readability at genuine font size, not a
# blown-up glyph stretched to an unrealistic square icon.
CELL = (60, 100)
READ_SIZES = ((10, 16), (11, 18))


def render(svg: str, size: tuple[int, int]) -> np.ndarray:
    png = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=size[0], output_height=size[1])
    return np.asarray(Image.open(io.BytesIO(png)).convert("RGBA"))[:, :, 3].copy()


def count_components(alpha: np.ndarray, threshold: int = 64) -> tuple[int, float]:
    """Count 8-connected ink islands without SciPy (CairoSVG + NumPy + PIL)."""
    mask = (alpha > threshold).copy()
    height,width = mask.shape
    components=[]
    for y in range(height):
        for x in range(width):
            if not mask[y,x]:
                continue
            mask[y,x]=False
            stack=[(y,x)]
            count=0
            while stack:
                sy,sx=stack.pop();count+=1
                for yy in range(max(0,sy-1), min(height,sy+2)):
                    for xx in range(max(0,sx-1),min(width,sx+2)):
                        if mask[yy,xx]:
                            mask[yy,xx]=False
                            stack.append((yy,xx))
            components.append(count)
    if not components:
        return 0,0.0
    return len(components),float(min(components)/sum(components))


def bbox(alpha: np.ndarray) -> tuple[int, int, int, int] | None:
    ys, xs = np.nonzero(alpha > 48)
    if not len(xs):
        return None
    return int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1)


def string_paths(xml: str):
    root = ET.fromstring(xml)
    paths = [node for node in root.iter() if node.tag.endswith("}path") or node.tag == "path"]
    return paths


def cosine_matrix(mat: np.ndarray) -> np.ndarray:
    vectors = mat.reshape((len(NAMES), -1)).astype(np.float32) / 255.0
    norm = np.linalg.norm(vectors, axis=1)
    norm[norm == 0] = 1
    vectors /= norm[:, None]
    result = vectors @ vectors.T
    return np.clip(result, 0, 1)


def jaccard_matrix(mat: np.ndarray, threshold: int = 72) -> np.ndarray:
    # Pairwise overlap / union, preserving the original 600×1000 cell positions.
    v=(mat>threshold).reshape((len(NAMES),-1)).astype(np.float32)
    overlap=v@v.T
    area=v.sum(axis=1)
    union=area[:,None]+area[None,:]-overlap
    return np.divide(overlap,union,out=np.zeros_like(overlap),where=union>0)


def font_check(names: list[str]) -> dict:
    f = GENERATED / "fonts" / "CuspellRecoveredPrototype-Regular.ttf"
    if not f.exists():
        return {"font_found": False, "errors": ["Generated TTF missing"]}
    ft = TTFont(f)
    cmap = ft.getBestCmap() or {}
    glyph_set = set(ft.getGlyphOrder())
    missing = [name for name in names if cmap.get(0xE000 + int(name[1:])) != name]
    widths = [ft["hmtx"].metrics[name][0] for name in names if name in ft["hmtx"].metrics]
    bad_width = [w for w in widths if w != 600]
    empty = [name for name in names if name in ft["glyf"] and ft["glyf"][name].numberOfContours == 0]
    return {
        "font_found": True,
        "cmap_count_in_pua": sum(0xE001 <= x <= 0xE096 for x in cmap),
        "glyph_count": len(ft.getGlyphOrder()),
        "missing_from_cmap": missing,
        "missing_from_glyph_order": sorted(set(names) - glyph_set),
        "non_600_advance_count": len(bad_width),
        "empty_glyph_outlines": empty,
        "woff2_found": (GENERATED / "fonts" / "CuspellRecoveredPrototype-Regular.woff2").exists(),
    }


def find_near_unrelated(high_cos, small_cos, high_jacc, small_jacc, mirror_links: set[frozenset]):
    results = []
    for i in range(len(NAMES)):
        for j in range(i + 1, len(NAMES)):
            a, b = NAMES[i], NAMES[j]
            if frozenset((a, b)) in mirror_links:
                continue
            val = float(high_cos[i, j]); val16 = float(small_cos[i, j])
            jac = float(high_jacc[i, j]); jac16 = float(small_jacc[i, j])
            if val >= .75 or val16 >= .82 or jac >= .60 or jac16 >= .67:
                results.append({"a": a, "b": b, "hi_cos": round(val, 4),
                                "px16_cos": round(val16, 4), "hi_iou": round(jac, 4),
                                "px16_iou": round(jac16, 4),
                                "risk_score": round(max(val, val16 * .94, jac * 1.06, jac16), 4)})
    return sorted(results, key=lambda d: (d["risk_score"], d["hi_cos"]), reverse=True)


def font_style(s: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    locations = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for x in locations:
        try:
            return ImageFont.truetype(x, s)
        except OSError:
            pass
    return ImageFont.load_default()


def contact_sheet(pairs: list[dict], images: dict[str, np.ndarray], name: str) -> None:
    count = min(len(pairs), 24)
    rowh, pairw = 168, 275
    head = 90
    canvas = Image.new("RGB", (pairw * 3 + 34, head + math.ceil(max(count, 1) / 3) * rowh + 40), "#f4f6f7")
    draw = ImageDraw.Draw(canvas)
    draw.text((20, 16), "CUSPELL  ·  POTENTIAL LOOK-ALIKE PAIRS", font=font_style(24, True), fill="#293745")
    draw.text((20, 53), "Candidates only — mirrored pairs excluded; compare by eye", font=font_style(13), fill="#5d6d78")
    for pos, item in enumerate(pairs[:count]):
        x = 16 + pos % 3 * pairw
        y = head + pos // 3 * rowh
        draw.rounded_rectangle((x, y, x + 255, y + 155), fill="white", outline="#c8d0d6", radius=9, width=2)
        draw.text((x + 13, y + 7), f"{item['a']}     {item['b']}", font=font_style(16, True), fill="#253643")
        for t, id in enumerate((item["a"], item["b"])):
            im = Image.fromarray(images[id]).resize((60, 100), Image.Resampling.BICUBIC)
            rgba = Image.new("RGBA", (60, 100), "black")
            rgba.putalpha(im)
            canvas.paste(rgba.convert("RGB"), (x + 45 + 106 * t, y + 30), rgba)
        draw.text((x + 14, y + 132), f"Shape {item['hi_cos']:.2f}  /  16px {item['px16_cos']:.2f}", font=font_style(12), fill="#687680")
    if not count:
        draw.text((30, 105), "No candidates above the thresholds", font=font_style(15), fill="#5d6d78")
    canvas.save(OUT / name)


def small_sheet(images, metrics):
    im = Image.new("RGB", (1200, 1080), "#eef2f4")
    dr = ImageDraw.Draw(im)
    dr.text((16, 12), "CUSPELL — ALL 150 GLYPHS AT 16px / 18px EM", font=font_style(24, True), fill="#263947")
    dr.text((16, 47), "Render from current source SVG in 600×1000 cell; no magnification", font=font_style(14), fill="#53636e")
    for j, name in enumerate(NAMES):
        x = 12 + (j % 10) * 119; y = 84 + (j // 10) * 65
        dr.rounded_rectangle((x, y, x + 112, y + 59), radius=6, fill="white", outline="#c6d0d7")
        dr.text((x + 4, y + 3), name, font=font_style(12, True), fill="#2c404b")
        for n,(w,h) in enumerate(READ_SIZES):
            alpha=Image.fromarray(images[name][n])
            black=Image.new("RGB", (w,h), "black")
            im.paste(black,(x + 17 + 48*n,y + 25),alpha)
            dr.text((x + 2 + 48*n,y + 42),f"{h}px",font=font_style(9),fill="#7a8a95")
    im.save(OUT / "all_at_16_and_18px.png")


def main() -> None:
    high, at16, at18, metrics = [], [], [], {}
    width_values = []
    for name in NAMES:
        record = GLYPHS[name]
        svg = record["svg"]
        alpha = render(svg, CELL)
        a16 = render(svg, READ_SIZES[0]); a18 = render(svg, READ_SIZES[1])
        high.append(alpha); at16.append(a16); at18.append(a18)
        xml_paths = string_paths(svg)
        ws=[];path_count=0
        for p in xml_paths:
            if p.attrib.get("stroke-width") is not None:
                ws.append(float(p.attrib["stroke-width"]))
            path_count+=len(re.findall(r"[Mm](?![A-Za-z])", p.attrib.get("d", "")))
        width_values.extend(ws)
        box=bbox(alpha)
        comps,small_comp=count_components(alpha)
        comps16,small16=count_components(a16,threshold=80)
        metrics[name] = {
            "confidence": record.get("confidence"), "approval": record.get("approval"),
            "historical_svg_is_outline_trace": any(p.attrib.get("fill", "") != "none" for p in xml_paths),
            "path_elements": len(xml_paths), "subpaths_approx":path_count,
            "stroke_widths": sorted(set(ws)), "bbox_high_px": box,
            "fraction_ink_at_16px": round(float(np.mean(a16) / 255.0), 4),
            "occupied_16px_pixels": int(np.count_nonzero(a16 >= 100)),
            "components_high": comps, "smallest_component_share": round(small_comp,4),
            "components_16px":comps16,"smallest_component_share_16px":round(small16,4),
        }
    higharr=np.stack(high);smallarr=np.stack(at16)
    hc=cosine_matrix(higharr);sc=cosine_matrix(smallarr)
    hj=jaccard_matrix(higharr);sj=jaccard_matrix(smallarr,threshold=80)
    partners=set();mirror_errors=[]
    for name in NAMES:
        other=GLYPHS[name].get("mirror_of")
        if other and other in GLYPHS:
            link=frozenset((name,other))
            partners.add(link)
            i=NAMES.index(name);k=NAMES.index(other)
            loss=float(np.abs(higharr[i].astype(np.float32)-np.fliplr(higharr[k]).astype(np.float32)).mean()/255)
            loss16=float(np.abs(smallarr[i].astype(np.float32)-np.fliplr(smallarr[k]).astype(np.float32)).mean()/255)
            mirror_errors.append({"a":other,"b":name,"mae":round(loss,4),"mae16":round(loss16,4),
                                  "pair_16px_cos":round(float(sc[i,k]),4)})
    mirror_errors.sort(key=lambda x:x["mae"],reverse=True)
    # Early original glyphs predate explicit mirror_of metadata. Detect only
    # adjacent odd/even pairs with almost mathematically exact reflection;
    # otherwise they create misleading "unrelated" false positives.
    inferred_mirror_links=[]
    for i in range(0,len(NAMES),2):
        a,b=NAMES[i],NAMES[i+1]
        link=frozenset((a,b))
        loss=float(np.abs(higharr[i].astype(np.float32)-np.fliplr(higharr[i+1]).astype(np.float32)).mean()/255)
        if loss < .005 and link not in partners:
            partners.add(link)
            inferred_mirror_links.append({"a":a,"b":b,"mae":round(loss,4)})
    near=find_near_unrelated(hc,sc,hj,sj,partners)
    mirrored_same_appearance=[x for x in mirror_errors if x["pair_16px_cos"]>=.94]
    distorted_mirrors=[x for x in mirror_errors if x["mae"]>.055]
    fine_parts=[name for name in NAMES if metrics[name]["smallest_component_share"]<.015 and metrics[name]["components_high"]>1]
    heavy=[name for name in NAMES if metrics[name]["subpaths_approx"]>3 and not metrics[name]["historical_svg_is_outline_trace"]]
    tiny=[name for name in NAMES if metrics[name]["occupied_16px_pixels"]<5]
    bounds=[name for name in NAMES if (box:=metrics[name]["bbox_high_px"]) and (box[0]<=0 or box[1]<=0 or box[2]>=CELL[0] or box[3]>=CELL[1])]
    unusual_width=sorted(set(width_values))
    traced=[n for n in NAMES if metrics[n]["historical_svg_is_outline_trace"]]
    font=font_check(NAMES)
    contact_sheet(near,dict(zip(NAMES,higharr)),"near_pairs.png")
    small_sheet({n:(at16[i],at18[i]) for i,n in enumerate(NAMES)},metrics)
    jsondata={"method":"Cairosvg alpha raster with fixed em cell; cosine+thresholded intersection-over-union at 60x100 and 10x16 pixels; near matches exclude declared mirror_of pairs", 
              "glyph_count":len(NAMES),"mirror_links_including_inferred":len(partners),"inferred_historical_mirror_links":inferred_mirror_links,"font":font,
              "summary":{"candidate_near_pairs":len(near),"declared_mirror_errors":len(distorted_mirrors),"inferred_undeclared_mirror_pairs":len(inferred_mirror_links),
                         "mirror_pairs_16px_almost_identical":len(mirrored_same_appearance),
                         "extra_stroke_paths_gt3":len(heavy),"outline_traced_glyphs":len(traced),
                         "tiny_fragments":len(fine_parts),"small_16px_ink_count_lt5":len(tiny),
                         "edge_clipping":len(bounds),"stroke_widths":unusual_width},
              "candidate_pairs":near, "mirror_errors":mirror_errors, "mirror_16px_near_identical":mirrored_same_appearance,
              "tiny_fragments":fine_parts,"small_ink":tiny,"clipped":bounds,"heavy":heavy,
              "glyph_metrics":metrics}
    (OUT/"audit_data.json").write_text(json.dumps(jsondata,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    def fmtpairs(items,limit=35):
        return "\n".join(f"| {p['a']} / {p['b']} | {p['hi_cos']:.3f} | {p['px16_cos']:.3f} | {p['hi_iou']:.3f} | {p['px16_iou']:.3f} |" for p in items[:limit]) if items else "| None above current thresholds | — | — | — | — |"

    s=jsondata["summary"]
    mirror_bad_desc=", ".join(f"{r['a']}/{r['b']}: {r['mae']}" for r in mirror_errors[:12]) or "none"
    mirror_same_desc=", ".join(f"{r['a']}/{r['b']}" for r in mirrored_same_appearance[:40]) or "none"
    text=["# Cuspell 150-glyph visual audit", "", "**Audit scope:** all 150 current active glyphs from the canonical `source_geometry.json`. The audit does **not** modify approved glyph geometry. All numeric scores are automatic *review flags*, not proof two glyphs are identical or approved/rejected.", "", "## 1. Summary", "", "| Check | Result |", "| --- | --- |",f"| Registered & rendered source SVGs | {len(NAMES)}/150 |",f"| Declared mirror references checked | {len(mirror_errors)} |",f"| Extra exact mirror siblings inferred from historical geometry | {len(inferred_mirror_links)} |",f"| High visual-similarity pairs excluding direct and inferred mirrors | {len(near)} candidates above thresholds |",f"| Declared mirrored links with visual mismatch (MAE > 0.055) | {len(distorted_mirrors)} |",f"| Declared mirrors almost identical *unmirrored* at 16px (cos≥0.94) | {len(mirrored_same_appearance)} |",f"| Multiple strokes (>3 start commands) excluding traced-fill images | {len(heavy)} |",f"| Tiny high-res detached pieces (<1.5% of ink area) | {len(fine_parts)} |",f"| Glyphs with <5 solid pixels at 16px | {len(tiny)} |",f"| High-resolution silhouette touching SVG cell boundary | {len(bounds)} |",f"| Observed SVG stroke widths (units) | {', '.join(str(round(x,2)) for x in unusual_width) or 'none'} |",
       "", "## 2. Potentially confusable *unrelated* pairs", "", "The ranking excludes both explicitly declared mirrors and geometrically exact adjacent mirror siblings, but **not intentional 180° variants** or historical visual families. Both high-res and native 16px scores are shown so that similar-looking strokes are not overlooked. A score of 1.0 means equal sampled alpha silhouettes; 0.0 means no overlapping ink in the fixed cell. These measures alone do not model handwriting variation.", "", "| Glyphs | 60×100 cosine | 16px cosine | 60×100 IoU | 16px IoU |", "|---|---:|---:|---:|---:|",fmtpairs(near),"", "See `near_pairs.png` (first 24 candidates) and `audit_data.json` (all candidate scores).", "", "Older mirror siblings (for example G071/G072, G079/G080) were inferred by geometric reflection because historical records do not always include mirror_of metadata. An inferred mirror relationship is **not** an extra visual design approval.", "", "## 3. Mirroring and small-size ambiguity", "", "A mirror relationship is measured after horizontally flipping the declared partner's alpha mask. Large MAE (>0.055) suggests the `mirror_of` metadata or geometry needs checking; values near zero usually indicate correct mirroring. The 16px cosine shown separately measures *the two signs as printed*, without flipping: a score ≥0.94 may mean the pair becomes almost indistinguishable at that size.", "", f"Mirrored links with largest post-flip error: {mirror_bad_desc}.", "", f"Mirror pairs with nearly identical 16px appearances ({len(mirrored_same_appearance)}): {mirror_same_desc}.", "", "## 4. Construction, pen strokes and small print", "", f"SVG stroke widths: **{', '.join(str(x) for x in unusual_width) or 'none'}**. These reflect `stroke-width` declarations for centerline SVGs only; filled screenshot traces cannot be assigned a reliable pen-width or gesture order from silhouettes alone.", "", f"Filled-outline source SVGs (typically screenshot traces, not pen-path guides): **{len(traced)}**. Their stroke count is not objectively recoverable from outline geometry; a hand-drawing test is still required.", "", f"Four-or-more distinct path starts (untraced SVGs): **{', '.join(heavy[:50]) or 'none'}**.", "", f"Suspicious tiny detached pieces in high-res raster: **{', '.join(fine_parts[:50]) or 'none'}**.", "", f"Less than five strong ink pixels at 16px em: **{', '.join(tiny[:50]) or 'none'}**.", "", f"Touches outer cell boundary (possible SVG clipping): **{', '.join(bounds[:50]) or 'none'}**.", "", "See `all_at_16_and_18px.png` for the entire inventory at native target rendering sizes. Text intended for users at this size must be evaluated by a human, because automated tests cannot establish legibility.", "", "## 5. Generated font integrity", "", f"- TTF present: **{font.get('font_found')}**. WOFF2 present: **{font.get('woff2_found')}**.", f"- Font private-use mappings G001–G150: **{font.get('cmap_count_in_pua','?')}** (expected 150).", f"- Missing/wrong cmap entries: **{', '.join(font.get('missing_from_cmap',[])) or 'none'}**.", f"- Missing glyph names: **{', '.join(font.get('missing_from_glyph_order',[])) or 'none'}**.", f"- Non-600 advance widths: **{font.get('non_600_advance_count','?')}**.", f"- Empty TTF glyph outlines: **{', '.join(font.get('empty_glyph_outlines',[])) or 'none'}**.", "", "## 6. Interpretation / next review", "", "1. Inspect `near_pairs.png`, especially pairs with cosine ≥0.90 at 60×100 or ≥0.95 at 16px. Decide whether apparent similarities are deliberate family members, accepted transformations or truly confusing alternatives.", "2. Check pairs that mirror correctly but render almost identical at 16px. The historical glyph register may deliberately include some near-symmetric mirrors; do not remove them automatically.", "3. Inspect `all_at_16_and_18px.png` at *actual* size, then perform a handwriting trial for multi-stroke candidates and screenshot-derived outlines.", "4. Do not revise or delete user-approved vectors without user review; preserve both the original sources and archived rejected variants.", "", "**Caveat:** all 150 active glyphs have been selected for the current recovery, but many later SVGs are reconstructed rather than authentic lost v0.19 geometry; 100 early glyphs have authentic historical vectors. Exact handwritten gesture orders for later reconstructions are not recovered.", ""]
    (OUT/"GLYPH_AUDIT.md").write_text("\n".join(text),encoding="utf-8")
    print("Cuspell audit:",json.dumps(s,ensure_ascii=False))
    print("Font:",json.dumps(font,ensure_ascii=False))
    print("Worst near-pairs:",[(p['a'],p['b'],p['hi_cos'],p['px16_cos']) for p in near[:15]])
    print("Report:",OUT/"GLYPH_AUDIT.md")

if __name__=="__main__":
    main()