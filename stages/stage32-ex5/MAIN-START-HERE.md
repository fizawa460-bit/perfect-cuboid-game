# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. current `stages/stage32/MAIN-STATE.json`;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. `stages/stage32-ex5/CROSS-LANE-STATE.json` when present;
6. `stages/stage32-ex5/README.md`;
7. this file;
8. `MAINBATCH-OPERATIONS.md`;
9. `stages/stage32-ex5/MAIN-STATE.json`;
10. only the active EX5 working set required by the selected route.

PR #1776 remains active/open/draft/unmerged. Historical Cycle1 files remain source-locked provenance.

## Cross-lane demand priority

Before local EX5 research, inspect every `OPEN` demand with `producer_lane=EX5`. A higher-priority OPEN demand preempts lower-priority local work. A SATISFIED demand is only an operational handoff and **does not grant mathematical credit**.

At current MAIN `e4d3b8b83626526ffeccdbd9c956081735fe1a6e`, the only registered EX5 producer demand, `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1`, is **SATISFIED**. There are no OPEN EX5 producer demands. A later OPEN demand may preempt local continuation after audit.

## Current authority

Current Stage32 MAIN is V15 `STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED`, with FULL178 still incomplete. Its authoritative residual is `17,128` strata / `47,598,978,285,064,933,757,427` terminals. This routing synchronization does not rewrite or promote EX5 mathematical evidence.

BC2-33 hostile audit **PASS** remains the last consumable EX5 mathematical authority: exact head `241d65c51f93b66b79f7e8407891cc46359a45c9`, review `5185961173`, lower bound `7255`, with `81` explicit UNKNOWN parents.

## BC2-34 repaired re-audit boundary

BC2-34 replayed exactly the audited BC2-33 81-UNKNOWN set at `60000 ms` per parent, one heavy runner, no scaleout, and produced retained computational evidence `17 UNSAT / 64 UNKNOWN / 0 SAT` with candidate lower bound `7272`.

Compute provenance is unchanged:

- execution head: `79167ffcdd0be4cf3bdcb7e652fad38acb447fb4`
- workflow: `34685719102`
- authorize job: `103532247242`
- compute job: `103532291007`
- artifact: `10296591024`
- checkpoint canonical: `e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba`
- checkpoint blob: `e566aeda2931642d79c88dc5eeb84b142f655609`
- remaining UNKNOWN hash: `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`

The first BC2-34 hostile audit **FAIL** is retained at exact head `75723b1626d7f40eb1ab75a1a52f2fc679d619bf`, review `5186319290`. The defect was not the mathematical output: BC2-34 directly executed the BC2-32 producer's `build_parent_space()` code without fail-closing the BC2-32 module identity itself.

The repaired boundary now source-locks that directly executed BC2-32 producer to Git blob `7cfe8450cb9b9ab7f04da797d487655505598b93`, which the failed audit independently confirmed at both the immutable execution head and failed-audit head. The repair receipt is `breadth-cycle-2/bc2-34-dependency-identity-repair.json`, blob `5569d0d0c806db361ad6cafdafbe5e7911850e4c`, canonical `fb111cd123eb1ee0aa99848fc7c75bd976684517cd63a2bfd44f9e9abdaed01f`. The consumed run receipt retains this dependency identity and failed-audit provenance, and `verify_main_state.py` necessarily executes `verify_bc2_34_dependency_identity_repair.py`.

Generation 1 remains consumed/disarmed. The BC2-34 heavy path remains retired. Heavy recomputation was not performed and the mathematical result was not rewritten. All 64 remaining UNKNOWN identities remain explicit UNKNOWN.

Until hostile re-audit PASS, BC2-34 `17/64/0` and lower bound `7272` are provisional retained evidence only; last audited credit remains BC2-33 lower bound `7255`.

The next command is `stage32ex5-audit`. BC2-35 remains blocked until hostile re-audit PASS. Do not resume compute, move to BC2-35, promote to Stage32 MAIN/N350, claim whole-first-block/FULL178/theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, or merge from this boundary.
