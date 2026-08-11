# Stage14-Work-bqX29 — atomic-capacity exhaustion and residual outer-selection split

## Status

`COMPLETE_ATOMIC_CAPACITY_EXHAUSTION_TO_RADIAL_OCCUPANCY_OR_SELECTED_CLASS_DEPLETION`

Consumes only merged theorem sources on latest main:

- merged `Stage14-Work-bpX28`;
- merged mainline `Stage14-4fb..4fd`;
- merged s-route `Stage14-s7-84..86`;
- merged fixed-U `Stage14-t124`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. What bpX28 left open

Work-bpX28 isolated the general charged capacity inequality

```text
M = sum_{x in S} w(x) <= |S| max_x w(x).
```

Its unresolved question was whether a fixed-power obstruction could still hide in a small outer support carrying large atomic weight.

The new merged descendants settle that question differently on the global/s heavy-ray packet and on fixed-U.

## 2. Mainline: atomic capacity is saturated only by polynomial radial occupancy

Merged `4fb` proves on one fixed heavy primitive reciprocal ray

```text
m_max(C) <= B^(rho(phi)+o(1)),
rho(phi)=1/4-phi<=1/24.
```

Merged `4fc` compares this with repeated-ray collision energy.  A surviving heavy packet

```text
M_C=B^(mu+o(1))
```

must satisfy

```text
0<mu<=rho(phi)<=1/24.
```

Merged `4fd` then uses the already charged `B^o(1)` reverse multiplicity per exact radial scale and proves that a maximizing heavy ray must carry

```text
B^(mu-o(1)) <= |H_*| <= B^(rho(phi)+o(1)).
```

Therefore a surviving heavy ray cannot support exponent-`mu` mass by concentrating it on `B^o(1)` radial atoms with anomalously large weights.  The mass exponent itself forces polynomially many distinct exact radial scales.

```text
MAINLINE_HEAVY_ATOMIC_CAPACITY_GAP_SUPERSEDED=true
MAINLINE_HEAVY_MASS_FORCES_MATCHING_RADIAL_SUPPORT_EXPONENT=true
MAINLINE_HEAVY_RADIAL_SUPPORT_LOWER_BOUND=B^(mu-o(1))
MAINLINE_HEAVY_RADIAL_SUPPORT_UPPER_BOUND=B^(1/4-phi+o(1))
MAINLINE_HEAVY_SURVIVOR_MU_RANGE=0<mu<=1/4-phi
```

The live heavy-ray question is now arithmetic density/structure of the polynomial radial support, not atomic weight capacity.

## 3. s-route: squareclass/kernel/square-part mobility is a finite fiber over the same radial coordinate

Merged `s7-84..86` consumes the same fixed primitive ray and the same agreement-pair compression.  After freezing one exact agreement pair,

```text
Xr*Yr = r0*h^2.
```

Writing the moving root factors in squareclass normal form and freezing the fixed noncommon squareclass data gives exact integers `c0,d0` with

```text
d0*J*a*b = c0*h.
```

For one exact `h`, the number of `(J,a,b)` factorizations is divisor-many:

```text
#(J,a,b | h) <= d_3(c0*h)=B^o(1).
```

Thus the s7-83 kernel-diffusion and fixed-kernel square-part branches are not independent polynomial outer coordinates.  They are `B^o(1)` fibers over the exact same radial coordinate `h` used by merged `4fd`.

Hence the stronger merged mainline mass-to-radial-support theorem directly supersedes the older s7-86 `ShortRadialScaleMassCapacityGap` receiver on this identical global heavy-ray packet:

```text
GLOBAL_S_EXACT_RADIAL_COORDINATE_IDENTIFIED=true
GLOBAL_S_RADIAL_FIBER_MULTIPLICITY=Bo1
S_HEAVY_CAPACITY_GAP_SUPERSEDED_BY_MERGED_4FD=true
GLOBAL_S_COMMON_RADIAL_OUTER_COORDINATE_PROVED=true
```

This is a same-packet theorem consumption, not a cross-promotion from fixed-U and not a second charge of the reverse fiber.

The global/s heavy receiver is therefore

```text
FixedPrimitiveRayFixedAgreementPairPolynomialRadialOccupancy
WithMassExponentMuAtMostOneQuarterMinusPhi.
```

