# Stage32-17 hostile audit

## Verdict

```text
PASS_EXACT_E20_A0_DELTA_AND_CUMULATIVE_LE114186_ZERO_TIER
```

PR: `#1376`

Audited functional aggregate head:

```text
526c149451449bd8542e33f3da3b1a416d87c3b9
```

The hostile audit accepts exactly the `d=8, g=0, e=20, a=0` cumulative materialized tier with per-cell branch count at most `114186`. It does not close the `e20/a0` parent, the full `d=8,g=0` row, Stage32-01, Stage32, or any Stage29 receiver.

## 1. Exact scope and profile boundary

The source-locked Stage32-14 profile was independently canonical-rehashed:

```text
profile canonical SHA256 = e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5
profile cells             = 1182
total materialized       = 7,806,762,328
```

Independent selection from the profile reproduces:

```text
predecessor <=65536:
  301 cells
  6,834,114 branches

delta 65536 < count <=114186:
  116 cells
  9,890,148 branches

cumulative <=114186:
  417 cells
  16,724,262 branches
```

The first profile value above the audited target is exactly

```text
115712 branches/cell
multiplicity = 128 cells
additional branches = 14,811,136
```

No cell on that plateau is included in Stage32-17.

## 2. Execution semantics and predecessor regression

`run_e20_work_bundle.py` is a thin adapter over the hostile-audited Stage32-16 exact bundle runner. It changes only the plan schema; solver, rational arithmetic, branch enumeration, UNKNOWN semantics, node-budget semantics, raw evidence generation, and post-verification compaction remain the Stage32-16 implementation.

The deterministic plan has:

```text
plan canonical SHA256 = 53eb260d70649fd6d938e3c7f4efa6b4c0fc1cfdfcb9c5e949ff5a706526e3f4
116 delta cells
364 modulo work items
<=32768 branches/work item
80 LPT bundles
4 dependency-ordered waves
max-parallel = 8
bundle load range = 109826..134565 branches
node limit/branch = 1,000,000
```

Before fanout, the maximum-load pilot recomputed hostile-audited predecessor cell `48`, shard `s0of2`:

```text
executed branches = 26,496
survivors = 0
branch-evidence-stream SHA256 =
b6d30e4f6d73d6e545d9594c29cebcbc4394f854d493b49b6c6aaa91233534b0
```

This exactly reproduces the predecessor certificate and validates the Stage32-17 plan-schema adapter against the previously audited execution semantics.

## 3. Source run, recovery, and exact reaggregation

The original source run `32779320736` successfully completed the pilot and 60 production bundles through waves 0--2. It later failed because ancestor Actions artifacts expired before wave3 could acquire its source-locked inputs. This was not a solver, UNKNOWN, node-budget, or arithmetic failure.

Recovery run `32796303960` independently regenerated the source locks/profile and executed only the missing 20 bundles. All recovered bundles completed exactly with UNKNOWN `0`.

The authoritative aggregate-only run is:

```text
run = 32802240965
job = 97665249993
head = 526c149451449bd8542e33f3da3b1a416d87c3b9
conclusion = success
```

It downloaded the 60 surviving source-run bundle receipts and 20 recovery receipts, proved that the sets are disjoint and their union is exactly the planned 80 bundles, then revalidated every compact certificate and every bundle commitment against the deterministic plan.

Hostile audit independently rechecked the final self-contained artifact and obtained:

```text
compact certificates = 364 / 364
bundle receipts       = 80 / 80
missing work items    = 0
duplicate work items  = 0
bad canonical hashes  = 0
bad deterministic receipt hashes = 0
bad modulo partitions = 0
receipt/certificate commitment mismatches = 0
```

For every compact certificate the audit rechecked the expected global-index modulo branch count, first/last branch index, `d=8,g=0,e=20,a=0`, node limit `1,000,000`, complete-branch flag, UNKNOWN count, and the receipt commitments to compact SHA, raw deterministic SHA, and branch-evidence-stream SHA.

## 4. Exact numerical result

The exact Stage32-17 delta is:

```text
cells                  = 116
materialized branches  = 9,890,148
search nodes            = 1,583,294
UNKNOWN                 = 0
numerical survivors     = 0
all delta cells         = UNSAT
```

Combining only with the hostile-audited Stage32-16 predecessor gives:

```text
cumulative cells        = 417 / 1182
materialized branches   = 16,724,262
search nodes             = 3,465,164
UNKNOWN                  = 0
numerical survivors      = 0
all selected cells       = UNSAT
remaining e20/a0 cells   = 765
```

The cumulative canonical SHA is

```text
c3680e432b12a61314c1852336a55e50f53ea23b151a05729d7f86db6b2e1d5c
```

and was independently recomputed from the downloaded aggregate JSON.

## 5. Historical Stage32-16 profile-SHA typo

The committed Stage32-16 execution state contains a 61-character transcription of the profile SHA in one metadata field:

```text
legacy = e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384d53fa1fee67c5
```

The Stage32-17 regenerated profile and deterministic plan independently lock the correct 64-character SHA:

```text
correct = e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5
```

The recovery adapter does not modify the historical audited file. It accepts exactly the known legacy string, independently re-locks the Stage32-16 predecessor canonical SHA

```text
5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c
```

and its recorded independent `48 artifacts / 287 compact certificates` reaggregation, then changes only an ephemeral copy of that metadata field before invoking the strict aggregate verifier. The audit accepts this as a metadata-transcription adapter only; no predecessor mathematical result is changed.

## 6. Final artifact

Authoritative artifact:

```text
name = stage32-17-e20-a0-le114186-recovered-exact-tier
run = 32802240965
artifact id = 9546895729
size = 788363 bytes
files = 451
compact certificates = 364
bundle receipts = 80
GitHub ZIP SHA256 = 37e4b66f2f6f62d05d9017b7f378edec9c7ea7b60d539c161a578fc59656e08a
```

The hostile audit independently downloaded the ZIP and reproduced the same ZIP SHA256. The root profile, plan, and aggregate canonical hashes were independently recomputed and matched exactly. Repository retention is currently five days, so the committed audit/execution state is the durable locator after artifact expiry.

## 7. Post-functional-head change audit

Comparing authoritative functional head `526c149...` to the pre-audit PR head `94d239...` shows exactly one later commit touching only:

```text
stages/stage32/32-17/README.md
stages/stage32/32-17/execution-state.json
```

No solver, plan, workflow execution, partition, compact-verifier, recovery-aggregator, or mathematical source changed after the authoritative aggregate. The latest PR workflow therefore correctly skips the expensive mathematical rerun.

## 8. Firewall and continuation

Accepted:

```text
E20_A0_LE114186_EXACT_ZERO_TIER=true
E20_A0_AUDITED_COMPLETED_CELLS=417
E20_A0_REMAINING_CELLS=765
UNKNOWN=0
```

Not accepted / still false:

```text
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
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

The next execution leaf remains inside Stage32-01 and must deal explicitly with the `115712 x 128` equal-cost plateau. It must not silently absorb that `14,811,136`-branch wall into this audit credit.
