# Stage14-Work-bwX35 receiver / capacity matrix

| Route / branch | Charged outer family | Legal capacity envelope | What is already exhausted | Principal-scale survivor | H status |
|---|---|---|---|---|---|
| main/s fixed-E primitive endpoint | moving scalar `s` after fixed `r0` | polynomial interval in `s` | unitary witness choice; `gcd(r0,s)=1` has only `B^o(1)` loss | one-dimensional conditional canonical/reverse completion | internal, no new heavy H / sH |
| main fixed-E two-sided | outer `m` | ordinary-divisor shadow `O_2s(m)` with `A_2s<=B_2s<=O_2s` | unitary restriction for upper-bound purposes | moving ordinary-divisor absolute capacity OR conditional completion | normalize interval before heavy H |
| s polynomial-E fixed primitive product | scalar `E` | polynomial `E` interval | known `gcd(sqf(E),K_Z)=1` mask has zero fixed-power deficit | residual E-local mask OR conditional completion | internal, no sH |
| main/s polynomial-E polynomial primitive product | outer pair `(E,m)` | no theorem-ready ordinary envelope yet | fixed-inner multiplicity already exhausted | bare unitary outer-pair existence OR conditional completion | internal |
| fixed-U endpoint, subquarter width | dyadic endpoint layer `H~B^lambda` | principal annulus capacity `<=B^(2lambda+o(1))` | all fixed-power `lambda<1/4` layers | none | discharged |
| fixed-U safe-modulus quarter endpoint | Gaussian cofactor endpoints with `lambda>=1/4-o(1)` | principal-scale endpoint layer | subquarter capacity; long safe branch by tH31 | fixed-residue Gaussian-prime short-interval occupancy | `tH32` frozen and needed |
| fixed-U beyond-Mitsui quarter endpoint | same quarter-scale endpoint with `d>d_safe` | quarter-scale capacity only | subquarter layers | large-subpolynomial-modulus short-interval residue bias | internal before later H |
| fixed-U beyond-Mitsui long headroom | long reciprocal interval with `d>d_safe` | long-headroom principal baseline | Mitsui-safe modulus range by positive tH31 | large-subpolynomial-modulus residue bias | internal before later H |

## Common structural lock

All current routes obey the same charged-once order of operations:

```text
absolute outer capacity / legal upper envelope
    -> discard subcritical layers
    -> retain only principal-scale survivors
    -> apply arithmetic theorem / conditional correlation analysis
```

This is a workflow and exponent-ledger equivalence only. It does not identify the arithmetic measures.

```text
COMMON_ABSOLUTE_CAPACITY_FIRST_PRINCIPLE_PROVED=true
COMMON_ABSOLUTE_CAPACITY_LOCALIZATION_LANGUAGE_PROVED=true
COMMON_ARITHMETIC_RESIDUAL_RECEIVER_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## q15 handoff status

```text
Q15_UNITARY_TO_ORDINARY_TRANSFER_RESOLVED_FOR_UPPER_BOUND=true
Q15_UNITARY_UPPER_ENVELOPE_ADAPTER_COMPLETE=true
Q15_BOUNDED_DISTORTION_UNITARY_ORDINARY_TRANSFER_PROVED=false
Q15_LOCALIZED_DIVISOR_WIDTH_COMPATIBILITY_REMAINS=true
Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=true
```

The ordinary-divisor enlargement may be used only as an upper envelope. It does not prove that the ordinary and unitary supports have comparable density.

## H matrix

```text
MAINLINE_H_NEEDED=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=true
TH32_NEEDED=true
TH32_EXECUTED=false
T_ROUTE_H_BLOCKING=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

## Whole-family boundary

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PRINCIPAL_SCALE_THEOREM_COVERAGE_COMPLETE=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```
