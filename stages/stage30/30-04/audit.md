# Stage30-04 — hostile audit

```text
AUDITED_PR=1330
AUDITED_SUBMISSION_HEAD=48cefa688f435512c636d60f961f45c07275f756
AUDIT_VERDICT=PASS_AFTER_BOUNDED_VERIFIER_AND_STATE_PRESERVATION_REPAIR
```

## Fresh state

PR #1330 is based exactly on merged main `f7b22bc4afc9caadb74f0f97067faa973d4272c6`, the merge commit of audited PR #1329. The submission targets the audited next leaf `30-04_CHATGPT_QI_FINITE_EQUIVARIANT_IDENTIFICATION`.

## Independent finite reconstruction

The audit independently rebuilt the modular finite group from matrices over `Z/4` and recovered:

```text
|SL2(Z/4)|=48
|PSL2(Z/4)|=24
V_mod=[g04,g06,g12,g14]
Omega_mod_3=[g06,g12,g14] -> [v0,v1,v2]
```

The four order-6 complements, in the exact audited Task-A label order, are:

```text
h0={g00,g04,g09,g15,g18,g21}
h1={g00,g04,g10,g13,g19,g20}
h2={g01,g04,g10,g15,g17,g23}
h3={g03,g04,g11,g13,g18,g23}
```

Thus Stage30-04 does not silently relabel the audited Task-A modular action objects.

Using the audited arrangement generators

```text
s_arr=(A1 A2)(B1 B2)
t_arr=(A1 A2 A3 C)(B1 B3)
```

and the reconstructed modular `4+3` action, all `4!*3!=144` bijection pairs were independently enumerated. Exactly 24 satisfy simultaneous equivariance under the same induced group identification:

```text
SURVIVING_EQUIVARIANT_IDENTIFICATION_COUNT=24
C_IMAGE_MULTIPLICITIES=h0:6,h1:6,h2:6,h3:6
```

The stored 24 candidates match the independently reconstructed set exactly.

## Generator-convention representative

The submission identifies `qicand-22` with

```text
A1,A2,A3,C -> h3,h2,h0,h1
B1,B2,B3   -> v0,v1,v2
```

Fresh audit verifies that transport by this bijection sends the two frozen arrangement generators exactly to the modular generators:

```text
s_arr -> S_mod
 t_arr -> T_mod
```

This claim was true, but the submitted verifier only checked the candidate ID and not the semantic generator transport. The verifier was strengthened on this PR to check both the Task-A label convention and the actual generator transport.

## Mathematical scope

The 24 survivors are finite-action relabellings. They do not constitute 24 certified cuboid/modular geometric adapters, and the generator-matched representative is only a convention-level witness.

Therefore the authoritative scope remains:

```text
FINITE_ACTION_EQUIVARIANCE=VERIFIED
SOURCE_GEOMETRIC_QI_ADAPTER_PROVED=false
QI_EQUIVARIANCE_VERIFIED=false
Q_GALOIS_COCYCLE_VERIFIED=false
Q_DESCENT_CREDIT=false
DEFECT_ELIMINATION_COUNT=0
R29_KUM5_DISCHARGED=false
```

The next load-bearing wall is exactly Stage30-05: supply a source-faithful common cuboid/moduli geometric or moduli anchor over `Q(i)` that can select/interpret the finite action identification.

## Recursive reclassification

```text
L30-QI-FINITE-EQUIVARIANT-SEARCH
  -> CLASS1_DISCHARGED_EXHAUSTIVE_24_CANDIDATES

L30-COMMON-GEOMETRIC_OR_MODULI-ANCHOR
  -> CLASS2_30-05

NEW_CLASS3_THEOREM_GATE
  -> NONE_EXPOSED_BY_30_04

HIDDEN_CLASS1_PENDING_COUNT=0
```

## Bounded controller-state preservation repair

The submitted V8 controller correctly recorded the 30-04 result but pruned several policy fields that had been explicitly audited at 30-03, including the final target and the inactive historical Codex tasks. This did not alter the mathematics, but it weakened the research-OS state.

Controller V9 restores the audited ownership/amendment provenance, active substage order, sole-future-Codex policy, inactive historical Task B/D flags, prompt-generation metadata, and final target while advancing the current item to 30-05.

## Final state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_BOUNDED_VERIFIER_AND_STATE_PRESERVATION_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=30-05_COMMON_QI_GEOMETRIC_OR_MODULI_ANCHOR
NEXT_EXPECTED_COMMAND=Stage30-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
