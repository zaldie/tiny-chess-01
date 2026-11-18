# tiny-chess-01 — 4 KB chess engine

A complete chess engine in a single `main.py` (4,091 bytes), Python 3.13
stdlib only. It speaks HTTP to the make.fun environment (`POST /game`,
`/move`, `/resign`) and searches each position itself.

## How it works

- **Board:** 0x88, signed pieces, incremental material + tapered
  piece-square tables, Zobrist hashing, tempo bonus +10.
- **Search:** negamax alpha-beta, transposition table, 2 killer moves
  per ply, MVV-LVA + promotion ordering, quiescence (captures/promotions,
  all evasions in check), repetition detection, iterative deepening to a
  **fixed 120,000-node budget** — no clock, fully deterministic.
- **Speed:** `__slots__`, square-list move generation, castling-rights
  list — ~1.2x nodes/sec, so 120k costs about as much as 100k did.
- **Size:** source is lzma-compressed (FORMAT_ALONE, preset 9) and
  base85-encoded inside `main.py`, which only decompresses and runs it.
  No other file is read, imported, or executed.

## Grade locally

From the kit directory (`tiny-chess-01-kit`):

```
node cli/makefun.mjs grade-local --kit . --bot /path/to/tiny-chess-01 \
  --driver process --instances 3
```

Or run practice trials manually: start `program/env/server.mjs` with a
practice `gauntlet.json`, run `main.py` with `MAKEFUN_ENV_URL` set, then
score with `program/scorer/score.mjs`.

License: MIT (see LICENSE).
