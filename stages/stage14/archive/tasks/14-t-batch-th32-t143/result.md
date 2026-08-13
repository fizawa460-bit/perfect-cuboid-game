# Stage14-t-batch — tH32 + t143

## Status

`STAGE14_T_BATCH=COMPLETE`

Starts from latest merged main

```text
5884e0ec4f9fc85589e00edafbdc6cda3c67bc2d
```

and executes the already-frozen `Stage14-tH32` target before consuming its verdict in `Stage14-t143`.

## Work units

### 1. Stage14-tH32

Independent primary-source audit of the safe-modulus quarter-scale fixed-residue Gaussian prime short-interval target.

Verdict:

```text
quarter scale H=B^(1/4-o(1)): NOT COVERED;
exact growing-residue direct Kai/Mitsui threshold:
  H >= B^(1/2)*exp(-c*sqrt(log B));
conductor-one Gaussian-sector comparator (Stucky):
  H >= B^(7/20+epsilon).
```

The possible real Hecke/Siegel zero can be retained in the Kai/Mitsui near-full threshold and causes only subpolynomial suppression. It is not the quarter-scale obstruction.

### 2. Stage14-t143

Consumes tH32 and discharges the safe-modulus near-full endpoint range

```text
H >= B^(1/2)*exp(-c_short*sqrt(log B)).
```

The remaining safe-modulus endpoint is localized to

```text
B^(1/4-o(1)) <= H
  < B^(1/2)*exp(-c_short*sqrt(log B)).
```

The two beyond-Mitsui branches remain unchanged.

## New receiver

```text
SafeMitsuiModulusIntermediateShortEndpointFixedGaussianResiduePrimeOccupancy
OR
QuarterScaleEndpointBeyondMitsuiModulusFixedGaussianResiduePrimeOccupancyBias
OR
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias
```

This is a material receiver change, so the shared batch contract stops after two substantive work units.

```text
BATCH_START_MAIN_SHA=5884e0ec4f9fc85589e00edafbdc6cda3c67bc2d
BATCH_PUBLICATION_MAIN_SHA=5884e0ec4f9fc85589e00edafbdc6cda3c67bc2d
BATCH_FIRST_STAGE=Stage14-tH32
BATCH_LAST_STAGE=Stage14-t143
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=2
BATCH_SUBSTANTIVE_STAGE_COUNT=2
BATCH_INTEGRATED_H_UNITS=Stage14-tH32
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUSafeMitsuiModulusIntermediateShortEndpointFixedGaussianResiduePrimeOccupancyOrQuarterEndpointBeyondMitsuiModulusBiasOrLongHeadroomBeyondMitsuiModulusBias
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
NEXT=Stage14-t144
```

Includes deterministic short-interval scale audit, regression of merged t140--t142 and t137--t139+tH31 batches, publication-main lock, and path-scoped CI.
