# Stage32 b16 weapon history

This ledger prevents equivalent failed ideas from being re-run under new names.

## Tried / frozen
- 18AF scheduler 1.0: improved 12 hard x1024 walls to 6; six remain.
- scheduler 0.5 (#1425): worse exact-check overhead; rejected.
- 18AG lower48 coordinate permutation: 0/6 at 18M.
- 18AI lower48 reverse permutation: no representative closure.
- 18AH full pairwise exact symmetry Gram/KKT: 0/6; wallclock-heavy.
- 18AI pairwise-deep: no representative closure.
- 18AJ baseline production: 0/6 at 18M.
- 18AK pairwise-cached: 0/6 at 18M.
- 18AK cap-sym-active: 0/6 at 18M.
- 18AK combined-active: 0/6 at 18M.
- 18AM constraint-directed lower48 basis variants (12 modes): 0 COMPLETE at 6M on p436/s5. This COMPLETE-only scout is retained as one-hit-breakthrough evidence only, not proof that all variants are useless at larger budgets.
- 18AL lower48 integer unimodular basis reduction, seven full-budget p436/s5 weapons: 0/7 COMPLETE at 18M. All seven ended RESOURCE_WALL_NODE_CAP. Run 33133446912; summary artifact 9672002328; digest sha256:ab3d2f12c0e66d4c64a4ffd60356597f1549a4fa9b393fc186553459883055. Frozen: do not retry forward/reverse/alternating2 basis shears or their pairwise-cached/cap-sym-active combinations under renamed variants.

## In flight / current
- 18AN progressive higher-order active-set scout: baseline control plus pair-capcap, triple-cap, triple-sym, triple-mixed at 1M/3M/6M.

## Important non-new route
- Aut symmetry is already materially present in the immutable b16 source via 256 exact symmetry breakers. Earlier b6 profiling established Aut order 1536 and strong canonical-augmentation compression. Do not relabel ordinary Aut breaker reuse as a new weapon.

## Distinct architectural families still not production-tested on the six b16 walls
- true partial-assignment orbit/stabilizer canonical augmentation beyond the existing fixed breaker bundle, only if shard-preserving exact action on current DFS coordinates is established;
- meet-in-the-middle / block enumeration redesign;
- resumable prefix/block certification that changes total recomputation architecture rather than merely traversal order.

Rule: unfinished algorithms are never promoted merely for lower runtime. Progressive scouts may mark `PROMISING` only from structural work-consumption metrics relative to an explicit baseline; full-budget confirmation is still required.
