# Stage14-t-batch — t147 through t149

## Status

`STAGE14_T_BATCH=COMPLETE`

Starts from latest merged main

```text
a0c01e4f1236e2a3c1f718f056fee6d4f1c73e20
```

and consumes merged Stage14-t146 plus Stage14-Work-byX37.

## Work units

### Stage14-t147
Restores the ordinary Gaussian residue denominator from the exact t135 baseline.  For odd squarefree `d`,

```text
|R_d|=phi(d)*|G(d)|=d^2*B^o(1),
```

so the endpoint principal capacity sharpens to

```text
M_Y
 <= B^o(1)/d^2
    * (Y/(h*k0)+1)(Y+1).
```

### Stage14-t148
Makes the sparse/many cofactor alternatives disjoint.  A genuinely sparse endpoint layer has only `B^o(1)` actual Gaussian cofactors.  Nonnegative localization then freezes any principal fixed-power depletion to one actual cofactor `z_*`, retaining both principal-scale baseline mass and fixed-power deficit.

The many branch becomes

```text
M_Y <= B^o(1)*Y^2/(h*k0*d^2).
```

### Stage14-t149
Consumes the sharpened capacity:

```text
MANY:
  Y >= B^(1/4-o(1))*d*sqrt(h*k0).
```

On beyond-Mitsui endpoint packets, merged t144 gives `h*k0>=C*d`, hence

```text
Y >= B^(1/4-o(1))*d^(3/2).
```

On SPARSE, one exact interval must satisfy

```text
H_*/d^2 >= B^(1/2-o(1)).
```

The safe-modulus portions are intersected with the already-consumed tH32 threshold `H<H_Kai(B)`; any subrange pushed above `H_Kai` is discharged without recharging tH32.

## New fixed-U receiver

```text
SafeMitsuiSingleCofactorSubKaiResidueNormalizedNearFullPrimeOccupancy
OR
SafeMitsuiManyCofactorResidueHostNormalizedIntermediatePrimeOccupancy
OR
BeyondMitsuiSingleCofactorResidueNormalizedNearFullPrimeOccupancyBias
OR
BeyondMitsuiManyCofactorResidueHostNormalizedEndpointPrimeOccupancyBias
OR
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

The batch stops at t149 because this is a material receiver change and reaches the t-component of the normal Work-byX37 revisit condition.

## CI repair carried in this batch

The merged t144--t146 dedicated CI had failed only because its audit searched t65 for the ASCII string

```text
h*k = epsilon*m
```

while t65 stores the exact relation in LaTeX as `hk=\varepsilon m`.  This batch repairs that replay assertion and the new dedicated CI explicitly reruns the repaired t144--t146 audit before the older tH32/t140 regressions.

```text
PREVIOUS_T144_146_CI_FAILURE_MATHEMATICAL=false
PREVIOUS_T144_146_CI_FAILURE_CLASS=assertion_text_format_only
PREVIOUS_T144_146_AUDIT_REPAIRED=true
```

## Batch lock

```text
BATCH_START_MAIN_SHA=a0c01e4f1236e2a3c1f718f056fee6d4f1c73e20
BATCH_PUBLICATION_MAIN_SHA=a0c01e4f1236e2a3c1f718f056fee6d4f1c73e20
BATCH_FIRST_STAGE=Stage14-t147
BATCH_LAST_STAGE=Stage14-t149
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
NEXT=Stage14-t150
```
