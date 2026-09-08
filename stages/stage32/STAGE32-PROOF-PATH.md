# Stage32 proof path and claim-management contract

Status: **ACTIVE MANAGEMENT LAYER — POST-#1728 V6-NEGATIVE FRONTIER**

This layer does not replace `MAIN-STATE.json`, retained certificates, leaf verifiers, hostile audits, or FINAL-CHECK. Ordinary routing authority is `stages/stage32/MAIN-STATE.json`; mathematical credit is bounded by registered immutable claim cores, exact source locks, and hostile-audit receipts.

Machine-readable files:

- `stages/stage32/proof/CLAIM-REGISTRY.json`
- `stages/stage32/proof/ACTIVE-FRONTIER.json`
- `stages/stage32/proof/LANE-ADAPTERS.json`
- `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md`
- `stages/stage32/proof/verify_stage32_claim_dag.py`
- `stages/stage32/proof/verify_stage32_active_frontier.py`
- `stages/stage32/FINAL-CHECK.json`

## 1. Stable claim / authority rule

Claim IDs use `S32.<DOMAIN>.<SEMANTIC_NAME>.V<n>`. The immutable core contains claim ID, kind, statement, scope key/scope, PROVES, DOES_NOT_PROVE, dependencies, adapter bridges when present, source locks, and replay verifier. A semantic/evidence change requires a new versioned claim ID. Audit metadata may advance on the same unchanged core only from an external exact-head hostile-audit receipt.

Authority states remain `SCRATCH`, `PROVISIONAL`, `AUDITED`, `DECLARED_GOAL`, `SUPERSEDED`, and `REVOKED`. `DECLARED_GOAL` grants no proof credit. Hostile-audit PASS, claim-DAG synchronization, merge-ready freshness, and merge authorization are distinct gates.

`MAIN-STATE.json` is mutable routing authority rather than immutable mathematical evidence. When an older registered claim source-locks a historical `MAIN-STATE.json` blob, the exact old routing blob may be retained under `proof/historical-routing-blobs/<blob_sha1>.json`; this does not relax any non-routing evidence lock.

## 2. Audited #1728 authority consumed by MAIN

PR #1728 supplied two hostile-audit checkpoints.

Terminal EX1 claim:

- `S32.EX1.ALL_V6_GENUS1_CARRIERS_EXCLUDED_CANDIDATE.V2`
- **AUDITED**
- exact head `e3c4a04d5010e6dca9428722e334890e2614297a`
- review `5147627146`
- result `FULL_TARGET_CLOSURE / ALL_V6_GENUS1_CARRIERS_EXCLUDED` at exact EX1 scope.

Concrete EX1 -> MAIN population adapter and MAIN-scope result:

- `S32.ADAPTER.EX1_V6_CARRIER_TO_MAIN_V6_CARRIER.V1` — **AUDITED**
- `S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2` — **AUDITED**
- exact promotion-audit head `89ba026f05f9fe5344c0f0fb41fe8c2366032877`
- review `5147810198`.

The promotion audit establishes exact population identity for integral irreducible geometric-genus-1 curves in Picard class V6 on the minimal desingularization S for row `g1-d186`. Therefore Stage32 MAIN may consume the statement that this entire V6 genus-1 carrier population is empty.

This does **not** itself grant Q602 exclusion, O210 exclusion, FULL178 completion, Stage32 closure, or Perfect Cuboid existence/nonexistence credit.

## 3. Post-#1728 active frontier

The active frontier is now exactly:

```text
S32.O210.EXCLUSION.V1                       [DECLARED_GOAL / OPEN]
S32.Q602.SURVIVORS_73_97_235.V1             [AUDITED_TRUE]
S32.Q602.EXCLUSION.V1                        [DECLARED_GOAL / OPEN]
S32.FULL178.NUMERICAL_CENSUS.V1              [DECLARED_GOAL / INCOMPLETE]
S32.GOAL.STAGE32_CLOSURE.V1                  [DECLARED_GOAL / BLOCKED]
```

The following former frontier nodes are no longer active because their premise/goal is dominated by the stronger audited whole-population V6 nonexistence result:

