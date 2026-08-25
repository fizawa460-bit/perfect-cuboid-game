# Stage32-18E — exact symmetry-pruned d16 b12 production

Accepted predecessor is the hostile-audited exact `d=16, g=0, b=10` checkpoint: 1,430 canonical records with histogram `{0:1,2:1,4:7,6:28,8:223,10:1170}`. Stage32-18D and scout3 established the next meaningful wall `b=12`; 64 inherited breakers hit the 500M-node profile cap, while 256 prefix-ranked Aut score inequalities reduced the 30-minute snapshot-fast profile to 216,940,544 nodes, but still timed out. Those profiles grant no b12 numerical credit.

This leaf changes the exact certifier rather than extending an uncertified floating run. The 256 scout3 inequalities are all genuine full-`Aut(S)` score inequalities `score(v) <= score(gv)`. Each one is converted to the same exact LDL coordinates as the audited cap constraints. Floating arithmetic is allowed only to schedule a proof attempt; an actual branch rejection occurs only when exact rational Cauchy--Schwarz proves that the remaining norm ball cannot reach the required nonnegative half-space. Exact integer breaker tests and full order-1536 canonicalization remain at leaves.

Execution is deliberately resource-safe and run-key gated:

1. source-lock and reconstruct the audited Stage32-18C exact sharded certifier;
2. reconstruct the scout3 256-breaker bundle and lock its canonical bundle SHA;
3. run an exact `b=6` regression requiring the hostile-audited 37-record dump byte-for-byte;
4. only after that gate, execute `b=12` as 64 deterministic exact prefix shards (`split_coordinate=54`, max parallel 8);
5. if all shards complete, aggregate exact records, require the `norm<=10` subset to be byte-identical to the hostile-audited exact b10 set, and independently reverify every b12 record under the full order-1536 group;
6. stop for hostile audit. A resource-wall shard failure receives no numerical credit and is preserved as an execution-design checkpoint for targeted repair.

The workflow listens only to `stages/stage32/runkeys/18e-b12-exact.json`; source, audit, README, and controller edits do not themselves authorize a heavy rerun.

```text
D16_B10_NUMERICAL_CREDIT=true
D16_B12_NUMERICAL_CREDIT=false
D16_B12_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT=false  # becomes true only in a complete aggregate certificate
FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED=false
SNAPSHOT_FAST_GLOBAL_COMPLETENESS_CERTIFIED=false
FULL_D16_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
```
