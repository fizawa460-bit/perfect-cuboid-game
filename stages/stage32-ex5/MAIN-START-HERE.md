# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/operations/state surface. Historical Cycle1 files remain source-locked provenance.

## Active work surface

PR #1776 is the active EX5 work surface. BC2-25 is retained and hostile-audited PASS at exact head `1d2e04486e170336ce02af144aabb08e4a80a31d`, review `5177354131`. Its retained boundary is `3` new parent UNSAT / `16` parent UNKNOWN / 0 SAT, known parent-UNSAT lower bound `7148`, with `36` UNKNOWN branches and `38` UNKNOWN p33 subbranches. The other `172` BC2-19 UNKNOWN identities remain uninferred.

Current main observed for this continuation is `c31684fb5f63d8a025eb298c91861d4c979b0e28`. The two commits beyond the PR merge-base were reviewed as non-load-bearing for BC2-25; merge-ready freshness remains PENDING and merge is not authorized.

## Startup route

`stage32ex5-mainbatch` may consume the BC2-25 PASS and execute only `BC2_26_BOUNDARY34_PARTITION_BOUNDED`: exact p34 partition of the 38 audited residual p33 UNKNOWN subbranches, maximum `110` leaves, concurrency 1. Preserve UNKNOWN and leave all `172` other identities uninferred.

After a BC2-26 result is frozen, stop and require a new `stage32ex5-audit` before BC2-27. No broad/heavy scale-out, merge, Stage32 MAIN/N350 promotion, theorem, receiver, effectivity, endpoint, or Perfect Cuboid credit is authorized.
