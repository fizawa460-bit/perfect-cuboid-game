# Stage14-s7-78 — heavy primitive reciprocal ray to fixed primitive norm-factor packet

## Status

`COMPLETE_HEAVY_PRIMITIVE_RECIPROCAL_RAY_TO_FIXED_PRIMITIVE_NORM_FACTOR_PACKET`

Consumes merged `Stage14-s7-75..77`, merged mainline `Stage14-4el..4ep`, merged `Stage14-Work-bnX26`, and latest main at batch start `2fd569305e0f8c1dc1acafe1c3b7a3c635aec0e4`. Unmerged descendants are advisory only.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Routing after merged 4el..4ep

Merged mainline now separates the polynomial-common-core obstruction into three pieces in addition to the low-core allocation gate:

```text
heavy primitive reciprocal ray,
separated genuine determinant mover,
diffuse primitive Gaussian norm-factor correlation.
```

The genuine-mover branch has already reached the mover-only auxiliary target

```text
FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
```

and merged 4en closes its near-maximal quotient subbranch. No positive mover-H result is merged, so the s route does not cross-promote a saving there.

Merged 4ep rewrites the diffuse branch as

```text
X0^2+Y0^2=C*m
```

with divisor/representation fibers already charged once.

The present stage therefore works only on the still-internal heavy-ray branch

```text
ConcentratedExactCommonCoreHeavyPrimitiveReciprocalRayIncidence.
```

```text
MERGED_4EL_4EP_CONSUMED=true
MOVER_H_RESULT_CONSUMED=false
HEAVY_RAY_INTERNAL_BRANCH_SELECTED=true
```

## 2. A primitive projective ray fixes the primitive vector up to O(1)

Fix one exact polynomial common-core modulus `C` and one primitive reciprocal projective ray `r` supplied by merged s7-77. Every candidate on this heavy ray has primitive vector

```text
v0(z)=(X0(z),Y0(z)),
gcd(X0,Y0)=1.
```

If two primitive integer vectors lie on the same rational ray, they agree up to the already-frozen finite sign/unit convention. Hence after freezing that O(1) label there is one primitive pair

```text
(x,y),
gcd(x,y)=1,
```

such that every incidence on the heavy ray has

```text
(X0,Y0)=(x,y).
```

Thus the heavy multiplicity is not multiplicity of projective scalings of the primitive vector itself.

```text
HEAVY_RAY_PRIMITIVE_VECTOR_FIXED_UP_TO_O1=true
PRIMITIVE_VECTOR_SCALING_MULTIPLICITY_AVAILABLE=false
```

## 3. The primitive Gaussian norm and complementary quotient are fixed

Every accepted reciprocal candidate on this exact modulus satisfies

```text
C | X0^2+Y0^2.
```

On the fixed heavy primitive ray define

```text
N0:=x^2+y^2,
m0:=N0/C.
```

Then `N0` and `m0` are fixed integers for the entire heavy-ray packet and

```text
N0=C*m0.
```

Consequently the heavy-ray branch is stronger than the diffuse 4ep norm-factor receiver: not only the modulus but also the primitive norm value and its complementary quotient are frozen.

```text
HEAVY_RAY_PRIMITIVE_NORM_VALUE_FIXED=true
HEAVY_RAY_COMPLEMENTARY_NORM_QUOTIENT_FIXED=true
HEAVY_RAY_NORM_FACTOR_EQUATION=N0_equals_C_times_m0
```

No saving follows merely from this identity; `C|N0` is the already-selected reciprocal root condition.

## 4. What can still vary

Merged s7-70 obtained `(X0,Y0)` by peeling the common integer scale from the unprimitive opposite-reciprocal vector. Write

```text
X=h*x,
Y=h*y,
h>=1,
```

where the charged common-core overlap with `C` has already been peeled to the allowed subpolynomial support. The exact radial scale `h` is not known to be `B^o(1)` and is not fixed by the primitive ray.

Before primitive peeling the signed factorization is

```text
X=p*c,
Y=q*d,
```

with `(p,q,c,d)` reconstructed from the same canonical physical witness. Hence every heavy-ray candidate satisfies

```text
p*c=h*x,
q*d=h*y.
```

The possible polynomial multiplicity has therefore moved entirely into

```text
radial scale h
+
divisor factorization of h*x and h*y
+
upstream canonical-allocation/background reverse fibers.
```

```text
HEAVY_RAY_UNPRIMITIVE_VECTOR_IS_RADIAL_DILATION=true
RADIAL_SCALE_H_SUBPOLYNOMIAL_BOUND_PROVED=false
```

## 5. Receiver and H decision

This is an internal normalization of the heavy-ray branch, not yet a material receiver change. The next stage should charge the divisor factorizations correctly and determine whether polynomial multiplicity can come from factorization choices or must persist in the radial/upstream background coordinate.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_78_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_78=COMPLETE_HEAVY_PRIMITIVE_RECIPROCAL_RAY_TO_FIXED_PRIMITIVE_NORM_FACTOR_PACKET
MERGED_4EL_4EP_CONSUMED=true
HEAVY_RAY_PRIMITIVE_VECTOR_FIXED_UP_TO_O1=true
HEAVY_RAY_PRIMITIVE_NORM_VALUE_FIXED=true
HEAVY_RAY_COMPLEMENTARY_NORM_QUOTIENT_FIXED=true
HEAVY_RAY_UNPRIMITIVE_VECTOR_IS_RADIAL_DILATION=true
RADIAL_SCALE_H_SUBPOLYNOMIAL_BOUND_PROVED=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_78_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-79
```