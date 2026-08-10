# Stage14-4cu

Stage14-4cu compares the selected xi residual Gaussian orientation with the merged Cayley xi-plus orientation.

Exact cross-root cells

```text
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)),
H=H_S*H_T
```

force

```text
H_S^2|g_S,
H_T^2|g_T,
```

where `g_S,g_T` are residual-host coordinate gcds.  Choosing the larger cross cell and writing `g_star=B^(rho+o(1))` gives

```text
J_star >= B^(chi-3rho-o(1)),
chi=2theta+2phi-3/4.
```

The joint good core obeys

```text
J_star | (z1*r2*s2-z2*r1*s1)(z1*r2*s2+z2*r1*s1).
```

The nonzero product has exponent at most `1/4`, forcing a residual-gcd saving.  The zero branch forces a `B^(1/8)` common coordinate divisor into the k residual host.

The resulting whole-family theorem is

```text
V(B) << B^(19/32+o(1)).
```

with possible saturation only at

```text
theta=19/64,
phi=1/4,
chi=11/32,
rho=1/32,
J_star~B^(1/4).
```

Next receiver:

```text
NineteenThirtySecondsJointCoreCayleyResidualLinearProductIncidence
```

H decision: `MAINLINE_H_NEEDED=false`.

Next: `Stage14-4cv`.