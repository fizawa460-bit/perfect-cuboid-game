# Stage14-s7-53 — pairwise covariance / connected triple cumulant split

## Status

`COMPLETE_PAIRWISE_VS_CONNECTED_TRIPLE_CUMULANT_REDUCTION`

Consumes merged `Stage14-s7-52`, merged `Stage14-s7-51`, merged `Stage14-sH50`, merged `Stage14-X15`, and latest-main compatibility through merged `Stage14-4dj` where available. No unmerged theorem is used.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root saving is claimed here.

---

## 1. Exact cellwise cumulant identity

On a full-conductor interior dense conditioning cell `Omega`, let

```text
W_+, W_-, W_k in {0,1},
mu_j = E_Omega W_j,
X_j = W_j-mu_j.
```

Define pairwise covariances

```text
Gamma_{+-}=E X_+ X_-,
Gamma_{+k}=E X_+ X_k,
Gamma_{-k}=E X_- X_k,
```

and the connected third cumulant

```text
Kappa_3 = E X_+ X_- X_k.
```

Then the exact identity is

```text
E[W_+W_-W_k]
 = mu_+mu_-mu_k
 + mu_k Gamma_{+-}
 + mu_- Gamma_{+k}
 + mu_+ Gamma_{-k}
 + Kappa_3.                                      (1.1)
```

This is the Möbius/cumulant decomposition of the three-weight intersection and is purely algebraic.

---

## 2. Pairwise-small strata are not genuine three-way obstructions

Fix `delta>0`. Suppose on a family of interior dense cells all three pairwise covariances satisfy

```text
|Gamma_{+-}|,
|Gamma_{+k}|,
|Gamma_{-k}| <= B^(-delta+o(1)).                  (2.1)
```

Because every `mu_j<=1`, the total pairwise contribution in (1.1) is

```text
O(B^(-delta+o(1)))
```

relative to the charged-once cell majorant. Thus at exponent `1/2` scale the only nonprincipal signed obstruction on this stratum is `Kappa_3`.

Conversely, if one pairwise covariance is not power-small, then the obstruction is already present on a two-weight marginal receiver and does not require a genuinely connected three-way theorem.

Hence square-root signed-correlation saturation splits into two disjoint logical receivers:

```text
PAIRWISE_BRANCH:
  at least one |Gamma_ij| = B^(-o(1));

CONNECTED_TRIPLE_BRANCH:
  all |Gamma_ij| = B^(-Omega(1))
  but |Kappa_3| may remain B^(-o(1)).             (2.2)
```

The stage does not assert that either branch actually saturates.

---

## 3. Interior variance constraints retained

Merged s7-52 already removes boundary-variance cells from the genuine three-way problem. Therefore on the connected-triple branch one additionally has

```text
mu_j = B^(-o(1)),
1-mu_j = B^(-o(1)),
Var(W_j)=B^(-o(1))
```

for each `j in {+,-,k}`.

Thus the connected receiver is not allowed to hide inside a nearly deterministic selector.

---

## 4. Principal-density branch retained separately

Merged s7-51 and merged 4dj-type localization show that any fixed-power deficit in the positive principal density is already strict sub-square-root. Therefore any principal square-root saturation occurs only on dense / near-maximal cells.

Stage14-s7-53 does not mix this positive principal issue with the signed covariance branches. The bookkeeping is now

```text
A. positive principal dense-cell occupancy;
B. pairwise signed covariance saturation;
C. connected third cumulant saturation.
```

A strict whole-family saving must eliminate or power-save all three surviving mechanisms.

---

## 5. Why no H is opened yet

The present reduction is still deterministic and changes the theorem target materially. Before an auxiliary theorem audit, the pairwise branch should be pushed back into the two-projection s-coordinates and checked for an exact finite-fiber / conductor / divisor reduction already available from s7-46--s7-50.

Only the connected-triple branch is a genuinely new three-weight object.

Therefore

```text
S7_53_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

---

## 6. New receivers

Pairwise branch:

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanPairwisePhysicalCovarianceSaturation
```

Connected branch:

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanConnectedThreeProjectionCumulant
```

The positive principal branch remains

```text
FullConductorNearMaximalConditionalPrincipalOccupancy
```

as already isolated by the dense-cell/mainline reductions.

---

## 7. Next

`Stage14-s7-54` should attack the pairwise branch first. For each of the three pairs `(+,-)`, `(+ ,k)`, `(-,k)`, translate the covariance back into the corresponding two-projection physical coordinate systems and determine whether one of the already-proved mixed-root / reciprocal / full-conductor finite-fiber structures removes an independent fixed-power degree of freedom.

Do not open a new H until that deterministic pairwise audit is exhausted.

---

## Stage boundary

```text
STAGE14_S7_53=COMPLETE_PAIRWISE_VS_CONNECTED_TRIPLE_CUMULANT_REDUCTION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
EXACT_THREE_WEIGHT_CUMULANT_IDENTITY_PROVED=true
PAIRWISE_COVARIANCE_BRANCH_SEPARATED=true
CONNECTED_TRIPLE_CUMULANT_BRANCH_SEPARATED=true
BOUNDARY_VARIANCE_PEEL_RETAINED=true
PRINCIPAL_DENSE_CELL_BRANCH_RETAINED=true
S7_53_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
PAIRWISE_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanPairwisePhysicalCovarianceSaturation
CONNECTED_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanConnectedThreeProjectionCumulant
NEXT=Stage14-s7-54
```
