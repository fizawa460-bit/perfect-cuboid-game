# Stage27-20-r302f — exact critical-wall budget isolates a quarter-power primitive-pair occupancy barrier

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_FIRST_MOMENT
PARENT_ROUTE=Stage27-20-r302e
SOURCE_STAGE=Stage20

On the nonproportional critical segment inherited from r301v,

\[
\theta=1/4,\qquad 1/8\le\phi\le1/4,\qquad \chi=2\phi-1/4.
\]

Stage14's charged-once complete-host decomposition has exponent costs

\[
\chi\quad\text{(common core)},
\]
\[
2\phi-\chi\quad\text{(primitive pair }(U,V)\text{)},
\]
\[
1/4-\chi\quad\text{(reduced column support)}.
\]

Substituting the critical relation gives

\[
2\phi-\chi=1/4,
\]

and

\[
\chi+(2\phi-\chi)+(1/4-\chi)
=(2\phi-1/4)+1/4+(1/2-2\phi)=1/2.
\]

Thus the primitive-pair layer occupies an exact quarter-power slot throughout the entire critical segment. This does **not** prove that the actual number of occupied primitive pairs is `B^(1/4+o(1))`; it identifies the complete-host budget that can saturate at that scale.

Consequently a direct legal progress theorem may target a physical-weighted primitive-pair support bound

\[
\mathcal W_{UV}(B)\ll B^{1/4-\delta+o(1)}
\]

uniformly after the compatible core/column weights are retained, or an equivalent correlation estimate saving `B^{-delta}` from the product of the three charged layers. An unweighted pair count, a second use of the root ledger, or a bare CRT modulus count is not enough.

This is a sharper theorem target than r302a's generic first moment:

`CriticalWallPhysicalPrimitivePairOccupancyOrCoreColumnCorrelationPowerDeficit`.

No such deficit is proved in this batch.

```text
STAGE27_20_R302F_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CRITICAL_THETA=1/4
CRITICAL_CHI=2phi-1/4
CRITICAL_PRIMITIVE_PAIR_HOST_EXPONENT=1/4
CRITICAL_TOTAL_HOST_EXPONENT=1/2
ACTUAL_PRIMITIVE_PAIR_SUPPORT_ASYMPTOTIC_CLAIMED=false
PHYSICAL_WEIGHTED_UV_POWER_DEFICIT_PROVED=false
CORE_COLUMN_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r302g
NEXT_TARGET=PROVE_CRITICAL_WALL_PHYSICAL_PRIMITIVE_PAIR_OCCUPANCY_OR_CORE_COLUMN_CORRELATION_POWER_DEFICIT
```
