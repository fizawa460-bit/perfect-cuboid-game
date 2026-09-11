# Stage32 MB104 — exact finite-m BTVA lower-bound wall at node support 14

Status: **RETAINED METHOD-SPECIFIC EXACT FINITE-m NONCLOSURE WALL / NO POPULATION-WIDE FINITE WINDOW**.

## Source

Bruin--Thomas--Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, Algebra & Number Theory 16 (2022), 1377--1405, DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908v3`.

Used published formulas:

- Proposition 3.1: for a nodal surface with `ell` A1 points and `r` removed exceptional components,
  `h0 >= chi(Y,S^m Omega^1_Y) + ell*chi1(A1,m) + r*chi0(A1,m)` for the stated range.
- Proposition 3.3: exact quasi-polynomial for `chi0(A1,m)` by `m mod 6`.
- Proposition 3.7: exact quasi-polynomial for `chi1(A1,m)` by `m mod 3`.
- Appendix RR formula for `chi(Y,S^m Omega^1_Y)`.
- Section 7: on the perfect-cuboid surface, taking `r=35` gives a positive lower bound beginning at `m=862` and yields finiteness for curves meeting at most 13 nodes.

For the cuboid resolution `K^2=16`, `c2=80`, so

`chiY(m)=-(32/3)m^3-40m^2-(64/3)m+8`.

The exact A1 correction formulas used are those of Propositions 3.3 and 3.7.

## Exact lower bound

Define

`LB_r(m)=chiY(m)+48*chi1(m)+r*chi0(m)`.

A carrier meeting `N` of the 48 surface nodes corresponds to `r=48-N` exceptional components in the Proposition 3.1 setup.

### Validation at N=13

For `N=13`, `r=35`.

Exact evaluation gives:

- `LB_35(m)<=0` for every integer `3<=m<=861`;
- `LB_35(862)=7320>0`;
- the six residue-class polynomials are increasing after this threshold, and all subsequent admissible integers are positive.

Thus the first positive exact lower bound is `m=862`, reproducing the published Section 7 threshold.

### N=14

For `N=14`, `r=34`. The six residue-class formulas reduce to:

- `m=0 mod 6`:
  `LB_34=-(5m^3+447m^2-18m-432)/54`;
- `m=1 mod 6`:
  `LB_34=-(5m^3+447m^2+441m-29)/54`;
- `m=2 mod 6`:
  `LB_34=-(m+1)(5m^2+442m-292)/54`;
- `m=3 mod 6`:
  `LB_34=-(5m^3+447m^2+441m+27)/54`;
- `m=4 mod 6`:
  `LB_34=-(5m^3+447m^2-18m-488)/54`;
- `m=5 mod 6`:
  `LB_34=-(m+1)(5m^2+442m+167)/54`.

On the admissible ranges `m>=3` these bracketed factors are strictly positive. Hence

`LB_34(m)<0` for every integer `m>=3`.

This is stronger than the preceding asymptotic observation `C(34)=-5/54`: the exact published Proposition 3.1 lower-bound expression never becomes positive at any finite symmetric power when support is 14.

## Decision

The direct BTVA Proposition 3.1 lower-bound route, even using the full exact finite-`m` quasi-polynomials rather than only the leading cubic coefficient, cannot certify a nonzero symmetric differential for the `N=14` population.

This does **not** prove that the actual space of symmetric differentials is zero. Proposition 3.1 is a lower bound. A successful `N>=14` continuation would need genuinely more information, such as:

- exact computation of the actual global section space rather than this lower bound;
- dependence among local extension conditions;
- explicit symmetric differentials/resultants/foliations;
- or independent Picard/jet/member geometry.

## Firewalls

- A negative lower bound is not interpreted as actual vanishing.
- No claim is made that low-genus curves with `N>=14` form an infinite family.
- `N<=13` abstract finiteness is not converted to a numerical degree cutoff.
- No finite Picard enumeration release.
- No `R29-LG2-MB` discharge, receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit.
- Merge remains unauthorized.
