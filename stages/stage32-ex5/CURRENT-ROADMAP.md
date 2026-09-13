# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged. Merge is not authorized.

BC2-36 hostile audit **PASS** is now consumed:

- exact head `9c63ccb48dd0e5bdeedda7739dd05e2404698465`
- review `5188625406`
- `11 UNSAT / 41 UNKNOWN / 0 SAT`
- audited known parent-UNSAT lower bound `7295`
- remaining UNKNOWN hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`

BC2-37 targets exactly those 41 hostile-audited UNKNOWN parents. The retained cold execution contract is:

- producer blob `35a1644c197fd32aec845332452cc918f3bc75d9`
- preflight canonical `30fa122941ee6b75e6e5004aa43ab121b216af93831cff0e9e22922f2438ddba`
- preflight blob `15a008cd4557fe4e81d31591c3d80b50bc595a03`
- timeout `120000 ms` per parent
- effective heavy concurrency `1`
- workflow timeout `110 minutes`
- compact artifact only; no scaleout
- generation 0 runkey is cold / `armed=false`

Cold exact-head EX5 / MAIN-startup / claim-frontier / stale-run CI must all succeed while BC2-37 heavy remains skipped. Only then may `stage32ex5-mainbatch` advance the runkey to generation 1 / `armed=true`. That semantic runkey change is the only automatic BC2-37 heavy authorization path.

While the authorized BC2-37 heavy run is active, the branch head must remain fixed. A successful computation is not audit credit: mainbatch must retain the exact result/run/artifact receipt, disarm the runkey, retire the heavy path, install a fail-closed verifier, freeze a BC2-37 hostile-audit boundary, and stop.

BC2-38 remains blocked until BC2-37 receives hostile-audit PASS. UNKNOWN remains UNKNOWN. No whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid, heavy-scaleout, or merge credit follows automatically.

Next command: `stage32ex5-mainbatch`.
