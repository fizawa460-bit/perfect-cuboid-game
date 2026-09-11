# Stage36 36-09EV — exact T6-profile rank-3 realization

## Purpose

36-09EU proves, on the entire fixed coarse profile

```text
D3,D3,D5,D7,P1,P7,Q1,Q1; shallow,
```

that the rho full-2 Selmer condition is exactly

```text
dim_F2 Sel^2(E_rho,p/Q)=2  iff  rank_F2(B)=3,
```

where `B` is the 4x3 matrix of directed Legendre bits from the four D-support vertices to the `P1,Q1,Q1` vertices. This leaf certifies one new primitive realization of that family and then independently discharges the 36-09EH no-4/no-3 conditions.

Entry authority is V276, exact head `4aecaa024f2e46273d15f8dc5f9e27015bc05347`, CI `34400789925 / 102631882375`.

## Primitive realization

Take

```text
(a,b)=(4802,5531),
p=4802/5531.
```

It is primitive and positive, with `a!=b`. Put

```text
N=a^2-b^2=-7532757,
d=ab=26559862,
P=N+2d=45586967,
Q=N-2d=-60652481,
D=P^2-Q^2=8Nd=-1600551891196272.
```

The exact factorizations needed for the labelled radical datum are

```text
P = 73 * 624479,
Q = -17 * 3567793,
D = -2^4 * 3^6 * 7^4 * 5531 * 10333.
```

Hence the odd labelled/mod-8 support is exactly

```text
D3 : 3,
D3 : 5531,
D5 : 10333,
D7 : 7,
P1 : 73,
P7 : 624479,
Q1 : 17,
Q1 : 3567793.
```

The dyadic branch is shallow, so this is exactly the 36-09EU coarse profile.

## Rank-3 matrix

Order the D vertices as `(3,5531,10333,7)`, and the three decisive columns as `(P1,Q1,Q1)=(73,17,3567793)`. In the Stage36 Legendre-bit convention the exact matrix is

```text
B =
0 1 0
1 1 0
1 1 0
1 1 1.
```

It has rank `3` over F2. Therefore 36-09EU gives

```text
dim_F2 Sel^2(E_rho,4802/5531/Q)=2.
```

No parameter-specific local point search or full Selmer recomputation is used.

## Independent EH torsion conditions

The 36-09EH rational 4-torsion test is controlled by `±8h`. Clearing denominators gives the integral square test on

```text
8Nd = -1600551891196272.
```

Its absolute value is not a square, so neither sign satisfies the rational-square condition.

For rational 3-torsion, use the exact 36-09EH division polynomial with denominators cleared as in 36-09EI. Modulo 5 its ascending coefficients are

```text
[4,0,4,0,3],
```

so

```text
psi_3(X)=3X^4+4X^2+4 (mod 5).
```

Its values on `X=0,1,2,3,4` are

```text
4,1,3,3,1,
```

hence it has no root in F5 and therefore no rational root. Thus the rational 3-torsion condition is also discharged.

By 36-09EH, the retained physical receiver sector for `p=4802/5531` is empty.

## Literal orbit closure

The exact 36-09EK positive literal orbit is

```text
{p,1/p,|c(p)|,1/|c(p)|},
c(p)=(p+1)/(p-1).
```

For this seed,

```text
|a-b|/(a+b)=729/10333.
```

Therefore the complete positive literal orbit is

```text
{4802/5531, 5531/4802, 729/10333, 10333/729}.
```

All four parameters define the same retained top curve and hence all four fixed-p receiver sectors are empty. They are disjoint from the previous exact 36-value registry, so the registry grows

```text
36 -> 40.
```

## Next leaf

The next useful question is no longer another exact-hash search. The EU criterion suggests searching for arithmetic constructions that force the T6 coarse profile and one nonzero 3x3 minor of `B`:

```text
36-09EW_RHO_T6_PROFILE_PARAMETRIC_REALIZATION_PREFLIGHT.
```

## Credit firewall

This leaf proves four additional fixed-p exclusions only. It does not prove the T6 coarse profile exhaustive, a uniform Sel2 theorem, a parent candidate-ledger shrink, receiver emptiness, R29/Q11 closure, endpoint closure, or Perfect Cuboid nonexistence.
