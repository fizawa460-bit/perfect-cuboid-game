# Stage32-10 — deep cumulative high-mass materialized-tier continuation

Accepted predecessor: hostile-audited Stage32-09 cumulative `<=256` checkpoint.

This unit keeps the exact Stage32-08 materialized qtail12 solver unchanged: same source-locked Picard core, immutable signature-cell inventory, exact 140 cap certificates, kernel dimension 12, and `1,000,000` node limit per materialized branch. It therefore advances only the cumulative selected-cell numerical tier; no algorithmic, effectivity, orbit, or receiver interpretation is introduced.

## Hostile-audited production evidence

Functional head `26f14e9686f9aaed6d6995dde47ea0f835f406fd` produced two successful workflows:

```text
run 32686588506 — <=4096 cumulative tiers

e8/a36
  selected cells      39/53
  scheduled branches  21,382
  complete cells      39
  UNSAT cells         25
  SAT cells           14
  numerical survivors 298
  UNKNOWN             0
  search nodes        137,474
  deterministic SHA   8e2ffd5cf7170ad51f647516f881be023a8b11050ab2bb2e5d8c580a6a513991

e10/a30
  selected cells      102/134
  scheduled branches  52,952
  complete cells      102
  UNSAT cells         102
  SAT cells           0
  numerical survivors 0
  UNKNOWN             0
  search nodes        202,964
  deterministic SHA   09ebeb9994ce8f4f78a0639a9ed0b71d02d483070ba8dafd201b40e751c651fd

run 32686588363 — e8/a36 <=65536 deep tier

  selected cells      44/53
  scheduled branches  122,906
  complete cells      44
  UNSAT cells         29
  SAT cells           15
  numerical survivors 330
  UNKNOWN             0
  search nodes        413,870
  deterministic SHA   d043aa870efaff6baf25188c5eac0eb94a3ae10490295a719007d16b3eeb10a5
```

The e8 `<=65536` tier is cumulative and contains the full `<=4096` tier exactly. Relative to e8 `<=4096`, it adds 5 cells, 101,524 materialized branches, 4 UNSAT cells, 1 SAT cell, and 32 new numerical Picard classes. Those 32 new classes all have self-intersection `-8`; no orbit or effectivity conclusion is assigned.

The accepted latest checkpoint for this unit is therefore asymmetric by executed cost:

```text
e8/a36  <=65536 : 44/53 cells, 122,906 branches, 330 numerical survivors, UNKNOWN 0
e10/a30 <=4096  : 102/134 cells, 52,952 branches, 0 numerical survivors, UNKNOWN 0
```

## Independent audit locks

Hostile audit independently verified all of the following from downloaded artifacts rather than trusting workflow summaries:

1. canonical profile SHAs reproduce exactly:
   - e8/a36 `97608b176d7a91677f63cd293502f7042a9a9f6ad30904631260c9d560b7be17`;
   - e10/a30 `993d0005f60499b50b03b899153b60f93de757a74f53d942e5a2168830cc5123`;
2. deterministic tier SHAs above recompute after recursively removing runtime-only fields;
3. profile-selected cell IDs/indices and scheduled branch totals equal the materialized tiers exactly;
4. the entire audited `<=256` predecessor is byte-equivalent after runtime-field removal inside both `<=4096` tiers;
5. the entire e8 `<=4096` tier is byte-equivalent after runtime-field removal inside e8 `<=65536`;
6. every accepted branch has final kernel dimension 12, no node-budget exhaustion, and complete terminal status;
7. e8 `<=65536` has 122,906 executed branch rows (`122,758 UNSAT`, `148 SAT_EXHAUSTED`) and 330 pairwise-distinct numerical survivors;
8. e10 `<=4096` has 52,952 executed branch rows (`52,568 UNSAT`, `384 UNSAT_RADIUS`) and zero survivors.

A provenance nuance is harmless but recorded: the e8 `<=65536` workflow downloads an earlier same-batch `<=4096` artifact from run `32686185075`. It hard-locks deterministic SHA `8e2ffd...`, and the final-head `<=4096` rerun `32686588506` independently reproduces the identical deterministic tier, so no mathematical content depends on the earlier runtime instance.

## Credit boundary

This remains a cumulative selected immutable-signature-cell numerical tier. Nine e8/a36 cells and thirty-two e10/a30 cells are still outside the latest accepted thresholds, and the much larger `e20/a0` parent remains untouched. Therefore neither parent, the full `d=8,g=0` row, nor Stage32-01 is complete.

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

Hostile-audit verdict: `PASS_DEEP_CUMULATIVE_E8_LE65536_E10_LE4096`. Continue only through the same Class-2 numerical-census leaf or another explicitly audited safe branch; effectivity remains a separate Stage32-02 obligation.