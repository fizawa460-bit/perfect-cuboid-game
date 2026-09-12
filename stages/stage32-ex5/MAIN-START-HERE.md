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

At current MAIN `e4d3b8b83626526ffeccdbd9c956081735fe1a6e`, `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` is **SATISFIED** and there are no OPEN EX5 producer demands. Local BC2-36 execution may therefore continue.

## Current authority

Current Stage32 MAIN is V15 `STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED`, with FULL178 incomplete and no EX5 auto-promotion.

BC2-35 hostile audit PASS is consumed from exact head `8bea7a6be26e01db0deb138dbd8406f578447921`, review `5187359907`.

Audited BC2-35 credit is bounded to:

- `12 UNSAT / 52 UNKNOWN / 0 SAT` on the exact BC2-34 64-parent target;
- known parent-UNSAT lower bound `7284`;
- remaining 52 UNKNOWN hash `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`.

## BC2-36 execution

BC2-36 execution targets exactly those 52 audited UNKNOWN parents.

- producer: `breadth-cycle-2/bc2_36_replay_explicit_fresh_unknown52.py`
- producer blob: `18f9c2146d5dc97400c4af1a8691560523cc03cf`
- preflight canonical: `b2cc1cd97fe8da4504da980aa1c470f1aa419f9417b3eea8b1533305382155b0`
- preflight blob: `aa9bf40cf3550cae33cdfe8669aa51a80acddcec`
- timeout: `100000 ms` per parent
- heavy concurrency: `1`
- workflow timeout: `110 minutes`
- no scaleout
- artifact retention: `2 days`
- runkey: `runkeys/bc2-36-fresh-unknown52-replay.json`

The producer source-locks BC2-32 (`7cfe8450cb9b9ab7f04da797d487655505598b93`), BC2-19 (`b2899aa228e7a3ee97526e3787ffbefa483530b4`), BC2-18 (`1e2ed93cae3c5b446c8d90c1ae2250be83289c79`), and the hostile-audited BC2-35 checkpoint before `build_parent_space()`.

Generation 0 is a cold state only. Heavy execution is authorized only after a fresh semantic runkey advance to generation 1. Ordinary synchronization must not rerun heavy work.

BC2-37 is blocked until BC2-36 has been retained, frozen, and receives hostile-audit PASS. No whole-first-block/FULL178 closure, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.
