# Stage27-20-r302d — exact outer-U disintegration of the MAIN wall physical host

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_WEIGHTED_ADAPTER
PARENT_ROUTE=Stage27-20-r302c
SOURCE_STAGE=Stage20

## 1. Refine the audited wall host, do not recount it

Fix the same constant `eta0>0` and retained nonproportional wall cells `P` from r302a-c. On the frozen Stage14 MAIN receiver the primitive rectangle variables include

\[
U=L_x^+,\qquad V=L_x^-,\qquad (U,V)=1.
\]

For a wall cell `P`, define

\[
H_{\rm phys}^{\rm MAIN}(P,U;B)
\]

to be the number of tuples in the already-charged complete Stage14 physical host lying in `P` and having outer coordinate `U`. Define `F_MAIN(P,U;B)` by additionally imposing the frozen nested-divisor and simultaneous two-root MAIN system.

This is only a disintegration of the existing host. Hence exactly

\[
H_{\rm phys}(P;B)=\sum_U H_{\rm phys}^{\rm MAIN}(P,U;B),
\]

and

\[
F_{\rm MAIN}(P;B)=\sum_U F_{\rm MAIN}(P,U;B),
\qquad
0\le F_{\rm MAIN}(P,U;B)\le H_{\rm phys}^{\rm MAIN}(P,U;B).
\]

No factor involving the number of `U` values is multiplied into the ledger. This agrees with audited Stage27-40ae: primitive `(U,V)` support is already charged in the Stage14 complete host.

## 2. Same-measure weighted exceptional-fiber theorem

Let `E` be any exceptional subset of the refined wall fibers `(P,U)`. A direct legal bad-mass theorem is

\[
\boxed{
\sum_{(P,U)\in E}H_{\rm phys}^{\rm MAIN}(P,U;B)
\le B^{-\delta_B+o(1)}
\sum_{P,U}H_{\rm phys}^{\rm MAIN}(P,U;B)
}
\tag{R302-UW}
\]

for some fixed `delta_B>0`, uniformly with the frozen physical masks and wall width.

The complete Stage14 host already gives, on this subfamily,

\[
\sum_{P,U}H_{\rm phys}^{\rm MAIN}(P,U;B)
\ll B^{1/2+o(1)}.
\]

Therefore `(R302-UW)` immediately yields

\[
\sum_{(P,U)\in E}H_{\rm phys}^{\rm MAIN}(P,U;B)
\ll B^{1/2-\delta_B+o(1)}.
\]

This is exactly the absolute bad-cell/fiber mass deficit demanded by audited r302c, now written in an outer-U measure that can genuinely have polynomially many labels without double charging them.

## 3. Good fibers plus bad physical mass

If the complementary good fibers satisfy

\[
\sum_{(P,U)\notin E}F_{\rm MAIN}(P,U;B)
\ll B^{1/2-\delta_G+o(1)}
\]

for fixed `delta_G>0`, then by `F_MAIN<=H_phys` on the exceptional fibers,

\[
\sum_{P,U}F_{\rm MAIN}(P,U;B)
\ll B^{1/2-\min(\delta_G,\delta_B)+o(1)}.
\]

R302b then gives the hypothetical global deficit

\[
\Delta=\min(\delta_G,\delta_B,2\eta_0,1/16)>0.
\]

R302d proves this adapter and relative-to-absolute conversion only. It does not prove `(R302-UW)` or the good-fiber first-moment estimate.

```text
STAGE27_20_R302D_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
MAIN_WALL_HOST_OUTER_U_DISINTEGRATION_DERIVED=true
OUTER_U_LABEL_CARDINALITY_RECHARGED=false
MAIN_FIBER_MONOTONE_DOMINATION=F_MAIN<=H_phys_MAIN
R302_UW_RELATIVE_TO_ABSOLUTE_TRANSFER_PROVED=true
MAIN_OUTER_U_PHYSICAL_WEIGHTED_EXCEPTIONAL_MASS_DEFICIT_PROVED=false
GOOD_FIBER_FIRST_MOMENT_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302e
```
