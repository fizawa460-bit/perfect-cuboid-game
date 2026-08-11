# Stage14-t95 — antipodal quotient occupancy variance dichotomy

## Status

`COMPLETE_ANTIPODAL_QUOTIENT_OCCUPANCY_VARIANCE_DICHOTOMY`

Consumes merged t94 and merged frozen tH26 without reopening H. Whole-family exponent remains `1/2`; strict sub-square-root remains unproved.

Let `Omega={+-1}^r/{+-1}` be the antipodal quotient from t94 and let `f:Omega->{0,1}` be the exact physical occupancy indicator after fixing the packet and the complete charged-once quotient majorant. Put

```text
mu = |Omega|^{-1} sum_x f(x),
g = f-mu.
```

For the normalized even-Walsh Fourier transform on `Omega`, Parseval gives the exact Bernoulli variance identity

```text
sum_{chi != 1} |fhat(chi)|^2
 = |Omega|^{-1} sum_x |g(x)|^2
 = mu*(1-mu).
```

Hence the principal pair mean and the centered-even quotient spectrum are not independent obstructions: both are governed by the single occupancy parameter `mu`.

Consequences:

1. If `mu=B^{-delta+o(1)}` for fixed `delta>0`, merged 4dj/t94 already gives exponent at most `1/2-delta`.
2. If `1-mu=B^{-delta+o(1)}`, then the full centered-even Fourier energy is `B^{-delta+o(1)}` and every Cauchy/Parseval use gains at least `B^{-delta/2+o(1)}` relative to the complete quotient majorant.
3. Therefore any square-root-saturating sequence not already saved by occupancy density or centered-energy deficit must satisfy simultaneously

```text
mu = B^{-o(1)},
1-mu = B^{-o(1)}.
```

This is an exponent-zero intermediate-occupancy regime. It is strictly smaller than the previous vague `near-maximal` language: the almost-full regime is now separated and analytically cheap on the centered side.

No theorem forces either `mu` or `1-mu` to have a fixed-power deficit on every physical packet, so no whole-family saving is claimed.

The remaining receiver is

```text
SharedUCanonicalLPFExponentZeroIntermediateAntipodalPairOccupancyEvenCorrelation
```

with `mu(1-mu)=B^{-o(1)}` and all t90-t94 physical masks retained.

```text
TH26_COMPLETE_CONSUMED=true
TH27_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-t96
```