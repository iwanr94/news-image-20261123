"""Draw the 23 November 2026 world-news front page (1024x1024).

Build tool only: renders entry.png locally with Pillow.
The grader entrypoint is main.ts (Node stdlib), not this file.
No network, no numpy. Verified stories only, per news-brief.txt.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (18, 35, 63)
PAPER = (247, 241, 222)
INK = (30, 36, 48)
RED = (179, 64, 46)
BLUE = (46, 94, 140)
GOLD = (200, 155, 60)
TEAL = (46, 125, 107)
SKY = (191, 217, 232)
SEA = (58, 110, 150)
GREY = (90, 96, 110)
WHITE = (255, 255, 255)
CREAM = (253, 250, 240)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(n, bold=False):
    return ImageFont.truetype(SANSB if bold else SANS, n)


def wrap(d, text, fnt, max_w):
    """Wrap text into lines fitting max_w pixels."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(d, cx, y, text, fill, fnt):
    d.text((cx - d.textlength(text, font=fnt) / 2, y), text,
           fill=fill, font=fnt)


def panel(d, x, y, w, h, accent):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10,
                        fill=CREAM, outline=accent, width=3)
    d.rectangle([x, y, x + w, y + 8], fill=accent)


def title_block(d, x, y, w, title, accent):
    """Title in up to 2 lines, bold, centred."""
    lines = wrap(d, title, font(18, True), w - 12)[:2]
    yy = y
    for ln in lines:
        centered(d, x + w // 2, yy, ln, INK, font(18, True))
        yy += 22
    return yy


def caption_block(d, x, y, w, text, max_lines=3):
    lines = wrap(d, text, font(16), w - 16)[:max_lines]
    yy = y
    for ln in lines:
        centered(d, x + w // 2, yy, ln, INK, font(16))
        yy += 20
    return yy


def draw_banner(d):
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.rectangle([0, 96, W, 102], fill=GOLD)
    centered(d, W // 2, 12, "23 NOVEMBER 2026", WHITE, font(46, True))
    centered(d, W // 2, 66, "W O R L D   N E W S", GOLD, font(18, True))


def draw_lead(d, x, y, w, h):
    """COP31 talks fail: globe with smoke over a broken talks table."""
    panel(d, x, y, w, h, RED)
    # Globe, left side
    cx, cy, r = x + 150, y + 150, 92
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLUE,
              outline=NAVY, width=4)
    d.ellipse([cx - 52, cy - 58, cx + 6, cy - 6], fill=TEAL)
    d.ellipse([cx - 6, cy + 8, cx + 58, cy + 62], fill=TEAL)
    d.ellipse([cx + 18, cy - 62, cx + 62, cy - 18], fill=TEAL)
    d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=WHITE, width=3)
    # Smoke rising from the globe
    for i, (sx, sy, sr) in enumerate([(cx + 70, cy - 78, 16),
                                      (cx + 96, cy - 104, 21),
                                      (cx + 74, cy - 132, 26)]):
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr],
                  fill=(150, 150, 150))
    # Broken talks table, right of globe
    tx = x + 300
    d.rectangle([tx, y + 190, tx + 330, y + 206], fill=(120, 82, 50))
    d.rectangle([tx + 16, y + 206, tx + 32, y + 252], fill=(120, 82, 50))
    d.rectangle([tx + 282, y + 206, tx + 298, y + 252], fill=(120, 82, 50))
    # Crack through the table: jagged gap
    d.polygon([(tx + 150, y + 190), (tx + 168, y + 206),
               (tx + 158, y + 190)], fill=PAPER)
    d.polygon([(tx + 150, y + 206), (tx + 168, y + 190),
               (tx + 160, y + 206)], fill=RED)
    # Cracked leaf on the table
    d.ellipse([tx + 60, y + 130, tx + 130, y + 182], fill=TEAL)
    d.line([tx + 62, y + 180, tx + 128, y + 132], fill=NAVY, width=3)
    d.line([tx + 96, y + 156, tx + 96, y + 132], fill=NAVY, width=2)
    d.line([tx + 96, y + 156, tx + 118, y + 172], fill=NAVY, width=2)
    # Labels, right side
    lx = x + 330
    d.text((lx, y + 22), "COP31 TALKS FAIL", fill=RED, font=font(40, True))
    d.text((lx, y + 78), "No deal without a fossil-fuel phase-out",
           fill=INK, font=font(21))


