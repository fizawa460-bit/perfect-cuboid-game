# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` is the historical Cycle1 source-locked contract and must remain unchanged.

## Audit target

If the user gives an exact PR/head, audit that target. Otherwise resolve the active EX5 surface from `MAIN-STATE.json`. Current intended target is Draft PR #1765, branch `impl/stage32ex5-bc2-12-outer-rank3`; re-read the exact head at audit time. CI green is not hostile-audit PASS.

## Current Stage32 authority observation

Stage32 remains `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. Observed MAIN PR #1753 head is `0f8cee995e5c982cdb7ceceae14d69f91e65588d`.

Latest retained MAIN checkpoint is N353 uniform FULL178 scalar-Hurwitz census, RESULT canonical `afd873201ed0deea149c502d681729508face43942df085af91db3e95fbf371b`. N353 is audit-candidate only and grants no MAIN pruning credit. MAIN is freshness-frozen at `98 ahead / 0 behind` from hostile-audited head `b56a832e6c194321916fe4ef63eef0d673b8ff9a`, with thresholds `90/100`. N350 remains the separate production-registration boundary.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance. Any old no-O210/Q602 wording is a historical-credit firewall, not a current-frontier description.

## Exact BC2-16 mathematical claim under audit

BC2-16 proposes only local finite Picard64 UNSAT for ranks `665..797` of `(g1-d008,e=4)`, extending the retained exact local prefix from `0..664` to **`0..797`**.

Audit must independently verify:

- BC2-15 checkpoint canonical `f88ebe53c4300c01fc0a4870cc0dca75a0a091b60c95c8da7e00926bcee43182` and exact structural block `665..797`;
- outer exceptional rank `5`, base terminal `[0,1,0,0,0,0,2,0,0,0,1]`, exceptional signature `[0,1,0,0,0,2,0,0,0,1]`;
- BC2-16 solver source commit `defd1ee771ad01c1bbabed348fda2aa06132e4fe`;
- generation-1 run-key arm / exact compute head `3f4fcca1e1b3462a23caee72d8274ad44a7643a3`;
- commit-range authorization, effective heavy concurrency `1`, retention `1` day, projected artifact ceiling `200000` bytes;
- mass split derived from the actual BC2-15 terminal and locked labels: fixed `4`, residual `0`;
- complete selected-exceptional parent partition count `1`;
- exact result `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`;
- exact workflow run `34441599406`, authorize job `102757603904`, compute job `102757639746`;
- artifact `10138147649`, ZIP bytes `4249`, SHA256 `fa297a4b22025dd5bcbd65a44cd5c658cab7ded96fcc0855dbacc22c41928341`;
- evidence canonical `47278e00902f049e354227f02fe891b199025129a8fd3387a0249ad3b5c5ac9c`;
- checkpoint canonical `8cfe535fbd486b32e21c9e2cbb7c2289f2880420e5aa4cf3fc98db5f7d310a20`;
- retained exact prefix `0..797` and next route `BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

Audit must confirm that all later bookkeeping/synchronization heads leave the BC2-16 run-key at generation `1` and do not re-arm its heavy compute. Older BC2-12/14 heavy workflows must likewise remain cold on unrelated synchronizations.

## Prior retained chain

BC2-12 remains ranks `399..531`: fixed mass `3`, residual `1`, `20/20 UNSAT`, evidence `d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a`, checkpoint `2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9`.

BC2-14 remains ranks `532..664`: fixed mass `4`, residual `0`, `1/1 UNSAT`, evidence `52fb48627a8646db2dc5b3e0b04eb32bc89ca9391988f4b91f7f51afada2de5d`, checkpoint `fa603024cbf3b89fb097401f4e5e9b3f0cad04a0a0b6dd0b919b3a37b2781c0e`.

## Claim-DAG synchronization

BC2-16 triggered `RETAINED_CONSOLIDATION`. Audit must verify claim-sync receipt canonical `ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd`: EX5 continues to `ATTACKS` existing `S32.FULL178.NUMERICAL_CENSUS.V1`; active-goal semantics, ACTIVE-FRONTIER, claim core, lane adapter, and MAIN authority were not changed. No promotion adapter consumes BC2-16.

Run:

`python stages/stage32/proof/verify_stage32_claim_dag.py --integrity`

`python stages/stage32/proof/verify_stage32_active_frontier.py`

A local EX5 audit PASS must not mutate MAIN authority by itself.

## Mandatory firewalls

Even if BC2-16 passes hostile audit:

- the whole `(g1-d008,e=4)` stratum remains open;
- FULL178 remains incomplete;
- N353 remains separate audit-candidate MAIN work and is not promoted by EX5;
- N350/N104 production coverage remains zero for EX5 unless MAIN separately registers an audited exact producer;
- no receiver/effectivity/actual-curve/theorem/final-milestone/endpoint credit is granted;
- no Perfect Cuboid existence/nonexistence claim is granted;
- V6/O210/Q602 are not reopened;
- merge remains a separate explicit user action.

Preserve all historical source-locked evidence. Do not rewrite the historical Cycle1 source-locked contract or `stage32-ex5.md` during audit.

## Audit result

A PASS must state the exact audited head and precise local credit ceiling. A moved head invalidates that PASS for the new head. FAIL must name the first load-bearing defect without repairing the research branch inside the audit operation.
