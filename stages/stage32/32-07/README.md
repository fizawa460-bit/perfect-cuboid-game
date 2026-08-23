# Stage32-07 — d=6, genus-0 exact-row continuation

This Stage32-main-batch continues the unibranch numerical component after the merged d=4,g=0 row closure.

Scope is deliberately limited to the previously-unfinished `d=6, g=0` row.

Why this row comes before any degree >= 8 backend:

- the exact Stage32 dual caps give nonexceptional intersections <= 3 and exceptional intersections <= 1 at degree 6;
- therefore the 48 selected exceptional coordinates are still genuinely binary;
- the merged Stage32-05 exact fixed-weight MITM quotient reducer already supports `--genus 0` and its q-tail domain `0..3` exactly fills the certified subgroup;
- no bounded-multiplicity exceptional generalization is needed yet.

The aggregate identities leave exactly 49 nonnegative `(e,a)` parents for this row.

Phase A of this batch runs the existing exact reducer in `--reducer-only` mode over all 49 parents, records every deterministic candidate count, and stops without solver or receiver credit. If the candidate total is tractable, the same PR may advance to exact QF_NIA closure for all reducer survivors, with SAT retained and UNKNOWN receiving no credit.

Mandatory firewalls:

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

Stop after this single row. Do not generalize to degree >= 8 until a separate exact bounded-multiplicity exceptional design is implemented and benchmarked.
