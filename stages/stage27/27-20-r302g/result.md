# Stage27-20-r302g — normalize the MAIN wall host by physical occupancy ratio

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302f
SOURCE_STAGE=Stage20

Fix the same constant wall width `eta0>0` and the audited r302d outer-U refinement. Write the fiber index as `x=(P,U)` and set

\[
H_x=H_{\rm phys}^{\rm MAIN}(P,U;B),\qquad F_x=F_{\rm MAIN}(P,U;B),
\]

so `0<=F_x<=H_x`. For `H_x>0` define the physical occupancy ratio

\[
\rho_x=F_x/H_x\in[0,1],
\]

and put `rho_x=0` when `H_x=0`. Let

\[
H=\sum_x H_x,\qquad F=\sum_xF_x=\sum_xH_x\rho_x.
\]

The frozen Stage14 complete-host ceiling gives

\[
H\ll B^{1/2+o(1)}.
\]

Therefore any fixed-power relative occupancy deficit

\[
\frac{1}{H}\sum_xH_x\rho_x\le B^{-\delta_\rho+o(1)}
\tag{R302-OCC1}
\]

implies

\[
F\ll B^{1/2-\delta_\rho+o(1)}.
\]

There is also an independent legal escape: if the complete wall host itself satisfies

\[
H\ll B^{1/2-\delta_H+o(1)},
\tag{R302-HOST}
\]

then the wall deficit follows even without relative occupancy decay. Thus r302 must prove either a host-mass deficit or a same-measure occupancy deficit; it must not infer one from raw outer-U cardinality.

This normalization is exact and uses no new counting factor.

```text
STAGE27_20_R302G_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
MAIN_OUTER_U_OCCUPANCY_RATIO_DEFINED=true
MAIN_OCCUPANCY_WEIGHT_IS_PHYSICAL_HOST=true
MAIN_OCCUPANCY_L1_DEFICIT_IMPLIES_WALL_DEFICIT=true
COMPLETE_WALL_HOST_DEFICIT_IS_ALTERNATIVE_SUCCESS=true
OUTER_U_CARDINALITY_RECHARGED=false
MAIN_OCCUPANCY_FIXED_POWER_DEFICIT_PROVED=false
COMPLETE_WALL_HOST_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302h
```
