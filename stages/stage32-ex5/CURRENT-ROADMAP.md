# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and is not rewritten.

## Stage32 context

Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Observed MAIN PR #1753 head is `0f8cee995e5c982cdb7ceceae14d69f91e65588d`.

The latest retained MAIN checkpoint is N353 uniform FULL178 scalar-Hurwitz census, RESULT canonical `afd873201ed0deea149c502d681729508face43942df085af91db3e95fbf371b`. It remains audit-candidate only and grants no MAIN pruning credit. MAIN is freshness-frozen at `98 ahead / 0 behind` from hostile-audited checkpoint `b56a832e6c194321916fe4ef63eef0d673b8ff9a`; re-audit threshold is `90`, hard halt `100`.

N350 remains a separate production-registration boundary. V6, O210, and Q602 are not current attack targets. `[73,97,235]` is historical/formal Q602 provenance, not a live survivor population.

## BC2 retained progress

The local `(g1-d008,e=4)` exact Picard64 UNSAT prefix is **`0..797`**:

- BC2-05: `0..132` exact UNSAT;
- BC2-08: `133..265` exact UNSAT;
- BC2-10: `266..398` exact UNSAT;
- BC2-12: `399..531` exact UNSAT;
- BC2-14: `532..664` exact UNSAT;
- BC2-16: `665..797` exact UNSAT.

For BC2-16 the retained BC2-15 terminal and locked label order give outer rank `5`, fixed exceptional mass `4`, residual mass `0`, hence one complete selected-exceptional parent. The exact QF_LIA Picard64 result is `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`.

BC2-16 evidence canonical: `47278e00902f049e354227f02fe891b199025129a8fd3387a0249ad3b5c5ac9c`.
BC2-16 checkpoint canonical: `8cfe535fbd486b32e21c9e2cbb7c2289f2880420e5aa4cf3fc98db5f7d310a20`.
Claim-sync canonical: `ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd`.

## Current route

`BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

Goal: structurally rederive the next exact 133-rank exceptional outer block after rank `797` using source `CompressedTerminalIndexer`, rank/unrank round trips, and source `terminal_predicate` replay. Stop after a structural checkpoint. Do not infer the next exceptional signature or mass split from BC2-16. A later bounded unit may construct its symbolic-x4 Picard64 parent partition.

Heavy scaleout is not authorized by this roadmap.

## Claim and promotion boundary

BC2-16 triggered retained-consolidation claim synchronization. EX5 remains an `ATTACKS` lane for `S32.FULL178.NUMERICAL_CENSUS.V1`; the active goal is unchanged and there is no current attack remap. No claim-core mutation, ACTIVE-FRONTIER remap, lane-adapter change, promotion adapter, or MAIN promotion was required.

This local result is not a MAIN-consumable production producer and receives zero N350/N104 production-coverage credit. Promotion to Stage32 MAIN requires a separately audited exact current-target producer/adapter and explicit MAIN-side registration. EX5 cannot self-promote.

## Credit ceiling

The exact prefix `0..797` proves only local finite Picard64 obstruction in the locked EX5 model. It does not prove the whole `(g1-d008,e=4)` stratum closed, FULL178 complete, receiver closure, effectivity or actual-curve nonexistence, Stage32 closure, theorem/endpoint credit, or Perfect Cuboid existence/nonexistence.

Legacy N150 references are compatibility/provenance only. N350 remains the production-registration boundary; N353 is the latest observed MAIN attack/audit-candidate checkpoint.

## Audit and merge

Current work is Draft PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3`. A future `stage32ex5-audit` must attack an exact fixed head independently. CI success is not hostile-audit PASS. Merge requires explicit user authorization.
