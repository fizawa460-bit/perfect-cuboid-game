# Stage14-t-batch — t137 through t139 with integrated positive tH31

## Status

`COMPLETE_POSITIVE_TH31_MITSUI_SAFE_LONG_HEADROOM_DISCHARGE`

Starts from and publication-rechecks latest merged main

```text
3af02c764300db002cce3e3bdf7da1236548ecbd
```

and follows the merged shared Stage14 batch contract plus t-route integrated-H specialization.

## Work units

1. `Stage14-t137` splits the t136 long-headroom `d=B^o(1)` branch into a Mitsui-safe pseudopolynomial modulus range

```text
d <= exp(c_safe*sqrt(log B))
```

and the genuinely larger subpolynomial range, while retaining the possible real exceptional-character residue sign.

2. `Stage14-t138` freezes the safe-range theorem target.  Fixed-power headroom allows cumulative prime-element estimates at the upper and lower endpoints to be subtracted, so the required target is only

```text
T_safe >= B^(-o(1)) M_safe.
```

3. `Stage14-tH31` independently audits the frozen t138 snapshot and returns a positive verdict.  Mitsui/Kai prime-element technology over `Q(i)` applies after choosing `c_safe` inside the pseudopolynomial modulus range.  A possible Siegel zero is retained; even in its suppressing residue sign it costs only `B^o(1)` at exponent level, so it cannot create fixed-power depletion.

4. `Stage14-t139` consumes tH31 and removes the complete Mitsui-safe long-headroom branch from the live receiver.

## New fixed-U receiver

The minimal remaining obstruction is

```text
EndpointShortFixedGaussianResiduePrimeOccupancyDeficit
OR
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

The endpoint-short branch is unchanged.  The long-headroom branch is now restricted to

```text
exp(c_safe*sqrt(log B)) < d = B^o(1).
```

This is a material receiver change, so the batch stops after four substantive work units.

No whole-family exponent is improved here.

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=3af02c764300db002cce3e3bdf7da1236548ecbd
BATCH_PUBLICATION_MAIN_SHA=3af02c764300db002cce3e3bdf7da1236548ecbd
BATCH_FIRST_STAGE=Stage14-t137
BATCH_LAST_STAGE=Stage14-t139
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=4
BATCH_SUBSTANTIVE_STAGE_COUNT=4
BATCH_INTEGRATED_H_UNITS=Stage14-tH31
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUEndpointShortFixedGaussianResiduePrimeOccupancyDeficitOrLongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
NEXT=Stage14-t140
```
