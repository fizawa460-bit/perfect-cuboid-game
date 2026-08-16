# Stage27-19-r401d — hostile audit history and fresh re-audit

## First hostile audit

The first audit found the mathematics acceptable but rejected the PR lifecycle state because r401c was still canonically recorded as pending and r401d was not registered.

```text
FIRST_AUDIT_VERDICT=FAIL
FIRST_MATHEMATICAL_AUDIT=PASS
FIRST_FAIL_REASON=STALE_R401C_PENDING_STATE_AND_MISSING_R401D_CANONICAL_REGISTRATION
```

The accepted mathematical content from that audit remains unchanged:

- exact R501 and R502 embeddings in the natural `(tau,u)` fibration;
- reduced `tau`-projection degree 8 for both families;
- universal toric height preflight `h_alg=2*d_x+2*d_y-g`, with the residual arithmetic/physical firewall retained;
- R501 ledger `(d_x,d_y,g,h)=(2,2,0,8)`;
- R502 ledger `(d_x,d_y,g,h)=(4,2,4,8)` with exact common factor `4*m*n*(m^2+3*n^2)`;
- `h_alg<8` accepted only as a sufficient one-parameter progress gate;
- no lower exponent above `1/4`, no true `N2` exponent, and no impossibility theorem proved.

## Fresh hostile re-audit after lifecycle repair

The lifecycle repair is accepted.

1. `Stage27-19-r401c` is now canonically `INTERMEDIATE_AUDITED_PASS_MERGED`, PR #1035, merge commit `4ca03c43f4ff2c858c51ac8959d6e75f077c6de7`.
2. `Stage27-19-r401d` is registered as `REPAIR_SUBMITTED_PENDING_FRESH_AUDIT` before this re-audit.
3. `docs/00_CURRENT_RESEARCH_STATUS.md` names r401d as the current repair submission and no longer leaves r401c pending.
4. `CURRENT_CHECKPOINT=40` is retained and checkpoint50 remains blocked.
5. The dedicated r401d verifier now asserts the canonical controller/status/audit lifecycle and the exact historical fail reason.
6. The dedicated `Stage27-19-r401d R501 R502 calibration` workflow is SUCCESS on repair head `56f4af1a42796f85538961deec04ca1e70aa6fc6`.

The older r401a/r401b/r401c regression failures on that repair head are successor-lifecycle-only failures in historical verifiers: they assert earlier current-stage / r401c-pending snapshots. Their logs do not reject the r401d mathematics or repaired canonical state. They are recorded as verifier debt and are not used to reopen the already-audited parent mathematics.

The lower-lane stopping boundary is accepted as a bounded repository routing decision, not as a theorem of impossibility. Lower reentry may reopen on a new effective physical-height `<8` rational curve, stronger cancellation, or a polynomially thicker family.

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R401D_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE

CANONICAL_CONTROLLER_SYNCED=true
CURRENT_RESEARCH_STATUS_SYNCED=true
R401D_LIFECYCLE_VERIFIER_COMPLETE=true
R401C_AUDITED_PASS_MERGED_SYNC_ACCEPTED=true

R501_TAU_EMBEDDING_ACCEPTED=true
R502_TAU_EMBEDDING_ACCEPTED=true
R501_TAU_PROJECTION_DEGREE=8
R502_TAU_PROJECTION_DEGREE=8
UNIVERSAL_TORIC_HEIGHT_LEDGER_ACCEPTED=true
R501_TORIC_DEGREE_LEDGER=dx2_dy2_g0_h8
R502_TORIC_DEGREE_LEDGER=dx4_dy2_g4_h8
R502_DEGREE12_TO_8_POLYNOMIAL_CANCELLATION_ACCEPTED=true
ONE_PARAMETER_ALGEBRAIC_PROGRESS_GATE_ACCEPTED=2dx+2dy-g<8
LOWER_BOUNDED_REENTRY_STOP_ACCEPTED=true
LOWER_IMPOSSIBILITY_THEOREM_PROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false

HISTORICAL_R401A_R401B_R401C_SUCCESSOR_VERIFIER_DEBT_NONBLOCKING=true
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_CHECKPOINT40_EXPLORATION=true
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
PREFERRED_POST_MERGE_LANE=UPPER_REENTRY
NEXT_UPPER_ROUTE=27-40af
MERGE_ALLOWED=true
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=merge PR #1036; then Stage27-main-batch
```
