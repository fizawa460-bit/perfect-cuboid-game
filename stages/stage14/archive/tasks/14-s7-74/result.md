# Stage14-s7-74 — saturation dichotomy between small common core and polynomial-core centered discrepancy

## Status

`COMPLETE_SMALL_CORE_VERSUS_POLYNOMIAL_CORE_CENTERED_DISCREPANCY_RECEIVER_SPLIT`

Consumes batch-local `Stage14-s7-72/73`, merged `Stage14-sH71`, merged `Stage14-4ef`, and latest main.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Reciprocal-root count after scale stratification

The canonical allocation-bearing reciprocal count is partitioned into `B^o(1)` common-core scale cells

```text
kappa=0
```

and fixed-power cells

```text
kappa>0.
```

Batch-local s7-73 gives on each polynomial cell

```text
N_root(kappa)=P_kappa+D_kappa,
P_kappa <= |Omega_kappa| B^(-kappa+o(1)),
```

while on the small-core cell the principal term has no fixed-power deficit.

## 2. Polynomial-core saturation requires centered discrepancy

Fix `kappa>0`. If the accepted reciprocal-root count on this cell has exponent-zero relative density,

```text
N_root(kappa)=|Omega_kappa| B^(-o(1)),
```

then the principal term is too small to support it. Hence necessarily

```text
|D_kappa|=|Omega_kappa| B^(-o(1)).
```

Thus every polynomial-common-core saturating cell forces exponent-zero centered discrepancy of the actual correlated canonical-allocation sequence against the frozen Gaussian root line.

```text
POLYNOMIAL_C0_SATURATION_FORCES_CENTERED_DISCREPANCY_EXPONENT_ZERO=true
```

This is stronger than the sH71 undifferentiated conditional-density receiver: the principal root density has now been discharged exactly.

## 3. Small-core branch cannot be closed by root principal density

On

```text
C0=B^o(1),
```

the root-line principal density is itself `B^(-o(1))`. Therefore a square-root-saturating sequence may survive without contradicting any root-spacing estimate.

The remaining legal polynomial-scale saving level on this branch lies in the canonical allocation-bearing slope family itself. Merged 4ef independently shows that the canonical allocation factor is the correlated three-divisor problem

```text
d_a|a,
d_b|b,
d_+|a^2+b^2
```

with all physical masks retained, and that separate minus/plus ledgers are exponent-neutral.

The s route does not claim the 4ef auxiliary theorem has been proved. It imports only the merged localization that no elementary one-side allocation saving remains.

```text
SMALL_C0_ROOT_PRINCIPAL_SAVING_UNAVAILABLE=true
SMALL_C0_REVERTS_TO_CANONICAL_ALLOCATION_DENSITY_OBSTRUCTION=true
MERGED_4EF_ALLOCATION_LOCALIZATION_IMPORTED=true
```

## 4. Material receiver split

The single s7-71 receiver

```text
CanonicalAllocationConditionalPrimitiveGaussianRootDensity
```

is no longer minimal. After merged sH71 plus s7-72/73, square-root saturation can occur only through one of two structurally distinct branches:

```text
Branch S:
  C0=B^o(1),
  canonical allocation-bearing primitive slopes retain exponent-zero density;

Branch L:
  C0=B^(kappa+o(1)), kappa>0,
  centered Gaussian root-line discrepancy retains exponent-zero size.
```

The canonical receiver is therefore

```text
SmallCommonCoreCanonicalBalancedIntegerGaussianAllocationDensity
OR
PolynomialCommonCoreCanonicalAllocationCenteredGaussianRootDiscrepancy.
```

```text
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. H decision

No new **sH** is opened at this boundary because the batch must stop immediately on receiver change. The two new branches require separate follow-up decisions:

- Branch S already coincides with the merged 4ef theorem-ready allocation-density gate; its external audit belongs to that frozen target rather than reopening sH71.
- Branch L is now smaller than sH71 and should first freeze the exact centered coefficient/quantifier contract before deciding whether a new discrepancy H is warranted.

```text
S7_74_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_74=COMPLETE_SMALL_CORE_VERSUS_POLYNOMIAL_CORE_CENTERED_DISCREPANCY_RECEIVER_SPLIT
POLYNOMIAL_C0_SATURATION_FORCES_CENTERED_DISCREPANCY_EXPONENT_ZERO=true
SMALL_C0_ROOT_PRINCIPAL_SAVING_UNAVAILABLE=true
SMALL_C0_REVERTS_TO_CANONICAL_ALLOCATION_DENSITY_OBSTRUCTION=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_S_RECEIVER=SmallCommonCoreCanonicalBalancedIntegerGaussianAllocationDensity_OR_PolynomialCommonCoreCanonicalAllocationCenteredGaussianRootDiscrepancy
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_74_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-75
```
