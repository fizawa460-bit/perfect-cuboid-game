# Stage28-40-r2 audit repair

```text
REPAIR_FOR_AUDIT_HEAD=c59a9e7028b70599eba3cdacad193940e06e58fa
AUDIT_VERDICT_ON_OLD_HEAD=FAIL_REPAIR_REQUIRED
REPAIR_SCOPE=LOCAL_ALGEBRAIC_FACTORISATION_WRITEUP
REPAIR_STATUS=COMPLETED_PENDING_FRESH_REAUDIT
MATHEMATICAL_CLAIM_CHANGE=NONE
```

The hostile audit correctly found that the old U10 submission displayed the Stage19 space-branch expression as a sum of two conjugate-pair products.  That displayed identity was false.

The repaired `branch-component-decomposition.md` now uses the exact four-factor product

\[
F_{\rm sp}/4=
(u_1u_2-iv_1v_2)(u_1u_2+iv_1v_2)
(u_1v_2-iu_2v_1)(u_1v_2+iu_2v_1).
\]

Multiplying and expanding gives exactly

\[
4u_1^2v_1^2u_2^2v_2^2
+(u_1^2-v_1^2)^2u_2^2v_2^2
+(u_2^2-v_2^2)^2u_1^2v_1^2,
\]

which is the previously defined `F_sp/4`.  An independent symbolic expansion check also gives zero difference.

## Downstream reread

- U10: the four geometric `(1,1)` factors and `4 x genus-0` branch profile now follow from the corrected product.
- U13: unchanged.  Its squareclass-separation argument only requires the corrected odd branch supports, so the distinct quadratic-extension conclusion remains the same.
- `result.md`: unchanged mathematically; its branch-profile summary is supported by the repaired U10 proof.
- `28-controller.json`: the last recorded audit verdict remains historical `FAIL_REPAIR_REQUIRED` until a fresh audit is performed.  This repair file is the current-head handoff and does not self-award PASS.

```text
U10_FACTORISATION_REPAIRED=true
U10_EXACT_EXPANSION_CHECK=PASS
U13_REREAD=PASS_NO_CLAIM_CHANGE
RESULT_REREAD=PASS_NO_CLAIM_CHANGE
SELF_AWARDED_AUDIT_PASS=false
MERGE_ALLOWED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_EXPECTED_COMMAND=Stage28-audit
```
