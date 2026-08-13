# Stage14-4fa — large fixed-ray overlap collapses the agreement-pair fiber

## Status

`COMPLETE_LARGE_FIXED_RAY_OVERLAP_AGREEMENT_FIBER_COMPRESSION`

Consumes Stage14-4ey/4ez and merged `Stage14-s7-29` primitive common-core root-line counting.

Freeze one exact heavy-ray packet

```text
C,
K,
G|K,
G=gcd(UV,K),
G>=B^(4phi-1/2-o(1)).
```

Stage14-4ez proves that the exact choice of `G` costs only `B^o(1)`. Since

```text
U*V=D
```

is squarefree and `gcd(U,V)=1`, write uniquely

```text
G_U=gcd(G,U),
G_V=gcd(G,V),
G=G_U*G_V,
U=G_U*u,
V=G_V*v.
```

The number of possible allocations `(G_U,G_V)` is at most `tau(G)=B^o(1)`.

Merged s7-29 gives, after its endpoint-small coefficient peel,

```text
C0 | a0^2 U^2+b0^2 V^2,
gcd(C0,a0*b0*U*V)=1,
C0=C*B^o(1)^(-1).
```

In particular `G` is a unit modulo `C0`. Substitution gives another primitive Gaussian root-line equation

```text
C0 | (a0*G_U)^2 u^2+(b0*G_V)^2 v^2,
gcd(u,v)=1,
```

with unit coefficients. The charged-once primitive determinant/root-line lemma therefore gives

```text
# {(u,v) on one fixed root line}
 <= B^o(1) * (1 + (u*v)/C0).
```

On square-root saturation,

```text
U*V=B^(2phi+o(1)),
C0=B^(chi+o(1)),
chi=2phi-1/4,
G=B^(g+o(1)),
g>=4phi-1/2.
```

Hence

```text
(u*v)/C0
 = B^(2phi-g-chi+o(1))
 = B^(1/4-g+o(1)).
```

Since merged 4ez gives uniformly `g>=1/3-o(1)`, the exponent `1/4-g` is strictly negative. Therefore

```text
boxed:
fixed (C,K,G,G_U,G_V, coefficient/root label)
 => #(U,V)=B^o(1).                              (1)
```

This is a conditional fiber compression using the **new fixed large divisor `G`**. It must not be multiplied as an independent second use of the old common-core root-line density.

Now fix one of the `B^o(1)` surviving agreement pairs. The exact 4ex square-value identity reads

```text
h^2*(x^2-y^2)
 = 4*epsilon_x*(Xr*Yr)*U*V.
```

All factors except `h` and `Z=Xr*Yr` are fixed. Merged square-root scales give

```text
Z=B^(1/2-2phi+o(1)).
```

Thus the number of exact radial scales on this fixed agreement fiber is at most

```text
#h <= B^(1/4-phi+o(1)) <= B^(1/24+o(1)).          (2)
```

Merged 4eq gives only `B^o(1)` physical reverse multiplicity for each exact `h`.

Equation (1) removes the polynomial primitive-agreement-pair freedom from the heavy-ray branch. Equation (2) leaves only a short one-dimensional radial square-scale support. We do **not** claim that the `1/24` bound is already a fixed-power deficit relative to the concentrated exact-`C` mass `M_C`; the merged collision-energy route records only `M_C=B^(eta+o(1))` for some `eta>0`, not a uniform lower bound `eta>1/24`.

Therefore the correct new receiver is

```text
FixedPrimitiveRayFixedAgreementPairShortRadialSquareScalePhysicalIncidence.
```

This is a material receiver change and ends the current batch under the batch contract.

```text
FIXED_LARGE_G_ALLOCATION_COST=Bo1
LARGE_G_COMMON_CORE_ROOT_LINE_FIBER=Bo1
HEAVY_RAY_PRIMITIVE_AGREEMENT_PAIR_POLYNOMIAL_FREEDOM_REMOVED=true
FIXED_AGREEMENT_RADIAL_SCALE_COUNT_MAX=B^(1/4-phi+o(1))
UNIFORM_FIXED_AGREEMENT_RADIAL_SCALE_COUNT_MAX=B^(1/24+o(1))
HEAVY_RAY_CLOSED=false
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairShortRadialSquareScalePhysicalIncidence
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4fb
```
