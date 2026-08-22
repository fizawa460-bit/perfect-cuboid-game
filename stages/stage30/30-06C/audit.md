# Stage30-06C — hostile audit of exact semilinear/cocycle certificate

```text
STAGE=30-06C
AUDITED_PR=1333
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPRO_STATE_PIN_REPAIR
```

## Scope

This audit consumes the external Codex verification for the already-audited Stage30-06 mathematical objects. It grants credit only to the finite exact certificate required by 30-06C. It does not perform Stage30-07 arithmetic-defect transport and does not discharge `R29-KUM5`.

## Independent audit findings

The submitted verifier is materially independent of the Stage30-06 generator checker. It reconstructs the relevant objects rather than importing prior booleans:

```text
SL2(Z/4) order = 48
PSL2(Z/4) order = 24
Task-A modular ID coverage = complete
endpoint projective group order = 24
all modular/end-point multiplication pairs checked = 24*24 = 576
```

It independently derives the source action from the diagonal Testa--Stoll `X(8) x X(8)` quotient, checks the frozen source-derived generators exactly, verifies preservation of the cuboid quadratic ideal for every generated endpoint element, and checks the full multiplication correspondence.

The exact residual data agree with the audited Stage30-06 specification:

```text
V_mod={g04,g06,g12,g14}
endpoint/sign-deck intersection = exactly V_mod

g04 -> identity
g06 -> negate {a1,a3,b2}
g12 -> negate {a2,a3,b1}
g14 -> negate {a1,a2,b1,b2}
```

The Galois action is exhaustively checked:

```text
theta(g)=D4*g*D4^-1
theta(S)=S
theta(T)=T^-1
theta fixes V_mod pointwise
```

The common-model coordinate cocycle remains

```text
c_sigma=delta_a3
c_sigma*sigma(c_sigma)=1
```

and the full semilinear identity

```text
sigma(alpha_hat(g))
 = c_sigma * alpha_hat(theta(g)) * c_sigma^-1
```

passes for all 24 residual modular elements with

```text
FAILED_ELEMENT_COUNT=0.
```

The certificate is deterministic and the verifier fails closed on wrong IDs, group order, duplicated endpoint representatives, multiplication mismatches, wrong V4 intersection/sign patterns, wrong theta, cocycle failure, any semilinear failure, stored-certificate mismatch, result-block mismatch, and manifest hash mismatch.

## Bounded reproducibility-state repair

The submitted reproduction manifest SHA-pinned `stages/stage30/controller.json`. That controller is an execution-state file and necessarily changes when this audit consumes the external result and advances Stage30 from `WAITING_EXTERNAL_CODEX_RESULT_C` to `30-07`.

Without a bounded repair, the act of recording a successful audit would immediately invalidate the manifest on the same PR.

Audit therefore performs the minimal state-pin repair:

```text
controller -> V14 audited state
repro-manifest controller SHA -> V14 audited controller content
```

No mathematical input, verifier algorithm, certificate row, endpoint representative, theta value, sign-deck pattern, cocycle value or semilinear PASS/FAIL value was changed.

The 30-06C reproduction certificate is therefore pinned to the audited PR state. Later controller advances are execution-state changes; historical reproduction should use the audited 30-06C commit/state rather than infer new mathematical input from future controller edits.

## Scope firewalls

The following remain untouched:

```text
c_sigma != kappa
V_mod != K8
K8_DEFECT_CLASSIFICATION_EXECUTED=false
DEFECT_ELIMINATION_COUNT=0
R29_KUM5_DISCHARGED=false
NEW_THEOREM_ASSUMED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

The next mathematical step is Stage30-07, which may use this audited all-24 semilinear certificate to transport/classify the eight already-audited marked `K8` defect states. It may not infer defect elimination merely from the 30-06C certificate.

## Final state

```text
SOURCE_DERIVED_DIAGONAL_LIFTS_VERIFIED=true
MODULAR_GROUP_ORDER=24
ENDPOINT_PROJECTIVE_GROUP_ORDER=24
MODULAR_ID_COVERAGE_COMPLETE=true
THETA_ALL24_VERIFIED=true
THETA_FIXES_V_MOD_POINTWISE=true
V4_SIGN_DECK_INTERSECTION_VERIFIED=true
C_SIGMA=delta_a3
C_SIGMA_COCYCLE_VERIFIED=true
SEMILINEAR_ALL24_VERIFIED=true
FAILED_ELEMENT_COUNT=0
EXACT_ARITHMETIC_ONLY=true

AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPRO_STATE_PIN_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
WAITING_EXTERNAL_CODEX_RESULT_C=false
NEXT_ITEM=30-07_CHATGPT_EIGHT_K8_DEFECT_TRANSPORT_CLASSIFICATION
NEXT_EXPECTED_COMMAND=Stage30-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
