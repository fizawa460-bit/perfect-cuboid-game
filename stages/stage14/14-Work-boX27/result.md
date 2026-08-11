# Stage14-Work-boX27 — subpolynomial-fiber exhaustion and polynomial outer mobility

## Status

`COMPLETE_SUBPOLYNOMIAL_FIBER_SUPPORT_RELOCATION_AND_POLYNOMIAL_OUTER_MOBILITY`

This integrated Work run consumes merged-only Stage14 sources on latest main at branch start:

- merged `Stage14-Work-bnX26`,
- mainline through merged `Stage14-4eu`, including `Stage14-4eq`,
- s-route through merged `Stage14-s7-80`,
- fixed-U t-route through merged `Stage14-t117`,
- merged `Stage14-q13` literature radar,
- previously merged negative H certificates `Stage14-sH71` and `Stage14-tH28`.

Unmerged descendants are advisory only.

The canonical whole-family boundary remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The Work gate is `RUN`: since merged Work-bnX26 the mainline advanced from 4ef to 4eu, the s route from s7-74 to s7-80, and the t route from t111 to t117, with multiple material receiver changes.

```text
STAGE14_WORK_TOOLBOX_X=RUN
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
```

## 1. Toolbox component — current receiver and H/supersession audit

Merged bnX26 established that the surviving polynomial-scale obstructions were correlation-sensitive. The later merged stages sharpen that statement substantially.

### 1.1 Heavy primitive ray: the fixed-h reverse fiber is now closed

Merged s7-80 left two heavy-ray alternatives:

```text
HR-C: fixed exact radial scale h with an unproved reverse fiber,
HR-D: genuinely diffuse polynomial radial support in h.
```

Merged 4eq consumes that exact s7-80 boundary and proves, without reversing an earlier implication illegally, that for fixed

```text
C,(x,y),h,X=h*x,Y=h*y
```

the exact second reciprocal identity fixes `W2=X^2-Y^2`, leaves only divisor-many `B^o(1)` choices for the required `(U,V,M)` packet, and then applies merged X13 in its proved direction. Therefore

```text
fixed exact h
 -> canonical physical background fiber = B^o(1).
```

Hence the radial-concentration branch is no longer live:

```text
S_ROUTE_FIXED_H_REVERSE_FIBER_SUPERSEDED_BY_MERGED_4EQ=true
FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=Bo1
HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true
HEAVY_RAY_RADIAL_DIFFUSION_BRANCH_RETAINED=true
```

A square-root-saturating heavy primitive ray must therefore use polynomially many exact radial scales `h`; a `B^o(1)` set of `h` values cannot carry the required polynomial mass after the per-h reverse fiber is charged once.

### 1.2 Mainline survivor list after 4eu

Merged 4eu leaves four legal global survivors:

```text
LOW COMMON CORE:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity;

POLYNOMIAL COMMON CORE / HEAVY RAY:
  FixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidence;

POLYNOMIAL COMMON CORE / GENUINE MOVER:
  FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion;

POLYNOMIAL COMMON CORE / DIFFUSE / POLYNOMIAL COMPLEMENTARY NORM:
  DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation.
```

The diffuse `m=B^o(1)` branch is already closed by merged 4es; the remaining diffuse obstruction has polynomial complementary norm `m`. Thus all surviving global branches have a polynomial outer family even though many auxiliary labels, roots, units, divisor splittings and reconstruction fibers are only `B^o(1)`.

```text
DIFFUSE_SUBPOLYNOMIAL_COMPLEMENTARY_QUOTIENT_BRANCH_CLOSED=true
GLOBAL_ACTIVE_POLYNOMIAL_OUTER_MOBILITY=true
```

The current global receiver is

```text
CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
OR FixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidence
OR FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
OR DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation.
```

### 1.3 Fixed-U t117 receiver

Merged t117 gives the exact weighted core factorization

```text
mu_core=lambda_loc*sigma_gen
```

and the three possible fixed-U saving mechanisms

```text
(A) ExceptionalLocalAdmissibleNormSupportWeightedDensityDeficit,
(B) GenericSplitPrimeOrientationPhysicalPrincipalDensityDeficit,
(C) PhysicalSelectedProjectiveClassNearTotalPrimeDepletion.
```

The inner exceptional/orientation labels above one fixed scalar norm are finite or `B^o(1)` by the merged fixed-U packet/orientation decomposition. Therefore (A) and (B) are not independent polynomial inner-fiber lengths: any fixed-power deficit in their weighted averages must be realized by a fixed-power deficit in the weighted set of outer scalar norms that carry at least one accepted inner label.

