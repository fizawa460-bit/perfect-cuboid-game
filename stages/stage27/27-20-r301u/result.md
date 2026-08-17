# Stage27-20-r301u — fixed-distance off-wall occupied support is strictly sub-half

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301t
SOURCE_STAGE=Stage20

Stage14 Proposition 3.6 gives the complete case split
\[
E\le \frac{7}{16}\qquad\text{(proportional)},
\]
\[
E_k\le 3\theta-\frac14\qquad\text{(nonproportional, }\theta\le1/4\text{)},
\]
\[
E_{\rm RRF}\le1-2\theta\qquad\text{(nonproportional, }\theta\ge1/4\text{)}.
\]
By r301t, occupied first-coordinate support is a subset of this same active-face measure; no independent saving is multiplied into another ledger.

Fix a constant `eta>0`. On the nonproportional branch, if `theta<=1/4-eta`, then
\[
E_k\le\frac12-3\eta,
\]
and if `theta>=1/4+eta`, then
\[
E_{\rm RRF}\le\frac12-2\eta.
\]
Thus the nonproportional off-wall contribution is at most
\[
B^{1/2-2\eta+o(1)}.
\]
The proportional contribution remains bounded by
\[
B^{7/16+o(1)}.
\]
Therefore, after the audited `B^o(1)` packet multiplicity, the full off-wall occupied support satisfies
\[
\boxed{|Q_{\rm off,eta}(B)|\ll B^{\max(1/2-2\eta,\,7/16)+o(1)}}
\]
or equivalently
\[
\boxed{|Q_{\rm off,eta}(B)|\ll B^{1/2-\min(2\eta,1/16)+o(1)}}.
\]
The same exponent bound holds for the corresponding occupied `j` support because r301m proves bounded physical multiplicity of the `q1 -> j` map.

For every fixed `eta>0` this is a genuine fixed-power saving below `1/2`, but it is capped by the proportional `7/16` branch once `eta>1/32`. This is not a global strict sub-square-root theorem: it excludes only cells a fixed distance from `theta=1/4`; a shrinking wall neighborhood remains.

```text
STAGE27_20_R301U_STATUS=AUDITED_PASS_MERGED
OFF_WALL_FIXED_DISTANCE_SUPPORT_SAVING_PROVED=true
OFF_WALL_NONPROPORTIONAL_BOUND=B^(1/2-2eta+o(1))
OFF_WALL_PROPORTIONAL_BOUND=B^(7/16+o(1))
OFF_WALL_Q1_BOUND=B^(1/2-min(2eta,1/16)+o(1))
OFF_WALL_J_BOUND=B^(1/2-min(2eta,1/16)+o(1))
CRITICAL_THETA=1/4
GLOBAL_Q1_SUPPORT_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301v
```
