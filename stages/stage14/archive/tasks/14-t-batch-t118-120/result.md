# Stage14-t-batch — t118 through t120

## Status

`COMPLETE_EXCEPTIONAL_MULTIPLIER_TO_GENERIC_NORM_SUPPORT_RECEIVER`

This batch uses the merged integrated-H contract from PR #721. No new tH target was exposed, so the integrated H work-unit count is zero.

## Source boundary

Batch start main:

```text
58ebe4a8312c74a7d909138c49472e1e4b0825e9
```

The batch consumes merged-only `Stage14-t117`, `Stage14-t91`, `Stage14-t114`, `Stage14-Work-boX27`, and the previously merged negative tH26/tH28 boundaries where cited.

During publication recheck, main advanced to

```text
826205ff8aee31a80612583248af81421000e39c
```

through merged mainline PR #722 (`Stage14-4ev..4ex`). That PR changes only the global heavy-ray radial receiver to a fixed-kernel square-value incidence, explicitly retains whole-family exponent `1/2`, and does not identify the fixed-U generic scalar-norm measure or cross-promote a saving. Therefore it does not change t118--t120.

## Work units

### Stage14-t118

The exceptional-local predicate is localized exactly to the exceptional norm factor

```text
n=m_E*n_G,
m_E=gcd(n,E_U^infinity),
gcd(n_G,E_U)=1.
```

After the finite unit/two-primary data are included in the exceptional label,

```text
L_U(n;e)=L_U^E(m_E;e).
```

Thus locally admissible norms are an exact union of exceptional-multiplier cylinders over the generic split-prime norm coordinate.

### Stage14-t119

For packet support `rad(E_U)<=B^C` and physical norm range `m_E<=B^A`, a uniform Rankin estimate at `s=1/log log B`, split at `p=log B`, proves

```text
# {m_E<=B^A: p|m_E => p|E_U}=B^o(1).
```

Hence the admissible exceptional multiplier and exceptional label can both be frozen at charged-once `B^o(1)` cost. The only remaining polynomial cofactor coordinate is the generic scalar norm `n_G`.

### Stage14-t120

After freezing `(m,e)`, the primitive orientation fiber over one generic norm is `B^o(1)`. Applying the merged Work-boX27 support-relocation lemma shows that any fixed-power cofactor-core loss must appear in the weighted outer support

```text
G_phys(m,e)
 = {g: exists primitive generic orientation epsilon surviving the full physical Boolean}.
```

Therefore the earlier t117 local/orientation density mechanisms are superseded as independent power sources. The current fixed-U saving mechanisms reduce to

```text
(A') ExceptionalMultiplierConditionedGenericSplitPrimePhysicalNormSupportDeficit
```

or

```text
(C) PhysicalSelectedProjectiveClassNearTotalPrimeDepletion.
```

This is a material receiver change, so the batch stops after three substantive work units.

## tH decision

No new tH is opened. The generic physical norm support still contains an existential global orientation Boolean not shown to be multiplicative, bounded-Fourier-degree, spin, or Type-I/II compatible. Merged tH26 already blocks generic Hecke/spin promotion at that coefficient level, while merged tH28 blocks a generic unmasked projected-norm sieve saving. The next step is internal arithmetic opening of the support Boolean.

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=58ebe4a8312c74a7d909138c49472e1e4b0825e9
BATCH_PUBLICATION_MAIN_SHA=826205ff8aee31a80612583248af81421000e39c
BATCH_FIRST_STAGE=Stage14-t118
BATCH_LAST_STAGE=Stage14-t120
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUExceptionalMultiplierConditionedGenericSplitPrimePhysicalNormSupportDeficitOrSelectedProjectiveClassNearTotalPrimeDepletion
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
NEXT=Stage14-t121
```
