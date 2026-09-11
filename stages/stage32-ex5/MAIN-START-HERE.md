# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/state surface. PR #1776 remains active. BC2-29 hostile audit **PASS** is exact head `ca8e0ea7209b898d24d5f647dcce11be1aff03b2`, review `5183342658`.

BC2-30 boundary42 executed exactly once at compute head `53be207f91cfd6b13ee8533efcf0af64bdccf3d6`, workflow run `34647160641`, compute job `103420643305`, artifact `10283165917`. The retained result checked all four p42 leaves: `4 UNSAT / 0 UNKNOWN / 0 SAT`; parent `1064` is newly UNSAT; **retained UNKNOWN=0**; known parent-UNSAT lower bound `7164`. Checkpoint canonical is `2bbb85361d29331957b0d6f6916ae18a18a4bb04bad4846a7144f94546a32c7a`; raw canonical is `61e9ed91020c56fba0d6addda5a31daca09a9765d7472e0ca1190c7d70e49521`.

The separate `172` BC2-19 UNKNOWN identities remain uninferred, so the whole first block is not closed. The generation-1 BC2-30 runkey is consumed/disarmed, the one-shot executor is removed, and the fail-closed retained verifier is installed. This is a fresh hostile-audit boundary. `stage32ex5-mainbatch` must stop here; BC2-31 is blocked until a fresh `stage32ex5-audit` PASS. No broad/heavy scaleout, merge, Stage32 MAIN/N350, whole-first-block/FULL178, theorem, effectivity, receiver, endpoint or Perfect Cuboid credit is authorized.
