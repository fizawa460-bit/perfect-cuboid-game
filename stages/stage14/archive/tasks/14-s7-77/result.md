# Stage14-s7-77 — heavy primitive-ray concentration versus genuine determinant-mover energy

## Status

`COMPLETE_CONCENTRATED_PROJECTIVE_COLLISION_TO_HEAVY_RAY_OR_GENUINE_MOVER_DICHOTOMY`

Consumes batch-local `Stage14-s7-75/76`, merged `Stage14-4ek`, and merged `Stage14-Work-bnX26`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Maximum ray multiplicity controls the proportional energy

For a fixed concentrated polynomial modulus `C`, write

```text
M_C=sum_r m_C(r),
m_max(C)=max_r m_C(r).
```

The repeated-ray pair mass satisfies exactly

```text
K_ray(C)=sum_r m_C(r)(m_C(r)-1)
       <= m_max(C) M_C.
```

Stage14-s7-75/76 gives on every concentrated saturating sequence

```text
K_ray(C)+K_mov(C)=M_C^2 B^(-o(1)).
```

## 2. Heavy-ray alternative

If

```text
K_ray(C)=M_C^2 B^(-o(1)),
```

then the inequality above forces

```text
m_max(C)=M_C B^(-o(1)).
```

Hence one primitive reciprocal projective ray carries exponent-zero fraction of the entire exact-`C` physical candidate mass.

This is not the old per-slope `B^o(1)` candidate fiber. It is a cross-background concentration statement:

```text
one fixed growing C,
one primitive reciprocal ray,
polynomially many canonical physical backgrounds producing that same ray.
```

Call the receiver

```text
ConcentratedExactCommonCoreHeavyPrimitiveReciprocalRayIncidence.
```

```text
LARGE_REPEATED_RAY_ENERGY_FORCES_HEAVY_PRIMITIVE_RAY=true
HEAVY_RAY_RELATIVE_MASS_EXPONENT_ZERO=true
```

No reverse-incidence bound for this heavy ray is presently merged.

## 3. Genuine mover alternative

If the repeated-ray contribution is not exponent-zero on the pair-density scale, then Stage14-s7-76 forces

```text
K_mov(C)=M_C^2 B^(-o(1)).
```

Thus exponent-zero mass lies on distinct primitive rays satisfying

```text
X1Y2-X2Y1=kC,
k!=0.
```

This is a genuine determinant-mover collision receiver. The same common-core modulus `C` is already charged; neither `C` nor the quotient `k` may be treated as a second independent modulus without an additional size/fiber theorem.

Call the receiver

```text
ConcentratedExactCommonCoreGenuineProjectiveDeterminantMoverEnergy.
```

```text
NON_HEAVY_RAY_SATURATION_FORCES_GENUINE_MOVER_ENERGY=true
SECOND_MODULUS_RECHARGE_ALLOWED=false
```

## 4. Full s-route receiver after the split

The other two branches from merged s7-74 / 4ek remain unchanged:

```text
small C0:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity;

polynomial C0, diffuse exact-modulus support:
  DiffusePolynomialCommonCoreCanonicalAllocationNormDivisorGraphDiscrepancy.
```

The concentrated polynomial branch has now split strictly further into

```text
heavy primitive reciprocal ray
OR
genuine nonzero determinant mover energy.
```

Therefore the current s receiver is

```text
SmallCommonCoreCanonicalBalancedIntegerGaussianAllocationDensity
OR
ConcentratedExactCommonCoreHeavyPrimitiveReciprocalRayIncidence
OR
ConcentratedExactCommonCoreGenuineProjectiveDeterminantMoverEnergy
OR
DiffusePolynomialCommonCoreCanonicalAllocationNormDivisorGraphDiscrepancy.
```

```text
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. H decision

No new sH is opened at this boundary. The new concentrated branches still have immediate internal questions:

```text
heavy ray:
  determine reverse multiplicity from fixed (C, primitive ray)
  back to canonical allocation slopes/witnesses;

mover:
  determine the physical size range and fiber structure of
  k=(X1Y2-X2Y1)/C;

diffuse:
  retain the variable norm-divisor graph quantifier audit.
```

Opening a common external theorem before those coefficients are frozen would repeat the theorem-shape mismatch certified by sH71.

```text
S7_77_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_77=COMPLETE_CONCENTRATED_PROJECTIVE_COLLISION_TO_HEAVY_RAY_OR_GENUINE_MOVER_DICHOTOMY
LARGE_REPEATED_RAY_ENERGY_FORCES_HEAVY_PRIMITIVE_RAY=true
HEAVY_RAY_RELATIVE_MASS_EXPONENT_ZERO=true
NON_HEAVY_RAY_SATURATION_FORCES_GENUINE_MOVER_ENERGY=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_S_RECEIVER=SmallCommonCoreCanonicalBalancedIntegerGaussianAllocationDensity_OR_ConcentratedExactCommonCoreHeavyPrimitiveReciprocalRayIncidence_OR_ConcentratedExactCommonCoreGenuineProjectiveDeterminantMoverEnergy_OR_DiffusePolynomialCommonCoreCanonicalAllocationNormDivisorGraphDiscrepancy
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_77_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-78
```
