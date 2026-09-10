# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` is the historical Cycle1 source-locked contract and must remain unchanged.

## Audit target

If the user gives an exact PR/head, audit that target. Otherwise resolve the active EX5 surface from `MAIN-STATE.json`. The current intended target is Draft PR #1765, branch `impl/stage32ex5-bc2-12-outer-rank3`; the exact head must be re-read at audit time.

Do not rely on chat summaries as mathematical evidence. CI green is not hostile-audit PASS.

## Current Stage32 authority

Stage32 remains in `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. Observed Stage32 MAIN #1753 head is `1edbb0775d2beac51d98c1327d2fe6b83c012323`. Current observed production boundary is N350 with stop gate `N350_HOSTILE_AUDIT_THEN_REGISTER_EXACT_PRODUCER_ADAPTER`.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance. Any old no-O210/Q602 wording is a historical-credit firewall, not a current-frontier description.

## Exact BC2-12 mathematical claim under audit

The mathematical credit proposed by BC2-12 remains local finite Picard64 UNSAT for ranks `399..531` of `(g1-d008,e=4)`, extending the retained exact local prefix to `0..531`.

The audit must independently verify the BC2-11 structural source lock, BC2-12 generation-1 heavy authorization, fixed exceptional mass `3`, residual mass `1`, complete `20`-parent partition, exact result `20/20 UNSAT`, `UNKNOWN=0`, `SAT=0`, evidence canonical `d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a`, and checkpoint canonical `2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9`.

Audit must also confirm that later synchronization did not re-arm the BC2-12 heavy job.

## BC2-13 structural claim under audit

BC2-13 adds structural replay only, with no Picard64 UNSAT credit for the new block. Audit must independently verify:

- predecessor BC2-12 checkpoint canonical `2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9`;
- next block ranks `532..664`, width `133`, outer exceptional rank `4`;
- base terminal at x4=0 `[0,1,0,0,0,0,1,1,0,0,1]`;
- exceptional signature `[0,1,0,0,0,1,1,0,0,1]`;
- all `133/133` rank/unrank round trips exact;
- all `133/133` source `terminal_predicate` replays exact;
- replay stream SHA256 `c7178bb53882b5e4c88309bf26ff149e993f07d4c610aec98c50f7a9a84005d5`;
- BC2-13 checkpoint canonical `77a0d31f6c5ca4b725c8d4f34ac2a867b82e042768858ff6475d949e1444f9c0`;
- solver/heavy compute not invoked by BC2-13;
- exact UNSAT prefix remains `0..531`, while structural replay reaches rank `664`;
- next route is `BC2_14_OUTER_RANK4_SYMBOLIC_X4_PARENT_PREFLIGHT`.

## Claim-DAG synchronization

BC2-12 triggered `RETAINED_CONSOLIDATION`; receipt canonical remains `3acaa613dabbaa0caa0fdee9bccf0220cd7b119fb304196d355f0528d648f639`. BC2-13 is structural-only and does not alter active-goal semantics. EX5 continues to attack existing `S32.FULL178.NUMERICAL_CENSUS.V1`; no MAIN dependency or producer adapter consumes BC2-12/13 at this checkpoint.

Run the Stage32 claim-DAG integrity and active-frontier verifiers. A local EX5 audit PASS must not mutate MAIN authority by itself.

## Mandatory firewalls

Even if BC2-12/13 pass hostile audit:

- ranks `532..664` are not Picard64-closed by BC2-13;
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
