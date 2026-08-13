# Stage14-4ct

Stage14-4ct imports merged `4cs` and `s7-32` and works only at the unique surviving `5/8` corner

```text
theta=5/16,
phi=1/4.
```

The xi-switched residual host satisfies, after the finite 2-primary convention,

```text
Z_S=lambda_S^2 W_S,
oddpart(N(W_S))=C*v,
C=B^(3/8+o(1)),
v<=B^(1/8+o(1)).
```

For

```text
g=oddpart(gcd(Re(W_S),Im(W_S))),
C_bad=gcd(C,g^2),
C_good=C/C_bad,
d=g^2/C_bad,
```

Stage14-4ct proves exactly

```text
C_good | oddpart(N(W_S/g)),
d | v.
```

Since `W_S/g` is primitive at odd primes, every prime of `C_good` is `1 mod 4`; hence there is a unique Gaussian orientation divisor `Pi_C` up to a unit with

```text
N(Pi_C)=C_good,
Pi_C | W_S/g.
```

Thus

```text
W_S=g*Pi_C*T_C,
oddpart(N(T_C))=v/d.
```

If `g=B^(rho+o(1))`, the resulting alternative one-host count is

```text
E <= 5/8-rho.
```

Therefore any fixed-power residual-host coordinate gcd is power-saved.  The only possible `5/8` saturation has

```text
g=B^o(1),
C_good=B^(3/8+o(1)).
```

The remaining receiver is

```text
TopCornerPrimitiveXiResidualGaussianCoreAgreementIncidence.
```

No auxiliary H is needed.  Stage14-4cu should compare the canonical `Pi_C` orientation with the common-core primitive xi-agreement orientation and the Cayley `C_+/C_-` orientation before requesting any external theorem.