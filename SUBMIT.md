# Submission checklist — news-image-20261124

Bounty: **Sum up 24 November's world news in one image**
https://make.fun/bounty/news-image-20261124
Prize: $100 USDC in escrow (50 places paid: 1st $20, 2nd $12, 3rd $6,
4th–10th $2, 11th–50th $1.20). **Deadline: Thu 26 Nov 2026, 00:00 UTC
(08:00 CST).** Max 10 submissions/day, 20 total; last submission before the
deadline is the final entry.

## What is ready in this folder

- `main.py` — deterministic entry program (copies `news.png` to
  `/output/entry.png`, no network). Tested: two runs, identical sha256.
- `news.png` — 1024×1024 PNG, 421,828 bytes (limit 1 MiB). Verified visually.
- `hero.png`, `compose.py` — illustration source + layout script.
- `LICENSE` (MIT), `README.md`.
- `transcripts/session-2026-11-26.json` — handed-over session file (fallback).

## Still to do (needs the top-level agent / the user)

1. **GitHub repo**: create a new public repo under **@haoyi0323** (the
   competition opened 23 Nov, so a repo created now qualifies), push this
   folder, record the full 40-char commit SHA.
2. **API key / account decision**: entry needs a make.fun API key
   (`af_...`) and a Solana keypair. Two options:
   - Enter under the existing account **@coral-comet-92-6766** (Google
     sign-in, haoyifang0323@gmail.com) — needs the connect flow and the
     GitHub push above.
   - Or a Muse-owned keypair account — the prize money belongs to Muse
     anyway (user's decision 26 Nov 2026: "这笔钱是你用来养活你的"), so
     this may be the cleaner long-term setup. Decide before submitting.
3. **Transcripts — IMPORTANT**: this competition has
   `handed_over_places: "none"`. A handed-over session (the file in
   `transcripts/`) is ranked but **takes no paid place**. To compete for
   money, the top-level agent must run the kit's bundle with
   `--muse-usage` so the recorded Muse sessions (top-level + this
   subagent) go up as a real bundle. Do not submit with the handed-over
   file alone if the prize matters.
4. **Submit** with the kit (`node cli/makefun.mjs submit`) or the API
   before the deadline; run `check` first and fix anything it flags.
5. **Wallet (later, only if we win)**: prize is USDC on Solana. Build a
   Muse-owned Solana wallet at claim time and keep the books under
   Muse's name. The user has no overseas account and does not take part
   in receiving the money. Nothing to do now.
