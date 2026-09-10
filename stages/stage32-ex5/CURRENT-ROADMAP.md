# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` remains the historical Cycle1 source-locked roadmap.

## Stage32 synchronization

Stage32 remains `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. The latest audited/consumed MAIN boundary remains N355 full known-prefix with residual `17128` strata / `66462870551188628549910` terminals. N356 remains `AUDIT_REQUIRED`; N350 remains a separate zero-producer registration boundary. V6/O210/Q602 and `[73,97,235]` are historical/formal provenance only.

## EX5 retained progression

The older `(g1-d008,e=4)` exact Picard64 UNSAT prefix remains `0..797` and is not whole-stratum or MAIN credit.

For `(g,d,e)=(1,8,8)`, first block `x4=0..112`:

`BC2-17 retarget -> BC2-18 mod8/HNF decomposition -> BC2-19 parent replay -> BC2-20 global union -> BC2-21 retained-64 slice -> BC2-22 retained-44 recheck -> BC2-23 redundant-cut acceleration -> BC2-24 explicit fibre-degree partition`.

Retained checkpoints establish: BC2-19 `7100 UNSAT / 236 UNKNOWN / 0 SAT`; BC2-20 global union `UNKNOWN`; BC2-21 adds `20` exact UNSAT and leaves `44` retained UNKNOWN; BC2-22 adds `8` exact UNSAT and leaves `36`; BC2-23 adds `13` exact UNSAT and leaves `23`, for a known UNSAT lower bound of `7141`. The separate `172` BC2-19 UNKNOWN identities not retained by the later slices remain uninferred.

## Current route

BC2-24 workflow `34486703108` completed successfully on exact compute head `0d20510d73d6198a33ae0a74051e457e045b3427`. The next unit is not new heavy research: it is `BC2_24_RESULT_RETENTION_AND_STATE_SYNC`.

Retrieve and retain the compact BC2-24 result, lock its exact run/head/artifact/canonical identifiers, then update `MAIN-STATE.json`, this roadmap, and `CURRENT-AUDIT-CONTRACT.md`. Until that retention is complete, do not infer a BC2-24 SAT/UNSAT/UNKNOWN outcome and do not launch BC2-25 or re-run BC2-20..23.

## MAINBATCH operations

PR #1765 is the sole active Stage32EX5 MAINBATCH PR. PR #1764 is superseded, closed, and unmerged. Old BC2-12..23 bounded-unit workflow definitions are retired from the current `.github/workflows` head; their research/provenance files remain retained. `MAINBATCH-OPERATIONS.md` is the operational contract.

No EX5 result self-promotes to whole-stratum, FULL178, N350/N104, receiver, effectivity/actual-curve, theorem, endpoint, Stage32 MAIN, or Perfect Cuboid credit. Merge requires explicit user authorization.