This gives the structural contraction

```text
(A) or (B)
 -> WeightedPhysicalScalarNormSupportDeficit
```

up to `B^o(1)` losses. Mechanism (C) remains a cofactor-dependent prime-depletion correlation and is not identified with the global branches.

```text
FIXED_U_LOCAL_AND_ORIENTATION_DEFICITS_RELOCATE_TO_WEIGHTED_NORM_SUPPORT=true
FIXED_U_INNER_LABEL_POWER_SAVING_AS_INDEPENDENT_LENGTH=false
```

A useful current fixed-U receiver is therefore

```text
SharedUWeightedPhysicalScalarNormSupportDeficit
OR PhysicalSelectedProjectiveClassNearTotalPrimeDepletion.
```

This is a structural supersession of the three-label presentation only; it does not prove either deficit.

## 2. X27 component — subpolynomial-fiber support relocation lemma

The preceding route-specific reductions are instances of one elementary charged-once principle.

Let `Y_B` be an outer index set with nonnegative weights `w_y`. For each `y`, let `F_y` be an inner fiber satisfying uniformly

```text
1 <= |F_y| <= B^o(1).
```

Let

```text
A(y,f) in {0,1}
```

be a physical acceptance predicate and define

```text
H = sum_y w_y |F_y|,
M = sum_y w_y sum_{f in F_y} A(y,f),
S = {y : exists f in F_y with A(y,f)=1}.
```

Since every `y in S` contributes at least one accepted point,

```text
M >= sum_{y in S} w_y.
```

And since `|F_y|<=B^o(1)`, uniformly,

```text
H <= B^o(1) sum_y w_y.
```

Therefore any fixed-power deficit

```text
M <= B^(-delta) H
```

forces

```text
sum_{y in S} w_y
 <= B^(-delta+o(1)) sum_y w_y.
```

Equivalently: once the inner fiber is only subpolynomial, a fixed positive `B`-power saving cannot live purely in nonzero inner-fiber density. It must relocate to the polynomial outer support on which the inner fiber is nonempty.

```text
SUBPOLYNOMIAL_FIBER_SUPPORT_RELOCATION_LEMMA_PROVED=true
COMMON_SUBPOLYNOMIAL_FIBER_EXHAUSTION_PROVED=true
COMMON_FIXED_POWER_SAVING_REQUIRES_POLYNOMIAL_OUTER_MOBILITY=true
```

This is a counting lemma, not an independence statement and not an arithmetic theorem about the remaining outer support.

## 3. Route instantiations

### 3.1 Global heavy ray

Take

```text
y = exact radial scale h.
```

Merged 4eq proves the reverse physical fiber over one fixed `h` is `B^o(1)`. Hence polynomial heavy-ray mass cannot be supported by `B^o(1)` exact `h` values. Saturation forces polynomial radial mobility.

```text
HEAVY_RAY_SATURATION_REQUIRES_POLYNOMIALLY_MANY_RADIAL_SCALES=true
```

### 3.2 Global diffuse complementary factor

Merged 4es closes the subpolynomial complementary quotient. Merged 4et/4eu leave only

```text
m=N(beta)=B^(lambda+o(1)), lambda>0,
```

inside the diffuse Gaussian-factor correlation. Thus the diffuse branch has already relocated its remaining difficulty to a polynomial outer complementary norm.

```text
DIFFUSE_SURVIVOR_REQUIRES_POLYNOMIAL_COMPLEMENTARY_NORM=true
```

### 3.3 Fixed-U physical core

Take

```text
y = scalar cofactor norm n,
f = exceptional/orientation label (e,epsilon).
```

Merged t115/t116 provide the norm-fiber tower and a `B^o(1)` inner label set. Applying the support-relocation lemma to the physical-core Boolean shows that any fixed-power loss from t117 mechanisms (A) or (B) is, after charged-once normalization, a weighted deficit in the outer scalar-norm support carrying at least one accepted physical label.

```text
FIXED_U_GENERIC_ORIENTATION_POWER_DEFICIT_RELOCATES_TO_WEIGHTED_NORM_SUPPORT=true
FIXED_U_EXCEPTIONAL_LOCAL_POWER_DEFICIT_RELOCATES_TO_WEIGHTED_NORM_SUPPORT=true
```

This does not settle mechanism (C), because selected projective prime occupancy varies with the cofactor and its interval and is a different correlation problem.

## 4. What X27 does not identify

The common outer-mobility principle does not identify the arithmetic outer variables:

