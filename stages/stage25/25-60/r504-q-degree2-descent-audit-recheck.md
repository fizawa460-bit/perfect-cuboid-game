# Stage25-60 R504 complete Q-degree-2 source descent hostile re-audit

Status: **PASS FOR DESCENT REPAIR; CHECKPOINT60 CONTINUES**

The previous hostile FAIL remains authoritative history for the overbroad claim that `(a u^2+b)/(u^2+1)` was a complete Q-rational degree-two normal form.

The repair is audited under the exact R504 equivalence: target coordinate fixed, source reparametrization only by `PGL_2(Q)`.

For any degree-two `phi in Q(u)`, `[Q(u):Q(phi)]=2`; characteristic zero gives a separable quadratic, hence Galois, extension. Its unique nontrivial deck automorphism fixes Q and lies in `Aut_Q Q(u)=PGL_2(Q)`.

A trace-zero representative `M=[[p,q],[r,-p]]` satisfies `M^2=(p^2+qr)I`; invertibility gives `p^2+qr != 0`. Its squareclass determines the fixed-point type.

- Split: Q-conjugate to `u -> -u`, fixed field `Q(u^2)`, hence normal-form species `(A*u^2+B)/(C*u^2+D)`.
- Nonsplit squareclass `d`: Q-conjugate to `u -> d/u`, fixed field `Q(u+d/u)`, hence normal-form species `(A*(u^2+d)+B*u)/(C*(u^2+d)+D*u)`.

Because `Q(phi)` equals the corresponding fixed field, `phi` is a Möbius transform of the displayed invariant generator. This proves completeness of the split/nonsplit source-equivalence species. The audit does not assert uniqueness of the coefficient tuple after residual source-centralizer actions.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_Q_DEGREE2_SOURCE_EQUIVALENCE=TARGET_FIXED_SOURCE_PGL2_Q
R504_Q_DEGREE2_DECK_INVOLUTION_DEFINED_OVER_Q=true
R504_Q_DEGREE2_INVOLUTION_CLASSES=SPLIT_OR_NONSPLIT_SQUARECLASS
R504_Q_DEGREE2_COMPLETE_DESCENT_ACCEPTED=true
R504_PREVIOUS_EVEN_NORMAL_FORM_COMPLETE_CLAIM=false
R504_PREVIOUS_EVEN_NORMAL_FORM_SCOPE=STRICT_SPLIT_SUBFAMILY
R504_FULL_SPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_NONSPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_FULL_Q_RATIONAL_EXTRA_INVOLUTION_LOCUS_CLOSED=false
R504_PRYM_AS_SOLE_DEGREE2_RESIDUAL_ACCEPTED=false
R504_EXTERNAL_THEOREM_GATE_ACCEPTED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #992; then Stage25-main-batch at checkpoint60
```
