# Stage14-s7-117 — consume caX39 and park only the aligned fixed-E two-sided external gate

## Status

`COMPLETE_ALIGNED_FIXED_E_TWO_SIDED_EXTERNAL_GATE_ISOLATION`

Consumes merged `Stage14-s7-114..116`, merged mainline `Stage14-4gf..4gh`, merged `Stage14-Work-caX39`, and merged clean-room `Stage14-4ghH` from batch-start main

```text
ac4fa88e39f51029c13a24a8d4c41841f69ab8bb.
```

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. The aligned realization inherits the exact first-moment gate

Merged s7-114 proves that the s fixed-E two-sided realization is literally the same charged primitive-pair packet as main 4gd. Merged Work-caX39 therefore transfers the 4gh support/first-moment equivalence without a new loss:

```text
#T_rec <= sum N_rec <= B^o(1)#T_rec,
delta_rec(s,fixed-E,two-sided)=delta_rec(main,fixed-E,two-sided).
```

Merged 4ghH audits exactly that first moment and leaves

```text
UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
```

as an unresolved external gate. Hence the aligned s realization is not advanced past that theorem boundary.

```text
S_FIXED_E_TWO_SIDED_FIRST_MOMENT_ADAPTER_CONSUMED=true
S_FIXED_E_TWO_SIDED_EXTERNAL_GATE=UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
S_FIXED_E_TWO_SIDED_EXTERNAL_GATE_RESOLVED=false
S_FIXED_E_TWO_SIDED_BRANCH_PARKED=true
```

This is a same-packet inheritance, not a second H invocation. The main 4ghH audit is not recharged as an sH.

## 2. The external gate is branch-local, not an s-wide stop

Work-caX39 explicitly preserves three nonaligned s realizations outside the fixed-E two-sided adapter:

```text
(A) fixed-E primitive endpoint;
(C) polynomial-E fixed primitive product;
(D) polynomial-E polynomial primitive product / fibered pair.
```

For these realizations s7-116 proves that no baseline-, measure-, witness-, and quantifier-preserving transfer of the main reciprocal-CRT packet has been established. Their receiver remains the generic prefilter followed by reverse/post-column existential completion.

Therefore the unresolved main H gate blocks only realization (B). It does not logically prevent further internal reduction of (A),(C),(D).

```text
S_ROUTE_GLOBALLY_BLOCKED_BY_MAIN_H=false
S_NONALIGNED_REALIZATIONS_REMAIN_ACTIVE=true
S_ROUTE_H_NEEDED=false
```

## 3. Receiver after synchronization

The s receiver is now explicitly asymmetric:

```text
(B) fixed-E two-sided:
    parked external first-moment gate
    + residual post-completion;

(A),(C),(D):
    deterministic prefilter
    + generic existential reverse/post-column completion.
```

No saving is claimed from the H failure, and no density is inferred for the active three branches.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_117_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-118
```

## Boundary

```text
STAGE14_S7_117=COMPLETE_ALIGNED_FIXED_E_TWO_SIDED_EXTERNAL_GATE_ISOLATION
S_FIXED_E_TWO_SIDED_BRANCH_PARKED=true
S_FIXED_E_TWO_SIDED_EXTERNAL_GATE_RESOLVED=false
S_ROUTE_GLOBALLY_BLOCKED_BY_MAIN_H=false
S_NONALIGNED_REALIZATIONS_REMAIN_ACTIVE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-118
```
