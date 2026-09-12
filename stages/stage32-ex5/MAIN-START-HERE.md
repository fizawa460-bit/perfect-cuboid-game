# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/state surface. PR #1776 remains active/open/draft/unmerged.

BC2-33 hostile audit **PASS** is consumed from exact head `241d65c51f93b66b79f7e8407891cc46359a45c9`, review `5185961173`. Its audited retained result is `26 UNSAT / 81 UNKNOWN / 0 SAT`, known parent-UNSAT lower bound `7255`, with all 81 current UNKNOWN identities explicit; hash `be6ee823abd48d2a6f8163c07977e4112036f38526f39cdddbdf331751170071`.

BC2-34 is the active bounded execution route. It may replay exactly those 81 audited UNKNOWN parents at `60000 ms` each on one heavy runner, effective concurrency 1, no scaleout, workflow timeout 90 minutes. Producer/preflight/runkey are source-locked. Generation 0 is cold/disarmed; generation 1 may be armed only after exact-head cold CI passes.

After a successful BC2-34 compute, mainbatch must retain the compact result and exact run/artifact receipt, consume/disarm the runkey, remove the heavy execution path, update fail-closed authority/verifiers, and freeze a new hostile-audit boundary. Then stop for `stage32ex5-audit`; BC2-35 remains blocked until PASS.

No timeout UNKNOWN is promoted to UNSAT. No whole-first-block/FULL178 authoritative closure, Stage32 MAIN/N350 promotion, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.
