# Stage14-Work-cnX52 — valuation-averaged reduced-modulus character integration

## Status

`COMPLETE_VALUATION_AVERAGED_REDUCED_MODULUS_CHARACTER_LOCALIZATION`

This Work run consumes merged Stage14-s7-159..161 on top of merged Work-cmX51/q25.

The exact common-core averaged reciprocal-CRT first moment has been reorganized as

```text
J_ccs = sum_nu J_nu = P_red + E_red,
Q_nu | Q=2UV,
P_red = sum_nu P_nu,
E_red = sum_nu E_nu.
```

For `Q_nu>1`, `P_nu=A_{nu,0}/phi(Q_nu)` and `E_nu` is the aggregate nonprincipal Dirichlet-character contribution modulo `Q_nu`; for the saturated case `Q_nu=1`, `E_nu=0`.

Hence the previous unit and nonunit arithmetic gates are superseded as separate charged obstructions. The remaining arithmetic task is one aggregate reduced-modulus principal-domination estimate, with the moving common-core and valuation averages retained.

A sufficient input is

```text
|E_red| <= (1-epsilon_B) P_red
```

at the required survival scale on every frozen principal cell. This Work stage does not prove that inequality.

The scalar and polynomial `(E,m)` charged measures remain distinct:

```text
UniformScalarFilteredTau3CommonCoreAndQValuationAveragedReducedModulusReciprocalCRTCharacterDiscrepancyBelowPrincipalMass

UniformPolynomialOuterPairFilteredTau3CommonCoreAndQValuationAveragedReducedModulusReciprocalCRTCharacterDiscrepancyBelowPrincipalMass
```

The residual root-origin/canonical/allocation/cell/post-column mask remains separately charged after this gate.

```text
UNIT_CHARACTER_PRINCIPAL_NONPRINCIPAL_DECOMPOSITION_CONSUMED=true
NONUNIT_REDUCED_MODULUS_STRATIFICATION_CONSUMED=true
UNIT_NONUNIT_RECOMBINATION_CONSUMED=true
UNIT_NONUNIT_SEPARATE_ARITHMETIC_GATES_RECHARGE_FORBIDDEN=true
S_REDUCED_MODULUS_CHARACTER_THEOREM_SPECIES_COUNT=2
REDUCED_MODULUS_AGGREGATE_DISCREPANCY_BOUND_PROVED=false
COMMON_CORE_AVERAGE_MUST_BE_RETAINED=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
Q_COMPONENT=COMPLETE
Q26_NEEDED=true
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
NEXT_S=Stage14-s7-162
NEXT_INTEGRATED_TARGET=ValuationAveragedReducedModulusCharacterPrincipalDominationVersusResidualPostMaskOrNoGo
NEXT_REVISIT_CONDITION=approximately_s7_164_or_earlier_on_character_normal_form_or_postmask_or_parked_gate_or_exponent_change
```