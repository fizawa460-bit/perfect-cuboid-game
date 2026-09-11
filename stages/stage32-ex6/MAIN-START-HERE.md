# Stage32EX6 MAIN startup

Ordinary `stage32ex6-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex6/MAIN-START-HERE.md`;
3. `stages/stage32-ex6/MAIN-STATE.json`;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. only the paths listed in `MAIN-STATE.json.current_leaf_working_set` plus exact demand artifacts selected by the registry.

This is the fixed ordinary startup contract. Mutable routing, current blocker, re-entry conditions, audit provenance, and next route live only in `MAIN-STATE.json`.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`. Before local work, inspect every OPEN demand involving EX6. A higher-priority OPEN demand where EX6 is producer preempts lower-priority local research. If EX6 is consumer of an OPEN demand, wait without duplicating producer mathematics; when it becomes SATISFIED, re-enter on the next mainbatch and validate satisfying artifact identity and population semantics before continuing. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync and MAIN promotion remain separate.

## Authority split

`MAIN-STATE.json` is a routing/resume projection, not a proof certificate. The merged EX6 lineage remains bounded evidence and does not close O266, descend to O264, or alter current Stage32 MAIN authority without a new audited promotion boundary.

## Execution contract

When explicitly reopened, execute one bounded O266 endpoint/re-entry unit with exact source locators, population/object semantics, replay path, and credit ceiling. A blocked endpoint route is not Stage32 exhaustion. The current state remains stopped until genuinely new endpoint input or an explicit higher-priority cross-lane demand appears.

Scratch work is non-authoritative; heavy/artifact-producing workflows require separate authorization. Cross-lane demand state is operational and separate from the mathematical claim DAG. Demand status alone must not mutate claim authority.

EX6 has no automatic promotion path. Any terminal result requires the existing hostile-audit and current-target EX->MAIN promotion rules.

Do not merge without explicit user authorization.
