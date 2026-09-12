# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/state surface. PR #1776 remains active/open/draft/unmerged.

BC2-33 hostile audit **PASS** is consumed from exact head `241d65c51f93b66b79f7e8407891cc46359a45c9`, review `5185961173`.

BC2-34 has completed and is retained/frozen for hostile audit. It replayed exactly the audited BC2-33 81-UNKNOWN set at `60000 ms` per parent, one heavy runner, no scaleout, and produced `17 UNSAT / 64 UNKNOWN / 0 SAT`. The known parent-UNSAT lower bound is `7272`. All 64 remaining UNKNOWN identities are explicit; hash `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`.

Execution receipt: head `79167ffcdd0be4cf3bdcb7e652fad38acb447fb4`, workflow `34685719102`, authorize job `103532247242`, compute job `103532291007`, artifact `10296591024`, result canonical `e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba`, checkpoint blob `e566aeda2931642d79c88dc5eeb84b142f655609`.

Generation 1 is consumed/disarmed. The BC2-34 heavy execution path is removed from the active workflow.

The next command is `stage32ex5-audit`. BC2-35 is blocked until that hostile audit returns PASS. Do not resume compute, move to BC2-35, promote to Stage32 MAIN/N350, claim FULL178/theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, or merge from this boundary.
