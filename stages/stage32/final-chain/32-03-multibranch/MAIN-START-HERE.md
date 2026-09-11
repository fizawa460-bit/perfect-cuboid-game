# Stage32 32-03 multibranch startup

Ordinary `stage32mb-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. `stages/stage32/final-chain/32-03-multibranch/MAIN-START-HERE.md`;
4. current `stages/stage32/MAIN-STATE.json`;
5. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
6. `stages/stage32/final-chain/32-03-multibranch/PREFLIGHT.json`;
7. `stages/stage32/final-chain/32-03-multibranch/MISSION.json`;
8. only the exact assets required by the selected MB node or cross-lane demand.

This lane is the dedicated Stage32 32-03-L multibranch researcher. Current Stage32 mathematical routing authority remains `MAIN-STATE.json`; cross-lane demand status controls operational priority only and cannot self-promote mathematical credit.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`. Before local MB work, inspect every OPEN demand involving MB. A higher-priority OPEN demand where MB is producer preempts lower-priority local research. If MB is consumer of an OPEN demand, wait without duplicating producer work; when it becomes SATISFIED, re-enter on the next `stage32mb-mainbatch`, validate satisfying artifact identity/source-population semantics, and continue immediately. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync and MAIN promotion remain separate.

## Ownership

MB owns the R29-LG2-MB multibranch final-chain obligations: exact population/normalization profile, local branch-delta-genus accounting, Aut(S) quotient semantics, a population-wide justified finite degree/intersection window, and only then finite Picard/effectivity backend work.

MB does **not** own FULL178 numerical census or 178 cuts, EX5 Picard64 FULL178 producer work, CUT direct completion-infeasibility, already-consumed V6/O210/Q602 exclusions, or MAIN final-milestone promotion.

## Route discipline

The retained route is MB101 -> MB102/MB103 -> MB104 -> MB105 -> MB190, subject to current retained MB state. Exceptional contact mass, normalization-preimage count and delta invariant remain distinct until an exact adapter proves the needed relation.

MB may run concurrently with 178/EX5/CUT only while semantic leaves remain nonoverlapping and no higher-priority cross-lane demand reassigns an operational dependency. If current MAIN routing or demand registry assigns MB a conflicting/higher-priority obligation, obey the current machine routing rather than continuing local history.

## Handoff and audit

A retained MB checkpoint receives zero receiver/final-milestone/theorem credit until hostile audit and explicit MAIN consumption. The cross-lane demand DAG is operational and separate from the mathematical claim DAG; demand status alone must not mutate claim authority. `stage32mb-audit` is audit-only.

Do not merge without explicit user authorization.
