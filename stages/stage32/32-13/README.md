# Stage32-13 — e10/a30 giant-tail closure

This unit continues the audited Stage32 d=8, g=0 numerical Picard census after the complete e8/a36 parent closure.

The audited e10/a30 profile has 134 immutable signature cells and 11,205,888 materialized branches. Existing exact evidence covers 130/134 cells. The four residual cells are:

- cell 43 `42ee1ca9ffc49798d5c927a6`: 1,095,920 branches;
- cell 64 `65bd86aef2d39bf5e13aa268`: 1,179,360 branches;
- cell 100 `cb01d3f2aed50c00b72d69e9`: 2,534,560 branches;
- cell 108 `d6c2af90f25f4a5940eb3dd1`: 2,596,160 branches.

No solver or mathematical constraint is changed. Stage32-13 reuses `32-11r/run_materialized_cell_shard.py` and partitions the first two cells into 8 exact residue shards each and the last two into 16 shards each. This gives 48 jobs with `max-parallel: 12` and roughly 140k–162k branches per job, matching the successful Stage32-11r execution scale.

## Storage-safe evidence mode

The first Stage32-13 run (`32702148657`) was manually cancelled after 15 raw shard artifacts had accumulated 265.5 MiB. The completed raw jobs were mathematically fine, but persisting one full branch-by-branch JSON per shard would have made the 48-shard run need roughly 0.8 GiB of artifact storage. That is an execution/storage design problem, not a mathematical or solver failure. The cancelled run is not accepted as Stage32-13 closure evidence.

The replacement workflow keeps the exact computation unchanged but changes only evidence persistence:

1. the existing exact shard solver writes the full raw JSON on the runner;
2. `compact_shard_certificate.py` rereads that raw JSON before upload and independently requires the exact modulo branch-index sequence, complete enumeration on every branch, no node-budget exhaustion, equality of branch-derived and top-level survivor ledgers, and all credit firewalls;
3. it hashes the raw deterministic report and a canonical per-branch evidence stream containing branch index, fixed-coordinate/base-certificate commitments, exact solver result, node/leaf counts, transcript SHA, and survivor basis SHAs;
4. only the compact certificate plus any actual numerical survivors is uploaded; the raw branch rows are deleted locally before artifact upload;
5. compact shard artifacts have `retention-days: 1`;
6. the final parent/orbit artifact has `retention-days: 30`.

A real cancelled-run artifact regression was performed before re-launch: raw cell-43 shard 3 contained 136,990 exact branches and was about 159 MB uncompressed; the post-verification compact certificate was about 2.3 KB, preserved zero survivors, and obtained compact SHA `ba4010d7d2fdf75fde6c0c44cd447a7ab75eaf5337347bc5a8719f6daabe2247`. This regression is a format/verification check only; the cancelled run remains non-credit evidence.

Thus compaction happens only after exact branch-by-branch verification. It does not prune search, drop UNKNOWN branches, change constraints, or replace computation with a summary shortcut.

After all 48 compact certificates complete, the workflow verifies exact disjoint/full branch coverage, combines the prior <=4096 tier, the 26 direct Stage32-11 e10 cells, the two Stage32-11r repaired e10 cells, and the four Stage32-13 giant cells into a 134/134 parent manifest. It then independently recloses the source-locked Aut(S) action of order 1536 and partitions every e10/a30 numerical survivor into full numerical orbits.

This is the next hostile-audit boundary. It does not imply effectivity, an actual curve, completion of the full d=8 row, receiver discharge, or any perfect-cuboid existence/nonexistence claim.

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
```
