# Stage14-s7-85 — fixed root-product squareclass reduces kernel diffusion to one shared squarefree overlap

## Status

`COMPLETE_ROOT_KERNEL_DIFFUSION_TO_SHARED_SQUAREFREE_OVERLAP`

Consumes batch-local `Stage14-s7-84`, merged `Stage14-s7-83`, and merged mainline `Stage14-4ex..4fa`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Freeze the root-side packet

By s7-84, after `B^o(1)` localization we may fix

```text
C,
primitive ray (x,y),
D0=x^2-y^2,
(U,V),
epsilon_x,
```

and retain the exact identity

```text
Xr*Yr = r0*h^2,
r0=D0/(4*epsilon_x*U*V)>0.
```

All physical gcd, squarefree, range, orientation and charged-once masks remain in force.

For positive root factors write uniquely

```text
|Xr|=kappa_x*a^2,
|Yr|=kappa_y*b^2,
```

with `kappa_x,kappa_y` squarefree and `a,b>=1`.

## 2. The product squareclass is fixed

Every positive rational squareclass has a unique positive squarefree integer representative.  Let

```text
K_Z
```

be the squarefree representative of the rational squareclass `[r0]` in `Q^*/Q^{*2}`.  Because multiplication by `h^2` does not change squareclass,

```text
sqf(|Xr*Yr|)=K_Z
```

for every physical radial point.

Equivalently,

```text
sqf(kappa_x*kappa_y)=K_Z.
```

This is the root-side form of the fixed-ray squareclass already present in merged 4ex; no generic square-density factor is charged.

```text
ROOT_PRODUCT_SQUAREFREE_KERNEL_FIXED=true
ROOT_PRODUCT_FIXED_KERNEL=K_Z
GENERIC_SQUARECLASS_DENSITY_RECHARGED=false
```

## 3. Exact symmetric-difference decomposition of two root kernels

Set

```text
J:=gcd(kappa_x,kappa_y),
A:=kappa_x/J,
B:=kappa_y/J.
```

Since `kappa_x,kappa_y` are squarefree,

```text
gcd(J,A*B)=1,
gcd(A,B)=1,
```

and

```text
kappa_x*kappa_y=J^2*A*B.
```

Therefore

```text
sqf(kappa_x*kappa_y)=A*B=K_Z.
```

Hence the noncommon parts `(A,B)` are merely an ordered coprime factorization of the fixed squarefree integer `K_Z`.  Their number is at most

```text
tau(K_Z)=B^o(1)
```

on every polynomial Stage14 height range.

After freezing this divisor-many split,

```text
kappa_x=J*A,
kappa_y=J*B,
A*B=K_Z,
```

and **all possible polynomial root-kernel mobility is carried by the one common squarefree overlap `J`**.

```text
ROOT_KERNEL_NONCOMMON_SPLIT_COST=Bo1
ROOT_KERNEL_DIFFUSION_ONLY_THROUGH_SHARED_OVERLAP_J=true
SHARED_ROOT_KERNEL_OVERLAP_J_SQUAREFREE=true
```

## 4. Interpretation of the s7-83 diffuse-kernel branch

Merged s7-83 branch A allowed polynomially many kernels for one selected root factor.  The present exact decomposition shows that those kernels cannot diffuse independently of the complementary root factor.  Up to a `B^o(1)` fixed split `(A,B)`, they move in lockstep through

```text
(kappa_x,kappa_y)=(J*A,J*B).
```

Thus a kernel-diffuse s packet is a **shared-overlap correlation**, not a one-factor squarefree-density problem.

No fixed-power saving follows from squarefreeness of `J`; generic squarefree support is positive-density and has already been accounted for.

```text
ONE_FACTOR_KERNEL_INDEPENDENCE_ASSUMED=false
GENERIC_SQUAREFREE_J_SAVING_CLAIMED=false
```

## 5. Receiver and H decision

The factor-specific coefficient system is now explicit enough to expose one exact common overlap `J`, but the square parts `(a,b)` and the radial coordinate `h` have not yet been combined with it.  Thus no external theorem is required yet.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_85_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

The next stage should substitute

```text
|Xr|=J*A*a^2,
|Yr|=J*B*b^2
```

into the exact root-product/radial identity and compare the resulting multiplicative fiber with the short `h` support of merged 4fa.

## Boundary

```text
STAGE14_S7_85=COMPLETE_ROOT_KERNEL_DIFFUSION_TO_SHARED_SQUAREFREE_OVERLAP
ROOT_PRODUCT_SQUAREFREE_KERNEL_FIXED=true
ROOT_KERNEL_NONCOMMON_SPLIT_COST=Bo1
ROOT_KERNEL_DIFFUSION_ONLY_THROUGH_SHARED_OVERLAP_J=true
ONE_FACTOR_KERNEL_INDEPENDENCE_ASSUMED=false
GENERIC_SQUAREFREE_J_SAVING_CLAIMED=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_85_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-86
```
