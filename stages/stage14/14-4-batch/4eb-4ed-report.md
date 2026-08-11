# Stage14-4 batch — 4eb through 4ed

Requested target was approximately five stages (`4eb` through `4ef`) in one batch. The batch is intentionally stopped after three substantive stages because a newly merged theorem boundary triggers the mandatory external-lemma gate.

Batch start main:

```text
e601b1e4224e718eafa67018f964ca40ee607377
```

Publication recheck observed newly merged main through:

```text
76bc8a4e59d8d220c58552e42dafef7d12ef55a3
```

including merged `Stage14-s7-69..71`. Unmerged descendants remain advisory only.

## Stage summary

`Stage14-4eb` independently substitutes the canonical primitive coordinates into the first reciprocal equation and proves it is the reconstructed identity `(D+A)^2-(D-A)^2=4DA`; no fixed-power selector remains there.

`Stage14-4ec` consumes newly merged s7-69/70 and reduces the only live reciprocal condition to the primitive Gaussian norm divisibility

```text
C0 | X0^2+Y0^2,
gcd(X0,Y0)=1,
gcd(C0,X0Y0)=1,
```

for a charged-once `B^o(1)` candidate fiber on the canonical allocation background.

`Stage14-4ed` consumes newly merged s7-71. It proves that the same `C0` root line cannot be double charged, divisor switching is only a `B^o(1)` reparametrization, pointwise root-line counting is insufficient, and the remaining object is genuinely an averaged correlated Gaussian-root density theorem.

## Mandatory stop

Merged s7-71 has already frozen the auxiliary target

```text
Stage14-sH71
CanonicalAllocationConditionalPrimitiveGaussianRootDensity
```

and no merged `sH71` result exists at publication recheck. Therefore creating `4ee` or `4ef` as substantive theorem stages would merely rewrite a receiver that is explicitly blocked on an external theorem audit. The requested five-stage batch correctly stops at three stages.

## Frozen batch boundary

```text
STAGE14_4_BATCH=STOPPED_EARLY
BATCH_START_MAIN_SHA=e601b1e4224e718eafa67018f964ca40ee607377
BATCH_PUBLICATION_MAIN_SHA=76bc8a4e59d8d220c58552e42dafef7d12ef55a3
BATCH_REQUESTED_MAX_STAGE_COUNT=5
BATCH_FIRST_STAGE=Stage14-4eb
BATCH_LAST_STAGE=Stage14-4ed
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_STOP_REASON=new_external_lemma_needed
NEWLY_MERGED_S7_69_71_CONSUMED=true
CURRENT_GLOBAL_RECEIVER=PrimitiveCoprimeBinaryFormsCanonicalBalancedIntegerGaussianAllocationDensity_x_ConditionalPrimitiveGaussianRootDensity
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=true
MAINLINE_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
S_ROUTE_H_NEEDED=true
AUXILIARY_STAGE=Stage14-sH71
NEXT=Stage14-sH71
```
