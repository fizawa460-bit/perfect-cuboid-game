# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. Historical audit contracts remain provenance.

BC2-33 hostile audit **PASS** is consumed from exact head `241d65c51f93b66b79f7e8407891cc46359a45c9`, review `5185961173`. It certified exactly `107 checked / 26 UNSAT / 81 UNKNOWN / 0 SAT`, known parent-UNSAT lower bound `7255`, and explicit remaining-UNKNOWN hash `be6ee823abd48d2a6f8163c07977e4112036f38526f39cdddbdf331751170071`.

BC2-34 may replay exactly those 81 hostile-audited UNKNOWN parent identities at `60000 ms` per parent, one heavy runner, effective concurrency 1, workflow timeout 90 minutes, no scaleout. Producer: `bc2_34_replay_explicit_fresh_unknown81.py`; preflight: `bc2-34-fresh-unknown81-replay-preflight.json`; runkey: `runkeys/bc2-34-fresh-unknown81-replay.json`.

The generation-0 runkey is cold and not execution authority. Generation 1 may be armed only after the exact cold head passes Stage32EX5 main integrity, Stage32 claim-frontier integrity, and stale-run sweeper. The gate must observe a fresh semantic runkey generation change and the exact BC2-33 PASS receipt above.

Every successful result must partition exactly 81 audited targets into UNSAT / UNKNOWN / SAT. Remaining UNKNOWN identities must be explicit and may not be relabelled UNSAT. Any SAT is only a Picard64 feasibility witness and grants no actual-curve/effectivity credit. The known parent-UNSAT lower bound may advance only by newly exact UNSAT parents from this 81-target set.

After successful compute, mainbatch must retain the compact artifact and exact run receipt, consume/disarm the runkey, remove the BC2-34 heavy path, install a fail-closed retained boundary, freeze for `stage32ex5-audit`, and block BC2-35 until PASS.

Whole-first-block closure, whole-stratum closure, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, and merge remain unauthorized.
