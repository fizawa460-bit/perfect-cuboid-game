# Stage32 MB104 — BTVA low-support threshold is sharp for the Proposition 3.1 asymptotic route

Status: **RETAINED METHOD-SPECIFIC NONCLOSURE WALL / NO POPULATION-WIDE FINITE WINDOW**.

## Source

Bruin--Thomas--Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, Algebra & Number Theory 16 (2022), 1377--1405, DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908v3`.

Relevant printed locations:

- Proposition 3.1: for a nodal surface with `ell` A1 points and `r` removed exceptional components,
  `h0 >= chi(Y,S^m Omega^1_Y) + ell*chi1(A1,m) + r*chi0(A1,m)`.
- Proposition 3.3: `chi0(A1,m) = (11/108)m^3 + O(m^2)`.
- Proposition 3.7: `chi(A1,m) = (1/4)m^3 + O(m^2)`, hence
  `chi1(A1,m) = (1/4-11/108)m^3+O(m^2)=(16/108)m^3+O(m^2)`.
- Section 7, perfect-cuboid application: with 48 nodes and `r=48-13=35`, the paper obtains
  `h0=(1/108)m^3+O(m^2)` and concludes finiteness for low-genus curves meeting at most 13 nodes.

The Section 7 statement and the local A1 formulas are used only at their published asymptotic strength.

## Exact coefficient replay

Write `C(r)` for the cubic coefficient in the Proposition 3.1 lower bound on the perfect-cuboid resolution after removing `r` exceptional components.

Section 7 gives

`C(35)=1/108`.

Since increasing `r` by one changes the cubic coefficient by exactly the A1 `chi0` coefficient `11/108`, we get

`C(r)=C(35)+(r-35)*(11/108)`

and therefore

`C(r)=(11r-384)/108`.

Consequences:

- `r=35`: `C=1/108>0`;
- `r=34`: `C=-10/108=-5/54<0`;
- because `r` is integral, `C(r)>0` iff `r>=35`.

For a curve meeting `N` surface nodes, the complement has `r=48-N` nodes. Thus this exact asymptotic lower-bound route has positive cubic coefficient precisely when

`48-N>=35`, i.e. `N<=13`.

At `N=14`, the coefficient is already negative.

## Decision

The retained BTVA Proposition 3.1 + local Euler-characteristic asymptotic route is **sharp at support 13** on the perfect-cuboid surface. Re-running the same asymptotic argument cannot move the retained finiteness boundary from `N<=13` to `N<=14`.

This does **not** say that there are infinitely many low-genus curves meeting 14 or more nodes. It also does not rule out:

- stronger exact finite-`m` computations of actual symmetric-differential spaces;
- additional vanishing or dependence among extension conditions;
- multiple explicit differentials/resultants/foliations;
- different global geometry or Picard/member arguments.

It only retires the direct asymptotic Proposition 3.1 threshold-extension attempt.

## Firewalls

- `N<=13` abstract finiteness is not converted to a numerical degree bound.
- Negative lower-bound cubic coefficient for `N=14` is not interpreted as vanishing of actual sections.
- No finite Picard enumeration release.
- No `R29-LG2-MB` discharge, receiver/theorem/endpoint credit, or Perfect-Cuboid conclusion.
- Merge remains unauthorized.
