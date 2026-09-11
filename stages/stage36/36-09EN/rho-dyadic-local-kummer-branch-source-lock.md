# Stage36 36-09EN — exact dyadic rho local Kummer branch formula

## Purpose

36-09EM closes every odd local Kummer block for the square-Legendre rho family. The only remaining local input in the exact 36-09EL Sel2 matrix is

```text
W_2 = delta_2(E(Q_2))
subset (Q_2^*/Q_2^{*2})^2,
```

for

```text
E: y^2=X(X-P^2)(X-Q^2),
delta(X,y)=([X],[X-P^2]).
```

This leaf gives a complete uniform dyadic formula.

We use the 36-09DW Q2 squareclass bit order

```text
Q_2^*/Q_2^{*2} ~= F2^3,
bits=(v2 parity,-1 bit,5 bit).
```

The exact local `[2]` Euler characteristic gives

```text
dim_F2 W_2=3.
```

## Remove the common square power

For primitive `(a,b)`, 36-09EL gives

```text
gcd(P,Q) in {1,2}.
```

Put

```text
r=v2(gcd(P,Q)) in {0,1},
A=P/2^r,
B=Q/2^r.
```

Then `A,B` are odd. The change

```text
X=2^(2r) Z,
y=2^(3r) Y
```

is a Q2-isomorphism and multiplies both Kummer coordinates only by squares, so it does not change their squareclasses. Thus it suffices to study

```text
Y^2=Z(Z-A^2)(Z-B^2)
```

with odd `A,B`.

Set

```text
m=v2(A^2-B^2)=v2(P^2-Q^2)-2r.
```

Because odd squares are `1 mod 8`, always `m>=3`; the Stage36 arithmetic gives the stronger `m>=4`:

- if `a,b` have opposite parity, `r=0`, `v2(a^2-b^2)=0`, and `m=3+v2(ab)>=4`;
- if `a,b` are both odd, `r=1`, `v2(a^2-b^2)>=3`, and `m=1+v2(a^2-b^2)>=4`.

Hence only two dyadic depth branches occur: `m=4` and `m>=5`.

## Deep branch: m>=5

Here

```text
A^2 ≡ B^2 mod 32.
```

We claim the first Kummer coordinate is always trivial.

If `v2(Z)>0`, then `Z-A^2` and `Z-B^2` are odd and their quotient is `1 mod 8` because their difference is divisible by `32`. Hence they have the same squareclass, and the equation forces `[Z]=1`.

If `Z` is odd and `v2(Z-A^2)<=2`, the same quotient argument again shows `(Z-A^2)/(Z-B^2)` is a square; the equation forces `[Z]=1`. If instead `v2(Z-A^2)>=3`, then

```text
Z ≡ A^2 ≡1 mod 8,
```

so `Z` is already a square unit.

Thus every local point has `[Z]=1`, hence

```text
W_2 subset {1} x (Q_2^*/Q_2^{*2}).
```

The right side has dimension three, equal to the exact local Kummer dimension. Therefore

```text
W_2={1} x (Q_2^*/Q_2^{*2}).
```

In six-bit concatenated form:

```text
span{
 (0,0,0, 1,0,0),
 (0,0,0, 0,1,0),
 (0,0,0, 0,0,1)
}.
```

## Shallow branch: m=4

Now write

```text
A^2-B^2=16c,
c odd.
```

We show

```text
[X] in <5>,
[X-A^2] has even valuation,
```

so

```text
W_2 subset <5> x < -1,5 >.
```

The right side has dimension `1+2=3`; equality then follows from `dim W_2=3`.

### Z even

If `v2(Z)>0`, both `Z-A^2` and `Z-B^2` are odd. Their quotient is `1 mod 8` because their difference is divisible by `16`. Hence the equation forces `[Z]=1`. The second coordinate is a unit squareclass, so its valuation bit is zero.

### Z odd

Put

```text
z=Z-A^2.
```

Then the third factor is `z+16c`.

- `v2(z)=1`: the ratio `(z+16c)/z` is `1 mod 8`, so the product of the two last factors is a square. But `Z=A^2+z` is `3 or 7 mod 8`, not a square unit. No local point occurs.
- `v2(z)=2`: the ratio has squareclass `[5]`. Also `Z ≡5 mod 8`. Thus `[Z]=[5]`, and the second coordinate has even valuation.
- `v2(z)=3`: `Z ≡1 mod 8` is square, but `(z+16c)/z` is `3 or 7 mod 8`, nonsquare. No local point occurs.
- `v2(z)=4`: `Z ≡1 mod 8`; the equation forces `v2(z+16c)` even. The second coordinate already has even valuation.
- `v2(z)>4`: `z+16c` has valuation exactly four; parity of the equation forces `v2(z)` even. Again `Z ≡1 mod 8`.

Hence the only possible first-coordinate squareclasses are `[1]` and `[5]`, while the second coordinate has valuation parity zero. Therefore

```text
W_2=<5> x < -1,5 >.
```

In six-bit form:

```text
span{
 (0,0,1, 0,0,0),
 (0,0,0, 0,1,0),
 (0,0,0, 0,0,1)
}.
```

## Primitive-input branch criterion

The shallow condition `m=4` is equivalent to exactly one of:

```text
1. a,b have opposite parity and v2(ab)=1;
2. a,b are both odd and v2(a^2-b^2)=3.
```

All other primitive positive pairs with `a!=b` are in the deep branch `m>=5`.

Thus `W_2` can be selected without any point search.

## Deterministic compatibility replay

The verifier replays the exact 36-09EJ Q2 Kummer computation for all 62 AX-box rows, transforms EJ's Kummer coordinates to the EL coordinates, and checks the above branch formula exactly. Both dyadic branches occur in the replay.

This bounded replay is a regression check. The uniform theorem is the valuation proof above.

## Exact gain

Together 36-09EM and 36-09EN now provide closed local Kummer formulas at every required place. Therefore the 36-09EL matrix

```text
M_Sel2(a,b)
```

is a fully explicit finite arithmetic algorithm for every primitive rational parameter `p=a/b`.

This does not imply that its nullity is always two. The next leaf is

```text
36-09EO_RHO_SYMBOLIC_SEL2_EVALUATOR_AND_PATTERN_PREFLIGHT,
```

which should evaluate the closed matrix without local point searches and identify a genuine arithmetic criterion/pattern for `Sel2_dim=2`.

## Credit firewall

```text
dyadic_local_kummer_branch_formula_complete = true
all_local_kummer_branch_formulas_complete = true
uniform_Sel2_dimension_2_theorem = false
new_fixed_parameter_exclusion = false
candidate_parameter_set_shrunk = false
receiver_emptiness_proved = false
R29_CAMP2_closed = false
Q11_CAMPEDELLI_closed = false
endpoint_closed = false
perfect_cuboid_nonexistence_claim = false
```
