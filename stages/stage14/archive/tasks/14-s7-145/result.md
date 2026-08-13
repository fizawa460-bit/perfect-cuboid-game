# Stage14-s7-145 — q21 intersection first/second moment test

## Status

`COMPLETE_Q21_INTERSECTION_SECOND_MOMENT_AUTOCONTROL`

Consumes Stage14-s7-144 and the already-consumed pushforward fiber bound from Stage14-s7-140/142.

For packet occupancy `a(theta)` define on the good set

```text
M1_G := sum_{theta in G} a(theta),
M2_G := sum_{theta in G} a(theta)^2.
```

The previously proved frozen-cell fiber envelope is

```text
0 <= a(theta) <= B^o(1).
```

Therefore pointwise `a(theta)^2 <= B^o(1) a(theta)`, hence

```text
M2_G <= B^o(1) M1_G.
```

Also Cauchy gives, for `H=G intersect pi(Lambda)`,

```text
M1_G^2 <= #H * M2_G,
```

so whenever `M1_G>0`,

```text
#H >= M1_G / B^o(1).
```

Together with `#H <= M1_G`, hit-packet support and the good-indicator first moment are fixed-power exponent equivalent.

The `B^o(1)` occupancy envelope is consumed only as a multiplicity sandwich; it is not recharged as a density saving.

Thus q21's second-moment branch introduces no new independent obstruction. The remaining analytic burden is a uniform lower bound for the first moment `M1_G` in the charged scalar or `(E,m)` measure.

```text
Q21_INTERSECTION_FIRST_SECOND_MOMENT_TEST=PASS_SECOND_MOMENT_AUTOCONTROL
S_GOOD_PACKET_SECOND_MOMENT_LE_Bo1_FIRST_MOMENT=true
S_GOOD_PACKET_SUPPORT_FIRST_MOMENT_FIXED_POWER_EQUIVALENT=true
S_GOOD_PACKET_FIRST_MOMENT_LOWER_BOUND_PROVED=false
PUSHFORWARD_FIBER_BOUND_RECHARGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-146
```