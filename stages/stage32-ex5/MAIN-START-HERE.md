# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/state surface. PR #1776 remains active/open/draft/unmerged.

BC2-32 hostile audit **PASS** is the current predecessor authority: exact head `5c68ed03d77d6443c54340c90d457e80441fe414`, review `5185434136`. Its audited targeted replay retained `63 UNSAT / 107 UNKNOWN / 0 SAT`, known parent-UNSAT lower bound `7229`, with all 107 current UNKNOWN identities explicit and hash `e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492`.

BC2-33 is the active bounded execution route. It may replay exactly those 107 audited UNKNOWN parents at `40000 ms` each on one heavy runner, effective concurrency 1, no scaleout. The producer, preflight and runkey are source-locked. Generation 0 is cold/disarmed; generation 1 may be armed only after exact-head cold CI passes.

After a successful BC2-33 compute, mainbatch must retain the compact result and run/artifact receipt, consume/disarm the runkey, remove the heavy execution path, update fail-closed authority/verifiers, and freeze a new hostile-audit boundary. Then `stage32ex5-mainbatch` stops and the next command is `stage32ex5-audit`; BC2-34 remains blocked until PASS.

No timeout UNKNOWN is promoted to UNSAT. No whole-first-block/FULL178 authoritative closure, Stage32 MAIN/N350 promotion, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.
