# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` is the historical Cycle1 source-locked contract and must remain unchanged.

## Audit target

If the user supplies an exact PR/head, audit that target. Otherwise resolve the active EX5 surface from `MAIN-STATE.json`. Current intended surface is Draft PR #1765, branch `impl/stage32ex5-bc2-12-outer-rank3`; re-read the exact head at audit time. CI green is not hostile-audit PASS, and a later moved head is not covered by an earlier exact-head PASS.

## Current Stage32 authority observation

Stage32 remains `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. Observed MAIN PR #1753 head is `6827e386f9c450414627573ea305b9794f2341bf`.

N355 full known-prefix is hostile-audited and consumed at review `5165895301`, exact head `3f3aadd2e5ada2a0a02a69490d6d659c02762682`, with authoritative residual `17128` strata / `66462870551188628549910` terminals. N356 optimistic exceptional transportation remains `AUDIT_REQUIRED`; its candidate work is not new MAIN pruning credit. N350 remains a separate zero-producer production-registration boundary. V6/O210/Q602 and `[73,97,235]` are historical/formal provenance only.

## BC2-19 retained claim

BC2-19 is not a whole-block UNSAT claim. Audit must verify that workflow `34467246133` at exact compute head `f28112e30c0863e359c375813219196131ec6a06` was validly run-key authorized and completed all `7336` BC2-18 mod8/HNF-surviving parents with exactly `7100 UNSAT / 236 UNKNOWN / 0 SAT` using per-parent timeout `2000ms`.

Required locks:

- BC2-17 evidence canonical `a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072`;
- BC2-18 checkpoint canonical `b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8` and feasible stream SHA256 `752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7`;
- BC2-19 raw result canonical `fcfecfc4dbd3592095c1c0302991c2b29bee22b6f3652d73612deea7775d7755` and status stream SHA256 `7a551339ab56ef34ed346b7586fd3d1f1ab81de042a3be9c1a9af2bc1d9ab18a`;
- retained checkpoint canonical `62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb`;
- artifact `10148676265`, ZIP bytes `3851`, ZIP SHA256 `a455af077828cd50e1db3a9736b7a6106fe8e2e09ffaaf9305883b1660cd2d3e`;
- `236 UNKNOWN` must remain unresolved and must not be relabelled UNSAT.

## BC2-20 exact-union claim to audit after execution

BC2-20 may claim only that one global QF_LIA system is logically equivalent to the union of BC2-18's `7336` parent-fixed BC2-19 systems for the locked `(g,d,e)=(1,8,8)`, `x4=0..112` target. Independently verify both directions:

1. every BC2-19 parent SAT solution satisfies the global all140 nonnegative/mass/fixed-pairing system;
2. every global integral Picard64 solution induces one BC2-18 enumerated parent, because total exceptional mass is `8`, the fixed selected-exceptional mass is `2`, the nineteen free selected-exceptional values are nonnegative with total at most `6`, and the integral Picard vector itself witnesses the selected64/HNF extension (including the induced x4 mod-8 admissibility).

Audit the dedicated run-key by exact commit range. Heavy compute must have effective concurrency `1`, one-day artifact retention, solver timeout `300000ms`, workflow timeout `10` minutes, and projected peak artifact at most `100000` bytes. Non-key synchronizations must remain cold.

Interpret outcomes narrowly. `UNSAT` may close only this certified first block under the locked model. `SAT` may produce only Picard64/all140 pairing feasibility, not an effective curve. `UNKNOWN` grants no closure. None of these outcomes self-promotes to Stage32 MAIN.

## Preserved prior EX5 boundary

The older `(g1-d008,e=4)` exact Picard64 prefix `0..797` remains a separate local finite result. Do not conflate it with the current `(g1-d008,e=8)` first-block route. Historical Cycle1 evidence and the historical Cycle1 source-locked contract remain unchanged.

## Mandatory firewalls

Audit must preserve: no whole-stratum closure unless separately proved; FULL178 incomplete; no N350/N104 production coverage from EX5; no receiver/effectivity/actual-curve/theorem/final-milestone/endpoint credit; no Perfect Cuboid existence/nonexistence claim; no V6/O210/Q602 reopening; no automatic MAIN promotion; merge remains a separate explicit user action.

A PASS must state the exact audited head and precise local credit ceiling. FAIL must identify the first load-bearing defect without repairing the research branch inside the audit operation.
