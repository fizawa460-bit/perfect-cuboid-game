# Stage27-20-r302b — a wall first-moment deficit transfers monotonically to occupied q1 support and N2

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_FIRST_MOMENT
PARENT_ROUTE=Stage27-20-r302a
SOURCE_STAGE=Stage20

## 1. Wall support

Let `Q_wall,eta0(B)` be the occupied `q1` values whose r301t Stage14 image lies in a nonproportional retained packet with `|theta-1/4|<eta0`.  The exact Möbius adapter is injective, and restricting the frozen Stage14 packet decomposition introduces only its audited `B^o(1)` dyadic/decorative multiplicity.

Every occupied wall `q1` has at least one legal physical completion tuple in the corresponding Stage14 MAIN receiver.  Therefore, without multiplying any independent local saving,

\[
|Q_{\rm wall,\eta_0}(B)|
\le B^{o(1)}
\sum_{P\in W_{\eta_0}^{\rm cell}(B)}F_{\rm MAIN}(P;B).
\]

Consequently the hypothetical r302a estimate `(R302-WFM)` implies

\[
\boxed{|Q_{\rm wall,\eta_0}(B)|\ll B^{1/2-\delta+o(1)}}.
\]

This implication is monotone: the MAIN receiver may count a larger legal candidate set than the occupied support, while all later physical masks only delete candidates.

## 2. Gluing to the audited off-wall theorem

R301u gives, for the same fixed `eta0`,

\[
|Q_{\rm off,\eta_0}(B)|
\ll B^{1/2-\min(2\eta_0,1/16)+o(1)}.
\]

Its proportional branch is already capped by `B^(7/16+o(1))`.  Thus `(R302-WFM)` would imply for the full occupied support

\[
|Q(B)|\ll B^{1/2-\Delta+o(1)},
\qquad
\Delta=\min(\delta,2\eta_0,1/16)>0.
\]

R301s then gives

\[
N_2(B)\le |Q(B)|B^{o(1)},
\]

so the same hypothetical theorem would yield

\[
\boxed{N_2(B)\ll B^{1/2-\Delta+o(1)}}.
\]

## 3. Scope firewall

R302b proves only this transfer implication.  It does not prove `(R302-WFM)`, does not assign a positive numerical `delta`, and does not promote checkpoint40 to checkpoint50.  The fixed local-root ledger, q0 collision identity, and exponent-neutral q0/j projections from r301w-y are not reused as new savings.

```text
STAGE27_20_R302B_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
HOST_TO_Q1_WALL_SUPPORT_MONOTONE_TRANSFER_PROVED=true
Q1_WALL_TO_GLOBAL_GLUE_FORMULA_PROVED=true
GLOBAL_DEFICIT_IF_R302_WFM=Delta=min(delta,2eta0,1/16)
R301S_SUPPORT_TO_N2_TRANSFER_REUSED=true
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302c
```
