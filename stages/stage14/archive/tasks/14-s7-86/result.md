# Stage14-s7-86 — shared root overlap and square parts collapse to a divisor-many fiber over the short radial scale

## Status

`COMPLETE_ROOT_OVERLAP_SQUAREPART_MOBILITY_TO_SHORT_RADIAL_FACTORIZATION_CAPACITY`

Consumes batch-local `Stage14-s7-84/85`, merged mainline `Stage14-4fa`, and merged `Stage14-Work-bpX28`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exact root-side normal form

After the `B^o(1)` localizations of s7-84/85, fix

```text
D0=x^2-y^2>0,
(U,V),
epsilon_x,
K_Z,
A*B=K_Z,
```

with `(A,B)` one ordered coprime factorization of the fixed squarefree kernel `K_Z`.

Every surviving root packet has

```text
|Xr|=J*A*a^2,
|Yr|=J*B*b^2,
```

where `J` is squarefree, `gcd(J,K_Z)=1`, and `a,b>=1`.  Consequently

```text
|Xr*Yr|
 = J^2*A*B*a^2*b^2
 = K_Z*(J*a*b)^2.                              (1)
```

## 2. Compare with the exact radial identity

Stage14-s7-84 retained

```text
|Xr*Yr|=r0*h^2,
r0=D0/(4*|U*V|)>0
```

after freezing the finite sign convention.

By definition of `K_Z`, the positive rational number

```text
r0/K_Z
```

is a rational square.  Choose fixed coprime positive integers `c0,d0` such that

```text
r0/K_Z=(c0/d0)^2.
```

Combining this with (1) gives the exact positive equality

```text
K_Z*(J*a*b)^2
 = K_Z*(c0*h/d0)^2.
```

Therefore

```text
boxed:
d0*J*a*b = c0*h.                              (2)
```

The coefficients `c0,d0` depend only on the already-frozen heavy-ray/agreement packet.  They may be polynomially large, but are fixed while the radial packet is counted.

```text
ROOT_OVERLAP_SQUAREPART_RADIAL_EQUATION=d0_J_a_b_equals_c0_h
FIXED_COEFFICIENT_RATIONAL_SQUARE_PEELED=true
```

## 3. For one exact h, root kernel/square-part choices are divisor-many

Fix one exact admissible `h`.  Equation (2) implies

```text
J*a*b | c0*h
```

up to the fixed divisibility requirement by `d0`.  Ignoring the additional squarefree, gcd, orientation and physical range filters only enlarges the count.  Thus

```text
# {(J,a,b): d0*J*a*b=c0*h}
 <= d_3(c0*h)
 = B^o(1)
```

uniformly on the polynomial Stage14 height range.

Hence neither

```text
moving shared kernel J
```

nor

```text
fixed-kernel square-part mobility a or b
```

is an additional polynomial coordinate after exact `h` is fixed.  The two branches of merged s7-83 recombine as divisor factorizations of the same short radial coordinate.

```text
FIXED_H_ROOT_OVERLAP_SQUAREPART_FIBER=Bo1
S7_83_KERNEL_AND_SQUAREPART_BRANCHES_RECOMBINE_OVER_H=true
ROOT_FACTOR_MOBILITY_INDEPENDENT_OF_H=false
```

## 4. Import the short radial support capacity

Merged 4fa proves, after the same fixed agreement localization,

```text
#h <= B^(1/4-phi+o(1))
   <= B^(1/24+o(1)).
```

Merged 4eq gives only `B^o(1)` full physical reverse multiplicity per exact `h`.  The new divisor-many root factorization of Section 3 does not change that exponent.

Therefore the full heavy-ray s packet above one fixed primitive ray/agreement packet has support capacity

```text
<= B^(1/24+o(1))
```

at the level of the remaining radial/root coordinates.

This is precisely the support side of the merged Work-bpX28 capacity inequality.  It does **not** close the heavy-ray branch because the concentrated exact-`C` ledger only guarantees a required mass exponent

```text
eta>0
```

without a merged uniform lower bound `eta>1/24`.

```text
S_ROUTE_HEAVY_RAY_SUPPORT_CAPACITY_EXPONENT_MAX=1/24
UNIFORM_REQUIRED_HEAVY_RAY_MASS_EXPONENT_GT_1_24_PROVED=false
HEAVY_RAY_CLOSED=false
```

## 5. Material receiver change

The s7-83 factor-level dichotomy

```text
DiffusePhysicalFactorSquarefreeKernelCorrelation
OR FixedFactorKernelPolynomialSquarePartPhysicalIncidence
```

is no longer minimal.  After consuming merged agreement compression and the exact root-product identity, both are divisor-many fibers above one short radial coordinate.

The minimal s heavy-ray receiver is now the same charged-once mass-capacity obstruction isolated by merged Work-bpX28:

```text
FixedPrimitiveRayFixedAgreementPairShortRadialScaleMassCapacityGap.
```

The unresolved datum is quantitative: compare the required heavy-ray mass exponent `eta` with the uniform support capacity `1/24`, or sharpen the atomic/support bound without recharging fixed-h reconstruction.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairShortRadialScaleMassCapacityGap
RECEIVER_MATERIALLY_CHANGED=true
```

## 6. H decision

No new `sH` is justified.  The current obstruction is not yet an external theorem contract; it is a missing internal exponent comparison in the already-merged collision ledger.

```text
S7_86_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

The next s stage should audit the concentrated exact-`C` collision-energy bookkeeping for a uniform lower bound on the required mass exponent `eta`, and compare it directly with `1/24`.  If no such lower bound follows, it should freeze the exact atomic-capacity obstruction instead of assuming one.

## Boundary

```text
STAGE14_S7_86=COMPLETE_ROOT_OVERLAP_SQUAREPART_MOBILITY_TO_SHORT_RADIAL_FACTORIZATION_CAPACITY
ROOT_OVERLAP_SQUAREPART_RADIAL_EQUATION=d0_J_a_b_equals_c0_h
FIXED_H_ROOT_OVERLAP_SQUAREPART_FIBER=Bo1
S7_83_KERNEL_AND_SQUAREPART_BRANCHES_RECOMBINE_OVER_H=true
S_ROUTE_HEAVY_RAY_SUPPORT_CAPACITY_EXPONENT_MAX=1/24
UNIFORM_REQUIRED_HEAVY_RAY_MASS_EXPONENT_GT_1_24_PROVED=false
HEAVY_RAY_CLOSED=false
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairShortRadialScaleMassCapacityGap
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_86_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-87
```
