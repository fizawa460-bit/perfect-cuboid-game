# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. Historical audit contracts remain provenance.

BC2-33 hostile audit **PASS** remains the last consumable EX5 mathematical authority: exact head `241d65c51f93b66b79f7e8407891cc46359a45c9`, review `5185961173`, known parent-UNSAT lower bound `7255`, with `81` explicit UNKNOWN parents.

## BC2-34 computation retained, first hostile audit failed

BC2-34 replayed exactly the hostile-audited BC2-33 81-UNKNOWN parent set at `60000 ms` per parent, one heavy runner, no scaleout.

Exact compute receipts remain unchanged:

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
- candidate known parent-UNSAT lower bound `7272`

The first BC2-34 hostile audit **FAIL** is retained at exact head `75723b1626d7f40eb1ab75a1a52f2fc679d619bf`, review `5186319290`. The audit accepted the computation, artifact identity, partition, checkpoint, runkey consumption and credit firewalls, but found one load-bearing dependency-identity defect: BC2-34 directly executed `b32.build_parent_space()` without itself fail-closing the identity of the BC2-32 producer module whose code was executed.

The failed audit independently confirmed that the BC2-32 producer was byte-identical at the immutable BC2-34 execution head and failed-audit head, Git blob `7cfe8450cb9b9ab7f04da797d487655505598b93`. Therefore no heavy recomputation is required solely for this repair and the mathematical result is not rewritten.

## Dependency-identity repair frozen for re-audit

The repair is retained in `breadth-cycle-2/bc2-34-dependency-identity-repair.json`, Git blob `5569d0d0c806db361ad6cafdafbe5e7911850e4c`, canonical `fb111cd123eb1ee0aa99848fc7c75bd976684517cd63a2bfd44f9e9abdaed01f`.

The consumed BC2-34 run receipt now records the missing BC2-32 producer identity, immutable execution head, failed-audit head/review, and the fact that neither heavy recomputation nor mathematical-result rewriting occurred. `verify_bc2_34_dependency_identity_repair.py` fail-closes the current BC2-32 blob against `7cfe8450...`, preserves the BC2-19/BC2-18 transitive source guards, locks the repair receipt, and is necessarily executed by `verify_main_state.py`.

Generation 1 remains consumed/disarmed. The BC2-34 heavy path remains retired. The live V22 state remains frozen with `re_audit_required=true`; BC2-35 remains blocked until a hostile re-audit PASS.

## Re-audit obligations and credit ceiling

Re-audit must verify the BC2-33 PASS receipt, unchanged BC2-34 compute/artifact/checkpoint evidence, exact `17/64/0` partition, remaining 64-identity hash, the repaired BC2-32 blob lock `7cfe8450cb9b9ab7f04da797d487655505598b93`, repair receipt blob/canonical, consumed-run repair projection, transitive BC2-19/BC2-18 guards, heavy-path retirement, and all credit firewalls.

Until that re-audit passes, BC2-34 `17/64/0` and lower bound `7272` are retained computational evidence but **not consumable audited credit**. Last hostile-audited credit remains BC2-33 lower bound `7255` with 81 explicit UNKNOWN parents.

Whole-first-block closure, whole-stratum closure, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, BC2-35 execution, and merge remain unauthorized. The next command is `stage32ex5-audit`.
