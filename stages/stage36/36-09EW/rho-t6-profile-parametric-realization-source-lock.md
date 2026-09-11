# Stage36 36-09EW — T6-profile parametric realization preflight

## Purpose

36-09EU proves that on the fixed coarse profile

```text
D3,D3,D5,D7,P1,P7,Q1,Q1; shallow
```

the rho full-2 Selmer condition is exactly `rank_F2(B)=3`. 36-09EV then gives one isolated primitive realization. This leaf replaces isolated search by a one-variable arithmetic skeleton whose coarse profile, decisive Legendre matrix, and EH no-4/no-3 conditions are forced by congruence once five explicit prime-value conditions hold.

Entry authority is V278, exact head `4d24772fbb03edcc1ac7e45d39dc7cd437914b66`, CI `34408388995 / 102656758007`.

## One-variable family

Let

```text
k = 729 = 3^6,
u > 258,
a = 2u,
b = 2u+k.
```

Then

```text
N = a^2-b^2 = -k(4u+k),
d = ab = 2u(2u+k),
P = N+2d = 8u^2-k^2,
Q = N-2d = -(8u^2+8ku+k^2).
```

Impose the single CRT progression

```text
u = 6147 (mod 11480).
```

Equivalently

```text
u=3 (mod 8),
u=1 (mod 7),
u=38 (mod 41),
u=2 (mod 5).
```

The first three congruences imply

```text
7 | P,
41 | |Q|,
```

and define

```text
s=(8u^2-k^2)/7,
t=(8u^2+8ku+k^2)/41.
```

## Exact conditional profile theorem

Assume the five integers

```text
u,
2u+729,
4u+729,
s,
t
```

are all prime. No infinitude claim for such hits is made.

Because `u=3 mod 8`, the odd radical data are

```text
D = -2^4 * 3^6 * u * (2u+729) * (4u+729),
```

with odd labelled residues

```text
3        : D3,
u        : D3,
4u+729   : D5,
2u+729   : D7.
```

Also `P=7s` and `|Q|=41t`, with

```text
7=DUMMY_P7,
s=P1,
41=Q1,
t=Q1,
```

since `s=t=1 mod 8`. Thus every prime-tuple hit has exactly the fixed EU T6 coarse profile, with the shallow dyadic branch inherited from this parity pattern.

## Congruence-fixed rank-3 matrix

Use D-row order

```text
(3, u, 4u+729, 2u+729)
```

and decisive columns

```text
(s, 41, t).
```

Quadratic reciprocity and the defining divisibility relations reduce every entry to the fixed residues `u mod 7 = 1` and `u mod 41 = 38`. In the Stage36 0/1 Legendre-bit convention the matrix is identically

```text
B =
1 1 0
0 1 1
0 0 1
0 1 0.
```

Hence `rank_F2(B)=3` for every prime-tuple hit. By 36-09EU,

```text
dim_F2 Sel^2(E_rho,p/Q)=2.
```

This is a congruence-family theorem conditional only on the five displayed primality conditions; it is not a Bateman-Horn/Schinzel/Dickson infinitude theorem.

## EH torsion conditions are also uniform on the progression

The no-4 condition is automatic for every prime-tuple hit because

```text
8Nd = -2^4 * 3^6 * u * (2u+729) * (4u+729)
```

has three distinct odd primes to odd exponent, so neither sign is a rational square.

The extra congruence `u=2 mod 5` gives

```text
a=4 mod 5,
b=3 mod 5,
```

and the cleared 36-09EH 3-division polynomial has ascending coefficients

```text
[4,0,4,0,3] mod 5.
```

Thus `psi_3(X)=3X^4+4X^2+4` modulo 5, with values `4,1,3,3,1`; it has no root modulo 5. Therefore every prime-tuple hit also satisfies the EH no-3 condition.

Consequently every prime-tuple hit in this progression has empty retained physical receiver sector, and its full positive EK literal orbit is excluded.

## New exact realization

The progression is nonempty at the required arithmetic level. Take

```text
u = 1601867,
a = 3203734,
b = 3204463,
p = 3203734/3204463.
```

Then

```text
2u+729 = 3204463 prime,
4u+729 = 6408197 prime,
s = 2932546079153 prime,
t = 500906480617 prime,
```

and `u` itself is prime. Exact factorization is

```text
P = 7 * 2932546079153,
Q = -41 * 500906480617,
D = -2^4 * 3^6 * 1601867 * 3204463 * 6408197.
```

The direct Legendre replay gives the same fixed rank-3 matrix above. The no-4 integer is

```text
8Nd = -383676395401189735185168,
```

and the mod-5 no-3 witness is the uniform polynomial above.

The complete positive literal orbit is

```text
{3203734/3204463,
 3204463/3203734,
 729/6408197,
 6408197/729}.
```

It is disjoint from the previous exact 40-value registry, so this leaf provisionally raises the registry

```text
40 -> 44.
```

## What this does and does not solve

The useful gain is structural: T6 rank-3 realization is now reduced to one fixed arithmetic progression and five explicit prime-value checks, with both the Legendre rank and EH torsion conditions forced uniformly. The remaining obstacle to an infinite family is the simultaneous prime-value problem for three linear and two quadratic polynomials; this leaf does not claim that infinitely many hits exist.

The next exact question is therefore

```text
36-09EX_RHO_T6_CONTROLLED_RADICAL_RELAXATION_PREFLIGHT
```

which should ask whether exact primality of all five values can be weakened to controlled radical/factor patterns while preserving an exact support-rank certificate.

## Credit firewall

This leaf proves one new four-point fixed-p exclusion orbit after CI consumption and proves a conditional congruence-family implication. It does not prove infinitely many hits, exhaust all maximal-rank profiles, establish a uniform Sel2 theorem, shrink the parent candidate ledger, prove receiver emptiness, close R29/Q11, close the endpoint, or prove Perfect Cuboid nonexistence.
