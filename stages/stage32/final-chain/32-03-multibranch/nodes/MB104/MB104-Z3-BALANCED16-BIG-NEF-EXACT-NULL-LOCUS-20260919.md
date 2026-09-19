# MB104 Z3 — balanced16 big-nef and exact null-locus classification — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT Z3 NEGATIVE-CURVE CLOSURE / NO CREDIT**

## Scope

This is an original Z3 effective-cone / stable-base re-audit on the four balanced incidence-16
uniform rays.

For a balanced support Sigma put

```text
P = 7H - 4 sum_(i in Sigma) E_i,
P^2=336.
```

The four retained support orbits are

```text
0000770000ff   orbit 48
00007b0000ff   orbit 48
000707000f0f  orbit 768
00070b000f0f  orbit 768.
```

The first two lie in incidence-16 size-3 support hyperplanes; the last two lie in incidence-16
size-24 support hyperplanes.

## 1. Hyperplane-contact inequality for an arbitrary test curve

Let L be the unique ambient hyperplane spanned by Sigma and let R be any integral
nonexceptional curve on the smooth cuboid resolution.

Write

```text
d=H.R,
m_i=E_i.R >=0.
```

If R is not contained in L, the retained Z33 local A1 hyperplane-contact lemma applies to every
normalization branch of R over every supported box node:

```text
ord_b(L) >= m_b.
```

Summing over all supported branches gives

```text
sum_(i in Sigma) m_i <= d.                  (Z3-HYP)
```

Therefore

```text
P.R
 =7d-4 sum_(i in Sigma)m_i
 >=3d
 >0.                                        (Z3-POS)
```

Thus every nonexceptional P-null or P-negative curve must be contained in the single support
hyperplane L.

## 2. Curves contained in L

An integral curve contained in L is an irreducible component of the hyperplane section S cap L.

The archived exact incidence-16 section classification gives:

### size-3 ambient hyperplane

```text
S cap L = Q1+Q2+Q3+Q4
```

with four smooth elliptic quartics.

For each of the two balanced size-48 support orbits, the retained balanced quotient computes four
zero-pairing quartics; equivalently each section component contains exactly seven supported nodes.

Hence

```text
P.Q_j = 7*4 -4*7 =0
```

for all four section components.

### size-24 ambient hyperplane

```text
S cap L = 2Q1+2Q2
```

with two smooth elliptic quartics.

For each of the two balanced size-768 support orbits, both reduced section components contain
exactly seven supported nodes, so again

```text
P.Q_j=0.
```

There is no negative section component.

## 3. Exceptional curves

For the 48 exceptional curves,

```text
P.E_i=8  if i in Sigma,
P.E_j=0  if j notin Sigma.
```

Thus none is negative.

## 4. Big and nef

Every irreducible curve is now covered:

- supported exceptional: positive;
- unsupported exceptional: zero;
- nonexceptional curve not contained in L: strictly positive by (Z3-POS);
- nonexceptional curve contained in L: one of the exact elliptic-quartic section components, with
  pairing zero.

Therefore for every one of the four balanced support orbits,

```text
P is nef.
```

Since

```text
P^2=336>0,
```

P is also big.

This is stronger than a finite retained curve-library test.  No hidden negative curve can force a
fixed component on the balanced uniform ray.

## 5. Exact null locus

The same proof classifies every irreducible P-null curve.

### size-48 supports

```text
Null(P)
 = 34 unsupported exceptional curves
   union
   4 elliptic quartic components of S cap L.
```

### size-768 supports

```text
Null(P)
 = 34 unsupported exceptional curves
   union
   2 elliptic quartic components of S cap L.
```

There are no other null curves: any other nonexceptional curve is outside L and has P.R>=3d>0.

## 6. Z3 disposition

The original Z3 hope was that a source-complete cone/null-locus theorem might reveal a hidden
negative or null class forcing reducibility.

For the balanced uniform hard core this route is now exact:

```text
hidden negative curve = none,
primitive ray          = big and nef,
null locus             = explicitly classified.
```

The later Picard/formal-gluing work then decides what the known null locus can do:

- orbit 00070b000f0f is excluded by non-torsion gluing holonomy;
- the two size-48 orbits have no finite formal Picard obstruction;
- orbit 000707000f0f has trivial ordinary and first-normal obstruction, and higher finite formal
  obstruction vanishes by the separate all-formal calculation.

Thus **Z3 as a negative-curve / hidden-null-locus search is exhausted on the balanced uniform
sector**.

This does not prove existence or irreducibility of carriers on the three surviving orbits and does
not close arbitrary unequal Picard classes.

## Source locks

Historical archive head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- incidence-16 section note blob `593868a09e41ebfd1ad7f0f4c1aa83f6ca5cd923`;
- incidence-16 section certificate blob `9c36555e495df0d8d6b816f1c0dc7d4c35b55848`;
- balanced quotient note blob `1dfafccb9559c98ccf71cc4b98449d784941d48f`;
- balanced quotient certificate blob `f63d08b9005762a02935a727f35e6581ae52aaab`.

Current:
- Z33 hyperplane-contact note blob `65656518d30f69ab3a4a892c8d4ae1d5ed72670e`.

## Firewalls

```text
balanced_uniform_P_big_nef=true
balanced_uniform_exact_null_locus_classified=true
hidden_negative_curve_route_closed=true
three_surviving_orbits_excluded=false
arbitrary_unequal_picard_classes_closed=false
whole_span5_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
