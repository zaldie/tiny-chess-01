# Test report — tiny-chess-01 (practice trials, 6 games each)

Final `main.py`: **4,091 bytes** (limit 4,096). Tree total <= 8,192 bytes.

## Final engine (120,000 nodes/move; speed 1.2x + tempo +10)

| Trial | Elo | W-D-L | Losses vs |
|---|---|---|---|
| 0 | 1,654 | 5-0-1 | nodes-500k |
| 1 | 1,279 | 3-0-3 | nodes-100k, nodes-250k, nodes-500k |
| 2 | 2,112 | 6-0-0 | — |
| **Mean** | **1,682** | **14-0-4** | |

Sunfish-4k baseline mean ~1,325. Mean +192 vs the first engine (1,490).
Trial 2 is a clean 6-0-0 sweep — the first for any variant. Target 6-0-0
in all 3 trials: **not reached** (trial 1 drops 3 to the top rungs).

## Move times (env clock, full trials)

| Trial | moves | avg | max |
|---|---|---|---|
| 0 | 232 | 2.56 s | 3.82 s |
| 1 | 360 | 2.61 s | 4.32 s |
| 2 | 270 | 2.46 s | 4.19 s |

No move near the 10 s limit. No time losses.

## Determinism

Same position, fresh engine, same budget: identical move and node count
(start: `b1c3`, 120,000 nodes). Fully deterministic, no clock.

## Variants tried

- First engine @100k: mean 1,490 (12-1-5).
- dense_s (NMP+LMR+PVS): games 3-6, 5-1-7 vs 6-1-5 — worse. Dropped.
- dense_e (tempo + bishop pair): self-play +2 only; not run in env.
- dense_ft150 @150k: net -1.5 across trials. Dropped.
- engine1 @150k: 1,279, max move 7.39 s — too risky. Dropped.
- engine2/3/4/5/6, cut-down: 1,191-1,451, all dropped.
