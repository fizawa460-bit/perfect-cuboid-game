# Stage29-09 — fresh audit contract

Audit `29-09_FULL_ENDPOINT_LOCAL_ARITHMETIC` adversarially. Do not accept the formulas merely because the finite regression passes.

Required checks:

1. Re-derive the seven-line branch incidence over every odd characteristic and verify that no extra intersection type appears at `p=3`.
2. Re-derive `A1,A2,A3`, especially the pair-sum-line elliptic trace term `E:y^2=x^3-x` and all boundary corrections.
3. Verify the normal-cover fiber multiplicities `64,32,16,8` and the substitution into the audited Stage29-02e Frobenius formula for `A0`.
4. Re-derive `q1` and `q2` from normalized `Q_p` Haar measure.
5. Re-derive the triple-point recurrence and the exact formula
   `q3=(p^2-(3+chi(-1))p+1)/(8(p+1)^2(p^2+1))`; explicitly check that unit multipliers at all eligible triple points do not alter the squareclass condition.
6. Verify that the projective reduction cylinders have equal mass `1/(p^2+p+1)` and hence that `Delta_p` is the exact odd-prime `P^2(Q_p)` density.
7. Verify the `p=2` firewall. The Euler-brick witness may prove local nonemptiness only; it must not be promoted to an exact 2-adic density or a rational perfect cuboid.
8. Verify the real positive-chamber statement.
9. Compare against Stage19 and Stage20 local laws on their actual matched hosts. Reject any multiplication or re-crediting across unmatched measures.
10. Decide whether `R29-KUM-LOC1` and `R29-KUM-LOC2` should remain umbrella partial discharges or may be marked discharged with separate bad-prime children. Do not hide the 2-adic remainder.
11. Check that `R29-KUM-LOC3` correctly names the missing physical-height/primitive/canonical equidistribution adapter before any global sieve claim.
12. Confirm that this is pre-attack infrastructure with no new route count or endpoint existence/nonexistence conclusion.

Expected audit outputs:

```text
AUDIT_VERDICT=PASS|PASS_AFTER_BOUNDED_REPAIR|FAIL_REPAIR_REQUIRED
R29_KUM_LOC1_STATUS=<exact>
R29_KUM_LOC2_STATUS=<exact>
R29_KUM_LOC2_2_STATUS=<exact>
R29_KUM_LOC3_STATUS=<exact>
DOUBLE_CHARGE_FIREWALL=PASS|FAIL
ROUTE_COUNT_CHANGE=0_or_explain
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM_IF_PASS=GAP_SCAN_B_ROADMAP_REVIEW_B
```
