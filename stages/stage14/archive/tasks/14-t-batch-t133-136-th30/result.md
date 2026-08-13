# Stage14-t-batch — t133 through t136 with integrated tH30

Starts from latest merged main

```text
43c2beeda0c9c5af2154d6deca5912d5be9e3ab2
```

and follows the merged shared Stage14 batch contract plus t-route integrated-H specialization.

## Work units

1. `Stage14-t133` — decomposes the fixed-class scalar norm weight by the finite D4 normalization state and freezes one state without losing a fixed depletion exponent. The cofactor weight becomes an exact primitive Gaussian representation multiplicity in one fixed open sector and one fixed raw projective class.
2. `Stage14-t134` — lifts that projective class to its `B^o(1)` ordinary Gaussian residue coset and freezes one exact cofactor residue `rho_* (mod d)` at subpolynomial cost.
3. `Stage14-t135` — lifts the fixed prime projective class to ordinary Gaussian residues, freezes one prime residue `beta_*`, and unfolds the scalar norm weight back to actual Gaussian cofactors. The target is an explicit fixed-sector/fixed-residue primitive Gaussian cofactor × fixed-residue Gaussian-prime reciprocal hyperbola. This materially changes theorem applicability and triggers `tH30`.
4. `Stage14-tH30` — independent audit of the frozen t135 snapshot. The old opaque-cofactor / Type-I--II adapter obstruction is removed, but no unconditional theorem covers every target packet because arbitrarily short endpoint intervals and individual `d=B^o(1)` residue classes with possible exceptional real-character bias remain.
5. `Stage14-t136` — consumes tH30 and reduces the live fixed-U obstruction to exactly two prime-side mechanisms: endpoint-short fixed-residue occupancy deficit, or long-headroom fixed-residue bias for an individual subpolynomial modulus.

## New receiver

```text
EndpointShortFixedGaussianResiduePrimeOccupancyDeficit
OR
LongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias
```

The previous arbitrary cofactor weight and physical-cofactor Type-I/II adapter are no longer live receiver components.

## H decision

`tH30` is complete and consumed.  No `tH31` is opened: the next internal step must first expose the scale/conductor structure of `d` on the long-headroom branch and separate a possible safe polylogarithmic range from the genuinely larger `B^o(1)` range.

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=43c2beeda0c9c5af2154d6deca5912d5be9e3ab2
BATCH_PUBLICATION_MAIN_SHA=43c2beeda0c9c5af2154d6deca5912d5be9e3ab2
BATCH_FIRST_STAGE=Stage14-t133
BATCH_LAST_STAGE=Stage14-t136
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=5
BATCH_SUBSTANTIVE_STAGE_COUNT=5
BATCH_INTEGRATED_H_UNITS=Stage14-tH30
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUEndpointShortFixedGaussianResiduePrimeOccupancyDeficitOrLongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
NEXT=Stage14-t137
```
