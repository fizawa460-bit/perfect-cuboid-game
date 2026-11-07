# 32R-44 d = 14 estimate and the ruling swap (2026-10-22, research)

- d = 14 Knuth estimate with the balanced-equality cut (n = 7): 91924 jobs (1083 nonempty), **1.37e14** nodes
  (d12 after cut 3.18e12). Dominant: 5|24|-16 29.7%, 5|22|-16 29.1%, 9|22|-16 11.0%, 7|22|-16 8.4% (g = 0 shell slices).
- The 6144 symmetry group has 3072 elements exchanging the V and H boundary curves (geometric subgroup: 768 of 1536).
  They map slice (n1, e) onto (d - n1, e). Earlier runs enumerated both orientations.
  Keeping only the cheaper orientation: d12 production part 1.06e12 -> 8.69e11 (x0.82); d14 1.37e14 -> 5.12e13 (x0.37).
- d12 production run restarted with SWAP_SKIP (15 slices skipped): 13148 jobs, producer 0658191d. The aborted run
  (3% of the weight) is kept as d12_run/results_v1_aborted.jsonl.
- d14 still ~1 month at the d12 rate; the g = 0 shell (c2 = -16) dominates, so the smooth-rational question matters
  even more there.

## 32R-45/46 enumerator speed tests (negative)
- Knuth estimates underestimate: completed d12 jobs have ~4.2x the estimated nodes (first 876 jobs); one job estimated
  < 3e8 took 3.84e9. The earlier "3 days / 18 h" figures were too low; real d12 (c2 >= -12) looks like ~1 week.
- LLL Gram-Schmidt profile is already flat (1..4, n = 53): BKZ cannot help; fpylll BKZ on the Gram gave a worse profile.
- Coordinate order (job 6|18|-12|1092, exact): LLL order 3.84e9 nodes; influence-last, influence-first, reversed all
  > 8e9 (stopped at the node limit). The production order is the best tested. Reordering abandoned.
