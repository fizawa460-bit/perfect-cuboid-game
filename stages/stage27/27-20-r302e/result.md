# Stage27-20-r302e — 40ae has the right weighted shape but not yet a T-to-MAIN measure adapter

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_WEIGHTED_ADAPTER
PARENT_ROUTE=Stage27-20-r302d
SOURCE_STAGE=Stage20

## 1. What audited 40ae actually supplies

Audited Stage27-40ae separates already-charged outer-`U` cardinality from a potentially new distribution theorem. In its T-route notation it defines actual incidence counts `T_U`, a principal baseline `M_U`, and accepts as a legal reopen contract a fixed-power weighted exceptional-baseline estimate or an equivalently strong weighted second moment over the physical `U` fibers.

This is structurally the same kind of theorem needed in r302d. But the symbol `U` being common does not identify the measures.

R302d uses

\[
H_{\rm phys}^{\rm MAIN}(P,U;B),
\]

the complete physical host dominating the MAIN nested-divisor/two-root receiver. Stage27-40ae uses the T-route principal baseline `M_U` attached to the terminal prime-occupancy formulation. The repository does not currently prove that these weights are equal, mutually comparable, or related by a one-sided domination strong enough to transfer a fixed power.

Therefore a 40ae theorem in `M_U` cannot be inserted into r302c merely because both routes are indexed by outer `U`.

## 2. Exact legal bridge

There are two legal ways to cross this measure gap.

### Route A — direct MAIN-host theorem

Prove `(R302-UW)` directly in the weight `H_phys^MAIN(P,U;B)`. This needs no T-route comparison and is the cleanest receiver.

### Route B — common-refinement domination

Construct a common physical refinement `R` of the relevant fixed-width wall packets and the audited 40ae outer-U fibers, with nonnegative weights `H_R` and `M_R`, such that the relevant exceptional sets satisfy

\[
\sum_{R\in E}H_R
\le B^{o(1)}\sum_{R\in E}M_R,
\]

while

\[
\sum_R M_R\ll B^{1/2+o(1)}.
\]

Then a fixed-power 40ae-type weighted exceptional estimate

\[
\sum_{R\in E}M_R
\le B^{-\delta+o(1)}\sum_R M_R
\]

would imply the r302d bad-host bound. A stronger pointwise Radon--Nikodym-type comparison is sufficient but not required; an aggregate comparison on every exceptional set produced by the theorem is enough.

No such common-refinement domination theorem is presently proved.

## 3. What cannot be used as a bridge

The following are insufficient by themselves:

- polynomial cardinality of outer `U`;
- ordinary unweighted BV/BDH class counts;
- a fixed-`U` class average from the subpolynomial class universe closed by 40ad;
- common use of the labels `U,V` in MAIN and T;
- Cauchy or random-class factors that recharge the already-counted primitive `(U,V)` support.

Thus 40ae is imported as a **theorem shape / weighting principle**, not as an already-applicable theorem for the MAIN wall host.

```text
STAGE27_20_R302E_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
STAGE27_40AE_IMPORTED_AS_WEIGHTED_THEOREM_SHAPE=true
STAGE27_40AE_T_BASELINE_EQUALS_MAIN_HOST_CLAIMED=false
T_TO_MAIN_COMMON_REFINEMENT_DOMINATION_REQUIRED=true
T_TO_MAIN_COMMON_REFINEMENT_DOMINATION_PROVED=false
DIRECT_MAIN_HOST_WEIGHTED_THEOREM_REMAINS_LEGAL=true
OUTER_U_CARDINALITY_RECHARGED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302f
```
