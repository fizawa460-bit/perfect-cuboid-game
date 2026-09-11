# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged.

## Consumed BC2-27 audit

BC2-27 hostile re-audit **PASS** is exact head `b70bc51909f5ed78641ee3b727a2258382ef950c`, review `5179488973`. The prior FAIL remains recorded at `43fce7733be95b47b2d2a4e4568300add7694224`, review `5179261378`. Audited bounded credit advances the known parent-UNSAT lower bound to `7155` and leaves 9 retained UNKNOWN parents / 13 branches / 13 p33 / 13 p34 / 13 p35 timeout leaves, 0 SAT, while the other `172` identities remain uninferred.

## BC2-28 authorized unit

BC2-28 may execute exactly once under its generation-1 runkey. Target: the 13 BC2-27 timeout p35 leaves. Partition: boundary38 with exact common second-factor fibre degree `n2`, `p38=0..floor(n2/2)`. Maximum `42` checks, timeout 2000 ms each, concurrency 1. The producer, manifest, preflight, runkey and BC2-27 PASS receipt must be exact source-locked.

A successful computation is not itself audit credit. Mainbatch must retain the raw result and exact run/artifact receipt, disarm the runkey, install a fail-closed verifier, freeze a new BC2-28 hostile-audit boundary, and stop. BC2-29 is blocked until a later `stage32ex5-audit` PASS.

Merge authorization remains false and independent. No whole-first-block, whole-stratum, FULL178, N350, Stage32 MAIN, theorem, effectivity, receiver, endpoint, Perfect Cuboid, or heavy-scaleout credit follows from BC2-28 execution.
