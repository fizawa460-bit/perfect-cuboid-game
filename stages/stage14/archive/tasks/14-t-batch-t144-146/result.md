# Stage14-t-batch — t144 through t146

## Status

`COMPLETE_HOSTED_MODULUS_AND_HOST_NORMALIZED_ENDPOINT_CAPACITY_LOCALIZATION`

Starts from latest merged main

```text
f9c3116fc82cacbcb494a055b40bb0daa825e19e
```

and consumes merged Stage14-t143/tH32 and Stage14-Work-bxX36.

Three substantive work units:

1. `Stage14-t144` — traces the beyond-Mitsui selector divisor back to the fixed-U host: `d|D_Ubeta|R*S`, `d<=m/2`, and `h*k0=eta*epsilon*m`. On endpoint packets the retained selector inequality gives the same coupling after substituting the reciprocal endpoint relation. Thus beyond-Mitsui endpoint modulus is not independent entropy; it forces simultaneously large fixed-U norm `m` and host scale `h*k0`.
2. `Stage14-t145` — retains the fixed-U denominator in the t140 endpoint annulus capacity:
   `M_Y <= B^o(1)*(Y/(h*k0)+1)*(Y+1)`. If `Y=B^(lambda+o(1))` and `h*k0=B^(rho+o(1))`, the capacity exponent is `max(2lambda-rho,lambda)`.
3. `Stage14-t146` — localizes every principal-scale endpoint layer into a sparse-near-full alternative or a host-normalized many-cofactor alternative. The latter requires
   `Y >= B^(1/4-o(1))*sqrt(h*k0)`. On beyond-Mitsui endpoint packets, `h*k0>=C*d` gives the stronger pseudopolynomial floor `Y >= B^(1/4-o(1))*sqrt(d)`.

New fixed-U receiver:

```text
SafeMitsuiModulusSubKaiSparseNearFullFixedGaussianResiduePrimeOccupancy
OR
SafeMitsuiModulusHostNormalizedIntermediateEndpointFixedGaussianResiduePrimeOccupancy
OR
BeyondMitsuiHostedSelectorSparseNearFullFixedGaussianResiduePrimeOccupancyBias
OR
BeyondMitsuiHostedSelectorHostNormalizedEndpointFixedGaussianResiduePrimeOccupancyBias
OR
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

The host-normalized endpoint branches satisfy

```text
H >= B^(1/4-o(1))*sqrt(h*k0).
```

The beyond-Mitsui hosted endpoint additionally has

```text
h*k0 >= C*d,
d>exp(c_safe*sqrt(log B)).
```

No new tH is opened: tH32 already audited the safe fixed-residue short-interval boundary, while t144--t146 are internal capacity/provenance refinements.

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=f9c3116fc82cacbcb494a055b40bb0daa825e19e
BATCH_PUBLICATION_MAIN_SHA=f9c3116fc82cacbcb494a055b40bb0daa825e19e
BATCH_FIRST_STAGE=Stage14-t144
BATCH_LAST_STAGE=Stage14-t146
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUSparseNearFullOrHostNormalizedEndpointOccupancyPlusBeyondMitsuiLongBias
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
NEXT=Stage14-t147
```
