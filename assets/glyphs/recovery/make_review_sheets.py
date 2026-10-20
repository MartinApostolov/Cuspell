#!/usr/bin/env python3
"""Create review PNGs from recovered glyph SVG files, visibly marking provenance."""
from pathlib import Path
import io, json, math
from PIL import Image, ImageDraw, ImageFont
import cairosvg

root = Path(__file__).resolve().parent
src = json.loads((root / "source_geometry.json").read_text())
out = root / "generated"
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 27)
except OSError:
    font = small = header = ImageFont.load_default()
colors = {
    "EXACT_V013":"#2ca57c",
    "EXACT_V014_R1":"#2379ae",
    "APPROVED_NEW_VECTOR":"#387bb8",
    "RETIRED_DUPLICATE_MIRROR":"#9aa5ab",
    "SCREENSHOT_TRACED":"#2ca57c",
    "SCREENSHOT_TENTATIVE_ID":"#c58a34",
    "DESCRIPTION_APPROX":"#d68836",
    "ACCEPTED_DESCR_APPROX":"#d87352",
    "UNREVIEWED_DESCR_APPROX":"#548fe0",
}
def sheet(first, last, columns=5):
    rows = math.ceil((last-first+1)/columns)
    w = 32 + columns*208
    h = 100 + rows*234
    image = Image.new("RGB", (w,h), "#f6f8f8")
    draw = ImageDraw.Draw(image)
    draw.text((32,15), f"CUSPELL • RECOVERED v0.19 · G{first:03}–G{last:03}", font=header, fill="#1c3641")
    draw.text((32,57), "Source: exact v0.13 or v0.14 R1 / screenshot trace / prose — NOT original v0.19", font=small, fill="#586b76")
    for n in range(first,last+1):
        x = 32 + ((n-first)%columns)*208
        y = 89 + ((n-first)//columns)*234
        id = f"G{n:03}"
        record = src["glyphs"][id]
        retired=record.get("lifecycle")=="retired"
        color = colors[record["confidence"]]
        draw.rounded_rectangle([x,y,x+198,y+221],radius=14,fill=("#f2f4f5" if retired else "#ffffff"),outline=color,width=2)
        if not retired:
            svg=(out/"glyphs"/f"{id}.svg").read_bytes()
            png = cairosvg.svg2png(bytestring=svg, output_width=165,output_height=169)
            glyph = Image.open(io.BytesIO(png)).convert("RGBA")
            image.paste(glyph,(x+16,y+6),glyph)
        else:
            draw.text((x+50,y+80),"RETIRED",font=font,fill="#7d878d")
        draw.text((x+16,y+180),id,font=font,fill="#263c46")
        if not retired:
            draw.text((x+93,y+185),record["confidence"].replace("_APPROX","").replace("SCREENSHOT_",""),font=small,fill="#657989")
    outfile=out/(f"Cuspell_Recovery_G{first:03}_G{last:03}.png" if first>1 else "Cuspell_Recovery_Full_Inventory.png")
    image.save(outfile)
    print(outfile.name)
for first,last,cols in ((1,150,10),(81,110,5),(111,120,5),(121,130,5),(131,140,5),(141,150,5)):
    sheet(first,last,cols)
