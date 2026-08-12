# Stage14-Work-chX46 receiver matrix

| Route / realization | Charged measure | Current arithmetic receiver | Status |
|---|---|---|---|
| main / aligned fixed-E two-sided | fixed-E primitive rectangle | `UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment` | parked external gate |
| s / nonaligned scalar branches | filtered-tau3 conditioned scalar support | `UniformScalarFilteredTau3ConditionedQ17GoodPacketPushforwardLowerCoverage` | active |
| s / polynomial outer-pair branch | filtered-tau3 conditioned `(E,m)` support | `UniformPolynomialOuterPairFilteredTau3ConditionedQ17GoodPacketPushforwardLowerCoverage` | active |
| s / all active nonaligned branches after coverage | same charged branch measure | residual root/canonical/post-column post-mask | active, separately charged |
| fixed-U | one frozen Gaussian residue packet | `SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio` | parked external gate |

## Non-transfer locks

```text
IDENTICAL_Q17_KERNEL_DOES_NOT_IDENTIFY_CHARGED_MEASURE=true
PUSHFORWARD_POINTWISE_UPPER_ENVELOPE_DOES_NOT_PROVE_GOOD_PACKET_COVERAGE=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## q ledger

```text
Q_LEDGER_BASELINE=Stage14-q17+Stage14-q20
Q21_NEEDED=false
Q21_TRIGGERED=false
```

## H ledger

```text
MAINLINE_H_NEEDED=true
MAINLINE_H_COMPLETED=true
MAINLINE_BLOCKED_BY_H=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
FIXED_U_H_COMPLETED=true
FIXED_U_BLOCKED_BY_H=true
TH34_NEEDED=false
```
