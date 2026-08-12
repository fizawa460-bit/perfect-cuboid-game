# Stage14-Work-clX50 receiver / supersession matrix

| Route / layer | Consumed facts | Active unresolved receiver | Forbidden shortcut |
|---|---|---|---|
| main aligned fixed-E | completed negative clean-room H audit | `UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment` | do not propagate this local external gate to all Stage14 branches |
| s nonaligned scalar | q17 kernel; filtered-tau3 support; q22 witness expansion; q23 joint incidence; s7-153..155 common-core/coprime-side split | `UniformScalarFilteredTau3MovingCommonCoreTwoCoprimeSideReciprocalCRTJointIncidenceFirstMomentLowerBound` then post-mask | no fixed-shift/AP promotion without an exact adapter |
| s nonaligned polynomial pair | same inner arithmetic, charged `(E,m)` outer measure | `UniformPolynomialOuterPairFilteredTau3MovingCommonCoreTwoCoprimeSideReciprocalCRTJointIncidenceFirstMomentLowerBound` then post-mask | no `(E,m)->Em` scalarization |
| fixed-U | completed negative tH33 audit | `SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio` | no modulus/residue averaging cross-promotion |
| q ledger | q23 generic witness-coupled joint-incidence radar | q24 sharpened moving-common-core / two-coprime-side radar | do not rerun q23 as q24 |

## Charged-once locks

```text
GOOD_INDICATOR_TO_Q17_WITNESS_EQUIVALENCE_RECHARGED=false
GOOD_PACKET_SECOND_MOMENT_RECHARGED=false
FIRST_REVERSE_EXACT_COMMON_GCD_RECHARGED=false
PQ_COMMON_PRIME_SUPPORT_LOCALIZATION_RECHARGED=false
PQ_COPRIME_SIDE_MOVERS_RECHARGED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
```

## Current s deficit ledger

Let `sigma_mult` be the already-charged filtered-tau3 first-layer exponent, `sigma_ccs` the exponent represented by the common-core/coprime-side joint incidence, and `tau_phys` the final physical exponent after the residual mask. Define

```text
delta_ccs  := sigma_mult - sigma_ccs,
delta_post := sigma_ccs - tau_phys.
```

Then

```text
tau_phys = sigma_mult - delta_ccs - delta_post.
```

q24 may address `delta_ccs` only. It may not be promoted through `delta_post` without a new exact adapter.
