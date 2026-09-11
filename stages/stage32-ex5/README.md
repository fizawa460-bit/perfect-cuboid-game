# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary `ATTACKS` / producer lane for Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Historical `stage32-ex5.md` is Cycle1 source-locked provenance.

Canonical commands and ownership live in `stages/stage32/COMMANDS.md`. Ordinary EX5 research uses `stage32ex5-mainbatch`; `stage32ex5-audit` is the hostile-audit command for a frozen exact checkpoint.

## Audited BC2-25 boundary

PR #1776 retains BC2-25 boundary33 refinement. BC2-25 proves parents `[584,1030,1056]` exact UNSAT and leaves `16` retained UNKNOWN parents, `36` UNKNOWN branches, `38` UNKNOWN p33 subbranches, and 0 SAT. The known parent-UNSAT lower bound is `7148`; the other `172` BC2-19 UNKNOWN identities remain uninferred.

The first hostile audit failed at `9bbc491cfde0f8a7f48d9742dad8ff368e4837b2` / review `5176133548`. After retained-verifier/state/source-lock repair, hostile re-audit **PASS** was granted at exact head `1d2e04486e170336ce02af144aabb08e4a80a31d`, review `5177354131`. That PASS is consumed for bounded BC2-26 only. Merge freshness remains separate and merge is not authorized.

## BC2-26 bounded continuation

BC2-26 targets exactly the 38 audited residual p33 UNKNOWN subbranches. It partitions each by boundary pairing label 34 using `n2 = 2*p34 + sum(incident exceptional pairings)` with `p34=0..floor(n2/2)`. The exact maximum is `110` p34 leaf checks, concurrency 1. The other `172` identities remain uninferred.

This is not broad/heavy scale-out and grants no whole-first-block, whole-stratum, FULL178, N350, Stage32 MAIN, theorem, effectivity, receiver, endpoint, or Perfect Cuboid credit. After BC2-26 is frozen, BC2-27 is blocked until a new hostile audit.
