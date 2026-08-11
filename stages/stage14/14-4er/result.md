# Stage14-4er — pin the diffuse norm-factor scales after radial-gcd closure

## Status

`COMPLETE_DIFFUSE_NORM_FACTOR_SCALE_PINNING_TO_TWO_POLYNOMIAL_FACTORS`

Consumes batch-local `Stage14-4eq`, merged `Stage14-4ep`, merged `Stage14-4dd/4de`, and the merged square-root equality packet.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering diffuse norm-factor receiver

Merged 4ep rewrites every accepted diffuse common-core candidate as

```text
N=X0^2+Y0^2=C*m,
```

with

```text
gcd(X0,Y0)=1,
gcd(C,X0Y0)=1,
C=B^(kappa+o(1)),
kappa>0,
```

and with `B^o(1)` projection fiber from the full physical candidate to `N`.

4ep left the complementary quotient scale

```text
m=B^(lambda+o(1)), lambda>=0
```

for the next internal audit.

## 2. 4eq removes the only possible polynomial radial loss

The raw opposite reciprocal signed factors satisfy

```text
X=hX0,
Y=hY0,
h=B^o(1)
```

by 4eq.  On the merged square-root equality packet, the two opposite signed linear factors are quarter-scale:

```text
X,Y=B^(1/4+o(1)).
```

Therefore the primitive pair has the same scale:

```text
X0,Y0=B^(1/4+o(1)),
```

and hence

```text
N=X0^2+Y0^2=B^(1/2+o(1)).
```

```text
DIFFUSE_PRIMITIVE_NORM_SCALE=1/2
RADIAL_GCD_DOES_NOT_CHANGE_NORM_EXPONENT=true
```

## 3. The common-core exponent remains in the square-root equality interval

On the equality band

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4.
```

The good primitive common core `C` differs from the physical common core only by `B^o(1)` support, so

```text
kappa=chi+o(1),
1/6<=kappa<=1/4.
```

Since `N=Cm` and `N=B^(1/2+o(1))`, the quotient exponent is forced:

```text
lambda=1/2-kappa.
```

Thus

```text
1/4<=lambda<=1/3.
```

In particular the complementary quotient is always genuinely polynomial on every diffuse square-root packet:

```text
m=B^(lambda+o(1)),
lambda>=1/4.
```

```text
DIFFUSE_QUOTIENT_EXPONENT_PINNED=true
DIFFUSE_QUOTIENT_EXPONENT=lambda_equals_1_2_minus_kappa
DIFFUSE_QUOTIENT_ALWAYS_POLYNOMIAL=true
NEAR_FULL_COMMON_CORE_m_Bo1_BRANCH_EMPTY=true
```

## 4. Updated diffuse receiver

The diffuse branch is no longer a generic factorization with an arbitrary small complementary quotient.  It consists only of two polynomial factors of a square-root-scale primitive Gaussian norm:

```text
N=C*m,
N=B^(1/2+o(1)),
C=B^(kappa+o(1)),       1/6<=kappa<=1/4,
m=B^(1/2-kappa+o(1)),  1/4<=1/2-kappa<=1/3.
```

Both factors remain selected by the same canonical physical witness; independence is not assumed.

Call the updated receiver

```text
DiffuseTwoPolynomialFactorCanonicalAllocationPrimitiveGaussianNormCorrelation.
```

This is a scale pinning, not a power saving by itself: the naive product support `C*m` still has exponent `1/2`.

## Boundary

```text
STAGE14_4ER=COMPLETE_DIFFUSE_NORM_FACTOR_SCALE_PINNING_TO_TWO_POLYNOMIAL_FACTORS
DIFFUSE_PRIMITIVE_NORM_SCALE=1/2
DIFFUSE_COMMON_CORE_EXPONENT_RANGE=[1/6,1/4]
DIFFUSE_QUOTIENT_EXPONENT=lambda_equals_1_2_minus_kappa
DIFFUSE_QUOTIENT_EXPONENT_RANGE=[1/4,1/3]
DIFFUSE_QUOTIENT_ALWAYS_POLYNOMIAL=true
NEAR_FULL_COMMON_CORE_m_Bo1_BRANCH_EMPTY=true
CURRENT_DIFFUSE_RECEIVER=DiffuseTwoPolynomialFactorCanonicalAllocationPrimitiveGaussianNormCorrelation
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4es
```
