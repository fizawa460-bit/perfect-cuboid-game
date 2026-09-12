# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary `ATTACKS` / producer lane for Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Ordinary EX5 research uses `stage32ex5-mainbatch`; `stage32ex5-audit` is used only after a new exact retained checkpoint is frozen. PR #1776 remains open/draft/unmerged.

At current MAIN `e4d3b8b83626526ffeccdbd9c956081735fe1a6e`, Stage32 is V15 `STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED`; authoritative residual is `17,128` strata / `47,598,978,285,064,933,757,427` terminals and FULL178 remains incomplete. EX5 must re-read current MAIN and `stages/stage32/proof/CROSS-LANE-DEMANDS.json` at startup rather than treating this observation as permanent authority.

The registered EX5 producer demand `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` is SATISFIED and there are currently no OPEN EX5 producer demands. A future higher-priority OPEN EX5 demand preempts lower-priority local continuation.

BC2-33 hostile audit **PASS** is exact head `241d65c51f93b66b79f7e8407891cc46359a45c9`, review `5185961173`.

BC2-34 replayed exactly the audited BC2-33 81-UNKNOWN set at `60000 ms` per parent, one heavy runner, no scaleout. The retained result is `17 UNSAT / 64 UNKNOWN / 0 SAT`; known parent-UNSAT lower bound `7272`; remaining UNKNOWN hash `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`.

Execution head `79167ffcdd0be4cf3bdcb7e652fad38acb447fb4`, workflow `34685719102`, compute job `103532291007`, artifact `10296591024`, checkpoint canonical `e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba`. The runkey is consumed/disarmed and the BC2-34 heavy path is retired.

BC2-34 is frozen for hostile audit. BC2-35 is blocked until audit PASS. UNKNOWN remains UNKNOWN. No whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem, effectivity, receiver, endpoint, Perfect Cuboid, heavy-scaleout, or merge credit is authorized.
