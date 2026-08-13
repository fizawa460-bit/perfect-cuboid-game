# Stage14-Work-bpX28 — outer-support capacity and atomic concentration boundary

## Status

`COMPLETE_OUTER_SUPPORT_CAPACITY_AND_ATOMIC_CONCENTRATION_INTEGRATION`

Consumes merged `Stage14-Work-boX27`, merged mainline through `Stage14-4fa`, merged s-route through `Stage14-s7-83`, merged fixed-U route through `Stage14-t123`, and latest merged main.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Why boX27 must be refined

Work-boX27 proved that after all `B^o(1)` inner fibers are charged once, a fixed-power saving must be visible on polynomial outer mobility. The newest merged descendants show that outer-support cardinality alone is still insufficient: a small outer set may carry essentially all principal weight.

For a finite or weighted outer family `S`, write

```text
M = sum_{x in S} w(x),
w(x)>=0.
```

Then exactly

```text
M <= |S| * max_{x in S} w(x).
```

At exponent level, if

```text
|S| <= B^(sigma+o(1)),
max_x w(x) <= B^(omega+o(1)),
```

then

```text
M <= B^(sigma+omega+o(1)).
```

Therefore a target mass `B^(eta-o(1))` is impossible whenever

```text
sigma+omega < eta.
```

Call this the charged-once **Outer Support Capacity Lemma**.

```text
OUTER_SUPPORT_CAPACITY_LEMMA_PROVED=true
OUTER_SUPPORT_CARDINALITY_ALONE_SUFFICIENT=false
ATOMIC_WEIGHT_CONTROL_REQUIRED_WHEN_SUPPORT_IS_SMALL=true
```

This is bookkeeping plus pigeonhole, not an external saving theorem. It may be used only after the relevant inner multiplicity has already been charged once.

## 2. Mainline heavy ray: explicit support exponent, unknown target exponent

Merged `Stage14-4fa` fixes the primitive ray and agreement packet at `B^o(1)` cost and leaves only the radial scale `h`, with

```text
#h <= B^(1/4-phi+o(1)) <= B^(1/24+o(1)).
```

Merged `4eq` gives only `B^o(1)` physical reverse multiplicity per exact `h`. Hence for this receiver

```text
sigma_h <= 1/24,
omega_h = 0.
```

The branch would close immediately if its required concentrated mass exponent `eta` were known uniformly to satisfy

```text
eta > 1/24.
```

But the merged collision ledger supplies only `eta>0` with no uniform lower bound above `1/24`. Therefore no strict saving may be declared.

```text
MAINLINE_HEAVY_RAY_SUPPORT_CAPACITY_EXPONENT_MAX=1/24
MAINLINE_HEAVY_RAY_ATOMIC_FIBER_EXPONENT=0
MAINLINE_HEAVY_RAY_CLOSURE_IF_ETA_GT_1_24=true
UNIFORM_HEAVY_RAY_REQUIRED_MASS_EXPONENT_GT_1_24_PROVED=false
HEAVY_RAY_CLOSED=false
```

The minimal heavy-ray receiver is now a **mass-versus-capacity comparison**, not an unstructured radial incidence problem:

```text
FixedPrimitiveRayFixedAgreementPairShortRadialScaleMassCapacityGap.
```

## 3. s-route: mobility has split into kernel support or square-part support

Merged `Stage14-s7-83` fixes one physical factor label `F_*` with polynomial value support and writes uniquely

```text
F_* = kappa * a^2.
```

Its exact support identity is

```text
|S_*| = sum_kappa |A_kappa|
      <= |K_*| * max_kappa |A_kappa|.
```

Thus one of the two outer coordinates must carry polynomial mobility:

```text
A. polynomial squarefree-kernel support |K_*|;
B. one fixed kernel with polynomial square-part support |A_kappa|.
```

This is precisely a two-level support-capacity decomposition. The missing step is not another generic square-density estimate; it is a physical atomic-capacity bound on one of these two coordinates with all correlated factor masks retained.

```text
S_ROUTE_TWO_LEVEL_OUTER_SUPPORT_CAPACITY_DECOMPOSITION=true
S_ROUTE_KERNEL_CARDINALITY_BRANCH_RETAINED=true
S_ROUTE_FIXED_KERNEL_SQUAREPART_CAPACITY_BRANCH_RETAINED=true
SQUARECLASS_RECHARGE_ALLOWED=false
```

No new sH is opened here because the factor-specific coefficient system is still not theorem-ready.

## 4. fixed-U: finite support is not a saving without atomic weight control

Merged `Stage14-t123` proves that the complement of the generic physical norm support is contained in

