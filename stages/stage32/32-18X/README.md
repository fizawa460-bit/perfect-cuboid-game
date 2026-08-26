# Stage32-18X — b16 exact leaf shard-geometry pilot

Stage32-18W established that b16 descendant work through probe coordinates 50 and 48 is reasonably balanced. That is not enough to authorize production: b14 later exposed deep full-leaf tails in residues that did not look extreme at p48.

18X therefore measures **actual exact b16 leaf traversal** on a small adversarial geometry pilot before any full census.

Three geometries are compared under the same immutable exact certifier and the same 40,000,000-node hard cap per job:

1. `c54/1024` historical-tail controls: residues `436,503,922`, each of which required roughly 109M–126M nodes at b14 before rescue;
2. `c48/1024` global shards: ids `0,436,748,922`;
3. `c48/2048` global shards: ids `0,436,748,922`.

The c48 split is intentionally global: it hashes at coordinate 48 instead of keeping every deep descendant of a single c54 residue in one job. The 2048-way variant halves the mean p48-prefix ownership again and is the safety-side fallback if 1024-way remains too heavy.

Every completed pilot is a genuine exact bound-16 traversal certificate, but the pilots cover only a tiny subset of the global partition and therefore grant **no b16 census credit**. Resource-wall outcomes are operational evidence only.

Decision rule:

- prefer c48/1024 if all four pilots complete comfortably (<=30M nodes and <=900s each);
- otherwise prefer c48/2048 if all four complete comfortably;
- otherwise redesign deeper/adaptively before production.

The c54 controls are diagnostic and are not required to complete.

Credit firewall:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
