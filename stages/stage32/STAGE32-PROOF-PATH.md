# Stage32 proof path and claim-management contract

Status: **ACTIVE MANAGEMENT LAYER — POST-#1730 Q602-V3-CONSUMED / POST-SYNC-AUDITED / FINAL-CHAIN FRONTIER**

This layer does not replace `MAIN-STATE.json`, retained certificates, leaf verifiers, hostile audits, or FINAL-CHECK. Ordinary routing authority is `stages/stage32/MAIN-STATE.json`; mathematical credit is bounded by registered immutable claim cores, exact source locks, and hostile-audit receipts.

Machine-readable files:

- `stages/stage32/proof/CLAIM-REGISTRY.json`
- `stages/stage32/proof/ACTIVE-FRONTIER.json`
- `stages/stage32/proof/LANE-ADAPTERS.json`
- `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md`
- `stages/stage32/FINAL-CHECK.json`

## 1. Stable claim / authority rule

Claim IDs use `S32.<DOMAIN>.<SEMANTIC_NAME>.V<n>`. A semantic/evidence change requires a new versioned claim/core. Audit metadata may advance on an unchanged core only from an external exact-head hostile-audit receipt. `MAIN-STATE.json` is mutable routing authority rather than immutable mathematical evidence.

Hostile-audit PASS, claim-DAG synchronization, merge-ready freshness, and merge authorization remain separate gates. No management update below grants new mathematical credit.

## 2. Audited V6 authority consumed by MAIN

The exact MAIN-scope population result remains:

- `S32.ADAPTER.EX1_V6_CARRIER_TO_MAIN_V6_CARRIER.V1` — **AUDITED**;
- `S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2` — **AUDITED**;
- promotion audit review `5147810198`, exact head `89ba026f05f9fe5344c0f0fb41fe8c2366032877`.

Thus the exact `g1-d186 / V6` integral irreducible geometric-genus-1 carrier population is empty. This does not by itself grant FULL178 completion or Stage32 closure.

## 3. Audited O210 V3 authority consumed by MAIN

The retained chain is:

- `S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1` — **AUDITED**, review `5141988194`;
- `S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3` — **AUDITED**, review `5143014619`;
- `S32.O210.EXCLUSION.V3` — **AUDITED**, review `5147304889`.

The O210 post-sync management transition received independent hostile-audit PASS in review `5149127765` at exact head `f11c8c3cb402e2ec50fccf264c0fb71f56d157f9`.

Current routing therefore retains `O210_excluded=true`; O210 is authority/provenance, not an open attack node.

## 4. Audited Q602 V3 authority synchronized, consumed, and post-sync audited

The object-level adapter remains:

- `S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1`;
- core `ed1ea5441a3b0bb876a3a8b93f272e2a16d693f1b44f0f050c13af1625c1e028`;
- hostile audit review `5149322780`, exact head `1689ed2bdfa149b5e462ce0182e7a7e7c31ee62c`.

Its object-map direction is actual Q602 realization -> underlying O210 cover. The separate theorem-credit/emptiness adapter remains:

- `S32.ADAPTER.O210_EMPTY_TO_Q602_REALIZATION_EMPTY.V1`;
- core `4dd78ed5a1917d7c953fee95bb52f1d1429e239ca90d3bf8dae26461e0611de8`;
- hostile audit review `5149462285`, exact head `6487de765b0d35e05d81018aeaff902af9b7d21a`.

The mathematical conclusion is:

- `S32.Q602.EXCLUSION.V3`;
- core `c85a76ac1ed07deec1d65269451452d33b63c3a5221134ee687e282951823067`;
- hostile audit review `5149462285`, exact head `6487de765b0d35e05d81018aeaff902af9b7d21a`.

The post-sync management transition itself received independent hostile-audit PASS in review `5149990935` at exact head `9b605ed7f44415198a0e261dc46971e5ecd3c80b`. PR #1730 was later merged as commit `733176600f99e91993d08c16aa98f09c08a1e726` without widening that mathematical scope.

