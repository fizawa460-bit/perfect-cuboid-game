# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. Historical audit contracts remain provenance.

BC2-33 hostile audit **PASS** is consumed from exact head `241d65c51f93b66b79f7e8407891cc46359a45c9`, review `5185961173`.

## BC2-34 retained boundary under audit

BC2-34 replayed exactly the hostile-audited BC2-33 81-UNKNOWN parent set at `60000 ms` per parent, one heavy runner, no scaleout.

Exact receipts:

- execution head `79167ffcdd0be4cf3bdcb7e652fad38acb447fb4`
- workflow `34685719102`
- authorize job `103532247242`
- compute job `103532291007`
- artifact `10296591024`
- artifact ZIP sha256 `1aff75ecda329d8770c7cd6c120eb0aeb8630521ed68dd93427079f8eee09792`
- raw JSON sha256 `d2b8963c21fbb3d8cf5c739169c41bdc6a0ac4036540d6cf8e6e807159033a63`
- retained result/checkpoint canonical `e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba`
- checkpoint git blob `e566aeda2931642d79c88dc5eeb84b142f655609`
- status stream sha256 `3dfc34636f7a44093e0c93034bf74442fd5cadcdf197b28f8bf674ca7bfe19c2`
- result `17 UNSAT / 64 UNKNOWN / 0 SAT`
- remaining UNKNOWN identity hash `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`
- known parent-UNSAT lower bound `7272`

Every remaining UNKNOWN identity is explicitly retained. No timeout UNKNOWN is relabelled UNSAT. There is no SAT witness.

The generation-1 runkey is consumed/disarmed. The BC2-34 authorize/compute heavy jobs are removed from the active workflow. The live state is frozen with `re_audit_required=true`; BC2-35 is blocked until hostile-audit PASS.

## Hostile-audit obligations

Audit must verify the BC2-33 PASS receipt, BC2-34 source/preflight/checkpoint blob and canonical locks, exact execution/artifact receipt, exact `17/64/0` partition, retained 64-identity hash, lower bound `7272`, runkey consumption/disarm, heavy-path retirement, and all credit firewalls.

Whole-first-block closure, whole-stratum closure, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, and merge remain unauthorized.
