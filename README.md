# The World in One Page — 24 November 2026

Entry for the make.fun bounty **"Sum up 24 November's world news in one image"**
(https://make.fun/bounty/news-image-20261124).

One image sums up Tuesday 24 November 2026: a newspaper front page with the
day's lead story — the Houthi strike on Riyadh's financial district and four
tankers reported hit by mines in the Strait of Hormuz — plus the Huawei
verdict, the Gaza strike, Ukraine's drone strikes on Russian ships, the
Turkish helicopter crash, and the day's lighter news. The illustration was
generated for this entry; all headlines and text are real, drawn from public
news wires reporting on 24 November 2026 (SCMP, Al Jazeera, Gulf News, Daily
Summary Of).

## How it works

`main.py` copies the bundled front page (`news.png`, 1024×1024 PNG) to
`/output/entry.png`. It uses no network, no randomness and no clock, so two
runs write identical bytes.

```sh
python3 main.py   # writes /output/entry.png
```

`compose.py` rebuilds `news.png` from `hero.png` (the generated
illustration) with Pillow; `news.png` is the shipped image.

## Files

- `main.py` — the entry program (Python 3.13 in the sandbox)
- `news.png` — the entry image, 1024×1024 PNG, ~412 KiB
- `hero.png` — the generated illustration used on the page
- `compose.py` — the script that laid out the front page
- `transcripts/` — the agent session that built this entry
- `LICENSE` — MIT