```text
B_bd(m)={g : k0*m*g in {1,2}},
|B_bd(m)|<=2.
```

If a fixed-power generic-support deficit occurs, then essentially all ambient principal weight must concentrate on those at-most-two boundary norms:

```text
sum_{g in B_bd(m)} A_m(g)
 >= (1-B^(-delta)) H_g.
```

Thus fixed-U gives the sharp counterexample to any cardinality-only argument:

```text
sigma_bd = 0
```

does **not** imply a power saving because the atomic weight exponent `omega_bd` is uncontrolled.

The fixed-U branch is therefore exactly an atomic-concentration problem:

```text
FiniteD4BoundaryGenericNormPrimePrincipalAtomicConcentration
OR
PhysicalSelectedProjectiveClassNearTotalPrimeDepletion.
```

```text
FIXED_U_FINITE_BOUNDARY_SUPPORT_EXPONENT=0
FIXED_U_FINITE_BOUNDARY_ATOMIC_WEIGHT_DEFICIT_PROVED=false
FINITE_SUPPORT_ALONE_FIXED_POWER_SAVING=false
FIXED_U_ATOMIC_CONCENTRATION_RECEIVER_PROVED=true
```

## 5. Integrated common principle

The three routes now share the following charged-once template:

```text
outer coordinate x
+ accepted atomic weight w(x)
+ support size exponent sigma
+ atomic capacity exponent omega
+ required mass exponent eta.
```

A power saving follows only from a certified gap

```text
sigma + omega < eta.
```

The arithmetic meanings remain different:

- mainline heavy ray: `x=h` and `sigma<=1/24`;
- s-route: `x=kappa` or `x=a` after factor-level squareclass localization;
- fixed-U: `x=g` on the finite D4 boundary, where `sigma=0` but `omega` may saturate.

Hence:

```text
COMMON_OUTER_SUPPORT_CAPACITY_LANGUAGE_PROVED=true
COMMON_SUPPORT_TIMES_ATOMIC_WEIGHT_TEMPLATE_PROVED=true
COMMON_ARITHMETIC_OUTER_COORDINATE_ADAPTER_PROVED=false
COMMON_ATOMIC_WEIGHT_THEOREM_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

## 6. Other mainline H gates

The non-heavy mainline branches remain unchanged:

```text
CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
```

No result from those H gates is consumed as a positive theorem here. The heavy-ray internal route remains live, so the whole mainline is not H-blocked.

```text
MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH29_NEEDED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

## 7. Current receivers

```text
CURRENT_GLOBAL_RECEIVER=
  FixedPrimitiveRayFixedAgreementPairShortRadialScaleMassCapacityGap
  OR CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
  OR FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
  OR DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation

CURRENT_S_RECEIVER=
  FixedPrimitiveRayDiffusePhysicalFactorSquarefreeKernelCorrelation
  OR FixedPrimitiveRayFixedFactorKernelPolynomialSquarePartPhysicalIncidence
  OR existing non-heavy correlation/H branches

CURRENT_FIXED_U_RECEIVER=
  SharedUFiniteD4BoundaryGenericNormPrimePrincipalAtomicConcentration
  OR PhysicalSelectedProjectiveClassNearTotalPrimeDepletion
```

## Boundary

```text
STAGE14_WORK_BPX28=COMPLETE_OUTER_SUPPORT_CAPACITY_AND_ATOMIC_CONCENTRATION_INTEGRATION
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
OUTER_SUPPORT_CAPACITY_LEMMA_PROVED=true
COMMON_OUTER_SUPPORT_CAPACITY_LANGUAGE_PROVED=true
COMMON_SUPPORT_TIMES_ATOMIC_WEIGHT_TEMPLATE_PROVED=true
MAINLINE_HEAVY_RAY_SUPPORT_CAPACITY_EXPONENT_MAX=1/24
UNIFORM_HEAVY_RAY_REQUIRED_MASS_EXPONENT_GT_1_24_PROVED=false
FIXED_U_FINITE_BOUNDARY_SUPPORT_EXPONENT=0
FIXED_U_FINITE_BOUNDARY_ATOMIC_WEIGHT_DEFICIT_PROVED=false
COMMON_ARITHMETIC_OUTER_COORDINATE_ADAPTER_PROVED=false
COMMON_ATOMIC_WEIGHT_THEOREM_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH29_NEEDED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_REVISIT_CONDITION=4fd_and_s7-86_and_t126_or_material_atomic_capacity_or_H_adapter_trigger
NEXT_INTEGRATED_TARGET=OuterAtomicWeightCapacityDeficitOrNoGo
```
