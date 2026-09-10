# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` remains the historical Cycle1 source-locked contract.

## Audit target

Unless the user supplies another exact target, audit Draft PR #1765, branch `impl/stage32ex5-bc2-12-outer-rank3`, and re-read its exact head at audit time. CI green is not hostile-audit PASS, and a moved head is not covered by an earlier PASS.

## Mandatory operational consolidation checks

Before mathematical credit review, verify all of the following:

1. PR #1764 is closed, unmerged, and marked superseded; PR #1765 is the only active Stage32EX5 MAINBATCH working PR.
2. `stages/stage32-ex5/MAINBATCH-OPERATIONS.md` is in the startup path and forbids ordinary creation of a second MAINBATCH PR while #1765 is active.
3. BC2-12 through BC2-23 bounded-unit workflow definitions are absent from the current `.github/workflows` head, while their solver/checkpoint/run-key/Git provenance remains available.
4. BC2-24 remains the only live Stage32EX5 bounded-unit heavy workflow at this boundary.
5. A non-key synchronization after the cleanup may materialize the BC2-24 authorize job, but its heavy `fibre-degree-partition` job must skip unless the BC2-24 run key generation advances in the exact `before..head` range.
6. This operational cleanup grants zero new mathematical or Stage32 MAIN credit and does not authorize merge.

## Retained mathematical boundary to preserve

The current `(g,d,e)=(1,8,8)`, first block `x4=0..112`, retained chain includes:

- BC2-19 checkpoint canonical `62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb`: `7100 UNSAT / 236 UNKNOWN / 0 SAT`.
- BC2-20 checkpoint canonical `5b702386389913ecae9972e210e67bccca992df3a84eda1199fbe1862e8cec06`, workflow `34477367203`: global union `UNKNOWN` at `300000ms`; no closure.
- BC2-21 checkpoint canonical `8b40a6b0ee650897d276fb7e543d6f31ef3f76af6f3e923e109b8d02ecd46f`, workflow `34481575923`: `20 UNSAT / 44 UNKNOWN / 0 SAT` on the retained first 64 identities.
- BC2-22 checkpoint canonical `e8151702d8386eeab44d9e9705abe7b4fa0e19dde96933ffdabdc56329f2fdc2`, workflow `34482947476`: `8 UNSAT / 36 UNKNOWN / 0 SAT` on the retained residual 44.
- BC2-23 checkpoint canonical `6da1c158da8f8171d446c39b517270c0f7bf524ac62df0cd8f9d099155cdb3a0`, workflow `34485549615`: `13 UNSAT / 23 UNKNOWN / 0 SAT`, known UNSAT lower bound `7141`; the other `172` BC2-19 UNKNOWN identities remain uninferred.

BC2-24 authorized workflow `34486703108` ran successfully on exact compute head `0d20510d73d6198a33ae0a74051e457e045b3427`, but its compact mathematical result is not yet retained in the repository at this cleanup boundary. Audit must not infer its SAT/UNSAT/UNKNOWN outcome from CI success alone. The current executable leaf is therefore `BC2_24_RESULT_RETENTION_AND_STATE_SYNC`, not a rerun of BC2-20..23.

## Freshness / firewalls

The last EX5 hostile-audited exact head remains `4cc001cffb871d3c6304cb38beebaf9bf2a75814`. The first cleanup head was 32 commits ahead, below the repository 90/100 intermediate-audit thresholds; re-count at audit time.

Preserve: no UNKNOWN->UNSAT relabelling; no uninferred identity fabrication; no whole-stratum closure unless separately proved; FULL178 incomplete; no N350/N104 production coverage from EX5; no receiver/effectivity/actual-curve/theorem/final-milestone/endpoint credit; no Perfect Cuboid existence/nonexistence claim; no V6/O210/Q602 reopening; no automatic MAIN promotion; merge remains an explicit user action.

A PASS must state the exact audited head and the precise local/operational credit ceiling. FAIL must identify the first load-bearing defect without repairing the research branch inside the audit operation.
