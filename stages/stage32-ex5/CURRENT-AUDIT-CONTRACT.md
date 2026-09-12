# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. The last consumable EX5 mathematical authority is BC2-34 hostile re-audit **PASS** at exact head `cdb455860849cfd064e3ab8c83d6d4993fb5ff1b`, review `5186516652`.

## Active BC2-35 audit boundary

BC2-35 is now a hostile-audit target. `MAIN-STATE.json` must remain `new_audit_boundary_exists=true`, `freeze_active=true`, and `re_audit_required=true` until `stage32ex5-audit` records PASS or a repair is required.

Retained BC2-35 execution receipt:

- execution head `c8b929e1fbbc12bb432a5d4bfd0b9aea0d03cfa8`
- workflow `34696592793`
- authorize job `103561025783`
- compute job `103561129955`
- artifact `10299388802`
- artifact ZIP sha256 `7e3b5a48300af52f19a329ed8f87e2048702b3587825b8893c2d5475aab150c3`
- raw JSON sha256 `da3f19d1e7e8f72052d9046f3e1482e669a50eeada228a3b113d440081bc266c`
- checkpoint canonical `14f808df5db80842b87efbbc0dafb9c68ad9cc5e3529b2647cfa66ee9faccf2f`
- checkpoint blob `ee95590c637735478c06af413835ea390000b445`

Retained mathematical partition:

- exact target: audited BC2-34 64-UNKNOWN set, hash `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`
- `12 UNSAT / 52 UNKNOWN / 0 SAT`
- remaining 52 UNKNOWN hash `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`
- candidate known parent-UNSAT lower bound `7284`
- last audited known parent-UNSAT lower bound remains `7272`

Source identity must fail-close BC2-35 producer `40111bb7619113d1c9c766089026bcf59d6bdb01`, preflight `bf2f4b1125925a27c820dfdc49ad796e69b268b4`, BC2-32 `7cfe8450cb9b9ab7f04da797d487655505598b93`, BC2-19 `b2899aa228e7a3ee97526e3787ffbefa483530b4`, and BC2-18 `1e2ed93cae3c5b446c8d90c1ae2250be83289c79`.

The generation-1 BC2-35 runkey must be consumed/disarmed and its exact receipt must match the checkpoint. The BC2-35 authorize/heavy executor must be absent from the active workflow. `verify_bc2_35_targeted_replay_checkpoint.py` must run on exact-head CI and fail-close partition, hashes, receipts, source locks, UNKNOWN retention and credit firewalls.

Hostile audit must independently verify that all 64 target identities are partitioned exactly, no UNKNOWN was dropped/relabelled, the artifact receipt matches the successful exact-head run, source dependencies are identity-locked, and no candidate credit leaked into Stage32 MAIN/FULL178 or theorem/effectivity/receiver/endpoint/Perfect Cuboid claims.

BC2-36 and all broad credit remain blocked until BC2-35 hostile-audit PASS. Merge remains unauthorized.
