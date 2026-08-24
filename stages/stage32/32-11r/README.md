# Stage32-11r — timeout-cell exact shard repair

Source production run: `32689063120` from PR `#1364`.

That 37-cell parallel batch completed all scheduled cells except exactly three jobs, each cancelled externally during the exact exhaustive step at the 90-minute job wall:

```text
e8/a36  cell 39  ceb88a2b425fb743669aa33e  529,480 branches
e10/a30 cell 27  2719e0ba39bfa79944906bf5  639,840 branches
e10/a30 cell 37  3af4cf3d535a93607ef8b5bb  605,120 branches
```

No failed job produced a completed cell artifact. The logs show no solver error and no reported `UNKNOWN_NODE_BUDGET`; the Python process was terminated by the external job timeout before report finalization.

This repair changes only outer execution partitioning. Each immutable cell's deterministic global branch order is split into four disjoint residue classes by `branch_index mod 4`. Every selected branch is still solved by the unchanged audited Stage32-08 `search_exhaustive` backend with the same source-locked Picard core, exact cap certificate, qtail12 shared context, and per-branch node limit `1,000,000`.

The aggregate verifier requires all twelve shard artifacts, proves that branch indices are pairwise disjoint and cover every index `0..N-1` in each of the three parent cells, rejects any node-budget exhaustion or incomplete branch, unions numerical survivors, and keeps all theorem/effectivity/receiver firewalls closed.

This is a resource-wall repair, not a new conceptual Stage32 leaf. A hostile audit is required after the repaired cells and the successful evidence from `#1364` are assembled.

```text
THEOREM_CREDIT=false
AUDIT_STATUS=PENDING
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
