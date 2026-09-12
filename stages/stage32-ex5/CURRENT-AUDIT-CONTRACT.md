# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. BC2-35 hostile audit **PASS** remains the predecessor consumable authority from exact head `8bea7a6be26e01db0deb138dbd8406f578447921`, review `5187359907`.

## Active BC2-36 audit boundary

BC2-36 is now a frozen hostile-audit target. `MAIN-STATE.json` must retain `new_audit_boundary_exists=true`, `freeze_active=true`, and `re_audit_required=true`; BC2-36 execution is retired and BC2-37 remains blocked.

BC2-36 targeted exactly the audited BC2-35 52-UNKNOWN set:

- identity hash `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`
- prior audited lower bound `7284`
- timeout `100000 ms` per parent
- concurrency `1`
- no scaleout
- producer blob `18f9c2146d5dc97400c4af1a8691560523cc03cf`
- preflight canonical `b2cc1cd97fe8da4504da980aa1c470f1aa419f9417b3eea8b1533305382155b0`
- preflight blob `aa9bf40cf3550cae33cdfe8669aa51a80acddcec`

Retained execution receipt:

- execution head `63986c900a34cbbfa00c96a0d2dcc38d3ffc92d5`
- workflow `34718999232`
- authorize job `103621253008`
- compute job `103621306508`
- artifact `10306816385`
- artifact ZIP sha256 `35de2891058d97483fd7b3c9c95ca5c1041d9d96096287b1b01652a944f63ccb`
- raw JSON sha256 `a70320e767ffe87d0751a7df195fd54387201e170e8f7daad43d41257af61f92`

Retained result to audit:

- `11 UNSAT / 41 UNKNOWN / 0 SAT`
- candidate lower bound `7295`
- remaining 41 UNKNOWN hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`
- status-stream sha256 `59c8f444d235a7b3223d2ef4df5c2da65636f66edc3f69ebd2572c2d3354dff8`
- checkpoint canonical `e92cd6d07299b833a79fe20b81e9de032d61790cf1b7a6fb81ec6adccdb49fdf`
- checkpoint blob `09ac58349e388c479ac77e04724bef2fd9b49b7e`
- consumed/disarmed runkey blob `78d9c847863232b10d149b651c32c668887e4b23`
- retained verifier blob `837e5d9f26088e723df759a674993f5ab900a4dc`

Hostile audit must independently verify exact target partition, artifact/raw-result identity, source-lock chain through BC2-32/BC2-19/BC2-18, UNKNOWN preservation, runkey consumption, heavy-path retirement, state freeze, and broad-credit firewalls.

A BC2-36 hostile-audit PASS may advance the local audited lower bound from `7284` to `7295` and release BC2-37 under the route contract. It does not by itself grant whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid, or merge credit.

Next command: `stage32ex5-audit`.
