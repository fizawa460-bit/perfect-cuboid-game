# MB104 Z3 — balanced16 primitive-ray nefness and exact null locus — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT NEF/NULL-LOCUS REDUCTION / NO CREDIT**

## Scope

This is a continuation of the original Z3 effective-cone / stable-base direction.

It applies only to the displayed uniform balanced incidence-16 genus-one span-five ray

```text
P = 7H - 4 sum_(i in Sigma) E_i,
|Sigma|=14,
```

for the three surviving balanced support orbits after Z33G:

```text
0000770000ff   orbit 48,
00007b0000ff   orbit 48,
000707000f0f   orbit 768.
```

The fourth balanced orbit `00070b000f0f` is already excluded by Z33G.

## 1. Curves not contained in the support hyperplane

Let L be the unique ambient hyperplane spanned by Sigma and let R be an irreducible
nonexceptional curve on the smooth cuboid resolution whose image is not contained in L.

Put

```text
d=H.R,
m_i=E_i.R >=0.
```

The retained Z33 local hyperplane-contact lemma gives, branch by branch over every supported
box node,

```text
ord_b(L|R) >= m_b.
```

Summing over all branches above the fourteen supported nodes,

```text
sum_(i in Sigma) m_i <= deg(L|R)=d.
```

Therefore

```text
P.R
 = 7d - 4 sum_(i in Sigma)m_i
 >= 7d-4d
 = 3d
 >0.
```

Thus every nonexceptional irreducible curve not contained in the support hyperplane pairs
strictly positively with P.

## 2. Curves contained in the support hyperplane

If an irreducible nonexceptional curve R is contained in L, then its image is an irreducible
component of the scheme-theoretic hyperplane section S cap L.

The archived exact section classification gives two incidence-16 possibilities.

### Size-3 ambient orbit

The section is the reduced union of four smooth elliptic quartics.

For a balanced N=14 support each quartic contains exactly seven supported box nodes. Hence for
each component Q,

```text
P.Q = 7*4 - 4*7 = 0.
```

### Size-24 ambient orbit

The reduced section support consists of two smooth elliptic quartics, each occurring with generic
scheme multiplicity two.

For a balanced N=14 support the supported-node split is exactly (7,7). Hence for each reduced
quartic component Q,

```text
P.Q = 7*4 - 4*7 = 0.
```

There are no other irreducible nonexceptional curves contained in L, because every such curve is a
component of the classified section.

## 3. Exceptional curves

For the 48 exceptional curves,

```text
P.E_i = 8   if i in Sigma,
P.E_j = 0   if j notin Sigma.
```

Thus exceptional curves are never negative.

## 4. Nefness

Every irreducible curve on the smooth resolution falls into exactly one of:

- supported exceptional curve: positive;
- unsupported exceptional curve: zero;
- nonexceptional curve outside L: strictly positive;
- nonexceptional curve inside L: one of the classified elliptic quartics, with pairing zero.

Therefore

```text
P is nef.
```

Since

```text
P^2=336>0,
```

P is also big.

## 5. Exact null locus

The preceding argument also identifies every irreducible curve R with P.R=0.

It consists exactly of:

1. the 34 unsupported exceptional (-2)-curves;
2. the zero-pairing elliptic-quartic components of the support hyperplane section:
   - four quartics for the two size-48 support orbits;
   - two quartics for the surviving size-768 support orbit.

No irreducible curve outside the support hyperplane can be null, because there P.R>=3H.R>0.

Thus the Z3 problem on these rays is no longer an unknown effective-cone search.  The complete
null locus is explicit.

## 6. Consequence for Z3

A hidden negative curve cannot force a fixed component on any of the three surviving balanced rays.

Hence the original Z3 strategy

```text
find a negative test curve / hidden stable-base fixed component
```

is closed in the negative direction on the balanced hard core.

Any remaining Z3 use must come from the geometry of the contraction / semiampleness / formal
restriction along this exact null locus, not from discovering another negative curve.

Current formal-restriction results already show:

- the two size-48 tree null unions have no finite formal Picard obstruction;
- the surviving size-768 union has trivial ordinary and first-normal obstruction, and higher
  finite formal Picard obstruction also vanishes.

Therefore a future Z3 continuation must be genuinely global (for example, contraction or
semiampleness geometry), not another local or finite formal-neighborhood search.

## Source locks

Historical archive head:
```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16.md`
  blob `593868a09e41ebfd1ad7f0f4c1aa83f6ca5cd923`;
- `GENUS1-SPAN5-UNIFORM-RAY-COMPONENT-CAPACITY.md`
  retained uniform-ray semantics;
- `GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT.md`
  blob `1dfafccb9559c98ccf71cc4b98449d784941d48f`.

Current compact branch:
- Z33 hyperplane-contact equality note;
- Z33G one-orbit elimination;
- Z3 size-48 formal-null note;
- Z37 first-normal note;
- Z3 all-formal surviving768 note.

## Firewalls

```text
balanced_surviving_rays_nef=true
balanced_surviving_rays_big=true
exact_null_locus_identified=true
hidden_negative_curve_route_closed=true
three_surviving_orbits_excluded=false
irreducible_genus_one_carrier_exists=false
whole_uniform_ray_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
