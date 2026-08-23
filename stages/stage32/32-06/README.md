# Stage32-06 — exact d=4, genus-0 row batch

This bounded Stage32-main-batch continues the unibranch numerical component after the merged Stage32-05 d=6,g=1 residual closure.

Scope is deliberately limited to the single previously-unfinished target row `d=4, g=0`.

Exact inputs and reductions:

- source-lock the rank-64 Stage32 Picard core from run `32624596141`;
- re-derive and exactly verify all 140 Stage32 dual-cap certificates;
- at degree 4, every nonexceptional intersection is at most 2 and every exceptional intersection is at most 1;
- reuse the exact selected-intersection transform (determinant `2^38`, inverse denominator 8) only to derive the complete `(e,a)` parent inventory;
- the exact aggregate structure leaves 25 feasible `(e,a)` parents out of 632 formal budget parents; the other 607 are excluded before lattice search;
- for each of the 25 feasible parents, run the generic exact rank-64 `QF_NIA` enumerator to exhaustion, not a model-limited search;
- the generic solver enumerates a superset because it does not use the new per-class dual caps internally; every completed model is therefore independently rechecked and filtered by the exact degree-4 caps afterward;
- a parent receives target-complete status only if the superset solver terminates `UNSAT` after enumerating every model. `UNKNOWN` or timeout receives no credit.

If the final cap-valid survivor count is zero, orbit deduplication is vacuous and this single `d=4,g=0` numerical row is complete pending hostile audit. If cap-valid survivors exist, the batch records them but does not claim orbit completion until an exact automorphism/orbit pass is supplied.

Mandatory firewalls remain:

```text
THEOREM_CREDIT=false
AUDIT_STATUS=PENDING
RECEIVER_CREDIT=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

Stop after this one row. Do not generalize the binary-exceptional MITM to degree >=8 in this batch: the exceptional cap becomes greater than 1 there, so the Stage32-05 fixed-weight binary architecture no longer applies without a new exact bounded-multiplicity design.
