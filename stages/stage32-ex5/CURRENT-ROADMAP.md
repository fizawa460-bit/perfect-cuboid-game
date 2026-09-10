# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and is not rewritten.

## Stage32 context

Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Observed MAIN PR #1753 head is `b1d44137e0dd87cd3a604221715596d9b3574bc5`. N349C hostile-audit handoff is the latest observed MAIN attack checkpoint; N350 remains the separate production-registration boundary.

V6, O210, and Q602 are not current attack targets. `[73,97,235]` is historical/formal Q602 provenance, not a live survivor population.

## BC2 retained progress

The local exact Picard64 UNSAT prefix remains `0..664`:

- BC2-05 `0..132` exact UNSAT;
- BC2-08 `133..265` exact UNSAT;
- BC2-10 `266..398` exact UNSAT;
- BC2-12 `399..531` exact UNSAT;
- BC2-14 `532..664` exact UNSAT.

BC2-15 structurally rederived the next 133-rank block without solver credit:

- ranks `665..797`;
- outer exceptional rank `5`;
- base terminal `[0,1,0,0,0,0,2,0,0,0,1]`;
- exceptional signature `[0,1,0,0,0,2,0,0,0,1]`;
- `133/133` rank/unrank and source-terminal-predicate replays exact;
- replay SHA `6655d249aa6d51cea8fe9bd7108c315c523b5ee1725d36dd1a1a537e11d4724f`;
- checkpoint canonical `f88ebe53c4300c01fc0a4870cc0dca75a0a091b60c95c8da7e00926bcee43182`.

Structural replay therefore reaches rank `797`, while exact UNSAT remains only through `664`.

## Current route

`BC2_16_OUTER_RANK5_SYMBOLIC_X4_PARENT_PREFLIGHT`.

Goal: apply the retained exact symbolic-x4 Picard64 selected-exceptional parent formulation only to ranks `665..797`. Derive fixed/residual exceptional mass from the actual BC2-15 terminal signature and locked label order before constructing the parent partition. Do not infer the split solely from outer rank `5`.

Heavy scaleout is not authorized by this roadmap. Any solver/artifact-producing execution requires a dedicated fresh run-key.

## Claim and promotion boundary

BC2-15 is structural-only, so it does not fire a new claim-DAG synchronization trigger. The last retained-consolidation synchronization remains BC2-14, receipt canonical `b42ff343464c2dfceaa9203309024f657ee1d0f29bfaa7e326b0dfcf21598ddc`. EX5 remains `ATTACKS` on `S32.FULL178.NUMERICAL_CENSUS.V1`; no claim-core mutation, ACTIVE-FRONTIER remap, or MAIN promotion occurs here.

The exact prefix plus structural replay does not prove the whole stratum closed, FULL178 complete, N350/N104 production coverage, receiver/effectivity/theorem/endpoint credit, Stage32 closure, or Perfect Cuboid existence/nonexistence.

Current work remains Draft PR #1765. A future `stage32ex5-audit` must attack an exact fixed head independently; CI success is not hostile-audit PASS. Merge requires explicit user authorization.
