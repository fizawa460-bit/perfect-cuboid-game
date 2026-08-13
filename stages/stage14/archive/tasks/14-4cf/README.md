# Stage14-4cf

This stage consumes merged Stage14-4ce and Stage14-s7-20.

The balanced switched-cell square divisibilities are lifted from rational norm divisibility to exact Gaussian square divisibility:

```text
Z_c = lambda_c^2 W_c,
N(lambda_c)=c_odd,
```

for `c in {beta,gamma,S,T}`.

The four residual norms are at most `B^(1/2+o(1))`; at the lower balanced edges they are `B^o(1)`. This removes independent local-density heuristics from the mainline receiver, but fixed-host divisor bounds do not globalize because the hosts move with the physical pair.

Current receiver:

```text
BalancedFourHostGaussianSquareDivisorIncidence
```

Current whole-family exponent remains `7/8`.

```text
MAINLINE_H_NEEDED=false
NEXT=Stage14-4cg
```

See `result.md` for the exact proof and boundary.
