# Stage32-16 execution evidence for hostile audit — PR #1374

Execution verdict: `PASS_EXACT_E20_A0_DELTA_AND_CUMULATIVE_LE65536_ZERO_TIER`

Audit state: `AUDIT_FINAL_VERDICT=WAIT`, `HOSTILE_AUDIT_REQUIRED=true`.

This file is an audit handoff, not a hostile-audit verdict. The independently
audited Stage32-15 predecessor remains unchanged.

## 1. Locked scope and exact execution

The functional head is `0893fb99699ae8b0f16b2041c484e5c2b31111c6`.
Authoritative workflow run `32733420941` succeeded after all dependency-ordered
waves and the final aggregate completed. No larger tier was launched.

Documentation commit `7a11a78e3c5bfb662911143ce3321b6c730900fa` exposed that
GitHub evaluates a pull-request `paths` filter against the PR's complete base
diff, so redundant run `32751922545` was queued. It was explicitly cancelled
during its pilot and supplies no bundle or aggregate credit. The workflow now
has a separate commit-range gate: synchronization events launch heavy jobs only
when one of the six exact Python execution sources changed. Workflow-only
maintenance requires explicit dispatch. This trigger correction does not alter
the functional head, solver, certificates, or authoritative run.

The exact source-locked e20/a0 profile canonical SHA-256 is
`e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5`.
The inherited hostile-audited `<=16384` checkpoint is 69 cells / 655,558
branches / 279,710 search nodes, with canonical SHA-256
`593bb0fc5231222ab9ce79ae0bd5802d77311d02fd633152d665f869b095611f`.

The deterministic profile predicate selected exactly the requested delta:

- `16384 < materialized branches/cell <= 65536`;
- 232 cells;
- 6,178,556 materialized branches.

The plan used 287 exact global-index modulo work items, each no larger than
32,768 branches. Deterministic longest-processing-time packing created 48
bundles with exact branch loads from 111,648 to 129,376, executed in four
dependency-ordered waves with maximum parallelism eight. The plan canonical
SHA-256 is
`1f6f879d3f0e9eafd74dffc5afc4695e27f9758101fe32e23ecffcb16f07bdd6`.

The final verifier found every planned residue exactly once and rejected no
missing, duplicate, incomplete, UNKNOWN, or node-exhausted item. Exact delta:

- 232/232 cells complete;
- 6,178,556/6,178,556 branches complete;
- 287/287 work items represented;
- 1,602,160 search nodes;
- UNKNOWN = 0;
- numerical survivors = 0;
- all delta cells UNSAT.

The cumulative `<=65536` tier is therefore:

- 301/301 selected cells complete;
- 6,834,114/6,834,114 branches complete;
- 1,881,870 search nodes;
- UNKNOWN = 0;
- numerical survivors = 0;
- all selected cells UNSAT;
- canonical SHA-256
  `5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c`.

The final artifact is `stage32-16-e20-a0-le65536-exact-tier`, id
`9529005890`, ZIP SHA-256
`efd8b4403eb4557e0fa61d1ac2f894dac517d7f6e06aae2c1e2f506b8b7876a7`.
Its `e20-tier65536.json` is 268,052 bytes with SHA-256
`f31b4e8222d3638e05ba8ee5dddc1ab1d3f1aef4ecb3d083fe29965c42aad558`.

## 2. Equivalence and independent verification

The replacement runner recomputed inherited cell 588, shard `s0of2`, exactly:
2,448 branches, 48 search nodes, zero UNKNOWN, and zero survivors. It reproduced
the inherited branch-evidence-stream SHA-256
`8d258cf6ae672e497af3dcf4f32afe4f1dc4b35b41a7cebcec2501da5b424544`
and all predecessor counters. The regression result canonical SHA-256 is
`a6d319062c8d0e7045654b6f167f8425839edbee0bc73b98c476c15956a3c544`.
Artifact id `9523004366` has ZIP SHA-256
`52802de9951110b6334987b51599ed579f81a51edb3270ddc79996566023dd0f`.

After Actions completion, all 48 bundle artifacts were downloaded and the
aggregate was rebuilt locally against the locked profile and predecessor.
That independent pass verified 287 compact certificates and 48 receipts, and
its parsed JSON object exactly equals the authoritative aggregate. It
reproduced canonical SHA-256
`5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c`.

## 3. Runtime and resource measurements

The 48 bundle jobs consumed 52,650.961084 runner-seconds: 773.488444 minimum,
1,120.981007 median, and 1,290.026382 maximum. Shared exact-context
initialization consumed 618.951230 seconds total.

Stage32-15's measured exact-step baseline was 0.013564005825 seconds per
branch. Stage32-16 used 0.008521564114 bundle-seconds per branch, a 1.591727x
runner-efficiency improvement. End-to-end workflow throughput rose from
343.194570 to 588.265829 branches per wall-second, a 1.714088x improvement.
The redesign used 48 bundle jobs instead of the 464 jobs projected by fixed
two-shards-per-cell execution.

The conservative new-run retained-storage bound was 22,540,000 bytes. The
actual 51 uploaded artifacts totaled 553,651 compressed bytes; the largest was
64,184 bytes. Post-verification compact certificates totaled 653,831 bytes
before artifact compression. The largest runner-local raw work-item file was
38,041,679 bytes and was not persisted. Historical inventory was treated only
as context and no authoritative historical evidence was deleted.

## 4. Audit firewall and stop boundary

This execution closes only the selected e20/a0 numerical tier through 65,536
materialized branches per cell. It does not close the 1,182-cell e20/a0 parent;
881 cells remain outside this tier. It supplies no effectivity, receiver,
full-row, full-window, or theorem credit.

Mandatory retained state:

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

The batch stops at this exact tier and awaits independent hostile audit. No
next-tier research, optimization, or computation is part of PR #1374.
