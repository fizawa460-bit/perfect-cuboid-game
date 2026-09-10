# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and is not rewritten.

## Stage32 context

Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Current observed Stage32 MAIN #1753 head is `b1d44137e0dd87cd3a604221715596d9b3574bc5`.

The latest retained MAIN attack checkpoint visible there is N349C hostile-audit handoff, canonical `2034688f2f881fbd1aeab8b4a567179a8767a7378daf43105910f0de92320eec`. N349C remains provisional; N260/N280 prerequisite audits are separate. The MAIN startup state still carries the older N350 stop-gate projection, so N350 is treated here only as the separate fail-closed production-registration boundary.

V6, O210, and Q602 are not current attack targets. `[73,97,235]` is historical/formal Q602 provenance, not a live survivor population.

## BC2 retained progress

The current local `(g1-d008,e=4)` exact Picard64 UNSAT prefix is `0..664`:

- BC2-05: `0..132` exact UNSAT;
- BC2-08: `133..265` exact UNSAT;
- BC2-10: `266..398` exact UNSAT;
- BC2-12: `399..531` exact UNSAT;
- BC2-14: `532..664` exact UNSAT.

For BC2-14, the exact BC2-13 structural signature plus locked assignment order gives fixed exceptional mass `4` and residual exceptional mass `0`. The selected-exceptional partition therefore has one parent, and the exact QF_LIA Picard64 solver result is `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`.

BC2-14 evidence canonical: `52fb48627a8646db2dc5b3e0b04eb32bc89ca9391988f4b91f7f51afada2de5d`.
BC2-14 checkpoint canonical: `fa603024cbf3b89fb097401f4e5e9b3f0cad04a0a0b6dd0b919b3a37b2781c0e`.

## Current route

`BC2_15_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

Goal: structurally rederive the next exact 133-rank exceptional outer block after rank `664` using the source `CompressedTerminalIndexer`, rank/unrank round trips, and source `terminal_predicate` replay. Stop after an exact structural checkpoint. Do not assume the next exceptional signature or mass split from BC2-14.

If BC2-15 succeeds structurally, a later bounded unit may construct its symbolic-x4 Picard64 parent partition. Heavy scaleout is not authorized by this roadmap.

## Claim and promotion boundary

BC2-14 triggered retained-consolidation claim synchronization. EX5 remains an `ATTACKS` lane for `S32.FULL178.NUMERICAL_CENSUS.V1`; the active goal semantics did not change, so no claim-core mutation or ACTIVE-FRONTIER remap was required. Receipt canonical: `b42ff343464c2dfceaa9203309024f657ee1d0f29bfaa7e326b0dfcf21598ddc`.

This local result is not a MAIN-consumable production producer and receives zero N350/N104 production-coverage credit. Promotion to Stage32 MAIN requires a separate exact current-target producer/adapter, replayable source locks, the required hostile audit, and explicit MAIN-side registration. EX5 cannot self-promote.

## Credit ceiling

The exact prefix `0..664` proves only local finite Picard64 obstruction in the locked EX5 model. It does not prove the whole `(g1-d008,e=4)` stratum closed, FULL178 complete, receiver closure, effectivity or actual-curve nonexistence, Stage32 closure, theorem/endpoint credit, or Perfect Cuboid existence/nonexistence.

N350 remains a production-registration boundary. Legacy N150 references are compatibility/provenance only. N349C is the latest observed MAIN attack/audit checkpoint and is independent of this EX5 local prefix.

## Audit and merge

Current work is Draft PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3`. A future `stage32ex5-audit` must attack an exact fixed head independently. CI success is not hostile-audit PASS. Merge requires explicit user authorization.
