# Stage36 36-09EH — generic rho quotient fixed-p exclusion criterion

## Purpose

36-09EG propagates the audited `p=2` obstruction only across the four positive parameters whose normalized genus-3 top equation is literally `C3_2`.

The present leaf extracts the **p-independent arithmetic mechanism** behind the successful rho quotient and turns it into a reusable sufficient criterion for excluding an arbitrary fixed physical rational parameter `p`.

This is a criterion/reduction theorem. It does not assert that every `p` satisfies the criterion and does not by itself add a new excluded parameter.

## Locked generic quotient

From hostile-audited 36-09O, write

```text
h = p - 1/p,
r = p + 1/p,
r^2 = h^2 + 4.
```

The rho quotient of the top genus-3 cover is

```text
S = t - 1/t,
V = y/t^2,
E_rho,p^quartic: V^2 = (S^2+r^2)(S^2+4r^2/h^2).
```

For the positive physical domain, `p` is rational, positive, nonzero and `p != 1`, hence `h != 0`. The values `h=+/-2` do not occur for rational `p`: solving `p-1/p=+/-2` gives quadratic equations with discriminant `8`.

The retained top boundary contains `t=0,+1,-1,infinity`.

## Uniform rational Weierstrass model

Expand the quartic as

```text
V^2 = S^4 + A S^2 + B^2,
A = r^2 + 4r^2/h^2,
B = 2r^2/h.
```

Use the standard even-quartic transformation, with the rational point `(S,V)=(0,B)` as origin:

```text
U = (V+B)/S^2,
W = S(U^2-1).
```

Then

```text
W^2 = (U^2-1)(2BU+A).
```

Setting `x=(2B)U`, `y=(2B)W` gives

```text
y^2 = (x-2B)(x+2B)(x+A).
```

Finally scale

```text
X = x*h^2/r^2,
Y = y*h^3/r^3.
```

Because `r^2=h^2+4`, the result is the uniform full-rational-2-torsion model

```text
E_rho,p^W: Y^2 = (X-4h)(X+4h)(X+r^2).
```

For `p=2`, `h=3/2`, `r=5/2`, the roots are `6,-6,-25/4`; multiplying `X` by `100` recovers the 36-09EE root set `600,-600,-625`. Thus the generic model specializes compatibly with the audited fixed-p2 model.

## Exact rational 4-torsion test

The nonzero rational 2-torsion x-coordinates are

```text
e1 = 4h,
e2 = -4h,
e3 = -r^2.
```

For a full-rational-2-torsion model, the standard halving criterion says `(ei,0)` is twice a rational point exactly when both differences from the other two roots are rational squares.

Using `r^2=h^2+4`:

```text
e1-e2 = 8h,
e1-e3 = r^2+4h = (h+2)^2,

e2-e1 = -8h,
e2-e3 = r^2-4h = (h-2)^2,

e3-e1 = -(h+2)^2,
e3-e2 = -(h-2)^2.
```

Since rational physical `p` never has `h=+/-2`, the last pair is strictly negative over Q and cannot be square. Therefore

```text
E_rho,p(Q) has rational order-4 torsion
iff 8h is a rational square or -8h is a rational square.
```

Hence the exact no-4-torsion condition is

```text
8h notin Q^2 and -8h notin Q^2.
```

## Rank-zero and odd-torsion reduction

The curve has full rational 2-torsion. The standard 2-descent exact sequence gives

```text
0 -> E(Q)/2E(Q) -> Sel^2(E/Q) -> Sha(E)[2] -> 0.
```

Because `dim_F2 E(Q)[2]=2`,

```text
dim_F2 Sel^2(E_rho,p/Q) = 2
```

forces

```text
rank E_rho,p(Q) = 0
```

(and also `Sha(E_rho,p)[2]=0`, though the latter is not needed for the direct rational-point criterion below).

Mazur's rational torsion classification, already source-locked by 36-09DZ, says that an elliptic curve over Q with full rational 2-torsion has torsion subgroup

```text
Z/2 x Z/2n, 1 <= n <= 4.
```

Therefore, once rational order-4 torsion is excluded, the only remaining enlargement beyond `(Z/2)^2` is the `n=3` case, which contains rational 3-torsion. Thus the two tests

```text
8h, -8h both nonsquares,
E_rho,p(Q)[3] = 0
```

together with rank zero imply

```text
E_rho,p(Q) = E_rho,p[2](Q) ~= (Z/2)^2.
```

A sufficient machine-checkable way to certify `E(Q)[3]=0` is to prove that the 3-division polynomial has no rational root. For

```text
Y^2 = X^3 + r^2 X^2 - 16h^2 X - 16h^2 r^2,
```

the 3-division polynomial is

```text
psi3(X) = 3X^4 + 4r^2 X^3 - 96h^2 X^2
          - 192h^2 r^2 X - 64h^2(r^4+4h^2).
```

No-rational-root is sufficient, not asserted necessary.

## Direct retained-open exclusion criterion

Assume for a fixed allowed rational `p`:

1. `dim_F2 Sel^2(E_rho,p/Q)=2`;
2. neither `8h` nor `-8h` is a rational square;
3. `E_rho,p(Q)[3]=0` (for example, `psi3` has no rational root).

Then

```text
E_rho,p(Q)=E_rho,p[2](Q).
```

Suppose a retained rational point existed on the top curve. Its rho image has

```text
S=t-1/t
```

and is a rational point of `E_rho,p`. Since retained `t` is finite and nonzero, this quotient point is affine. On the quartic model the only affine rational 2-torsion points have `S=0`; the other two 2-torsion points are the infinity branches. Hence

```text
S=0 -> t-1/t=0 -> t=+1 or -1,
```

contradicting the retained boundary.

Therefore the three displayed elliptic conditions imply

```text
U_ret(C3_p)(Q)=empty,
```

and by the hostile-audited generic 36-09O physical forward adapter the retained physical receiver sector over that fixed `p` is empty.

## Why this is stronger operationally than replaying 36-09EE

For future fixed parameters, one need not reproduce the full p=2 genus-3 pro-Selmer/Brauer computation merely to prove rational receiver emptiness. It is enough to certify on the single rho elliptic quotient:

```text
Sel2 dimension = 2,
no rational 4-torsion,
no rational 3-torsion.
```

The second condition is already reduced uniformly to the explicit square test `+/-8h notin Q^2`.

## Credit firewall

This leaf proves a conditional fixed-p exclusion theorem only. It does not claim:

```text
that every rational p satisfies the three conditions,
that any new p outside the 36-09EG orbit is excluded,
candidate_parameter_set_shrunk,
receiver_emptiness_proved,
R29_CAMP2_closed,
Q11_CAMPEDELLI_closed,
endpoint_closed,
perfect_cuboid_nonexistence_claim.
```
