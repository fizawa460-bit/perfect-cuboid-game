# Stage32-18AY — B16 172-monster selective subfrontier design

Status: DESIGN_COMPLETE_READY_FOR_IMPLEMENTATION

## Input

The six cut39 walls have completed equal-budget tier3 cost measurement at 262144 nodes. The unresolved parent-frontier counts are:

- p436/s5: 36
- p436/s362: 34
- p503/s118: 31
- p503/s665: 30
- p922/s13: 22
- p922/s38: 19
- total: 172

These are resource-capped frontier parents, not mathematical survivors and not UNSAT/SAT claims.

## Why not blind tier4

A uniform larger node budget would measure only another point on the same heavy tail and can spend most of the run inside a small number of pathological parents. Earlier whole-wall lower-cut scouting also showed that dropping from cut39 to cut31 globally creates a frontier of order 1.5 million states on p436/s5, so a whole-wall cut31 rerun is deliberately forbidden.

## Selected strategy

Keep the certified cut39 partition fixed and operate only on the 172 explicit monster parent IDs.

For each selected cut39 parent:

1. replay exactly to that parent using the existing deterministic frontier numbering;
2. instead of solving the parent to completion, descend only that parent from coordinate 39 to a secondary cut;
3. emit/count its child subfrontier with a parent-local child index and deterministic transcript commitment;
4. do not descend any cut39 parent outside the explicit monster ID set;
5. compare child counts and cheap child-cost samples before choosing production budgets.

The first secondary-cut scout should use cut31 because that cut is already characterized at whole-wall scale. However, it must be selective-parent only. If selected expansion exceeds a conservative child cap, stop and retry at cut35 before any larger fanout.

## Required implementation interface

Add a selective subfrontier mode to the exact certifier with arguments equivalent to:

- `--subfrontier-parent-id-file <ids>`
- `--subfrontier-parent-cut 39`
- `--subfrontier-child-cut 31`
- `--subfrontier-child-cap <cap>`
- `--subfrontier-output <csv/json>`

Each emitted child identity must be `(wall, parent_frontier_id, child_frontier_id)` and numbering must be deterministic under the locked source artifact.

The compact certificate must record:

- locked source artifact id/digest;
- wall and exact selected parent IDs;
- parent cut and child cut;
- per-parent child counts;
- total emitted child count;
- cap/overflow status;
- deterministic child-frontier stream SHA256;
- zero silent omission/duplication of selected parents;
- all mathematical-credit firewalls false.

## First scout

Implement and run one representative wall first: p436/s5, exactly its 36 monster parents. Persist only the compact distribution/certificate. Raw subfrontier rows remain runner-local after hashing.

Scale to the other five walls only if:

- p436/s5 expansion completes under the child cap;
- artifact size remains compact;
- effective Stage32 heavy concurrency remains <=18;
- the child-count distribution shows selective subdivision is materially more informative than blind tier4 probing.

## Stop rules

Do not:

- rerun any of the 239... already tier3-resolved cut39 parents;
- run whole-wall cut31;
- arm B18 or higher;
- treat a capped parent as a mathematical survivor;
- promote numerical, theorem, receiver, or endpoint credit from this scout.

If one or a few parents dominate child fanout, isolate those parents individually rather than raising the global budget.

## Intended next state

`32-18AZ_D16_B16_P436S5_36_MONSTER_SELECTIVE_SUBFRONTIER_SCOUT`
