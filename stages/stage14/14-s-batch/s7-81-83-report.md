# Stage14-s-batch report — s7-81 through s7-83

```text
STAGE14_S_BATCH=COMPLETE
BATCH_START_MAIN_SHA=826205ff8aee31a80612583248af81421000e39c
BATCH_PUBLICATION_MAIN_SHA=PENDING_FINAL_RECHECK
BATCH_FIRST_STAGE=Stage14-s7-81
BATCH_LAST_STAGE=Stage14-s7-83
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_S_RECEIVER=LowCoreThreeDivisorCorrelation_OR_HeavyRayFactorKernelDiffusionOrSquarePartMobility_OR_SeparatedMoverDispersionH_OR_DiffusePolynomialGaussianFactorCorrelationH
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-84
```

This batch is restacked on latest merged main after `Stage14-4ev..4ex` independently advanced the heavy-ray radial branch beyond the earlier s7-80 boundary. The merged mainline result

```text
T=4*Xr*Yr*epsilon_x*U*V=K*(t0*h)^2
```

with fixed primitive-ray squarefree kernel `K` and injective `h -> T` is treated as theorem source rather than reproved.

`s7-81` removes the harmless square `4` and frozen sign and rewrites the fixed-kernel condition exactly as

```text
sqf(|Xr|*|Yr|*|U|*|V|)=K,
```

or primewise as one valuation-parity relation across the four correlated physical factors. No per-prime independent density is charged.

`s7-82` chooses one charged factor packet per accepted radial value. Since distinct accepted `h` give distinct products `T`,

```text
#H_phys <= |S_Xr| |S_Yr| |S_U| |S_V|.
```

Therefore polynomial radial support forces at least one of the four factor-value supports to be polynomial; one mover factor label can be frozen at O(1) cost.

`s7-83` writes the selected mover factor uniquely as

```text
F_*=kappa*a^2
```

and proves the quantitative dichotomy: polynomial factor mobility forces either polynomially many squarefree kernels `kappa`, or one fixed kernel carrying polynomially many square-part values `a`. The heavy-ray receiver materially changes to

```text
FixedPrimitiveRayDiffusePhysicalFactorSquarefreeKernelCorrelation
OR
FixedPrimitiveRayFixedFactorKernelPolynomialSquarePartPhysicalIncidence.
```

The batch stops at that receiver change. No new `sH` is opened: both branches first need their exact factor-specific physical coefficient systems exposed. Existing mover/diffuse H gates are different receivers and are not cross-promoted.
