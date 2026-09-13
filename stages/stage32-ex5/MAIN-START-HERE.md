# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order: `AGENTS.md`; `stages/stage32/COMMANDS.md`; current `stages/stage32/MAIN-STATE.json`; `stages/stage32/proof/CROSS-LANE-DEMANDS.json`; `stages/stage32-ex5/CROSS-LANE-STATE.json` when present; `README.md`; this file; `MAINBATCH-OPERATIONS.md`; `MAIN-STATE.json`; then only the active EX5 working set.

PR #1776 remains active/open/draft/unmerged. Merge is not authorized.

## Cross-lane demand priority

Before local work, inspect every OPEN demand with `producer_lane=EX5`. A higher-priority OPEN producer demand preempts lower-priority local work. A SATISFIED demand is only an operational handoff and **does not grant mathematical credit**. `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` remains SATISFIED and there are no OPEN EX5 producer demands.

## Current authority

Stage32 MAIN remains `STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED`, FULL178 incomplete, with no EX5 auto-promotion. Current observed main is `4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c`; EX5 does not mutate Stage32 MAIN authority.

BC2-37 hostile audit PASS is consumed:

- audited exact head `9852fcec959962607da3290100291a60185e7104`;
- review `5189412496`;
- `7 UNSAT / 34 UNKNOWN / 0 SAT`;
- audited known parent-UNSAT lower bound `7302`;
- remaining 34 UNKNOWN hash `b2b0d1ef7d667fc380457818aa352e770f41fcdef7ca34c9ea88372c3193f891`.

## BC2-38 hostile-audit boundary

BC2-38 replayed exactly those 34 hostile-audited UNKNOWN parents at `140000 ms` per parent with effective heavy concurrency `1` and no scaleout. Execution head `d26a27e8564458f3d575ec58601b2226fc23944f`, workflow `34742297972`, authorizer `103683927278`, compute `103683975497`, artifact `10313851431` belong to the retained execution receipt.

The retained result is `4 UNSAT / 30 UNKNOWN / 0 SAT`. Candidate lower bound `7306` is not yet consumable; audited lower bound remains `7302` until BC2-38 hostile audit PASS. Remaining 30 UNKNOWN hash is `d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7`. UNKNOWN remains UNKNOWN.

The BC2-38 runkey is consumed/disarmed, the BC2-38 heavy path is retired, and V30 is frozen with `new_audit_boundary_exists=true`, `freeze_active=true`, and `re_audit_required=true`. BC2-39 is blocked until BC2-38 hostile audit PASS.

No whole-first-block/whole-stratum/FULL178 closure, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.

Next command: `stage32ex5-audit`.
