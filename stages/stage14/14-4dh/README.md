# Stage14-4dh

Stage14-4dh consumes merged `Stage14-4dg`, merged `Stage14-s7-49`, and merged `Stage14-X15`.

The stage has two exact purposes.

First, it synchronizes the s7-49 Gaussian root label with the X15 third Pythagorean projection.  If

```text
rho = m*n^{-1} (mod C_*),
rho^2 = -1 (mod C_*),
X_- = m*n,
X_0 = (m^2-n^2)/2,
```

then every physical root line satisfies

```text
X_0 = rho*X_- (mod C_*).
```

Thus the X15 third projection does not supply a second independent local density factor.

Second, it recombines the exact-conductor frequencies of s7-49 into Ramanujan sums.  For

```text
x_rho=m-rho*n,
```

the root-line indicator is

```text
1_{C_*|x_rho}
 = (1/C_*) * sum_{q|C_*} c_q(x_rho).
```

The `q=1` term is the already-known principal density.  For `q>1`, writing

```text
d=gcd(q,x_rho)
```

gives

```text
|c_q(x_rho)| <= d,
# {primitive quarter pairs: d|x_rho}
 <= B^o(1)*(1+B^(1/2)/d).
```

The Ramanujan amplitude `d` and root-line spacing `1/d` cancel exactly at fixed-power scale.  After summing `C_*~B^chi`, all nonzero conductors are bounded absolutely by `B^(1/2+o(1))`, uniformly for `1/6<=chi<=1/4`.

Therefore conductor loss is harmless for preserving the square-root theorem, but it does not yield a strict sub-square-root saving.

The remaining mainline object is a **same-root, signed Ramanujan physical correlation** whose principal term is still of square-root size.  Any strict improvement must either prove a genuine principal-density deficit under the full physical masks or exploit signed correlation across the Ramanujan conductor sum; taking absolute values conductor-by-conductor cannot suffice.

Current theorem:

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
```

The s route is active and owns its own next step `Stage14-s7-50`; this stage makes no s-route reactivation judgment.

Next mainline stage: `Stage14-4di`.
