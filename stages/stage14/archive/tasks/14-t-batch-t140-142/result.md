# Stage14-t-batch — t140 through t142 endpoint quarter-width localization

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=923b4b92bdfa90d7fa626e9ec512ea2cfb06c00e
BATCH_PUBLICATION_MAIN_SHA=923b4b92bdfa90d7fa626e9ec512ea2cfb06c00e
BATCH_FIRST_STAGE=Stage14-t140
BATCH_LAST_STAGE=Stage14-t142
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_FROZEN_H_TARGETS=Stage14-tH32
BATCH_STOP_REASON=receiver_change
```

## Results

- `t140`: defines the exact additive prime width `H(z)=X_U/N(z)-2sqrt(B)` and proves its exact equivalence to the distance of `N(z)` from the top cofactor endpoint. A dyadic width `Y=B^(lambda+o(1))` has principal capacity at most `B^(2lambda+o(1))`.
- `t141`: since `T_edge<=B^o(1)M_edge`, any endpoint sequence that can obstruct a uniform strict `B^(1/2)` bound must carry `M_edge=B^(1/2-o(1))`. Dyadic localization plus the t140 capacity bound forces `H>=B^(1/4-o(1))`; every fixed-power-below-quarter endpoint width is discharged by capacity alone.
- `t142`: crosses the remaining quarter-scale endpoint with the positive tH31 Mitsui modulus split. The safe-modulus endpoint is now a theorem-ready fixed-residue Gaussian short-interval target; the beyond-Mitsui endpoint and long-headroom branches retain the large-subpolynomial modulus obstruction. `tH32` is frozen but not executed because t142 is a material receiver change.

Current receiver:

```text
SafeMitsuiModulusQuarterScaleEndpointFixedGaussianResiduePrimeOccupancy
OR
QuarterScaleEndpointBeyondMitsuiModulusFixedGaussianResiduePrimeOccupancyBias
OR
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias
```

H ledger:

```text
TH31_COMPLETE_CONSUMED=true
T_ROUTE_H_NEEDED=true
T_ROUTE_H_REQUEST=Audit the sharp unconditional safe-modulus fixed-residue Gaussian prime short-interval threshold at the quarter-scale endpoint.
T_ROUTE_H_TARGET=stages/stage14/14-t142/th32-target.md
T_ROUTE_H_BLOCKING=false
TH32_NEEDED=true
TH32_EXECUTED=false
```

Whole-family ledger:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-tH32
```