## 4. fixed-U: the finite atomic boundary is discharged, not estimated

Merged `t124` proves that the finite D4 boundary atoms do not contribute to the actual strict physical short-cover chamber.  Splitting by their ambient principal mass gives:

```text
boundary-heavy
  -> nonboundary physical baseline is already fixed-power small;

boundary-light
  -> renormalize to the nonboundary baseline and retain a fixed positive target exponent.
```

Therefore the Work-bpX28 finite-boundary atomic-weight obstruction is no longer a live fixed-U theorem receiver.

```text
FIXED_U_FINITE_BOUNDARY_ATOMIC_BRANCH_DISCHARGED=true
FIXED_U_ATOMIC_WEIGHT_OBSTRUCTION_SUPERSEDED=true
FIXED_U_BOUNDARY_HEAVY_CORE_SAVING_CLOSED=true
FIXED_U_BOUNDARY_LIGHT_RENORMALIZATION_RETAINS_POSITIVE_POWER=true
```

The only live fixed-U mechanism is

```text
SharedUNonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion.
```

No `tH29` is justified yet: `t125` must first freeze the exact nonboundary cofactor-to-projective-class map and physical prime interval.

## 5. Integrated conclusion

All three routes have now moved beyond the generic Work-bpX28 question "can a small outer support carry too much mass?":

- global/s heavy ray: exponent-level mass forces polynomial exact-`h` occupancy with the same exponent;
- fixed-U: the only finite atomic support branch is removed by the strict physical chamber and a baseline split.

So atomic support cardinality/atomic weight concentration is not the common final receiver.

```text
COMMON_ATOMIC_CAPACITY_AS_FINAL_RECEIVER_SUPERSEDED=true
COMMON_OUTER_SUPPORT_CAPACITY_LEMMA_RETAINED_AS_BOOKKEEPING=true
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

The remaining mechanisms are arithmetically different:

```text
GLOBAL/S:
  polynomial exact-radial-scale physical occupancy

FIXED-U:
  nonboundary cofactor-selected projective prime-class near-total depletion.
```

No finite-fiber arithmetic map preserving the physical measures and quantifier order between these coordinates is proved.

```text
COMMON_ARITHMETIC_OUTER_COORDINATE_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## 6. Current receivers and H decisions

```text
CURRENT_GLOBAL_RECEIVER=FixedPrimitiveRayFixedAgreementPairPolynomialRadialOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
CURRENT_S_RECEIVER=FixedPrimitiveRayFixedAgreementPairPolynomialRadialOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
CURRENT_FIXED_U_RECEIVER=SharedUNonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion

MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH29_NEEDED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

The mainline H flag refers only to the existing non-heavy three-divisor / mover / diffuse correlation targets.  The heavy radial branch still has an internal arithmetic successor.

## 7. Next integrated target

The next common test is whether the two remaining outer-selection mechanisms admit any exact common structure beyond generic occupancy language:

```text
NEXT_INTEGRATED_TARGET=RadialOccupancyVersusSelectedProjectiveClassDepletionAdapterOrNoGo
```

Normal revisit condition:

```text
NEXT_REVISIT_CONDITION=4fg+s7-89+t127
```

Earlier revisit is justified by any of:

- a fixed-power deficit for the polynomial radial support;
- deterministic closure of selected-projective-class depletion;
- a theorem-ready `tH29` target;
- a new mainline H result;
- an exact physical finite-fiber adapter between the residual outer coordinates;
- any new strict sub-square-root whole-family exponent.

## Boundary locks

```text
STAGE14_WORK_BQX29=COMPLETE
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
COMMON_ATOMIC_CAPACITY_AS_FINAL_RECEIVER_SUPERSEDED=true
GLOBAL_S_COMMON_RADIAL_OUTER_COORDINATE_PROVED=true
S_HEAVY_CAPACITY_GAP_SUPERSEDED_BY_MERGED_4FD=true
FIXED_U_FINITE_BOUNDARY_ATOMIC_BRANCH_DISCHARGED=true
COMMON_ARITHMETIC_OUTER_COORDINATE_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH29_NEEDED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_INTEGRATED_TARGET=RadialOccupancyVersusSelectedProjectiveClassDepletionAdapterOrNoGo
NEXT_REVISIT_CONDITION=4fg+s7-89+t127
```
