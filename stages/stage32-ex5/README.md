# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary `ATTACKS` lane for the current Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`. The primary incomplete requirement remains `32-01 FULL178`.

## Current Stage32 authority observation

Observed Stage32 MAIN PR #1753 head: `c2c1041298ae34a593fcb48d04c0e0a20dc9c37a`.

MAIN has advanced through the N101–N353 chain. **N353 is now hostile-audited and consumed**: review `5163144778`, exact audited head `0f8cee995e5c982cdb7ceceae14d69f91e65588d`. Its necessary cut is live MAIN credit at the exact stated ceiling: `12788` strata / `264541612417334415376` terminals rejected, leaving `47703` strata / `346053443361304169755481593` terminals.

The current MAIN gate is **N354 two-sided scalar Hurwitz**. N354 RESULT canonical is `9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4`; audit-candidate exact head is `ab0ce28876dbba306985343c104b02b69cec89fb`; handoff canonical is `350afe8c3fbda418a888feff4e8c8233acc44b6472e825cf9d758c22d69065f6`. N354 is `AUDIT_REQUIRED`; its candidate counts are not MAIN pruning credit until hostile audit passes.

The freshness checkpoint has reset to the audited N353 head. Current MAIN head is `9 ahead / 0 behind` that checkpoint; there is no current freshness freeze.

N350 remains the separate fail-closed production-registration boundary with zero registered producers. EX5 cannot self-register and receives no N350/N104/FULL178 production coverage from local results alone.

V6, O210, and Q602 are historical/formal prerequisite provenance, not current EX5 attack targets. The formal Q602 residue triple `[73,97,235]` is not the current Stage32 survivor population.

## Current exact EX5 progress

The local `(g1-d008,e=4)` Picard64 exact UNSAT blocks are `0..132`, `133..265`, `266..398`, `399..531`, `532..664`, and `665..797`. Therefore the retained local exact UNSAT prefix is **`0..797`**.

BC2-16 consumed the exact BC2-15 structural replay for ranks `665..797`. From the actual retained terminal plus locked label order it derived outer exceptional rank `5`, base terminal `[0,1,0,0,0,0,2,0,0,0,1]`, fixed exceptional mass `4`, residual mass `0`, and a complete one-parent symbolic-x4 partition. Exact result: `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`.

BC2-16 evidence canonical: `47278e00902f049e354227f02fe891b199025129a8fd3387a0249ad3b5c5ac9c`.
BC2-16 checkpoint canonical: `8cfe535fbd486b32e21c9e2cbb7c2289f2880420e5aa4cf3fc98db5f7d310a20`.
Claim-sync receipt canonical: `ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd`.

The whole `(g1-d008,e=4)` stratum remains open and FULL178 remains incomplete.

## Current next unit

`BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

It must structurally rederive the next 133-rank exceptional outer block after rank `797` by exact rank/unrank and source `terminal_predicate` replay before any new Picard64 solver credit is allowed.

## Claim and credit boundary

BC2-16 triggered `RETAINED_CONSOLIDATION`. EX5 continues to attack `S32.FULL178.NUMERICAL_CENSUS.V1`; this is the unchanged current attack target. No ACTIVE-FRONTIER remap, claim-core mutation, lane-adapter change, promotion adapter, or MAIN credit was created.

The `0..797` local prefix does not prove whole-stratum closure, FULL178 completion, N350/N104 production coverage, receiver closure, effectivity, actual-curve existence/nonexistence, Stage32 closure, theorem/endpoint credit, or Perfect Cuboid existence/nonexistence.

The legacy `N150` path remains only a compatibility alias. Historical exact evidence is immutable. `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and `AUDIT-CONTRACT.md` is the historical Cycle1 source-locked contract.

Current working PR is Draft #1765 on `impl/stage32ex5-bc2-12-outer-rank3`. CI success is not hostile-audit PASS. Merge is not authorized.
