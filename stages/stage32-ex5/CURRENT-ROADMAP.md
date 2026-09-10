# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and is not rewritten.

## Stage32 context

Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Current observed Stage32 MAIN #1753 head is `1edbb0775d2beac51d98c1327d2fe6b83c012323` and the stop gate remains `N350_HOSTILE_AUDIT_THEN_REGISTER_EXACT_PRODUCER_ADAPTER`.

V6, O210, and Q602 are not current attack targets. `[73,97,235]` is historical/formal Q602 provenance, not a live survivor population.

## BC2 retained progress

The current local `(g1-d008,e=4)` exact Picard64 UNSAT prefix is `0..531`:

- BC2-05: `0..132` exact UNSAT;
- BC2-08: `133..265` exact UNSAT;
- BC2-10: `266..398` exact UNSAT;
- BC2-12: `399..531` exact UNSAT.

BC2-12 evidence canonical: `d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a`.
BC2-12 checkpoint canonical: `2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9`.

BC2-13 structurally rederived the next block, without solver credit:

- ranks `532..664`, width `133`;
- outer exceptional rank `4`;
- base terminal at x4=0 `[0,1,0,0,0,0,1,1,0,0,1]`;
- exceptional signature `[0,1,0,0,0,1,1,0,0,1]`;
- `133/133` exact rank/unrank replays;
- `133/133` exact source `terminal_predicate` replays;
- replay stream SHA256 `c7178bb53882b5e4c88309bf26ff149e993f07d4c610aec98c50f7a9a84005d5`;
- checkpoint canonical `77a0d31f6c5ca4b725c8d4f34ac2a867b82e042768858ff6475d949e1444f9c0`.

The exact UNSAT prefix remains `0..531`; ranks `532..664` are structural-only at this checkpoint.

## Current route

`BC2_14_OUTER_RANK4_SYMBOLIC_X4_PARENT_PREFLIGHT`.

Goal: apply the retained exact symbolic-x4 Picard64 selected-exceptional parent formulation only to ranks `532..664`, deriving fixed/residual exceptional mass from the actual BC2-13 terminal signature before constructing the parent partition. Do not infer the split from the outer-rank number.

Heavy scaleout is not authorized by this roadmap. A dedicated fresh run-key is required for solver/artifact-producing execution.

## Claim and promotion boundary

BC2-12 triggered retained-consolidation claim synchronization. EX5 remains an `ATTACKS` lane for `S32.FULL178.NUMERICAL_CENSUS.V1`; BC2-13 does not alter the active goal semantics, so no claim-core mutation or ACTIVE-FRONTIER remap is required. The local results are not a MAIN-consumable production producer and receive zero N350/N104 production-coverage credit.

Promotion to Stage32 MAIN requires a separate exact current-target producer/adapter, replayable source locks, the required hostile audit, and explicit MAIN-side registration. EX5 cannot self-promote.

## Credit ceiling

The exact prefix `0..531` plus structural replay through `664` proves only local finite/structural progress in the locked EX5 model. It does not prove the whole `(g1-d008,e=4)` stratum closed, FULL178 complete, receiver closure, effectivity or actual-curve nonexistence, Stage32 closure, theorem/endpoint credit, or Perfect Cuboid existence/nonexistence.

N350 remains the current production boundary. Legacy N150 references are compatibility/provenance only.

## Audit and merge

Current work is Draft PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3`. A future `stage32ex5-audit` must attack an exact fixed head independently. CI success is not hostile-audit PASS. Merge requires explicit user authorization.
