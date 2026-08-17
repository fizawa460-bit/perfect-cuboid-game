# Stage27-20-r302a — specialize the frozen Stage14 MAIN first-moment gate to the fixed-width wall slab

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_FIRST_MOMENT
PARENT_ROUTE=Stage27-20-r301z
SOURCE_STAGE=Stage20

## 1. Fixed-width wall family

Fix a constant `eta0>0`.  Let `W_eta0(B)` denote the nonproportional occupied Stage14 packets reached from the Stage20/27 occupied `q1` support through the audited r301t Möbius adapter, with

\[
|\theta-1/4|<\eta_0,
\]

and with all frozen Stage14 physical masks, canonical orientation, primitive conditions, dyadic/decorative states, and the cutoff `d<=B` retained.

R301z proves that a fixed-power bound

\[
|W_{\eta_0}(B)|\ll B^{1/2-\delta+o(1)}
\]

for some fixed `eta0,delta>0` is sufficient, together with r301u, for a global strict sub-square-root upper bound.  It does not prove this wall estimate.

## 2. Exact frozen MAIN receiver on this family

Stage14 final freezes the MAIN route after the H normalization as a primitive-rectangle nested-divisor first moment.  In its final notation the moving data include primitive rectangle sides `U,V`, squarefree/nested divisor choices

\[
t_p,t_q\mid m^\circ,\qquad N=t_pt_q,\qquad f\mid N,
\]

and the two simultaneous quadratic root constraints

\[
\boxed{G_-f^2\equiv-G_+N\pmod{2U}},
\qquad
\boxed{G_-f^2\equiv G_+N\pmod{2V}}.
\]

All coprimality, k-free/nested-divisor, sign, parity, chamber, endpoint, and physical masks from the frozen MAIN receiver remain filters.  No root-line or local-prime factor from the already charged Stage14 host ledger is multiplied in again.

For a retained wall packet `P`, write `F_MAIN(P;B)` for the number of legal physical MAIN receiver tuples in `P` satisfying the displayed nested-divisor and simultaneous-root system after the variables already accounted for by the frozen complete-host construction are kept in their original quantifier order.

The wall-slab specialization of the old external gate is therefore the aggregate theorem

\[
\boxed{
\sum_{P\in W_{\eta_0}^{\rm cell}(B)}F_{\rm MAIN}(P;B)
\ll B^{1/2-\delta+o(1)}
}
\tag{R302-WFM}
\]

for some fixed `eta0,delta>0`, where `W_eta0^cell` is the audited subpolynomial dyadic/decorative partition of the physical wall family.  A uniform bound of this strength on every retained dyadic/decorative wall cell is a sufficient stronger form because the number of such cells is `B^o(1)`.

## 3. What is new and what is not

This is a target specialization, not a proof of the analytic theorem.  The imported Stage14 external theorem class is

`UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment`.

The Stage14 hostile applicability audit ended at

`COMPLETE_UNRESOLVED_EXTERNAL_FIRST_MOMENT_GATE`

with `OFF_THE_SHELF_THEOREM_APPLICABLE=false`: available nearby divisor/AP results do not simultaneously preserve two nested divisors of a moving product, the two quadratic root conditions modulo the primitive rectangle sides, every retained cell, and the physical masks.

R302a sharpens the restart target by restricting that exact receiver to the only fixed-width region that can still obstruct the current half-power theorem.  It does not remove any of the analytic uniformity requirements.

```text
STAGE27_20_R302A_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
WALL_SLAB_MAIN_FIRST_MOMENT_SPECIALIZATION_DERIVED=true
WALL_SLAB_FIXED_ETA0=true
MAIN_NESTED_DIVISOR_SYSTEM_RETAINED=true
MAIN_TWO_SIMULTANEOUS_ROOT_CONGRUENCES_RETAINED=true
MAIN_PHYSICAL_MASKS_RETAINED=true
STAGE14_LOCAL_ROOT_LEDGER_RECHARGED=false
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
OFF_THE_SHELF_FIRST_MOMENT_APPLICABLE=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r302b
```
