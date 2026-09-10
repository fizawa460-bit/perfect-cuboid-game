# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32-ex5/README.md`;
3. this file;
4. `stages/stage32-ex5/MAIN-STATE.json`;
5. only `MAIN-STATE.json.current_leaf_working_set`.

Do not preload unrelated Stage32 history, other EX lanes, Research OS, or large retained payloads unless the active leaf explicitly triggers them.

## Current authority

Stage32 remains in `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is the primary incomplete requirement. Observed Stage32 MAIN #1753 head is `b1d44137e0dd87cd3a604221715596d9b3574bc5`.

The latest retained checkpoint visible at that head is N349C hostile-audit handoff, canonical `2034688f2f881fbd1aeab8b4a567179a8767a7378daf43105910f0de92320eec`. It is provisional/audit-pending, with N260/N280 prerequisite audits separate. The MAIN startup state still exposes an older N350 stop-gate projection; treat N350 as the fail-closed production-registration boundary, not as the latest attack checkpoint.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance only. EX5 does not reopen them.

## Current frontier

The retained local `(g1-d008,e=4)` exact Picard64 UNSAT prefix is `0..664`, consisting of five 133-rank blocks: `0..132`, `133..265`, `266..398`, `399..531`, and `532..664`.

BC2-14 exactly closed ranks `532..664`. From the actual BC2-13 terminal plus locked assignment order it derived fixed exceptional mass `4`, residual mass `0`, hence one complete selected-exceptional parent. Exact result: `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`.

BC2-14 evidence canonical: `52fb48627a8646db2dc5b3e0b04eb32bc89ca9391988f4b91f7f51afada2de5d`.
BC2-14 checkpoint canonical: `fa603024cbf3b89fb097401f4e5e9b3f0cad04a0a0b6dd0b919b3a37b2781c0e`.

The whole stratum is still open. FULL178 is still incomplete. No N350, receiver, effectivity, theorem, endpoint, or Stage32 MAIN credit follows.

## Current unit

`BC2_15_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

BC2-15 must rederive the next 133-rank exceptional outer block after rank 664 structurally before any new Picard64 closure credit. The ordinary startup contract does not authorize heavy compute.

## Claim-DAG state

BC2-14 retained consolidation was checked against the Stage32 claim-management layer. EX5 continues to attack `S32.FULL178.NUMERICAL_CENSUS.V1`; no ACTIVE-FRONTIER remap, claim-core mutation, or MAIN promotion occurred. Required claim-DAG integrity and active-frontier verifiers remain part of the EX5 main workflow.

## Execution contract

Each `stage32ex5-mainbatch` executes one bounded mathematical/interface unit, retains exact evidence with source locks and credit firewalls, synchronizes current routing, and stops at a coherent checkpoint. Heavy/artifact-producing work requires a dedicated fresh run-key authorization under repository policy.

Historical `stage32-ex5.md` and `AUDIT-CONTRACT.md` are immutable source-locked Cycle1 records. Exact retained evidence/checkpoints are not rewritten for terminology synchronization.

Do not merge without explicit user authorization. Current working PR #1765 remains a separate audit/merge surface.
