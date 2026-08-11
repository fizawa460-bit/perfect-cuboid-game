# Stage14-4et — Gaussian bilinear factorization of the diffuse coprime norm-factor survivor

## Status

`COMPLETE_DIFFUSE_COPRIME_NORM_FACTOR_TO_GAUSSIAN_BILINEAR_PRODUCT_REDUCTION`

Consumes batch-local `Stage14-4es`, merged `Stage14-4ep`, and the frozen Gaussian root-orientation data from the common-core packet.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering primitive coprime norm factorization

The diffuse saturation packet now has

```text
N=X0^2+Y0^2=C*m,
gcd(X0,Y0)=1,
gcd(C,m)=B^o(1),
N=B^(1/2+o(1)),
C=B^(kappa+o(1)),
1/6<=kappa<=1/4,
m=B^(1/2-kappa+o(1)).
```

Peel the `B^o(1)` common support and the finite 2-primary decoration.  At fixed-power scale we may therefore treat

```text
gcd(C,m)=1
```

with both factors odd.

## 2. Primitive sum-of-two-squares support is split-prime support

Let

```text
z:=X0+iY0 in Z[i].
```

Because `gcd(X0,Y0)=1`, no odd prime `p=3 mod 4` can divide `N(z)`: if it did, the standard sum-of-two-squares local argument would force `p|X0,Y0`.

Hence, after the finite 2-primary peel, every rational prime dividing `N=Cm` is split in `Z[i]`.

This is not a new density saving: Gaussian splitting has already been charged in the Stage14 physical packet.

```text
PRIMITIVE_NORM_ODD_SUPPORT_GAUSSIAN_SPLIT=true
GAUSSIAN_SPLITTING_RECHARGE_ALLOWED=false
```

## 3. The frozen common-core root orientation selects a Gaussian divisor of norm C

For every prime power of `C`, the physical common-core packet already freezes one root of `-1` and therefore one of the two conjugate Gaussian prime orientations.  Since `C|N(z)` and `gcd(C,X0Y0)=1`, those local choices assemble, up to units and `B^o(1)` endpoint decorations, into a Gaussian divisor

```text
alpha | z,
N(alpha)=C.
```

Because `gcd(C,m)=1`, the complementary Gaussian factor

```text
beta:=z/alpha
```

has

```text
N(beta)=m
```

and is coprime to `alpha` away from units/2-primary support.

Thus every live diffuse candidate has a factorization

```text
z=epsilon * alpha * beta,
N(alpha)=C,
N(beta)=m,
```

with `epsilon` a Gaussian unit and the common-core orientation carried by `alpha`.

Conversely, for fixed `(alpha,beta)` the primitive vector `(X0,Y0)` is recovered exactly up to the finite unit/conjugation convention, after which merged 4ep gives only `B^o(1)` physical reconstruction multiplicity.

```text
DIFFUSE_GAUSSIAN_PRODUCT_FACTORIZATION_PROVED=true
COMMON_CORE_ORIENTATION_SELECTS_ALPHA=true
GAUSSIAN_PRODUCT_TO_PHYSICAL_PACKET_FIBER=Bo1
```

## 4. The bare bilinear factorization is exponent-neutral

The norm scales are

```text
N(alpha)=B^(kappa+o(1)),
N(beta)=B^(1/2-kappa+o(1)).
```

A trivial charged-once support ledger for the two factors is therefore

```text
kappa + (1/2-kappa) = 1/2.
```

Finite Gaussian representation/orientation multiplicities are `B^o(1)` and cannot be charged again.  Hence the bare multiplicative factorization does not improve the whole-family exponent.

```text
BARE_GAUSSIAN_BILINEAR_PRODUCT_EXPONENT=1/2
BARE_GAUSSIAN_FACTORIZATION_FIXED_POWER_SAVING_PROVED=false
```

The only remaining possible gain is correlation-sensitive: `alpha` is not an arbitrary Gaussian factor of norm `C`, `beta` is not an arbitrary complementary factor, and the product must arise from the same canonical balanced integer/Gaussian allocation and reciprocal physical masks.

## 5. The exact diffuse receiver is now bilinear and theorem-shaped

After all elementary reductions, the diffuse branch consists of coprime Gaussian factor pairs

```text
(alpha,beta)
```

with polynomial complementary norm scales, product

```text
z=alpha*beta,
```

and the full canonical physical acceptance weight retained.

Define

```text
DiffuseCoprimePolynomialGaussianNormFactorCanonicalAllocationBilinearCorrelation.
```

No ordinary unrestricted Gaussian divisor count can save a power because the unrestricted product ledger is exactly square-root scale.

```text
DIFFUSE_RECEIVER_MATERIALLY_CHANGED=true
NEW_DIFFUSE_THEOREM_SHAPE_EXPOSED=true
```

## Boundary

```text
STAGE14_4ET=COMPLETE_DIFFUSE_COPRIME_NORM_FACTOR_TO_GAUSSIAN_BILINEAR_PRODUCT_REDUCTION
PRIMITIVE_NORM_ODD_SUPPORT_GAUSSIAN_SPLIT=true
GAUSSIAN_SPLITTING_RECHARGE_ALLOWED=false
DIFFUSE_GAUSSIAN_PRODUCT_FACTORIZATION_PROVED=true
COMMON_CORE_ORIENTATION_SELECTS_ALPHA=true
GAUSSIAN_PRODUCT_TO_PHYSICAL_PACKET_FIBER=Bo1
BARE_GAUSSIAN_BILINEAR_PRODUCT_EXPONENT=1/2
BARE_GAUSSIAN_FACTORIZATION_FIXED_POWER_SAVING_PROVED=false
CURRENT_DIFFUSE_RECEIVER=DiffuseCoprimePolynomialGaussianNormFactorCanonicalAllocationBilinearCorrelation
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4eu
```
