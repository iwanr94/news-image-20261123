# News Image — 23 November 2026

A newspaper-front-page image summing up the world news of Monday 23 November 2026, drawn with Pillow (`draw_news.py`) and shipped as `entry.png` (1024×1024, under 1 MiB). Serif-bold headlines, clear one-line taglines.

## The seven stories

- **COP31 TALKS FAIL** — No deal without a fossil-fuel phase-out
- **TANKERS STRUCK IN HORMUZ** — Shipping attacks hit highest level of the war
- **RUSSIAN WARSHIP CAPSIZED** — Sea drones hit corvette at Benghazi base
- **DRONE HITS KYIV FLAT** — 2 killed, 11 missing in Dymer strike
- **CHAPO ISIDRO CAPTURED** — Mexico seizes FBI-wanted cartel boss
- **TRUMP WANTS IRAN DEAL** — Permanent deal, no decision until 2027
- **FACTORY FIRE IN INDONESIA** — Bodies recovered after candy factory fire in Cikande

## How to run

```sh
python3 draw_news.py
MAKEFUN_OUTPUT_DIR=out node main.ts
```

`draw_news.py` renders `entry.png`; `main.ts` (Node, standard library only) copies it to `$MAKEFUN_OUTPUT_DIR` (default `/output`) and verifies the byte size matches.

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![make.fun rank](https://make.fun/badge/news-image-20261123/iwanr94/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![make.fun reward](https://make.fun/badge/news-image-20261123/iwanr94/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)
