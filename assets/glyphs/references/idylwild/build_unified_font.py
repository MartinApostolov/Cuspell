#!/usr/bin/env python3
"""Build one installable review font for all 150 Cuspell + 299 Idylwild designs.

The canonical Cuspell TTF glyph outlines are copied unchanged. CC0 source
icons are converted from the supplied 16x16 pixel sprites to monochrome
TrueType contours. This is a candidate *comparison* font, NOT an adoption
of Idylwild's designs as Cuspell roots.
"""
from __future__ import annotations
import hashlib
import io
import json
import math
import re
import zipfile
from pathlib import Path
from html import escape
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]  # assets/
RECOVERY = ROOT / "glyphs" / "recovery"
ORIG = BASE / "original"
DEST = BASE / "keyboard_kit"
FONT_NAME = "CuspellCodexReview-Regular.ttf"
ZIP_NAME = "Cuspell_Codex_Keyboard_Kit.zip"
INPUT_FONT = RECOVERY / "generated" / "fonts" / "CuspellRecoveredPrototype-Regular.ttf"
SHA = {
    "idylwilds_runic_codex.zip": "1f5473b40e96fdaa980bc93993890a2f9e49d13ba0fdb6d5895bbacf5cb4cda5",
    "idylwilds_alchemical_codex.zip": "50ffd77d022dd0a62603f105dfc1b94ccff767e126622a3105ce03dc612dc055",
}
PUA_CUSPELL = 0xE001
PUA_RUNIC = 0xE100
PUA_ALCHEMICAL = 0xE200

def validate_sources():
    for name,sha in SHA.items():
        p=ORIG/name
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha:
            raise ValueError("Missing or altered original ZIP: "+str(p))
        with zipfile.ZipFile(p) as z:
            if z.testzip():
                raise ValueError("CRC error in original ZIP: "+str(p))

def bitmap_icon(z: zipfile.ZipFile, name: str, invert_white=False):
    with Image.open(io.BytesIO(z.read(name))) as im:
        im=im.convert("RGBA")
        if im.size!=(16,16):
            raise ValueError("Unexpected tile size for "+name)
        # Runic: all opaque pixels are ink (black alpha antialiased).
        # Alchemical: black outlines are ink; opaque white interiors must
        # remain white/negative space to preserve its original structure.
        return [[im.getpixel((x,y))[3] >= 64 and
                 (not invert_white or max(im.getpixel((x,y))[:3]) < 128)
                 for x in range(16)] for y in range(16)]

def pixel_contours(mask):
    """A non-overlapping rectangle for each maximal horizontal run of pixels,
    merging equal-length run spans vertically wherever possible."""
    active={}
    rects=[]
    for y in range(17):
        runs=[]
        if y<16:
            x=0
            while x<16:
                if not mask[y][x]:
                    x+=1
                    continue
                x0=x
                while x<16 and mask[y][x]:
                    x+=1
                runs.append((x0,x))
        current=set(runs)
        for run,(top,last) in list(active.items()):
            if run not in current:
                rects.append((run[0],top,run[1],last+1))
                del active[run]
        for run in runs:
            if run in active:
                top,_=active[run]
                active[run]=(top,y)
            else:
                active[run]=(y,y)
    return rects

def glyph_from_icon(mask):
    pen=TTGlyphPen(None)
    # Fit the compact 16x16 sprite into 600x1000 tall Cuspell em.
    # Scaling is a review-font presentation choice only, not a source edit.
    sx,sy=31,40
    left,bottom=52,180
    rects=pixel_contours(mask)
    if not rects:
        raise ValueError("Blank candidate icon")
    for x0,y0,x1,y1 in rects:
        l=left+x0*sx
        r=left+x1*sx
        t=bottom+(16-y0)*sy
        b=bottom+(16-y1)*sy
        pen.moveTo((l,b))
        pen.lineTo((l,t))
        pen.lineTo((r,t))
        pen.lineTo((r,b))
        pen.closePath()
    return pen.glyph()

def set_font_name(font):
    vals={
      1:"Cuspell Codex Comparison",
      2:"Regular",
      3:"CuspellCodexComparison-2026-10-22",
      4:"Cuspell Codex Comparison Regular",
      6:"CuspellCodexComparison-Regular",
      13:"Cuspell original glyph source; third-party Idylwild pixel art CC0. See accompanying SOURCES.txt.",
    }
    table=font["name"]
    # Replace all old source-font naming records to avoid same-name conflicts.
    table.names=[]
    for name_id,value in vals.items():
        table.setName(value,name_id,3,1,0x409)
        table.setName(value,name_id,1,0,0)
    if "OS/2" in font:
        # Existing font comes with these values, but clarify no restriction.
        font["OS/2"].fsType=0

