# Stage27-19-r5at-r5av — fresh hostile audit for PR #1072

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
CI_AUDIT=PASS
INTEGRATION_AUDIT=PENDING_MAIN_SYNC

AUDIT_PR=1072
AUDITED_CONTENT_COMMIT=34c24f3a61176f652a0f35b84d9c74c351879270
DEDICATED_CI_RUN=32013624871
DEDICATED_CI_CONCLUSION=success

R5AT_MATHEMATICS=PASS
R5AU_MATHEMATICS=PASS
R5AV_MATHEMATICS=PASS

FIXED_R_KAPPA_ENTROPY_COLLAPSE_PROVED=true
FIXED_R_DYADIC_WEIGHTED_HOST_PROVED=true
HYPERBOLIC_BOUNDARY_IS_CURRENT_PRIMARY_BARRIER=true
SQRT_BOUNDARY_MODULUS_SAVING_PROVED=false
FIXED_R_OUTER_SUPPORT_FIXED_POWER_BOUND_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false

CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=false
FRESH_REAUDIT_REQUIRED=false
NEXT_DERIVED_ROUTE=27-19-r5aw
NEXT_BATCH=Stage27-19-r5-main-batch
NEXT_TARGET=BOUNDARY_FACTORIZATION_OR_FIXED_R_OUTER_SUPPORT_COUNT
```

## Hostile audit findings

1. **Fixed-R kappa compression — PASS.** The exact physical-height factorization implies `kappa | R`. Therefore, at fixed physical diagonal `R`, admissible squarefree kernels lie among the divisors of `R` and contribute only `tau(R)=B^o(1)` choices. Combined with the audited double-Pell completion bound, fixed outer data plus fixed `R` have only `B^o(1)` residual completions.

2. **Fixed-R dyadic host — PASS.** The repaired fixed-modulus estimate is used with the correct `(X*k)^eps` prefactor before Stage19 specialization. With `X_R=R/(delta*C)` and actual `kappa | R`, the dyadic host is

   `T_R <<_eps R^eps (X_R/K + sqrt(X_R))`.

   The earlier varying-modulus `K` entropy is therefore removed at fixed `R`, while the `1/K` density gain survives.

3. **Coefficient-cell accumulation — PASS.** Grouping by `t=delta*c0*cs*cn` with multiplicity `d_4(t)` gives the main contribution `(R/K) sum_{t<=R} d_4(t)/t` and boundary contribution `sqrt(R) sum_{t<=R} d_4(t)/sqrt(t)`. This yields

   `T_R^(all cells)(kappa~K) <<_eps R^eps (R/K + R)`.

4. **Barrier identification — PASS.** The active obstruction is no longer varying-modulus entropy. The surviving `R` term comes from the accumulated hyperbolic square-root boundary (equivalently, the still-uncontrolled actual fixed-R outer support). A successor must either gain modulus saving on this boundary or prove a fixed-power bound for the actual fixed-R outer support.

5. **Scope firewall — PASS.** No square-root boundary saving, fixed-R outer-support fixed-power estimate, global strict sub-square-root upper bound, new `mu<1/2`, or true `N2` exponent is claimed. Checkpoint50 remains blocked.

6. **Lifecycle — PASS, pending merge integration.** The audited mathematical content is exactly commit `34c24f3a61176f652a0f35b84d9c74c351879270`; dedicated workflow run `32013624871` completed successfully. The PR has since become stale against moving `main`, so synchronization is an integration step only and does not invalidate the mathematical audit. No fresh mathematical re-audit is required unless the mathematical content changes during synchronization.

```text
AUDIT_STATUS=PASS
STATUS=AUDITED_PASS_PENDING_MERGE
STOP_REASON=AWAIT_MAIN_SYNC_AND_MERGE;_DO_NOT_START_R5AW
```