```text
global low-C      : primitive slope / correlated divisor allocation,
global heavy ray  : radial scale h,
global mover      : polynomial determinant/projective collision family,
global diffuse    : complementary Gaussian norm m,
fixed-U           : weighted scalar cofactor norm n and cofactor-selected prime depletion.
```

No merged theorem supplies measure-preserving maps among these objects. Therefore

```text
COMMON_ARITHMETIC_OUTER_MOBILITY_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
GLOBAL_FIXED_U_BACKGROUND_MEASURES_IDENTIFIED=false
```

The result is a legal common proof architecture: eliminate/recharge no `B^o(1)` fibers, expose the polynomial outer support, then attack its actual physical correlation.

## 5. Literature / q13 interface

Merged q13 confirms there is still no direct theorem for the full current obstruction. Its three useful falsifiable tests align exactly with the surviving polynomial outer families:

```text
Q13_THREE_DIVISOR_MULTI_POLYNOMIAL_WEIGHT_TEST,
Q13_PROJECTIVE_KLOOSTERMAN_TRANSFER_TEST,
Q13_DIFFUSE_MODULUS_SW_TEST.
```

The heavy-ray branch remains internal and, after 4eq, has become an explicitly one-dimensional polynomial radial-support problem rather than an external theorem target.

```text
Q13_DIRECT_FULL_OBSTRUCTION_THEOREM_AVAILABLE=false
HEAVY_RAY_EXTERNAL_SEARCH_TRIGGERED=false
```

## 6. H decisions

### Mainline

There are now three separate theorem-ready mainline branches and one internal branch.

```text
MAINLINE_H_NEEDED=true
MAINLINE_H_TARGETS=
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity;
  FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion;
  DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

The heavy-ray radial-diffusion receiver remains internal and prevents the whole mainline from being classified as H-blocked.

### s route

Merged 4eq resolves s7-80's fixed-h reverse-fiber uncertainty. No new sH is needed at this boundary; the existing mover-only H gate belongs to the shared global/s mover branch, while the radial-diffusion branch should continue internally.

```text
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

### fixed-U t route

Merged t117 explicitly requires further internal opening of the outer norm-support mechanisms before another external audit.

```text
FIXED_U_H_NEEDED=false
TH29_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## 7. Charged-once locks

The following cannot be reused as fresh savings:

```text
finite Gaussian units/orientations,
B^o(1) divisor factorizations,
B^o(1) fixed-h reverse reconstruction,
B^o(1) fixed-norm exceptional/orientation labels,
standalone Gaussian split support,
projective class partition into B^o(1) cells,
previous collision-energy localization,
previous principal-density decompositions.
```

```text
SUBPOLYNOMIAL_INNER_FIBER_RECHARGE_ALLOWED=false
FIXED_H_REVERSE_FIBER_RECHARGE_ALLOWED=false
FIXED_NORM_LABEL_FIBER_RECHARGE_ALLOWED=false
PRIME_CLASS_PARTITION_RECHARGE_ALLOWED=false
```

## Boundary

```text
STAGE14_WORK_BOX27=COMPLETE_SUBPOLYNOMIAL_FIBER_SUPPORT_RELOCATION_AND_POLYNOMIAL_OUTER_MOBILITY
STAGE14_WORK_TOOLBOX_X=RUN
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_GLOBAL_RECEIVER=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensityOrFixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidenceOrFixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersionOrDiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
CURRENT_FIXED_U_RECEIVER=SharedUWeightedPhysicalScalarNormSupportDeficitOrPhysicalSelectedProjectiveClassNearTotalPrimeDepletion
SUBPOLYNOMIAL_FIBER_SUPPORT_RELOCATION_LEMMA_PROVED=true
COMMON_SUBPOLYNOMIAL_FIBER_EXHAUSTION_PROVED=true
COMMON_FIXED_POWER_SAVING_REQUIRES_POLYNOMIAL_OUTER_MOBILITY=true
HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true
HEAVY_RAY_RADIAL_DIFFUSION_BRANCH_RETAINED=true
FIXED_U_LOCAL_AND_ORIENTATION_DEFICITS_RELOCATE_TO_WEIGHTED_NORM_SUPPORT=true
COMMON_ARITHMETIC_OUTER_MOBILITY_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH29_NEEDED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_REVISIT_CONDITION=4ex_and_s7-83_and_t120_or_material_H_or_adapter_trigger
```

Next integrated target:

```text
PolynomialOuterSupportCorrelationIntersectionOrNoGo
```
