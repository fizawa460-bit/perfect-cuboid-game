# Stage32EX4 MAIN startup

Ordinary `stage32ex4-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex4/MAIN-START-HERE.md`;
3. `stages/stage32-ex4/MAIN-STATE.json`;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. only the paths listed in `MAIN-STATE.json.current_leaf_working_set` plus exact demand artifacts selected by the registry.

This file is the fixed ordinary startup contract. Mutable frontier, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The final target and dependency roadmap live in `stages/stage32-ex4/stage32-ex4.md`.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`. Before local work, inspect every OPEN demand involving EX4. A higher-priority OPEN demand where EX4 is producer preempts lower-priority local research. If EX4 is consumer of an OPEN demand, wait without duplicating producer mathematics; when it becomes SATISFIED, re-enter on the next mainbatch and validate satisfying artifact identity and population semantics before continuing. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync and MAIN promotion remain separate.

## Authority split

`MAIN-STATE.json` is a compact routing/resume projection, not a proof certificate. Exact marking/Q602 claims require source locks, retained artifacts/verifiers, and hostile-audit authority. A gauge choice, nonunique conjugator, conditional residue, source-gap diagnosis, or partial `3 -> 1` result is not terminal EX4 closure.

## Execution contract

Execute one bounded marking/conjugator/source diagnostic with exact object type, model, source locators, admissible coordinate changes, residual ambiguity, replay path, and credit ceiling. A failed source or nonunique conjugator is not EX4 exhaustion.

Scratch work is non-authoritative; heavy/artifact-producing workflows require separate authorization. Cross-lane demand state is operational and separate from the mathematical claim DAG. Demand status alone must not mutate claim authority.

`stage32ex4-audit` remains independent audit-only work. PASS does not automatically merge, alter MAIN authority, or contract historical Q602 provenance.

Do not merge without explicit user authorization.
