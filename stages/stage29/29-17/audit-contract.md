# Stage29-17 final hostile-audit contract

This is the final Stage29 audit. Do not merge during audit.

## Fresh state lock

Read fresh from GitHub:

- PR base/head/draft/mergeable state;
- current `main` SHA;
- merged `GAP_SCAN_FINAL/audit-state.json`;
- merged `29-16/audit-state.json` and active/inactive ledgers;
- this 29-17 submission diff;
- current checks/workflow status.

The audit must not infer Stage29 closure from the operator's intent alone. Closure is allowed only if the handoff is internally consistent with the audited repository.

## Independent accounting

Reconstruct, without trusting the submission counts:

```text
SOURCE_FRONTIER_COUNT
CLOSED_CLASS1_COUNT
ACTIVE_CLASS2_COUNT
ACTIVE_CLASS3_COUNT
DORMANT_CLASS4_COUNT
FINAL_ACTIVE_KERNEL_COUNT
FINAL_CLASS2_KERNEL_COUNT
FINAL_CLASS3_KERNEL_COUNT
```

Expected values are respectively

```text
46, 6, 13, 11, 16, 13, 4, 9.
```

Require every active source receiver to remain mapped exactly once and all 16 dormant receivers to retain reactivation triggers. No hidden Class-1 work may be left pending.

## Semantic firewalls

Hostile-check every close statement against the merged source records.

In particular:

- Stage29 close is a program-phase close, not a proof of perfect-cuboid existence/nonexistence.
- `J12-POP-INTERACTION=GREEN` is theorem/output credit, not endpoint decision credit.
- `P/M3` remains unknown.
- `P/M3 -> 0`, if later proved, would not imply `P=0`.
- `PESCH-E1` remains conjectural; only the conditional implication is certified.
- the Brauer Class-2 kernel is a dependency DAG, not a strict linear chain.
- nine current execution owners means scheduling ownership only, not mathematical/statistical independence.
- no external claimed proof receives theorem credit unless primary full text and proof are source-locked and verified.

## Major-output spot checks

Spot-check the handoff summary against authoritative Stage29 records, including at least:

1. endpoint upper `P(B) <<_epsilon B^(1/2+epsilon)`;
2. exact final population-incidence/nested-host conclusions and their non-emptiness firewall;
3. `Delta_2=1/53760`;
4. Beauville exact squareclass/codimension-one parity closure;
5. modular marked defect count `8` and exact scope;
6. Ford seven-line base-complement geometric `Br[2]` precursor dimension `9`;
7. `K_c` ruled `(4,4)` model and geometric `Br[2]` dimension `2`;
8. one-step descent/etale-Brauer equivalence and the no-finite-open-twist inference firewall.

If any summary sentence overstates an audited source, repair the handoff on this same PR before PASS.

## Close-state requirements

PASS requires:

```text
GAP_SCAN_FINAL_AUDITED_PASS=true
SOURCE_FRONTIER_COUNT=46
CLOSED_CLASS1_COUNT=6
ACTIVE_CLASS2_COUNT=13
ACTIVE_CLASS3_COUNT=11
DORMANT_CLASS4_COUNT=16
FINAL_ACTIVE_KERNEL_COUNT=13
FINAL_CLASS2_KERNEL_COUNT=4
FINAL_CLASS3_KERNEL_COUNT=9
ACTIVE_SOURCE_ENTRY_UNMAPPED_COUNT=0
ACTIVE_SOURCE_ENTRY_DUPLICATE_MAPPING_COUNT=0
HIDDEN_CLASS1_PENDING_COUNT=0
DORMANT_REACTIVATION_TRIGGER_MISSING_COUNT=0
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If PASS, create/update an authoritative `audit-state.json` in this directory with:

```text
STAGE29_STATUS=CLOSED_ENDPOINT_SYNTHESIS_COMPLETE_RESIDUAL_RESEARCH_FRONTIER_FROZEN
STAGE29_CLOSED=true
PERFECT_CUBOID_PROBLEM_STATUS=OPEN
AUDIT_REQUIRED=false
MERGE_ALLOWED=true
STAGE29_CLOSE_ALLOWED=true
NEXT_ITEM=NONE_AUTOMATIC
```

Also repair `controller-delta.json` and PR body to the audited close state. Mark ready only if consistent with repository workflow; do not merge.

## Failure / backflow

FAIL or backflow is required if:

- a hidden executable Class-1 task is discovered;
- the final anti-miss audit did not actually pass on main;
- a count or mapping is inconsistent;
- a purported dormant item has an already-fired trigger;
- a handoff statement changes theorem scope;
- a current source proves or refutes a claim that the close summary marks differently.

Do not create Stage29-18 as bookkeeping. A real repair belongs on this PR. A genuinely new post-close research program should be separate from Stage29.

## Required final audit output

```text
GAP_SCAN_FINAL_AUDITED_PASS=true|false
SOURCE_FRONTIER_COUNT=<int>
CLOSED_CLASS1_COUNT=<int>
ACTIVE_CLASS2_COUNT=<int>
ACTIVE_CLASS3_COUNT=<int>
DORMANT_CLASS4_COUNT=<int>
FINAL_ACTIVE_KERNEL_COUNT=<int>
FINAL_CLASS2_KERNEL_COUNT=<int>
FINAL_CLASS3_KERNEL_COUNT=<int>
HIDDEN_CLASS1_PENDING_COUNT=<int>
ATTACK_ROUTE_COUNT=<int>
GREEN_ROUTE_COUNT=<int>
AMBER_ROUTE_COUNT=<int>
P_OVER_M3_SCALE_KNOWN=true|false
STAGE29_CLOSED=true|false
PERFECT_CUBOID_PROBLEM_STATUS=OPEN|CLOSED
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
MERGE_ALLOWED=true|false
STAGE29_CLOSE_ALLOWED=true|false
NEXT_ITEM=<value>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
