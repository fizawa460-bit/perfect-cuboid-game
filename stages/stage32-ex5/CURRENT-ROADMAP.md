# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged.

BC2-32 hostile audit **PASS** is predecessor authority: exact head `5c68ed03d77d6443c54340c90d457e80441fe414`, review `5185434136`. It certified the targeted `170` replay as `63 UNSAT / 107 UNKNOWN / 0 SAT`, raising the bounded known parent-UNSAT lower bound to `7229`; all 107 remaining UNKNOWN identities are explicit, hash `e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492`.

The current route is `BC2_33_REFINE_REMAINING_FRESH_UNKNOWN_SET`. BC2-33 targets exactly those audited 107 UNKNOWN parents, using the same retained Picard64/QF_LIA feasibility model at `40000 ms` per parent, one heavy runner, effective concurrency 1, no scaleout. The cold runkey begins at generation 0 / disarmed and may be advanced to generation 1 only after the exact cold head passes EX5 main integrity, Stage32 claim-frontier integrity, and stale-run sweeper.

If compute succeeds, retain every remaining UNKNOWN identity and any SAT Picard64 witness exactly, consume/disarm the runkey, remove the heavy execution path, freeze the BC2-33 result, and stop for `stage32ex5-audit`. BC2-34 remains blocked until hostile-audit PASS.

Whole-first-block/FULL178 closure, Stage32 MAIN/N350 promotion, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, and merge remain unauthorized.
