# Stage14-4cg

Stage14-4cg consumes merged 4cf and couples its four Gaussian residual hosts before any fixed-host summation.

Main exact reductions:

```text
q_beta=q_gamma=:q_k,
q_S=q_T=:q_xi,
```

and, with

```text
H_k^+=delta^2 s1^2 s2^2+alpha^2 r1^2 r2^2,
H_xi^+=J^2 y1^2 y2^2+R^2 x1^2 x2^2,
```

```text
g1*g2*K_switch*H_k^+=2*Xi_switch*H_xi^+.
```

After removing switched odd parts, both plus factors have the same odd common core `C`; this `C` survives into both residual norms. Thus

```text
q_k=C*u,
q_xi=C*v,
u*v<=B^(1/4+o(1)).
```

The endpoint cell exponents are additionally confined to

```text
0<=theta-phi<=1/8,
theta+phi>=3/8
```

up to `o(1)` widths.

No new whole-family saving is claimed. The next receiver is `CoupledCommonCoreGaussianResidualIncidence`; Stage14-4ch should attack bounded physical-lift/reconstruction before importing an external incidence theorem.
