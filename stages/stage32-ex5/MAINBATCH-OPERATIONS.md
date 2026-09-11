# Stage32EX5 MAINBATCH operations

This file is an operational contract only. It grants no mathematical, FULL178, Stage32 MAIN, N350, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Working surface

PR #1776 is the active Stage32EX5 work/audit surface. Current Stage32 routing is still read from `stages/stage32/MAIN-STATE.json`; EX5 does not override MAIN authority.

## Retained BC2-25 boundary

BC2-25 retains 3 newly exact-UNSAT parents and leaves `16` retained UNKNOWN parents, 36 UNKNOWN branches, 38 UNKNOWN subbranches, and 0 SAT. The known parent-UNSAT lower bound is `7148`. The other `172` BC2-19 UNKNOWN identities remain uninferred. UNKNOWN must not be relabelled UNSAT.

The first hostile audit of #1776 failed at exact head `9bbc491cfde0f8a7f48d9742dad8ff368e4837b2` / review `5176133548`; compute run `34574409241` remains successful retained provenance. Repair requires the BC2-25 retained verifier, synchronized MAIN-STATE/audit boundary, and fail-closed transitive source locks through BC2-24/BC2-18 to the hperp and pairing engines.

## Mainbatch rule

For the current boundary, `stage32ex5-mainbatch` may repair and verify the existing #1776 checkpoint only. It must obtain exact-head integrity PASS and then stop for `stage32ex5-audit`.

BC2-26 is blocked until BC2-25 hostile-audit PASS. Do not launch BC2-26, broad/heavy scale-out, merge, N350 registration, or Stage32 MAIN promotion before that gate clears.

## Workflow lifecycle

Historical bounded-unit compute provenance remains in source/checkpoint/run-key/run ids. Retired historical leaf workflows must not be re-enabled as automatic PR triggers. Permanent repository/EX5 integrity gates remain governed by `AGENTS.md` and the repository workflow lifecycle policy.
