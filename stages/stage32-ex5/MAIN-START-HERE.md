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

At current MAIN `e4d3b8b83626526ffeccdbd9c956081735fe1a6e`, `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` is **SATISFIED** and there are no OPEN EX5 producer demands. Local BC2-35 hostile audit may therefore continue.

## Current authority

Current Stage32 MAIN is V15 `STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED`, with FULL178 incomplete and no EX5 auto-promotion.

The last consumable EX5 mathematical authority remains BC2-34 hostile re-audit PASS at exact head `cdb455860849cfd064e3ab8c83d6d4993fb5ff1b`, review `5186516652`:

- audited BC2-34: `17 UNSAT / 64 UNKNOWN / 0 SAT`;
- audited known parent-UNSAT lower bound: `7272`;
- audited remaining 64 UNKNOWN hash: `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`.

## BC2-35 retained execution

BC2-35 heavy execution completed successfully at exact head `c8b929e1fbbc12bb432a5d4bfd0b9aea0d03cfa8`.

- workflow: `34696592793`
- authorize job: `103561025783`
- compute job: `103561129955`
- artifact: `10299388802`
- artifact ZIP sha256: `7e3b5a48300af52f19a329ed8f87e2048702b3587825b8893c2d5475aab150c3`
- raw JSON sha256: `da3f19d1e7e8f72052d9046f3e1482e669a50eeada228a3b113d440081bc266c`
- retained result: `12 UNSAT / 52 UNKNOWN / 0 SAT`
- candidate known parent-UNSAT lower bound: `7284`
- retained UNKNOWN hash: `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`
- checkpoint canonical: `14f808df5db80842b87efbbc0dafb9c68ad9cc5e3529b2647cfa66ee9faccf2f`
- checkpoint blob: `ee95590c637735478c06af413835ea390000b445`

The BC2-35 runkey is consumed/disarmed at generation 1. The BC2-35 authorize/heavy jobs are retired from the active workflow. The retained verifier `breadth-cycle-2/verify_bc2_35_targeted_replay_checkpoint.py` fail-closes the checkpoint, run receipt, source locks, partition and UNKNOWN identities.

## Audit stop

The current route is `HOSTILE_AUDIT_BC2_35_TARGETED_REPLAY`. Run `stage32ex5-audit` on the exact frozen head after exact-head CI is green.

BC2-36 is blocked until BC2-35 hostile-audit PASS. The `7284` lower bound is a retained **candidate**, not consumable audited credit; audited credit remains `7272` until PASS. No whole-first-block/FULL178 closure, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.
