# 24-14num-r203 — finite matched-ratio audit and interpretation

STATUS=FINITE_MATCHED_RATIO_AUDIT_COMPLETE_CI_SUCCESS
PARENT_STAGE=Stage24
TRACK_ROLE=ADDITIONAL_NUMERICAL_RESEARCH
INPUTS=24-14num-r201,24-14num-r202
PR=972
CI_RUN=31845881894
CI_CONCLUSION=SUCCESS

## Audit verdict

The r201/r202 data form an exact same-population ladder. Every directional subtotal equals its total, the 200k overlap and sharding gates were already exact, and no population/cutoff/multiplicity adapter is needed.

| `B` | `M2(B)` | `N2(B)` | `N2/M2` |
|---:|---:|---:|---:|
| 2000 | 4812 | 5 | 0.00103906899 |
| 100000 | 796698 | 89 | 0.000111711088 |
| 200000 | 1896505 | 116 | 0.0000611651567 |
| 500000 | 5899985 | 188 | 0.0000318644878 |
| 1000000 | 13817725 | 255 | 0.0000184545575 |

On these five sampled cutoffs the finite survivor ratio strictly decreases. From 100k to 1m:

- `M2` grows by about `17.34`;
- `N2` grows by about `2.87`;
- `N2/M2` decreases by about `6.05`;
- the decade effective exponents are approximately `1.239` for `M2`, `0.457` for `N2`, and `-0.782` for the ratio.

These are finite effective slopes, not asymptotic exponents.

## Directional audit at one million

```text
direction       a          b          c
M2        4592536    5816786    3408403
N2             98        101         56
N2/M2   2.1339e-5  1.7364e-5  1.6430e-5
```

The directional survivor rates are not equal at this cutoff; the observed order is `a>b>c`. The maximum/minimum spread is only about `1.30`, so this is a refinement signal, not evidence of different directional exponents or limits.

## Interpretation boundary

The exact finite observations are compatible with strong thinning, and they agree qualitatively with the independently proved Stage24 ratio tending to zero once the source asymptotic and target upper bound are used. They do not identify the true order of `N2`, prove an intrinsic half-power law, supply an unbounded family, or turn finite `N3=0` into nonexistence.

## Additional-computation decision

One million is sufficient for the present numerical lane. No 2m-or-higher computation is required now and none is launched by r203. Reopen numerical scaling only if a later Stage24 checkpoint presents specific competing laws that the larger window could distinguish, or requires a targeted test of directional stabilization.

```text
R203_POPULATION_MATCH=EXACT
R203_FINITE_RATIO_STRICTLY_DECREASING_ON_SAMPLED_LADDER=true
R203_TRUE_ASYMPTOTIC_EXPONENT_IDENTIFIED=false
R203_DIRECTIONAL_LIMIT_IDENTIFIED=false
R203_ADDITIONAL_COMPUTATION_REQUIRED=false
R203_AUTOMATIC_COMPUTATION=false
R203_ASYMPTOTIC_CLAIM=false
R203_PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
R203_CI_STATUS=SUCCESS
R203_CI_RUN=31845881894
```
