# Stage32 proof path and claim-management contract

Status: **ACTIVE MANAGEMENT LAYER — CURRENT-SCOPE MIGRATION ONLY**

This file is the human-readable Stage32 proof route. It does not replace `MAIN-STATE.json`, existing certificates, leaf verifiers, hostile audits, or EX lane state. Mathematical authority remains in the exact registered claim statement together with its locked evidence and audit status.

Machine-readable authority for this management layer:

- `stages/stage32/proof/CLAIM-REGISTRY.json`
- `stages/stage32/proof/CLAIM-REGISTRY.schema.json`
- `stages/stage32/proof/LANE-ADAPTERS.json`
- `stages/stage32/proof/verify_stage32_claim_dag.py`
- `stages/stage32/FINAL-CHECK.json`

## 1. Stable claim IDs

Claim IDs use:

`S32.<DOMAIN>.<SEMANTIC_NAME>.V<n>`

The semantic core of a claim is:

`claim_id + kind + statement + scope_key + scope + PROVES + DOES_NOT_PROVE + requires`.

The registry stores `claim_core_sha256` over that canonical core. Once a claim is depended on, the core is immutable. A semantic correction, stronger/weaker quantifier, changed population/model/field, changed `PROVES`, changed `DOES_NOT_PROVE`, or changed dependency set requires a new versioned claim ID. Audit/authority metadata may advance on the same core, e.g. `PROVISIONAL -> AUDITED`, but hostile-audit PASS is never inferred or self-assigned.

## 2. Authority states

- `SCRATCH`: exploratory only. No non-scratch claim may depend on it.
- `PROVISIONAL`: retained candidate with exact scope/source locks, but no hostile-audit credit.
- `AUDITED`: hostile-audit PASS receipt is present and source locks match.
- `DECLARED_GOAL`: target, operating contract, or structural boundary; grants no mathematical credit.
- `SUPERSEDED`: retained for provenance only.
- `REVOKED`: unusable for dependencies or FINAL-CHECK.

A state file saying that a candidate is ready, repaired, or CI-clean never changes `PROVISIONAL` to `AUDITED`.

## 3. Claim record contract

Every registered claim contains:

- `statement`: exact bounded statement;
- `scope_key` and `scope`: population/model/field/hypothesis boundary;
- `PROVES`: only what downstream work may consume;
- `DOES_NOT_PROVE`: explicit anti-overclaim firewall;
- `requires`: stable claim IDs forming the dependency DAG;
- `source_locks`: exact repository path plus Git blob SHA-1 and, where available, certificate canonical SHA-256;
- `authority_status`;
- `audit_receipt`: PASS receipt for audited claims, pending/failed receipt for provisional candidates when relevant;
- optional `replay_verifier`: existing leaf/state verifier path.

`MAIN-STATE.json` remains routing authority, not a proof certificate. Claim registration does not rewrite historical evidence.

## 4. Current migrated graph

Only the current audited frontier and live MAIN/EX lanes are registered in V1.

```text
S32.MAIN.CURRENT_TARGET_CONTEXT.V1              [DECLARED_GOAL]
        |
        +--> S32.MAIN.HDECK_CHARACTER_DIRECTION.V1      [AUDITED]
        |         |
        |         +--> EX4 lane contract consumes the abstract direction only
        |
        +--> S32.MAIN.V6_BIJECTIVE_NORMALIZATION_EXCLUSION.V2 [PROVISIONAL]
        |
        +--> S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V1    [DECLARED_GOAL]
                  |
                  +--> EX1 lane contract
                  |       |
                  |       +--> S32.EX1.CANDIDATE_THROUGH_05F.V1 [PROVISIONAL]
                  +--> EX2 lane contract
                  +--> EX3 lane contract
                  +--> EX4 lane contract
                  +--> EX5 lane contract
```

The audited H-deck claim proves the abstract `chi_u -> Z3 -> delta_0inf` direction but not an absolute retained W-line or residue. The current bijective-normalization exclusion remains provisional because the Stage32 consolidation re-audit is pending after the recorded scope repair. EX1's repaired 00-through-05F package also remains provisional because re-audit is pending after a prior hostile-audit FAIL. EX2–EX5 are registered only as lane contracts/bootstrap boundaries.

## 5. MAIN / EX reference adapter

`LANE-ADAPTERS.json` maps each of `MAIN`, `EX1`, `EX2`, `EX3`, `EX4`, and `EX5` to the claim IDs it may cite from this registry.

This is deliberately external to the existing `MAIN-STATE.json` files. The adapter:

- does not modify ordinary startup order;
- does not turn state prose into proof;
- does not promote EX results;
- does not authorize heavy compute;
- does not merge;
- allows a lane to cite an audited claim without copying its text and to see an adjacent provisional claim without inheriting its credit.

An actual EX-to-MAIN mathematical promotion still requires a new explicit adapter claim binding the audited EX terminal population to the then-current MAIN population. If two mathematical claims cross `scope_key`, the DAG verifier requires an explicit scope adapter rather than silently accepting the dependency.

## 6. Stage32 global proof route

The inherited Stage32 dependency route remains:

```text
32-01 audited numerical census ---------+
                                         |
32-02 audited effectivity disposal ------+--> 32-04 audited integrated synthesis
                                         |            |
32-03 audited multibranch ledger --------+            v
                                                 32-05 hostile-audit release
                                                        |
                                                        v
                                                STAGE32_CLOSED
```

The final reserved stable IDs are:

- `S32.PROOF.NUMERICAL_CENSUS.V1`
- `S32.PROOF.EFFECTIVITY_DISPOSAL.V1`
- `S32.PROOF.MULTIBRANCH_LEDGER.V1`
- `S32.PROOF.INTEGRATED_SYNTHESIS.V1`
- `S32.PROOF.HOSTILE_AUDIT_RELEASE.V1`
- `S32.PROOF.STAGE32_CLOSED.V1`

They are intentionally not fabricated into the registry before exact audited artifacts exist.

## 7. FINAL-CHECK

`FINAL-CHECK.json` is fail-closed. `verify_stage32_claim_dag.py --integrity` checks the current management layer and is expected to pass during ongoing research. `--final` additionally requires all reserved closure claims above, each at `AUDITED`, with a PASS hostile-audit receipt and matching source locks.

The final Stage32 claim must explicitly `PROVES`:

`STAGE32_CLOSED=true`

and must not claim either:

- `PERFECT_CUBOID_EXISTENCE_CLAIM=true`
- `PERFECT_CUBOID_NONEXISTENCE_CLAIM=true`

Until the reserved audited closure chain exists, `--final` must return `NOT_READY_STAGE32_FINAL_CHECK`; that is the correct state, not a verifier defect.

## 8. Migration boundary

V1 does **not** migrate every Stage32 PR, controller revision, old certificate, scratch experiment, archive item, or historical roadmap into claims. Existing certificate/verifier/source-lock chains remain valid in place.

Migration is required only when an old result becomes load-bearing for a new current claim. At that time, register the smallest exact claim needed, lock its evidence, preserve its actual audit status, and add only the dependency edges required by the current proof path. This avoids a second historical database and prevents file/claim explosion.
