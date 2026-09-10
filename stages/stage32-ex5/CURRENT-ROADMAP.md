# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and is not rewritten.

## Stage32 synchronization

Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Observed MAIN PR #1753 head is `6827e386f9c450414627573ea305b9794f2341bf` and observed default `main` is `5ca6acba4b591d9e2d40057241c850598c1fa1df`.

The latest audited/consumed MAIN authority is N355 full known-prefix: review `5165895301`, exact head `3f3aadd2e5ada2a0a02a69490d6d659c02762682`, result canonical `7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775`, residual `17128` strata / `66462870551188628549910` terminals. N356 optimistic exceptional transportation is the next retained candidate and remains `AUDIT_REQUIRED`; it contributes zero new MAIN pruning credit until its own audit passes. N350 producer count remains zero.

For the current EX5 `(g,d,e)=(1,8,8)` target, N356's new inequality specializes to `b-c<=16`; nonnegative exceptional mass `8` already implies `b-c<=8`, so N356 is nonbinding here. V6/O210/Q602 and `[73,97,235]` remain historical/formal provenance, not current targets/survivors.

## EX5 retained progress

The older `(g1-d008,e=4)` exact Picard64 UNSAT prefix remains `0..797` and is not promoted to whole-stratum or MAIN credit.

The current `(g1-d008,e=8)` path is:

`BC2-17 exact retarget` -> `BC2-18 selected-exceptional mod8/HNF decomposition` -> `BC2-19 normal positivity/mass parent replay` -> `BC2-20 global union check`.

BC2-18 reduced `177100` enumerated selected-exceptional parents to exactly `7336` mod8/HNF-extendable parents. BC2-19 workflow `34467246133` then checked all `7336`: `7100 UNSAT`, `236 UNKNOWN`, `0 SAT`. The retained BC2-19 checkpoint canonical is `62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb`; raw result canonical is `fcfecfc4dbd3592095c1c0302991c2b29bee22b6f3652d73612deea7775d7755`. UNKNOWN is not UNSAT, so the first block remains open.

## Current route — BC2-20

`BC2_20_GLOBAL_NORMAL_POSITIVITY_UNION_CHECK` replaces the parent-by-parent disjunction by one exact Picard64 integer system. It retains all140 nonnegativity, normal mass `112`, exceptional mass `8`, and the ten fixed BC2-17 exceptional pairings. Since those fixed selected exceptionals have mass `2`, every global solution has nineteen free selected-exceptional nonnegative integers with total at most `6`, hence induces one of BC2-18's weak-composition parents; integral Picard coordinates also witness the selected64 HNF extension. Conversely every BC2-19 SAT parent is a global solution. Therefore global SAT iff at least one BC2-18 parent is SAT.

Execution is one bounded heavy job, concurrency `1`, solver timeout `300000ms`, workflow timeout `10` minutes, one compact JSON artifact retained for one day, projected peak artifact `<=100000` bytes against the repository `500 MB` operating budget. Only a fresh commit-range run-key arm may launch it.

Outcome routing: global UNSAT -> retain exact first-block obstruction and assess whether any larger stratum coverage adapter exists; global SAT -> retain only a Picard64/all140 pairing-feasibility witness and analyze stronger special-fibre constraints; global UNKNOWN -> fall back to exact slicing of the `236` BC2-19 UNKNOWN parents.

## Credit and audit boundary

No BC2-20 outcome automatically grants whole-stratum, FULL178, N350/N104 production, receiver, effectivity/actual-curve, theorem, endpoint, Stage32 closure, or Perfect Cuboid existence/nonexistence credit. EX5 remains an `ATTACKS` lane on `S32.FULL178.NUMERICAL_CENSUS.V1`; MAIN promotion requires an explicit current-target adapter and the audit state required by Stage32.

Draft PR #1765 remains the working surface. Current retained growth from its last hostile-audited exact head `4cc001cffb871d3c6304cb38beebaf9bf2a75814` was only six commits through the BC2-19 arm, below the 90/100 intermediate-audit thresholds. CI success is not hostile-audit PASS. Merge requires explicit user authorization.
