# Stage32 b16 weapon history

This ledger prevents algorithm-name churn from re-running equivalent failed ideas.

## Tried / frozen
- 18AF scheduler 1.0: improved 12 hard x1024 walls to 6; six remain.
- alternate scheduler 0.5 (#1425): worse overhead; rejected.
- 18AG lower48 cap-activity coordinate permutation: 0/6, 18M node cap.
- lower48 reverse permutation (18AI): representative scout failed to close.
- 18AH full pairwise exact symmetry Gram/KKT: 0/6; wallclock-heavy.
- 18AI pairwise-deep: representative scout failed to close.
- 18AJ clean baseline production: 0/6 at 18M.
- 18AK pairwise-cached: 0/6 at 18M.
- 18AK cap-sym-active: 0/6 at 18M.
- 18AK combined-active: 0/6 at 18M.

## Current distinct family
- 18AL lower48 integer unimodular basis reduction:
  - forward-greedy
  - reverse-greedy
  - alternating2

## Not yet tried as production families
- exact partial-assignment orbit / canonical-augmentation pruning from Aut group action;
- meet-in-the-middle / block enumeration redesign;
- more global lower48 lattice reduction beyond bounded elementary greedy shears.

Rule: unfinished algorithms are not promoted merely for lower runtime. COMPLETE is the closure criterion.
