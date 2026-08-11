# Stage14-t101

Status: `COMPLETE_SINGLE_ELEMENTARY_MOVER_PRINCIPAL_CENTERED_SPLIT`

Consumes merged Stage14-t100 and completed immutable Stage14-tH27. tH26/tH27 are not reopened.

For one surviving elementary mover boundary event E under the frozen packet measure M, define

```text
rho_E = E_M[1_E]
1_E^circ = 1_E-rho_E
```

Then exactly

```text
1_E = rho_E + 1_E^circ
E_M[1_E^circ] = 0
E_M[|1_E^circ|^2] = rho_E(1-rho_E)
```

This applies separately to SIGN, DIV and PROJ mover branches. The tH27 negative certificate is consumed literally: existing discrepancy technology can act on the centered term but does not uniformly remove the positive principal density.

If `rho_E=B^{-delta+o(1)}` for fixed delta>0, the principal contribution has a fixed-power occupancy deficit. If `1-rho_E=B^{-delta+o(1)}`, the centered L2 energy has the same fixed-power deficit and Cauchy yields a half-exponent discrepancy gain. Therefore any square-root-saturating mover sequence must satisfy

```text
rho_E=B^{-o(1)}
1-rho_E=B^{-o(1)}
```

No fixed positive delta is proved here.

```text
STAGE14_T101=COMPLETE_SINGLE_ELEMENTARY_MOVER_PRINCIPAL_CENTERED_SPLIT
MERGED_T100_CONSUMED=true
TH26_COMPLETE_CONSUMED=true
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH28_NEEDED=false
PRINCIPAL_CENTERED_SPLIT_EXACT=true
CENTERED_TERM_MEAN_ZERO=true
CENTERED_L2_ENERGY_EQUALS_RHO_ONE_MINUS_RHO=true
FIXED_POWER_LOW_DENSITY_SAVING_AVAILABLE=true
FIXED_POWER_COMPLEMENT_DEFICIT_DISCREPANCY_SAVING_AVAILABLE=true
EXPONENT_ZERO_INTERMEDIATE_MOVER_DENSITY_IS_MINIMAL_SURVIVOR=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFSingleElementaryMoverExponentZeroIntermediatePrincipalDensityPlusCenteredDiscrepancy
NEXT=Stage14-t102
```
