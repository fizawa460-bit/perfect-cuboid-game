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

Before local EX5 research, inspect every `OPEN` demand with `producer_lane=EX5`. A higher-priority OPEN producer demand preempts lower-priority local work. A SATISFIED demand is only an operational handoff and **does not grant mathematical credit**.

At current MAIN `e4d3b8b83626526ffeccdbd9c956081735fe1a6e`, `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` is **SATISFIED** and there are no OPEN EX5 producer demands. Local BC2-35 execution may therefore continue.

## Current authority

Current Stage32 MAIN is V15 `STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED`, with FULL178 incomplete and no EX5 auto-promotion.

BC2-34 hostile re-audit PASS is consumed from exact head `cdb455860849cfd064e3ab8c83d6d4993fb5ff1b`, review `5186516652`.

Audited BC2-34 credit is bounded to:

- `17 UNSAT / 64 UNKNOWN / 0 SAT` on the exact BC2-33 81-parent target;
- known parent-UNSAT lower bound `7272`;
- remaining 64 UNKNOWN hash `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`.

## BC2-35 execution

BC2-35 execution targets exactly those 64 audited UNKNOWN parents.

- producer: `breadth-cycle-2/bc2_35_replay_explicit_fresh_unknown64.py`
- producer blob: `40111bb7619113d1c9c766089026bcf59d6bdb01`
- preflight canonical: `e74e6c15050187d06c472c2eff6156c66837f8f9c9de3d2cfca7629b431dadb4`
- preflight blob: `bf2f4b1125925a27c820dfdc49ad796e69b268b4`
- timeout: `80000 ms` per parent
- heavy concurrency: `1`
- no scaleout
- artifact retention: `2 days`
- runkey: `runkeys/bc2-35-fresh-unknown64-replay.json`

The producer explicitly source-locks the directly executed BC2-32 module (`7cfe8450cb9b9ab7f04da797d487655505598b93`) before `build_parent_space()`, plus BC2-19 and BC2-18. This preserves the dependency-identity repair required by the BC2-34 hostile audit.

BC2-35 generation 0 is a cold state only. Heavy execution is authorized only after a fresh semantic runkey advance to generation 1. Ordinary synchronization must not rerun heavy work.

BC2-36 is blocked until BC2-35 has been retained, frozen, and receives hostile-audit PASS. No whole-first-block/FULL178 closure, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.
