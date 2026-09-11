# Stage32 32-03 multibranch startup

Ordinary `stage32mb-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. `stages/stage32/final-chain/32-03-multibranch/MAIN-START-HERE.md`;
4. `stages/stage32/final-chain/32-03-multibranch/PREFLIGHT.json`;
5. `stages/stage32/final-chain/32-03-multibranch/MISSION.json`;
6. current `stages/stage32/MAIN-STATE.json`;
7. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
8. only the exact assets required by the current MB node plus any exact demand artifact/state explicitly selected by the registry.

This lane is the dedicated Stage32 32-03-L multibranch researcher. The preflight explicitly permits mission work without waiting for 32-01/FULL178, and the operator has now allocated parallel capacity. Current Stage32 routing authority remains `MAIN-STATE.json`; cross-lane demand state controls operational priority only and this lane cannot self-promote.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`. Before substantive local work, inspect every OPEN demand involving MB. A higher-priority OPEN demand where MB is producer preempts lower-priority local research. If MB is consumer of an OPEN demand, wait without duplicating producer mathematics; when it becomes SATISFIED, re-enter on the next `stage32mb-mainbatch` and validate satisfying artifact identity and source-population semantics before resuming. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync and MAIN promotion remain separate.

## Ownership

MB owns the R29-LG2-MB multibranch final-chain obligations: exact population/normalization profile, local branch-delta-genus accounting, Aut(S) quotient semantics, a population-wide justified finite degree/intersection window, and only then finite Picard/effectivity backend work.

MB does **not** own:

- FULL178 numerical census, N356, or other 178 cuts;
- EX5 Picard64/node-support FULL178 producer research;
- already-consumed V6/O210/Q602 exclusions;
- the unibranch 176/192 degree cap unless a new multibranch proof is supplied;
- EX6 O266 tensor routes already recorded as nonexcluding/dominated;
- MAIN final milestone promotion, theorem/endpoint credit, or merge.

## First route

Start at `MB101`: freeze the exact R29-LG2-MB population and normalization-profile adapter. Do not jump directly to finite Picard enumeration. The load-bearing sequence is MB101 -> MB102/MB103 -> MB104 -> MB105 -> MB190, interpreted through the current retained MB state.

Exceptional contact mass, number of normalization preimages, and delta invariant are distinct until an exact local adapter proves the relation required in the current profile.

## Parallelism rule

`stage32mb-mainbatch` may run concurrently with `stage32-01-178-mainbatch`, `stage32ex5-mainbatch`, and `stage32cut-mainbatch` because its target receiver and output contract are independent. If current MAIN routing later assigns the same semantic leaf elsewhere, or a valid higher-priority cross-lane demand changes its operational dependency, stop and obey current machine routing rather than duplicating it.

## Handoff and audit

A retained MB checkpoint receives zero receiver/final-milestone/theorem credit until hostile audit and explicit MAIN consumption. Cross-lane demand state is operational and separate from the mathematical claim DAG; demand status alone does not grant mathematical credit. `stage32mb-audit` is audit-only. Any final-milestone transition remains a MAIN claim-sync event.

Do not merge without explicit user authorization.
