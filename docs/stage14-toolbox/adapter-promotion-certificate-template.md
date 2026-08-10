# Stage14 adapter promotion certificate template

Copy one block per receiver. Promotion is valid only when every required field is filled by an exact source and every gate is true.

## Common fields

- Receiver:
- Source stage and commit:
- Physical coefficient space:
- Centering/selector:
- Uniform dyadic range:
- Bad primes and exceptional parameters:
- Quantitative target:
- Recombination loss:
- Regression command/result:

```text
SAME_PHYSICAL_COEFFICIENT_SPACE=false
CENTERING_PRESERVED=false
UNIFORM_PARAMETER_RANGE_PROVED=false
EXCEPTIONS_CONTROLLED=false
TARGET_ESTIMATE_PROVED=false
ZERO_FIXED_POWER_RECOMBINATION_LOSS=false
REGRESSION_PASS=false
PROMOTION_READY=false
```

## S receiver supplement

Receiver: `BalancedFourHostGaussianSquareDivisorIncidence`.

The certificate must retain all eight cells, the same physical pair, all four Gaussian hosts and their oriented square divisors. It must prove moving-host uniformity and a fixed-power gain before physical recombination. A fixed-host divisor bound is insufficient.

```text
FOUR_HOST_SIMULTANEITY_PRESERVED=false
MOVING_HOST_UNIFORMITY_PROVED=false
FIXED_POWER_INCIDENCE_GAIN_PROVED=false
PHYSICAL_PAIR_RECOMBINATION_ZERO_LOSS=false
```

## Fixed-U invisible supplement

Receiver: `SharedUPhysicalToroidalMellinCorrelation`.

The rank-one Kummer/Mellin certificate and kernel-side CRT tensorization are imported from t57. The certificate must instead prove correlation for the actual centered physical selector while retaining fixed U, divisor fan, moving pi,V,delta, hyperbola, reconstruction, interval, branch and bad-prime masks, with the same state across both primes.

```text
T57_KERNEL_CERTIFICATE_IMPORTED=true
T57_KERNEL_CRT_ZERO_LOSS_IMPORTED=true
ACTUAL_PHYSICAL_SELECTOR_RETAINED=false
TOROIDAL_MELLIN_CORRELATION_PROVED=false
TWO_PRIME_PHYSICAL_DISPERSION_PROVED=false
```

## Mixed supplement

The invisible/visible packet is not promoted by the invisible certificate.

```text
MIXED_BRANCH_SEPARATE=true
MIXED_BRANCH_ESTIMATE_PROVED=false
MIXED_BRANCH_PROMOTION_READY=false
```
