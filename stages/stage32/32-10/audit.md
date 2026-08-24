# Stage32-10 hostile audit

Verdict: `PASS_DEEP_CUMULATIVE_E8_LE65536_E10_LE4096`

Audited PR: #1360  
Audited functional head: `26f14e9686f9aaed6d6995dde47ea0f835f406fd`

## Scope

This audit accepts only the deeper cumulative numerical materialization checkpoint produced by the unchanged Stage32-08 qtail12 solver. It does not accept parent completion, effectivity, actual-curve existence, orbit classification beyond prior audited claims, Stage29 receiver discharge, route-color change, or any perfect-cuboid theorem claim.

## Workflow evidence

Successful functional-head runs:

- `32686588506` — Stage32-10 exact `<=4096` high-mass tiers;
- `32686588363` — Stage32-10 e8 exact `<=65536` deep tier.

Accepted exact results:

```text
e8/a36 <=4096
  39/53 cells
  21,382 branches
  25 UNSAT cells / 14 SAT cells
  298 numerical survivors
  UNKNOWN 0
  nodes 137,474
  SHA 8e2ffd5cf7170ad51f647516f881be023a8b11050ab2bb2e5d8c580a6a513991

e10/a30 <=4096
  102/134 cells
  52,952 branches
  102 UNSAT cells / 0 SAT cells
  0 numerical survivors
  UNKNOWN 0
  nodes 202,964
  SHA 09ebeb9994ce8f4f78a0639a9ed0b71d02d483070ba8dafd201b40e751c651fd

e8/a36 <=65536
  44/53 cells
  122,906 branches
  29 UNSAT cells / 15 SAT cells
  330 numerical survivors
  UNKNOWN 0
  nodes 413,870
  SHA d043aa870efaff6baf25188c5eac0eb94a3ae10490295a719007d16b3eeb10a5
```

The accepted latest asymmetric checkpoint is e8/a36 `<=65536` plus e10/a30 `<=4096`.

## Independent recomputation

The audit downloaded the current artifacts and independently performed the following checks.

1. Recomputed deterministic tier SHA256 values using canonical JSON with recursive removal of `elapsed_seconds`, `shared_context_preparation_seconds`, and the embedded deterministic-hash field. All three hashes matched exactly.
2. Recomputed audited materialization-profile hashes:
   - e8/a36 `97608b176d7a91677f63cd293502f7042a9a9f6ad30904631260c9d560b7be17`;
   - e10/a30 `993d0005f60499b50b03b899153b60f93de757a74f53d942e5a2168830cc5123`.
3. Reconstructed threshold-eligible cells directly from `cells_sorted_by_branch_count`; selected cell IDs, selected cell indices, cell counts, and scheduled branch totals matched exactly for e8/e10 `<=4096` and e8 `<=65536`.
4. Compared every audited `<=256` predecessor cell against the corresponding recomputed `<=4096` cell after recursively stripping runtime-only fields; all records matched exactly for both parents.
5. Compared every e8 `<=4096` cell against the corresponding e8 `<=65536` cell after the same normalization; all records matched exactly.
6. Enumerated every accepted branch row:
   - e8 `<=4096`: 21,382 rows = 21,250 `UNSAT` + 132 `SAT_EXHAUSTED`;
   - e10 `<=4096`: 52,952 rows = 52,568 `UNSAT` + 384 `UNSAT_RADIUS`;
   - e8 `<=65536`: 122,906 rows = 122,758 `UNSAT` + 148 `SAT_EXHAUSTED`.
7. Every branch had final kernel dimension 12 and `node_budget_exhausted=false`.
8. e8 `<=4096` has 298 unique basis-coordinate and selected-coordinate survivor hashes; e8 `<=65536` has 330 unique hashes. The latter contains the former and adds exactly 32 new numerical classes, all with self-intersection `-8`.
9. e10 `<=4096` has zero survivors.

## Provenance nuance

The e8 `<=65536` workflow uses same-batch run `32686185075` as its `<=4096` predecessor. This does not weaken the certificate: it hard-locks deterministic SHA `8e2ffd5c...`, while final functional-head run `32686588506` independently reproduces that exact deterministic tier. Runtime-instance identity is therefore irrelevant to the mathematical prefix claim.

## Repo-local repairs

No solver or mathematical computation was changed by hostile audit. The audit repaired handoff state only:

- expanded `stages/stage32/32-10/README.md` from a pre-execution plan into the exact accepted evidence record;
- added this audit record and `audit-state.json`;
- advanced `stages/stage32/controller.json` from the audited `<=256` checkpoint to the accepted deep-tier checkpoint.

## Firewalls

All remain enforced:

```text
FULL_D8_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
theorem_credit=false
receiver_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
stage32_closed=false
```

Nine e8/a36 cells and thirty-two e10/a30 cells remain outside the latest accepted thresholds; `e20/a0`, full d=8, the complete Stage32-01 numerical census, effectivity, multibranch synthesis, and final Stage32 closure remain open.

`MERGE_ALLOWED=true` and `ADVANCE_ALLOWED=true` at audit scope, subject to ordinary GitHub mergeability/CI state after the audit-record commits.