# Stage14-4gd — open the pair completion Boolean as an exact reciprocal divisor/CRT system

## Status

`COMPLETE_PAIR_COMPLETION_BOOLEAN_TO_EXACT_RECIPROCAL_DIVISOR_CRT_SYSTEM`

Consumes batch-local `Stage14-4gc`, merged `Stage14-4eq`, merged `Stage14-X13`, and merged fixed-ray/agreement reductions through `Stage14-4fa/4fg`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Fixed coefficients on one pair packet

Freeze the exact `B^o(1)` packet labels already charged by the merged route, including

```text
primitive reciprocal ray (x,y),
primitive xi-agreement pair (U,V), gcd(U,V)=1,
E=E0,
d0,
endpoint-small r,s,
epsilon_x,epsilon_k,
finite orientation/two-primary chart data.
```

For `(u,v) in R_prim` from 4gc, put

```text
m=u*v,
n=E0*m,
H0=d0*E0,
h=H0*m.
```

The fixed reciprocal-ray coordinates are then

```text
Xrec=h*x=H0*x*m,
Yrec=h*y=H0*y*m.                                   (1)
```

Merged 4fw/4fg gives the physical root products

```text
|Xr|=alpha*E0*u^2,
|Yr|=beta*E0*v^2                                  (2)
```

for fixed packet coefficients `alpha,beta`.

The second reciprocal identity

```text
Xrec^2-Yrec^2
 =4*epsilon_x*Xr*Yr*U*V                           (3)
```

introduces no new `(u,v)` selector on this normalized packet.  Substituting (1)--(2), both sides are `(u*v)^2` times fixed coefficients, and the coefficient equality is exactly the already-frozen fixed-ray square-value identity inherited from 4fa/4fg.  Thus (3) is a consistency identity of the coordinate construction, not a fresh density condition.

```text
SECOND_RECIPROCAL_IDENTITY_PAIR_DEPENDENT_DEFICIT=0
SECOND_RECIPROCAL_IDENTITY_RECHARGED=false
```

## 2. First divisor layer: factor the two reciprocal products

Use the X13 signed notation

```text
Xrec=p*c,
Yrec=q*d.
```

For fixed `(u,v)`, every candidate is obtained by choosing

```text
p | Xrec,
q | Yrec,
```

and setting

```text
c=Xrec/p,
d=Yrec/q.                                         (4)
```

The number of such first-layer choices is bounded by

```text
tau(Xrec)*tau(Yrec)=B^o(1).                        (5)
```

All quotient-cell, sign and finite orientation restrictions are filters on these divisor choices; they do not enlarge (5).

## 3. Second divisor layer: the first reciprocal difference of squares

For a first-layer choice `(p,q,c,d)`, define

```text
W1:=4*r*s*epsilon_k*p*q.                           (6)
```

A physical reverse completion requires positive integers `a,b` satisfying

```text
(a*U)^2-(b*V)^2=W1.                                (7)
```

Factor (7) exactly as

```text
F_-:=a*U-b*V=2*A,
F_+:=a*U+b*V=2*D,
F_-*F_+=W1,
0<F_-<F_+.                                         (8)
```

Conversely, a positive factor pair `(F_-,F_+)` of `W1` reconstructs

```text
a=(F_++F_-)/(2*U),
b=(F_+-F_-)/(2*V).                                 (9)
```

Thus integrality is equivalent to the exact fixed-modulus congruences

```text
F_+ + F_- == 0 (mod 2*U),
F_+ - F_- == 0 (mod 2*V),                          (10)
```

with positivity and the inherited endpoint conditions, including the required divisibilities of

```text
A=F_-/2,
D=F_+/2
```

by the frozen endpoint-small labels, imposed as filters.

For each `(p,q)`, the number of factor pairs in (8) is at most

```text
tau(W1)=B^o(1).                                    (11)
```

## 4. Exact bare reciprocal candidate set

Define `Omega_rec(u,v)` to be the set of tuples

```text
omega=(p,q,c,d,F_-,F_+,a,b)
```

satisfying (4), (6), (8)--(10), positivity, parity and the endpoint-small divisibility filters, but **not** yet imposing the remaining Stage14 root-origin, canonical allocation/orientation, labelled cell/switch, reverse/post-column completion masks.

Equations (5) and (11) give uniformly

```text
#Omega_rec(u,v)=B^o(1).                             (12)
```

For `omega in Omega_rec(u,v)`, let

```text
R_post(u,v;omega) in {0,1}
```

be the exact conjunction of every retained physical condition not already used in defining `Omega_rec`, including root-origin/cell realization, canonical allocation/orientation and post-column physical reconstruction.

Then the pair completion Boolean from 4gc is exactly

```text
C_pair(u,v)=1
 iff
exists omega in Omega_rec(u,v) with R_post(u,v;omega)=1.   (13)
```

No independence is asserted in (13), and no physical mask is dropped.

```text
EXACT_RECIPROCAL_DIVISOR_CRT_CANDIDATE_SET_DEFINED=true
FIXED_PAIR_BARE_RECIPROCAL_CANDIDATE_FIBER=Bo1
PAIR_COMPLETION_BOOLEAN_EXACTLY_RECIPROCAL_CANDIDATE_PLUS_POST_MASK=true
```

## 5. Square-valued reconstructed column parameter

The same substitution also makes the X13 reconstructed column parameter explicit.  Since

```text
M=4*r*s*Xr*Yr*epsilon_x*epsilon_k,
```

(2) gives

```text
M=M0*m^2,
M0:=4*r*s*alpha*beta*E0^2*epsilon_x*epsilon_k,      (14)
```

with `M0` fixed on the packet.  Thus the completion problem is not a generic moving-column family: it is X13 reverse reconstruction along one fixed square class `M0*m^2`.

This observation does not by itself prove a density loss; it identifies the exact arithmetic species that the next stage will place into a nested-support exponent ledger.

```text
X13_COLUMN_PARAMETER_FIXED_SQUARE_CLASS_M0_TIMES_m2=true
GENERIC_MOVING_COLUMN_ENTROPY_RECHARGED=false
```

## 6. H decision

No new heavy H is opened yet.  Before an external theorem audit, the reciprocal candidate existence support and the residual post-mask support must be separated at exponent level so that any theorem is compared against the actual capacity headroom `kappa-mu`.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4ge
```

## Boundary

```text
STAGE14_4GD=COMPLETE_PAIR_COMPLETION_BOOLEAN_TO_EXACT_RECIPROCAL_DIVISOR_CRT_SYSTEM
SECOND_RECIPROCAL_IDENTITY_PAIR_DEPENDENT_DEFICIT=0
EXACT_RECIPROCAL_DIVISOR_CRT_CANDIDATE_SET_DEFINED=true
FIXED_PAIR_BARE_RECIPROCAL_CANDIDATE_FIBER=Bo1
PAIR_COMPLETION_BOOLEAN_EXACTLY_RECIPROCAL_CANDIDATE_PLUS_POST_MASK=true
X13_COLUMN_PARAMETER_FIXED_SQUARE_CLASS_M0_TIMES_m2=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4ge
```