# Stage14-s7-158 — unit-character / nonunit-residue receiver split

## Status

`COMPLETE_UNIT_CHARACTER_NONUNIT_RESIDUE_RECEIVER_CHANGE`

Stage14-s7-156 shows that the moving common core cannot be globally frozen at one exact value without an unproved density assertion. Stage14-s7-157 shows that side-host coprimality does not by itself give a positive Euler product, but on the unit CRT stratum it gives an exact quotient-residue / Dirichlet-character expansion.

Accordingly split the charged joint incidence exactly into

```text
J_ccs = J_unit + J_nonunit,
```

where

```text
J_unit    : gcd(W1(lambda),2UV)=1,
J_nonunit : gcd(W1(lambda),2UV)>1.
```

The common-core average remains inside both terms.

## 1. Unit stratum

On `J_unit`, the q17 CRT indicator is one fixed unit residue class modulo `Q=2UV` after passing to `r=n*f^{-1}`. The principal Dirichlet character contributes the unsigned allocation mass divided by `phi(Q)`. The nonprincipal characters measure the exact discrepancy from that principal contribution.

Thus a sufficient arithmetic theorem for positive unit-stratum mass is a uniform estimate showing that the total nonprincipal character contribution is strictly smaller, at the required fixed-power scale, than the principal mass on every frozen principal cell.

Scalar theorem species:

```text
UniformScalarFilteredTau3CommonCoreAveragedTwoCoprimeSideReciprocalCRTUnitCharacterDiscrepancyBelowPrincipalMass
```

Polynomial outer-pair theorem species:

```text
UniformPolynomialOuterPairFilteredTau3CommonCoreAveragedTwoCoprimeSideReciprocalCRTUnitCharacterDiscrepancyBelowPrincipalMass
```

No such estimate is proved here.

## 2. Nonunit stratum

When `gcd(W1,2UV)>1`, the quotient-unit character reduction is unavailable without first resolving the `2UV`-supported valuation/allocation pattern between `f` and `n`. This is an exact local-residue support problem and remains separately charged; it is not discarded as a lower-order set.

Scalar theorem species:

```text
UniformScalarFilteredTau3CommonCoreAveragedQSupportedValuationReciprocalCRTNonunitIncidenceLowerBound
```

Polynomial outer-pair theorem species:

```text
UniformPolynomialOuterPairFilteredTau3CommonCoreAveragedQSupportedValuationReciprocalCRTNonunitIncidenceLowerBound
```

The two strata are alternatives in an exact partition. Their exponents are not multiplied, and neither is assumed negligible.

After either arithmetic gate, the residual root-origin/canonical/allocation/cell/post-column mask remains separately charged.

```text
RECEIVER_MATERIALLY_CHANGED=true
COMMON_CORE_AVERAGE_MUST_BE_RETAINED=true
UNIT_NONUNIT_CRT_PARTITION_PROVED=true
UNIT_CHARACTER_PRINCIPAL_NONPRINCIPAL_SPLIT_PROVED=true
UNIT_CHARACTER_DISCREPANCY_BOUND_PROVED=false
NONUNIT_Q_SUPPORTED_VALUATION_GATE_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
Q25_THEOREM_TARGET_NOW_STABLE=true
Q25_NEEDED=true
S_ROUTE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-159
```
