# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order: `AGENTS.md` -> `stages/stage32-ex5/README.md` -> this file -> `MAINBATCH-OPERATIONS.md` -> `MAIN-STATE.json` -> only the active working set. Do not preload unrelated Stage32 history, other EX lanes, or large retained payloads unless the active leaf explicitly triggers them.

## Current authority

Stage32 remains `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. The latest audited/consumed MAIN boundary remains N355 full known-prefix with residual `17128` strata / `66462870551188628549910` terminals. N356 remains audit-required. V6/O210/Q602 and `[73,97,235]` remain historical/formal provenance only.

PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3` is the sole active Stage32EX5 MAINBATCH working PR. PR #1764 is superseded, closed, and unmerged. Merge is not authorized.

## Current EX5 boundary

The current `(g,d,e)=(1,8,8)` first-block route has progressed beyond the older BC2-20 state projection:

- BC2-20 global union: `UNKNOWN` after `300000ms`; no closure.
- BC2-21 first retained-64 slice: `20 UNSAT / 44 UNKNOWN / 0 SAT`.
- BC2-22 retained-44 recheck: `8 UNSAT / 36 UNKNOWN / 0 SAT`.
- BC2-23 redundant N355 acceleration: `13 UNSAT / 23 UNKNOWN / 0 SAT`; known UNSAT lower bound `7141`, with `172` other BC2-19 UNKNOWN identities still uninferred.
- BC2-24 exact fibre-degree partition was validly authorized and run as workflow `34486703108` on compute head `0d20510d73d6198a33ae0a74051e457e045b3427`; CI execution succeeded. Its compact mathematical result has not yet been retained into the repository at this operational cleanup boundary, so no BC2-24 SAT/UNSAT/UNKNOWN outcome is asserted here.

## Current bounded unit

`BC2_24_RESULT_RETENTION_AND_STATE_SYNC`.

Do not launch another heavy EX5 unit until the compact BC2-24 result is retrieved/retained, source-locked, and the mutable state/roadmap/audit surfaces are synchronized. In particular, if `MAIN-STATE.json.current` still names BC2-20, treat that leaf as stale and non-executable; this startup file plus `MAINBATCH-OPERATIONS.md` is the newer operational guard until BC2-24 result retention updates the compact state.

Retiring old workflow definitions does not retire their retained checkpoints, solvers, run keys, commit history, or audit provenance. No effectivity, actual-curve, whole-stratum, FULL178, N350, receiver, theorem, endpoint, Stage32 MAIN, or Perfect Cuboid credit follows automatically.
