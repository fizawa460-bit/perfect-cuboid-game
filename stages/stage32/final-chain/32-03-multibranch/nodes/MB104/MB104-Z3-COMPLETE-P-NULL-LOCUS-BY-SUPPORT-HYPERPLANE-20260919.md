# MB104 Z3 — complete P-null locus by support-hyperplane geometry — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT NULL-LOCUS COMPLETENESS / NO CREDIT**

## Purpose

Supersede the need for an open-ended P-null curve search on the three surviving balanced incidence-16
support orbits.

Let

```text
P = 7H - 4 sum_(i in Sigma) E_i,
|Sigma|=14,
```

and let L be the unique ambient support hyperplane spanned by Sigma.

The later Z39 finite-degree reduction gives a finite search, but the exact Z33 hyperplane-contact
lemma plus the archived incidence-16 section classification give a stronger direct argument.

## 1. A nonexceptional P-null curve cannot lie outside L

Let R be a nonexceptional integral curve on the smooth resolution and put

```text
e = H.R > 0,
M_Sigma = sum_(i in Sigma) E_i.R.
```

If the image of R is not contained in L, the exact Z33 local contact lemma gives

```text
M_Sigma <= e.
```

But P.R=0 means

```text
7e - 4 M_Sigma = 0,
M_Sigma = 7e/4.
```

For positive e,

```text
7e/4 > e,
```

contradicting the hyperplane-contact upper bound.

Therefore

```text
P.R=0 and R nonexceptional
=> image(R) subset L.
```

This argument has no degree assumption.

## 2. Curves inside L are exactly section components

An integral curve on the cuboid surface whose image is contained in L is an irreducible component
of the scheme-theoretic hyperplane section

```text
Sbar cap L.
```

The archived exact incidence-16 section classification is complete.

### Size-3 ambient incidence-16 orbit

The reduced hyperplane section is exactly four smooth elliptic quartics.

For a balanced N=14 support, every one of the four quartics contains exactly seven supported nodes,
hence

```text
P.Q = 7*4 - 4*7 = 0.
```

There are no other nonexceptional irreducible components.

### Size-24 ambient incidence-16 orbit

The reduced hyperplane section is exactly two smooth elliptic quartics, each occurring with generic
scheme multiplicity two.

For the balanced (7,7) support split,

```text
P.Q = 0
```

for both reduced quartic components.

Again there are no other nonexceptional irreducible components.

## 3. Exceptional curves

For the exceptional curves,

```text
P.E_i = 8  if i in Sigma,
P.E_j = 0  if j notin Sigma.
```

Thus the exceptional P-null curves are exactly the 34 unsupported exceptional curves.

## 4. Complete null locus

For each surviving balanced support, the complete irreducible P-null locus is therefore:

```text
unsupported exceptional (-2)-curves
+
zero-pairing elliptic quartic components of the support hyperplane section.
```

Orbitwise:

```text
0000770000ff:
  34 unsupported exceptionals + 4 zero elliptic quartics.

00007b0000ff:
  34 unsupported exceptionals + 4 zero elliptic quartics.

000707000f0f:
  34 unsupported exceptionals + 2 zero elliptic quartics.
```

No unknown degree-8/12/16/20 P-null curve exists.

## 5. Consequence for Z39/Z40

The Z39 degree set

```text
{4,8,12,16,20}
```

is a valid necessary reduction but is not needed for null-locus completeness on these balanced
supports.

The planned Z40 Picard64 enumeration cannot discover an additional geometric P-null curve:
any such curve would have to lie outside the support hyperplane by virtue of not being a known
section component, but that contradicts the exact Z33 contact inequality.

Thus the geometric null-locus classification closes before Picard enumeration.

A lattice class surviving Z40 would at most be a numerical class not represented by an integral
curve; it cannot invalidate the geometric argument above.

## Source locks

Predecessor exact head:
```text
b28adadc95776762754e1415a0ecab0da1d4cd8e
```

- Z33 hyperplane-contact note blob
  `65656518d30f69ab3a4a892c8d4ae1d5ed72670e`.

Historical archive head:
```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- incidence-16 section classification blob
  `593868a09e41ebfd1ad7f0f4c1aa83f6ca5cd923`;
- balanced quotient blob
  `1dfafccb9559c98ccf71cc4b98449d784941d48f`.

## Firewalls

```text
complete_P_null_locus_classified=true
unknown_positive_degree_P_null_curve=false
Z40_geometric_null_enumeration_needed=false
three_surviving_orbits_excluded=false
P_semiample_not_claimed=true
whole_uniform_ray_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
