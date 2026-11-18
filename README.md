# tiny-chess-01 — 4 KB chess engine

A complete chess engine in one `main.py` (4,091 bytes), Python 3.13
stdlib only. It speaks HTTP to the make.fun env (`POST /game`, `/move`,
`/resign`) and searches each position itself.

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

From the kit directory:

```
node cli/makefun.mjs grade-local --kit . --bot /path/to/tiny-chess-01 \
  --driver process --instances 3
```

License: MIT (see LICENSE).
