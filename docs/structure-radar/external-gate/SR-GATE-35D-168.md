# StructureRadar parallel batch 35D — SR-STR-168 twisted-divisor expansion

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

on the retained physical Gaussian branch. Fixed-`m` representation multiplicity was bounded only by `B^o(1)` and was not charged as a density saving.

## 1. Exact arithmetic expansion of the Gaussian multiplicity

For positive integers `n`, the ordered signed two-square representation number satisfies

```text
r_2(n) = 4 sum_{d|n} chi_4(d),
```

where `chi_4` is the primitive real character modulo 4. Therefore the common-quotient multiplicity has the exact expansion

```text
r_2(a m) r_2(b m)
 = 16 sum_{d1|a m} sum_{d2|b m} chi_4(d1) chi_4(d2).
```

Consequently any same-measure common-`m` correlation of the form

```text
sum_m w(m) r_2(a m) r_2(b m)
```

becomes exactly

```text
16 sum_{d1,d2} chi_4(d1)chi_4(d2)
   sum_{m: d1|a m, d2|b m} w(m),
```

with the original nonnegative/signed physical weight `w(m)` retained. No ambient representation-density statement is used.

Because `(a,b)=1`, the conditions `d1|a m` and `d2|b m` may further be reduced by removing the portions already dividing `a` and `b`; the remaining divisibility constraints are imposed on the same common quotient `m`. This is deterministic divisor algebra, not a saving.

## 2. Smaller restart point

The old gate `SameMeasurePhysicalCommonNormQuotientCorrelationDeficit` bundled Gaussian representation theory with the physical weighted correlation. The Gaussian representation layer is now fully converted to a mod-4 twisted divisor convolution.

The surviving theorem target is

```text
FIRST_MISSING_LEMMA=SameMeasurePhysicalTwistedDivisorConvolutionCorrelationDeficit
```

A sufficient form is:

> Uniformly in the retained coprime parameters `(a,b)`, prove a fixed positive-power deficit for the exact `H_phys^MAIN`-derived common-quotient weight against the two mod-4 twisted divisor constraints obtained above, preserving all masks and quantifier order. Equivalent spectral/dispersion/divisor-correlation formulations are admissible only if their coefficient norms are controlled by the same physical measure.

This target is narrower than a generic Gaussian norm-family theorem: the Gaussian geometry has been reduced to explicit `chi_4` divisor convolution on the single common scalar `m`.

## 3. Firewalls

```text
COMMON_NORM_QUOTIENT_PARAMETERIZATION_REUSED=true
R2_CHI4_DIVISOR_EXPANSION=PROVED
GAUSSIAN_MULTIPLICITY_AS_POWER_SAVING_FORBIDDEN=true
TWISTED_DIVISOR_CORRELATION_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=SameMeasurePhysicalTwistedDivisorConvolutionCorrelationDeficit
SR_STR_168_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
