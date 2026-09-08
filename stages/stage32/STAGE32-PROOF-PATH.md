# Stage32 proof path and claim-management contract

Status: **ACTIVE MANAGEMENT LAYER — CURRENT ACTIVE FRONTIER MIGRATION ONLY**

This layer does not replace `MAIN-STATE.json`, existing certificates, leaf verifiers, hostile audits, or EX lane state. Routing authority remains in the existing state files; mathematical credit is bounded by the registered claim statement, exact source locks, authority status, and hostile-audit receipt.

Machine-readable files:

- `stages/stage32/proof/CLAIM-REGISTRY.json` — base/current authority and lane contracts.
- `stages/stage32/proof/ACTIVE-FRONTIER.json` — current active mathematical frontier only.
- `stages/stage32/proof/CLAIM-REGISTRY.schema.json` — claim record contract inherited by the frontier shard.
- `stages/stage32/proof/LANE-ADAPTERS.json` — external MAIN/EX claim-reference boundary and machine-readable claim-sync trigger set.
- `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` — on-demand synchronization procedure used only at retained consolidation, authority/audit transitions, promotion, active-frontier remap, or final-milestone transition.
- `stages/stage32/proof/verify_stage32_claim_dag.py` — base claim/DAG verifier and fail-close regression tests.
- `stages/stage32/proof/verify_stage32_active_frontier.py` — composed base + active-frontier verifier, including lane startup claim-sync hooks and the stopped-lane promotion gate.
- `stages/stage32/FINAL-CHECK.json` — fail-closed Stage32 closure check.

## 1. Stable claim IDs and immutable core

Claim IDs use `S32.<DOMAIN>.<SEMANTIC_NAME>.V<n>`.

The immutable core is:

`claim_id + kind + statement + scope_key + scope + PROVES + DOES_NOT_PROVE + requires + bridges + source_locks + replay_verifier`.

`bridges` is mandatory for every `adapter_contract` and contains at least exact `from_scope_key` and `to_scope_key`. It is omitted for ordinary non-adapter claims. Because bridge semantics are part of the immutable core, changing an adapter from one scope transfer to another necessarily changes `claim_core_sha256`; it cannot silently reuse the same semantic claim hash.

`claim_core_sha256` commits to that core. A changed quantifier, population, model, field, proof dependency, bridge, source lock, verifier, PROVES, or DOES_NOT_PROVE requires a new versioned claim ID. Audit metadata may advance on the same core, but hostile-audit PASS is never inferred or self-assigned.

Authority states remain `SCRATCH`, `PROVISIONAL`, `AUDITED`, `DECLARED_GOAL`, `SUPERSEDED`, and `REVOKED`. `DECLARED_GOAL` is a stable target node and grants no mathematical credit. A state saying ready/repaired/CI-clean does not create `AUDITED` credit.

## 2. Active-frontier node contract

Every node in `ACTIVE-FRONTIER.json` carries:

- exact `statement`;
- `authority_status` and `frontier_status`;
- `proves` / `does_not_prove`;
- `requires` dependency IDs;
- exact `source_locks` and optional `replay_verifier`;
- `audit_receipt`;
- explicit `blockers`;
- `lane_links` with `MAIN=OWNER` and EX lanes as `ATTACKS` or `CONSUMES`.

The active-frontier shard contains mathematical claims only, so its declared common core-key list omits the adapter-only `bridges` field. Adapter claims live in the base registry, where bridge shape and bridge immutability are enforced. The active-frontier verifier composes the two registries and then reuses the same immutable-core, dependency, cycle, source-lock, replay-verifier, and cross-scope checks.

## 3. Current active mathematical frontier

The migrated nodes are exactly the currently load-bearing frontier, not a replay of Stage32 history:

