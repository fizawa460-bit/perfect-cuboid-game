# Stage14-4ez — fixed-ray squareclass forces a large agreement/kernel overlap

## Status

`COMPLETE_FIXED_RAY_SQUARECLASS_TO_LARGE_AGREEMENT_KERNEL_OVERLAP`

Consumes Stage14-4ey and the merged square-root saturation scales of `Stage14-4dd`, `Stage14-s7-28`, and `Stage14-s7-46`.

Let

```text
D=U*V=sf_odd(K*Z),
G:=gcd(D,K).
```

Every prime of `D/G` is absent from `K`. Since `D` is the squarefree kernel of `K*Z`, such a prime must divide `Z`. Therefore exactly

```text
D/G | rad(Z),
```

and hence

```text
G >= D/rad(Z) >= D/Z.                           (1)
```

Now use only merged equality-packet scales. Merged s7-46 gives

```text
U*V=oddpart(RJ)=B^(2phi+o(1)),
R,J=B^(phi+o(1)).
```

Merged 4dd gives

```text
P,Q=B^(1/4+o(1)),
```

and merged s7-28 gives

```text
Z=Xr*Yr=P*Q/(R*J).
```

Consequently

```text
D = B^(2phi+o(1)),
Z = B^(1/2-2phi+o(1)).
```

Substituting into (1), every square-root-saturating heavy-ray packet satisfies

```text
boxed:
G >= B^(4phi-1/2-o(1)).                           (2)
```

On the complete square-root band

```text
5/24 <= phi <= 1/4,
```

this gives the uniform fixed-power lower bound

```text
boxed:
G >= B^(1/3-o(1)).                                (3)
```

Thus radial heavy-ray saturation cannot occur through a generic fixed-kernel squareclass: the physical xi-agreement product must share a **large fixed-power divisor** with the squarefree kernel `K` of the one frozen primitive reciprocal ray.

Because `G|K` and `K` is fixed on the ray,

```text
# {possible exact G} <= tau(K)=B^o(1).
```

Hence one exact large divisor `G` may be frozen at charged-once `B^o(1)` loss on any saturating subsequence.

This is a new cross-coordinate relation between the fixed projective ray and the canonical xi-agreement allocation; it is not the old common-core Gaussian root condition and is not a reuse of the same-side/cross-root gcd savings.

```text
AGREEMENT_KERNEL_OVERLAP_G_DEFINED=true
D_OVER_G_DIVIDES_RAD_Z=true
AGREEMENT_KERNEL_OVERLAP_EXPONENT_LOWER_BOUND=4phi-1/2
UNIFORM_AGREEMENT_KERNEL_OVERLAP_LOWER_BOUND=1/3
EXACT_G_FREEZING_COST=Bo1
FRESH_CROSS_COORDINATE_OVERLAP_EXPOSED=true
RECEIVER_MATERIALLY_CHANGED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4fa
```
