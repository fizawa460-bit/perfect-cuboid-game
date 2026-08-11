# Stage14-4eq — close the concentrated heavy primitive-ray branch by reverse finite fiber

## Status

`COMPLETE_HEAVY_PRIMITIVE_RAY_REVERSE_MULTIPLICITY_CLOSURE`

Consumes merged `Stage14-4ep`, merged `Stage14-s7-75..77`, merged `Stage14-s7-31`, merged `Stage14-s7-42`, merged `Stage14-X13`, merged `Stage14-4dd/4de`, and latest main

```text
2fd569305e0f8c1dc1acafe1c3b7a3c635aec0e4.
```

Unmerged descendants are advisory only.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering heavy-ray survivor

Merged s7-77 and 4el retain, on one concentrated exact polynomial common-core modulus `C`, the possible survivor

```text
ConcentratedExactCommonCoreHeavyPrimitiveReciprocalRayIncidence.
```

Write the opposite reciprocal signed products as

```text
X := Q_xi+P_xi = c p,
Y := Q_xi-P_xi = d q,
```

with `X>Y>0`.  Let

```text
h := gcd(X,Y),
X=h X0,
Y=h Y0,
gcd(X0,Y0)=1.
```

The primitive ray is the projective vector `(X0:Y0)`.

## 2. The radial gcd is already subpolynomial on every square-root packet

Exactly

```text
gcd(Q_xi+P_xi,Q_xi-P_xi) | 2*gcd(P_xi,Q_xi).
```

Merged s7-31 identifies the odd common divisor of the physical pair `(P_xi,Q_xi)` with the cross-root common scale: every common odd prime is carried by one of the two cross-root cells.  Merged s7-42 and the equality refinement 4dd force that cross-root scale to satisfy

```text
H=B^o(1)
```

on every possible square-root-saturating sequence.  The standard frozen 2-primary convention contributes only `B^o(1)`.

Therefore

```text
h=B^o(1).
```

In particular, for one fixed primitive ray, the raw signed-product vector `(X,Y)` has only `B^o(1)` possible radial scales.

```text
OPPOSITE_RECIPROCAL_RAW_RADIAL_GCD=Bo1
HEAVY_RAY_POLYNOMIAL_RADIAL_DILATION_AVAILABLE=false
```

## 3. A fixed raw signed-product vector has only divisor-many reciprocal data

Fix `(X,Y)`.  Since

```text
X=c p,
Y=d q,
```

the possible positive factorizations `(c,p,d,q)` are bounded by

```text
tau(X) tau(Y)=B^o(1).
```

Now use the exact second reciprocal difference of squares from merged X13:

```text
(c p)^2-(d q)^2
 = 4 X_root Y_root epsilon_x U V.
```

The left side

```text
W2:=X^2-Y^2>0
```

is fixed.  Hence every positive physical tuple `(X_root,Y_root,U,V)` is a factorization of the fixed polynomially bounded integer `W2/4` up to the finite 2-primary decoration.  The total number of such tuples is therefore `B^o(1)`.

The endpoint-small factors `(r,s)` and finite `epsilon_k` then give only `B^o(1)` possibilities for the X13 column numerator

```text
M=4 r s X_root Y_root epsilon_x epsilon_k.
```

Thus

```text
fixed (X,Y)
 => # {(U,V,M)}=B^o(1).
```

## 4. Invoke the merged X13 reverse reciprocal theorem in its legal direction

Merged X13 proves

```text
fixed (U,V,M)
 => # {(a,b,c,d,p,q) and full post-column physical reconstruction}=B^o(1).
```

Combining Sections 2 and 3 with X13 gives

```text
fixed primitive ray (X0:Y0)
 => full physical packet multiplicity = B^o(1)
```

on the square-root equality family.  Fixing the exact common-core modulus `C` can only decrease this fiber.

Therefore the global primitive-ray multiplicity left open by s7-76/77 is now bounded:

```text
GLOBAL_PRIMITIVE_RAY_MULTIPLICITY_BOUND=Bo1
HEAVY_PRIMITIVE_RAY_REVERSE_FIBER=Bo1
```

## 5. Heavy-ray energy cannot saturate

For one concentrated exact modulus let `M_C` be the polynomial candidate mass and `m_C(r)` the primitive-ray multiplicity.  Section 4 gives

```text
m_max(C)=B^o(1).
```

Hence the repeated-ray pair mass satisfies

```text
K_ray(C)
 <= m_max(C) M_C
 <= M_C B^o(1),
```

whereas merged s7-77 requires quadratic-scale pair mass

```text
M_C^2 B^(-o(1))
```

for a heavy-ray saturation mechanism.  Since `M_C=B^(mu+o(1))` with fixed `mu>0` on a concentrated saturating cell, these are incompatible.

```text
HEAVY_PRIMITIVE_RAY_BRANCH_CLOSED=true
CONCENTRATED_SATURATION_MUST_USE_GENUINE_MOVER_BRANCH=true
```

The mover-only H target frozen at 4eo is untouched.

## Boundary

```text
STAGE14_4EQ=COMPLETE_HEAVY_PRIMITIVE_RAY_REVERSE_MULTIPLICITY_CLOSURE
OPPOSITE_RECIPROCAL_RAW_RADIAL_GCD=Bo1
HEAVY_RAY_POLYNOMIAL_RADIAL_DILATION_AVAILABLE=false
HEAVY_PRIMITIVE_RAY_REVERSE_FIBER=Bo1
GLOBAL_PRIMITIVE_RAY_MULTIPLICITY_BOUND=Bo1
HEAVY_PRIMITIVE_RAY_BRANCH_CLOSED=true
CONCENTRATED_SATURATION_MUST_USE_GENUINE_MOVER_BRANCH=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4er
```
