# Stage14-4ep — diffuse modulus graph contracts to primitive Gaussian norm-factor correlation

## Status

`COMPLETE_DIFFUSE_COMMON_CORE_NORM_DIVISOR_GRAPH_TO_NORM_FACTOR_CORRELATION`

Consumes merged `Stage14-4ek`, merged `Stage14-s7-74`, merged `Stage14-Work-bnX26`, and batch-local `Stage14-4el..4eo`. No positive conclusion from the new 4eo auxiliary target is consumed.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Diffuse branch still has exponent-zero accepted incidence

Fix a polynomial common-core exponent cell

```text
C=B^(kappa+o(1)), kappa>0.
```

Merged s7-73/74 and 4eh show that the root-line principal mass is at most `B^(-kappa+o(1))` of the candidate background. Therefore an exponent-zero positive centered discrepancy on the diffuse branch forces exponent-zero actual accepted incidence mass after the principal term is removed.

For every accepted candidate,

```text
N := X0^2+Y0^2,
C | N,
N=C*m,
m in Z_{>0}.
```

```text
DIFFUSE_CENTERED_SATURATION_FORCES_EXPONENT_ZERO_ACCEPTED_NORM_DIVISOR_INCIDENCE=true
```

## 2. The variable modulus has only divisor-many degree over one norm value

For each positive integer `N`, the number of possible divisors `C|N` is

```text
tau(N)=B^o(1)
```

on every Stage14 polynomial height range. The number of primitive representations

```text
N=X^2+Y^2,
gcd(X,Y)=1
```

is also `B^o(1)` (bounded by the ordinary sum-of-two-squares representation divisor function). The already-merged reverse reciprocal / allocation reconstruction above one primitive candidate contributes only another `B^o(1)` factor.

Hence the projection

```text
accepted candidate z -> N=X0(z)^2+Y0(z)^2
```

has `B^o(1)` fiber multiplicity on the charged-once physical packet.

```text
ACCEPTED_NORM_VALUE_PROJECTION_FIBER=Bo1
VARIABLE_COMMON_CORE_DIVISOR_MULTIPLICITY=Bo1
PRIMITIVE_TWO_SQUARE_REPRESENTATION_MULTIPLICITY=Bo1
```

Therefore the diffuse exact-modulus support cannot obtain a new power merely from having many possible divisors of one norm value. If polynomially many exact `C` values are genuinely needed, polynomially many physical norm values (up to `B^o(1)` fibers) are needed as well.

```text
DIFFUSE_C_SUPPORT_IMPLIES_DIFFUSE_NORM_VALUE_SUPPORT_UP_TO_BO1=true
DIVISOR_MULTIPLICITY_RECHARGE_ALLOWED=false
```

## 3. Exact norm-factor receiver

The diffuse branch is exponent-equivalent to the physical support of tuples

```text
N=X0^2+Y0^2=C*m,
C=B^(kappa+o(1)), kappa>0,
gcd(X0,Y0)=1,
gcd(C,X0Y0)=1,
```

where `C` is the common-core factor selected by the same canonical allocation / reciprocal witness and is diffuse across a polynomial family of values.

Freeze also the quotient scale

```text
m=B^(lambda+o(1)), lambda>=0
```

at `B^o(1)` dyadic cost. The remaining object is

```text
DiffuseCanonicalAllocationPrimitiveGaussianNormFactorCorrelation
```

rather than an arbitrary variable-modulus root graph.

```text
DIFFUSE_NORM_DIVISOR_GRAPH_REWRITTEN_AS_NORM_FACTOR_EQUATION=true
QUOTIENT_SCALE_LAMBDA_CAN_BE_FROZEN=true
COMMON_CORE_AND_QUOTIENT_INDEPENDENCE_ASSUMED=false
```

## 4. What this does and does not buy

The identity `N=C*m` is only a reparameterization. Generic divisor existence, Gaussian splitting, primitive two-square representation count, and finite candidate fibers are already charged and provide no fixed-power loss.

The surviving arithmetic issue is the **correlation** between

```text
canonical physical allocation background,
primitive Gaussian norm value N,
physically selected common-core factor C,
complementary quotient m,
full reciprocal/range/chart masks.
```

This agrees with merged Work-bnX26's correlation-only obstruction principle.

No new diffuse-branch H is opened yet. Before theorem audit, the quotient exponent `lambda` should be split into near-full-common-core (`m=B^o(1)`) and genuinely two-polynomial-factor regimes and the corresponding physical coefficient system frozen.

```text
NEW_DIFFUSE_H_NEEDED=false
PREFERRED_NEXT_INTERNAL_REDUCTION=CommonCoreQuotientScaleSplitOfDiffusePrimitiveGaussianNormFactorCorrelation
```

## Batch boundary

After five substantive stages, the current arithmetic survivors are

```text
LOW COMMON CORE:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
  (existing mainline H target)

POLYNOMIAL COMMON CORE / CONCENTRATED EXACT C:
  FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
  (new 4eo auxiliary H target)

POLYNOMIAL COMMON CORE / DIFFUSE C:
  DiffuseCanonicalAllocationPrimitiveGaussianNormFactorCorrelation
  (continue internally by quotient-scale split)
```

## Boundary

```text
STAGE14_4EP=COMPLETE_DIFFUSE_COMMON_CORE_NORM_DIVISOR_GRAPH_TO_NORM_FACTOR_CORRELATION
DIFFUSE_CENTERED_SATURATION_FORCES_EXPONENT_ZERO_ACCEPTED_NORM_DIVISOR_INCIDENCE=true
ACCEPTED_NORM_VALUE_PROJECTION_FIBER=Bo1
DIFFUSE_C_SUPPORT_IMPLIES_DIFFUSE_NORM_VALUE_SUPPORT_UP_TO_BO1=true
DIFFUSE_NORM_DIVISOR_GRAPH_REWRITTEN_AS_NORM_FACTOR_EQUATION=true
QUOTIENT_SCALE_LAMBDA_CAN_BE_FROZEN=true
NEW_DIFFUSE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT_H_TARGETS=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity;FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
NEXT=Stage14-4eq
```
