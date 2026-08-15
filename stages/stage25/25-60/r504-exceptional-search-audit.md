# Stage25-60 R504 exceptional degree-two search hostile audit

Status: **PREVIOUS FAIL PRESERVED; REPAIR SUBMITTED FOR FRESH AUDIT**

The previous FAIL is retained as historical provenance: the family `(a u^2+b)/(u^2+1)` was incorrectly promoted to a complete Q-degree-two normal form.

The repair does not defend that claim. Instead it proves the exact source-equivalence descent needed by R504.

## Repair theorem

For a degree-two base-change map `phi:P1_u -> P1_k` over Q, with target coordinate fixed and only source `PGL2(Q)` changes allowed:

1. `Q(u)/Q(phi)` is separable quadratic and hence has a unique Q-rational deck involution;
2. every involution in `PGL2(Q)` is Q-conjugate either to the split form `u -> -u` or to a nonsplit form `u -> d/u`, with `d` defined modulo Q-squares;
3. the fixed fields are respectively `Q(u^2)` and `Q(u+d/u)`;
4. hence every degree-two base change is source-equivalent to exactly one of the normal-form species
   - split: `(A*u^2+B)/(C*u^2+D)`;
   - nonsplit: `(A*(u^2+d)+B*u)/(C*(u^2+d)+D*u)`.

The earlier even family is explicitly downgraded to a strict split subfamily. Its symbolic invariant calculations remain valid only in that subfamily.

## Current audit request

Fresh audit should check the complete split/nonsplit descent theorem, not re-audit the already accepted even-subfamily invariant algebra.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
REPAIR_SUBMITTED=true
R504_Q_DEGREE2_COMPLETE_DESCENT_PROVED=true
R504_PREVIOUS_EVEN_NORMAL_FORM_COMPLETE_CLAIM=false
R504_FULL_SPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_NONSPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_PRYM_AS_SOLE_DEGREE2_RESIDUAL_ACCEPTED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
```
