# Stage14-s7-143 — freeze q17-good intersection lower-coverage receiver

## Status

`COMPLETE_Q17_GOOD_INTERSECTION_LOWER_COVERAGE_RECEIVER_CHANGE`

Consumes batch-local `Stage14-s7-141/142` and merged `Stage14-Work-chX46`.

## 1. Minimal unresolved arithmetic support target

The active nonaligned arithmetic obstruction is now exactly the exponent of

```text
H = G intersect pi(Lambda),
```

or equivalently the exponent of

```text
Lambda_H = {lambda in Lambda : pi(lambda) in G}.
```

By s7-142 these have the same fixed-power exponent. Therefore no pointwise pushforward weight comparison is needed as an additional theorem object once the intersection support itself is controlled.

The stable theorem species are

```text
UniformScalarFilteredTau3Q17GoodPacketPushforwardIntersectionLowerCoverage
UniformPolynomialOuterPairFilteredTau3Q17GoodPacketPushforwardIntersectionLowerCoverage.
```

The pair theorem retains the charged `(E,m)` outer measure; no `Em` scalarization is permitted.

```text
S_PUSHFORWARD_WEIGHT_COMPARISON_AS_FINAL_TARGET_SUPERSEDED=true
S_Q17_GOOD_INTERSECTION_THEOREM_SPECIES_COUNT=2
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
```

## 2. Exact deficit ledger

Let `S_mult=Lambda`, `S_hit=Lambda_H`, and let `S_phys` be the final support after the residual post-mask. With exponents

```text
sigma_mult, sigma_hit, tau_phys
```

define

```text
delta_hit := sigma_mult-sigma_hit,
delta_post := sigma_hit-tau_phys.
```

Then exactly

```text
tau_phys = sigma_mult-delta_hit-delta_post.
```

The q17 reciprocal-CRT kernel is not charged again.

```text
S_GOOD_INTERSECTION_POSTMASK_LEDGER_PROVED=true
Q17_INNER_KERNEL_DEFICIT_RECHARGED=false
POST_MASK_REMAINS_SEPARATE=true
```

## 3. Routing decision

This is a material sharpening of the s7-140 / Work-chX46 lower-coverage receiver: the missing adapter is now a concrete intersection-support theorem rather than a generic lower-domination statement.

A new s-local H is not opened. The object is now sufficiently stable to justify the next XQ/q decision about whether a nonduplicate literature/interface search exists for this intersection-support species.

```text
RECEIVER_MATERIALLY_CHANGED=true
S_ROUTE_H_NEEDED=false
Q21_THEOREM_TARGET_NOW_STABLE=true
Q21_TRIGGER_DECISION_DEFERRED_TO_XQ=true
WORK_CHX46_REVISIT_TRIGGER_S7_143_REACHED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-144
```

## Boundary

```text
STAGE14_S7_143=COMPLETE_Q17_GOOD_INTERSECTION_LOWER_COVERAGE_RECEIVER_CHANGE
S_Q17_GOOD_INTERSECTION_THEOREM_SPECIES_COUNT=2
S_Q17_GOOD_PACKET_COVERAGE_PROVED=false
Q21_THEOREM_TARGET_NOW_STABLE=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-144
```
