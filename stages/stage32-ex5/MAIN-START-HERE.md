# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/state surface. PR #1776 remains active/open/draft/unmerged.

BC2-32 hostile audit **PASS** is the predecessor authority: exact head `5c68ed03d77d6443c54340c90d457e80441fe414`, review `5185434136`.

BC2-33 generation 2 has completed and is retained/frozen for hostile audit. It replayed exactly the audited BC2-32 107-UNKNOWN set at `40000 ms` per parent, one heavy runner, no scaleout, and produced `26 UNSAT / 81 UNKNOWN / 0 SAT`. The known parent-UNSAT lower bound is now `7255` within the retained EX5 Picard64 feasibility surface. All 81 remaining UNKNOWN identities are explicit; hash `be6ee823abd48d2a6f8163c07977e4112036f38526f39cdddbdf331751170071`.

Execution receipt: head `109aa38ff7e7d18e80697970489976acfd489503`, workflow `34681698147`, authorize job `103521379130`, compute job `103521422359`, artifact `10294224700`, result canonical `3310103df67d47d89ac121504a668158e0946070a7b15da07bbb0af7105fa73c`, checkpoint blob `465dcb5c535c6cbbedc25ef2afe26915291ce38b`.

Generation 1 was cancelled by stale-head cleanup and is explicitly non-credit. Generation 2 is consumed/disarmed. The BC2-33 heavy execution path is removed from the active workflow.

The next command is `stage32ex5-audit`. BC2-34 is blocked until that hostile audit returns PASS. Do not resume compute, move to BC2-34, promote to Stage32 MAIN/N350, claim FULL178/theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, or merge from this boundary.
