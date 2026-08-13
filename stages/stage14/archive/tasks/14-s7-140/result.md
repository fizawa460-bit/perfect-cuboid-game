# Stage14-s7-140 — one-sided pushforward envelope and exact lower-coverage gate

## Status

`COMPLETE_ONE_SIDED_PUSHFORWARD_CONTROL_AND_LOWER_COVERAGE_RECEIVER_CHANGE`

Consumes batch-local `Stage14-s7-138/139` and merged `Stage14-Work-cgX45`.

## 1. What the existing multiplicity bounds do prove

For each s witness `lambda`, the map `pi(lambda)=theta` is deterministic. Earlier Stage14 divisor/factorization bounds imply that on a frozen polynomial-height principal cell the number of retained first-layer witness decorations mapping to one complete kernel packet is at most `B^o(1)`.

Hence

```text
a_s(theta) <= B^o(1)
```

pointwise after all already-frozen labels are included in `theta`.

This is a genuine one-sided pushforward envelope. It is not a lower comparison with the q17 primitive-pair weight.

```text
S_PUSHFORWARD_POINTWISE_UPPER_ENVELOPE=Bo1
S_PUSHFORWARD_UPPER_CONTROL_PROVED=true
```

## 2. Missing direction is support coverage / lower domination

The q17 theorem domain is built from its fixed-E primitive-pair baseline. The s pushforward support may occupy only a subset selected by the filtered-tau3 first layer and branch-specific prefilters. No merged theorem proves that a fixed-power proportion of q17-good reciprocal-CRT packets is hit by that subset, or equivalently that the s pushforward mass has a uniform lower comparison on q17-good packets.

Thus the remaining arithmetic transfer gate is not another divisor multiplicity estimate. It is

```text
FilteredTau3ConditionedQ17ReciprocalCRTPushforwardLowerCoverage
```

with two charged-measure variants:

```text
UniformScalarFilteredTau3ConditionedQ17ReciprocalCRTPushforwardLowerCoverage
UniformPolynomialOuterPairFilteredTau3ConditionedQ17ReciprocalCRTPushforwardLowerCoverage.
```

```text
S_PUSHFORWARD_LOWER_DOMINATION_PROVED=false
S_Q17_GOOD_PACKET_COVERAGE_PROVED=false
Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false
```

## 3. Deficit ledger

Let `S_mult` be the already-charged first-layer support, `S_cov` those points whose pushed-forward kernel packet lies in the transferable q17-good covered support, and `S_phys` the final post-mask support. Write exponents

```text
sigma_mult, sigma_cov, tau_phys
```

and deficits

```text
delta_cov := sigma_mult-sigma_cov,
delta_post := sigma_cov-tau_phys.
```

Then exactly

```text
tau_phys = sigma_mult-delta_cov-delta_post.
```

The q17 inner kernel itself contributes no new arithmetic-species deficit: its equations are already identified. The unresolved issue is coverage in the conditioned s measure, followed separately by the residual post-mask.

```text
S_CONDITIONED_MEASURE_COVERAGE_POSTMASK_LEDGER_PROVED=true
Q17_INNER_KERNEL_DEFICIT_RECHARGED=false
POST_MASK_REMAINS_SEPARATE=true
```

## 4. Receiver change and routing

The active nonaligned receiver is now the lower-coverage adapter above, followed by the residual post-mask. This is materially sharper than the generic conditioned-measure-transfer label of s7-137.

A new q pass is still not justified: q17 already searched the inner kernel and q20 the conditioned-correlation architecture. The new object is a Stage14-specific pushforward coverage adapter and should first be structurally analyzed by the s/XQ routes.

```text
RECEIVER_MATERIALLY_CHANGED=true
Q21_NEEDED=false
S_ROUTE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-141
```
