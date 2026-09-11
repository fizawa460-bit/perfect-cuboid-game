# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary `ATTACKS` / producer lane for Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Ordinary research uses `stage32ex5-mainbatch`; hostile audit uses `stage32ex5-audit`.

## Audited predecessor BC2-26

PR #1776 BC2-26 hostile audit PASS is exact head `34d6b030095b97c738f6faf6b9045f366622592c`, review `5177919212`. It left 12 retained UNKNOWN parents and authorized the bounded BC2-27 generation only.

## Active BC2-27 retained audit boundary

BC2-27 exactly partitions the 23 BC2-26 residual p34 UNKNOWN leaves by boundary label 35, at most 70 p35 leaves. It proves 3 additional parents `[1066,1117,1133]` exact UNSAT and leaves `9` retained UNKNOWN parents, `13` UNKNOWN branches, `13` UNKNOWN p33 subbranches, `13` UNKNOWN p34 leaves and `13` timeout UNKNOWN p35 leaves, with 0 SAT. Known parent-UNSAT lower bound is `7155`; the other `172` BC2-19 UNKNOWN identities remain uninferred.

Checkpoint canonical: `0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462`. Compute run: `34593864110`; exact compute head: `21828bcf36ea33d1e6c26465eea74c646ba26901`.

This is the new hostile-audit boundary. BC2-28 is blocked until BC2-27 hostile-audit PASS. No Stage32 MAIN/N350, whole-first-block, whole-stratum, FULL178, theorem, effectivity, receiver, endpoint, Perfect Cuboid, heavy-scaleout, or merge credit is authorized.
