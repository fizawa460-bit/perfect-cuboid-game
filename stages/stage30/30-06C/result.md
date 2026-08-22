# Stage30-06C — exact semilinear/cocycle verification result

## Verdict

The frozen source-derived action passes the independent exact verification.
The verifier reconstructs `SL2(Z/4)` and its quotient by `±I`, derives the
endpoint generators through the diagonal Testa--Stoll `X(8) x X(8)` quotient,
and establishes a bijection between all 24 Task-A modular IDs and 24 distinct
projective endpoint representatives.

All 576 multiplication pairs preserve that correspondence.  Every endpoint
representative preserves the cuboid quadratic ideal.  The exact sign-deck
intersection is precisely

```text
{g04,g06,g12,g14}=j(V_mod),
```

with the four frozen sign patterns.  Conjugation by `D4` gives the frozen
`theta` on all 24 elements and fixes `V_mod` pointwise.  Finally,

```text
c_sigma=delta_a3,
c_sigma*sigma(c_sigma)=1,
sigma(alpha_hat(g))=c_sigma*alpha_hat(theta(g))*c_sigma^-1
```

holds in `PGL7(Q(i))` for every one of the 24 elements.  Arithmetic uses only
integers, rational numbers, and exact pairs representing rational Gaussian
numbers; no floating-point computation is present.

This is external computational input only.  It receives no Stage30
mathematical credit until a later hostile audit consumes it.  No `K8` defect
was classified or eliminated, and no endpoint existence or nonexistence claim
is made.

## Reproduction

From the repository root:

```text
python stages/stage30/30-06C/verify_semilinear_cocycle.py
```

The default verifier independently reconstructs the certificate, requires
exact equality with the checked-in JSON, checks the result block, and verifies
all source/output SHA-256 entries in the reproduction manifest.  Any mismatch
terminates with a nonzero exit status.

## Required result block

```text
CODEX_TASK=C_30_06C
INPUT_SOURCE_LOCK_COMPLETE=true
EXACT_ARITHMETIC_ONLY=true
SOURCE_DERIVED_DIAGONAL_LIFTS_VERIFIED=true
MODULAR_GROUP_ORDER=24
MODULAR_ID_COVERAGE_COMPLETE=true
THETA_ALL24_VERIFIED=true
THETA_FIXES_V_MOD_POINTWISE=true
ENDPOINT_PROJECTIVE_GROUP_ORDER=24
V4_SIGN_DECK_INTERSECTION_VERIFIED=true
C_SIGMA=delta_a3
C_SIGMA_COCYCLE_VERIFIED=true
SEMILINEAR_ALL24_VERIFIED=true
FAILED_ELEMENT_COUNT=0
CHECKER_PRESENT=true
CHECKER_PASS=true
K8_DEFECT_CLASSIFICATION_EXECUTED=false
DEFECT_ELIMINATION_COUNT=0
NEW_THEOREM_ASSUMED=false
R29_KUM5_DISCHARGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Compatibility fields required by the amended handoff contract:

```text
GALOIS_ACTION_CHECK=PASS
COCYCLE_IDENTITY_CHECK=PASS
SEMILINEAR_COMPATIBILITY_CHECK=PASS
CANDIDATE_ADAPTER_COUNT=1
CHECKED_CANDIDATE_COUNT=1
UNRESOLVED_ASSUMPTION_COUNT=0
```
