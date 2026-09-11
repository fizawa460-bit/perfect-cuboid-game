# Stage36 36-09EL — square-Legendre rho family and symbolic Sel2 matrix preflight

## Purpose

36-09EJ computes exact `Sel^2` dimensions for a bounded 62-row parameter box by intersecting exact local full-2 Kummer images. 36-09EK closes the resulting fixed-parameter exclusions under literal top-curve symmetry. The present leaf extracts the exact **scalable algebraic form** of that computation.

The goal is not to enlarge the bounded box. It is to isolate the finite symbolic data needed for a uniform or family-level Sel2 criterion and to rule out an over-compressed one-squareclass model that the exact EJ data falsify.

The formal Arsenal match is `S34-W01 SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT`: retain exact factor/gcd/valuation support and only then reduce to a finite F2 branch problem. This card supplies a proof pattern only; all formulas below are derived afresh for the Stage36 rho family.

## Exact square-Legendre normalization

For primitive positive `p=a/b`, `a!=b`, put

```text
N=a^2-b^2,
d=ab,
M=a^2+b^2,
P=N+2d=a^2+2ab-b^2,
Q=N-2d=a^2-2ab-b^2.
```

36-09EJ uses the integral rho model

```text
y^2=(x-4Nd)(x+4Nd)(x+M^2).
```

Translate

```text
X=x+M^2.
```

The three roots become exactly

```text
0,
M^2+4Nd=P^2,
M^2-4Nd=Q^2,
```

because `M^2=N^2+4d^2`. Hence

```text
y^2=X(X-P^2)(X-Q^2).
```

Neither `P` nor `Q` can vanish for rational positive `p`: `P=0` or `Q=0` gives a quadratic equation in `p` with discriminant `8`.

Scaling

```text
u=X/P^2,
v=y/P^3,
s=Q/P
```

gives the exact square-Legendre family

```text
E_s: v^2=u(u-1)(u-s^2).
```

Thus the Legendre parameter is itself a rational square, `lambda=s^2`.

## Exact prime-support factorization

The root differences in the translated integral model are

```text
P^2,
Q^2,
D=P^2-Q^2=8Nd.
```

Write `g=gcd(|P|,|Q|)`. For primitive `(a,b)`, the same parity calculation used elsewhere in Stage36 gives

```text
g in {1,2}.
```

With `P0=P/g`, `Q0=Q/g`, one has `gcd(P0,Q0)=1` and

```text
P0^2-Q0^2 = 8ab(a^2-b^2)/g^2.
```

Therefore every odd bad prime belongs to one of the exact arithmetic branches

```text
q | P0,
q | Q0,
q | a,
q | b,
q | a^2-b^2,
```

with overlaps controlled by the displayed coprimality and primitive input. This is the factor-level data that a scalable Sel2 matrix must retain.

## Generic F2 Sel2 matrix template

Let `S_f` be the finite primes dividing the three root differences, together with `2`, and let

```text
G=[-1] union sorted(S_f).
```

The global full-2 descent ambient space is

```text
V_S = Q(S,2)^2 ~= F2^(2|G|).
```

For each `v in {infinity} union S_f`, let

```text
L_v : V_S -> (Q_v^*/Q_v^{*2})^2
```

be the explicit squareclass localization matrix in the 36-09DW bit conventions, and let

```text
W_v = delta_v(E_s(Q_v))
```

be the local Kummer image. Its exact dimension is

```text
1 at infinity,
3 at Q_2,
2 at odd Q_q.
```

Choose any F2 basis of the annihilator `W_v^perp` for the ordinary dot product in the chosen squareclass bit coordinates. Stack the rows

```text
W_v^perp * L_v
```

for all required places. Call the resulting matrix `M_Sel2(a,b)`. Then exactly

```text
dim_F2 Sel^2(E_rho,p/Q)
 = 2|G| - rank_F2 M_Sel2(a,b).
```

This is already a finite symbolic matrix theorem. The only remaining non-formal input is a branch formula for `W_v` in terms of local arithmetic data of `P,Q,N,d`.

## A one-squareclass compression is false

It would be tempting to make `W_q` depend only on the local squareclass of

```text
D=P^2-Q^2.
```

The exact EJ local Kummer computation disproves this.

Use the translated full-2 model and Kummer coordinates

```text
delta(X,y)=([X],[X-P^2]).
```

At `q=17`, both of the following primitive rows have

```text
[D]=[1] in Q_17^*/Q_17^{*2}.
```

### Row (a,b)=(1,5)

```text
P=-14,
Q=-34,
17 | Q,
17 does not divide P.
```

The exact saturated local Kummer image is

```text
W_17 = span{(1,0,0,0),(0,1,0,0)},
```

where each squareclass coordinate uses the odd-prime bit order `(valuation parity, nonsquare-unit bit)`.

### Row (a,b)=(1,7)

```text
P=-34,
Q=-62,
17 | P,
17 does not divide Q.
```

The same local `D` squareclass occurs, but the exact saturated image is

```text
W_17 = span{(1,0,1,0),(0,1,0,1)}.
```

The two subspaces are different. Therefore

```text
local squareclass of D alone != local Kummer branch.
```

Any Monsky-style compression for this family must retain at least the branch information distinguishing divisibility/residue data of `P` and `Q` (and, at other support primes, the corresponding `N,d` branches).

## Exact gain and next obligation

36-09EL establishes:

1. the exact square-Legendre normalization `v^2=u(u-1)(u-s^2)`;
2. the exact finite prime-support factorization;
3. the exact global F2 localization/annihilator matrix formula for Sel2 dimension;
4. an explicit counterexample to a false single-`D`-squareclass local model.

It does **not** yet provide closed formulas for every local branch `W_v`, and therefore it does not add new fixed-p exclusions beyond the 16-value registry already promoted by 36-09EK.

The next leaf is

```text
36-09EM_RHO_FULL2_LOCAL_KUMMER_BRANCH_FORMULA_PREFLIGHT
```

whose task is to derive exact odd-prime and dyadic branch formulas for `W_v` from the factor classes of `P,Q,N,d` and local Hilbert/Legendre-symbol data.

## Credit firewall

```text
uniform_Sel2_dimension_2_theorem = false
new_fixed_parameter_exclusion = false
candidate_parameter_set_shrunk = false
receiver_emptiness_proved = false
R29_CAMP2_closed = false
Q11_CAMPEDELLI_closed = false
endpoint_closed = false
perfect_cuboid_nonexistence_claim = false
```
