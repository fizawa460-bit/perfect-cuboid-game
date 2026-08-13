# Stage14-4ep — diffuse modulus graph contracts to primitive Gaussian norm-factor correlation

## Status

`COMPLETE_DIFFUSE_COMMON_CORE_NORM_DIVISOR_GRAPH_TO_NORM_FACTOR_CORRELATION`

Consumes merged `Stage14-4ek`, merged `Stage14-s7-74`, newly merged `Stage14-s7-75..77`, merged `Stage14-Work-bnX26`, and corrected batch-local `Stage14-4el..4eo`. No positive conclusion from the new 4eo auxiliary target is consumed.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
HEAVY_RAY_BRANCH_UNCHANGED=true
MOVER_H_RESULT_CONSUMED=false
```

## 1. Diffuse branch still has exponent-zero accepted incidence

Fix a polynomial common-core exponent cell

```text
C=B^(kappa+o(1)), kappa>0.
```

Merged s7-73/74 and 4eh show that the root-line principal mass is `B^(-kappa+o(1))` relative to the candidate background. Therefore exponent-zero positive centered discrepancy on the diffuse branch forces exponent-zero actual accepted incidence mass after the principal term is removed.

For every accepted candidate,

```text
N:=X0^2+Y0^2,
C|N,
N=C*m,
m in Z_{>0}.
```

```text
DIFFUSE_CENTERED_SATURATION_FORCES_EXPONENT_ZERO_ACCEPTED_NORM_DIVISOR_INCIDENCE=true
```

## 2. Variable modulus has only divisor-many degree over one norm value

For each positive integer `N`,

```text
# {C:C|N} = tau(N)=B^o(1)
```

on the Stage14 polynomial height range. Primitive representations

```text
N=X^2+Y^2,
gcd(X,Y)=1
```

also have `B^o(1)` multiplicity, and reverse reciprocal/allocation reconstruction above one primitive candidate has another `B^o(1)` charged-once fiber.

Hence

```text
accepted candidate z -> N=X0(z)^2+Y0(z)^2
```

has `B^o(1)` fiber multiplicity.

```text
ACCEPTED_NORM_VALUE_PROJECTION_FIBER=Bo1
VARIABLE_COMMON_CORE_DIVISOR_MULTIPLICITY=Bo1
PRIMITIVE_TWO_SQUARE_REPRESENTATION_MULTIPLICITY=Bo1
DIFFUSE_C_SUPPORT_IMPLIES_DIFFUSE_NORM_VALUE_SUPPORT_UP_TO_BO1=true
DIVISOR_MULTIPLICITY_RECHARGE_ALLOWED=false
```

## 3. Exact norm-factor receiver

The diffuse branch is exponent-equivalent to physical tuples

```text
N=X0^2+Y0^2=C*m,
C=B^(kappa+o(1)), kappa>0,
gcd(X0,Y0)=1,
gcd(C,X0Y0)=1,
```

where `C` is selected by the same canonical allocation / reciprocal witness and ranges diffusely over a polynomial family.

Freeze the quotient scale

```text
m=B^(lambda+o(1)), lambda>=0
```

at `B^o(1)` dyadic cost. The receiver becomes

```text
DiffuseCanonicalAllocationPrimitiveGaussianNormFactorCorrelation.
```

```text
DIFFUSE_NORM_DIVISOR_GRAPH_REWRITTEN_AS_NORM_FACTOR_EQUATION=true
QUOTIENT_SCALE_LAMBDA_CAN_BE_FROZEN=true
COMMON_CORE_AND_QUOTIENT_INDEPENDENCE_ASSUMED=false
```

## 4. No new saving is created by the reparameterization

The identity `N=C*m` is only a re-expression. Generic divisor existence, Gaussian splitting, primitive two-square representation multiplicity, and finite candidate fibers are already charged.

The surviving issue is the correlation among

```text
canonical physical allocation background,
primitive Gaussian norm value N,
physically selected common-core factor C,
complementary quotient m,
full reciprocal/range/chart masks.
```

No diffuse H is opened yet. The next internal split should distinguish

```text
m=B^o(1)
```

from a genuinely polynomial quotient scale and freeze the corresponding physical coefficient system.

```text
NEW_DIFFUSE_H_NEEDED=false
PREFERRED_NEXT_INTERNAL_REDUCTION=CommonCoreQuotientScaleSplitOfDiffusePrimitiveGaussianNormFactorCorrelation
```

## Current four surviving mechanisms

After publication recheck against merged s7-75..77, the complete current arithmetic survivor list is

```text
LOW COMMON CORE:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
  -> existing mainline allocation H target

POLYNOMIAL COMMON CORE / CONCENTRATED HEAVY RAY:
  ConcentratedExactCommonCoreHeavyPrimitiveReciprocalRayIncidence
  -> internal reverse-multiplicity audit remains

POLYNOMIAL COMMON CORE / CONCENTRATED GENUINE MOVER:
  FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
  -> new 4eo mover-only auxiliary H target

POLYNOMIAL COMMON CORE / DIFFUSE C:
  DiffuseCanonicalAllocationPrimitiveGaussianNormFactorCorrelation
  -> internal quotient-scale split remains
```

The mover H target does not cover or consume the heavy-ray branch.

## Boundary

```text
STAGE14_4EP=COMPLETE_DIFFUSE_COMMON_CORE_NORM_DIVISOR_GRAPH_TO_NORM_FACTOR_CORRELATION
DIFFUSE_CENTERED_SATURATION_FORCES_EXPONENT_ZERO_ACCEPTED_NORM_DIVISOR_INCIDENCE=true
ACCEPTED_NORM_VALUE_PROJECTION_FIBER=Bo1
DIFFUSE_C_SUPPORT_IMPLIES_DIFFUSE_NORM_VALUE_SUPPORT_UP_TO_BO1=true
DIFFUSE_NORM_DIVISOR_GRAPH_REWRITTEN_AS_NORM_FACTOR_EQUATION=true
QUOTIENT_SCALE_LAMBDA_CAN_BE_FROZEN=true
HEAVY_RAY_BRANCH_UNCHANGED=true
MOVER_H_RESULT_CONSUMED=false
NEW_DIFFUSE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT_H_TARGETS=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity;FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
NEXT=Stage14-4eq
```
