# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` is the historical Cycle1 source-locked contract and must remain unchanged.

## Audit target

If the user gives an exact PR/head, audit that target. Otherwise resolve the active EX5 surface from `MAIN-STATE.json`. The current intended target is Draft PR #1765, branch `impl/stage32ex5-bc2-12-outer-rank3`; the exact head must be re-read at audit time.

Do not rely on chat summaries as mathematical evidence. CI green is not hostile-audit PASS.

## Current Stage32 authority

Stage32 remains in `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. Observed Stage32 MAIN #1753 head is `58a25f59c3f82738c4666c76233568a038d151df`. Current observed production boundary is N350 with stop gate `N350_HOSTILE_AUDIT_THEN_REGISTER_EXACT_PRODUCER_ADAPTER`.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance. Any old no-O210/Q602 wording is a historical-credit firewall, not a current-frontier description.

## Exact BC2-12 claim under audit

The only new mathematical credit proposed by BC2-12 is local finite Picard64 UNSAT for ranks `399..531` of `(g1-d008,e=4)`, extending the retained exact local prefix from `0..398` to `0..531`.

The audit must independently verify:

- BC2-11 checkpoint canonical `b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d` and exact structural block `399..531`;
- BC2-12 solver source lock and heavy-run authorization chain;
- exceptional split derived from the exact BC2-11 terminal/locked labels: fixed mass `3`, residual mass `1`;
- complete parent partition count `20`;
- exact solver result `20/20 UNSAT`, `UNKNOWN=0`, `SAT=0`;
- evidence canonical `d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a`;
- checkpoint canonical `2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9`;
- retained exact prefix `0..531` and next route `BC2_13_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

The exact heavy run was authorized by a fresh generation-1 run-key and used effective heavy concurrency 1. Audit must confirm that later synchronization commits did not re-arm the heavy job.

## Claim-DAG synchronization

BC2-12 triggered `RETAINED_CONSOLIDATION`. Audit must verify claim-sync receipt canonical `3acaa613dabbaa0caa0fdee9bccf0220cd7b119fb304196d355f0528d648f639` and the decision that no active-frontier remap occurred: EX5 continues to attack existing `S32.FULL178.NUMERICAL_CENSUS.V1`; no MAIN dependency or producer adapter consumes BC2-12 at this checkpoint.

Run the Stage32 claim-DAG integrity and active-frontier verifiers. A local EX5 audit PASS must not mutate MAIN authority by itself.

## Mandatory firewalls

Even if BC2-12 passes hostile audit:

- the whole `(g1-d008,e=4)` stratum remains open;
- FULL178 remains incomplete;
- N350/N104 production coverage remains zero for EX5 unless MAIN separately registers an audited exact producer;
- no receiver/effectivity/actual-curve/theorem/final-milestone/endpoint credit is granted;
- no Perfect Cuboid existence/nonexistence claim is granted;
- V6/O210/Q602 are not reopened;
- merge remains a separate explicit user action.

Preserve all historical source-locked evidence. Do not rewrite the historical Cycle1 source-locked contract or `stage32-ex5.md` during audit.

## Audit result

A PASS must state the exact audited head and the precise local credit ceiling. A moved head invalidates that PASS for the new head. FAIL must name the first load-bearing defect without repairing the research branch inside the audit operation.
