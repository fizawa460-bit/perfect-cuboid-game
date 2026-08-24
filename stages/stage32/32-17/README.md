# Stage32-17 — e20/a0 exact continuation to the pre-115712 plateau boundary

This batch advances only the `d=8, g=0, e=20, a=0` numerical parent from the hostile-audited cumulative `materialized branches/cell <= 65536` checkpoint.

The Stage32-14 profile has a natural execution boundary immediately before a 128-cell equal-cost plateau:

- audited predecessor: `301` cells / `6,834,114` branches;
- selected delta: `65536 < branches/cell <= 114186`;
- delta: `116` cells / `9,890,148` branches;
- cumulative target: `417` cells / `16,724,262` branches;
- next profile value: `115,712`, with multiplicity `128` cells.

Stage32-17 therefore stops before the `115712 x 128` plateau instead of silently absorbing another `14,811,136` branches into the same audit unit.

Execution preserves the audited Stage32-16 exact solver semantics. The Stage32-17 runner is a thin schema adapter over `32-16/run_e20_work_bundle.py`; no search, cap, rational, branch, UNKNOWN, or node-budget semantics are changed. Dynamic global-index modulo shards remain bounded by `32,768` branches. The exact delta produces `364` work items, deterministically LPT-packed into `80` bundles over four dependency-ordered waves with `max-parallel: 8`.

A maximum-load bundle is executed as the pilot. The pilot also recomputes audited predecessor cell `48`, shard `s0of2` (`26,496` branches) and must reproduce branch-evidence-stream SHA-256 `b6d30e4f6d73d6e545d9594c29cebcbc4394f854d493b49b6c6aaa91233534b0` before fanout receives credit.

Raw exhaustive branch evidence remains runner-local and is deleted only after complete exact verification and compact-certificate creation. The conservative incremental retained-artifact bound is `27,280,000` bytes, below the repo policy's `100 MB` fallback ceiling and independent of deletion of historical evidence.

Audit boundary:

```text
AUDIT_FINAL_VERDICT=WAIT
HOSTILE_AUDIT_REQUIRED=true
E20_A0_PARENT_COMPLETE=false
STAGE32_01_COMPLETE=false
STAGE32_CLOSED=false
FULL_D8_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
```

Any UNKNOWN, node-budget exhaustion, missing/duplicate modulo residue, failed pilot/regression, artifact/storage gate failure, or incomplete wave blocks aggregate credit. No `115712` plateau cell is part of this batch.
