# news-image-20261123 — The World Today: Monday 23 November 2026

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Herman-234/news-image-23-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Herman-234/news-image-23-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261123)

One image summing up the world news of **Monday 23 November 2026**, for the
[make.fun bounty](https://make.fun/bounty/news-image-20261123)
($100, 50 places paid). `main.ts` (Node 22, standard library only) copies
`entry.png` to the output directory; `draw.py` is the generator that drew it
(Pillow, deterministic — same input, same bytes).

## The six stories

1. **Climate** — COP31 climate talks fail to reach a major deal as divisions deepen — *BBC News*
2. **USA** — Democrats win largest House majority since 1992 in the midterms — *BBC News*
3. **Ukraine** — Ukrainians search for missing after Russian strikes hit homes — *BBC News*
4. **Libya** — Explosion on Russian ship at Libya port blamed on suspected drone attack — *BBC News*
5. **South Korea** — South Korea education minister resigns over exam-cheating scandal — *BBC News*
6. **Indonesia** — Three killed, dozens missing after fire at Indonesian factory — *BBC News*

Headlines verified against the live BBC News world feed on 23 Nov 2026
(https://www.bbc.com/news/world). See `headlines.md` for timestamps.

## Run

```sh
python3 draw.py                      # regenerate entry.png (1024x1024)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
