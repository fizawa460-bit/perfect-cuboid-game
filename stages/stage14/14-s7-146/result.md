# Stage14-s7-146 — freeze good-packet indicator first-moment lower-bound receiver

## Status

`COMPLETE_GOOD_PACKET_INTERSECTION_TO_FIRST_MOMENT_RECEIVER_CHANGE`

Consumes Stage14-s7-144/145 and merged Work-ciX47/q21.

The previous generic intersection lower-coverage target is now equivalent at fixed-power scale to a first-moment lower bound for

```text
M1_G = sum_{lambda in Lambda} 1_G(pi(lambda))
     = sum_{theta in G} a(theta).
```

The second moment is automatically controlled by the already-consumed `B^o(1)` occupancy envelope, so no separate dispersion/collision theorem is required merely to pass from this first moment to intersection support.

The two charged theorem species are therefore sharpened to

```text
UniformScalarFilteredTau3Q17GoodPacketIndicatorFirstMomentLowerBound
UniformPolynomialOuterPairFilteredTau3Q17GoodPacketIndicatorFirstMomentLowerBound.
```

For the pair branch, all weights and quantifiers remain on `(E,m)`; no projection to `n=Em` is charged as a saving or used to change theorem measure.

Let `sigma_mult` denote the first-layer charged support exponent, `sigma_good` the exponent of witnesses counted by `M1_G`, and `tau_phys` the final physical exponent. Define

```text
delta_good := sigma_mult - sigma_good,
delta_post := sigma_good - tau_phys.
```

Then exactly

```text
tau_phys = sigma_mult - delta_good - delta_post.
```

The residual root/canonical/post-column mask remains separately charged after the good-indicator first-moment gate.

No direct theorem from q21 proves the required lower bound, so the theorem species is analytically unresolved. This is a material receiver change from intersection support to exact first-moment correlation.

```text
RECEIVER_MATERIALLY_CHANGED=true
Q21_INTERSECTION_SECOND_MOMENT_NEW_GATE=false
S_GOOD_PACKET_FIRST_MOMENT_LOWER_BOUND_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
Q22_THEOREM_TARGET_NOW_STABLE=true
NEXT=Stage14-s7-147
```