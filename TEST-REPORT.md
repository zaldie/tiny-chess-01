# Test report — tiny-chess-01 (practice trials, 6 games each)

Final `main.py`: **4,094 bytes** (limit 4,096). Tree under 8,192 bytes.

## Final engine — sr_nmp (null-move pruning R=3, 120,000 nodes/move)

| Trial | Elo | W-D-L | Spare | Dropped vs |
|---|---|---|---|---|
| 0 | 1,809 | 5-1-0 | 527 | draw vs nodes-500k |
| 1 | 2,112 | 6-0-0 | 579 | — (clean sweep) |
| 2 | 1,545 | 4-1-1 | 458 | draw vs nodes-250k, loss vs nodes-500k |
| **Mean** | **1,822** | **15-2-1** | | |

Sunfish-4k baseline mean ~1,325. Mean +140 vs dense_ft (1,682),
+332 vs first engine (1,490).

## Move times

No time losses in any full trial. Mini-trial re-run (trial 1 games
5,6, solo): avg 2.83 s, max 4.19 s — well under the 10 s limit.

## Determinism

Same position, fresh engine, same budget: identical move and node
count. Fully deterministic, no clock.

## Variants tried

- First engine @100k: mean 1,490 (12-1-5).
- dense_ft @120k: mean 1,682 (14-0-4), trial 2 = 6-0-0. Superseded
  by sr_nmp (backup: dense_ft_main.py in tiny-chess-01-dev/).
- sr_nmp (NMP R=3): **this engine**, mean 1,822 (15-2-1), trial 1
  = 6-0-0.
- sr_pvs (PVS only): selfplay 12-4-4; mini trial 1 1-1. Dropped.
- sr_nmppvs (NMP+PVS): pack 4,074, but selfplay vs dense 7-5-8
  and mini trial 1 0-0-2 (game 6 lost by TIME, max 12.69 s).
  Dropped — PVS hurts game 5 and risks timeouts.
- dense_s, LMR, check extension, eval variants: dropped in round 3
  (see sr_REPORT.md in tiny-chess-01-dev/).
