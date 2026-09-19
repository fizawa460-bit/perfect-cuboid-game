# MB104 Z40B — support-hyperplane complete null-locus bypass — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT Z40 ENUMERATION BYPASS / NO CREDIT**

## Purpose

The active Z40 route proposes a rank-64 Picard enumeration of 17 numerical shells in degrees

```text
4,8,12,16,20
```

to prove completeness of the (P)-null locus for the three surviving balanced incidence-16
support orbits.

For these three **uniform balanced rays**, that enumeration is unnecessary.

The retained Z33 hyperplane-contact inequality and the exact incidence-16 hyperplane-section
classification already force every nonexceptional (P)-null curve to be one of the known
zero-pairing elliptic quartics.

## Setup

Fix one of the surviving balanced supports

```text
0000770000ff
00007b0000ff
000707000f0f
```

and let (Lsubset mathbf P^6) be its unique support hyperplane.

The primitive ray is

```text
P = 7H - 4 sum_(i in Sigma) E_i,
|Sigma|=14.
```

Let (R) be an irreducible nonexceptional curve on the smooth cuboid resolution and put

```text
e=H.R>0,
M_i=E_i.R>=0.
```

## 1. A P-null curve cannot leave the support hyperplane

Assume the image of (R) is **not** contained in (L).

The Z33 local A1 hyperplane-contact lemma gives, for every normalization branch (b) of (R)
over a supported box node,

```text
ord_b(L|R) >= m_b.
```

Summing over all branches above the fourteen supported nodes,

```text
sum_(i in Sigma) M_i <= deg(L|R)=e.
```

Therefore

```text
P.R
 = 7e - 4 sum_(i in Sigma)M_i
 >= 7e-4e
 = 3e
 >0.
```

Hence

```text
P.R=0
=> image(R) is contained in L.
```

This argument uses no degree bound, Hodge estimate, adjunction estimate, or Picard enumeration.

## 2. Any nonexceptional curve contained in L is a section component

The singular cuboid surface has dimension two, so (Scap L) is a one-dimensional
scheme-theoretic hyperplane section.

If the image of an irreducible nonexceptional curve (R) is contained in (L), then its image
is an irreducible one-dimensional closed subset of (Scap L), hence an irreducible component
of the reduced support of that hyperplane section.

The archived exact incidence-16 section classification is complete.

### Incidence-16 size-3 ambient orbit

The reduced section is exactly four smooth elliptic quartics.

For every balanced (N=14) support, each quartic contains exactly seven supported nodes, so

```text
P.Q = 7*4 - 4*7 = 0.
```

There are no other nonexceptional section components.

### Incidence-16 size-24 ambient orbit

The scheme section is

```text
2Q_1 + 2Q_2
```

with two smooth elliptic quartics as its reduced support.

For every balanced (N=14) support the split is exactly ((7,7)), hence

```text
P.Q_1=P.Q_2=0.
```

Again there are no other nonexceptional section components.

## 3. Exceptional curves

For exceptional curves,

```text
P.E_i=8  if i in Sigma,
P.E_j=0  if j notin Sigma.
```

Thus the exceptional null curves are exactly the 34 unsupported exceptional curves.

## 4. Complete null locus

Combining the three cases, the complete irreducible (P)-null locus is:

```text
unsupported exceptional curves
+
the known zero-pairing elliptic-quartic components of S cap L.
```

Orbitwise:

```text
0000770000ff:
  34 unsupported exceptional curves + 4 known elliptic quartics.

00007b0000ff:
  34 unsupported exceptional curves + 4 known elliptic quartics.

000707000f0f:
  34 unsupported exceptional curves + 2 known elliptic quartics.
```

No additional integral (P)-null curve of degrees 8,12,16,20 can exist.

## 5. Relation to Z39/Z40

Z39 is a valid weaker finite reduction:

```text
P.R=0 => e in {4,8,12,16,20}.
```

But for the three balanced uniform rays the support-hyperplane argument is stronger:

```text
P.R=0 and R nonexceptional
=> R lies in S cap L
=> R is one of the classified degree-4 elliptic quartics.
```

Therefore the active Z40 17-shell Picard64 enumeration is not needed to establish null-locus
completeness for these three rays.

This note does **not** say the Picard64 machinery is wrong or useless.  It says that for this
specific balanced-uniform null-locus question a direct geometric proof supersedes the numerical
enumeration.

## 6. Consequence for Z3

Together with the earlier exact positivity argument,

```text
P is big and nef,
Null(P) is now geometrically complete.
```

The remaining Z3 question is no longer:

```text
are there hidden negative/null curves?
```

It is only whether the contraction/semiampleness geometry of this **known** null configuration
can obstruct an irreducible member of (|lP|).

The retained formal-Picard work already shows that finite formal restriction does not exclude
the three surviving orbits.

## Source locks

Historical archive head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16.md`
  blob `593868a09e41ebfd1ad7f0f4c1aa83f6ca5cd923`;
- `GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT.md`
  blob `1dfafccb9559c98ccf71cc4b98449d784941d48f`;
- Z33 hyperplane-contact note at predecessor audited surface
  `MB104-Z33-SPAN5-HYPERPLANE-CONTACT-EQUALITY-20260919.md`.

Current compact branch:

- `MB104-Z3-BALANCED16-PRIMITIVE-RAY-NEF-NULL-LOCUS-20260919.md`
  blob `dca4eecabe748febaa3f898f99711d1da9beb23f`.

## Firewalls

```text
complete_P_null_locus_balanced_uniform=true
Z40_picard64_needed_for_this_null_locus=false
three_surviving_orbits_excluded=false
semiampleness_proved=false
irreducible_carrier_exists=false
whole_uniform_ray_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
