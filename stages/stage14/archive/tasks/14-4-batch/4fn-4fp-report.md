# Stage14-main-batch report — 4fn through 4fp

## Boundary

```text
STAGE14_MAIN_BATCH=COMPLETE
BATCH_START_MAIN_SHA=43c2beeda0c9c5af2154d6deca5912d5be9e3ab2
BATCH_PUBLICATION_MAIN_SHA=43c2beeda0c9c5af2154d6deca5912d5be9e3ab2
BATCH_FIRST_STAGE=Stage14-4fn
BATCH_LAST_STAGE=Stage14-4fp
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_MAIN_RECEIVER=FixedComplementaryDilationOuterSupportOfPhysicalShortUnitaryDivisorExistence_OR_PolynomialComplementaryDilationOuterPairSupportOfPhysicalShortUnitaryDivisorExistence_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fq
```

## Result

This batch consumes merged mainline through `4fm`, merged `s7-93..95`, merged `Work-btX32`, merged `t132` only through the btX32 integrated boundary, and q14 only as the existing literature-routing boundary.

### 4fn — fixed-E inner weight projects to outer support

Freeze exact admissible `E=E0` and write `m=n/E0`. The inner candidates are unitary divisors

```text
u || m,
u in U_E0(m),
```

with exact canonical/reverse Boolean `k_E0(m,u)`. Since

```text
#{u || m}<=2^omega(m)<=tau(m)=B^o(1),
```

define

```text
A_E0(m)=1{exists physical unitary candidate u}.
```

Then

```text
A_E0(m)
<= sum_u k_E0(m,u)
<= B^o(1) A_E0(m).
```

Therefore the fixed-E weighted incidence and the outer accepted-`m` support are exponent-equivalent.

### 4fo — polynomial-E inner weight projects to outer-pair support

For `E=B^(epsilon+o(1))`, `epsilon>0`, write `n=E*m` and keep the exact Boolean `k(E,m,u)`. For every fixed outer pair `(E,m)`, the unitary inner fiber is still `B^o(1)`. Hence with

```text
A_poly(E,m)=1{exists physical unitary candidate u},
```

one has

```text
sum_{E,m} A_poly(E,m)
<= I_poly
<= B^o(1) sum_{E,m} A_poly(E,m).
```

The two-variable outer correlation remains genuine; only inner multiplicity is exhausted.

### 4fp — material receiver change

A surviving heavy packet therefore forces either

```text
#{m:A_E0(m)=1}>=B^(mu-o(1))
```

for one exact `E0=B^o(1)`, or

```text
#{(E,m):A_poly(E,m)=1}>=B^(mu-o(1)).
```

Thus the heavy obstruction is no longer an inner-dependent weighted-unitary multiplicity. It is the outer density of integers / outer pairs admitting at least one **physical** short unitary-divisor witness.

The canonical/reverse mask is retained inside the existential predicate; no pointwise independence or factorization is claimed.

## q14 / integrated boundary

The fixed-E branch is now even closer to Ford's existential divisor-in-an-interval quantifier, but the divisor is unitary and the canonical/reverse physical restriction remains. No bounded-distortion comparison with the unrestricted Ford ensemble is proved. The polynomial-E branch remains a two-variable outer-support problem.

```text
PHYSICAL_WEIGHT_OUTERIZED_AT_SUPPORT_LEVEL=true
POINTWISE_WEIGHT_FACTORIZATION_PROVED=false
Q14_STEP3_CHARGED_PHYSICAL_MEASURE_BOUNDED_DISTORTION=NOT_PROVED
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

This receiver change satisfies the common batch stop rule after three substantive work units.

## Publication recheck

Latest merged main remained

```text
43c2beeda0c9c5af2154d6deca5912d5be9e3ab2
```

through publication recheck. No concurrent unmerged route result is consumed as a theorem source.
