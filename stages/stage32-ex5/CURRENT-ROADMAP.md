# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and is not rewritten.

## Stage32 context

Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Observed MAIN PR #1753 head is `c2c1041298ae34a593fcb48d04c0e0a20dc9c37a`.

MAIN has accumulated the N101–N353 chain. N353 is now hostile-audited and consumed: review `5163144778`, exact head `0f8cee995e5c982cdb7ceceae14d69f91e65588d`. Its exact necessary cut is live at the audited ceiling.

The current MAIN gate is N354 two-sided scalar Hurwitz. RESULT canonical `9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4`; audit candidate head `ab0ce28876dbba306985343c104b02b69cec89fb`; handoff canonical `350afe8c3fbda418a888feff4e8c8233acc44b6472e825cf9d758c22d69065f6`. N354 is `AUDIT_REQUIRED`; candidate rejection `30575` strata / `307492486826907032120701491` terminals and candidate remaining `17128` strata / `38560956534397137634780102` terminals are diagnostic until audit PASS.

Freshness checkpoint is the audited N353 head; current MAIN is `9 ahead / 0 behind` and is not freshness-frozen.

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

Legacy N150 references are compatibility/provenance only. N350 remains the production-registration boundary; N353 is audited and N354 is the current MAIN hostile-audit gate.

## Audit and merge

Current work is Draft PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3`. A future `stage32ex5-audit` must attack an exact fixed head independently. CI success is not hostile-audit PASS. Merge requires explicit user authorization.
