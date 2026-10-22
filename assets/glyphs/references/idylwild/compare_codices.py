#!/usr/bin/env python3
"""Non-destructive, indexed source comparison for two CC0 Idylwild packs.

DOES NOT assign meanings, register imported glyphs, or modify Cuspell SVGs.
"""
from __future__ import annotations
import argparse, hashlib, io, json, re, zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE=Path(__file__).resolve().parent
ORIGINAL=BASE/"original"
REVIEWS=BASE/"reviews"
PACKS={
 "runic":("idylwilds_runic_codex.zip","1f5473b40e96fdaa980bc93993890a2f9e49d13ba0fdb6d5895bbacf5cb4cda5",224),
 "alchemical":("idylwilds_alchemical_codex.zip","50ffd77d022dd0a62603f105dfc1b94ccff767e126622a3105ce03dc612dc055",75),
}
CW,CH,NCOLS,PAD,GAP=112,113,8,24,36
PANEL_W=CW*NCOLS+2*PAD

def font(sz,bold=False):
    name="/usr/share/fonts/truetype/dejavu/DejaVuSans"+("-Bold.ttf" if bold else ".ttf")
    try:return ImageFont.truetype(name,sz)
    except OSError:return ImageFont.load_default()

def read_assets():
    result={}
    for kind,(filename,digest,expected) in PACKS.items():
        p=ORIGINAL/filename
        if hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
            raise ValueError(f"Invalid original Idylwild archive checksum: {p}")
        with zipfile.ZipFile(p) as z:
            if z.testzip():raise ValueError(f"Corrupt Idylwild ZIP: {p}")
            if kind=="runic":
                names={int(m.group(1)):n for n in z.namelist()
                       if (m:=re.fullmatch(r"runes/rune(\d+)\.png",n))}
                if set(names)!=set(range(1,225)):
                    raise ValueError("Expected exactly rune1.png through rune224.png")
                if sum(n.startswith("runes/") and n.endswith(".png") for n in z.namelist())!=672:
                    raise ValueError("Runic variants must total 672 icons (224 shapes in 3 styles)")
                pairs=[(f"R{i:03}",names[i]) for i in range(1,225)]
            else:
                names={int(m.group(1)):n for n in z.namelist()
                       if (m:=re.fullmatch(r"tile(\d{3})\.png",n))}
                if set(names)!=set(range(225)):
                    raise ValueError("Expected exactly tile000.png through tile224.png")
                pairs=[(f"A{i+1:03}",names[i]) for i in range(75)]
            if len(pairs)!=expected:raise AssertionError("Wrong design count")
            result[kind]=[]
            for ident,n in pairs:
                with Image.open(io.BytesIO(z.read(n))) as img:
                    if img.size!=(16,16):raise ValueError(f"{n} not 16x16")
                    result[kind].append((ident,img.convert("RGBA").copy()))
    return result

def text(draw,xy,message,size=16,bold=False,fill="#17334f"):
    draw.text(xy,message,font=font(size,bold),fill=fill)

def contact_sheet(panels,filename,subtitle):
    rows=max((len(p["items"])+NCOLS-1)//NCOLS for p in panels)
    w=84+len(panels)*PANEL_W+(len(panels)-1)*GAP
    h=205+rows*CH+94
    image=Image.new("RGB",(w,h),"#eff3fa");d=ImageDraw.Draw(image)
    text(d,(45,34),"CUSPELL  /  GLYPH SOURCE COMPARISON",35,True)
    text(d,(45,87),subtitle,17,False,"#51657a")
    d.line((45,135,w-45,135),fill="#9baec1",width=2)
    for j,p in enumerate(panels):
        x0=42+j*(PANEL_W+GAP)
        text(d,(x0+PAD,162),p["name"],24,True)
        text(d,(x0+PAD,197),p["desc"],15,False,"#51657a")
        for i,(ident,src) in enumerate(p["items"]):
            x=x0+PAD+(i%NCOLS)*CW;y=236+(i//NCOLS)*CH
            dark=p.get("dark",False)
            d.rounded_rectangle((x,y,x+CW-7,y+CH-6),radius=11,
                fill=("#20384f" if dark else "#ffffff"),
                outline=("#344c68" if dark else "#d3dfe9"),width=2)
            icon=src.resize((78,78),Image.Resampling.NEAREST if src.size==(16,16) else Image.Resampling.LANCZOS)
            image.paste(icon,(x+13,y+7),icon)
            box=d.textbbox((0,0),ident,font=font(14,True))
            text(d,(x+(CW-7-box[2]+box[0])//2,y+85),ident,14,True,
                "#dfebf4" if dark else "#17334f")
    text(d,(45,h-62),"Idylwild sources: CC0. Cuspell: current project source. Candidate review only; no meanings assigned.",
         16,False,"#51657a")
    text(d,(45,h-35),"Compare distinct shapes, not colored variants. Source pixels scaled using nearest-neighbor.",
         16,False,"#51657a")
    REVIEWS.mkdir(parents=True,exist_ok=True)
    output=REVIEWS/filename
    image.save(output,optimize=True)
    print(f"CREATED {output} ({image.width}x{image.height})")

def load_cuspell(path):
    import cairosvg
    glyphs=json.loads(path.read_text(encoding="utf-8"))["glyphs"]
    ids=[f"G{i:03}" for i in range(1,151)]
    if set(glyphs)!=set(ids):raise ValueError("Expected exactly G001-G150")
    items=[]
    for gid in ids:
        svg=glyphs[gid]["svg"]
        with Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),
                        output_width=72,output_height=120))) as src:
            icon=src.convert("RGBA")
            icon.thumbnail((67,78))
            frame=Image.new("RGBA",(78,78),(255,255,255,0))
            frame.alpha_composite(icon,((78-icon.width)//2,(78-icon.height)//2))
            items.append((gid,frame))
    return items

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cuspell-source",type=Path,
        default=BASE.parent.parent/"recovery"/"source_geometry.json")
    args=ap.parse_args()
    images=read_assets()
    runic={"name":"RUNIC CODEX","desc":"224 original designs  /  black icon variant",
           "items":images["runic"]}
    alchemical={"name":"ALCHEMICAL CODEX",
                "desc":"75 original designs  /  white icon variant",
                "items":images["alchemical"],"dark":True}
    cuspell={"name":"CUSPELL","desc":"150 current original SVG glyphs",
             "items":load_cuspell(args.cuspell_source)}
    contact_sheet([runic,alchemical],"01_runic_vs_alchemical.png",
                  "Full indexed catalogue  /  Idylwild Runic (224) and Alchemical (75)")
    contact_sheet([runic,alchemical,cuspell],
                  "02_runic_vs_alchemical_vs_cuspell.png",
                  "Full indexed catalogue  /  224 Runic  +  75 Alchemical  +  150 Cuspell")
    report={
      "status":"comparison_only_not_added_to_cuspell_registry",
      "licenses":"CC0 (OpenGameArt source page declarations)",
      "archives":{key:{"filename":v[0],"sha256":v[1],"unique_design_count":v[2]}
                  for key,v in PACKS.items()},
      "cuspell_source":str(args.cuspell_source.relative_to(BASE.parent.parent))
          if args.cuspell_source.is_relative_to(BASE.parent.parent) else str(args.cuspell_source),
      "cuspell_glyphs_rendered":len(cuspell["items"]),
      "output":["01_runic_vs_alchemical.png",
                "02_runic_vs_alchemical_vs_cuspell.png"]
    }
    (REVIEWS/"comparison_manifest.json").write_text(
        json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print("PASS: source hashes, archive design counts, full Cuspell compare")
if __name__=="__main__":main()
