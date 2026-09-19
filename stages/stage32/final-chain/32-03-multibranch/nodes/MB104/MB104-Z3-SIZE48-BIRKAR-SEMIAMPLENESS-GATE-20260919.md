# MB104 Z3 — size-48 Birkar semiampleness gate — 2026-09-19

Status: **PARALLEL PRE-AUDIT SOURCE-BASED SEMIAMPLENESS RESULT / NO CREDIT**

## Scope

This applies only to the two surviving balanced size-48 support orbits

```text
0000770000ff
00007b0000ff
```

for the primitive ray

```text
P=7H-4 sum_(i in Sigma)E_i.
```

The preceding Z3 work proves:

```text
P is big and nef,
Null(P) is complete and explicit.
```

The goal is to decide whether the size-48 null configuration is strong enough to prove
semiampleness of P.

## 1. Complete null locus for a size-48 support

For either size-48 support, the four zero-pairing elliptic quartics occur in two connected tree
components

```text
Q_1 -- E_a -- Q_2,
Q_3 -- E_b -- Q_4,
```

where (E_a,E_b) are the repeated omitted unsupported exceptional curves.

The remaining 32 unsupported exceptional curves are isolated from the zero-quartic union.

Thus the complete null locus is a disjoint union of

```text
two Q-E-Q trees
+
32 isolated exceptional P1s.
```

## 2. All finite thickenings of the Q-E-Q trees

The retained Z3 size-48 formal-neighborhood computation proves for a tree component

```text
U=Q_1+E+Q_2
```

that for every n>=1

```text
H^1(U,O_U(-nU))=0.
```

Since

```text
O_U(P)~=O_U,
```

the Picard transition maps between successive infinitesimal neighborhoods are isomorphisms and

```text
O_(nU)(P)~=O_(nU)
```

for every finite n>=1.

## 3. Isolated unsupported exceptional curves

Let E be any of the 32 isolated unsupported exceptional curves.

Then

```text
E~=P1,
E^2=-2,
P.E=0,
```

so

```text
O_E(P)~=O_E.
```

For every n>=1,

```text
O_E(-nE)~=O_P1(2n),
H^1(E,O_E(-nE))=0.
```

Therefore the same infinitesimal Picard induction gives

```text
O_(nE)(P)~=O_(nE)
```

for every finite n.

Because the connected components of the complete null locus are disjoint, these statements combine
componentwise:

```text
O_(n Null(P))(P) ~= O_(n Null(P))
```

for every finite n>=1.

## 4. Birkar semiampleness criterion

Caucher Birkar, *The augmented base locus of real divisors over arbitrary fields*,
Math. Ann. 368 (2017), Theorem 1.5, proves:

for a nef Q-Cartier divisor L on a projective scheme, there exists a closed subscheme Z whose
reduced scheme is the exceptional/null locus E(L), such that

```text
L semiample  <=>  L|Z semiample.
```

Apply this to L=P.

Since Z_red=Null(P) and the ambient surface is Noetherian, some power of the ideal of Null(P)
is contained in the ideal of Z. Equivalently, Z is contained in some finite thickening

```text
Z subset n Null(P).
```

But P is trivial on every finite thickening of Null(P). Hence

```text
P|Z is trivial,
```

in particular semiample.

Birkar's criterion therefore gives

```text
P is semiample
```

for both size-48 balanced support orbits.

## 5. Meaning for Stage32

This is **not an exclusion** of the two support orbits.

It closes the original Z3 obstruction mechanism much more strongly:

```text
no hidden negative curve,
complete null locus known,
all formal null restrictions trivial,
P semiample.
```

Thus the effective-cone/stable-base geometry of P cannot by itself rule out these two balanced rays.

Any future exclusion must use the special requirement that a member of |lP| have geometric genus
one / the exact multibranch singularity packet; it cannot come merely from non-semiampleness or
a hidden base component.

## 6. Size-768 boundary

No semiampleness claim is made here for `000707000f0f`.

For that orbit the core two-quartic cycle is formally trivial to all orders in the retained
calculation, but the complete null locus also contains attached unsupported exceptional leaves.
A whole-null-scheme formal-gluing adapter should be made explicit before applying Birkar.

## Source locks

Repository:
- Z40B complete-null-locus bypass;
- Z3 size-48 formal-null-neighborhood note
  blob `931a0d5813985b3b96d8cd5105816feea3b01529`;
- archived balanced quotient blob
  `1dfafccb9559c98ccf71cc4b98449d784941d48f`.

External:
- C. Birkar, Math. Ann. 368 (2017), 905--921,
  *The augmented base locus of real divisors over arbitrary fields*,
  Theorem 1.5.

## Firewalls

```text
size48_P_semiample=true
size48_orbits_excluded=false
size768_P_semiample=false
genus_one_carrier_exists=false
whole_uniform_ray_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
