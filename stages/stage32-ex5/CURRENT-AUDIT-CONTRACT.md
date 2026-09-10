# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` is the historical Cycle1 source-locked contract and must remain unchanged.

## Audit target

If the user gives an exact PR/head, audit that target. Otherwise resolve the active EX5 surface from `MAIN-STATE.json`. Current intended target is Draft PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3`; re-read the exact head at audit time. CI green is not hostile-audit PASS.

## Current Stage32 authority observation

Stage32 remains `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. Observed MAIN PR #1753 head is `b1d44137e0dd87cd3a604221715596d9b3574bc5`. N349C hostile-audit handoff, canonical `2034688f2f881fbd1aeab8b4a567179a8767a7378daf43105910f0de92320eec`, is the latest observed MAIN attack checkpoint and remains provisional. N350 is the separate production-registration boundary. V6/O210/Q602 and `[73,97,235]` are historical/formal provenance; old no-O210/Q602 language is a historical-credit firewall, not a current-frontier description.

## Retained exact BC2-14 claim

BC2-14 retains local Picard64 UNSAT for ranks `532..664`, extending exact prefix to `0..664`. Audit must independently verify fixed exceptional mass `4`, residual mass `0`, complete one-parent partition, `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`, evidence canonical `52fb48627a8646db2dc5b3e0b04eb32bc89ca9391988f4b91f7f51afada2de5d`, checkpoint canonical `fa603024cbf3b89fb097401f4e5e9b3f0cad04a0a0b6dd0b919b3a37b2781c0e`, exact compute head `05656d9fadb676422ebfa0977536fd99239600fd`, and that later bookkeeping did not re-arm its heavy workflow.

## New BC2-15 structural claim under audit

BC2-15 grants structural replay only and must be checked independently against the source indexer and source `terminal_predicate`:

- predecessor BC2-14 checkpoint canonical `fa603024cbf3b89fb097401f4e5e9b3f0cad04a0a0b6dd0b919b3a37b2781c0e`;
- ranks `665..797`, width `133`, outer exceptional rank `5`;
- previous block ends at rank `664` with x4=`132`;
- base terminal at x4=0 `[0,1,0,0,0,0,2,0,0,0,1]`;
- exceptional signature `[0,1,0,0,0,2,0,0,0,1]`;
- all `133/133` rank/unrank round trips exact;
- all `133/133` source `terminal_predicate` replays exact;
- x4 is innermost and the exceptional signature is constant across the block;
- replay stream SHA256 `6655d249aa6d51cea8fe9bd7108c315c523b5ee1725d36dd1a1a537e11d4724f`;
- checkpoint canonical `f88ebe53c4300c01fc0a4870cc0dca75a0a091b60c95c8da7e00926bcee43182`;
- solver/heavy compute not invoked;
- exact UNSAT prefix remains `0..664`, structural replay reaches `797`;
- next route is `BC2_16_OUTER_RANK5_SYMBOLIC_X4_PARENT_PREFLIGHT`.

## Claim-DAG synchronization

BC2-15 is structural-only and does not create a new retained mathematical dependency, authority transition, EX-to-MAIN promotion, active-frontier remap, or final-milestone transition. The last claim-sync receipt remains BC2-14 canonical `b42ff343464c2dfceaa9203309024f657ee1d0f29bfaa7e326b0dfcf21598ddc`. EX5 continues to attack `S32.FULL178.NUMERICAL_CENSUS.V1` with no MAIN promotion.

Run the Stage32 claim-DAG integrity and active-frontier verifiers.

## Mandatory firewalls

Even if BC2-14/15 pass hostile audit, ranks `665..797` are not Picard64-closed by BC2-15; the whole `(g1-d008,e=4)` stratum remains open; FULL178 remains incomplete; EX5 has no N350/N104 production coverage; N349C/N260/N280 authority is not altered; no receiver/effectivity/actual-curve/theorem/final-milestone/endpoint or Perfect Cuboid existence/nonexistence credit follows; V6/O210/Q602 are not reopened; merge remains a separate explicit user action.

Preserve the historical Cycle1 source-locked contract and `stage32-ex5.md` unchanged.