def verify_input_font(font):
    cmap=font.getBestCmap()
    for i in range(1,151):
        cp=PUA_CUSPELL+i-1
        gid=f"G{i:03d}"
        if cmap.get(cp)!=gid:
            raise ValueError(f"Cuspell original glyph mismatch U+{cp:04X}: {cmap.get(cp)!r}, wanted {gid}")
    if font["head"].unitsPerEm!=1000:
        raise ValueError("Expected 1000 units per em, review builder would need scaling")
    return {PUA_CUSPELL+i-1:font["glyf"][f"G{i:03d}"].compile(font["glyf"])
            for i in range(1,151)}

def build():
    validate_sources()
    if not INPUT_FONT.is_file():
        raise FileNotFoundError("Current Cuspell TTF not found: "+str(INPUT_FONT))
    font=TTFont(INPUT_FONT,recalcTimestamp=False)
    originals=verify_input_font(font)
    cmap=font.getBestCmap().copy()
    entries=[]
    order=font.getGlyphOrder().copy()
    with zipfile.ZipFile(ORIG/"idylwilds_runic_codex.zip") as zr:
        runes={int(m.group(1)):p for p in zr.namelist()
               if (m:=re.fullmatch(r"runes/rune(\d+)\.png",p))}
        if set(runes)!=set(range(1,225)):
            raise AssertionError("Expected 224 numbered Runic designs")
        for i in range(1,225):
            name=f"runic{i:03d}"
            cp=PUA_RUNIC+i-1
            font["glyf"][name]=glyph_from_icon(bitmap_icon(zr,runes[i]))
            font["hmtx"].metrics[name]=(600,0)
            cmap[cp]=name;order.append(name)
            entries.append({"collection":"Runic","id":f"R{i:03d}","codepoint":f"U+{cp:04X}","character":chr(cp),"glyph":name,"source_path":runes[i]})
    with zipfile.ZipFile(ORIG/"idylwilds_alchemical_codex.zip") as za:
        alch={int(m.group(1)):p for p in za.namelist()
              if (m:=re.fullmatch(r"tile(\d{3})\.png",p))}
        if set(alch)!=set(range(225)):
            raise AssertionError("Expected 225 Alchemical tiles (75 sets of 3 variants)")
        for i in range(75):
            name=f"alchemical{i+1:03d}"
            cp=PUA_ALCHEMICAL+i
            font["glyf"][name]=glyph_from_icon(bitmap_icon(za,alch[i],invert_white=True))
            font["hmtx"].metrics[name]=(600,0)
            cmap[cp]=name;order.append(name)
            entries.append({"collection":"Alchemical","id":f"A{i+1:03d}","codepoint":f"U+{cp:04X}","character":chr(cp),"glyph":name,"source_path":alch[i]})
    font.setGlyphOrder(order)
    # All PUA characters are in the Basic Multilingual Plane.
    for t in font["cmap"].tables:
        if t.isUnicode():
            if t.format==4 or t.format==12:
                t.cmap.update(cmap)
    font["maxp"].numGlyphs=len(order)
    font["hhea"].numberOfHMetrics=len(order)
    set_font_name(font)
    DEST.mkdir(parents=True,exist_ok=True)
    out=DEST/FONT_NAME
    font.save(out,reorderTables=True)
    font.close()
    saved=TTFont(out,recalcTimestamp=False)
    final=saved.getBestCmap()
    if len({final.get(cp) for cp in range(PUA_CUSPELL,PUA_CUSPELL+150)})!=150:
        raise AssertionError("Cuspell mapping lost unique glyphs")
    for cp,data in originals.items():
        nm=f"G{cp-PUA_CUSPELL+1:03d}"
        if saved["glyf"][nm].compile(saved["glyf"])!=data:
            raise AssertionError("Original Cuspell outline changed for "+nm)
    for r in entries:
        cp=int(r["codepoint"][2:],16)
        if final.get(cp)!=r["glyph"]:
            raise AssertionError("Lost Idylwild mapping for "+r["id"])
    count=sum(1 for cp in final if PUA_CUSPELL<=cp<=0xE24A)
    if count != 449:
        raise AssertionError(f"Expected 449 mapped glyphs, got {count}")
    saved.close()
    return entries,out

