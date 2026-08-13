# Stage14-main-batch report — 4fh through 4fj

## Boundary

```text
STAGE14_MAIN_BATCH=COMPLETE
BATCH_START_MAIN_SHA=d519dcccee5bedb4844dbcee5cb4b5171600c0bf
BATCH_PUBLICATION_MAIN_SHA=1416641f09246c308227f6ab51952a7afcc6d5e3
BATCH_FIRST_STAGE=Stage14-4fh
BATCH_LAST_STAGE=Stage14-4fj
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_MAIN_RECEIVER=FixedPrimitiveRayFixedAgreementPairInteriorShortReciprocalSquareclassDivisorPhysicalIncidenceWithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fk
```

## Result

This batch starts from merged `4fg` and consumes merged `s7-89` plus merged `Work-brX30` on the identical global heavy reciprocal-window packet.

### 4fh — exact reciprocal-window geometry

For fixed root windows

```text
I_X=[X_-,X_+],
I_Y=[Y_-,Y_+],
```

and fixed `beta0=B0*c0^2`, the two root conditions become

```text
L in [X_-/A,X_+/A],
L in [beta0*n^2/Y_+, beta0*n^2/Y_-].
```

Their intersection is nonempty exactly for

```text
N_-^2 <= n^2 <= N_+^2,
N_-^2=X_-Y_-/(A beta0),
N_+^2=X_+Y_+/(A beta0).
```

Thus pure geometry contributes one ordinary radial product window, not an independent fixed-power loss. The logarithmic overlap length is piecewise linear and vanishes only at the two radial endpoints.

### 4fi — endpoint support is too small

On an exponent cell `n=B^(nu+o(1))` with required support exponent `mu`, choose

```text
theta>nu-mu.
```

The two endpoint strips of logarithmic thickness `B^-theta` contain only

```text
B^(nu-theta+o(1))=o(B^mu)
```

integers. A surviving heavy packet therefore retains `B^(mu-o(1))` interior radial values, each with reciprocal L-window relative width at least

```text
B^(-theta+o(1)).
```

No short-divisor density theorem is assumed.

### 4fj — existential occupancy becomes a physical incidence sum

For fixed `n`, the admissible squareclass-divisor candidate set `C(n)` has size `B^o(1)`. Retain every transported primitive/canonical/reverse-completion mask in one Boolean `w_phys(n,L)` and define

```text
I_int=sum_n sum_{L in C(n)} w_phys(n,L).
```

Then

```text
#accepted interior n
 <= I_int
 <= B^o(1) #accepted interior n.
```

Hence the existence count and the physical `(n,L)` incidence count are exponent-equivalent. A heavy survivor requires

```text
I_int>=B^(mu-o(1)).
```

This materially changes the heavy receiver to

```text
FixedPrimitiveRayFixedAgreementPairInteriorShortReciprocalSquareclassDivisorPhysicalIncidence
WithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu.
```

The residual physical weight is still bundled, so a new heavy H audit is premature. `4fk` should open `w_phys(n,L)` before freezing an external theorem target.

## Cross-route boundary

Merged Work-brX30 identifies the same reciprocal `(n,L)` coordinate on the s route, but forbids multiplying the two counts. Its fixed-U hyperbola has a different measure and quantifier order; no saving is cross-promoted.

```text
GLOBAL_S_RECIPROCAL_COORDINATE_COUNTS_MULTIPLICABLE=false
COMMON_ARITHMETIC_RECIPROCAL_WINDOW_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
NEW_HEAVY_MAIN_H_NEEDED=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

## Publication recheck

Main advanced during the batch to merged q14 at

```text
1416641f09246c308227f6ab51952a7afcc6d5e3.
```

q14 is consumed as a literature-routing boundary only. It confirms that Ford-type divisor-in-an-interval results are the closest classical architecture, but no direct theorem preserves the Stage14 squareclass restriction, reciprocal partner, charged physical subfamily, and bundled `w_phys(n,L)` masks with a fixed-power deficit. Therefore it does not alter 4fh--4fj and supports the decision not to open a new heavy H before `4fk` exposes the residual physical weight.

```text
Q14_CONSUMED_AS_ROUTING_BOUNDARY=true
Q14_DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
Q14_FORD_TRANSFER_PREMATURE_BEFORE_W_PHYS_OPENING=true
```
