# Stage14-main-batch report — 4fw through 4fy

## Boundary

```text
STAGE14_MAIN_BATCH=COMPLETE
BATCH_START_MAIN_SHA=5884e0ec4f9fc85589e00edafbdc6cda3c67bc2d
BATCH_PUBLICATION_MAIN_SHA=5884e0ec4f9fc85589e00edafbdc6cda3c67bc2d
BATCH_FIRST_STAGE=Stage14-4fw
BATCH_LAST_STAGE=Stage14-4fy
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_MAIN_RECEIVER=FixedComplementaryDilationPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport_OR_FixedComplementaryDilationTwoSidedPrincipalRectangularDistinctProductCapacityVersusConditionalPhysicalLiftDeficit_OR_PolynomialComplementaryDilationFixedPrimitiveProductResidualELocalMaskVersusConditionalPhysicalCompletionDeficit_OR_PolynomialComplementaryDilationPolynomialPrimitiveProductBareUnitaryOuterPairShadowVersusConditionalPhysicalCompletionDeficit_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fz
```

## Result

This batch consumes merged mainline through `4fv`, merged `s7-102..104`, merged `q15`, and merged `Work-bwX35`. The frozen but unexecuted fixed-U `tH32` target remains route-local and is not cross-promoted.

### 4fw — exact straightening of the moving ordinary divisor interval

On fixed `E=E0`, the two primitive factors satisfy

```text
m=u*v,
|Xr|=alpha*E0*u^2,
|Yr|=beta*E0*v^2.
```

The frozen root/exponent chart therefore gives two fixed integer factor windows `D,V`. The moving ordinary-divisor shadow is exactly

```text
exists d|m with d in D and m/d in V
```

and hence

```text
O_2s(m)=1 <=> m in P(D,V):={dv:d in D,v in V}.
```

Thus q15's moving-center normalization issue is eliminated algebraically. The fixed-E two-sided ordinary envelope is a rectangular distinct-product support problem.

### 4fx — close subcritical rectangles by elementary pair capacity

Write

```text
#D=B^(kappa_D+o(1)),
#V=B^(kappa_V+o(1)).
```

Since

```text
#P(D,V)<=#D#V,
```

merged Work-bwX35's absolute-capacity lemma closes every rectangle with

```text
kappa_D+kappa_V <= mu-eta
```

for fixed `eta>0`. Every surviving principal rectangle must satisfy

```text
kappa_D+kappa_V >= mu-o(1).
```

### 4fy — material receiver change

On a surviving principal rectangle define

```text
#P(D,V)=B^(pi+o(1)),
#physical support=B^(tau+o(1)),
delta_lift=pi-tau.
```

Then heavy survival is exactly

```text
pi-delta_lift=tau>=mu.
```

The remaining fixed-E two-sided mechanisms are therefore separated into

```text
P: fixed-power distinct-product capacity loss,
C: fixed-power conditional physical-lift loss inside the product support.
```

The former Ford-style moving divisor interval is no longer the minimal object. The new fixed-E two-sided receiver is

```text
FixedComplementaryDilationTwoSidedPrincipalRectangularDistinctProductCapacityVersusConditionalPhysicalLiftDeficit.
```

No new heavy H is opened yet: the next internal step must split principal rectangles by multiplication-map collision energy versus near-injective product support and compare the resulting `pi` threshold to `mu` before freezing an external theorem target.

## Charged-once locks

```text
Q15_UNITARY_UPPER_ENVELOPE_ADAPTER_COMPLETE=true
Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=false
Q15_LOCALIZED_DIVISOR_ROUTE_SUPERSEDED_BY_RECTANGULAR_PRODUCT_CAPACITY=true
SUBCRITICAL_RECTANGLE_CAPACITY_BRANCH_CLOSED=true
DISTINCT_PRODUCT_CAPACITY_MECHANISM_SEPARATED=true
CONDITIONAL_PHYSICAL_LIFT_MECHANISM_SEPARATED=true
UNITARY_ORDINARY_BOUNDED_DISTORTION_PROVED=false
LITERATURE_FIXED_POWER_SAVING_IMPORTED=false
FIXED_U_SAVING_CROSS_PROMOTED=false
```
