# Stage32 proof path and claim-management contract

Status: **ACTIVE MANAGEMENT LAYER — CURRENT ACTIVE FRONTIER MIGRATION ONLY**

This layer does not replace `MAIN-STATE.json`, existing certificates, leaf verifiers, hostile audits, or EX lane state. Routing authority remains in the existing state files; mathematical credit is bounded by the registered claim statement, exact source locks, authority status, and hostile-audit receipt.

Machine-readable files:

- `stages/stage32/proof/CLAIM-REGISTRY.json` — base/current authority and lane contracts.
- `stages/stage32/proof/ACTIVE-FRONTIER.json` — current active mathematical frontier only.
- `stages/stage32/proof/CLAIM-REGISTRY.schema.json` — claim record contract inherited by the frontier shard.
- `stages/stage32/proof/LANE-ADAPTERS.json` — external MAIN/EX claim-reference boundary.
- `stages/stage32/proof/verify_stage32_claim_dag.py` — base claim/DAG verifier.
- `stages/stage32/proof/verify_stage32_active_frontier.py` — composed base + active-frontier verifier.
- `stages/stage32/FINAL-CHECK.json` — fail-closed Stage32 closure check.

## 1. Stable claim IDs and immutable core

Claim IDs use `S32.<DOMAIN>.<SEMANTIC_NAME>.V<n>`.

The immutable core is:

`claim_id + kind + statement + scope_key + scope + PROVES + DOES_NOT_PROVE + requires + source_locks + replay_verifier`.

`claim_core_sha256` commits to that core. A changed quantifier, population, model, field, proof dependency, source lock, verifier, PROVES, or DOES_NOT_PROVE requires a new versioned claim ID. Audit metadata may advance on the same core, but hostile-audit PASS is never inferred or self-assigned.

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

The active-frontier verifier composes these nodes with `CLAIM-REGISTRY.json`, then reuses the same immutable-core, dependency, cycle, source-lock, replay-verifier, and cross-scope checks. It also requires every EX1–EX5 lane to connect to at least one current frontier node.

## 3. Current active mathematical frontier

The migrated nodes are exactly the currently load-bearing frontier, not a replay of Stage32 history:

```text
V6 carrier decision
  S32.V6.ACTUAL_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1    [DECLARED_GOAL / OPEN]
  S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1        [DECLARED_GOAL / OPEN]

remaining nonbijective-normalization branches
  S32.V6.SURFACE_NODE_MULTIBRANCH.V1                      [DECLARED_GOAL / OPEN]
  S32.V6.SMOOTH_AMBIENT_LOCUS_CURVE_SINGULARITY.V1       [DECLARED_GOAL / OPEN]

O210 / Q602
  S32.O210.EXCLUSION.V1                                   [DECLARED_GOAL / OPEN]
  S32.Q602.SURVIVORS_73_97_235.V1                         [AUDITED]
       -> S32.Q602.EXCLUSION.V1                           [DECLARED_GOAL / OPEN]

marking / same-member bridge
  S32.MAIN.HDECK_CHARACTER_DIRECTION.V1                   [AUDITED, base registry]
       -> S32.J2.DELTA0INF_ABSOLUTE_W_LINE_MARKING.V1     [DECLARED_GOAL / OPEN]
  S32.V6.ACTUAL_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1
       -> S32.V6.MEMBER_LEVEL_Q602_LOCAL_IDENTITY.V1      [DECLARED_GOAL / BLOCKED]

production / closure
  S32.FULL178.NUMERICAL_CENSUS.V1                         [DECLARED_GOAL / INCOMPLETE]
       -> S32.GOAL.STAGE32_CLOSURE.V1                     [DECLARED_GOAL / BLOCKED]
```

The audited residue node records only that the current survivor set is exactly `[73,97,235]` and remains uncontracted by the audited H-deck preflight. It does not select an absolute residue and does not exclude Q602 or O210.

The V6 surface-node and smooth-ambient nodes are separate because the current MAIN frontier has only reduced a surviving carrier to nonbijective normalization somewhere; neither location/type branch is closed. The existing bijective-normalization result remains a separate **PROVISIONAL** base-registry claim pending hostile re-audit after scope repair.

## 4. MAIN / EX attack map

EX1–EX5 are research lanes inside this Stage32 DAG, not independent mathematical Stages. Their current connections are stored on the frontier nodes themselves:

- `EX1`: attacks V6 actual-member/nonexistence, surface-node multibranch, smooth-ambient singularity, member-level identity, and contributes toward Stage32 closure.
- `EX2`: attacks actual V6 member, population-wide V6 member nonexistence, smooth-ambient singularity, and member-level identity.
- `EX3`: attacks surface-node/cover interaction, O210, Q602, and member-level identity; consumes the audited `[73,97,235]` survivor set.
- `EX4`: attacks absolute `delta_0inf` W-line marking, Q602 exclusion, and member-level identity; consumes the audited H-deck direction and `[73,97,235]` set.
- `EX5`: attacks the FULL178/receiver-breadth production route and therefore the numerical-census input to Stage32 closure.

No `ATTACKS` or `CONSUMES` edge grants credit. EX -> MAIN mathematical promotion still requires an audited EX terminal claim plus an explicit current-target promotion adapter. `LANE-ADAPTERS.json` itself never promotes.

## 5. FULL178 and closure

`S32.FULL178.NUMERICAL_CENSUS.V1` is deliberately an incomplete goal node. Current retained production state still has:

- `FULL_178_ROW_SWEEP_AUTHORIZED=true`;
- `FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false`;
- numerical Picard leaf checks incomplete.

Authorization/indexability therefore cannot be confused with completed numerical census credit.

`S32.GOAL.STAGE32_CLOSURE.V1` is also only a stable goal node. Actual final closure remains governed by `FINAL-CHECK.json`, whose audited milestones are:

- `S32.PROOF.NUMERICAL_CENSUS.V1`;
- `S32.PROOF.EFFECTIVITY_DISPOSAL.V1`;
- `S32.PROOF.MULTIBRANCH_LEDGER.V1`;
- `S32.PROOF.INTEGRATED_SYNTHESIS.V1`;
- `S32.PROOF.HOSTILE_AUDIT_RELEASE.V1`;
- `S32.PROOF.STAGE32_CLOSED.V1`.

Those final audited proof nodes are still absent until their exact audited artifacts exist. `--final` must therefore remain `NOT_READY_STAGE32_FINAL_CHECK`.

## 6. Migration boundary

This migration intentionally does **not** register every historical Stage32 PR, controller revision, FULL178 generation/checkpoint, archived route, scratch experiment, or old certificate as a claim. Existing evidence remains in place.

Historical material is migrated only when it becomes a direct source/dependency of a current active claim. This keeps the DAG small and prevents a second history database from replacing the existing repository evidence system.

No claim in this management migration authorizes merge, heavy compute, receiver/theorem credit, or Perfect Cuboid existence/nonexistence credit.
