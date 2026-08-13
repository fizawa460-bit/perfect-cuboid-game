# Stage14-s7-63 — proportional collision-energy peel on the primitive divisor-pair receiver

## Status

`COMPLETE_PROPORTIONAL_COLLISION_ENERGY_PEEL_ON_PRIMITIVE_DIVISOR_PAIR_MASS`

Consumes merged `Stage14-s7-62`, merged `Stage14-Work-biX21`, merged `Stage14-4dv`, merged `Stage14-4dw`, merged `Stage14-s7-46`, and latest main. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged s7-62 forces collision energy `B^(1-o(1))`; Work-biX21 freezes one `ell_*=B^o(1)` carrying state mass `B^(1/2-o(1))`; 4dv proves the fixed-prime pair-collision equation is tautological; and 4dw reduces the live state mass to primitive divisor-pair physical-mask mass.

Stage14-s7-63 adds one exact refinement: proportional/diagonal copies of one primitive divisor-pair direction cannot account for the forced exponent-one energy.

## 1. Primitive complementary direction

On the plus graph

```text
r*s=y,
r^2+s^2=2 ell_* x,
r=D-A,
s=D+A.
```

Merged s7-46 gives `D=h0 D0`, `A=h0 A0`, `gcd(D0,A0)=1`, `h0=B^o(1)`. Hence

```text
gcd(r,s) | 2 gcd(D,A)=B^o(1).
```

Write

```text
r=g r0,
s=g s0,
gcd(r0,s0)=1,
g=B^o(1).
```

This agrees with merged 4dw's primitive divisor-pair reduction.

```text
MERGED_4DW_PRIMITIVE_DIVISOR_PAIR_REDUCTION_IMPORTED=true
COMPLEMENTARY_FACTOR_GCD=Bo1
PRIMITIVE_COMPLEMENTARY_DIRECTION_WELL_DEFINED=true
```

## 2. Proportional classes are subpolynomial

For two states put

```text
Delta=r_1 s_2-r_2 s_1.
```

If `Delta=0`, the positive coprime primitive cores have the same projective ratio, hence under the fixed ordering convention

```text
(r_1^0,s_1^0)=(r_2^0,s_2^0).
```

A proportional class therefore varies only through `g=B^o(1)` and already-frozen endpoint/2-primary decorations. Thus

```text
# proportional class = B^o(1).
```

With the charged-once physical multiplicity convention,

```text
Energy_prop
 <= B^o(1) * M(ell_*)
 = B^(1/2+o(1)).
```

But s7-62 forces

```text
Energy_total >= B^(1-o(1)).
```

Therefore

```text
Energy_nonprop >= B^(1-o(1))
```

in lower-bound exponent sense.

```text
PROPORTIONAL_COLLISION_CLASS_SIZE=Bo1
PROPORTIONAL_COLLISION_ENERGY_UPPER_EXPONENT=1/2
FORCED_COLLISION_ENERGY_CANNOT_BE_PROPORTIONAL=true
NONPROPORTIONAL_COLLISION_ENERGY_FORCED=true
NONPROPORTIONAL_COLLISION_ENERGY_LOWER_EXPONENT=1
```

## 3. Nonproportional determinant identity

For `Delta!=0`, define

```text
Sigma=r_1 r_2+s_1 s_2.
```

Lagrange gives

```text
Sigma^2+Delta^2
=(r_1^2+s_1^2)(r_2^2+s_2^2)
=4 ell_*^2 x_1 x_2.
```

If both states lie on the same Gaussian root line modulo `ell_*`, then

```text
ell_* | Delta,
ell_* | Sigma.
```

For opposite root orientations neither divisibility is forced in general. Since `ell_*=B^o(1)`, this gives no fixed-power spacing.

```text
NONPROPORTIONAL_LAGRANGE_DETERMINANT_IDENTITY_PROVED=true
SAME_GAUSSIAN_ROOT_ORIENTATION_DIVIDES_DETERMINANT_AND_DOT_PRODUCT=true
OPPOSITE_GAUSSIAN_ROOT_ORIENTATION_FORCES_SUCH_DIVISIBILITY=false
HEAVY_PRIME_DIVISIBILITY_GIVES_FIXED_POWER_SAVING=false
```

