# Stage14-t-batch — t115 through t117

## Status

`COMPLETE_COFACTOR_CORE_NORM_FIBER_AND_THREE_MECHANISM_REDUCTION`

Runs the canonical `Stage14-t-batch` contract from latest merged main

```text
2fd569305e0f8c1dc1acafe1c3b7a3c635aec0e4
```

and consumes merged `Stage14-t114`, merged `Stage14-t91`, merged `Stage14-Work-bnX26`, and the completed negative tH26/tH28 boundaries where relevant.  Unmerged descendants are advisory only.

## Batch progress

### Stage14-t115

The t114 weighted physical cofactor-core density is decomposed exactly by scalar norm fibers.  The principal prime weight is constant on a fixed norm fiber:

```text
A_gamma=A(N(gamma)).
```

Hence

```text
mu_core
 = [sum_n A(n) R_n rho_core(n)]/[sum_n A(n)R_n].
```

The internal primitive Gaussian orientation multiplicity is only `B^o(1)`; the outer norm coordinate remains the polynomial-scale variable.

### Stage14-t116

Merged t91 is used to split each primitive norm fiber into

```text
exceptional packet-supported label e
+
generic split-prime orientation cube epsilon.
```

The ell-independent physical core becomes exactly

```text
C_U(n;e,epsilon)=L_U(n;e) S_U(n;e,epsilon),
```

where the fixed-packet local interactions are confined to exceptional support and the remaining global Boolean may still correlate generic orientation bits.  Exceptional label **count** is only `B^o(1)` and cannot be recharged, but the scalar norm support on which any local label survives may still be power thin.

### Stage14-t117

Define the charged-once exceptional-local admissible density `lambda_loc` and conditional generic-orientation principal density `sigma_gen`.  Then

```text
mu_core=lambda_loc*sigma_gen
```

exactly.  Combining this with merged t114 yields the fixed-U three-mechanism trichotomy: any fixed-power saving must come from at least one of

```text
(A) ExceptionalLocalAdmissibleNormSupportWeightedDensityDeficit,
(B) GenericSplitPrimeOrientationPhysicalPrincipalDensityDeficit,
(C) PhysicalSelectedProjectiveClassNearTotalPrimeDepletion.
```

This is a material receiver change from the two-branch t114 receiver, so the batch stops after three substantive stages.

No new tH is justified.  tH26 already gives the negative generic Hecke/projective boundary, while tH28 gives the negative projected-support boundary.  Mechanisms (A) and (B) first require internal arithmetic decomposition before a new external theorem target is precise enough to freeze.

Publication recheck found latest merged main unchanged at

```text
2fd569305e0f8c1dc1acafe1c3b7a3c635aec0e4.
```

The newly merged mainline `Stage14-4el..4ep` / s-route `s7-75..77` correlation work does not identify the fixed-U norm-fiber measure or cross-promote a saving, so it does not alter this t-route boundary.

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=2fd569305e0f8c1dc1acafe1c3b7a3c635aec0e4
BATCH_PUBLICATION_MAIN_SHA=2fd569305e0f8c1dc1acafe1c3b7a3c635aec0e4
BATCH_FIRST_STAGE=Stage14-t115
BATCH_LAST_STAGE=Stage14-t117
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUExceptionalLocalNormSupportDeficitOrGenericOrientationPrincipalDensityDeficitOrSelectedClassNearTotalDepletion
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
NEXT=Stage14-t118
```
