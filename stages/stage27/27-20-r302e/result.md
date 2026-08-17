# Stage27-20-r302e — the next legal saving must hit primitive-pair occupancy in physical weight

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_FIRST_MOMENT
PARENT_ROUTE=Stage27-20-r302d
SOURCE_STAGE=Stage20

R302d closes pure CRT repackaging. The surviving place for a genuinely new saving is earlier: after the common-core data are fixed, but before the primitive rectangle pair `(U,V)` and the reduced column support are charged independently by the Stage14 complete-host ledger.

For a fixed-width critical wall slab, define the physical primitive-pair weight

\[
w_B(U,V)=\#\{\text{legal wall MAIN tuples carried by the primitive pair }(U,V)\},
\]

where all frozen common-core, nested-divisor, root, parity, chamber and physical filters are retained in their original quantifier order. This is a pushforward of the same Stage14 physical-host measure; it is not an unweighted count of residue labels.

A sufficient genuinely new theorem is therefore a fixed-power occupancy deficit of the form

\[
\sum_{(U,V)\in\mathcal P_{\rm wall}(B)} w_B(U,V)
\ll B^{1/2-\delta+o(1)}
\]

for some fixed `delta>0`, or a good/bad decomposition in which the bad primitive-pair preimage has the same fixed-power deficit in physical host mass.

Equivalently, a local statement may be used only if it creates a new correlation between the primitive-pair choice and the common-core/reduced-column variables. Counting fewer residue classes modulo `U` or `V` without controlling the physical preimage is insufficient and would repeat the r302c measure error.

This theorem is not proved here. The point of r302e is to remove exponent-neutral CRT algebra from the search space and identify the exact charged measure where a new first moment must act.

```text
STAGE27_20_R302E_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PHYSICAL_PRIMITIVE_PAIR_WEIGHT_DEFINED=true
PRIMITIVE_PAIR_WEIGHT_USES_STAGE14_HOST_MEASURE=true
UNWEIGHTED_RESIDUE_CLASS_COUNT_SUFFICIENT=false
NEW_CORRELATION_WITH_CORE_OR_COLUMN_REQUIRED=true
PRIMITIVE_PAIR_OCCUPANCY_FIXED_POWER_DEFICIT_PROVED=false
BAD_PAIR_PHYSICAL_PREIMAGE_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r302f
```
