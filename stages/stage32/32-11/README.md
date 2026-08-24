# Stage32-11 — profile-guided parallel exact tail closure

Accepted predecessor: hostile-audited Stage32-10, with e8/a36 complete through the cumulative `<=65536` tier (44/53 cells) and e10/a30 complete through `<=4096` (102/134 cells).

This unit does **not** change the numerical solver. It reuses the exact Stage32-08 one-signature-cell exhaustive runner, the source-locked Picard core, the audited immutable materialization profiles, the exact 140 cap certificate derivation, kernel dimension 12, and the existing `1,000,000` node limit per branch. The only operational change is scheduling: expensive remaining cells are run independently in a matrix so the 90-minute Actions wall applies per cell instead of to a cumulative serial tier.

## Scheduled batch

- e8/a36: all 9 cells not contained in the audited `<=65536` checkpoint, totaling 1,661,045 materialized branches. If all nine complete exactly with no UNKNOWN, the e8/a36 53-cell parent numerical census is complete and must stop for hostile audit before any parent/orbit interpretation.
- e10/a30: all 28 cells with audited profile cost `4096 < branches <= 700000`, totaling 3,746,936 materialized branches. Together with the audited `<=4096` checkpoint this can reach 130/134 cells. Four giant profile cells remain outside this batch at 1,095,920; 1,179,360; 2,534,560; and 2,596,160 branches.

Every matrix job locks its exact profile row `(cell_index, cell_id, materialized_branch_count)`, re-derives the exact cap certificate, executes the existing exhaustive qtail12 cell solver, rejects node-budget exhaustion/UNKNOWN, and preserves all theorem/receiver/effectivity firewalls. `fail-fast` is disabled so one resource-wall cell does not discard evidence from completed siblings.

This is intentionally a large batch rather than another sequence of bookkeeping thresholds. The next stop is meaningful: exact e8 parent completion, an UNKNOWN/90-minute resource wall, or completion of the planned e10 tranche.

```text
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
FULL_D8_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
