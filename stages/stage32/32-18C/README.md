# Stage32-18C — d16 b10 resource-safe exact/cross-certified production

This unit advances only the next meaningful even norm wall after hostile-audited b8: `b10`.

The b8 exact baseline required about 32m48s, so b10 is not executed as one monolithic exact job. The resource-safe design is:

1. run the existing 64-breaker fast implementation at b10 as a bounded preview;
2. mechanically derive an exact sharded certifier from the same hostile-audited Stage32-18A exact source blob;
3. partition the exact DFS at a fixed prefix depth using a deterministic hash of the already-assigned exact coordinate prefix;
4. run 16 disjoint exact shards;
5. aggregate the complete exact canonical set, independently verify it under the full order-1536 group, and require equality with the fast canonical set.

The shard assignment depends only on the exact prefix coordinate vector, not traversal order or a floating decision. Floating arithmetic remains only a scheduler for whether to attempt an exact Cauchy–Schwarz prune test; no floating comparison can reject a branch.

The audited b8 histogram `{0:1,2:1,4:7,6:28,8:223}` and cumulative canonical count `260` are enforced as predecessor regressions inside the b10 aggregate.

No b10 numerical credit is granted unless all 16 exact shards complete and the exact/fast canonical sets agree.

```text
AUDIT_STATUS=PENDING
FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED=false
D16_PRODUCTION_EXACT_OR_CROSS_CERTIFICATE_REQUIRED=true
FULL_D16_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
```

After a complete b10 cross-certificate, stop for hostile `Stage32-audit`.
