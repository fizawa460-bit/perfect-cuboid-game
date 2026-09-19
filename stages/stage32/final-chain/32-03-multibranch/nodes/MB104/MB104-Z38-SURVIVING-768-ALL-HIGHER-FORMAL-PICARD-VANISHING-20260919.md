# MB104 Z38 — surviving-768 all-higher formal Picard vanishing — 2026-09-19

Status: **PRE-AUDIT EXACT ALL-FINITE-THICKENING FORMAL NO-GO / NO CREDIT**

## Input

For the surviving balanced support

```text
000707000f0f
```

let `U=A union B` be its two zero-pairing elliptic quartics.

The exact geometry retained from Z33H/Z37 is

```text
A^2=B^2=-4,
A.B=2,
A and B meet transversely at r_+,r_-.
```

Z33G proves `O_U(P) ~= O_U`, and Z37 proves `O_{2U}(P) ~= O_{2U}`.

## Higher Picard transition kernel

Let `I=I_U=O_S(-U)`. For `n>=1`,

```text
I^n/I^(n+1) ~= O_U(-nU).
```

The units sequence gives

```text
H^1(U,O_U(-nU))
 -> Pic((n+1)U)
 -> Pic(nU)
 -> H^2(U,O_U(-nU)).
```

Since `U` is a curve, the final H2 is zero.

Because

```text
U.A=A^2+A.B=-2,
U.B=-2,
```

we have

```text
deg O_A(-nU)=deg O_B(-nU)=2n.
```

These have positive degree, so componentwise H1 vanishes for every `n>=1`.

For `n>=2`, subtract the two intersection points `D=r_++r_-`. Then

```text
deg O_A(-nU-D)=deg O_B(-nU-D)=2n-2>0.
```

Hence the evaluation maps from either elliptic component to the two node fibers are surjective.

The normalization sequence

```text
0 -> O_U(-nU)
  -> O_A(-nU) plus O_B(-nU)
  -> k(r_+) plus k(r_-)
  -> 0
```

therefore gives

```text
H^1(U,O_U(-nU))=0
```

for every `n>=2`.

Thus

```text
Pic((n+1)U) -> Pic(nU)
```

is an isomorphism for every `n>=2`.

## Induction from Z37

Z37 gives `O_{2U}(P) ~= O_{2U}`. Induction through the transition isomorphisms gives

```text
O_{nU}(P) ~= O_{nU}
```

for every finite `n>=1`, and hence

```text
O_{nU}(lP) ~= O_{nU}
```

for every `l>=1`.

So the complete finite formal-Picard tower along the surviving two-quartic null union is compatible with the ray.

This proves neither effectivity nor existence of a carrier.

## Consequence

Together with the retained size-48 formal-neighborhood vanishing, the known zero-quartic formal Picard route has no remaining balanced orbit to attack.

## Next route

```text
MB104-Z39-REMAINING-BALANCED-SEMAMPLE-CONTRACTION-DESCENT-PREFLIGHT
```

Test whether the big-nef balanced ray descends through contraction of its known null configuration to a class whose linear systems impose a new irreducibility or genus constraint. Stop if contraction only confirms compatibility.

## Firewalls

```text
all_finite_formal_restrictions_trivial=true
surviving_768_excluded=false
remaining_balanced_support_count=864
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
