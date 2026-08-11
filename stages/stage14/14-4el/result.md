# Stage14-4el — integrate merged s7-75..77 heavy-ray / genuine-mover split

## Status

`COMPLETE_MERGED_S7_75_77_HEAVY_RAY_OR_GENUINE_MOVER_MAINLINE_INTEGRATION`

Consumes merged `Stage14-4ek`, merged `Stage14-Work-bnX26`, and newly merged `Stage14-s7-75..77` on publication main `b41566868a201b220ef432528b0bcc01198e92ff`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Diagonal collisions are discharged

For one concentrated exact polynomial common-core modulus `C`, merged 4ek gives the character/projective-collision energy. Merged s7-75 makes the unit-incidence normalization explicit and proves that a square-root-saturating exact-`C` cell has

```text
M_C=B^(mu+o(1)), mu>0,
K_off(C)=M_C^2 B^(-o(1)),
```

while the literal diagonal contributes only

```text
K_diag(C)=M_C B^o(1).
```

Therefore diagonal self-pairs are fixed-power too small.

```text
MERGED_S7_75_CONSUMED=true
DIAGONAL_COLLISIONS_CANNOT_SUPPORT_CONCENTRATED_SATURATION=true
```

## 2. Zero determinant is a repeated primitive ray, not a finite global fiber

Merged s7-76 defines

```text
Delta(z1,z2)=X1*Y2-X2*Y1
```

and proves the exact decomposition

```text
K_off(C)=K_ray(C)+K_mov(C),
```

where

```text
K_ray(C): Delta=0,
K_mov(C): Delta=kC, k!=0.
```

Because every candidate vector is primitive, `Delta=0` means the same primitive projective ray up to the frozen finite sign/unit convention. However this does **not** imply a `B^o(1)` global reverse fiber: polynomially many distinct canonical physical backgrounds may produce the same primitive reciprocal ray.

```text
MERGED_S7_76_CONSUMED=true
ZERO_DETERMINANT_COLLISION_IFF_SAME_PRIMITIVE_PROJECTIVE_RAY=true
GLOBAL_PRIMITIVE_RAY_MULTIPLICITY_BOUND=UNPROVED
REPEATED_RAY_RECHARGED_AS_FINITE_FIBER=false
```

This supersedes the earlier batch-local attempt to discard all proportional collisions by per-candidate finite-fiber bookkeeping.

## 3. Quantitative heavy-ray / genuine-mover dichotomy

For primitive ray multiplicities `m_C(r)`, merged s7-77 gives

```text
M_C=sum_r m_C(r),
K_ray(C)=sum_r m_C(r)(m_C(r)-1)
       <= m_max(C) M_C.
```

Since

```text
K_ray(C)+K_mov(C)=M_C^2 B^(-o(1)),
```

one of two mechanisms must carry exponent-zero pair mass.

### Heavy-ray branch

If repeated-ray energy is exponent-zero, then

```text
m_max(C)=M_C B^(-o(1)).
```

Thus one fixed growing `C` and one primitive reciprocal ray are produced by an exponent-zero fraction of the physical backgrounds.

Receiver:

```text
ConcentratedExactCommonCoreHeavyPrimitiveReciprocalRayIncidence.
```

### Genuine-mover branch

Otherwise

```text
K_mov(C)=M_C^2 B^(-o(1))
```

on pairs of distinct primitive rays satisfying

```text
X1*Y2-X2*Y1=kC,
k!=0.
```

Receiver:

```text
ConcentratedExactCommonCoreGenuineProjectiveDeterminantMoverEnergy.
```

```text
MERGED_S7_77_CONSUMED=true
HEAVY_PRIMITIVE_RAY_SURVIVOR_RETAINED=true
GENUINE_DETERMINANT_MOVER_SURVIVOR_RETAINED=true
LARGE_REPEATED_RAY_ENERGY_FORCES_HEAVY_PRIMITIVE_RAY=true
NON_HEAVY_RAY_SATURATION_FORCES_GENUINE_MOVER_ENERGY=true
```

## 4. Mainline routing

Stage14-4em will work **only on the genuine-mover branch**, determining the physical scale and fiber structure of

```text
k=(X1Y2-X2Y1)/C.
```

The heavy-ray branch remains live and requires a later reverse-incidence audit from fixed `(C, primitive ray)` back to canonical allocation slopes/witnesses. It is not consumed or bounded away by 4em.

The diffuse exact-modulus branch from 4ek also remains independent.

## Boundary

```text
STAGE14_4EL=COMPLETE_MERGED_S7_75_77_HEAVY_RAY_OR_GENUINE_MOVER_MAINLINE_INTEGRATION
MERGED_S7_75_77_CONSUMED=true
DIAGONAL_COLLISIONS_CANNOT_SUPPORT_CONCENTRATED_SATURATION=true
GLOBAL_PRIMITIVE_RAY_MULTIPLICITY_BOUND=UNPROVED
HEAVY_PRIMITIVE_RAY_SURVIVOR_RETAINED=true
GENUINE_DETERMINANT_MOVER_SURVIVOR_RETAINED=true
LARGE_REPEATED_RAY_ENERGY_FORCES_HEAVY_PRIMITIVE_RAY=true
NON_HEAVY_RAY_SATURATION_FORCES_GENUINE_MOVER_ENERGY=true
NEW_RECIPROCAL_H_NEEDED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4em
```