def art_tanker(d, x, y, w):
    cy = y + 160
    d.rectangle([x + 10, cy - 10, x + w - 10, cy + 46], fill=SEA)
    d.rectangle([x + 34, cy - 52, x + w - 34, cy - 8], fill=(40, 44, 54))
    d.polygon([(x + w - 34, cy - 52), (x + w - 14, cy - 8),
               (x + w - 34, cy - 8)], fill=(40, 44, 54))
    d.rectangle([x + 52, cy - 78, x + 96, cy - 52], fill=WHITE)
    d.rectangle([x + 110, cy - 66, x + 150, cy - 52], fill=GOLD)
    # Flames on deck
    d.polygon([(x + 150, cy - 52), (x + 168, cy - 92), (x + 186, cy - 52)],
              fill=(230, 120, 30))
    d.polygon([(x + 162, cy - 52), (x + 176, cy - 78), (x + 190, cy - 52)],
              fill=(240, 200, 60))
    d.ellipse([x + 158, cy - 96, x + 188, cy - 66], fill=(150, 150, 150))
    d.ellipse([x + 176, cy - 116, x + 204, cy - 90], fill=(170, 170, 170))
    d.line([x + 10, cy + 46, x + w - 10, cy + 46], fill=WHITE, width=3)


def art_warship(d, x, y, w):
    cy = y + 150
    d.rectangle([x + 10, cy, x + w - 10, cy + 40], fill=SEA)
    # Hull listing to starboard (tilted polygon)
    d.polygon([(x + 30, cy - 30), (x + w - 40, cy - 58),
               (x + w - 20, cy - 18), (x + 46, cy + 6)], fill=(90, 96, 110))
    d.rectangle([x + 78, cy - 78, x + 92, cy - 44], fill=(70, 76, 90))
    d.rectangle([x + 120, cy - 66, x + 150, cy - 44], fill=(70, 76, 90))
    d.polygon([(x + 84, cy - 78), (x + 84, cy - 104), (x + 96, cy - 78)],
              fill=RED)
    d.ellipse([x + 130, cy - 100, x + 158, cy - 72], fill=(150, 150, 150))
    d.line([x + 30, cy + 40, x + w - 30, cy + 40], fill=WHITE, width=3)


def art_flat(d, x, y, w):
    bx, by = x + (w - 120) // 2, y + 60
    d.rectangle([bx, by, bx + 120, by + 130], fill=(196, 164, 120))
    d.rectangle([bx, by, bx + 120, by + 130], outline=INK, width=2)
    for r in range(5):
        for c in range(3):
            wx, wy = bx + 14 + c * 38, by + 10 + r * 24
            d.rectangle([wx, wy, wx + 22, wy + 14],
                        fill=GOLD if (r + c) % 2 else (90, 110, 140))
    # Damaged top corner, one smoke puff above it
    d.polygon([(bx + 84, by), (bx + 120, by), (bx + 120, by + 34),
               (bx + 100, by + 18)], fill=(60, 56, 52))
    d.ellipse([bx + 92, by - 22, bx + 122, by + 6], fill=(150, 150, 150))
    # Rubble at the base
    d.polygon([(bx - 8, by + 130), (bx + 30, by + 130),
               (bx + 12, by + 152)], fill=(120, 116, 110))
    d.polygon([(bx + 40, by + 130), (bx + 90, by + 130),
               (bx + 66, by + 154)], fill=(100, 96, 90))


