# Stage27-60a — interval-stable transition calculus

```text
TASK_ID=Stage27-60a
PARENT=Stage27-50c
ROUTE_KIND=MAINLINE_INTERVAL_TRANSITION_CALCULUS
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

Checkpoint50 exported the certified Stage27 state as an exponent interval rather than a point value:

\[
\alpha_{N_2}\in[1/4,1/2]
\]

in the usual exponent-envelope sense. Checkpoint60 therefore asks which downstream transition statements are stable for every admissible value in this interval.

For any downstream population exponent `gamma`, a comparison `alpha_N2 < gamma` is certified only if the whole interval lies below `gamma`, i.e. `1/2<gamma`; similarly `alpha_N2 > gamma` is certified only if `1/4>gamma`. If `gamma` lies in `[1/4,1/2]`, ordering is unresolved without additional information.

For exponent losses or retention ratios represented by an affine monotone map

\[
F(\alpha)=u+v\alpha,
\]

with known sign of `v`, the certified image is exactly the endpoint interval

\[
F([1/4,1/2])=[\min(F(1/4),F(1/2)),\max(F(1/4),F(1/2))].
\]

Thus downstream Stage27 calculations need not stop merely because the true `N2` exponent is unknown: they may propagate interval-valued exponents whenever the transformation is monotone and already justified by earlier stage contracts.

No new counting theorem is claimed here.

```text
INTERVAL_TRANSITION_CALCULUS_PROVED=true
POINT_VALUE_REQUIRED_FOR_MONOTONE_PROPAGATION=false
N2_INTERVAL=[1/4,1/2]
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-60b
```
