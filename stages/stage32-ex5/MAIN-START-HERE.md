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

## BC2-37 hostile-audit boundary

BC2-37 replayed exactly those 41 hostile-audited UNKNOWN parents at `120000 ms` per parent with effective heavy concurrency `1` and no scaleout. Execution head `52dfcb0ae986dac1b27998349feb97171c30be1b`, workflow `34728149823`, authorizer `103645902953`, compute `103645956700`, artifact `10309795138` all belong to the retained execution receipt.

The retained result is `7 UNSAT / 34 UNKNOWN / 0 SAT`. The candidate lower bound `7302` is not yet consumable; the audited lower bound remains `7295` until BC2-37 hostile audit PASS. Remaining 34 UNKNOWN hash is `b2b0d1ef7d667fc380457818aa352e770f41fcdef7ca34c9ea88372c3193f891`. UNKNOWN remains UNKNOWN.

The BC2-37 runkey is consumed/disarmed, the BC2-37 heavy path is retired, and V28 is frozen with `new_audit_boundary_exists=true`, `freeze_active=true`, and `re_audit_required=true`. BC2-38 is blocked until BC2-37 hostile audit PASS.

No whole-first-block/whole-stratum/FULL178 closure, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.

Next command: `stage32ex5-audit`.
