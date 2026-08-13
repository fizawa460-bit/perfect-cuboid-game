# Stage14-4dc — Gaussian product root-line compression and refined mainline H gate

## Status

`COMPLETE_GAUSSIAN_PRODUCT_ROOT_LINE_COMPRESSION_TRANSVERSE_RESULTANT_NOGO_AND_MAINLINE_H_GATE`

Stage14-4dc consumes merged `Stage14-4db`, `Stage14-s7-44`, `Stage14-s7-42`, `Stage14-s7-29`, and the X13 reverse-reciprocal square-root theorem.

The entering theorem remains

```text
V(B) << B^(1/2+o(1)).
```

No fixed `delta>0` below square root is proved here.  This stage compresses the s7-44 dual-root-line receiver and proves a stronger no-go for a second full-core determinant modulus.

## 1. Saturating coefficient space

Every possible square-root equality sequence is already confined to

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=K=B^o(1),
C/J=B^o(1),
C_Cayley/J=B^o(1).
```

Hence at fixed-power scale

```text
C=J=C_Cayley
```

and all four odd cross-state root-gcd cells are subpolynomial.

The s7-44 charged-once ledger is

```text
C choice                  : chi
primitive Gaussian (U,V) : 2phi-chi=1/4
primitive endpoint column: 1/4-chi=1/2-2phi
post-column fiber         : 0
```

with total `1/2`.

## 2. Gaussian product coordinates

Use

```text
a=c_x^+,
b=c_x^-,
D+A=aU,
D-A=bV,
gcd(U,V)=1.
```

Write

```text
g=gcd(a,b),
a=g*a0,
b=g*b0,
gcd(a0,b0)=1.
```

Merged s7-29 gives `g=B^o(1)` at the endpoint.  Define

```text
P=a0*U,
Q=b0*V.
```

Merged s7-27 gives

```text
oddpart(a*b)=oddpart(u_res).
```

Merged s7-42 gives on `theta=1/4`

```text
u_res<=B^(A(phi)+o(1)),
A(phi)=1/2-2phi,
```

while s7-29 gives

```text
U*V=B^(2phi+o(1)).
```

Therefore

```text
P*Q<=B^(1/2+o(1)).
```

## 3. Coefficient-free full-core Gaussian line

The s7-29 good core `C0=C/B^o(1)` satisfies

```text
C0 | a0^2 U^2+b0^2 V^2,
gcd(C0,a0*b0*U*V)=1.
```

Thus exactly

```text
C0 | P^2+Q^2.
```

Also

```text
P=(D+A)/g,
Q=(D-A)/g,
```

so `gcd(P,Q)` is supported on the endpoint-small factor `2*gcd(A,D)/g`; after a `B^o(1)` peel the product pair is primitive.

For each of the `B^o(1)` roots of `t^2=-1 (mod C0)`, the primitive determinant lemma gives

```text
#(P,Q)<=B^(1/2-chi+o(1)).
```

This is exactly

```text
(1/2-2phi)+(2phi-chi)=1/2-chi,
```

so it absorbs both the first residual support and the primitive `(U,V)` support without double charging.

## 4. Divisor split and physical completion

For fixed `(P,Q)`, the number of splittings

```text
P=a0*U,
Q=b0*V
```

is at most `tau(P)tau(Q)=B^o(1)`.

All coprimality, dyadic, squarefree-cell, interval and statewise-reducedness conditions only filter those splittings.  Once a split is fixed, `u_res` is fixed up to `B^o(1)` decoration.  Merged s7-42 gives

```text
RESIDUAL_TO_SINGLE_COLUMN_FIBER_MULTIPLICITY=Bo1,
```

and X13 gives post-column reciprocal completion multiplicity `B^o(1)`.

Hence

```text
fixed (C,P,Q)
=> full physical completion multiplicity = B^o(1)
```

after divisor splitting.

The square-root count is equivalently

```text
C choice                    : chi
Gaussian product root line  : 1/2-chi
physical completion         : 0
---------------------------------
total                       : 1/2.
```

## 5. Transverse rational resultant no-go

Put

```text
A_z=z1*r2*s2,
B_z=z2*r1*s1.
```

Merged s7-44 gives, for every odd `p^e||C0`,

```text
P/Q == rho_p,      rho_p^2 == -1,
A_z/B_z == sigma_p,sigma_p^2 == 1.
```

The root polynomials satisfy

```text
Res(t^2+1,t^2-1)=4.
```

Thus for every odd prime `p|C0`, neither `rho_p=sigma_p` nor `rho_p=-sigma_p` is possible.  Consequently

```text
gcd(C0,P*B_z-Q*A_z)=1,
gcd(C0,P*B_z+Q*A_z)=1.
```

The obvious rational cross determinant and cross sum therefore carry **no** part of the full good core.  They cannot supply a second determinant spacing.

Quadratic cross norms such as

```text
P^2*B_z^2+Q^2*A_z^2
```

are divisible by `C0`, but only because they are algebraic combinations of

```text
P^2+Q^2 ==0,
A_z^2-B_z^2==0  (mod C0).
```

They are not independent moduli and cannot be charged again.

## 6. Minimal receiver and H contract

The s7-44 dual-root-line Cartesian product is therefore reparameterized as

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergy.
```

