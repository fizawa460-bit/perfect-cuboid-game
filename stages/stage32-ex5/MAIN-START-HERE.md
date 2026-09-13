# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order: `AGENTS.md`; `stages/stage32/COMMANDS.md`; current `stages/stage32/MAIN-STATE.json`; `stages/stage32/proof/CROSS-LANE-DEMANDS.json`; `stages/stage32-ex5/CROSS-LANE-STATE.json` when present; `README.md`; this file; `MAINBATCH-OPERATIONS.md`; `MAIN-STATE.json`; then only the active EX5 working set.

PR #1776 remains active/open/draft/unmerged. Merge is not authorized.

## Cross-lane demand priority

Before local work, inspect every OPEN demand with `producer_lane=EX5`. A higher-priority OPEN producer demand preempts lower-priority local work. A SATISFIED demand is only an operational handoff and **does not grant mathematical credit**. `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` remains SATISFIED and there are no OPEN EX5 producer demands.

## Current authority

Stage32 MAIN remains `STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED`, FULL178 incomplete, with no EX5 auto-promotion. Current observed main is `4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c`; its net content drift from the BC2-36 audit setup does not alter the source-locked Stage32 MAIN authority blob.

BC2-36 hostile audit PASS is consumed:

- audited exact head `9c63ccb48dd0e5bdeedda7739dd05e2404698465`;
- review `5188625406`;
- `11 UNSAT / 41 UNKNOWN / 0 SAT`;
- audited known parent-UNSAT lower bound `7295`;
- remaining 41 UNKNOWN hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`.

## BC2-37 cold execution boundary

BC2-37 targets exactly those 41 hostile-audited UNKNOWN parents. The producer is source-locked, timeout is `120000 ms` per parent, effective heavy concurrency is `1`, and heavy scaleout is forbidden. The cold runkey is generation 0 / `armed=false`; therefore cold exact-head CI must skip BC2-37 heavy execution.

Only after cold exact-head CI succeeds may `stage32ex5-mainbatch` advance the runkey to generation 1 / `armed=true`. That semantic runkey change is the sole automatic heavy authorization path. While heavy execution is active, the branch head must remain fixed.

BC2-38 is blocked until a retained BC2-37 result receives hostile-audit PASS. UNKNOWN remains UNKNOWN. No whole-first-block/FULL178 closure, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.
