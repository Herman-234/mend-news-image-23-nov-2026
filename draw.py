#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news poster as a 1024x1024 PNG.

My own layout: dark masthead, six story tiles in a 2x3 grid, each tile
with a coloured number disc, a region tag, the headline and its source.
Deterministic: same input -> same bytes. No network, no timestamps.
Run:  python3 draw.py   (writes entry.png beside this file)

Headlines verified against the live BBC News world feed, 23 Nov 2026:
 1. COP31 climate talks fail to reach a major deal (BBC, 02:17)
 2. Democrats win largest House majority since 1992 (BBC, 04:26)
 3. Ukrainians search for missing after Russian strikes (BBC, 01:57)
 4. Explosion on Russian ship at Libya port, suspected drone attack (BBC, 01:16)
 5. South Korea education minister resigns over exam scandal (BBC)
 6. Three killed, dozens missing after fire at Indonesian factory (BBC)
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

INK = (18, 24, 38)        # masthead
TEAL = (0, 128, 128)
PAPER = (238, 240, 243)
CARD = (255, 255, 255)
GREY = (90, 96, 108)
LINE = (200, 205, 212)
ACCENTS = [(196, 38, 38), (0, 90, 160), (150, 70, 170), (0, 120, 80), (190, 110, 0), (30, 110, 150)]

STORIES = [
    ("1", "CLIMATE", "COP31 climate talks fail to reach a major deal as divisions deepen", "BBC News"),
    ("2", "USA", "Democrats win largest House majority since 1992 in the midterms", "BBC News"),
    ("3", "UKRAINE", "Ukrainians search for missing after Russian strikes hit homes", "BBC News"),
    ("4", "LIBYA", "Explosion on Russian ship at Libya port blamed on suspected drone attack", "BBC News"),
    ("5", "SOUTH KOREA", "South Korea education minister resigns over exam-cheating scandal", "BBC News"),
    ("6", "INDONESIA", "Three killed, dozens missing after fire at Indonesian factory", "BBC News"),
]

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 118], fill=INK)
    d.rectangle([0, 118, W, 124], fill=TEAL)
    f_title = font(BOLD, 58)
    f_date = font(BOLD, 26)
    d.text((32, 16), "THE WORLD TODAY", font=f_title, fill=(255, 255, 255))
    d.text((32, 80), "MONDAY 23 NOVEMBER 2026  •  SIX STORIES THAT DEFINED THE DAY",
           font=f_date, fill=(140, 220, 220))
    # 2 x 3 grid of tiles
    pad, gap = 24, 20
    tw = (W - 2 * pad - gap) // 2
    th = 268
    top0 = 146
    f_num = font(BOLD, 30)
    f_tag = font(BOLD, 22)
    f_head = font(BOLD, 25)
    f_src = font(REG, 20)
    for i, (num, tag, head, src) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = pad + col * (tw + gap)
        y0 = top0 + row * (th + gap)
        x1, y1 = x0 + tw, y0 + th
        d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=CARD, outline=LINE, width=2)
        accent = ACCENTS[i]
        d.rectangle([x0, y0 + 14, x0 + 8, y1 - 14], fill=accent)
        # number disc
        cx, cy, r = x0 + 48, y0 + 46, 26
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=accent)
        tw_num = d.textlength(num, font=f_num)
        d.text((cx - tw_num / 2, cy - 21), num, font=f_num, fill=(255, 255, 255))
        d.text((x0 + 86, y0 + 30), tag, font=f_tag, fill=accent)
        lines = wrap(d, head, f_head, tw - 64)
        y = y0 + 88
        for ln in lines[:4]:
            d.text((x0 + 32, y), ln, font=f_head, fill=(20, 20, 20))
            y += 33
        d.text((x0 + 32, y1 - 38), "Source: " + src + "  •  23 Nov 2026",
               font=f_src, fill=GREY)
    # footer strip
    d.text((32, 992), "Six verified headlines — BBC News world feed, 23 November 2026",
           font=font(REG, 18), fill=GREY)
    img.save("entry.png", format="PNG", optimize=True)

if __name__ == "__main__":
    main()
