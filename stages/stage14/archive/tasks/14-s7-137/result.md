# Stage14-s7-137 — isolate conditioned reciprocal-CRT measure deficit from post-mask deficit

## Status

`COMPLETE_CONDITIONED_RECIPROCAL_CRT_MEASURE_FIREWALL_AND_RECEIVER_CHANGE`

Consumes batch-local `Stage14-s7-135/136`, merged `Stage14-s7-130`, and merged `Stage14-Work-cfX44`.

On one principal active nonaligned cell define nested supports

```text
S_mult := charged outer points with at least one retained filtered-tau3 first witness,
S_crt  := points in S_mult for which at least one retained witness extends through the q17 reciprocal/CRT inner kernel,
S_phys := points in S_crt for which at least one complete witness passes the residual root/canonical/post-column mask.
```

Exactly

```text
S_phys subset S_crt subset S_mult.
```

Write exponents

```text
#S_mult = B^(sigma_mult+o(1)),
#S_crt  = B^(sigma_crt+o(1)),
#S_phys = B^(tau+o(1)).
```

and conditional deficits

```text
delta_crt_cond := sigma_mult-sigma_crt,
delta_post     := sigma_crt-tau.
```

Then

```text
tau = sigma_mult-delta_crt_cond-delta_post.
```

The first-layer filtered-tau3 support/moment adapter and second-layer fixed-candidate multiplicity bounds are already consumed and are not charged again.

The new arithmetic burden is therefore not a new inner kernel theorem. It is a measure-preserving lower-ratio statement for the already-known reciprocal/CRT kernel under the retained filtered-tau3 witness conditioning. Scalar and polynomial `(E,m)` variants remain distinct.

```text
S_CONDITIONED_RECIPROCAL_CRT_DEFICIT_LEDGER_PROVED=true
S_HEAVY_SURVIVAL_BUDGET=sigma_mult_minus_delta_crt_cond_minus_delta_post_ge_mu
Q17_INNER_KERNEL_RESEARCH_RECHARGED=false
Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
```

The active theorem species are now frozen as

```text
UniformScalarFilteredTau3ConditionedQ17ReciprocalCRTMeasureTransfer
UniformPolynomialOuterPairFilteredTau3ConditionedQ17ReciprocalCRTMeasureTransfer.
```

followed by the separately charged residual post-mask. The aligned fixed-E two-sided realization remains parked at `UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment`.

```text
CURRENT_S_RECEIVER=FixedETwoSidedParkedUniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment_OR_UniformScalarFilteredTau3ConditionedQ17ReciprocalCRTMeasureTransferThenConditionalPostMask_OR_UniformPolynomialOuterPairFilteredTau3ConditionedQ17ReciprocalCRTMeasureTransferThenConditionalPostMask
RECEIVER_MATERIALLY_CHANGED=true
S_ROUTE_H_NEEDED=false
Q21_NEEDED=false
WORK_CFX44_REVISIT_TRIGGER_S7_137_REACHED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-138
```
