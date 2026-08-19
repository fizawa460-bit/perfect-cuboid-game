# StructureRadar parallel batch 35D — SR-STR-168 twisted-divisor ambient expansion with physical adapter firewall

BATCH_ID=SR-BATCH-PARALLEL-35D-168-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=D
STRUCTURE=SR-STR-168
MODE=PARALLEL_DEEP_ATTACK
BASE_MAIN=4d87d7f5461ee019229b31cd5f8c0947e13dbc0c
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 33D. There the norm-ratio collision was reduced exactly to

```text
N(z1)=a m,
N(z2)=b m,
(a,b)=1,
m>=1,
```

on the retained physical Gaussian branch. The actual object is the restricted physical representation weight `R_phys(n;packet)`, not automatically the full ambient two-square representation number `r_2(n)`.

## 1. Exact ambient arithmetic identity

For positive integers `n`, the ordered signed ambient two-square representation number satisfies

```text
r_2(n) = 4 sum_{d|n} chi_4(d),
```

where `chi_4` is the primitive real character modulo 4. Hence the ambient product has the exact expansion

```text
r_2(a m) r_2(b m)
 = 16 sum_{d1|a m} sum_{d2|b m} chi_4(d1) chi_4(d2).
```

Consequently an **ambient** common-`m` correlation of the form

```text
sum_m w(m) r_2(a m) r_2(b m)
```

can be rewritten exactly as

```text
16 sum_{d1,d2} chi_4(d1)chi_4(d2)
   sum_{m: d1|a m, d2|b m} w(m).
```

Because `(a,b)=1`, the divisibility constraints can then be reduced deterministically to constraints on the same common quotient `m` after removing portions already supplied by `a` and `b`.

This identity is useful arithmetic normalization, but it is **not** yet an exact expansion of the Stage14/MAIN physical object `R_phys(a m;packet_1)R_phys(b m;packet_2)`. The physical primitive/orientation/range/charged-once masks live on Gaussian representations themselves and cannot be replaced by ambient `r_2` merely by moving them into a scalar weight `w(m)`.

## 2. Correct smaller restart point

The audit therefore does not accept the stronger statement that the physical Gaussian representation layer has already been fully converted to a mod-4 divisor convolution.

What has been exposed is the ambient target architecture. The first missing bridge is now

```text
FIRST_MISSING_LEMMA=SameMeasurePhysicalRestrictedGaussianToTwistedDivisorConvolutionAdapter
```

A sufficient form is:

> Uniformly in the retained coprime parameters `(a,b)`, express the exact restricted physical representation correlation in the common quotient `m` as a `B^o(1)`-complexity combination of mod-4 twisted divisor-convolution terms, or another equivalent spectral/divisor form, with coefficient `L1/L2` norms controlled by the original physical energy and with all primitive/orientation/range/charged-once masks and quantifier order preserved. Only after this exact same-measure adapter is proved may a fixed-power twisted-divisor correlation theorem be charged.

After that adapter, the next analytic target would be a same-measure fixed-power deficit for the resulting twisted divisor correlations. The ambient `r_2` identity alone supplies no density saving and no license to discard physical representation masks.

## 3. Firewalls

```text
COMMON_NORM_QUOTIENT_PARAMETERIZATION_REUSED=true
AMBIENT_R2_CHI4_DIVISOR_EXPANSION=PROVED
PHYSICAL_RPHYS_TO_AMBIENT_R2_REPLACEMENT_PROVED=false
PHYSICAL_RESTRICTED_TO_TWISTED_DIVISOR_ADAPTER_PROVED=false
GAUSSIAN_MULTIPLICITY_AS_POWER_SAVING_FORBIDDEN=true
TWISTED_DIVISOR_CORRELATION_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=SameMeasurePhysicalRestrictedGaussianToTwistedDivisorConvolutionAdapter
SR_STR_168_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
