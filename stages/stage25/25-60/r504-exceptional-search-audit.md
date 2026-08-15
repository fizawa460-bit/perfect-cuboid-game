# Stage25-60 R504 exceptional degree-two search hostile audit

Status: **FAIL — symbolic closure is valid only inside the submitted even normal-form subfamily; the claimed general Q-rational degree-two normalization is not proved**

## Accepted

- The symbolic elimination inside the family
  \[
  \phi_{a,b}(u)=\frac{a u^2+b}{u^2+1}
  \]
  is internally consistent.
- The factorization
  \[
  EB^2-AD^2=16(a-b)^3(a+b)(ab-1)(ab+1)
  \]
  is accepted for that family.
- The submitted complementary-quartic invariant closures on `a+b=0` and `ab=1` are accepted for that family.
- No new Stage19 family or global exponent change is claimed.

## Hostile blocker

The artifact calls the displayed two-parameter even family the **general degree-two search normalized modulo source PGL2 over Q**. That reduction is not established.

A general Q-rational degree-two map is a ratio of two binary quadratic forms. Over an algebraic closure one may move its critical points to `0, infinity` and obtain an even form. Over Q, however, the critical divisor need not split over Q and the relevant quadratic denominator/form need not be Q-equivalent to `u^2+1` by a source transformation in `PGL2(Q)`. Thus the submitted normal form can omit Q-rational degree-two maps whose critical points are conjugate over a quadratic extension or whose binary quadratic form lies in a different Q-equivalence class.

Therefore the statement

```text
R504_GENERAL_DEGREE2_NORMAL_FORM=phi_(a,b)(u)=(a*u^2+b)/(u^2+1)
R504_GENERAL_DEGREE2_PARAMETER_DIMENSION=2
```

is not accepted as a complete Q-rational normal form without a descent/classification proof. Consequently the claimed

```text
R504_EXTRA_INVOLUTION_DEGREE2_LOCUS=CLOSED_WITH_SYMBOLIC_CERTIFICATE
```

can only be accepted with the narrower scope

```text
R504_EXTRA_INVOLUTION_EVEN_NORMAL_FORM_SUBFAMILY=CLOSED_WITH_SYMBOLIC_CERTIFICATE
```

and the residual cannot yet be reduced uniquely to the Prym non-bielliptic locus.

## Additional consistency issue

The submission itself disagrees on residual status:

- `r504-exceptional-base-change-search.md` says `LIVE_PRYM_ISOGENY_LOCUS`;
- `r504-prym-external-theorem-gate.md`, controller, and symbolic script submit `EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT`.

That inconsistency is non-fatal by itself because all versions keep Stage70 blocked, but it confirms the route boundary is not yet stable enough for deep-stop classification.

## Required repair

Either:

1. prove a complete Q-rational normal-form theorem for degree-two maps under the exact allowed source equivalence, including nonsplit critical-point cases and Q-equivalence classes of binary quadratic forms, and then extend the symbolic involution analysis to every resulting Q-form; or
2. explicitly downgrade the current calculation to the even/split-critical subfamily and keep the omitted Q-rational degree-two forms live.

Only after that may the Prym theorem gate be audited as the sole remaining degree-two mechanism.

```text
AUDIT_VERDICT=FAIL
DISCOVERY_AUDIT_VERDICT=FAIL
HOSTILE_AUDIT=true
R504_EVEN_NORMAL_FORM_SYMBOLIC_ELIMINATION_ACCEPTED=true
R504_GENERAL_Q_DEGREE2_NORMAL_FORM_ACCEPTED=false
R504_FULL_Q_RATIONAL_EXTRA_INVOLUTION_LOCUS_CLOSED=false
R504_PRYM_AS_SOLE_DEGREE2_RESIDUAL_ACCEPTED=false
R504_EXTERNAL_THEOREM_GATE_ACCEPTED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
REPAIR_SCOPE=PROVE_COMPLETE_Q_DEGREE2_NORMAL_FORM_OR_DOWNGRADE_TO_EVEN_SUBFAMILY_AND_KEEP_NONSPLIT_Q_FORMS_LIVE
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
NEXT_EXPECTED_COMMAND=Stage25-main-batch
```
