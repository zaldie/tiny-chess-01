# tiny-chess-01 — 4 KB chess engine

A complete chess engine in a single `main.py` (3,361 bytes), Python 3.13
stdlib only. It speaks HTTP to the make.fun environment (`POST /game`,
`/move`, `/resign`) and searches each position itself.

## How it works

- **Board:** 0x88, signed pieces, incremental material + tapered
  piece-square tables, Zobrist hashing, tempo bonus +10.
- **Search:** negamax alpha-beta, null-move pruning (R=3),
  transposition table, 2 killer moves per ply, MVV-LVA + promotion
  ordering, quiescence, repetition detection, iterative deepening to
  a **fixed 120,000-node budget** — no clock, fully deterministic.
- **Speed:** `__slots__`, square-list move generation — ~1.2x
  nodes/sec, so 120k costs about as much as 100k did.
- **Size:** source is packed with the kit's `makefun compress`
  (LZMA stream in a latin-1 string) inside `main.py`, which only
  decompresses and runs it.
  No other file is read, imported, or executed.

## Grade locally

From the kit directory (`tiny-chess-01-kit`):

```
node cli/makefun.mjs grade-local --kit . --bot /path/to/tiny-chess-01 \
  --driver process --instances 3
```

License: MIT (see LICENSE).
