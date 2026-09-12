# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged.

BC2-32 hostile audit **PASS** is predecessor authority: exact head `5c68ed03d77d6443c54340c90d457e80441fe414`, review `5185434136`. It certified the targeted `170` replay as `63 UNSAT / 107 UNKNOWN / 0 SAT`, raising the bounded known parent-UNSAT lower bound to `7229`; all 107 remaining UNKNOWN identities are explicit, hash `e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492`.

The current route remains `BC2_33_REFINE_REMAINING_FRESH_UNKNOWN_SET`: exactly those audited 107 UNKNOWN parents, same retained Picard64/QF_LIA feasibility model, `40000 ms` per parent, one heavy runner, no scaleout.

Generation 1 at head `75760777934825de9851811c708871412d99ab0e` was authorized correctly (workflow `34681403712`, authorize job `103520578151`) but compute job `103520625439` was cancelled by the repository stale-head sweeper before completion. Validation and artifact upload were skipped. No solver result from that run is retained and it grants zero mathematical credit. The cancellation is fail-closed in the runkey.

The execution gate is now generation-2-only. Generation 1 is disarmed. After the repaired exact cold head passes EX5 main integrity, Stage32 claim-frontier integrity, and stale-run sweeper, mainbatch may advance only the BC2-33 runkey to generation 2 / armed=true. No unrelated branch commit may be made while that heavy run is active.

After a successful generation-2 compute, retain every remaining UNKNOWN identity and any SAT Picard64 witness exactly, consume/disarm the runkey, remove the heavy execution path, freeze the BC2-33 result, and stop for `stage32ex5-audit`. BC2-34 remains blocked until hostile-audit PASS.

Whole-first-block/FULL178 closure, Stage32 MAIN/N350 promotion, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, and merge remain unauthorized.
