# Stage27-19-r401d — hostile audit

```text
AUDIT_VERDICT=FAIL
MATHEMATICAL_AUDIT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R401D_STATUS=MATHEMATICS_PASS_LIFECYCLE_SYNC_REQUIRED
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
```

## Scope

Hostile intermediate audit of PR #1036 / Stage27-19-r401d. This audit does not close Stage27 checkpoint40 and does not advance to checkpoint50.

## 1. R501/R502 calibration

Accepted mathematically.

- R501 embeds exactly in the master receiver with the displayed `x1,y1,z1`, and the split-coordinate formulas for `tau1,u1` check identically.
- R502 embeds exactly with the displayed `x2,y2,z2`, and the split-coordinate formulas for `tau2,u2` check identically.
- In both cases the reduced rational map to the `tau`-line has degree 8.

```text
R501_TAU_EMBEDDING_ACCEPTED=true
R502_TAU_EMBEDDING_ACCEPTED=true
R501_TAU_PROJECTION_DEGREE=8
R502_TAU_PROJECTION_DEGREE=8
```

## 2. Toric height ledger

Accepted as an algebraic preflight, with the stated arithmetic firewall retained.

For homogeneous toric pairs of degrees `d_x,d_y`, the raw three-edge degree is `2*d_x+2*d_y`. If a common homogeneous polynomial factor of degree `g` divides all three raw edges, removing it gives

```text
h_alg=2*d_x+2*d_y-g.
```

This is not by itself a lower theorem: residual arithmetic gcd, parameter multiplicity, canonicalization, positivity and exactly-two control still have to be supplied.

For R501, `(d_x,d_y,g,h)=(2,2,0,8)` and `(E0,X0,Y0)=2*(C1,A1,B1)` checks exactly.

For R502, `(d_x,d_y,g,h)=(4,2,4,8)`. The factor

```text
G2=4*m*n*(m^2+3*n^2)
```

is a genuine homogeneous common polynomial factor of degree 4, and

```text
(E0,X0,Y0)=G2*(C2,A2,B2)
```

checks exactly. Thus the nominal degree 12 composition reduces structurally to degree 8 before the previously-audited residual arithmetic gcd bound is applied.

```text
UNIVERSAL_TORIC_HEIGHT_LEDGER_ACCEPTED=true
R501_TORIC_DEGREE_LEDGER=dx2_dy2_g0_h8
R502_TORIC_DEGREE_LEDGER=dx4_dy2_g4_h8
R502_DEGREE12_TO_8_POLYNOMIAL_CANCELLATION_ACCEPTED=true
```

## 3. Lower progress / stopping rule

Accepted only as a bounded routing rule, not as an impossibility theorem.

For a one-rational-parameter family with quadratically many reduced source parameters of height `T`, no fixed-power loss in the physical adapters, and algebraic physical height `T^h`, the criterion `h<8` is a sufficient route to beat the current quarter-power exponent. A polynomially thicker family or an additional proved cancellation remains an independent reopen condition.

```text
ONE_PARAMETER_ALGEBRAIC_PROGRESS_GATE_ACCEPTED=2dx+2dy-g<8
LOWER_BOUNDED_REENTRY_STOP_CANDIDATE_ACCEPTED=true
LOWER_IMPOSSIBILITY_THEOREM_PROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PREFERRED_POST_AUDIT_LANE=UPPER_REENTRY
PROPOSED_NEXT_UPPER_ROUTE=27-40af
```

## 4. Blocking lifecycle defect

The PR does not synchronize the canonical Stage27 controller or `docs/00_CURRENT_RESEARCH_STATUS.md`.

At the audited branch head, both still report `Stage27-19-r401c` as `SUBMITTED_PENDING_FRESH_AUDIT`, even though PR #1035 has already passed hostile audit and merged, and the present submission is r401d. The dedicated r401d verifier also does not check this lifecycle state, so its SUCCESS does not cover the inconsistency.

Required repair before merge:

1. mark `Stage27-19-r401c` as audited PASS + merged with PR #1035 and merge commit `4ca03c43f4ff2c858c51ac8959d6e75f077c6de7`;
2. register `Stage27-19-r401d` in the controller and current-status document;
3. keep `CURRENT_CHECKPOINT=40`, `ADVANCE_TO_CHECKPOINT50=false`, and checkpoint50 blocked;
4. after audit repair, record r401d as intermediate PASS awaiting merge (or equivalent repository-native lifecycle state), not as a stage/checkpoint closeout;
5. extend the r401d verifier to assert the synchronized lifecycle state so the stale-controller condition cannot silently recur.

```text
CANONICAL_CONTROLLER_SYNCED=false
CURRENT_RESEARCH_STATUS_SYNCED=false
R401D_LIFECYCLE_VERIFIER_COMPLETE=false
FAIL_REASON=STALE_R401C_PENDING_STATE_AND_MISSING_R401D_CANONICAL_REGISTRATION
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=repair lifecycle sync; then Stage27-19-r401-audit
```

Dedicated `Stage27-19-r401d R501 R502 calibration` CI on submission head `9889600487c9157e899e5a44369c10e34182fb32` is SUCCESS. Relevant Stage27 regressions are also green. The audit FAIL is therefore repository lifecycle/integration only, not a mathematical rejection.
