# Stage25-60 R504 Prym external theorem gate

STATUS=SUSPENDED_PENDING_COMPLETE_Q_DEGREE2_STRATA
ROUTE=R504
CHECKPOINT=60

The earlier attempt to promote the residual directly to a Prym/Humbert external theorem gate was premature because the submitted even family was not a complete Q-degree-two source normal form.

A complete source-descent is now separately proved in `r504-q-degree2-complete-descent.md`: every degree-two base change over Q has a Q-rational deck involution and, after source `PGL2(Q)`, lies in either the split normal form
\[
(Au^2+B)/(Cu^2+D)
\]
or the nonsplit squareclass normal form
\[
(A(u^2+d)+Bu)/(C(u^2+d)+Du).
\]

Therefore the Prym gate can only become load-bearing after the full split stratum and all nonsplit squareclass strata have been analyzed and reduced to a common Prym/isogeny problem.

```text
R504_PRYM_EXTERNAL_GATE_STATUS=SUSPENDED
R504_PRYM_GATE_PREVIOUS_SOLE_RESIDUAL_CLAIM=WITHDRAWN
R504_FULL_SPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_NONSPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```
