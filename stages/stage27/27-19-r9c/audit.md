# Stage27-19 r9 hostile audit

```text
AUDIT_VERDICT=PASS
AUDITED_PR=1263
AUDITED_SUBMISSION_HEAD=cd869d0a8589c3dcef0aef8b93659a5ca9556805
SAUNDERSON_SPACE_DIAGONAL_IDENTITY_AUDIT=PASS
EUCLID_SUBSTITUTION_DEGREE8_MODEL_AUDIT=PASS
SQUAREFREE_AUDIT=PASS
GENUS3_AUDIT=PASS
FALTINGS_FIXED_CURVE_FINITE_RATIONAL_POINTS_AUDIT=PASS
THICK_FAMILY_NO_GO_AUDIT=PASS
ISOLATED_POINTS_NOT_EXCLUDED_AUDIT=PASS
PERFECT_CUBOID_NONEXISTENCE_CLAIM_AUDIT=PASS_FALSE
R9_ROUTE_ARBITRATION_AUDIT=PASS
REPAIR_REQUIRED=false
SUBMITTED_HEAD_CI=NOT_CONFIGURED
MERGE_ALLOWED=true
ADVANCE_TO_CHECKPOINT50=false
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
NEXT_ACTION=TARGETED_EXTERNAL_LOWER_CONSTRUCTION_SEARCH
```

Independent algebra verifies

`A^2+B^2+C^2 = w^2(w^4+16u^2v^2)`

under `u^2+v^2=w^2`, and primitive Euclid substitution yields exactly

`r^8+68r^6s^2-122r^4s^4+68r^2s^6+s^8`.

The univariate degree-eight polynomial has gcd 1 with its derivative, hence the hyperelliptic model is smooth of genus 3. Faltings therefore gives finiteness of rational points on this fixed curve. This is sufficient to rule out the polynomially thick Saunderson Stage19 lower-family mechanism, but it does not rule out isolated rational points/perfect-cuboid candidates.

The r9c arbitration is therefore correct: do not manufacture r9d from the same exhausted repo-native construction gates; the useful next move is genuinely new external construction evidence or a new cross-divisibility identity.
