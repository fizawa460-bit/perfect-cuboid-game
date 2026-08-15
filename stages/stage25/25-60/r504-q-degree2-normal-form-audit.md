# Stage25-60 R504 Q-degree-2 normal-form/descent audit

STATUS=HISTORICAL_FAIL_SUPERSEDED_BY_COMPLETE_SOURCE_DESCENT_PASS
ROUTE=R504
CHECKPOINT=60

## Historical question

Can every quadratic rational map over `Q` be reduced by source `PGL_2(Q)` to
\[
\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1}?
\]

No. That family is only a strict split subfamily. The earlier hostile FAIL on PR #992 was correct and remains historical provenance.

## Superseding repair

The authoritative repair is now:

- `stages/stage25/25-60/r504-q-degree2-complete-descent.md`;
- hostile re-audit PASS: `stages/stage25/25-60/r504-q-degree2-descent-audit-recheck.md`.

The exact R504 equivalence is target fixed / source `PGL_2(Q)`. Under that equivalence every degree-two base change has a Q-rational deck involution and falls into one of two source-conjugacy species:

- split: `(A*u^2+B)/(C*u^2+D)`;
- nonsplit squareclass `d`: `(A*(u^2+d)+B*u)/(C*(u^2+d)+D*u)`.

The old even-family symbolic elimination remains valid only inside its strict split subfamily.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
CURRENT_REAUDIT_VERDICT=PASS
R504_Q_DEGREE2_COMPLETE_DESCENT_ACCEPTED=true
R504_Q_DEGREE2_EVEN_NORMAL_FORM_COMPLETE=false
R504_Q_DEGREE2_EVEN_NORMAL_FORM_SCOPE=STRICT_SPLIT_SUBFAMILY
R504_FULL_SPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_NONSPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_PRYM_EXTERNAL_GATE_DEEP_STOP_ALLOWED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```
