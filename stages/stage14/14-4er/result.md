# Stage14-4er — quotient-scale split of the diffuse primitive Gaussian norm factor

## Status

`COMPLETE_DIFFUSE_PRIMITIVE_NORM_FACTOR_QUOTIENT_SCALE_SPLIT`

Consumes merged `Stage14-4ep`, merged `Stage14-s7-72..74`, merged `Stage14-q13`, and batch-local `Stage14-4eq` only for route bookkeeping.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Merged 4ep gives the diffuse accepted-incidence equation

```text
N=X0^2+Y0^2=C*m,
gcd(X0,Y0)=1,
gcd(C,X0Y0)=1,
```

with `B^o(1)` fiber from a charged physical candidate to its norm value `N`, and only divisor-many choices of `C|N` once `N` is fixed.

Freeze one polynomial common-core exponent cell

```text
C=B^(kappa+o(1)),
1/6<=kappa<=1/4,
```

using the merged square-root equality band. Also freeze the complementary quotient exponent

```text
m=B^(lambda+o(1)),
lambda>=0.
```

This yields the exact dichotomy

```text
D0: lambda=0,  m=B^o(1),
D1: lambda>0,  m polynomial.
```

No independence between `C,m` and the canonical physical background is assumed.

The small-quotient and polynomial-quotient branches are arithmetically different: on D0 the norm value is essentially the common core up to a subpolynomial multiplier; on D1 the primitive Gaussian norm has two genuinely growing rational factors.

```text
DIFFUSE_QUOTIENT_SCALE_CELL_DEFINED=true
DIFFUSE_SMALL_QUOTIENT_BRANCH_DEFINED=true
DIFFUSE_POLYNOMIAL_QUOTIENT_BRANCH_DEFINED=true
COMMON_CORE_QUOTIENT_INDEPENDENCE_ASSUMED=false
```

No saving is claimed at this split itself. Stage14-4es will count D0 directly through the norm-value projection.

```text
STAGE14_4ER=COMPLETE_DIFFUSE_PRIMITIVE_NORM_FACTOR_QUOTIENT_SCALE_SPLIT
DIFFUSE_COMMON_CORE_EXPONENT_RANGE=[1/6,1/4]
DIFFUSE_QUOTIENT_SCALE_CELL_DEFINED=true
DIFFUSE_SMALL_QUOTIENT_BRANCH_DEFINED=true
DIFFUSE_POLYNOMIAL_QUOTIENT_BRANCH_DEFINED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4es
```
