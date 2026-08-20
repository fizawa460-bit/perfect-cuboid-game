# Stage27-50 — operator-override handoff from Checkpoint 40

```text
TASK_ID=Stage27-50
PROGRAM=Stage27-TRUE-N2-EXPONENT-ATTACK
ROUTE_KIND=MAINLINE_CHECKPOINT_REENTRY
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
OPERATOR_OVERRIDE=true
```

Checkpoint 40 had remained blocked by an active Stage27-19 reentry route. That blocker has now been explicitly withdrawn by operator direction after the Stage27-19 upper/lower exploration was pushed through r10 without changing the certified exponents.

The mathematical state is carried forward unchanged:

```text
STAGE27_CURRENT_N2_LOWER=1/4
STAGE27_CURRENT_N2_UPPER=1/2_PLUS_EPSILON
STAGE27_STRICT_SUB_SQRT_UPPER_PROVED=false
STAGE27_LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
STAGE27_TRUE_N2_EXPONENT_IDENTIFIED=false
```

This handoff does **not** claim that the checkpoint-40 progress gates were discharged. Instead it records an operator decision to stop treating the open Stage27-19 theorem/construction gates as blockers for the broader Stage27 mainline.

The prior unresolved gates remain archived/open for future reentry only upon genuinely new input:

- upper: a same-measure coupled-support/incidence theorem, a compatible separated correlation theorem, or another independent fixed-power support mechanism;
- lower: a moving square-lift section/multisection, a low-height cross-cancellation family with `2d_x+2d_y-g<=7`, or another construction with `rho/h>1/4`.

Checkpoint-50 work may therefore proceed using the unchanged bracket

\[
B^{1/4-o(1)} \lesssim N_2(B) \lesssim B^{1/2+o(1)},
\]

with the explicit understanding that the bracket is inherited, not improved.

The first Checkpoint-50 task is synthesis rather than another Stage19 attack: identify what conclusions, comparisons, or downstream Stage27 contracts remain valid under this inherited bracket, and isolate which statements require the true exponent versus only the certified interval.

```text
CHECKPOINT40_ACTIVE_REENTRY_BLOCKER_WITHDRAWN_BY_OPERATOR=true
CHECKPOINT40_PROGRESS_GATES_DISCHARGED=false
CHECKPOINT50_ENTRY_ALLOWED_BY_OPERATOR_OVERRIDE=true
INHERITED_LOWER_EXPONENT=1/4
INHERITED_UPPER_EXPONENT=1/2_PLUS_EPSILON
TRUE_EXPONENT_STILL_OPEN=true
STAGE19_REENTRY_STATUS=FROZEN_UNTIL_GENUINELY_NEW_INPUT
NEXT_DERIVED_ROUTE=27-50a
ADVANCE_TO_CHECKPOINT60=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage27-50-audit
```
