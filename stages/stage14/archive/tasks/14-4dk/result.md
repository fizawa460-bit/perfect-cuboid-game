# Stage14-4dk — interior-marginal reduction inside near-maximal principal cells

## Status

`COMPLETE_NEAR_MAXIMAL_CELL_INTERIOR_VARIANCE_REDUCTION`

Consumes merged `Stage14-4dj`, merged `Stage14-s7-52`, merged `Stage14-X15`, and merged `Stage14-Work-bdX16` on latest main.

The entering theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Stage14-4dj localized possible square-root saturation to full-conductor cells whose exact physical occupancy relative to the charged-once complete-coordinate majorant satisfies

```text
omega(c)=B^(-o(1)).
```

Stage14-s7-52 independently proves the deterministic variance boundary peel for the three physical selectors.  We now intersect these two merged reductions.

## 1. Three-selector cell notation

Inside a surviving full-conductor root cell `c`, retain

```text
W_+, W_-, W_k in {0,1},
mu_j = E_c W_j,
V_j = mu_j(1-mu_j),
X_j = W_j-mu_j.
```

The X15 exact triple-centering identity is retained without taking absolute values before the decomposition.

## 2. Boundary marginals cannot support the genuine three-way obstruction

Merged s7-52 gives

```text
|E_c X_i X_j| <= sqrt(V_i V_j),
|E_c X_+ X_- X_k| <= sqrt(V_i V_j)
```

for every pair `(i,j)`.  If some `V_j <= B^(-delta)`, then every covariance containing `X_j` has a `B^(-delta/2)` loss.  The remaining pairwise term either lies in the already-removed sparse marginal case or the selector `W_j` is deterministic up to `B^(-delta+o(1))`, reducing the three-weight incidence to a two-weight intersection plus a strict-sub-square-root exceptional set.

Therefore the near-maximal cells from 4dj which can still carry a genuinely three-projection square-root obstruction must satisfy simultaneously

```text
omega(c)=B^(-o(1)),
mu_j=B^(-o(1)),
1-mu_j=B^(-o(1)),
V_j=B^(-o(1))
for j in {+,-,k}.
```

This is an exact intersection of two already-merged deterministic contractions; it is not a multiplication of two square-root coordinate counts and does not create a new power saving by itself.

## 3. Principal-density consequence

On every fixed-power boundary stratum, either

```text
omega(c) <= B^(-delta)
```

and 4dj gives exponent `1/2-delta`, or some selector variance satisfies

```text
V_j <= B^(-delta)
```

and s7-52 removes the genuinely three-way obstruction by covariance loss / deterministic-selector reduction.

Hence a square-root-saturating genuinely three-projection sequence is confined to **interior dense near-maximal cells**.  The remaining issue is no longer conductor loss, sparse principal density, or boundary variance.

## 4. Remaining connected obstruction

The surviving X15 expansion still contains three pairwise covariance terms and the genuine triple covariance.  Interior marginals do not imply these terms are small.  In particular, Cauchy--Schwarz is now only `B^o(1)` at exponent scale.

The next exact reduction is therefore to distinguish pairwise saturation from genuinely triple-connected saturation by conditioning/subtracting the three pairwise intersections and isolating the connected three-way cumulant.  This matches the independently merged s7-52 next receiver.

No new theorem family is exposed yet, so another H audit is premature.

## Boundary

```text
STAGE14_4DK=COMPLETE_NEAR_MAXIMAL_CELL_INTERIOR_VARIANCE_REDUCTION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEAR_MAXIMAL_OCCUPANCY_IMPORTED=true
INTERIOR_VARIANCE_REDUCTION_IMPORTED=true
SQRT_THREE_PROJECTION_SATURATION_REQUIRES_OMEGA=Bo0=true
SQRT_THREE_PROJECTION_SATURATION_REQUIRES_ALL_MARGINALS_INTERIOR=true
FIXED_POWER_OCCUPANCY_BOUNDARY_REMOVED=true
FIXED_POWER_VARIANCE_BOUNDARY_THREE_WAY_OBSTRUCTION_REMOVED=true
PAIRWISE_AND_TRIPLE_COVARIANCE_REMAIN_MAIN_TERM_SCALE_POSSIBLE=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

New receiver:

```text
FullConductorNearMaximalInteriorDensePrimitiveQuarterPythagoreanThreeProjectionPairwiseOrConnectedTripleCovariance
```

Next: `Stage14-4dl`.
