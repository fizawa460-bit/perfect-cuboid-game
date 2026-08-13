# Stage14-t-batch — t124 early stop on receiver change

## Result

Starts from latest merged main

```text
95e98cbd6626bc8f50a1397be881d04722b271ff
```

and consumes merged Stage14-t123, merged Stage14-t74/t89/t122, merged Stage14-Work-bpX28, and the shared Stage14 batch contract introduced by merged PR #727.

Stage14-t124 performs the finite-boundary atomic audit left by t123/bpX28.

The D4-boundary atoms are rejected by the strict physical short-cover chamber.  Splitting by their ambient principal mass gives an exact proof routing:

```text
boundary-heavy:
  nonboundary mass is fixed-power small
  -> actual physical count is already fixed-power small;

boundary-light:
  nonboundary baseline remains polynomially comparable
  -> any target fixed-power saving retains a fixed positive exponent
     after renormalization and must come from selected projective-class depletion.
```

Therefore

```text
FiniteD4BoundaryGenericNormPrimePrincipalAtomicConcentration
```

is discharged as a separate live theorem receiver.  The only live fixed-U mechanism is now

```text
SharedUNonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion.
```

This is a material receiver change at the first substantive work unit.  Under the shared common contract, receiver change is an allowed early-stop event before the normal three-unit minimum, so the batch ends here rather than manufacturing t125 in the same PR.

No integrated tH unit is needed.  A new tH29 remains premature until t125 freezes the exact nonboundary cofactor-to-class map and prime interval.

Publication recheck found main unchanged.

```text
STAGE14_T_BATCH=STOPPED_EARLY
BATCH_START_MAIN_SHA=95e98cbd6626bc8f50a1397be881d04722b271ff
BATCH_PUBLICATION_MAIN_SHA=95e98cbd6626bc8f50a1397be881d04722b271ff
BATCH_FIRST_STAGE=Stage14-t124
BATCH_LAST_STAGE=Stage14-t124
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=1
BATCH_SUBSTANTIVE_STAGE_COUNT=1
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUNonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
NEXT=Stage14-t125
```