- `S32.V6.ACTUAL_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1`
- `S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1`
- `S32.V6.SURFACE_NODE_MULTIBRANCH.V2`
- `S32.V6.SMOOTH_AMBIENT_LOCUS_CURVE_SINGULARITY.V2`
- `S32.J2.DELTA0INF_ABSOLUTE_W_LINE_MARKING.V1`
- `S32.V6.MEMBER_LEVEL_Q602_LOCAL_IDENTITY.V2`.

Removal from the active frontier does **not** mean those old statements were independently hostile-audited true. In particular, the local multibranch/smooth-singularity branches and absolute-marking problem are retired only because no target V6 genus-1 carrier exists on the selected closure route.

The historical `[73,97,235]` survivor claim remains audited arithmetic provenance. It is not contradicted by V6 population emptiness: it records what survived the older residue filter before the new population-level obstruction is applied.

## 4. Remaining O210 / Q602 adapters

The next cross-lane obligation is deliberately typed.

For O210, MAIN must retain and hostile-audit an adapter proving that the exact current O210 carrier/cover population is a subpopulation of the already audited-empty MAIN V6 integral-irreducible genus-1 carrier population. Only then may `S32.O210.EXCLUSION.*` receive authority from population emptiness. This is not an EX3 monodromy proof.

For Q602, MAIN must separately retain and hostile-audit an adapter showing that the exact current Q602 admissible-residue population is attached only to that same carrier population. `S32.Q602.EXCLUSION.V1` expressly permits an equally exact population-preserving obstruction. If this adapter passes, Q602 can be closed without pretending that 73, 97, and 235 were individually eliminated by the old residue-specific arithmetic. O210 does not follow automatically from Q602, and Q602 does not follow automatically from O210.

Until these adapters receive hostile-audit PASS and claim synchronization:

```text
Q602_excluded=false
O210_excluded=false
```

## 5. MAIN / EX routing after remap

- `EX1`: `COMPLETED_AUDITED_HANDOFF`. No active attack; retained as authority/provenance.
- `EX2`: `DOMINATED_BY_AUDITED_V6_NONEXISTENCE`. Actual-member/genus-1 reconstruction is no longer load-bearing; re-entry requires explicit remap.
- `EX3`: remains attached to O210 and Q602 as an alternative route while MAIN tests the V6-empty population adapters.
- `EX4`: absolute-marking route is parked; remains attached to Q602 as an alternative until the population adapter is audited.
- `EX5`: remains active on FULL178 / receiver breadth.
- `EX6`: remains `STOPPED_PENDING_NEW_ENDPOINT_INPUT`.

Empty active refs for EX1/EX2/EX6 are fail-closed by `promotion_blocked_without_active_claim=true` in `LANE-ADAPTERS.json`.

## 6. Claim-DAG synchronization

Ordinary `stage32mainbatch` startup remains the Stage-local four-item startup and does not preload this proof layer. On `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, follow `CLAIM-SYNC-CONTRACT.md` and run:

```text
python stages/stage32/proof/verify_stage32_claim_dag.py --integrity
python stages/stage32/proof/verify_stage32_active_frontier.py
```

Scratch-only diagnostics do not trigger claim-DAG writes.

## 7. FULL178 and final closure remain open

`S32.FULL178.NUMERICAL_CENSUS.V1` remains incomplete. #1728 does not set `FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=true` and does not discharge the independent numerical-production obligation.

Stage32 final closure is still governed by `FINAL-CHECK.json`. The reserved audited milestone chain remains:

- `S32.PROOF.NUMERICAL_CENSUS.V1`
- `S32.PROOF.EFFECTIVITY_DISPOSAL.V1`
- `S32.PROOF.MULTIBRANCH_LEDGER.V1`
- `S32.PROOF.INTEGRATED_SYNTHESIS.V1`
- `S32.PROOF.HOSTILE_AUDIT_RELEASE.V1`
- `S32.PROOF.STAGE32_CLOSED.V1`.

The final root must transitively consume every required milestone, and all load-bearing mathematical/adapter dependencies must have audited authority. Until that chain exists, `--final` must remain `NOT_READY_STAGE32_FINAL_CHECK`.

No Stage32 claim here authorizes Perfect Cuboid existence/nonexistence or merge by itself.
