# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/state surface. PR #1776 remains active.

BC2-27 hostile re-audit **PASS** is exact head `b70bc51909f5ed78641ee3b727a2258382ef950c`, review `5179488973`. Audited known parent-UNSAT lower bound is `7155`; remaining retained uncertainty is 9 parents / 13 branches / 13 p33 / 13 p34 / 13 p35 timeout leaves, with 0 SAT. The other `172` identities remain uninferred.

BC2-28 is now the one authorized bounded unit. It partitions exactly the 13 timeout p35 leaves by boundary38 using `p38=0..floor(n2/2)`, with at most `42` checks, 2000 ms per subbranch and concurrency 1. The armed runkey must source-lock the producer, target manifest, preflight and BC2-27 PASS receipt.

BC2-29 is blocked until BC2-28 result retention and a new hostile-audit boundary. No broad/heavy scaleout, merge, Stage32 MAIN/N350, FULL178, theorem, effectivity, receiver, endpoint or Perfect Cuboid credit is authorized.
