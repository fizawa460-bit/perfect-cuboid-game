# Stage27-20-r301u — fixed-distance off-wall occupied support is strictly sub-half

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301t
SOURCE_STAGE=Stage20

Stage14 Proposition 3.6 gives the complete nonproportional host bounds
\[
E_k\le 3\theta-\frac14\quad(\theta\le1/4),\qquad
E_{\rm RRF}\le1-2\theta\quad(\theta\ge1/4),
\]
and the proportional branch is `<=7/16`.
By r301t, occupied first-coordinate support is a subset of this same active-face measure; no independent saving is multiplied into another ledger.

Fix a constant `eta>0`. If `theta<=1/4-eta`, then
\[
E_k\le\frac12-3\eta.
\]
If `theta>=1/4+eta`, then
\[
E_{\rm RRF}\le\frac12-2\eta.
\]
Hence, after the `B^o(1)` packet multiplicity,
\[
\boxed{|Q_{\rm off,eta}(B)|\ll B^{1/2-2\eta+o(1)}}.
\]
The same exponent bound holds for the corresponding occupied `j` support because r301m proves bounded physical multiplicity of the `q1 -> j` map.

This is not a global strict sub-square-root theorem: it excludes only cells a fixed distance from `theta=1/4`. A shrinking wall neighborhood remains.

```text
STAGE27_20_R301U_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
OFF_WALL_FIXED_DISTANCE_SUPPORT_SAVING_PROVED=true
OFF_WALL_Q1_BOUND=B^(1/2-2eta+o(1))
OFF_WALL_J_BOUND=B^(1/2-2eta+o(1))
CRITICAL_THETA=1/4
GLOBAL_Q1_SUPPORT_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301v
```
