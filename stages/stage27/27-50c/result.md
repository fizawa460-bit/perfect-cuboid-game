# Stage27-50c — Checkpoint50 synthesis boundary

```text
TASK_ID=Stage27-50c
PARENT=Stage27-50b
ROUTE_KIND=MAINLINE_SYNTHESIS_BOUNDARY
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

Checkpoint50 has now converted the unresolved Stage27 exponent into a stable interval-valued mainline contract.

Certified carried state:

\[
1/4\le \underline\alpha_{N_2}\le \overline\alpha_{N_2}\le 1/2
\]

in the usual `o(1)` exponent sense, with no claim that a single true exponent is known to exist or equal either endpoint.

Mainline consequences:

1. Stage19 theorem/construction reentry no longer blocks Stage27 progression;
2. future Stage27 checkpoints may consume the interval `[1/4,1/2]` as an inherited contract;
3. any statement stable throughout the interval may be certified;
4. any statement whose truth depends on where the exponent lies inside the interval remains explicitly conditional/unresolved;
5. Stage26 comparison against the `M_3` lower exponent `1/3` remains unresolved because `1/3` lies inside the interval.

No additional mathematical improvement is claimed at Checkpoint50. This checkpoint is a synthesis and routing result.

The next mainline checkpoint should therefore be allowed to ask a new downstream question under the inherited interval rather than reopening the same Stage19 exponent attack.

```text
CHECKPOINT50_SYNTHESIS_COMPLETE=true
INHERITED_N2_EXPONENT_INTERVAL=[1/4,1/2]
TRUE_N2_EXPONENT_IDENTIFIED=false
STAGE19_BLOCKER_ACTIVE=false
N2_VS_M3_ORDERING_RESOLVED=false
ADVANCE_TO_CHECKPOINT60=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage27-50-audit
POST_AUDIT_NEXT_ROUTE=Stage27-60-main-batch
```
