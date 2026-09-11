# Stage36 36-09FA — residual-core partial-Legendre chart realization

## Purpose

36-09EY replaced full support-rank computation by the exact identity

```text
rank_F2(M)=k+rank_F2(H),
dim_F2 Sel^2(E_rho,p/Q)=nullity_F2(H).
```

36-09EZ then found 29 fixed arithmetic realizations, but finite full-pattern accumulation is not a route to a uniform theorem. FA extracts a genuinely weaker symbolic condition from one recurrent coarse support type: only the Legendre bits needed by a legal leaf certificate are retained; every other pairwise Legendre bit becomes a don't-care variable.

Entry authority is V286, exact head `5c2224442466ad5990866018cfc1f92deb048c62`, CI `34414312546 / 102675622532`. The exact fixed-p registry on entry is 192 and the exact sufficient full-template count is 17.

## Fixed coarse support type

Work in the retained one-variable family

```text
K=729,
a=2u,
b=2u+729,
P=8u^2-729^2,
Q=-(8u^2+8*729u+729^2),
u=17627 (mod 34440).
```

Assume the labelled odd support has exactly the following coarse type, with all displayed prime variables distinct:

```text
D3 : 3, d
D5 : e
D7 : f
P1 : p1, p2
P7 : 7
Q1 : 41
Q7 : q1, q2
```

The dyadic branch is shallow. The two P1 primes may be ordered so that one of the charts below holds; q1,q2 may be ordered arbitrarily in Chart A and either order in Chart B because both Q7 conditions are symmetric.

Let

```text
chi_r(s)=0  if (s/r)=+1,
chi_r(s)=1  if (s/r)=-1.
```

After quadratic reciprocity, the support type has 45 independent unordered pairwise Legendre bits.

## Chart A — codimension six

Require only

```text
chi_3(p1)=1,
chi_3(p2)=0,
chi_d(p1)=0,
chi_d(p2)=0,
chi_d(41)=1,
chi_e(p2)=1.
```

No other pairwise Legendre bit is fixed.

For the canonical support order

```text
3,d,e,f,p1,p2,7,41,q1,q2
```

the symbolic Stage36 support matrix has size 24x24. Replaying the retained leaf-pivot proof on the witness `u=22885787` produces a system of leaf/core equations whose exact F2 row-reduction is precisely the six equations above. Therefore every assignment of the other 39 Legendre bits preserves the same legal 22 rank-one leaf eliminations and leaves the 2x2 zero residual core. Hence

```text
rank_F2(M)=22=2n-2,
nullity_F2(H)=2,
dim_F2 Sel^2(E_rho,p/Q)=2.
```

This is a partial-Legendre theorem, not a full pattern-hash theorem.

## Chart B — codimension nine

A second leaf certificate on the same coarse support type requires only

```text
chi_3(p1)=1,
chi_3(p2)=0,
chi_d(p2)=1,
chi_f(p1)=0,
chi_f(p2)=0,
chi_f(7)=0,
chi_f(41)=1,
chi_f(q1)=0,
chi_f(q2)=0.
```

Again every omitted Legendre bit is free. Exact symbolic row-reduction gives codimension nine; the retained witness `u=35456387` has 22 legal leaf pivots and residual core `0_2`, so every arithmetic support satisfying Chart B also has `dim Sel^2=2`.

The two charts are sufficient conditions. Their union is not claimed necessary, exhaustive, or a classification of this coarse support type.

## EH conditions are uniform on the progression

The stronger progression gives

```text
u=2 (mod 3),
u=3 (mod 8),
u=2 (mod 5).
```

Set `b=2u+729` and `q=4u+729`. Since `gcd(u,729)=1`,

```text
gcd(u,b)=gcd(u,q)=gcd(b,q)=1.
```

Moreover `u=3 mod 8`, so u is not a square. If `u*b*q` were a square, pairwise coprimality would force u itself to be a square, contradiction. Thus

```text
|8Nd| = 2^4 * 3^6 * u*b*q
```

is not a square, and neither sign is a rational square. The 36-09EH no-4 condition therefore holds for every positive u in this progression, with no primality assumption.

The same `u=2 mod 5` computation used in 36-09EW gives the cleared 3-division polynomial

```text
3X^4+4X^2+4 (mod 5),
```

with values `4,1,3,3,1`; hence it has no root mod 5 and the no-3 condition is also uniform.

Consequently every actual arithmetic realization of the coarse support type satisfying Chart A or Chart B is EH-clean; by the retained fixed-p criterion its complete positive literal orbit is excluded.

## Exact arithmetic realizations

The existing EZ registry already contains the Chart-A witness

```text
u=22885787.
```

FA adds four disjoint realizations outside the previous 192-value registry:

```text
u=35456387   Chart B
u=433686107  Chart A
u=658407107  Chart B
u=728044787  Chart B
```

Each has the exact coarse support above, exact support-matrix rank 22, 22 legal leaf pivots, residual `0_2`, uniform EH no-4/no-3, and a four-point EK literal orbit. The four new literal orbits are pairwise disjoint and disjoint from the exact 192-value registry, so after CI consumption the fixed-p registry may move

```text
192 -> 208.
```

A targeted discovery scan was used to locate the displayed witnesses, but no bounded-window exhaustiveness or density statement is promoted.

## What FA changes

FA replaces one full-pattern-hash dependence by two exact partial-Legendre charts on a fixed coarse support type. Chart A fixes only 6 of 45 reciprocity bits; Chart B fixes 9 of 45. This is the first retained Stage36 condition in this route where a large complement of pairwise Legendre data is explicitly proved irrelevant to Selmer rank.

The next leaf is

```text
36-09FB_RHO_PARTIAL_LEGENDRE_CHART_ARITHMETIC_REALIZATION_PREFLIGHT.
```

Its purpose is to ask whether Chart A or B can be forced by arithmetic congruence/splitting conditions without first factoring a bounded list of u-values.

## Credit firewall

FA does not prove infinitely many chart realizations, does not classify all residual cores or all maximal-rank profiles, does not prove a uniform Sel2 theorem for every u in the progression, does not shrink the parent candidate ledger, and does not prove receiver/R29/Q11/endpoint/Perfect Cuboid closure.
