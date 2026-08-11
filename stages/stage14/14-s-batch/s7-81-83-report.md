# Stage14-s-batch report — s7-81 through s7-83

```text
STAGE14_S_BATCH=COMPLETE
BATCH_START_MAIN_SHA=58ebe4a8312c74a7d909138c49472e1e4b0825e9
BATCH_PUBLICATION_MAIN_SHA=PENDING_FINAL_RECHECK
BATCH_FIRST_STAGE=Stage14-s7-81
BATCH_LAST_STAGE=Stage14-s7-83
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_S_RECEIVER=LowCoreThreeDivisorCorrelation_OR_HeavyRayPolynomialRadialSquareDilationPhysicalFactorSupport_OR_SeparatedMoverDispersionH_OR_DiffusePolynomialGaussianFactorCorrelationH
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-84
```

This batch starts from latest merged main after the batch-contract update that integrates newly exposed `sH` audits into the same batch. No new `sH` is exposed here, so all three substantive work units are ordinary s stages.

Merged `4eq` and Work-boX27 supersede the unresolved fixed-`h` branch left by s7-80: one exact radial value has only `B^o(1)` canonical-background reverse multiplicity. `s7-81` then proves a raw-cell packing bound

```text
M_ray <= B^o(1) * (1 + min(R/|x|,S/|y|)),
```

so polynomial heavy-ray mass forces polynomial radial capacity and a corresponding primitive-ray height gap.

`s7-82` substitutes the moving radius into the exact second reciprocal identity:

```text
h^2*(x^2-y^2)=4*epsilon_x*Xr*Yr*U*V.
```

Thus radial mobility enters the physical packet only through a moving square dilation `h^2` of the fixed primitive-ray factor `D0=x^2-y^2`; fixed-`h` divisor/reconstruction fibers remain `B^o(1)` and cannot be recharged.

`s7-83` removes those inner fibers and defines the exact accepted radial support. The heavy-ray branch is now exponent-equivalent to the set of `h` for which the square dilate `h^2 D0` admits a full physical factor packet and canonical reconstruction. Prime valuations move by the even increments `2 v_ell(h)`.

The heavy-ray receiver therefore materially changes from opaque radial incidence to

```text
FixedPrimitiveReciprocalRayPolynomialRadialSquareDilationPhysicalFactorSupport.
```

The batch stops at that first receiver change. No new sH is opened; `s7-84` should project the retained squarefree/coprime/allocation masks onto the moving prime valuations of `h` before deciding whether a theorem audit is warranted.