```text
V6 carrier decision
  S32.V6.ACTUAL_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1    [DECLARED_GOAL / OPEN]
  S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1        [DECLARED_GOAL / OPEN]

remaining nonbijective-normalization branches
  S32.V6.SURFACE_NODE_MULTIBRANCH.V2                      [DECLARED_GOAL / OPEN]
  S32.V6.SMOOTH_AMBIENT_LOCUS_CURVE_SINGULARITY.V2       [DECLARED_GOAL / OPEN]

O210 / Q602
  S32.O210.EXCLUSION.V1                                   [DECLARED_GOAL / OPEN]
  S32.Q602.SURVIVORS_73_97_235.V1                         [AUDITED]
       -> S32.Q602.EXCLUSION.V1                           [DECLARED_GOAL / OPEN]

marking / same-member bridge
  S32.MAIN.HDECK_CHARACTER_DIRECTION.V1                   [AUDITED, base registry]
       -> S32.J2.DELTA0INF_ABSOLUTE_W_LINE_MARKING.V1     [DECLARED_GOAL / OPEN]
  S32.V6.ACTUAL_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1
       -> S32.V6.MEMBER_LEVEL_Q602_LOCAL_IDENTITY.V2      [DECLARED_GOAL / BLOCKED]

production / closure
  S32.FULL178.NUMERICAL_CENSUS.V1                         [DECLARED_GOAL / INCOMPLETE]
       -> S32.GOAL.STAGE32_CLOSURE.V1                     [DECLARED_GOAL / BLOCKED]
```

The audited residue node records only that the current survivor set is exactly `[73,97,235]` and remains uncontracted by the audited H-deck preflight. It does not select an absolute residue and does not exclude Q602 or O210.

The V6 surface-node and smooth-ambient nodes are separate because the current MAIN frontier has only reduced a surviving carrier to nonbijective normalization somewhere; neither location/type branch is closed. The existing bijective-normalization result remains a separate **PROVISIONAL** base-registry claim pending hostile re-audit after scope repair.

## 4. MAIN / EX attack map

EX1–EX6 are research lanes inside the Stage32 management system, not independent mathematical Stages. Their current connections are stored in `LANE-ADAPTERS.json`; active lanes are mirrored on frontier-node `lane_links`:

- `EX1`: attacks V6 actual-member/nonexistence, surface-node multibranch, smooth-ambient singularity, member-level identity, and contributes toward Stage32 closure.
- `EX2`: attacks actual V6 member, population-wide V6 member nonexistence, smooth-ambient singularity, and member-level identity.
- `EX3`: attacks surface-node/cover interaction, O210, Q602, and member-level identity; consumes the audited `[73,97,235]` survivor set.
- `EX4`: attacks absolute `delta_0inf` W-line marking, Q602 exclusion, and member-level identity; consumes the audited H-deck direction and `[73,97,235]` set.
- `EX5`: attacks the FULL178/receiver-breadth production route and therefore the numerical-census input to Stage32 closure.
- `EX6`: merged reverse O266 endpoint lane. #1697 ended `O266_ENDPOINT_NOT_CLOSED` and the lane is currently `STOPPED_PENDING_NEW_ENDPOINT_INPUT`; it therefore has no active `ATTACKS`/`CONSUMES` ref and is promotion-blocked. Its bounded result does not exclude O266, descend to O264, or move current MAIN routing. Re-entry must first perform `ACTIVE_FRONTIER_REMAP` to an exact registered claim.

No `ATTACKS` or `CONSUMES` edge grants credit. EX -> MAIN mathematical promotion still requires an audited EX terminal claim plus an explicit current-target promotion adapter. `LANE-ADAPTERS.json` itself never promotes. A stopped lane with no active claim cannot promote at all.

### 4.1 On-demand synchronization with ordinary batch work

Ordinary `stage32main batch` / `stage32exN-mainbatch` startup remains unchanged and does **not** preload this proof-management layer. Scratch-only diagnostics remain outside the claim DAG.

When a mapped lane reaches one of the machine-readable trigger events in `LANE-ADAPTERS.json` — `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION` — the agent must open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and synchronize only the affected claim/lane boundary before treating the checkpoint or downstream credit transition as complete.

Audit transitions are fail-closed and asymmetric: a PASS cannot raise consumable authority before synchronization, while a known FAIL or revocation blocks downstream consumption immediately even if the registry downgrade has not yet been written.

A future EX lane may perform scratch/provisional research before enrollment, but it cannot promote mathematical credit to MAIN until `LANE-ADAPTERS.json` contains its exact state/startup references and the claim boundary required by its current status. A stopped lane may be enrolled with no active claim only under the explicit stopped-lane gate; re-entry must attach an exact active claim before promotion.

