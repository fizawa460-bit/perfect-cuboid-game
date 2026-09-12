# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. current `stages/stage32/MAIN-STATE.json`;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. `stages/stage32-ex5/CROSS-LANE-STATE.json` when present;
6. `stages/stage32-ex5/README.md`;
7. this file;
8. `MAINBATCH-OPERATIONS.md`;
9. `stages/stage32-ex5/MAIN-STATE.json`;
10. only the active EX5 working set required by the selected route.

PR #1776 remains active/open/draft/unmerged. Historical Cycle1 files remain source-locked provenance.

## Cross-lane demand priority

Before local EX5 research, inspect every OPEN demand with `producer_lane=EX5`. A higher-priority OPEN producer demand (that is, an OPEN demand for which EX5 is the producer) preempts lower-priority local work. A SATISFIED demand is only an operational handoff and **does not grant mathematical credit**.

At current MAIN `e4d3b8b83626526ffeccdbd9c956081735fe1a6e`, `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` is **SATISFIED** and there are no OPEN EX5 producer demands. The frozen BC2-36 hostile-audit boundary may therefore continue.

## Current authority

Current Stage32 MAIN is V15 `STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED`, with FULL178 incomplete and no EX5 auto-promotion.

BC2-35 hostile audit PASS remains the last consumable EX5 mathematical authority:

- exact head `8bea7a6be26e01db0deb138dbd8406f578447921`;
- review `5187359907`;
- `12 UNSAT / 52 UNKNOWN / 0 SAT`;
- audited known parent-UNSAT lower bound `7284`;
- remaining 52 UNKNOWN hash `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`.

## BC2-36 retained audit boundary

BC2-36 executed exactly those 52 audited UNKNOWN parents at `100000 ms` per parent, one heavy runner, no scaleout.

Execution receipt:

- execution head `63986c900a34cbbfa00c96a0d2dcc38d3ffc92d5`;
- workflow `34718999232`;
- authorize job `103621253008`;
- compute job `103621306508`;
- artifact `10306816385`;
- artifact ZIP sha256 `35de2891058d97483fd7b3c9c95ca5c1041d9d96096287b1b01652a944f63ccb`;
- raw JSON sha256 `a70320e767ffe87d0751a7df195fd54387201e170e8f7daad43d41257af61f92`.

Retained candidate result:

- `11 UNSAT / 41 UNKNOWN / 0 SAT`;
- candidate known parent-UNSAT lower bound `7295`;
- remaining 41 UNKNOWN hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`;
- checkpoint canonical `e92cd6d07299b833a79fe20b81e9de032d61790cf1b7a6fb81ec6adccdb49fdf`;
- checkpoint blob `09ac58349e388c479ac77e04724bef2fd9b49b7e`;
- consumed runkey blob `78d9c847863232b10d149b651c32c668887e4b23`.

The BC2-36 heavy executor is retired. `7295` is candidate-only until hostile audit PASS; the consumable audited lower bound remains `7284`.

The next command is `stage32ex5-audit`. BC2-37 is blocked until BC2-36 hostile-audit PASS. No timeout UNKNOWN is relabelled UNSAT. No whole-first-block/FULL178 closure, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.
