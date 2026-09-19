# MB104 Z3 — surviving-768 all-formal null-neighborhood vanishing — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT FORMAL-PICARD NO-GO / NO CREDIT**

## Input

For the surviving balanced support

```text
000707000f0f,
```

let

```text
U=A union B
```

be the union of its two zero-pairing elliptic quartics.

Retained exact geometry:

```text
A^2=B^2=-4,
A.B=2,
A and B meet transversely at two smooth points p,q.
```

Z33G proves

```text
O_U(P) ~= O_U.
```

Z37 computes the only potentially nontrivial first-normal cycle class and obtains

```text
O_{2U}(P) ~= O_{2U}.
```

This note shows that no higher finite formal-neighborhood obstruction can reappear.

## 1. Higher infinitesimal kernels

For n>=1,

```text
I_U^n/I_U^(n+1) ~= O_U(-nU).
```

Set

```text
L_n=O_U(-nU).
```

On either elliptic component,

```text
deg(L_n|A)
 = -n U.A
 = -n(A^2+A.B)
 = 2n,

deg(L_n|B)=2n.
```

Hence

```text
H^1(A,L_n|A)=H^1(B,L_n|B)=0
```

for every n>=1.

## 2. Normalization exact sequence

Normalize U at the two transverse intersection points.  For L_n,

```text
0 -> L_n
  -> L_n|A direct_sum L_n|B
  -> (L_n)_p direct_sum (L_n)_q
  -> 0.
```

Thus H^1(U,L_n) is the cokernel of the two-point evaluation map.

For n>=2,

```text
deg(L_n|A(-p-q))=2n-2 >=2.
```

On an elliptic curve a positive-degree line bundle has H^1=0.  Therefore

```text
H^1(A,L_n|A(-p-q))=0,
```

so

```text
H^0(A,L_n|A) -> (L_n)_p direct_sum (L_n)_q
```

is already surjective.  Consequently the full normalization evaluation is surjective and

```text
H^1(U,O_U(-nU))=0,  n>=2.                    (FORMAL-H1)
```

The exceptional case is exactly n=1, where the component degree after subtracting p+q is zero.
That is precisely the first-normal interface isolated by Z33H and explicitly killed by Z37.

## 3. Picard transitions

For each n>=1 the units sequence for successive infinitesimal neighborhoods gives

```text
H^1(U,O_U(-nU))
 -> Pic((n+1)U)
 -> Pic(nU)
 -> H^2(U,O_U(-nU)).
```

Since U is a curve,

```text
H^2(U,O_U(-nU))=0.
```

By (FORMAL-H1), for every n>=2,

```text
Pic((n+1)U) -> Pic(nU)
```

is an isomorphism.

Z37 gives triviality at the only exceptional first step:

```text
O_{2U}(P) ~= O_{2U}.
```

Induction therefore yields

```text
O_{nU}(P) ~= O_{nU}
```

for every finite n>=1, and hence

```text
O_{nU}(lP) ~= O_{nU}
```

for all l,n>=1.

## 4. Z3 consequence

The formal Picard/null-neighborhood route is now completely classified on the four balanced
incidence-16 support orbits:

```text
00070b000f0f  orbit 768:
  EXCLUDED already by non-torsion ordinary Pic^0 cycle holonomy.

000707000f0f  orbit 768:
  survives ordinary Pic^0;
  first-normal class vanishes;
  every higher finite formal Picard obstruction vanishes.

0000770000ff orbit 48:
  every finite formal Picard obstruction vanishes (tree calculation).

00007b0000ff orbit 48:
  every finite formal Picard obstruction vanishes (tree calculation).
```

Thus further deepening of Z3 by finite formal neighborhoods is exhausted.

This does not imply the three surviving orbits have effective irreducible carriers.  It says only
that restriction of O(lP) to the retained formal null locus cannot exclude them.

Any remaining Z3 continuation must use genuinely global cone/contraction/effectivity information,
not deeper formal Picard gluing.

## Source locks

- Z33G note blob `14c1661c5a3b1975474c1f983ed08b29c2150731`;
- Z37 note blob `87ee5db44a7784a2d1e64a9effe4fbe3bd525c66`;
- Z37 certificate is the exact first-normal input;
- size-48 formal-null note blob `931a0d5813985b3b96d8cd5105816feea3b01529`.

## Firewalls

```text
formal_Z3_route_exhausted_on_three_survivors=true
three_surviving_orbits_excluded=false
remaining_balanced_support_count=864
whole_uniform_ray_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