For

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
```

sum over `C~B^chi` and primitive product pairs

```text
P*Q<=B^(1/2+o(1)),
C/B^o(1) | P^2+Q^2,
```

retaining only divisor splittings that admit every original physical mask and exact reciprocal completion.

The trivial complete count is `B^(1/2+o(1))`.  A strict sub-square-root theorem must establish, uniformly over the whole phi band,

```text
sum_C I_C^phys << B^(1/2-delta+o(1))
```

for some fixed `delta>0`.

Merged s7-44 already opens the correct average-incidence gate.  4dc narrows that gate and promotes it to the mainline:

```text
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=true
```

with target

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving.
```

The H audit must retain the full physical masks and must not reuse `C` as a second determinant modulus.  Suitable candidate mechanisms include genuine dispersion/large-sieve, Gaussian integer energy, or a determinant method on the physical completion subset.

The generic genus-one H is not reopened.  Merged `t80/t81/t82/tH23` remain fixed-U coefficient-space work and are not cross-promoted without an explicit bridge.

## Global ledger

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Next: `Stage14-4dd_after_H`.

## Stage boundary

```text
STAGE14_4DC=COMPLETE_GAUSSIAN_PRODUCT_ROOT_LINE_COMPRESSION_TRANSVERSE_RESULTANT_NOGO_AND_MAINLINE_H_GATE
MERGED_4DB_IMPORTED=true
MERGED_S7_44_IMPORTED=true
MERGED_S7_42_IMPORTED=true
MERGED_S7_29_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
SQRT_SATURATION_THETA=1/4
SQRT_SATURATION_PHI_RANGE=[5/24,1/4]
SQRT_SATURATION_COMMON_CORE_EXPONENT=chi=2phi-1/4
SQRT_SATURATION_GLOBAL_ODD_ROOT_PRIMITIVITY=true
SIGNED_QUOTIENT_FIRST_RESIDUAL_PRODUCT_IMPORTED=true
GAUSSIAN_PRODUCT_COORDINATES=P=a0*U,Q=b0*V
GAUSSIAN_PRODUCT_PAIR_SIZE_EXPONENT_AT_MOST=1/2
GAUSSIAN_PRODUCT_ROOT_EQUATION=P^2+Q^2=0_mod_C0
GAUSSIAN_PRODUCT_ROOT_LINE_EXPONENT=1/2-chi
PRODUCT_PAIR_TO_RESIDUAL_PRIMITIVE_SPLIT_MULTIPLICITY=Bo1
PRODUCT_PAIR_TO_SINGLE_COLUMN_MULTIPLICITY=Bo1
DUAL_ROOT_LINE_CARTESIAN_PRODUCT_REPARAMETERIZED=true
PRODUCT_ROOT_LINE_PLUS_CORE_TRIVIAL_COMPLETE_COUNT=1/2
TRANSVERSE_ROOT_POLYNOMIAL_RESULTANT=4
RATIONAL_CROSS_DETERMINANT_COPRIME_TO_FULL_GOOD_CORE=true
RATIONAL_CROSS_SUM_COPRIME_TO_FULL_GOOD_CORE=true
GAUSSIAN_CROSS_NORM_SECOND_MODULUS_ALLOWED=false
SECOND_FULL_CORE_DETERMINANT_SPACING_LEGAL=false
REMAINING_RECEIVER=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergy
S7_44_H_GATE_IMPORTED=true
S7_44_DUAL_ROOT_LINE_H_TARGET_REFINED=true
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=true
MAINLINE_H_TARGET=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving
MAINLINE_H_REQUIRED_OUTPUT=sum_C_I_C_phys<=B^(1/2-delta+o(1))_for_some_fixed_delta>0
GENERIC_GENUS_ONE_H_REOPENED=false
T80_CROSS_PROMOTED_TO_MAINLINE=false
T81_CROSS_PROMOTED_TO_MAINLINE=false
T82_CROSS_PROMOTED_TO_MAINLINE=false
TH23_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4dd_after_H
```