def make_html(entries):
    # All 150 inherited existing PUA signs, plus 299 new font glyphs.
    full=[{"collection":"Cuspell","id":f"G{i:03d}",
           "codepoint":f"U+{PUA_CUSPELL+i-1:04X}","character":chr(PUA_CUSPELL+i-1)}
          for i in range(1,151)]+entries
    embedded=json.dumps(full,ensure_ascii=True,separators=(",",":"))
    html="""<!doctype html>
<html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cuspell — Type &amp; Compare 449 Glyphs</title>
<style>
@font-face{font-family:Codex;src:url('CuspellCodexReview-Regular.ttf') format('truetype')}
:root{font-family:system-ui,sans-serif;color:#203046;background:#f1f5fa}
body{margin:0 auto;max-width:1400px;padding:24px}h1{margin:10px 0}
p{line-height:1.5}.caption{color:#516c84}.toolbar{position:sticky;top:0;background:#eef4fa;
border:1px solid #b9c9d9;padding:14px;border-radius:12px;z-index:3}
button{border:1px solid #9eb6cd;background:white;border-radius:7px;padding:9px 12px;cursor:pointer}
button:hover{background:#dcecf9}button.active{background:#193b63;color:white}
input,textarea{font:inherit;border:1px solid #9eb6cd;border-radius:6px;padding:9px}
#search{min-width:200px}#work{width:100%;box-sizing:border-box;min-height:130px;
font:42px Codex;background:white;resize:vertical;line-height:1.5;margin-top:9px}
#grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(92px,1fr));gap:9px;margin:18px 0}
.tile{min-height:95px;display:flex;flex-direction:column;align-items:center;
justify-content:center;background:white;border:1px solid #c9d5e1}
.tile .char{font:52px Codex;line-height:1.25}.tile small{color:#536a80}
#status{min-height:25px;color:#205c40}.help{background:white;border-radius:10px;padding:13px}
@media(max-width:500px){body{padding:11px}.toolbar{position:static}#work{font-size:32px}}
</style>
<h1>Cuspell · 449-glyph review keyboard</h1>
<p class="caption">150 existing Cuspell + 224 Idylwild Runic + 75 Idylwild Alchemical. Click glyphs to compose text. These are <b>unassigned comparison symbols</b>, not 299 new roots.</p>
<div class="toolbar">
  <div id="tabs">
    <button data-c="all" class="active">All (449)</button>
    <button data-c="Cuspell">Cuspell (150)</button>
    <button data-c="Runic">Runic (224)</button>
    <button data-c="Alchemical">Alchemical (75)</button>
  </div>
  <p><label for="search">Find ID / hex:</label> <input id="search" placeholder="e.g. G070, R038, A012, E100" aria-label="Find glyph"></p>
  <label for="work">Your text (uses the installed/review font):</label>
  <textarea id="work" spellcheck="false" autocomplete="off"></textarea>
  <div>
    <button id="copy">Copy glyph text</button>
    <button id="space">Insert space</button>
    <button id="clear">Clear</button>
    <button id="export">Save text file</button>
  </div>
  <p id="status" aria-live="polite">Choose a collection and click glyphs below to type.</p>
</div>
<div id="grid"></div>
<section class="help">
<h2>How to use this as an installable font</h2>
<p>Install <code>CuspellCodexReview-Regular.ttf</code> from the same ZIP (double-click and choose Install on Windows/macOS; open in Fonts on Linux). Select <b>Cuspell Codex Comparison</b> in your document editor, then paste glyph text copied from the box above.</p>
<p>Characters use the Unicode Private Use Area: Cuspell U+E001–U+E096; Runic U+E100–U+E1DF; Alchemical U+E200–U+E24A. Other fonts will not display them correctly. The text file and clipboard retain codes, not ordinary letters. This kit is for comparison, not the final Cuspell assignment or player UI.</p>
<p>The 299 imported designs are rendered as monochrome TrueType pixel-derived outlines. Cuspell's existing font outlines remain unchanged. Licensing/provenance: Idylwild source assets CC0; see SOURCES.txt.</p>
</section>
<script>
const GLYPHS=__GLYPHS__;
const search=document.querySelector("#search"),grid=document.querySelector("#grid");
const work=document.querySelector("#work"),status=document.querySelector("#status");
let choice="all";
function render(){
 const s=search.value.trim().toUpperCase();
 grid.replaceChildren();
 let visible=GLYPHS.filter(x=>(choice==="all"||x.collection===choice)&&
   (!s||x.id.includes(s)||x.codepoint.includes(s)));
 for(const x of visible){
  const b=document.createElement("button");b.type="button";b.className="tile";
  b.title=x.collection+" "+x.id+" "+x.codepoint;
  const mark=document.createElement("span");mark.className="char";mark.textContent=x.character;
  const id=document.createElement("small");id.textContent=x.id+"  "+x.codepoint;
  b.append(mark,id);b.onclick=()=>{
    const a=work.selectionStart,b=work.selectionEnd;
    work.setRangeText(x.character,a,b,"end");work.focus();
    status.textContent="Inserted "+x.id+" ("+x.codepoint+")";
  };
  grid.append(b);
 }
 status.textContent="Showing "+visible.length+" designs";
}
document.querySelectorAll("#tabs button").forEach(b=>b.onclick=()=>{
 choice=b.dataset.c;document.querySelectorAll("#tabs button").forEach(a=>a.classList.toggle("active",a===b));render()
});
search.addEventListener("input",render);
document.querySelector("#copy").onclick=async()=>{
 try {await navigator.clipboard.writeText(work.value);status.textContent="Copied. Set your target document font to Cuspell Codex Comparison."}
 catch(e){work.select();status.textContent="Browser denied clipboard: select and copy the text manually."}
};
document.querySelector("#space").onclick=()=>{work.setRangeText(" ",work.selectionStart,work.selectionEnd,"end");work.focus()};
document.querySelector("#clear").onclick=()=>{work.value="";status.textContent="Cleared."};
document.querySelector("#export").onclick=()=>{
 const blob=new Blob([work.value],{type:"text/plain;charset=utf-8"});
 const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download="cuspell-comparison.txt";a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);
};
render();
</script></html>""".replace("__GLYPHS__",embedded)
    (DEST/"keyboard.html").write_text(html,encoding="utf-8")
    (DEST/"glyph_map.csv").write_text("collection,id,codepoint,character\n"+
        "".join(f'{e["collection"]},{e["id"]},{e["codepoint"]},{e["character"]}\n'
                for e in full),encoding="utf-8")
    (DEST/"SOURCES.txt").write_text(
        "Cuspell Codex Comparison (review font, not final language mapping)\n\n"
        "Existing G001–G150 outlines: Cuspell project canonical generated TTF.\n"
        "Idylwild's Runic Codex: https://opengameart.org/content/idylwilds-runic-codex\n"
        "Idylwild's Alchemical Codex: https://opengameart.org/content/idylwilds-alchemical-codex\n"
        "Third-party artwork license: CC0, per source pages.\n\n"
        "Install CuspellCodexReview-Regular.ttf, open keyboard.html, click glyphs\n"
        "to compose text, copy and paste into an editor selecting this font.\n"
        "Cuspell private use: U+E001–U+E096 (150 glyphs).\n"
        "Idylwild Runic: U+E100–U+E1DF (224 glyphs).\n"
        "Idylwild Alchemical: U+E200–U+E24A (75 glyphs).\n\n"
        "The candidate sprite tiles are imported as solid one-color pixel\n"
        "outlines and not treated as canonical registered Cuspell runes.\n",
        encoding="utf-8")
    return full

def build_zip():
    p=DEST/ZIP_NAME
    with zipfile.ZipFile(p,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name in [FONT_NAME,"keyboard.html","glyph_map.csv","SOURCES.txt"]:
            data=(DEST/name).read_bytes()
            info=zipfile.ZipInfo(name,date_time=(2026,10,22,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(info,data)
    return p

if __name__=="__main__":
    entries,out=build()
    all_entries=make_html(entries)
    pkg=build_zip()
    meta={
       "status":"comparison_only",
       "font":FONT_NAME,
       "num_cuspell":150,"num_runic":224,"num_alchemical":75,
       "num_total":449,
       "pua_ranges":{"cuspell":["E001","E096"],"runic":["E100","E1DF"],
                     "alchemical":["E200","E24A"]},
       "source_font":"assets/glyphs/recovery/generated/fonts/CuspellRecoveredPrototype-Regular.ttf",
       "font_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
       "kit_sha256":hashlib.sha256(pkg.read_bytes()).hexdigest()
    }
    (DEST/"font_manifest.json").write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8")
    print(f"PASS: wrote {out}, {pkg} and keyboard.html with {len(all_entries)} indexed glyphs")
