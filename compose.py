#!/usr/bin/env python3
"""Compose the 24 Nov 2026 world-news front page (1024x1024 PNG).

Layout: masthead, lead story on the Gulf, hero illustration, four
more stories in two columns, an 'also' strip and a footer.
All text is rendered with PIL so the judge can read it exactly.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (22, 22, 22)
NAVY = (20, 33, 61)
RED = (163, 30, 34)
GREY = (90, 86, 78)
LINE = (200, 192, 176)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning list of lines fitting `width` px."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, width, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 40  # margin
CW = W - 2 * M  # content width

# ---- Masthead ----
d.rectangle([0, 0, W, 112], fill=NAVY)
d.text((M, 18), "THE WORLD", font=font(SERIF_B, 58), fill=(250, 247, 240))
d.text((M, 82), "IN ONE PAGE", font=font(SANS_B, 17), fill=(212, 175, 105))
date_txt = "TUESDAY, 24 NOVEMBER 2026"
dw = d.textlength(date_txt, font=font(SANS_B, 19))
d.text((W - M - dw, 30), date_txt, font=font(SANS_B, 19), fill=(250, 247, 240))
sub = "ONE IMAGE  ·  THE WHOLE DAY"
sw = d.textlength(sub, font=font(SANS, 15))
d.text((W - M - sw, 60), sub, font=font(SANS, 15), fill=(180, 190, 210))
d.rectangle([0, 112, W, 116], fill=RED)

y = 132
# ---- Lead kicker + headline ----
d.text((M, y), "THE GULF  —  LEAD STORY", font=font(SANS_B, 18), fill=RED)
y += 28
y = draw_para(d, M, y, CW, ["MISSILES OVER THE GULF"],
              font(SERIF_B, 56), INK, 62)
y += 4
deck = ("A Houthi strike hits a tower in Riyadh's financial district, wounding 11 — "
        "the second attack in under a week. In the Strait of Hormuz, four tankers "
        "are reported hit by mines as Iran warns shipping to keep clear.")
y = draw_para(d, M, y, CW, wrap(d, deck, font(SERIF, 23), CW),
              font(SERIF, 23), (48, 48, 48), 30)
y += 10

# ---- Hero illustration ----
hero = Image.open("hero.png").convert("RGB")
tw, th = 944, 258
# center-crop to target aspect
scale = max(tw / hero.width, th / hero.height)
hero = hero.resize((int(hero.width * scale), int(hero.height * scale)),
                   Image.LANCZOS)
left = (hero.width - tw) // 2
top = (hero.height - th) // 2
hero = hero.crop((left, top, left + tw, top + th))
img.paste(hero, (M, y))
d.rectangle([M, y, M + tw, y + th], outline=INK, width=2)
y += th + 8
cap = ("Tankers in the Strait of Hormuz, where four vessels were reported hit by mines "
       "on Tuesday. Illustration.")
y = draw_para(d, M, y, CW, wrap(d, cap, font(SANS, 15), CW),
              font(SANS, 15), GREY, 20)
y += 10
d.line([(M, y), (W - M, y)], fill=LINE, width=2)
y += 14

# ---- Two-column stories ----
stories = [
    ("HUAWEI GUILTY ON TRADE SECRETS",
     "A U.S. jury convicts the Chinese telecom giant of stealing trade "
     "secrets and bank fraud — but clears it of racketeering."),
    ("GAZA STRIKE KILLS HAMAS SECURITY CHIEF",
     "An Israeli air strike kills the group's internal security head in "
     "Gaza City, despite a ceasefire in place since last year."),
    ("UKRAINE HITS RUSSIAN SHIPS",
     "Drone strikes on a cargo ship in the Gulf of Finland and another off "
     "Libya raise the alarm across NATO."),
    ("FIVE DIE IN TURKISH HELICOPTER CRASH",
     "An air force helicopter goes down after take-off in western Türkiye. "
     "Gunmen hold 25 hostage in a Colombian supermarket."),
]
col_w = (CW - 24) // 2
row_h = 0
top_y = y
for i, (head, body) in enumerate(stories):
    cx = M + (i % 2) * (col_w + 24)
    cy = top_y + (i // 2) * 152
    d.text((cx, cy), head, font=font(SANS_B, 19), fill=RED)
    bl = wrap(d, body, font(SERIF, 20), col_w)
    draw_para(d, cx, cy + 28, col_w, bl, font(SERIF, 20), (48, 48, 48), 26)
    if i % 2 == 0:
        d.line([(cx + col_w + 12, cy), (cx + col_w + 12, cy + 140)],
               fill=LINE, width=1)
y = top_y + 2 * 152 + 2
d.line([(M, y), (W - M, y)], fill=LINE, width=2)
y += 12

# ---- Also strip ----
d.text((M, y), "ALSO:  ", font=font(SANS_B, 18), fill=RED)
ax = M + d.textlength("ALSO:  ", font=font(SANS_B, 18))
also = ("Senegal regain the Africa Cup  ·  Shenzhou 24 carries Pakistan's first astronaut")
y = draw_para(d, ax, y, W - M - ax, wrap(d, also, font(SANS, 17), W - M - ax),
              font(SANS, 17), (48, 48, 48), 23)
y += 8
d.line([(M, y), (W - M, y)], fill=LINE, width=2)
y += 10
foot = "The world on Tuesday 24 November 2026 — drawn from public news wires. One image, the whole day."
d.text((M, y), foot, font=font(SANS, 14), fill=GREY)

img.save("news.png", optimize=True)
print("saved news.png", img.size, "final footer y =", y)
