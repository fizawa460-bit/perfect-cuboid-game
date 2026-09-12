# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged.

BC2-34 hostile re-audit **PASS** remains the last consumable mathematical authority: exact head `cdb455860849cfd064e3ab8c83d6d4993fb5ff1b`, review `5186516652`, audited lower bound `7272`.

BC2-35 heavy execution is complete and retained:

- execution head: `c8b929e1fbbc12bb432a5d4bfd0b9aea0d03cfa8`
- workflow: `34696592793`
- authorize job: `103561025783`
- compute job: `103561129955`
- artifact: `10299388802`
- artifact ZIP sha256: `7e3b5a48300af52f19a329ed8f87e2048702b3587825b8893c2d5475aab150c3`
- raw JSON sha256: `da3f19d1e7e8f72052d9046f3e1482e669a50eeada228a3b113d440081bc266c`
- result: `12 UNSAT / 52 UNKNOWN / 0 SAT`
- candidate known parent-UNSAT lower bound: `7284`
- remaining UNKNOWN hash: `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`
- checkpoint canonical: `14f808df5db80842b87efbbc0dafb9c68ad9cc5e3529b2647cfa66ee9faccf2f`
- checkpoint blob: `ee95590c637735478c06af413835ea390000b445`

The generation-1 runkey is consumed/disarmed. The BC2-35 heavy path is retired. `verify_bc2_35_targeted_replay_checkpoint.py` is the retained fail-closed verifier.

Current operational step: `stage32ex5-audit` on the frozen BC2-35 boundary. BC2-36 remains blocked until hostile-audit PASS.

No timeout UNKNOWN is relabelled UNSAT. The retained `7284` lower bound is candidate-only until audit PASS; audited EX5 lower bound remains `7272`. No Stage32 MAIN/FULL178/N350/theorem/effectivity/receiver/endpoint/Perfect Cuboid/merge credit follows automatically.
