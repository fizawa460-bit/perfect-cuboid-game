# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged.

BC2-35 hostile audit **PASS** remains the last consumable local mathematical authority:

- exact head `8bea7a6be26e01db0deb138dbd8406f578447921`
- review `5187359907`
- `12 UNSAT / 52 UNKNOWN / 0 SAT`
- audited known parent-UNSAT lower bound `7284`
- remaining UNKNOWN hash `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`

BC2-36 replayed exactly those 52 audited UNKNOWN parents at `100000 ms` per parent, one heavy runner, no scaleout.

Retained BC2-36 candidate result:

- `11 UNSAT / 41 UNKNOWN / 0 SAT`
- candidate known parent-UNSAT lower bound `7295`
- remaining UNKNOWN hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`
- execution head `63986c900a34cbbfa00c96a0d2dcc38d3ffc92d5`
- workflow `34718999232`
- authorize job `103621253008`
- compute job `103621306508`
- artifact `10306816385`
- artifact ZIP sha256 `35de2891058d97483fd7b3c9c95ca5c1041d9d96096287b1b01652a944f63ccb`
- raw JSON sha256 `a70320e767ffe87d0751a7df195fd54387201e170e8f7daad43d41257af61f92`
- checkpoint canonical `e92cd6d07299b833a79fe20b81e9de032d61790cf1b7a6fb81ec6adccdb49fdf`
- checkpoint blob `09ac58349e388c479ac77e04724bef2fd9b49b7e`
- consumed runkey blob `78d9c847863232b10d149b651c32c668887e4b23`

The heavy path is retired and the retained fail-closed verifier is installed. The current route is the frozen `HOSTILE_AUDIT_BC2_36_TARGETED_REPLAY` boundary.

Next command: `stage32ex5-audit`.

BC2-37 remains blocked until BC2-36 hostile-audit PASS. Until then the audited lower bound remains `7284`; `7295` is candidate-only. No timeout UNKNOWN is relabelled UNSAT and no Stage32 MAIN/FULL178/N350/theorem/effectivity/receiver/endpoint/Perfect Cuboid/merge credit follows automatically.
