# Stage32EX2 MAIN startup

Ordinary `stage32ex2-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex2/MAIN-START-HERE.md`;
3. `stages/stage32-ex2/MAIN-STATE.json`;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. only the paths listed in `MAIN-STATE.json.current_leaf_working_set` plus exact demand artifacts selected by the registry.

This file is the fixed ordinary startup contract. Mutable frontier, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The mathematical target and dependency roadmap live in `stages/stage32-ex2/stage32-ex2.md` and are opened only when the active task/working set requires them.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`. Before local work, inspect every OPEN demand involving EX2. A higher-priority OPEN demand where EX2 is producer preempts lower-priority local research. If EX2 is consumer of an OPEN demand, wait without duplicating producer mathematics; when it becomes SATISFIED, re-enter on the next mainbatch and validate satisfying artifact identity and population semantics before resuming. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync and MAIN promotion remain separate.

## Authority split

`MAIN-STATE.json` is a routing/resume projection, not a proof certificate. Exact mathematical claims require source locks, retained leaf artifacts/verifiers, and hostile-audit records. The final EX2 target remains an actual integral irreducible geometric-genus-1 member decision or a population-wide negative linear-system proof; a finite reconstruction miss never suffices.

## Execution contract

Execute one bounded reconstruction/decomposition/verification unit at a time, with exact source locators, object/model/population semantics, replay path, blocker/reopen condition, and credit ceiling. A failed reconstruction technique is `LEAF_BLOCKED`, not EX2 exhaustion.

Scratch work is non-authoritative; heavy/artifact-producing workflows require separate authorization. Cross-lane demand state is operational and separate from the mathematical claim DAG. Demand status alone must not mutate claim authority.

`stage32ex2-audit` remains an independent hostile-audit lane. PASS does not auto-merge or auto-promote Stage32 MAIN.

Do not merge without explicit user authorization.
