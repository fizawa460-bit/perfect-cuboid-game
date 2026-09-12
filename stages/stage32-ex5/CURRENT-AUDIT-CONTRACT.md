# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. BC2-35 hostile audit **PASS** is consumed from exact head `8bea7a6be26e01db0deb138dbd8406f578447921`, review `5187359907`.

## No active BC2-36 audit boundary yet

BC2-36 is currently an execution route, not a hostile-audit target. `MAIN-STATE.json` must remain `new_audit_boundary_exists=false`, `freeze_active=false`, and `re_audit_required=false` while the fresh BC2-36 runkey/execution is active.

BC2-36 targets exactly the audited BC2-35 52-UNKNOWN set:

- identity hash `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`
- prior audited lower bound `7284`
- timeout `100000 ms` per parent
- concurrency `1`
- workflow timeout `110 minutes`
- no scaleout
- producer blob `18f9c2146d5dc97400c4af1a8691560523cc03cf`
- preflight canonical `b2cc1cd97fe8da4504da980aa1c470f1aa419f9417b3eea8b1533305382155b0`
- preflight blob `aa9bf40cf3550cae33cdfe8669aa51a80acddcec`

Source identity must fail-close the hostile-audited BC2-35 checkpoint, BC2-32 `7cfe8450cb9b9ab7f04da797d487655505598b93`, BC2-19 `b2899aa228e7a3ee97526e3787ffbefa483530b4`, and BC2-18 `1e2ed93cae3c5b446c8d90c1ae2250be83289c79`.

A successful heavy run alone is **not audit credit**. Before `stage32ex5-audit` is valid for BC2-36, mainbatch must retain the raw compact result and exact run/artifact receipt, independently verify hashes/counts/UNKNOWN identities, consume/disarm the runkey, retire the heavy executor, install a retained fail-closed verifier, update state/docs to a frozen new audit boundary, and obtain exact-head CI success.

Until then the last consumable local mathematical authority is BC2-35 lower bound `7284` with 52 explicit UNKNOWN parents. BC2-37 and all broad Stage32/FULL178/N350/theorem/effectivity/receiver/endpoint/Perfect Cuboid/merge credit remain blocked.
