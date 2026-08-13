# Stage14-4et — Gaussian bilinear reduction of the diffuse polynomial-quotient branch

## Status

`COMPLETE_DIFFUSE_POLYNOMIAL_QUOTIENT_TO_GAUSSIAN_BILINEAR_CORRELATION`

Consumes batch-local `Stage14-4es`, merged `Stage14-4ep`, merged `Stage14-s7-72..74`, and merged `Stage14-q13`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

The only live diffuse branch now has

```text
z:=X0+iY0,
gcd(X0,Y0)=1,
N(z)=X0^2+Y0^2=C*m,
C=B^(kappa+o(1)), 1/6<=kappa<=1/4,
m=B^(lambda+o(1)), lambda>0.
```

The physical common-core support is odd Gaussian-split with a frozen root orientation at each prime of `C`. For every accepted candidate, those local orientations select a Gaussian divisor

```text
alpha | z,
N(alpha)=C,
```

up to the already-frozen finite unit/2-primary decorations. Define

```text
beta:=z/alpha.
```

Then exactly

```text
z=epsilon*alpha*beta,
N(alpha)=C,
N(beta)=m
```

for a Gaussian unit `epsilon`.

No coprimality between `N(alpha)` and `N(beta)` is asserted here; common rational prime support, if present, remains part of the physical correlation rather than being silently peeled.

For fixed `(alpha,beta)` the primitive vector `(X0,Y0)` is recovered up to O(1) unit/conjugation data. Merged 4ep then gives only `B^o(1)` physical reverse multiplicity through the charged norm-value projection and reciprocal reconstruction.

```text
DIFFUSE_POLYNOMIAL_QUOTIENT_GAUSSIAN_FACTORIZATION_PROVED=true
COMMON_CORE_ROOT_ORIENTATION_SELECTS_ALPHA=true
GAUSSIAN_FACTOR_PAIR_TO_PHYSICAL_PACKET_FIBER=Bo1
CORE_QUOTIENT_COPRIMALITY_ASSUMED=false
```

This Gaussian product factorization is a reparameterization, not a saving. Ordinary divisor multiplicity, split-prime support, primitive sum-of-two-squares representation counts, and finite Gaussian orientations are already charged and cannot be multiplied as fresh density factors.

The remaining issue is correlation-sensitive:

```text
alpha is the physically selected common-core Gaussian factor;
beta is the same witness's polynomial complementary factor;
alpha*beta must pass canonical balanced integer/Gaussian allocation,
reciprocal, range, chart, primitive and squarefree/coprime masks.
```

Define the live diffuse receiver

```text
DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation.
```

Merged q13 classifies Wright 2026 partially-fixed-modulus / unbalanced-dispersion technology as a plausible architecture only after an exact convolution and Siegel-Walfisz adapter is proved; no saving is imported here.

```text
DIFFUSE_RECEIVER_MATERIALLY_CHANGED=true
NEW_DIFFUSE_THEOREM_SHAPE_EXPOSED=true
Q13_WRIGHT2026_DIRECT_IMPORT=false
```

```text
STAGE14_4ET=COMPLETE_DIFFUSE_POLYNOMIAL_QUOTIENT_TO_GAUSSIAN_BILINEAR_CORRELATION
DIFFUSE_POLYNOMIAL_QUOTIENT_GAUSSIAN_FACTORIZATION_PROVED=true
GAUSSIAN_FACTOR_PAIR_TO_PHYSICAL_PACKET_FIBER=Bo1
CORE_QUOTIENT_COPRIMALITY_ASSUMED=false
CURRENT_DIFFUSE_RECEIVER=DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4eu
```
