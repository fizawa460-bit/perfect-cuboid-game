# Stage27-19-r5ah-r5ai final hostile audit

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
DEDICATED_CI_AUDIT=PASS
LIFECYCLE_AUDIT=PASS_AFTER_SUCCESSOR_REGISTRATION

PR=1054
PR_STATE=MERGED
MERGE_COMMIT=38dd56bc3fdcc6830f39340f00bb7bcfc4ad66f9

REPOSITORY_WIDE_PR_CHECK_NOTE=HISTORICAL_STAGE27_VERIFIERS_HAD_STALE_LIVE_LIFECYCLE_ASSERTS
HISTORICAL_VERIFIER_REPAIR_SCOPE=LIFECYCLE_ASSERTIONS_ONLY
HISTORICAL_MATHEMATICAL_ASSERTIONS_CHANGED=false

CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false

EXACT_PRIMITIVE_SCALE_FACTORIZATION_PROVED=true
EXACT_PHYSICAL_DIAGONAL_PRODUCT_PROVED=true
HIDDEN_GAMMA_BRANCH_CLOSED=true
THRESHOLD_CANCELLATION_DICHOTOMY_PROVED=true

STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false

AUDIT_CLOSE_R5AH_R5AI=true
NEXT_DERIVED_ROUTE=27-19-r5aj
```

## Mathematical audit

The exact primitive-scale identity

\[
\Gamma=2\delta\varepsilon
\gcd(m,r)\gcd(m,s_0)\gcd(r,n_0)
\]

is consistent with the primitive slope coprimalities and the 2-adic parity split. The three cross-gcd channels are pairwise coprime and their square divisibilities into `p+q` and `J` are valid.

On a Stage19 survivor, writing

\[
p+q=\kappa c^2,\qquad J=\kappa w^2,
\]

the legal cross-gcd cancellation is absorbed into

\[
c=c_0c',\qquad w=c_sc_nw',
\]

and the physical space diagonal is exactly

\[
R=(h/\varepsilon)\kappa w'c'.
\]

The r5ai threshold dichotomy is then immediate from the positive integer residual factor `L=w'c'`.

No strict sub-square-root upper bound, new exponent below `1/2`, or true asymptotic exponent is inferred.

## CI/lifecycle note

The dedicated `Stage27-19-r5ah exact primitive scale` workflow succeeded on the r5ah-r5ai branch. Some repository-wide historical Stage27 checks failed because their verifiers asserted that old routes must still be in their former `PENDING` lifecycle state, even though those routes had already been audited and merged. Those failures are lifecycle-verifier debt, not failures of the r5ah-r5ai mathematical assertions.

The successor r5aj-r5ak branch records this final audit, closes the r5ah route contract, synchronizes the Stage27 controller, and updates only stale historical lifecycle assertions while preserving their mathematical checks.
