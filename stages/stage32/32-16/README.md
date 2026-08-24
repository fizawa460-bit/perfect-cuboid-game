# Stage32-16: exact e20/a0 cumulative tier `<=65536`

This batch advances only the declared `d=8, g=0, e=20, a=0` numerical
component from the hostile-audited Stage32-15 cumulative tier `<=16384` to
the cumulative tier `<=65536`.

The inherited evidence is not recomputed. Its canonical SHA-256 is
`593bb0fc5231222ab9ce79ae0bd5802d77311d02fd633152d665f869b095611f`
and it covers 69 cells / 655,558 exact materialized branches. The new delta is
exactly 232 cells / 6,178,556 branches; the target cumulative tier is 301
cells / 6,834,114 branches.

## Execution architecture

`build_e20_tier65536_plan.py` verifies the source-locked profile and audited
predecessor, profiles the exact branch distribution, and applies two
execution-only transformations:

1. A cell is divided into the minimum number of modulo shards needed to keep
   each work item at most 32,768 materialized branches. This produces 287
   exact work items instead of mechanically creating two shards for every
   cell.
2. The work items are assigned by deterministic longest-processing-time
   packing to 48 bundles using exact expected branch count as the workload.
   Bundle loads range from 111,648 to 129,376 branches. A maximum-load bundle
   runs first as the representative storage/runtime gate. The remaining 47
   bundles run in four explicit dependency-ordered waves (12 total bundles per
   wave, with the pilot replacing one wave-0 matrix entry), with at most eight
   concurrent runners inside a wave. A failure or UNKNOWN prevents later waves.

`run_e20_work_bundle.py` initializes the inherited exact Picard/FLINT search
context once per bundle and then executes each planned modulo shard with the
unchanged 1,000,000-node limit per branch. It uses the same exact 12-dimensional
FP140 exhaustive search, all 140 caps, exact rational arithmetic, branch-base
construction, and `GLOBAL_BRANCH_INDEX_MOD_SHARD_COUNT` partition semantics as
Stage32-15. Any incomplete branch or exhausted node budget makes compaction
fail and stops the workflow.

Raw branch rows exist only runner-locally, one work item at a time. Each raw
shard is independently verified by `compact_e20_dynamic_shard.py`; only then
is its compact certificate written and the raw file deleted. Transient bundle
artifacts have one-day retention. The aggregate independently requires every
planned modulo residue exactly once and re-verifies every compact and bundle
hash before combining the delta with the audited predecessor.

The workflow trigger names only executable Stage32-16 sources and the workflow
itself. Because GitHub evaluates pull-request path filters against the PR's
entire base diff, a lightweight change gate also compares only the newly pushed
commit range. Heavy jobs run only when an exact Python execution source changed
(or on an initial/explicit dispatch); README, audit, execution-state, and
workflow-maintenance-only revisions cannot relaunch the heavy tier.

The storage preflight inventories all retained repository artifacts for audit
context but gates only the incremental footprint of this batch. Without
depending on deletion, the new run has a conservative 22,540,000-byte bound:
5,740,000 bytes for 287 compact shard certificates, 4,800,000 bytes for 48
bundle receipts, 10,000,000 bytes for the final aggregate, and 2,000,000 bytes
for the plan, storage report, and targeted regression evidence. Transient
bundle artifacts retain for one day. Authoritative historical evidence is not
deleted.

A targeted replacement-runner regression recomputes only inherited cell 588,
shard `s0of2` (2,448 branches). The local prelaunch check reproduced the
predecessor branch-evidence stream SHA-256
`8d258cf6ae672e497af3dcf4f32afe4f1dc4b35b41a7cebcec2501da5b424544`,
48 search nodes, zero survivors, and every compact aggregate counter exactly.
The Actions pilot repeats and preserves this narrowly scoped regression.

## Measured predecessor baseline

Actions run 32726279718 used 105 measured bulk shard jobs for 604,320 branches.
Those jobs consumed 11,524 runner-seconds, of which 8,197 seconds were in the
exact enumeration step and 3,327 seconds were repeated setup/non-enumeration
work. Median job, exact-step, and non-exact times were 109, 79, and 31 seconds.
A mechanical two-shard design for the current 232-cell delta would require 464
compute jobs; Stage32-16 uses 48 gated bundles and reuses the exact context
within each bundle. Final observed runtime/resource comparisons are recorded
after exact aggregation.

## Completed execution and audit boundary

Authoritative workflow run `32733420941` completed successfully at functional
head `0893fb99699ae8b0f16b2041c484e5c2b31111c6`. All 287 planned work items in
all 48 bundles were present and verified. The exact delta disposition is 232
cells / 6,178,556 branches / 1,602,160 search nodes, with zero UNKNOWN and zero
numerical survivors. Combined with the inherited predecessor, the cumulative
result is 301 cells / 6,834,114 branches / 1,881,870 search nodes, again with
zero UNKNOWN and zero numerical survivors.

The final aggregate canonical SHA-256 is
`5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c`.
The final artifact is `stage32-16-e20-a0-le65536-exact-tier`, id `9529005890`,
with ZIP SHA-256
`efd8b4403eb4557e0fa61d1ac2f894dac517d7f6e06aae2c1e2f506b8b7876a7`.
An independent local re-aggregation from all 48 downloaded bundle artifacts
reproduced the same parsed aggregate and canonical hash.

The Actions predecessor regression reproduced the inherited 2,448-branch
neighbor exactly. Its result canonical SHA-256 is
`a6d319062c8d0e7045654b6f167f8425839edbee0bc73b98c476c15956a3c544`;
the regression artifact is id `9523004366`, ZIP SHA-256
`52802de9951110b6334987b51599ed579f81a51edb3270ddc79996566023dd0f`.

Measured bundle runner time was 52,650.961084 seconds total, with 773.488444
seconds minimum, 1,120.981007 seconds median, and 1,290.026382 seconds maximum.
The new runner used 0.008521564114 bundle-seconds per branch versus
0.013564005825 exact-step seconds per branch in the measured Stage32-15
baseline, a 1.591727x runner-efficiency improvement. End-to-end Actions
throughput rose from 343.194570 to 588.265829 branches per wall-second, a
1.714088x improvement, while processing 10.1827x the delta branch volume.

Actual uploaded storage for all 51 run artifacts was 553,651 compressed bytes,
far below the conservative 22,540,000-byte incremental bound. The largest
uploaded artifact was 64,184 bytes; the largest runner-local raw work-item file
was 38,041,679 bytes and was not persisted. No authoritative historical
evidence was deleted.

This is an execution result, not a self-awarded hostile-audit verdict.
`AUDIT_FINAL_VERDICT=WAIT` and `HOSTILE_AUDIT_REQUIRED=true` until an independent
audit accepts the evidence. The declared `<=65536` stopping boundary has been
reached, and this batch launches no larger tier.

The following remain unchanged:

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

This batch makes no claim about existence or nonexistence of a perfect cuboid.
