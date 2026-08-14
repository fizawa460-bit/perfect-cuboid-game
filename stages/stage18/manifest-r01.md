# Stage18 R01 manifest

```text
BUNDLE_ID=STAGE18-FINAL-SELF-CONTAINED-20260814-R01
STATUS=CANDIDATE_PENDING_FRESH_STAGE18_AUDIT
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
STAGE=Stage18
PR=922
```

## Canonical Stage18 artifacts

```text
CONTROLLER=stages/stage18/18-controller.json
CHECKPOINT10=stages/stage18/18-10/result.md
CHECKPOINT20=stages/stage18/18-20/result.md
COUNTS=stages/stage18/18-20/counts.csv
ENUMERATOR=stages/stage18/18-20/enumerate.py
CHECKPOINT30=stages/stage18/18-30/result.md
CHECKPOINT40=stages/stage18/18-40/result.md
CHECKPOINT50=stages/stage18/18-50/result.md
CHECKPOINT60=stages/stage18/18-60/result.md
CHECKPOINT60_AUDIT=stages/stage18/18-60/audit.md
CHECKPOINT70=stages/stage18/18-70/result.md
FINAL_BUNDLE=stages/stage18/final.md
```

## Frozen theorem interface

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]
\[
\frac{M_2(B)}{U(B)}\sim\frac{36\zeta(3)C_{M_2}}{\pi}\frac{(\log B)^5}{B^2}\to0.
\]

The causal normal form is
\[
s^2+x^2=p^2,\qquad s^2+y^2=q^2,\qquad x^2+y^2\notin\square.
\]

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
ARSENAL_PROMOTION_REQUIRED=NO
UPSTREAM_INTERFACES_EXACT=true
STAGE16_TO_18_INCREMENTAL_CAUSE=DEFER_TO_STAGE22
STAGE18_TO_20_INCREMENTAL_CAUSE=DEFER_TO_STAGE26
NEXT_STAGE_AFTER_PASS=Stage19
CODEX_REQUIRED=false
AUDIT_REQUIRED=true
```
