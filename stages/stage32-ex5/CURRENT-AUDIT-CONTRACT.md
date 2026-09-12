# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. BC2-34 hostile re-audit **PASS** is consumed from exact head `cdb455860849cfd064e3ab8c83d6d4993fb5ff1b`, review `5186516652`.

## No active BC2-35 audit boundary yet

BC2-35 is currently an execution route, not a hostile-audit target. `MAIN-STATE.json` must remain `new_audit_boundary_exists=false`, `freeze_active=false`, and `re_audit_required=false` while the fresh BC2-35 runkey/execution is active.

BC2-35 targets exactly the audited BC2-34 64-UNKNOWN set:

- identity hash `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`
- prior audited lower bound `7272`
- timeout `80000 ms` per parent
- concurrency `1`
- no scaleout
- producer blob `40111bb7619113d1c9c766089026bcf59d6bdb01`
- preflight canonical `e74e6c15050187d06c472c2eff6156c66837f8f9c9de3d2cfca7629b431dadb4`
- preflight blob `bf2f4b1125925a27c820dfdc49ad796e69b268b4`

Source identity must fail-close BC2-32 `7cfe8450cb9b9ab7f04da797d487655505598b93`, BC2-19 `b2899aa228e7a3ee97526e3787ffbefa483530b4`, and BC2-18 `1e2ed93cae3c5b446c8d90c1ae2250be83289c79`.

A successful heavy run alone is **not audit credit**. Before `stage32ex5-audit` is valid for BC2-35, mainbatch must retain the raw compact result and exact run/artifact receipt, independently verify hashes/counts/UNKNOWN identities, consume/disarm the runkey, retire the heavy executor, install a retained fail-closed verifier, update state/docs to a frozen new audit boundary, and obtain exact-head CI success.

Until then the last consumable local mathematical authority is BC2-34 lower bound `7272` with 64 explicit UNKNOWN parents. BC2-36 and all broad Stage32/FULL178/N350/theorem/effectivity/receiver/endpoint/Perfect Cuboid/merge credit remain blocked.
