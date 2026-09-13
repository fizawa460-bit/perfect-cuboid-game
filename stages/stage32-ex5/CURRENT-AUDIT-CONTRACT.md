# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. Merge is not authorized.

BC2-36 hostile audit **PASS** is consumed from exact head `9c63ccb48dd0e5bdeedda7739dd05e2404698465`, review `5188625406`. Its bounded EX5 authority is `11 UNSAT / 41 UNKNOWN / 0 SAT`, audited known parent-UNSAT lower bound `7295`, remaining UNKNOWN hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`.

## Active BC2-37 execution contract

There is **no new hostile-audit boundary yet**. `MAIN-STATE.json` must retain `new_audit_boundary_exists=false`, `freeze_active=false`, and `re_audit_required=false` while BC2-37 is merely authorized for a fresh-runkey execution. BC2-38 remains blocked.

BC2-37 may target only the exact hostile-audited BC2-36 41-UNKNOWN set:

- identity hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`
- prior audited lower bound `7295`
- timeout `120000 ms` per parent
- effective heavy concurrency `1`
- no scaleout
- producer blob `35a1644c197fd32aec845332452cc918f3bc75d9`
- preflight canonical `30fa122941ee6b75e6e5004aa43ab121b216af93831cff0e9e22922f2438ddba`
- preflight blob `15a008cd4557fe4e81d31591c3d80b50bc595a03`

The generation-0 runkey is cold and must not execute heavy work. Only a later semantic generation-1 / `armed=true` runkey advancement after four-way cold exact-head CI SUCCESS may authorize the single BC2-37 heavy runner.

If the heavy run succeeds, mainbatch must independently verify that all 41 target identities are partitioned exactly once into UNSAT / UNKNOWN / SAT; UNKNOWN must remain UNKNOWN. It must then retain the exact artifact/raw-result/source/run receipt, consume/disarm the runkey, retire the BC2-37 heavy executor, install a fail-closed retained verifier, and freeze a new BC2-37 hostile-audit boundary before any audit is requested.

A future BC2-37 hostile-audit PASS may consume only the bounded BC2-37 refinement. It cannot automatically grant whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid, or merge credit.

Next command before a retained boundary exists: `stage32ex5-mainbatch`.