### 4.2 EX1 retained terminal candidate checkpoint

At the current retained-consolidation checkpoint, `S32.EX1.ALL_V6_GENUS1_CARRIERS_EXCLUDED_CANDIDATE.V1` is registered as **PROVISIONAL**, not `AUDITED`. Its exact retained manifest is `stages/stage32-ex1/ex1-05af-retained-terminal-consolidation.json`, and its wrapper verifier is `stages/stage32-ex1/verify_ex1_05af_retained_terminal_consolidation.py`.

The candidate consumes the hostile-audited EX1 package through 05H, then retains the 05O–05AF chain needed for the terminal integral-descent contradiction. At provisional scope it excludes all 29 h=4 states and the three Q602 residues `[73,97,235]`; together with the audited predecessor this is an audit-ready candidate for `ALL_V6_GENUS1_CARRIERS_EXCLUDED`.

This checkpoint deliberately does **not** rewrite `stages/stage32-ex1/MAIN-STATE.json`: the existing audited EX1 claim and lane contract source-lock its current blob as immutable evidence. Until hostile audit of the terminal package, that audited state remains the routing/authority ceiling, while the new retained manifest carries the provisional operational checkpoint. No active-frontier goal is marked closed, no EX→MAIN promotion adapter is fired, and no Stage32 MAIN mathematical credit is granted.

## 5. FULL178 and closure

`S32.FULL178.NUMERICAL_CENSUS.V1` is deliberately an incomplete goal node. Current retained production state still has `FULL_178_ROW_SWEEP_AUTHORIZED=true`, `FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false`, and incomplete numerical Picard leaf checks. Authorization/indexability therefore cannot be confused with completed numerical census credit.

`S32.GOAL.STAGE32_CLOSURE.V1` is the stable **frontier goal**, not the final audited proof certificate. Actual final closure remains governed by `FINAL-CHECK.json`, whose separate audited proof milestones are:

- `S32.PROOF.NUMERICAL_CENSUS.V1`;
- `S32.PROOF.EFFECTIVITY_DISPOSAL.V1`;
- `S32.PROOF.MULTIBRANCH_LEDGER.V1`;
- `S32.PROOF.INTEGRATED_SYNTHESIS.V1`;
- `S32.PROOF.HOSTILE_AUDIT_RELEASE.V1`;
- `S32.PROOF.STAGE32_CLOSED.V1`.

FINAL-CHECK requires more than six independently AUDITED nodes. The final root `S32.PROOF.STAGE32_CLOSED.V1` must transitively depend on every other required milestone. A disconnected collection of audited milestone claims therefore fails closed even if the final root itself is AUDITED and carries `STAGE32_CLOSED=true`.

Those final audited proof nodes remain absent until their exact audited artifacts exist. `S32.GOAL.STAGE32_CLOSURE.V1` can never substitute for them; `--final` therefore remains `NOT_READY_STAGE32_FINAL_CHECK`.

## 6. Fail-close regression checks

`verify_stage32_claim_dag.py --self-test-fail-closed` executes synthetic regressions for the management invariants most likely to be silently weakened, including disconnected final milestones, FINAL-CHECK contract weakening, unresolved mathematical goal consumption, and adapter bridge immutability/shape.

The dedicated CI also runs the real `--final` path and requires exit code `2` plus `NOT_READY_STAGE32_FINAL_CHECK` while the reserved final chain is absent.

The active-frontier verifier additionally checks mapped startup hooks, the exact five synchronization triggers, the asymmetric audit transition gate, and that the only mapped lane allowed to have no active claim is the explicitly stopped and promotion-blocked EX6 lane. CI separately replays `stages/stage32-ex6/verify_main_state.py`.

## 7. Migration boundary

This migration intentionally does **not** register every historical Stage32 PR, controller revision, FULL178 generation/checkpoint, archived route, scratch experiment, or old certificate as a claim. Existing evidence remains in place.

Historical material is migrated only when it becomes a direct source/dependency of a current active claim. This keeps the DAG small and prevents a second history database from replacing the existing repository evidence system.

No claim in this management migration authorizes merge, heavy compute, receiver/theorem credit, or Perfect Cuboid existence/nonexistence credit.
