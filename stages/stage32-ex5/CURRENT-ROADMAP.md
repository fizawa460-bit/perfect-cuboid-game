# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and is not rewritten.

## Stage32 context

Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Current observed Stage32 MAIN #1753 head is `58a25f59c3f82738c4666c76233568a038d151df` and the stop gate remains `N350_HOSTILE_AUDIT_THEN_REGISTER_EXACT_PRODUCER_ADAPTER`.

V6, O210, and Q602 are not current attack targets. `[73,97,235]` is historical/formal Q602 provenance, not a live survivor population.

## BC2 retained progress

The current local `(g1-d008,e=4)` exact Picard64 UNSAT prefix is `0..531`:

- BC2-05: `0..132` exact UNSAT;
- BC2-08: `133..265` exact UNSAT;
- BC2-10: `266..398` exact UNSAT;
- BC2-12: `399..531` exact UNSAT.

BC2-12 source-locks the BC2-11 structural block and derives the exceptional partition from the actual terminal/label map. The split is fixed mass `3`, residual mass `1`; all `20` selected-exceptional parents are exact UNSAT with no UNKNOWN and no SAT branch.

Evidence canonical: `d55b84e9b90692c14211e7d1affe73857f0cec2496305121067e2cd71d8da58a`.
Checkpoint canonical: `2fdb506c601ece59ef107fa62fc4e8948b6ea5145dae413e63ccc2d11691ecd9`.

## Current route

`BC2_13_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

Goal: structurally rederive the next exact 133-rank exceptional outer block after rank 531 using the source `CompressedTerminalIndexer`, rank/unrank round trips, and source `terminal_predicate` replay. Stop after an exact structural checkpoint. Do not assume the next exceptional signature or mass split from BC2-12.

If BC2-13 succeeds structurally, a later bounded unit may construct its symbolic-x4 Picard64 parent partition. Heavy scaleout is not authorized by this roadmap.

## Claim and promotion boundary

BC2-12 triggered retained-consolidation claim synchronization. EX5 remains an `ATTACKS` lane for `S32.FULL178.NUMERICAL_CENSUS.V1`; the active goal semantics did not change, so no claim-core mutation or ACTIVE-FRONTIER remap was required. This local result is not a MAIN-consumable production producer and receives zero N350/N104 production-coverage credit.

Promotion to Stage32 MAIN requires a separate exact current-target producer/adapter, replayable source locks, the required hostile audit, and explicit MAIN-side registration. EX5 cannot self-promote.

## Credit ceiling

The exact prefix `0..531` proves only local finite Picard64 obstruction in the locked EX5 model. It does not prove the whole `(g1-d008,e=4)` stratum closed, FULL178 complete, receiver closure, effectivity or actual-curve nonexistence, Stage32 closure, theorem/endpoint credit, or Perfect Cuboid existence/nonexistence.

N350 remains the current production boundary. Legacy N150 references are compatibility/provenance only.

## Audit and merge

Current work is Draft PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3`. A future `stage32ex5-audit` must attack an exact fixed head independently. CI success is not hostile-audit PASS. Merge requires explicit user authorization.
