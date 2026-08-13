# Stage14-4db

Stage14-4db consumes merged `Stage14-X13`, `Stage14-4da`, `Stage14-s7-42`, `Stage14-4cx`, and `Stage14-4cz` on latest main.

The entering theorem is already

```text
V(B) << B^(1/2+o(1)).
```

Stage14-4db does **not** claim a strict sub-square-root whole-family bound.  It changes the quantifier order on the remaining square-root band and proves that every fixed-power cross-root gcd stratum is already strict sub-square-root.

Use the X13/4da square-root-band notation

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=B^(s+o(1)),
J=B^(j+o(1)),
d=chi-j,
D0|H^2,
G=H^2/D0=B^(e+o(1)),
e=2s-d,
K=B^(kappa+o(1)),
a_col=1/2-2phi.
```

The key new quantifier order is to choose `H` before the lost core.  For fixed `H`,

```text
D0 | H^2
```

has only divisor-many possibilities.  Once `J`, `H`, and the endpoint-small decoration are fixed, `C=J*(C/J)` is therefore fixed up to `B^o(1)` possibilities.  The cross-root split `H=H_S H_T` is also divisor-many.

The merged fixed-`C` primitive-pair count remains

```text
B^(2phi-chi+o(1)).
```

The reduced column product satisfies

```text
K^2*G | R_col,
|R_col|<=B^(a_col+o(1)).
```

Because `G` is already fixed after `H,D0` are fixed, a nonempty `(s,kappa,d)` stratum has charged-once exponent

```text
j+s+kappa
+(2phi-chi)
+(a_col-2kappa-e)
=1/2-kappa-s.
```

Thus

```text
E_4db(s,kappa) <= 1/2-kappa-s.
```

Every fixed-power `H` or `K` stratum is strictly below square root.  Equality can survive only when

```text
H=B^o(1),
K=B^o(1).
```

Then `D0|H^2` forces

```text
C/J=B^o(1),
j=chi,
```

and all four odd cross-state root-gcd cells are subpolynomial.

The refined square-root receiver is

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullJointCoreSingleColumnIncidence
```

with

```text
theta=1/4,
5/24<=phi<=1/4,
chi=j=2phi-1/4,
H_S=H_T=K_x=K_y=B^o(1),
C/J=B^o(1),
column support<=B^(1/2-2phi+o(1)),
post-column reciprocal completion=B^o(1).
```

No mainline H/tH theorem is needed yet.  The next exact step is to exploit the globally odd-primitive reduced endpoint-linear pair after all common root-gcd and lost-core factors have disappeared at fixed-power scale.

Next: `Stage14-4dc`.
