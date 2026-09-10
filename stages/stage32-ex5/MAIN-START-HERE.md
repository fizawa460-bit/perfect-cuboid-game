# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order: `AGENTS.md` -> `stages/stage32-ex5/README.md` -> this file -> `MAIN-STATE.json` -> only `MAIN-STATE.json.current_leaf_working_set`. Do not preload unrelated Stage32 history, other EX lanes, or large retained payloads unless the active leaf explicitly triggers them.

## Current authority

Stage32 remains `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. Observed MAIN PR #1753 head is `6827e386f9c450414627573ea305b9794f2341bf`; observed default `main` is `5ca6acba4b591d9e2d40057241c850598c1fa1df`.

N355 full known-prefix is hostile-audited and consumed at review `5165895301`, exact head `3f3aadd2e5ada2a0a02a69490d6d659c02762682`, leaving `17128` strata / `66462870551188628549910` terminals. N356 optimistic exceptional transportation is retained but `AUDIT_REQUIRED`; no new N356 MAIN pruning credit exists. The MAIN head is `8 ahead / 0 behind` the N355 audited head, so no intermediate freshness freeze is active. N350 remains the separate fail-closed production-registration boundary with zero registered producers.

V6/O210/Q602 and `[73,97,235]` remain historical/formal provenance only.

## Current EX5 frontier

The historical local `(g1-d008,e=4)` exact UNSAT prefix remains `0..797`; it is not a whole-stratum result. The current target is instead the `(g1-d008,e=8)` N354 survivor first block `x4=0..112`.

BC2-19 workflow `34467246133` completed all `7336` BC2-18 mod8/HNF-surviving parents with `7100 UNSAT / 236 UNKNOWN / 0 SAT`. Checkpoint canonical: `62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb`. Because `236` remain UNKNOWN, whole-block UNSAT is not credited.

## Current bounded unit

`BC2_20_GLOBAL_NORMAL_POSITIVITY_UNION_CHECK`.

Run one exact global QF_LIA system equivalent to the union of the `7336` BC2-18 parent-fixed systems. The global formulation keeps integral Picard64 coordinates, all140 nonnegative pairings, normal mass `112`, exceptional mass `8`, and the ten BC2-17 fixed exceptional pairings. A global solution induces a BC2-18 parent; a BC2-19 parent solution satisfies the global system. This is an exact disjunction compression, not a heuristic relaxation.

Heavy execution is allowed only through the dedicated fresh run-key `stages/stage32-ex5/runkeys/bc2-20-global-normal-positivity-union.json`; effective heavy concurrency is one, artifact retention one day, projected artifact below `100000` bytes. Do not mutate the branch while the authorized run is unresolved.

SAT is Picard64 pairing feasibility only; UNSAT is only the certified first-block obstruction; UNKNOWN remains blocked. No effectivity, actual-curve, whole-stratum, FULL178, N350, receiver, theorem, endpoint, Stage32 MAIN, or Perfect Cuboid credit follows automatically.

Historical `stage32-ex5.md` and `AUDIT-CONTRACT.md` are immutable Cycle1 source-locked records. Current working PR #1765 remains Draft/open/unmerged. Merge requires explicit user authorization.
