# Stage14-4ex — radial square support to fixed-kernel square-value incidence

## Status

`COMPLETE_RADIAL_SQUARE_SUPPORT_TO_FIXED_KERNEL_SQUARE_VALUE_INCIDENCE`

Consumes Stage14-4ev/4ew and merged Work-boX27.

Write the moving second-reciprocal product in 4ew as

```text
T:=4*Xr*Yr*epsilon_x*U*V.
```

On the fixed primitive ray,

```text
T=(x^2-y^2) h^2.
```

Let

```text
K:=sqf(x^2-y^2),
x^2-y^2=K*t0^2
```

with `K` squarefree and `t0>=1`; both are fixed on the frozen primitive ray. Then every radial point satisfies

```text
T=K*(t0*h)^2.                                  (1)
```

Thus all accepted moving products `T` lie in one fixed squarefree-kernel class. The radial coordinate is recovered from the square part:

```text
h=sqrt(T/K)/t0,
```

when the divisibility/parity conditions hold. Hence the map

```text
h -> T
```

is injective on the fixed ray, and merged 4eq supplies only `B^o(1)` physical completion over each `T`.

The heavy-ray branch is therefore exactly a fixed-squarefree-kernel square-value incidence problem for the canonical moving product `4*Xr*Yr*epsilon_x*U*V`. Generic density of squares among integers cannot be charged because `T` is itself a structured product and may be biased toward this kernel.

```text
FIXED_RAY_SQUAREFREE_KERNEL_K_FIXED=true
RADIAL_H_TO_MOVING_PRODUCT_T_INJECTIVE=true
HEAVY_RAY_RECEIVER=FixedPrimitiveRayCanonicalReciprocalProductFixedKernelSquareValueIncidence
GENERIC_SQUARE_DENSITY_RECHARGE_ALLOWED=false
RECEIVER_MATERIALLY_CHANGED=true
NEXT_H_NEEDED=false
NEXT=Stage14-4ey
```