def art_handcuffs(d, x, y, w):
    cx = x + w // 2
    d.ellipse([cx - 78, y + 78, cx - 18, y + 138], outline=INK, width=8)
    d.ellipse([cx + 18, y + 78, cx + 78, y + 138], outline=INK, width=8)
    d.line([cx - 18, y + 108, cx + 18, y + 108], fill=INK, width=8)
    d.rectangle([cx - 8, y + 96, cx + 8, y + 120], fill=GOLD)
    # Police badge above
    d.polygon([(cx - 26, y + 44), (cx + 26, y + 44), (cx + 18, y + 72),
               (cx, y + 84), (cx - 18, y + 72)], fill=GOLD)
    d.ellipse([cx - 8, y + 54, cx + 8, y + 70], fill=NAVY)


def art_flags(d, x, y, w):
    cx = x + w // 2
    # Flag poles
    d.rectangle([cx - 74, y + 56, cx - 70, y + 150], fill=INK)
    d.rectangle([cx + 70, y + 56, cx + 74, y + 150], fill=INK)
    # Left flag: stripes with a blue canton (US hint)
    fx = cx - 118
    for i, col in enumerate([RED, WHITE, RED, WHITE, RED, WHITE, RED]):
        d.rectangle([fx, y + 56 + i * 6, cx - 70, y + 62 + i * 6], fill=col)
    d.rectangle([fx, y + 56, fx + 20, y + 76], fill=NAVY)
    for dy in (4, 12):
        for dx in (5, 13):
            d.ellipse([fx + dx, y + 56 + dy, fx + dx + 3, y + 59 + dy],
                      fill=WHITE)
    # Right flag: green-white-red horizontal bands (Iran hint)
    gx = cx + 70
    d.rectangle([gx, y + 56, gx + 48, y + 70], fill=(35, 140, 70))
    d.rectangle([gx, y + 70, gx + 48, y + 84], fill=WHITE)
    d.rectangle([gx, y + 84, gx + 48, y + 98], fill=RED)
    # Handshake below the flags, no faces
    d.polygon([(x + 28, y + 138), (cx - 16, y + 152),
               (cx - 16, y + 176), (x + 28, y + 166)], fill=NAVY)
    d.polygon([(x + w - 28, y + 138), (cx + 16, y + 152),
               (cx + 16, y + 176), (x + w - 28, y + 166)], fill=(60, 60, 66))
    d.ellipse([cx - 26, y + 146, cx + 26, y + 182], fill=(212, 178, 138),
              outline=INK, width=2)
    d.line([cx - 12, y + 152, cx - 12, y + 176], fill=INK, width=2)
    d.line([cx + 2, y + 152, cx + 2, y + 176], fill=INK, width=2)


STORIES = [
    ("TANKERS STRUCK IN HORMUZ",
     "Shipping attacks hit highest level of the war", art_tanker, BLUE),
    ("RUSSIAN WARSHIP CAPSIZED",
     "Sea drones hit corvette at Benghazi base", art_warship, RED),
    ("DRONE HITS KYIV FLAT",
     "2 killed, 11 missing in Dymer strike", art_flat, GOLD),
    ("CHAPO ISIDRO CAPTURED",
     "Mexico seizes FBI-wanted cartel boss", art_handcuffs, TEAL),
    ("TRUMP WANTS IRAN DEAL",
     "Permanent deal, no decision until 2027", art_flags, BLUE),
]


def draw_small(d, x, y, w, h, title, tag, art, accent):
    panel(d, x, y, w, h, accent)
    title_block(d, x, y + 14, w, title, accent)
    art(d, x, y, w)
    caption_block(d, x, y + 218, w, tag)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_banner(d)
    draw_lead(d, 16, 112, 992, 268)
    # Row 1: three panels
    for i, x in enumerate([16, 350, 684]):
        title, tag, art, accent = STORIES[i]
        draw_small(d, x, 392, 322, 296, title, tag, art, accent)
    # Row 2: two wider panels
    for j, x in enumerate([16, 518]):
        title, tag, art, accent = STORIES[3 + j]
        draw_small(d, x, 700, 490, 296, title, tag, art, accent)
    img.save("entry.png")
    print("wrote entry.png", img.size, img.mode)


if __name__ == "__main__":
    main()
