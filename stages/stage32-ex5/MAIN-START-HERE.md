# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order: `AGENTS.md` -> `stages/stage32-ex5/README.md` -> this file -> `MAINBATCH-OPERATIONS.md` -> `MAIN-STATE.json` -> only the active working set. Historical Cycle1 files remain source-locked provenance.

## Current authority

PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3` is the sole Stage32EX5 MAINBATCH surface. Current `main` is `6bad01a45b3c57d8697df79c1790bd2f30af68de`, containing merged Stage32 MAIN #1753. N355 is consumed authority; N356 is `AUDIT_REQUIRED` and deferred with zero MAIN pruning credit. The e=4 exact local prefix is `0..797`.

## Executable boundary

The executable boundary is `BC2-24` retained merge checkpoint. Its exact retained result is: 4 newly UNSAT parents, `19` retained UNKNOWN, 0 SAT; known parent-UNSAT lower bound `7145`; `172` other BC2-19 UNKNOWN identities remain uninferred. The whole first block, whole stratum, and FULL178 remain open.

Read only:
- `breadth-cycle-2/bc2-24-explicit-fibre-degree-partition-checkpoint.json`
- `breadth-cycle-2/bc2-24-explicit-fibre-degree-partition-preflight.json`
- `breadth-cycle-2/bc2_24_explicit_fibre_degree_partition.py`
- `runkeys/bc2-24-explicit-fibre-degree-partition.json`
- `verify_main_state.py`

## Stop rule

Do not open BC2-25, do not rerun prior BC2 units, and do not broaden research on PR #1765. Merge is the priority: make integrity/lifecycle checks green, perform hostile re-audit on the frozen exact head, then merge PR #1765. UNKNOWN must not be relabelled UNSAT. No Stage32 MAIN, N350, theorem, receiver, effectivity, endpoint, or Perfect Cuboid credit follows from this checkpoint.
