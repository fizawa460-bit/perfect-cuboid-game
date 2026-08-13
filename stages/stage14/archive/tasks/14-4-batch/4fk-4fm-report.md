# Stage14-main-batch report — 4fk through 4fm

## Boundary

```text
STAGE14_MAIN_BATCH=COMPLETE
BATCH_START_MAIN_SHA=1cce848e748d6b02d7e878c6bd1b326e953bc98c
BATCH_PUBLICATION_MAIN_SHA=1cce848e748d6b02d7e878c6bd1b326e953bc98c
BATCH_FIRST_STAGE=Stage14-4fk
BATCH_LAST_STAGE=Stage14-4fm
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_MAIN_RECEIVER=FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence_OR_PolynomialComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fn
```

## Result

This batch consumes merged mainline through `4fj`, merged `s7-90..92`, merged `Work-bsX31`, and merged `q14` as a negative/directness boundary.

### 4fk — exact physical-weight opening

Merged Work-bsX31 identifies the main heavy incidence with the exact primitive-ratio coordinates

```text
n=E*u*v,
gcd(u,v)=1,
L=E*u^2,
L/n=u/v.
```

Therefore the 4fj interior incidence pulls back to

```text
I_int
 = sum_n
   sum_{gcd(u,v)=1, uv|n, u/v in R_int(n)}
      m_E(E) m_cpl(n,u,v,E),
E=n/(uv).
```

Here `m_E` contains only the inherited squareclass/gcd conditions proved to depend on `E`/`sqf(E)`, while `m_cpl` retains every remaining canonical/reverse physical condition. This is an exact Boolean conjunction, not an independence factorization.

### 4fl — projective endpoint versus balanced primitive ratios

After exponent localization

```text
nu=epsilon+alpha+beta,
E~B^epsilon,
u~B^alpha,
v~B^beta,
```

one can freeze a finite alternative:

```text
alpha=0,
beta=0,
or alpha,beta>0.
```

A subpolynomial primitive factor may be frozen at `B^o(1)` cost, but the endpoint branch does not close because the complementary dilation and the opposite primitive factor may remain polynomial. Radial endpoint discharge from 4fi is not reusable as projective-ratio endpoint discharge.

### 4fm — complementary-dilation split and unitary-divisor receivers

If `E=B^o(1)`, freeze exact `E=E0` and put `m=n/E0`. Then

```text
m=u*v,
gcd(u,v)=1,
u/v=u^2/m.
```

Thus `u` is a unitary divisor of `m` lying in the transported short interval `sqrt(m R_int(E0 m))`, with the exact canonical/reverse Boolean retained.

If `E` has polynomial scale, it cannot be frozen. The receiver becomes a two-level correlation

```text
n=E*m,
u|m,
gcd(u,m/u)=1,
u^2/m in R_int(E*m),
```

weighted by the complementary-`E` and canonical/reverse physical masks.

This materially changes the heavy receiver to

```text
FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence
OR
PolynomialComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation.
```

## q14 / H boundary

The fixed-`E` branch passes the geometric part of q14's Ford transfer test but is still not a direct Ford theorem: the divisor is unitary, the canonical/reverse physical Boolean remains, and no bounded-distortion comparison of the charged Stage14 baseline with the unrestricted Ford ensemble is proved. The polynomial-`E` branch retains an additional polynomial correlation.

```text
Q14_STEP1_RECIPROCAL_WINDOW_TO_ONE_DIVISOR_INTERVAL=PASS_AT_GEOMETRY_LEVEL
Q14_STEP2_SQUARECLASS_REMOVAL=PASS_ONLY_ON_FIXED_E_BRANCH_AFTER_FREEZE
Q14_STEP3_CHARGED_PHYSICAL_MEASURE_BOUNDED_DISTORTION=NOT_PROVED
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

The next mainline step is `Stage14-4fn`, opening the canonical/reverse completion Boolean on the fixed-`E` unitary-divisor branch first.

## Publication recheck

Latest merged main remained

```text
1cce848e748d6b02d7e878c6bd1b326e953bc98c
```

through publication recheck. No concurrent unmerged route result is consumed as a theorem source.
