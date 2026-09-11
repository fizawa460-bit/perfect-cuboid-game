# Stage32EX3 MAIN startup

Ordinary `stage32ex3-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex3/MAIN-START-HERE.md`;
3. `stages/stage32-ex3/MAIN-STATE.json`;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. only the paths listed in `MAIN-STATE.json.current_leaf_working_set` plus exact demand artifacts selected by the registry.

This file is the fixed ordinary startup contract. Mutable frontier, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The final target and dependency roadmap live in `stages/stage32-ex3/stage32-ex3.md`.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`. Before local work, inspect every OPEN demand involving EX3. A higher-priority OPEN demand where EX3 is producer preempts lower-priority local research. If EX3 is consumer of an OPEN demand, wait without duplicating producer mathematics; when it becomes SATISFIED, re-enter on the next mainbatch and validate satisfying artifact identity and population semantics before continuing. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync and MAIN promotion remain separate.

## Authority split

`MAIN-STATE.json` is the mutable routing/resume projection, not a proof certificate. Exact O210/Q602 claims require source locks, retained artifacts/verifiers, and hostile-audit authority. A finite monodromy/Nielsen ledger, abstract cover, or missing adapter does not close the carrier-attached O210 target.

## Execution contract

Execute one bounded cover/monodromy/adapter unit with exact object types, assumptions, population, source locators, and replay path. A failed route is not EX3 exhaustion. Retain a precise blocker/reopen condition and move only to a materially distinct legal route.

Scratch work is non-authoritative; heavy/artifact-producing workflows require separate authorization. Cross-lane demand state is operational and separate from the mathematical claim DAG. Demand status alone must not mutate claim authority.

`stage32ex3-audit` remains independent audit-only work. PASS does not automatically merge, alter MAIN authority, or grant endpoint credit.

Do not merge without explicit user authorization.
