# Stage14-s7-111 — consume Work-byX37 and put all s heavy realizations on exact pre-completion candidate coordinates

## Status

`COMPLETE_GLOBAL_S_COMPLETION_ONLY_CONSOLIDATION_AND_EXACT_PRECOMPLETION_RECONSTRUCTION`

Consumes merged `Stage14-s7-108..110`, merged mainline through `Stage14-4gb`, merged q16 only on its certified fixed-E ambient rectangle, and merged `Stage14-Work-byX37` from batch-start main

```text
a0c01e4f1236e2a3c1f718f056fee6d4f1c73e20.
```

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Consume the ambient multiplicative-compression exhaustion once

Merged Work-byX37 proves that the fibered multiplication map

```text
Phi(E,d,v)=(E,dv)
```

has output fibers of size at most `tau(m)=B^o(1)` at polynomial Stage14 height. Together with merged 4fz/4ga/4gb this removes, at fixed-power scale,

```text
- fixed-E distinct-product compression,
- fixed-E unitary/coprime recovery,
- polynomial-E fibered ordinary distinct-product compression.
```

No one of those mechanisms is charged again on the s route.

Thus the four live heavy realizations are completion/lift receivers only:

```text
(A) fixed-E primitive endpoint:
    one-dimensional conditional physical completion;

(B) fixed-E two-sided principal rectangle:
    conditional canonical/reverse physical completion
    with ambient-capacity headroom;

(C) polynomial-E fixed primitive product:
    one-dimensional conditional physical completion;

(D) polynomial-E polynomial primitive product:
    conditional physical lift inside a full-exponent fibered ambient support.
```

```text
WORK_BYX37_CONSUMED=true
S_AMBIENT_MULTIPLICATIVE_COMPRESSION_RECHARGED=false
S_ALL_FOUR_HEAVY_REALIZATIONS_COMPLETION_ONLY=true
```

## 2. Exact common pre-completion coordinates

All four realizations are restrictions of the exact normalized primitive-ratio coordinates

```text
E=J1*g^2,
J1=sqf(E),
n=E*u*v,
gcd(u,v)=1,
L=E*u^2,
|Xr|=alpha*E*u^2,
|Yr|=beta*E*v^2,
h=d0*E*u*v.
```

The already-frozen coefficient-allocation packet gives

```text
J=c_J*J1,
a1=g*u,
b1=g*v,
a=c_a*a1,
b=c_b*b1,
```

with the corresponding fixed packet coefficients in `alpha,beta,c_J,c_a,c_b,d0`.

The branch specializations are only freezes of these coordinates:

```text
(A) E=E0 and one primitive side is frozen/subpolynomial;
(B) E=E0 and both primitive sides lie on the surviving principal rectangle;
(C) (m,u,v)=(m0,u0,v0) is frozen while E moves;
(D) E and m=u*v both move on a principal fibered cell.
```

For every exact candidate in any branch, the tuple

```text
(E,J1,g,u,v,n,L,J,a1,b1,a,b,h,|Xr|,|Yr|)
```

is therefore determined by the candidate and already-frozen packet data before any reverse/post-column extension is requested.

```text
PRECOMPLETION_NORMALIZED_RECONSTRUCTION_EXACT=true
PRECOMPLETION_RECONSTRUCTION_MULTIPLICITY=1
FROZEN_PACKET_LABELS_RECHARGED=false
```

This reconstruction statement is algebraic. It does not assert that the reconstructed candidate is physically completable.

## 3. Define the exact completion Boolean on the reconstructed candidate

Let `chi` denote one exact reconstructed pre-completion candidate. Define

```text
C_phys(chi)=1
```

iff `chi` passes every still-live physical condition, including every canonical/root-origin/allocation/parity condition not already forced and the required reverse/post-column completion condition.

Merged 4fk and s7-97 prove that this Boolean cannot be replaced by an unrestricted arithmetic density, and merged Work-byX37 proves only that ambient multiplicative representation fibers are `B^o(1)`.

Hence the heavy support in every branch is exactly a subset selected by `C_phys` from its already-charged pre-completion candidate support.

```text
EXACT_PHYSICAL_COMPLETION_BOOLEAN_DEFINED=true
PHYSICAL_COMPLETION_EXISTENCE_AUTOMATIC=false
COMPLETION_BOOLEAN_REPLACED_BY_GENERIC_DENSITY=false
```

## 4. Receiver and H decision

This stage synchronizes all four branches to one exact candidate language but does not yet change the minimal receiver: the Boolean `C_phys` is still bundled.

The next stage must separate predicates whose truth is already determined by the reconstructed pre-completion tuple from predicates that genuinely quantify over additional reverse/post-column completion variables. That split must be logical, not probabilistic.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_111_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-112
```

## Boundary

```text
STAGE14_S7_111=COMPLETE_GLOBAL_S_COMPLETION_ONLY_CONSOLIDATION_AND_EXACT_PRECOMPLETION_RECONSTRUCTION
WORK_BYX37_CONSUMED=true
S_ALL_FOUR_HEAVY_REALIZATIONS_COMPLETION_ONLY=true
PRECOMPLETION_NORMALIZED_RECONSTRUCTION_EXACT=true
EXACT_PHYSICAL_COMPLETION_BOOLEAN_DEFINED=true
PHYSICAL_COMPLETION_EXISTENCE_AUTOMATIC=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_111_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-112
```