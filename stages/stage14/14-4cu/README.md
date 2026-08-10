# Stage14-4cu

Stage14-4cu consumes merged `4ct`, `s7-32`, `4cs`, and `4cr`.

The stage compares the Gaussian orientation of a selected xi residual host `W_S` or `W_T` with the xi plus-host orientation used by the Cayley split.  The cross-root gcd

```text
H=oddpart(gcd(x1*x2,y1*y2))
```

splits exactly into

```text
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)),
H=H_S*H_T.
```

The matched cross cell forces a square into the coordinate gcd of the corresponding residual host.  Choosing the larger cross cell gives a selected residual gcd `g_star=B^(rho+o(1))` and a joint Cayley/residual good core

```text
J_star >= B^(chi-3rho-o(1)),
chi=2theta+2phi-3/4.
```

Primewise orientation comparison gives

```text
J_star | L_-*L_+,
L_-=z1*r2*s2-z2*r1*s1,
L_+=z1*r2*s2+z2*r1*s1.
```

If the product is nonzero, `|L_-L_+|<=B^(1/4+o(1))`, forcing a positive residual gcd when `chi>1/4`.  Combining this with the gcd-stratified xi one-host count gives

```text
E_nonprop<=19/32.
```

If `L_-=0`, the two `z` roots share a gcd of exponent `1/8`; that gcd survives into the k residual host and gives

```text
E_prop<=9/16.
```

Therefore

```text
V(B) << B^(19/32+o(1)).
```

The unique possible saturation of the new envelope is

```text
theta=19/64,
phi=1/4,
chi=11/32,
rho=1/32,
log_B J_star=1/4.
```

The next receiver is

```text
NineteenThirtySecondsJointCoreCayleyResidualLinearProductIncidence
```

and the next mainline task is `Stage14-4cv`.

H decision:

```text
MAINLINE_H_NEEDED=false
```

No t-route theorem is cross-promoted.