# Stage14-4es — close the diffuse subpolynomial complementary-quotient branch

## Status

`COMPLETE_DIFFUSE_SUBPOLYNOMIAL_COMPLEMENTARY_QUOTIENT_NORM_VALUE_SAVING`

Consumes batch-local `Stage14-4er` and merged `Stage14-4ep`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Work on branch D0:

```text
N=X0^2+Y0^2=C*m,
C=B^(kappa+o(1)),
1/6<=kappa<=1/4,
m=B^o(1).
```

There are at most

```text
B^(kappa+o(1))
```

possible exact common-core integers in one exponent cell and only `B^o(1)` possible exact integers `m` in the subpolynomial quotient cell. Hence the number of possible norm values satisfies

```text
# {N=C*m} <= B^(kappa+o(1)) <= B^(1/4+o(1)).
```

Merged 4ep proves that the charged physical candidate projection

```text
physical candidate -> N=X0^2+Y0^2
```

has `B^o(1)` fiber after the existing divisor/primitive-representation/reverse-reconstruction decorations are charged once.

Therefore the complete D0 physical contribution satisfies

```text
V_D0(B) << B^(1/4+o(1))
```

and is fixed-power below the global square-root barrier.

```text
DIFFUSE_SMALL_QUOTIENT_BRANCH_BOUND_EXPONENT=1/4
DIFFUSE_SMALL_QUOTIENT_BRANCH_STRICTLY_SUBSQRT=true
DIFFUSE_SMALL_QUOTIENT_BRANCH_CLOSED=true
```

No Gaussian split-prime density or root-line spacing is recharged. The saving comes solely from the norm-value support after `m` becomes subpolynomial.

Thus every diffuse square-root-saturating sequence must lie on branch D1 with a genuinely polynomial complementary quotient:

```text
m=B^(lambda+o(1)),
lambda>0.
```

Remaining diffuse receiver:

```text
DiffusePolynomialComplementaryQuotientCanonicalAllocationPrimitiveGaussianNormFactorCorrelation.
```

```text
STAGE14_4ES=COMPLETE_DIFFUSE_SUBPOLYNOMIAL_COMPLEMENTARY_QUOTIENT_NORM_VALUE_SAVING
DIFFUSE_SMALL_QUOTIENT_BRANCH_BOUND_EXPONENT=1/4
DIFFUSE_SMALL_QUOTIENT_BRANCH_CLOSED=true
DIFFUSE_SATURATION_REQUIRES_POLYNOMIAL_COMPLEMENTARY_QUOTIENT=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4et
```
