# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/state surface. PR #1776 remains active/open/draft/unmerged.

BC2-32 hostile audit **PASS** is the current predecessor authority: exact head `5c68ed03d77d6443c54340c90d457e80441fe414`, review `5185434136`. Its audited targeted replay retained `63 UNSAT / 107 UNKNOWN / 0 SAT`, known parent-UNSAT lower bound `7229`, with all 107 current UNKNOWN identities explicit and hash `e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492`.

BC2-33 is the active bounded execution route: exactly those 107 audited UNKNOWN parents, `40000 ms` each, one heavy runner, effective concurrency 1, no scaleout. Generation 1 was correctly authorized but its compute job `103520625439` in workflow `34681403712` was cancelled by stale-head cleanup before completion; no validation/artifact occurred and no result or credit is retained. The runkey is disarmed with an explicit non-credit cancellation receipt.

The current execution gate is generation-2-only. After the repaired exact cold head passes EX5 main integrity, Stage32 claim-frontier integrity, and stale-run sweeper, `stage32ex5-mainbatch` may advance only the BC2-33 runkey from generation 1 to generation 2 / armed=true. Once generation 2 is running, do not move the branch head until the heavy job completes or fails.

After a successful compute, mainbatch must retain the compact result and run/artifact receipt, consume/disarm the runkey, remove the heavy execution path, update fail-closed authority/verifiers, and freeze a new hostile-audit boundary. Then `stage32ex5-mainbatch` stops and the next command is `stage32ex5-audit`; BC2-34 remains blocked until PASS.

No timeout UNKNOWN is promoted to UNSAT. No whole-first-block/FULL178 authoritative closure, Stage32 MAIN/N350 promotion, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.
