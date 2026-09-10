# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary `ATTACKS` lane for Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Historical `stage32-ex5.md` is the historical Cycle1 source-locked roadmap and is not rewritten.

## Current Stage32 authority observation

Observed Stage32 MAIN PR #1753 head: `6827e386f9c450414627573ea305b9794f2341bf`. Current default `main` observed: `5ca6acba4b591d9e2d40057241c850598c1fa1df`.

The latest consumed MAIN authority is the N355 full known-prefix cut: hostile-audit review `5165895301`, exact audited head `3f3aadd2e5ada2a0a02a69490d6d659c02762682`, retained result canonical `7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775`. Its authoritative residual is `17128` strata / `66462870551188628549910` terminals.

N356 optimistic exceptional transportation is the current retained MAIN candidate and remains `AUDIT_REQUIRED`; it has no new MAIN pruning credit yet. For the current EX5 target `(g,d,e)=(1,8,8)`, N356 gives `b-c<=16`, while nonnegative exceptional pairings of total mass `8` already imply `b-c<=8`, so N356 does not prune this EX5 target. N350 remains zero registered producers.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance, not the current Stage32 survivor population or current EX5 attack targets.

## Retained EX5 progress

The older local `(g1-d008,e=4)` exact Picard64 UNSAT prefix remains **`0..797`** across six blocks: `0..132`, `133..265`, `266..398`, `399..531`, `532..664`, `665..797`. It does not close the whole stratum.

The current route instead attacks an audited N354 survivor at `(g1-d008,e=8)`, first normal block `x4=0..112`:

- BC2-17 fixed the exact terminal/Picard64 retarget, evidence canonical `a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072`;
- BC2-18 exhaustively enumerated `177100` selected-exceptional parents and retained exactly `7336` mod-8/HNF-extendable parents, checkpoint canonical `b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8`;
- BC2-19 exact normal-positivity/mass replay completed all `7336` checks: `7100 UNSAT / 236 UNKNOWN / 0 SAT`. It therefore does **not** prove whole-block UNSAT. Retained checkpoint canonical `62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb`, raw result canonical `fcfecfc4dbd3592095c1c0302991c2b29bee22b6f3652d73612deea7775d7755`, workflow `34467246133`.

## Current unit

`BC2_20_GLOBAL_NORMAL_POSITIVITY_UNION_CHECK` replaces the 7336 parent-fixed disjunction by one exact global Picard64 QF_LIA feasibility system. Any global integral solution induces one of BC2-18's enumerated weak-composition parents because total exceptional mass is `8`, the ten fixed selected exceptional coordinates have mass `2`, and the nineteen free selected exceptional values are nonnegative with total at most `6`; conversely every BC2-19 parent SAT solution satisfies the global system. Thus the global SAT/UNSAT question is exact for this parent union.

SAT would give only a Picard64/all140 pairing-feasibility witness; UNSAT would close only this certified first block; UNKNOWN remains unresolved. No outcome self-promotes to Stage32 MAIN.

## Credit and merge boundary

EX5 has no N350/N104 production coverage, receiver, effectivity/actual-curve, theorem, endpoint, FULL178, Stage32 closure, or Perfect Cuboid existence/nonexistence credit. Current work remains Draft PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3`. CI success is not hostile-audit PASS. Merge requires explicit user authorization.
