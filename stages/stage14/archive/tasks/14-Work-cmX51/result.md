# Stage14-Work-cmX51 — common-core averaged unit-character / nonunit-local receiver

## Status

`COMPLETE_COMMON_CORE_AVERAGED_UNIT_CHARACTER_NONUNIT_LOCALIZATION`

Consumes merged Work-clX50/q24 and merged Stage14-s7-156..158.

## 1. Charged-once consumption

```text
COMMON_CORE_CONDITIONING_AUDIT_CONSUMED=true
COMMON_CORE_AVERAGE_MUST_BE_RETAINED=true
COPRIME_SIDE_POSITIVE_DENSITY_FACTORIZATION_FAILURE_CONSUMED=true
UNIT_STRATUM_DIRICHLET_CHARACTER_EXPANSION_CONSUMED=true
UNIT_NONUNIT_CRT_PARTITION_CONSUMED=true
COMMON_CORE_SIDE_COPRIME_DECOMPOSITION_RECHARGE_FORBIDDEN=true
```

The exact charged arithmetic first moment is partitioned

```text
J_ccs = J_unit + J_nonunit,
```

with the common-core average retained inside both terms.

## 2. Unit stratum

On `gcd(W1(lambda),Q)=1`, `Q=2UV`, the reciprocal-CRT quotient condition is one unit residue class modulo `Q`. The exact Dirichlet-character expansion separates the principal allocation mass divided by `phi(Q)` from the total nonprincipal-character discrepancy.

Scalar receiver:

```text
UniformScalarFilteredTau3CommonCoreAveragedTwoCoprimeSideReciprocalCRTUnitCharacterDiscrepancyBelowPrincipalMass
```

Polynomial outer-pair receiver:

```text
UniformPolynomialOuterPairFilteredTau3CommonCoreAveragedTwoCoprimeSideReciprocalCRTUnitCharacterDiscrepancyBelowPrincipalMass
```

## 3. Nonunit stratum

On `gcd(W1(lambda),Q)>1`, unit-group character orthogonality cannot replace the original CRT support before the `Q`-supported valuation/allocation pattern between reciprocal factors is resolved.

Scalar receiver:

```text
UniformScalarFilteredTau3CommonCoreAveragedQSupportedValuationReciprocalCRTNonunitIncidenceLowerBound
```

Polynomial outer-pair receiver:

```text
UniformPolynomialOuterPairFilteredTau3CommonCoreAveragedQSupportedValuationReciprocalCRTNonunitIncidenceLowerBound
```

The two strata are exact alternatives, not multiplicative independent factors and not automatically comparable in size.

## 4. Integrated conclusion

```text
S_UNIT_NONUNIT_THEOREM_SPECIES_COUNT=4
UNIT_CHARACTER_PRINCIPAL_DOMINATION_PROVED=false
NONUNIT_Q_SUPPORTED_VALUATION_GATE_PROVED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
Q25_THEOREM_TARGET_CONSUMED=true
```

The residual root-origin/canonical/allocation/cell/post-column mask remains separately charged after either arithmetic gate.

## 5. H and whole-family locks

```text
MAINLINE_H_NEEDED=true
MAINLINE_H_COMPLETED=true
MAINLINE_BLOCKED_BY_H=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
FIXED_U_H_COMPLETED=true
FIXED_U_BLOCKED_BY_H=true
TH33_COMPLETE_CONSUMED=true
TH34_NEEDED=false
WHOLE_STAGE14_BLOCKED_BY_EXTERNAL_GATES=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

## 6. Next

q25 is triggered because Stage14-s7-158 froze a new stable two-part theorem target.

Normal Work/XQ revisit: approximately `Stage14-s7-161`, or earlier on a proved unit-character principal-domination adapter, a proved nonunit valuation decomposition/positive local density, a material post-mask receiver change, parked-gate resolution, or exponent change.