Therefore the Q602 post-sync audit gate is complete. `Q602_excluded=true` remains bounded to `NO_GEOMETRICALLY_ADMISSIBLE_FIXED_TARGET_CONFIGURATION`. Formal arithmetic labels `[73,97,235]` remain retained provenance; no residue-specific arithmetic impossibility is asserted.

The remaining mathematical interface is now exactly:

`FULL178_AND_FINAL_MILESTONE_CHAIN`.

## 5. MAIN / EX routing after Q602 completion

- `MAIN`: integration/frontier coordinator. Current route is `FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS`.
- `EX1`: completed audited handoff; provenance only.
- `EX2`: old V6 actual-member branch dominated by audited V6 population emptiness; no active claim.
- `EX3`: O210/Q602 authority consumer/provenance only.
- `EX4`: Q602 marking provenance only; selected route parked.
- `EX5`: active FULL178 / receiver-breadth weapon lane. The BTVA node-support/span checkpoint is audited infrastructure, but FULL178 remains incomplete.
- `EX6`: stopped pending new endpoint input.

PR #1742 is an EX5 working surface for BC2-02. Its retained blocker says FULL178 production lacks the exact per-candidate 59-entry Picard witness / 48 exceptional-pairing support certificate needed to fire the BTVA projective-span cut. That blocker is not Stage32 MAIN mathematical credit.

## 6. Formal final-chain execution

The current Stage32 roadmap chain is:

```text
32-01-XL  complete unibranch numerical census       R29-LG2
32-02-L   rigorous effectivity certification         R29-LG2-EFF
32-03-L   multibranch-at-node carrier ledger         R29-LG2-MB
32-04-M   integrated low-genus carrier synthesis
32-05     final hostile audit
```

Current execution interpretation:

1. `32-01-XL` is primary and incomplete. FULL178 support reconstruction and independent global cuts may proceed in parallel.
2. `32-02-L` final execution waits for the complete 32-01 survivor/orbit ledger, but effectivity verifier/linear-system/decomposition/RR-vanishing preparation may proceed without claiming effectivity disposal.
3. `32-03-L` is a separate receiver and may progress independently of FULL178. It must classify multibranch normalization profiles, delta/genus corrections, exact Aut(S) quotienting, justified finite degree/intersection restrictions, finite Picard enumeration where available, and exact effectivity/carrier certificates.
4. `32-04-M` waits for 32-01/02/03 outputs.
5. MAIN must stop before self-awarding `32-05`; final hostile audit is external.

Historical path collision warning: existing `stages/stage32/32-02/` contains older local Z3/Normaliz production evidence, and existing `stages/stage32/32-03/` is the historical `e4/a32` affine-lattice closure package. Neither directory is the formal current effectivity/multibranch unit described above. Do not overwrite or reinterpret them; materialize new final-chain work under unambiguous namespaced paths.

The retained routing checkpoint is `stages/stage32/mainbatch-final-chain-reentry-20260909.json`.

## 7. Claim-DAG synchronization

On `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, follow `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and run the claim-DAG and active-frontier verifiers. Scratch-only diagnostics do not promote authority.

This reentry changes routing/audit metadata only. The V6/O210/Q602 immutable mathematical cores above remain unchanged.

## 8. FULL178 and final closure remain open

`S32.FULL178.NUMERICAL_CENSUS.V1` remains incomplete. The reserved final milestone chain remains:

- `S32.PROOF.NUMERICAL_CENSUS.V1`
- `S32.PROOF.EFFECTIVITY_DISPOSAL.V1`
- `S32.PROOF.MULTIBRANCH_LEDGER.V1`
- `S32.PROOF.INTEGRATED_SYNTHESIS.V1`
- `S32.PROOF.HOSTILE_AUDIT_RELEASE.V1`
- `S32.PROOF.STAGE32_CLOSED.V1`

Until the complete externally audited chain exists, FINAL-CHECK must remain `NOT_READY_STAGE32_FINAL_CHECK`.

No Stage32 claim here authorizes Perfect Cuboid existence/nonexistence or merge.
