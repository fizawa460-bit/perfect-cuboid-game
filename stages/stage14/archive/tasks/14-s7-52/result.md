# Stage14-s7-52 — interior-variance reduction for dense principal cells

## Status

`COMPLETE_DENSE_CELL_VARIANCE_COVARIANCE_BOUNDARY_PEEL`

Consumes merged `Stage14-s7-51`, merged `Stage14-sH50`, merged `Stage14-X15`, and latest main.

The whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Stage14-s7-51 already removes cells with a fixed-power lower-tail deficit

```text
mu_+ mu_- mu_k < B^(-delta).
```

Stage14-s7-52 now peels the complementary **boundary-variance** cells on the covariance side.

For each conditioning cell `Omega`, let

```text
W_+, W_-, W_k in {0,1},
mu_j=E_Omega W_j,
V_j=mu_j(1-mu_j).
```

Write centered weights

```text
X_j=W_j-mu_j.
```

Then exactly

```text
E X_j^2 = V_j.
```

Pairwise covariance satisfies Cauchy--Schwarz:

```text
|E(X_i X_j)| <= sqrt(V_i V_j).
```

Since `|X_j|<=1`, the genuine triple covariance satisfies, for every pair `(i,j)`,

```text
|E(X_+ X_- X_k)| <= sqrt(V_i V_j).
```

Hence if any one variance has fixed-power loss

```text
V_j <= B^(-delta),
```

then every covariance term containing `X_j` is at most `B^(-delta/2)` times the ambient cell mass.  The sole pairwise covariance not containing `X_j` is multiplied in the exact triple-centering formula by `mu_j`; if `V_j<=B^-delta` and the cell survived s7-51, then either

```text
mu_j <= B^(-delta+o(1))
```

which was already removed by s7-51, or

```text
1-mu_j <= B^(-delta+o(1)),
mu_j=1-B^(-delta+o(1)).
```

In the latter case the `j`-selector is deterministic up to a fixed-power exceptional set.  Replacing `W_j` by `1` changes the physical incidence by at most `B^(1/2-delta+o(1))`; after this replacement the exact three-weight problem reduces to the corresponding two-weight physical intersection.  Therefore boundary-variance cells do not create a new three-way square-root obstruction.

Consequently any genuinely three-projection square-root saturation sequence may be restricted to

```text
boxed:
mu_j = B^(-o(1)),
1-mu_j = B^(-o(1)),
V_j = B^(-o(1))
for j in {+,-,k}.
```

Equivalently all three marginals are fixed-power interior: none is polynomially sparse and none is polynomially almost deterministic.

This is a deterministic contraction only.  It does not prove a fixed whole-family delta because `B^{-o(1)}` may still tend to zero and the surviving interior covariance can remain main-term scale.

The new receiver is

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanThreeProjection
ConditionalJointDensityAndMainTermScaleSignedCovariance.
```

The next exact task is to separate **pairwise saturation** from genuinely **triple-connected saturation**.  Stage14-s7-53 should subtract/condition on the three pairwise intersections and isolate the connected three-way cumulant.  A new H is premature until that deterministic cumulant reduction is completed.

## Boundary

```text
STAGE14_S7_52=COMPLETE_DENSE_CELL_VARIANCE_COVARIANCE_BOUNDARY_PEEL
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_51_DENSE_LOWER_TAIL_IMPORTED=true
PAIRWISE_COVARIANCE_VARIANCE_BOUND_PROVED=true
TRIPLE_COVARIANCE_VARIANCE_BOUND_PROVED=true
FIXED_POWER_BOUNDARY_VARIANCE_THREE_WAY_OBSTRUCTION_REMOVED=true
SQRT_THREE_PROJECTION_SATURATION_REQUIRES_ALL_MARGINALS_INTERIOR=true
SQRT_SATURATION_REQUIRES_MU_J=Bo0_NOT_FIXED_POWER_ZERO=true
SQRT_SATURATION_REQUIRES_ONE_MINUS_MU_J=Bo0_NOT_FIXED_POWER_ZERO=true
S7_52_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanThreeProjectionConditionalJointDensityAndMainTermScaleSignedCovariance
NEXT=Stage14-s7-53
```
