# Stage14-4dl — pairwise correlation localization versus connected triple branch

## Status

`COMPLETE_PAIRWISE_CORRELATION_COEFFICIENT_LOCALIZATION`

Consumes merged `Stage14-4dk`, merged `Stage14-s7-53`, merged `Stage14-X15`, and current latest-main context.

The entering theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged s7-53 gives the exact split

```text
E[W_+W_-W_k]
 = mu_+mu_-mu_k
 + mu_k Gamma_{+-}
 + mu_- Gamma_{+k}
 + mu_+ Gamma_{-k}
 + Kappa_3,
```

where `Gamma_ij=E X_i X_j` and `Kappa_3=E X_+X_-X_k`. Stage14-4dk has already restricted possible three-projection square-root saturation to near-maximal, interior-dense full-conductor cells.

## 1. Normalize the pairwise branches

On every surviving interior cell define

```text
V_j=mu_j(1-mu_j),
r_ij = |Gamma_ij| / sqrt(V_i V_j),
```

with `r_ij=0` when `V_iV_j=0`. By Cauchy--Schwarz,

```text
0 <= r_ij <= 1.
```

No new arithmetic weight is introduced; this only stratafies the already-separated pairwise branch by how close it is to the variance envelope.

## 2. Fixed-power correlation deficit is strict sub-square-root

Fix `delta>0`. On any pairwise stratum with

```text
r_ij <= B^(-delta+o(1)),
```

one has

```text
|Gamma_ij|
 <= B^(-delta+o(1)) sqrt(V_iV_j)
 <= B^(-delta+o(1)).
```

Since the ambient charged-once cell mass is at most `B^(1/2+o(1))`, the corresponding pairwise contribution is

```text
<< B^(1/2-delta+o(1)).
```

Therefore a pairwise covariance branch can contribute at square-root scale only if for at least one pair

```text
r_ij = B^(-o(1)).
```

Equivalently, square-root pairwise saturation requires fixed-power near-saturation of the Cauchy--Schwarz correlation envelope.

## 3. Logical branch split after localization

The surviving signed obstruction now separates into

```text
PAIRWISE_NEAR_MAX_BRANCH:
  for at least one ij in {+-,+k,-k},
  r_ij = B^(-o(1));

CONNECTED_TRIPLE_BRANCH:
  all pairwise r_ij are fixed-power small,
  while |Kappa_3| may still be B^(-o(1)).
```

The positive principal branch remains the near-maximal occupancy receiver already isolated in 4dj/4dk.

This is a deterministic localization only. It does not assert that a near-maximal pairwise correlation actually occurs, and it does not turn pairwise and connected-triple branches into multiplicable savings.

## 4. Why no H is opened

The pairwise near-max branch is still expressible in the existing two-projection physical coordinates. Before any theorem audit, the next internal task is to push each of the three pairs `(+,-)`, `(+ ,k)`, `(-,k)` back through the exact mixed-root / reciprocal / full-conductor finite-fiber maps and test whether near-maximal correlation forces an exact common factor, deterministic selector, or finite-fiber collapse.

The connected triple branch remains genuinely three-way and is not modified by this stage.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DL=COMPLETE_PAIRWISE_CORRELATION_COEFFICIENT_LOCALIZATION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MERGED_S7_53_CUMULANT_SPLIT_IMPORTED=true
PAIRWISE_CORRELATION_COEFFICIENT_DEFINED=true
PAIRWISE_FIXED_POWER_CORRELATION_DEFICIT_STRICT_SUBSQRT=true
PAIRWISE_SQRT_SATURATION_REQUIRES_RIJ=Bo0=true
CONNECTED_TRIPLE_BRANCH_RETAINED=true
PRINCIPAL_NEAR_MAX_BRANCH_RETAINED=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

Pairwise receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanNearMaxPairwiseCorrelationPhysicalIncidence
```

Connected receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanConnectedThreeProjectionCumulant
```

Next: `Stage14-4dm`.
