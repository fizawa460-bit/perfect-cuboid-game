# Stage14-4cr

Stage14-4cr combines merged `s7-30` and merged `4cq` on the same charged-once physical common-core strip.

The two valid block envelopes are

```text
E_30 <= max(theta+phi+1/8, 1-2theta),
E_Cayley <= 5/4-2theta.
```

Taking their minimum gives

```text
V(B) << B^(2/3+o(1)).
```

The unique possible `2/3` saturation block is

```text
theta=7/24,
phi=1/4,
c=1/3.
```

Stage14-4cr also splits the 4cq good common core exactly. With

```text
M=4*r*s*X*Y*epsilon_x*epsilon_k,
N=a*b*c*d,
```

define

```text
C_- = gcd(C_*,M-N),
C_+ = gcd(C_*,M+N).
```

Then

```text
C_-*C_+=C_*,
gcd(C_-,C_+)=1.
```

`C_+` is the same Gaussian orientation support of the two reciprocal plus norms; `C_-` is the opposite orientation support. Equivalently there are Gaussian divisors `Pi_+,Pi_-` with

```text
N(Pi_+)=C_+,
N(Pi_-)=C_-,
Pi_+Pi_- | Z_k,
Pi_+conj(Pi_-) | Z_xi.
```

The remaining receiver is

```text
TwoThirdsCayleyGaussianCommonGcdRootProductIncidence.
```

No mainline H is needed before the exact `h / C_bad / C_+ / C_-` decomposition is exhausted.