## 4. Why this still does not create a determinant saving

Merged 4dv proves that once `ell_*` is fixed,

```text
x_2(r_1^2+s_1^2)=x_1(r_2^2+s_2^2)
```

is tautological because each state separately satisfies `r_i^2+s_i^2=2 ell_* x_i`.

The Lagrange identity above is likewise a consequence of the two individual fixed-prime norm equations. Thus exponent-one nonproportional energy is real, but it is not a new codimension-two incidence family and may not be charged as an independent determinant saving.

```text
MERGED_4DV_FIXED_PRIME_COLLISION_TAUTOLOGY_IMPORTED=true
NONPROPORTIONAL_COLLISION_PAIR_ADDS_FRESH_CODIMENSION=false
GENERIC_DETERMINANT_SAVING_FROM_COLLISION_EQUATION_LEGAL=false
COLLISION_ENERGY_DOUBLE_CHARGE_ALLOWED=false
```

## 5. Remaining receiver

The proportional explanation is eliminated, while the collision-energy language is discharged as a localization device exactly as in 4dv. The live receiver is therefore merged 4dw's primitive divisor-pair physical-mask mass:

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianPrimePrimitiveDivisorPairPhysicalMaskMass.
```

For the plus branch:

```text
ell_*=B^o(1) fixed,
r<s,
gcd_odd(r,s)=1,
r == +/- i_* s (mod ell_*),
x=(r^2+s^2)/(2 ell_*),
y=rs,
```

with all balanced/range/chart/orientation/reciprocal-completion masks transported as in 4dw.

The next s stage should work directly on those transported masks; pair collision energy has no remaining independent arithmetic content.

## 6. H decision

No new H is opened at s7-63. Merged 4dv/4dw have already changed the theorem shape from pairwise incidence to a one-state primitive divisor-pair family. The physical masks must be transported explicitly before a theorem audit is well posed.

```text
S7_63_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_63=COMPLETE_PROPORTIONAL_COLLISION_ENERGY_PEEL_ON_PRIMITIVE_DIVISOR_PAIR_MASS
MERGED_S7_62_FORCED_ENERGY_IMPORTED=true
MERGED_WORK_BIX21_HEAVY_PRIME_IMPORTED=true
MERGED_4DV_FIXED_PRIME_COLLISION_TAUTOLOGY_IMPORTED=true
MERGED_4DW_PRIMITIVE_DIVISOR_PAIR_REDUCTION_IMPORTED=true
COMPLEMENTARY_FACTOR_GCD=Bo1
PRIMITIVE_COMPLEMENTARY_DIRECTION_WELL_DEFINED=true
PROPORTIONAL_COLLISION_CLASS_SIZE=Bo1
PROPORTIONAL_COLLISION_ENERGY_UPPER_EXPONENT=1/2
FORCED_COLLISION_ENERGY_CANNOT_BE_PROPORTIONAL=true
NONPROPORTIONAL_COLLISION_ENERGY_FORCED=true
NONPROPORTIONAL_COLLISION_ENERGY_LOWER_EXPONENT=1
NONPROPORTIONAL_LAGRANGE_DETERMINANT_IDENTITY_PROVED=true
SAME_GAUSSIAN_ROOT_ORIENTATION_DIVIDES_DETERMINANT_AND_DOT_PRODUCT=true
OPPOSITE_GAUSSIAN_ROOT_ORIENTATION_FORCES_SUCH_DIVISIBILITY=false
NONPROPORTIONAL_COLLISION_PAIR_ADDS_FRESH_CODIMENSION=false
GENERIC_DETERMINANT_SAVING_FROM_COLLISION_EQUATION_LEGAL=false
COLLISION_ENERGY_DOUBLE_CHARGE_ALLOWED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_63_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanFixedSubpolynomialGaussianPrimePrimitiveDivisorPairPhysicalMaskMass
NEXT=Stage14-s7-64
```
