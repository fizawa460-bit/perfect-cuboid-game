# Stage14-num-α10 — exact B400m stability checkpoint

> STATUS: `STAGE14_NUM_ALPHA10=COMPLETE_EXACT_B400M_CHECKPOINT`
>
> CLASSIFICATION: finite exact census + operational finite stability diagnostics; no asymptotic claim.

The validated α engine scanned only the new interval `300m<d<=400m` in four disjoint 25m shards. Before accepting the new checkpoint, the nested B250m and B300m subsets reproduced merged α9 in every frozen count, graph field and SHA lock.

## Exact B400m checkpoint

```text
(Na,Nb,Nc)=(1240,1252,702)
N2=3194
T=0
active oriented faces=4639
raw pair edges=3194
max degree=12
object SHA=ac17f7bf946d1314e8c3cab52ca667a25754e5f04ab048a7c8e0794d38416afa
object+mask SHA=b57c4487096ff53993dc0f3660b649312006f82ffce20f2d4c89e6653f424ffb
vertex SHA=2b19a2653786555caa8eb57c8cc2cdb0497f71864972869c34f988f4bc3c8a75
edge SHA=61427610256b561d4585dbfa060c1b7d73d2e1b89b7da711d8faadb383df89ae
```

New shell `300m<d<=400m`: `{'a': 123, 'b': 121, 'c': 84, 'total': 328, 'triple': 0}`.

## Stability panel

`N2/sqrt(B)` is `0.168043434861348` at B250m, `0.165468587149747` at B300m, and `0.159700000000000` at B400m.

For 300m→400m, the largest primary relative drift is `3.6121%` and `all_primary_at_or_below_2pct=false`.

The terminal stopping gate is intentionally not evaluated here; α11 still needs the 400m→500m transition. This 2% gate is an operational finite-data convention, not an asymptotic theorem or confidence interval. `T=0` through B400m is not a nonexistence proof.

```text
B250M_ALPHA9_FULL_HASH_REGRESSION_MATCH=true
B300M_ALPHA9_FULL_HASH_REGRESSION_MATCH=true
B400M_EXACT_CENSUS_FROZEN=true
PERFECT_CUBOID_EMERGENCY=false
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha11 exact B500m terminal checkpoint and stability stop gate
```
