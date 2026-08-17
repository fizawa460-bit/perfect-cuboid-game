# Stage27-20-r302c — the legal averaged alternative is a physically weighted good/bad wall-cell dichotomy

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_FIRST_MOMENT
PARENT_ROUTE=Stage27-20-r302b
SOURCE_STAGE=Stage20

## 1. Why an unweighted exceptional-set statement is not enough

The frozen Stage14 MAIN gate asks for control compatible with every retained principal regime because the half-power obstruction may concentrate.  Saying that a theorem holds for all but `o(#cells)` cells, or on average in an unrelated auxiliary-label measure, does not by itself bound the physical wall population: one exceptional wall cell can still carry `B^(1/2+o(1))` complete-host mass.

Thus an averaged theorem is useful only if its exceptional set is charged in the same physical complete-host measure that dominates occupied `q1` support.

## 2. Exact good/bad alternative

Partition the retained fixed-width wall cells into

\[
W_{\eta_0}^{\rm cell}=\mathcal G\sqcup\mathcal B.
\]

A sufficient replacement for full every-cell uniformity is the pair of estimates

\[
\sum_{P\in\mathcal G}F_{\rm MAIN}(P;B)
\ll B^{1/2-\delta_G+o(1)},
\]

and

\[
\sum_{P\in\mathcal B}H_{\rm phys}(P;B)
\ll B^{1/2-\delta_B+o(1)},
\]

for fixed `delta_G,delta_B>0`, where `H_phys(P;B)` is a complete Stage14 physical-host count for the bad cell before later restrictive masks.  The bad-cell cost must be a genuine physical mass bound; cardinality of the set of bad labels alone is not enough.

Because every legal MAIN tuple in a bad cell is dominated by its complete physical host,

\[
\sum_{P\in W_{\eta_0}^{\rm cell}}F_{\rm MAIN}(P;B)
\ll B^{1/2-\min(\delta_G,\delta_B)+o(1)}.
\]

R302b then transfers this to occupied `q1` support and, after r301u/r301s,

\[
N_2(B)\ll B^{1/2-\Delta+o(1)},
\quad
\Delta=\min(\delta_G,\delta_B,2\eta_0,1/16)>0.
\]

## 3. Surviving theorem target

The next analytic attack therefore has two legal success modes:

1. prove the uniform/aggregate wall-slab MAIN first-moment power deficit from r302a; or
2. prove it on a good set and prove a fixed-power **physical-host mass deficit** for the exceptional bad set.

An exceptional-set theorem averaged over moduli, residues, or auxiliary labels cannot be promoted unless an exact adapter bounds the exceptional preimage in this physical host measure.  This is the same accounting firewall that blocked earlier unweighted average-to-fixed-packet promotions.

No such theorem is proved in r302c.

```text
STAGE27_20_R302C_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PHYSICALLY_WEIGHTED_EXCEPTIONAL_CELL_DICHOTOMY_DERIVED=true
UNWEIGHTED_EXCEPTIONAL_CELL_COUNT_SUFFICIENT=false
UNRELATED_LABEL_AVERAGE_SUFFICIENT=false
BAD_CELL_PHYSICAL_HOST_MASS_DEFICIT_REQUIRED=true
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
BAD_CELL_FIXED_POWER_MASS_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r302d
STOP_REASON=WALL_SLAB_FIRST_MOMENT_POWER_DEFICIT_OR_PHYSICALLY_WEIGHTED_EXCEPTIONAL_CELL_MASS_DEFICIT_REQUIRED
```
