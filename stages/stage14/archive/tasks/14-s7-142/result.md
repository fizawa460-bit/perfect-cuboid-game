# Stage14-s7-142 — q17-good hit packets and s witnesses have the same fixed-power exponent

## Status

`COMPLETE_GOOD_PACKET_HIT_TO_WITNESS_SUPPORT_EXPONENT_EQUIVALENCE`

Consumes batch-local `Stage14-s7-141` and the merged `B^o(1)` pushforward-fiber envelope.

## 1. Hit witness support

With

```text
H := G intersect pi(Lambda),
```

define

```text
Lambda_H := {lambda in Lambda : pi(lambda) in G}.
```

Because every `theta in H` is in `pi(Lambda)`, its fiber contains at least one retained s witness. By the already-consumed uniform fiber envelope it contains at most `B^o(1)` witnesses. Therefore

```text
#H <= #Lambda_H <= B^o(1) #H.
```

Hence `H` and `Lambda_H` have the same fixed-power exponent on every frozen principal cell.

```text
S_GOOD_HIT_PACKET_TO_WITNESS_SUPPORT_EQUIVALENCE_PROVED=true
S_GOOD_HIT_FIBER_MULTIPLICITY=Bo1
S_GOOD_HIT_FIBER_MULTIPLICITY_RECHARGED=false
```

## 2. Exact coverage deficit

Write

```text
#Lambda = B^(sigma_mult+o(1)),
#Lambda_H = B^(sigma_hit+o(1)).
```

Define

```text
delta_hit := sigma_mult-sigma_hit >= 0.
```

This is exactly the fixed-power loss incurred by restricting the conditioned s measure to q17-good pushforward packets. It is the same exponent loss whether measured using hit witnesses `Lambda_H` or hit packets `H`.

No statement here proves `delta_hit=0` or `delta_hit>0`.

```text
S_Q17_GOOD_PACKET_HIT_DEFICIT_DEFINED=true
S_Q17_GOOD_PACKET_HIT_DEFICIT_ZERO_PROVED=false
```

## 3. Post-mask remains outside

The residual root/canonical/post-column mask is not part of `G`, `H`, or `Lambda_H`. Its loss remains a separate later deficit and cannot be inferred from q17-good arithmetic support.

```text
POST_MASK_REMAINS_SEPARATE=true
Q17_GOOD_HIT_SAVING_CROSS_PROMOTABLE_TO_POST_MASK=false
```

## Boundary

```text
STAGE14_S7_142=COMPLETE_GOOD_PACKET_HIT_TO_WITNESS_SUPPORT_EXPONENT_EQUIVALENCE
S_GOOD_HIT_PACKET_TO_WITNESS_SUPPORT_EQUIVALENCE_PROVED=true
S_Q17_GOOD_PACKET_HIT_DEFICIT_DEFINED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-143
```
