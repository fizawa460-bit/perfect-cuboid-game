# Stage32 proof path and claim-management contract

Status: **ACTIVE MANAGEMENT LAYER — POST-#1730 Q602-V3-CONSUMED FRONTIER**

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

## 2. Audited V6 authority consumed by MAIN

PR #1728 supplied the load-bearing V6 checkpoints.

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

The promotion audit establishes exact population identity for integral irreducible geometric-genus-1 curves in Picard class V6 on the minimal desingularization S for row `g1-d186`. Therefore Stage32 MAIN consumes the statement that this entire V6 genus-1 carrier population is empty.

This V6 result by itself does **not** grant Q602 exclusion, O210 exclusion, FULL178 completion, Stage32 closure, or Perfect Cuboid existence/nonexistence credit.

## 3. Audited O210 V3 authority synchronized and consumed

The O210 chain retained from PR #1714 is:

- `S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1` — **AUDITED**, review `5141988194`, exact head `8da8d4cd932c5c9b82dfd0c304638e866c656069`, core `78399b9797723b4134198b2f4b2dc3ed3024897b7ad128d1f0621e1e85cf8102`.
- `S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3` — **AUDITED**, review `5143014619`, exact head `280595ed892ae2ef70e049a3f722ea024452e206`, core `55505658e272ec7d60372f2d67cb93c9c007d782145f18d5ef9d2c1146582c88`.
- `S32.O210.EXCLUSION.V3` — **AUDITED**, review `5147304889`, exact head `040dfb6c7e1dc40573866bb10f62e93419121711`, core `7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824`.

PR #1730 pre-sync hostile audit review `5148641910` authorized synchronization of these unchanged audited cores into the effective active frontier. The post-sync state therefore has:

```text
S32.O210.EXCLUSION.V3                       [AUDITED_TRUE]
S32.Q602.SURVIVORS_73_97_235.V1             [AUDITED_TRUE]
S32.Q602.EXCLUSION.V3                        [AUDITED_TRUE]
S32.FULL178.NUMERICAL_CENSUS.V1              [DECLARED_GOAL / INCOMPLETE]
S32.GOAL.STAGE32_CLOSURE.V1                  [DECLARED_GOAL / BLOCKED]
```

and routing firewalls:

```text
O210_excluded=true
Q602_excluded=true
O212_plus_advance_allowed=false
FULL178_complete=false
Stage32_closed=false
```

`[73,97,235]` remains audited arithmetic provenance. O210 population emptiness does not erase those formal residue labels; it only removes the underlying geometric O210 carrier/cover population.

The O210 post-sync management transition received independent hostile-audit PASS in review `5149127765` at `f11c8c3cb402e2ec50fccf264c0fb71f56d157f9`. The later Q602 transition below consumes that established O210 authority.

## 4. Audited Q602 V3 authority synchronized and consumed

Review `5149322780` at exact head `1689ed2bdfa149b5e462ce0182e7a7e7c31ee62c` audited the total object-level forgetful adapter:

- `S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1`
- core `ed1ea5441a3b0bb876a3a8b93f272e2a16d693f1b44f0f050c13af1625c1e028`.

Its direction is actual geometrically admissible Q602 configurations -> underlying O210 carriers/covers. It forgets only the correspondence/residue decoration. No reverse object map, injectivity, or surjectivity is asserted.

Review `5149462285` at exact head `6487de765b0d35e05d81018aeaff902af9b7d21a` audited the separate emptiness-credit transport and V3 conclusion:

- `S32.ADAPTER.O210_EMPTY_TO_Q602_REALIZATION_EMPTY.V1`, core `4dd78ed5a1917d7c953fee95bb52f1d1429e239ca90d3bf8dae26461e0611de8`.
- `S32.Q602.EXCLUSION.V3`, core `c85a76ac1ed07deec1d65269451452d33b63c3a5221134ee687e282951823067`.

The theorem-credit bridge is `S32.O210.COVER -> S32.Q602.ARITHMETIC`: a total map to an empty population forces the domain empty. It does not reverse the object map. The effective active frontier registers both adapters as AUDITED supporting claims and replaces Q602 V1 with the unchanged AUDITED V3 core. Q602 V2 remains retained historical mathematics and **DO_NOT_REGISTER_AS_ACTIVE** because its dependency variance is incompatible with the current DAG contract.

`Q602_excluded=true` means no geometrically admissible configuration in the exact fixed target. Formal arithmetic labels `[73,97,235]` remain unchanged; no independent residue-specific arithmetic contradiction is claimed.

The new **post-sync hostile re-audit remains PENDING**. Consuming the existing exact-core receipts is not a self-audit of this management change. The next route is `HOSTILE_REAUDIT_Q602_V3_MAIN_SYNC_THEN_FULL178_AND_FINAL_SYNTHESIS`; the remaining mathematical interface is `FULL178_AND_FINAL_MILESTONE_CHAIN`.

Historical preflight artifacts and their verifiers remain byte-unchanged. CI replays their pre-sync assertions in a separate checkout of the exact audited head `6487de765b0d35e05d81018aeaff902af9b7d21a`. Those outputs describe historical state only. Current-head authority, immutable cores, source locks, routing, and firewalls are checked separately by `proof/verify_stage32_q602_sync.py` and the active-frontier verifier. A historical PASS cannot substitute for the live check.

## 5. MAIN / EX routing after Q602 sync


- `MAIN`: consumes audited V6 population nonexistence and audited O210 exclusion V3. It also consumes audited Q602 V3 geometric-realization exclusion. Next is post-sync re-audit, FULL178, and final synthesis.
- `EX1`: `COMPLETED_AUDITED_HANDOFF`. No active attack; retained as authority/provenance.
- `EX2`: `DOMINATED_BY_AUDITED_V6_NONEXISTENCE`. Actual-member/genus-1 reconstruction is no longer load-bearing; re-entry requires explicit remap.
- `EX3`: O210 terminal and exact EX3->MAIN adapter are audited and consumed into MAIN O210 V3. EX3 remains attached as O210/Q602 authority consumer and provenance; no active Q602 attack remains.
- `EX4`: absolute-marking route is parked for the selected path; remains attached as Q602 authority consumer and provenance; no active Q602 attack remains.
- `EX5`: remains active on FULL178 / receiver breadth; O210 closure does not complete the numerical census.
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

`S32.FULL178.NUMERICAL_CENSUS.V1` remains incomplete. Audited V6, O210, and Q602 decisions do not set `FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=true` and do not discharge the independent numerical-production obligation.

Stage32 final closure is still governed by `FINAL-CHECK.json`. The reserved audited milestone chain remains:

- `S32.PROOF.NUMERICAL_CENSUS.V1`
- `S32.PROOF.EFFECTIVITY_DISPOSAL.V1`
- `S32.PROOF.MULTIBRANCH_LEDGER.V1`
- `S32.PROOF.INTEGRATED_SYNTHESIS.V1`
- `S32.PROOF.HOSTILE_AUDIT_RELEASE.V1`
- `S32.PROOF.STAGE32_CLOSED.V1`.

The final root must transitively consume every required milestone, and all load-bearing mathematical/adapter dependencies must have audited authority. Until that chain exists, `--final` must remain `NOT_READY_STAGE32_FINAL_CHECK`.

No Stage32 claim here authorizes Perfect Cuboid existence/nonexistence or merge by itself.

