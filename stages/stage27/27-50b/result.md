# Stage27-50b — interval comparison against the certified Stage26 M3 lower

```text
TASK_ID=Stage27-50b
PARENT=Stage27-50a
ROUTE_KIND=MAINLINE_COMPARISON_SYNTHESIS
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The current certified inputs are

\[
N_2(B)\in[B^{1/4-o(1)},\,B^{1/2+o(1)}]
\]

and from Stage26

\[
M_3(B)\ge B^{1/3-o(1)}.
\]

These are not enough to order the two quantities asymptotically on exponent scale. The Stage26 lower exponent `1/3` lies strictly inside the current Stage27 interval `[1/4,1/2]`.

Therefore:

- the certified lower bound for `M_3` is stronger than the certified lower bound for `N_2`;
- this does **not** imply `M_3(B)>N_2(B)` asymptotically, because the true `N_2` exponent may exceed `1/3`;
- conversely the current `N_2` upper `1/2+o(1)` does not imply `N_2(B)>M_3(B)`, since Stage26 has no matching upper exponent identifying `M_3`;
- a finite-range fitted Stage27 slope near `0.421...` cannot resolve this comparison.

Thus the comparison is formally classified as

```text
N2_VS_M3_EXPONENT_ORDER=UNRESOLVED_OVERLAPPING_INTERVALS
M3_CERTIFIED_LOWER_STRONGER_THAN_N2_CERTIFIED_LOWER=true
ASYMPTOTIC_ORDERING_PROVED=false
```

This is still useful mainline information: Checkpoint50 records precisely which requested cross-stage comparisons survive the unresolved true `N_2` exponent and which do not.

The same interval-overlap rule should be used for subsequent Stage27 comparisons. A downstream comparison becomes decidable only when the other quantity has a certified interval wholly below `1/4` or wholly above `1/2`, or when a stronger directional theorem is available.

```text
INTERVAL_COMPARISON_PROTOCOL_APPLIED=true
FALSE_ORDERING_FROM_LOWER_BOUNDS_FORBIDDEN=true
NEXT_DERIVED_ROUTE=27-50c
ADVANCE_TO_CHECKPOINT60=false
```
