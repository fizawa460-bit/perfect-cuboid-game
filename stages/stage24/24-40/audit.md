# Stage24-40 fresh audit

AUDIT_VERDICT=PASS
CHECKPOINT=40
PR=975

## Verdict

The narrow repair is accepted. The previous fresh audit rejected exactly one step: summing the per-fixed-curve `B^(2/5+o(1))` estimate over a `B`-dependent moving family without a uniform implied constant / uniform `o(1)`, and then inferring a `B^(1/10-o(1))` proliferation threshold.

The repaired checkpoint removes that extrapolation everywhere material:

- no live `N_curves(B) << K(B) B^(2/5+o(1))` claim remains for `K(B)` varying with `B`;
- no `B^(1/10-o(1))` proliferation conclusion remains;
- the missing uniform bounded-height summation is explicitly retained as part of the moving-family gate.

The substantive checkpoint40 conclusions accepted in the first audit remain valid:

- Stage14-4ak closes the full physical `M.C=4` fixed-rational-curve square-root mechanism;
- every individual fixed physical rational curve therefore has `M.C>=5` and exponent at most `2/5`;
- every genuinely fixed finite collection is strict sub-square-root;
- Stage14-4dj confines any possible square-root saturation to `omega(c)=B^(-o(1))` near-maximal occupancy cells;
- Q06 / Stage15 retain a genuine moving genus-one/Jacobi first-small-point / transverse-incidence / uniform-family gate;
- the same local squareclass tensor remains logarithmic even under hypothetical polynomial prime windows;
- the centered character/dispersion route still has no certified `kappa<1`;
- finite census data remain diagnostic only.

No whole-family strict sub-square-root theorem is obtained. The strongest certified global numerator upper bound remains

`N2(B) <<_epsilon B^(1/2+epsilon)`.

The half-power exponent is not promoted to a true or intrinsic exponent.

```text
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_VERDICT=PASS
AUDIT_VERDICT=PASS
FIXED_M4_SQRT_MECHANISM_ELIMINATED_ACCEPTED=true
FIXED_CURVE_SINGLE_EXPONENT_2_5_ACCEPTED=true
FIXED_FINITE_COLLECTION_SUBSQRT_ACCEPTED=true
PRINCIPAL_DENSITY_LOCALIZATION_ACCEPTED=true
Q06_MOVING_FAMILY_BOUNDARY_ACCEPTED=true
GROWING_MODULUS_RECHECK_ACCEPTED=true
NONUNIFORM_KB_SUMMATION_REMOVED=true
B_ONE_TENTH_PROLIFERATION_CLAIM=false
GROWING_CURVE_FAMILY_UNIFORM_SUMMATION_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_PROVED=false
CURRENT_WHOLE_FAMILY_UPPER=N2(B)<<_epsilon B^(1/2+epsilon)
HALF_POWER_INTRINSIC_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=50
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
```
