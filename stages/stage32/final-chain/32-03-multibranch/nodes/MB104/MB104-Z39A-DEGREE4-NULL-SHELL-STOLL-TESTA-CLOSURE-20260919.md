# MB104 Z39A — degree-4 P-null shell closure by Stoll--Testa low-degree classification — 2026-09-19

Status: **PARALLEL PRE-AUDIT SOURCE-BASED DEGREE-4 SHELL CLOSURE / NO CREDIT**

## Purpose

Z39 reduces every nonexceptional integral P-null curve to

```text
e=H.R in {4,8,12,16,20}.
```

This note removes the degree-4 shell from the unknown part of the Z40 enumeration by using the
2026 Stoll--Testa classification of low-degree integral curves on the cuboid surface.

## External source

Michael Stoll and Damiano Testa,
*Curves on the surface of cuboids*,
Mathematics of Computation (2026), DOI 10.1090/mcom/4238.

The paper completely classifies integral curves of degree at most 6 on the cuboid surface.

The exact statements needed here are:

- Theorem 15(2): there are no smooth rational curves of degree 4.
- Theorem 15(3): every degree-4 curve of arithmetic genus 1 belongs to the known collection G.
- Theorem 16:
  - an integral curve spanning P^3 is one of the known genus-one curves in G;
  - a plane-contained integral curve is a conic;
  - a degree-4 curve spanning P^4 would be a rational normal quartic, hence smooth rational and is excluded by Theorem 15(2).

These cases exhaust the possible projective spans of an integral degree-4 curve.

Therefore:

```text
every integral degree-4 curve on the cuboid surface
is one of the known genus-one quartics in G.
```

## Application to P-null curves

For each of the balanced incidence-16 support orbits, the retained exact known-curve replay already
computes P-intersection with the twelve known elliptic quartics.

The only degree-4 known curves with

```text
P.Q=0
```

are precisely the already-retained zero-pairing elliptic quartics:

- four for each size-48 support orbit;
- two for each size-768 support orbit.

Hence there is no unknown nonexceptional degree-4 P-null curve.

For the surviving hard core after Z33G this means:

```text
0000770000ff:
  e=4 P-null curves = its four retained zero quartics only.

00007b0000ff:
  e=4 P-null curves = its four retained zero quartics only.

000707000f0f:
  e=4 P-null curves = its two retained zero quartics only.
```

## Consequence for Z40

The unknown Picard64 null-curve enumeration no longer needs the degree-4 shell.

The unresolved positive-degree set becomes

```text
e in {8,12,16,20}.
```

The known degree-4 null quartics must still remain in the complete null locus; they are simply not
unknown enumeration candidates.

This is a geometric source theorem, not merely a lattice filter.

## Source locks / anchors

External:
- Stoll--Testa, DOI 10.1090/mcom/4238;
- Theorems 15 and 16 in the accepted/published 2026 version.

Retained repository inputs:
- Z39 finite-degree reduction;
- archived balanced quotient note blob
  `1dfafccb9559c98ccf71cc4b98449d784941d48f`,
  which enumerates the 12 known elliptic quartics and their supportwise P-pairings.

## Firewalls

```text
degree4_unknown_P_null_curves=false
degree4_known_null_quartics_retained=true
remaining_unknown_degrees={8,12,16,20}
complete_null_locus_classified=false
whole_uniform_ray_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
