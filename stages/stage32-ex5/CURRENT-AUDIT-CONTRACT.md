# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` is the historical Cycle1 source-locked contract and must remain unchanged.

## Audit target

If the user gives an exact PR/head, audit that target. Otherwise resolve the active EX5 surface from `MAIN-STATE.json`. The current intended target is Draft PR #1765, branch `impl/stage32ex5-bc2-12-outer-rank3`; the exact head must be re-read at audit time.

Do not rely on chat summaries as mathematical evidence. CI green is not hostile-audit PASS.

## Current Stage32 authority observation

Stage32 remains in `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. Observed Stage32 MAIN #1753 head is `b1d44137e0dd87cd3a604221715596d9b3574bc5`.

The latest retained MAIN checkpoint visible at that head is N349C hostile-audit handoff, canonical `2034688f2f881fbd1aeab8b4a567179a8767a7378daf43105910f0de92320eec`. N349C remains provisional and its N260/N280 prerequisite audits are separate. The MAIN startup state still contains an older N350 stop-gate projection; N350 remains the production-registration boundary but must not be presented as the latest attack checkpoint.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance. Any old no-O210/Q602 wording is a historical-credit firewall, not a current-frontier description.

## Exact BC2-14 mathematical claim under audit

The new mathematical credit proposed by BC2-14 is local finite Picard64 UNSAT for ranks `532..664` of `(g1-d008,e=4)`, extending the retained exact local prefix from `0..531` to `0..664`.

The audit must independently verify:

- BC2-13 checkpoint canonical `77a0d31f6c5ca4b725c8d4f34ac2a867b82e042768858ff6475d949e1444f9c0` and exact structural block `532..664`;
- BC2-14 solver source commit `834d7d4b57659e96f27b1f73f569a9f1e1a79751`;
- generation-1 run-key arm commit / exact compute head `05656d9fadb676422ebfa0977536fd99239600fd`;
- commit-range heavy authorization, effective heavy concurrency `1`, artifact retention `1` day, and projected artifact ceiling `200000` bytes;
- exceptional split derived from the exact BC2-13 terminal and locked labels: fixed mass `4`, residual mass `0`;
- complete selected-exceptional parent partition count `1`;
- exact solver result `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`;
- exact run `34437319330`, authorize job `102745011293`, compute job `102745081056`;
- evidence canonical `52fb48627a8646db2dc5b3e0b04eb32bc89ca9391988f4b91f7f51afada2de5d`;
- checkpoint canonical `fa603024cbf3b89fb097401f4e5e9b3f0cad04a0a0b6dd0b919b3a37b2781c0e`;
- retained exact prefix `0..664` and next route `BC2_15_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

Audit must confirm that later bookkeeping/synchronization commits did not re-arm BC2-14 heavy computation. The older BC2-12 heavy workflow must likewise remain cold on unrelated synchronizations.

## Prior retained chain

BC2-12 remains the exact `399..531` result: fixed mass `3`, residual mass `1`, `20/20 UNSAT`, evidence canonical `d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a`, checkpoint canonical `2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9`.

BC2-13 is the structural bridge for `532..664`: outer exceptional rank `4`, base terminal `[0,1,0,0,0,0,1,1,0,0,1]`, exceptional signature `[0,1,0,0,0,1,1,0,0,1]`, `133/133` rank/unrank and source-terminal-predicate replays, replay SHA `c7178bb53882b5e4c88309bf26ff149e993f07d4c610aec98c50f7a9a84005d5`.

## Claim-DAG synchronization

BC2-14 triggered `RETAINED_CONSOLIDATION`. Audit must verify claim-sync receipt canonical `b42ff343464c2dfceaa9203309024f657ee1d0f29bfaa7e326b0dfcf21598ddc` and the decision that no active-frontier remap occurred: EX5 continues to attack existing `S32.FULL178.NUMERICAL_CENSUS.V1`; no MAIN dependency or producer adapter consumes BC2-14 at this checkpoint.

Run the Stage32 claim-DAG integrity and active-frontier verifiers. A local EX5 audit PASS must not mutate MAIN authority by itself.

## Mandatory firewalls

Even if BC2-14 passes hostile audit:

- the whole `(g1-d008,e=4)` stratum remains open;
- FULL178 remains incomplete;
- N350/N104 production coverage remains zero for EX5 unless MAIN separately registers an audited exact producer;
- N349C/N260/N280 authority is neither granted nor altered by EX5;
- no receiver/effectivity/actual-curve/theorem/final-milestone/endpoint credit is granted;
- no Perfect Cuboid existence/nonexistence claim is granted;
- V6/O210/Q602 are not reopened;
- merge remains a separate explicit user action.

Preserve all historical source-locked evidence. Do not rewrite the historical Cycle1 source-locked contract or `stage32-ex5.md` during audit.

## Audit result

A PASS must state the exact audited head and the precise local credit ceiling. A moved head invalidates that PASS for the new head. FAIL must name the first load-bearing defect without repairing the research branch inside the audit operation.
