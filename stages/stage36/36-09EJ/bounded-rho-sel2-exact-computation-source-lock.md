# Stage36 36-09EJ — bounded rho Sel2 exact computation source lock

## Purpose

36-09EH gives a fixed-parameter exclusion criterion for the rho elliptic quotient. 36-09EI proves that on the ordered primitive box

```text
p=a/b, 1<=a,b<=10, gcd(a,b)=1, a!=b,
```

all 62 parameters already satisfy the no-rational-4-torsion and no-rational-3-torsion parts. The sole remaining condition is

```text
dim_F2 Sel^2(E_rho,p/Q)=2.
```

This leaf computes those 62 Sel2 dimensions exactly. It then applies the already exact-green 36-09EH criterion to every row with Sel2 dimension 2.

## Integral full-2-torsion model

Put

```text
N=a^2-b^2,
M=a^2+b^2,
d=ab.
```

36-09EH gives the rho model with roots `4h,-4h,-r^2`, where `h=N/d` and `r=M/d`. Scaling `x=d^2 X`, `y=d^3 Y` gives the integral Q-isomorphic model

```text
E_{a,b}: y^2=(x-e1)(x-e2)(x-e3),
e1=4Nd,
e2=-4Nd,
e3=-M^2.
```

The root differences are

```text
e1-e2=8Nd,
e1-e3=(N+2d)^2,
e2-e3=(N-2d)^2.
```

Hence all bad primes are contained in the finite set of prime divisors of

```text
2*(e1-e2)*(e1-e3)*(e2-e3).
```

Call the resulting finite set `S_f`, always including 2. Outside `S_f`, the full-2 Kummer classes are unramified, so the global Sel2 group lies in

```text
Q(S,2)^2,
S={infinity} union S_f.
```

The ordered global squareclass generators per coordinate are `[-1]` followed by the primes of `S_f` in increasing order.

## Kummer coordinates

For a non-2-torsion point `(x,y)`, use the standard full-rational-2-torsion Kummer pair

```text
delta(x,y)=([x-e1],[x-e2]).
```

For the two basis 2-torsion points `T1=(e1,0)` and `T2=(e2,0)`, the limiting Kummer classes are

```text
delta(T1)=([(e1-e2)(e1-e3)],[e1-e2]),
delta(T2)=([e2-e1],[(e2-e1)(e2-e3)]).
```

These formulas follow directly by replacing the vanishing coordinate with the product of the two nonvanishing root differences in the usual full-2 descent map.

## Exact local images by theorem-saturated witnesses

36-09DW source-locks the local multiplication-by-two Euler characteristic used here. Because every `E_{a,b}` has full rational 2-torsion,

```text
dim_F2 E(Q_v)/2E(Q_v)=2  for odd finite v,
dim_F2 E(Q_2)/2E(Q_2)=3.
```

At the real place the cubic has three distinct real roots, so `E(R)` has two connected components and

```text
dim_F2 E(R)/2E(R)=1.
```

Thus a finite list of explicit local Kummer witnesses is exact as soon as its span reaches dimensions `2/3/1` at odd/Q2/real places respectively.

The verifier starts with the two displayed rational 2-torsion classes and then checks every integer `x` in the deterministic range

```text
-50 <= x <= 50
```

with `x` not a root. It tests whether `(x-e1)(x-e2)(x-e3)` is a square in `Q_v`; whenever it is, the associated Kummer pair is added. For all 62 rows and every required finite place, the resulting span reaches the theorem-supplied target dimension. The largest minimum witness bound actually needed is 47, attained at `(a,b,p)=(7,6,97)` and its reciprocal row.

Therefore the local images are exact; the bounded witness search is not used as an exhaustiveness theorem, only to saturate a known exact local dimension.

## Global intersection

For each row:

1. build the ambient `Q(S,2)^2` F2-space;
2. localize every global squareclass basis vector at every place in `S` using the same bit conventions as 36-09DW:
   - real: sign bit;
   - odd p: `(valuation parity, nonsquare-unit bit)`;
   - p=2: `(valuation parity, -1 bit, 5 bit)`;
3. require the localized pair to lie in the exact local Kummer image;
4. collect all resulting F2 linear constraints and compute the nullity.

That nullity is exactly `dim_F2 Sel^2(E_{a,b}/Q)`.

As a compatibility check, the rows `p=2` and `p=1/2` both reproduce Sel2 dimension 2 for the rho quotient, agreeing with the fixed-p2 EC computation up to Q-isomorphic scaling and coordinate basis.

## Exact 62-row result

The Sel2 dimension distribution is

```text
dim 2 : 14 rows
dim 3 : 14 rows
dim 4 : 30 rows
dim 5 :  4 rows
```

The exact `dim=2` rows are

```text
(1,2), (1,3), (1,5),
(2,1), (2,3), (2,7), (2,9),
(3,1), (3,2),
(5,1), (5,9),
(7,2),
(9,2), (9,5).
```

Equivalently the positive parameter values are

```text
{1/3,1/2,1/5,2,2/3,2/7,2/9,3,3/2,5,5/9,7/2,9/2,9/5}.
```

The canonical row encoding is

```text
a,b,semicolon-separated-S_f,ambient_dimension,constraint_rank,sel2_dimension
```

in lexicographic `(a,b)` order with a trailing newline. Its SHA-256 digest is

```text
1a1ef2d5c15d74062f6af417f88b70ec358012afceb8c18aa9d4b55c7133eeea
```

## New fixed-parameter exclusions

36-09EI already proves no4 and no3 for all 62 rows. Hence all 14 Sel2-dimension-2 rows satisfy the complete 36-09EH criterion and their retained physical receiver sectors are empty.

Four were already present in the 36-09EG literal `C3_2` orbit:

```text
{1/3,1/2,2,3}.
```

The ten genuinely new excluded positive parameters are

```text
{1/5,5,2/3,3/2,2/7,7/2,2/9,9/2,5/9,9/5}.
```

Thus, after CI consumption, the fixed-parameter exclusion registry may expand from 4 values to 14 values.

## Credit firewall

This bounded box is not an exhaustive authority-level parameter ledger for the physical receiver. Therefore this leaf does not prove

```text
candidate_parameter_set_shrunk,
receiver_emptiness_proved,
R29_CAMP2_closed,
Q11_CAMPEDELLI_closed,
endpoint_closed,
perfect_cuboid_nonexistence_claim.
```

The exact new credit is only ten additional fixed-p sector exclusions inside the tested primitive box.
