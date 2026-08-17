# Stage27-20-r301v — exact critical-support wall and remaining receiver

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301u
SOURCE_STAGE=Stage20

On the Stage14 feasible domain set `theta=1/4`. Then
\[
\frac18\le\phi\le\frac14,\qquad
\chi=2\theta+2\phi-\frac34=2\phi-\frac14\in[0,1/4].
\]
For nonproportional cells, both complete-host exponents saturate:
\[
\boxed{E_k=3\theta-1/4=1/2},\qquad
\boxed{E_{\rm RRF}=1-2\theta=1/2}.
\]
The proportional branch stays below the wall (`<=7/16`). Thus the surviving fixed-power obstruction is precisely the nonproportional segment
\[
\boxed{\theta=1/4,\quad 1/8\le\phi\le1/4,\quad \chi=2\phi-1/4}.
\]

R301s gives `N2(B) <= |Q(B)| B^o(1)` and r301u gives fixed-power savings at every fixed distance from the wall. A sufficient new receiver is therefore a target-specific critical support theorem
\[
\boxed{|Q_{\rm crit}(B)|\ll B^{1/2-\delta+o(1)}}
\]
for some fixed `delta>0`, with a compatible wall-neighborhood statement. The existing fixed-x elliptic `B^o(1)`, fixed-x squareclass `B^o(1)`, height-only support, and off-wall Stage14 hosts do not supply this deficit.

Legal next weapons are critical-wall-specific: weighted local obstruction, occupied-slope collision/energy deficit, or a thin-projection theorem on the exact critical receiver.

```text
STAGE27_20_R301V_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CRITICAL_SUPPORT_SEGMENT_IDENTIFIED=true
CRITICAL_THETA=1/4
CRITICAL_PHI_RANGE=[1/8,1/4]
CRITICAL_CHI_FORMULA=2phi-1/4
CRITICAL_E_K=1/2
CRITICAL_E_RRF=1/2
FIXED_X_FIBER_EXPONENT_ALREADY_ZERO=true
CRITICAL_Q1_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301w
```
