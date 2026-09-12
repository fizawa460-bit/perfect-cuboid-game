# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged.

BC2-33 hostile audit **PASS** is consumed: exact head `241d65c51f93b66b79f7e8407891cc46359a45c9`, review `5185961173`. Audited retained result is `26 UNSAT / 81 UNKNOWN / 0 SAT`; known parent-UNSAT lower bound `7255`; remaining-UNKNOWN hash `be6ee823abd48d2a6f8163c07977e4112036f38526f39cdddbdf331751170071`.

Current route: `BC2_34_REFINE_REMAINING_FRESH_UNKNOWN_SET`. Target exactly those 81 audited UNKNOWN parents. Replay uses the retained Picard64/QF_LIA model at `60000 ms` per parent, one heavy runner, effective concurrency 1, no scaleout, 90-minute workflow timeout.

The BC2-34 runkey is generation 0 / disarmed. It may advance to generation 1 only after the exact cold head passes Stage32EX5 main integrity, Stage32 claim-frontier integrity, and stale-run sweeper. Ordinary synchronization must not run BC2-34 heavy compute.

After successful compute: retain every remaining UNKNOWN identity and any SAT Picard64 witness exactly, consume/disarm the runkey, remove the BC2-34 heavy path, freeze the retained result, then stop for `stage32ex5-audit`. BC2-35 remains blocked until hostile-audit PASS.

Whole-first-block/FULL178 closure, Stage32 MAIN/N350 promotion, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, and merge remain unauthorized.
