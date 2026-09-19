# MB104 Z5' — 000707 e=4 individual six-value passports are Hurwitz-feasible for all l — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT ALL-l ONE-FACTOR NO-GO / NO CREDIT**

## Purpose

The exact factor-cusp adapter upgrades the old type-pair passport on

```text
Sigma=000707000f0f
```

to individual X(4)=C8/G branch values.

In the e=4 equality case, the normalization E carries two degree-56l maps

```text
phi_1,phi_2:E->C8/G ~= P1.
```

The six branch values are ordered

```text
(1,-1,i,-i,0,infinity).
```

The exact supported-node cells give the individual unramified counts

```text
factor 1:
u=(32,24,56,0,0,0) l,

factor 2:
u=(56,0,24,32,0,0) l.
```

Using u_q+2r_q=56l, the simple-ramification counts are

```text
factor 1:
r=(12,16,0,28,28,28) l,

factor 2:
r=(0,28,16,12,28,28) l.
```

This note checks whether either one-factor passport is topologically impossible.

It is not: both admit explicit connected genus-one monodromy for every l>=1.

## 1. Factor-1 construction

Let n=56l and partition the letters into two sets

```text
A={0,...,24l-1},
B={24l,...,56l-1}.
```

Define involutions:

```text
s_1:
  12l disjoint transpositions pairing consecutive letters in A;
  32l fixed letters.

s_2:
  16l disjoint transpositions pairing consecutive letters in B;
  24l fixed letters.

s_3 = identity.

s_6 = s_1 s_2.
```

Since s_1 and s_2 have disjoint supports, they commute and s_6 is a fixed-point-free involution
with 28l transpositions.

The transpositions of s_6 give 28l disjoint two-vertex components.  For each component j choose an
ordered pair (u_j,v_j).  Define a second fixed-point-free involution

```text
T = product_j (v_j, u_(j+1 mod 28l)).
```

Set

```text
s_4=T,
s_5=T.
```

Then

```text
s_1 s_2 s_3 s_4 s_5 s_6
 = s_1 s_2 T T (s_1 s_2)
 = 1.
```

The union of the s_6 matching and the T matching is a single alternating cycle through all n
letters.  Hence the generated permutation group is transitive.

The six transposition counts are exactly

```text
(12,16,0,28,28,28)l.
```

Their sum is 112l, so Riemann--Hurwitz gives genus one.

## 2. Factor-2 construction

Again n=56l.  Split the letters into

```text
A'={0,...,32l-1},
B'={32l,...,56l-1}.
```

Define

```text
t_1 = identity,

t_3:
  16l consecutive transpositions on A';

t_4:
  12l consecutive transpositions on B';

t_2 = t_3 t_4.
```

Because t_3,t_4 have disjoint supports, t_2 is a fixed-point-free involution with 28l
transpositions.

Let T' be the alternating-cycle perfect matching obtained from the 28l transposition components of
t_2 exactly as above, and set

```text
t_5=T',
t_6=T'.
```

Then

```text
t_1 t_2 t_3 t_4 t_5 t_6
 = (t_3 t_4)t_3 t_4 T'T'
 =1,
```

and the generated action is transitive.

The six transposition counts are exactly

```text
(0,28,16,12,28,28)l.
```

Again the total index is 112l and the resulting connected cover has genus one.

## 3. Consequence

The newly source-locked individual branch-value passports are much sharper than the old pair
totals, but **neither factor alone is obstructed**.

For every l>=1 there exist connected genus-one covers of P1 of degree 56l with exactly the required
cycle types.

Therefore the following are now exhausted as standalone exclusions of the 000707/e=4 packet:

```text
- scalar Riemann--Hurwitz;
- type-pair totals;
- individual six-value fixed-point counts;
- individual six-value simple-ramification counts;
- one-factor transitivity/product-one Nielsen existence.
```

The only possible Z5' obstruction must use the genuinely simultaneous data:

```text
the two factor maps arise from the same G-stable
Z subset C8 x C8
and the exact 12-cell node pairing couples their fibers.
```

## 4. Exact single-fiber saturation retained

The factor-cusp adapter also gives two full unramified fibers in the e=4 case:

```text
factor 1, value +i:
  7 supported nodes * 8l = 56l points;

factor 2, value +1:
  7 supported nodes * 8l = 56l points.
```

So these two fibers are completely reduced and consist entirely of supported normalization points.

This extra simultaneous information is not used by the one-factor feasibility construction above
and remains available for the next two-factor gate.

## Firewalls

```text
one_factor_passports_feasible_for_all_l=true
two_factor_common_cover_realized=false
cuboid_carrier_exists=false
e4_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
