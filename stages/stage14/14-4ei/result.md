# Stage14-4ei — global saturation dichotomy: low common core versus polynomial centered discrepancy

## Status

`COMPLETE_LOW_CORE_ALLOCATION_VS_POLYNOMIAL_CORE_CENTERED_DISCREPANCY_DICHOTOMY`

Consumes batch-local `Stage14-4eg/4eh`, merged `Stage14-4ef`, and merged `Stage14-sH71`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Exponent-scale common-core dichotomy

On any candidate square-root-saturating subsequence, pass to a further subsequence on which

```text
kappa := log_B C0
```

has a limiting exponent in the Stage14 dyadic sense. There are exactly two exponent-level regimes:

```text
LOW CORE:
  kappa=0,
  C0=B^o(1);

POLYNOMIAL CORE:
  kappa>=epsilon
```

for some fixed `epsilon>0` after a further dyadic restriction.

The `B^o(1)` candidate and label unions do not change this dichotomy.

```text
COMMON_CORE_EXPONENT_DICHOTOMY_EXHAUSTIVE=true
```

## 2. Low-core branch returns to canonical allocation density

Merged sH71 and Stage14-4eg prove that when

```text
C0=B^o(1),
```

the root-line principal density is itself `B^(-o(1))`. Therefore no uniform fixed-power saving can be extracted from root spacing alone on this branch.

The exact global density chain remains

```text
mu_G = mu_can * mu_root.
```

Since `mu_root` is allowed to be exponent-zero in the low-core regime, the only already-exposed independent factor capable of closing this branch is the canonical allocation density. By merged 4ef that factor is the fixed-type simultaneous incidence

```text
d_a|a,
d_b|b,
d_+|a^2+b^2
```

with all physical masks retained.

Thus the low-core receiver is

```text
SubpolynomialCommonCoreCanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity.
```

```text
LOW_CORE_ROOT_SPACING_POWER_SAVING_AVAILABLE=false
LOW_CORE_BRANCH_RETURNS_TO_CANONICAL_ALLOCATION_CORRELATION=true
```

This does not prove the allocation saving; the 4ef theorem gate remains open.

## 3. Polynomial-core branch is centered discrepancy

On the polynomial-core regime, Stage14-4eh proves the principal root-line mass is strictly power-small. Hence square-root saturation forces

```text
D_kappa = |I_kappa| B^(-o(1))
```

for the centered root-line discrepancy.

The polynomial-core receiver is therefore

```text
PolynomialCommonCoreCanonicalAllocationCenteredGaussianRootLineDiscrepancy.
```

No additional allocation saving is multiplied here: proving a fixed-power bound for this centered discrepancy alone would close the polynomial-core reciprocal branch.

```text
POLYNOMIAL_CORE_BRANCH_REDUCED_TO_CENTERED_ROOT_DISCREPANCY=true
```

## 4. Canonical two-branch obstruction

The former opaque product receiver can now be replaced, for the purpose of ruling out square-root saturation, by the explicit alternative:

```text
A. SubpolynomialCommonCoreCanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
or
B. PolynomialCommonCoreCanonicalAllocationCenteredGaussianRootLineDiscrepancy.
```

A strict sub-square-root theorem follows if one proves a fixed-power deficit on the relevant branch uniformly:

```text
low core  -> allocation correlation deficit,
polynomial core -> centered discrepancy deficit.
```

```text
SQRT_OBSTRUCTION_SPLIT_INTO_LOW_CORE_ALLOCATION_OR_POLYNOMIAL_CORE_DISCREPANCY=true
```

## 5. H decision

The allocation-side theorem gate from 4ef remains valid:

```text
MAINLINE_ALLOCATION_H_NEEDED=true
MAINLINE_ALLOCATION_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
```

No **new** H is opened here for the polynomial-core branch because the centered discrepancy has not yet been expanded into an exact harmonic/energy object. The next internal step should do that expansion first.

```text
NEW_H_TRIGGERED_BY_4EI=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4EI=COMPLETE_LOW_CORE_ALLOCATION_VS_POLYNOMIAL_CORE_CENTERED_DISCREPANCY_DICHOTOMY
COMMON_CORE_EXPONENT_DICHOTOMY_EXHAUSTIVE=true
LOW_CORE_BRANCH_RETURNS_TO_CANONICAL_ALLOCATION_CORRELATION=true
POLYNOMIAL_CORE_BRANCH_REDUCED_TO_CENTERED_ROOT_DISCREPANCY=true
SQRT_OBSTRUCTION_SPLIT_INTO_LOW_CORE_ALLOCATION_OR_POLYNOMIAL_CORE_DISCREPANCY=true
MAINLINE_ALLOCATION_H_NEEDED=true
MAINLINE_ALLOCATION_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
NEW_H_TRIGGERED_BY_4EI=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ej
```
