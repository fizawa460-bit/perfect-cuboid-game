# Stage32-18X — b16 real-leaf tail-geometry pilot

Accepted predecessor: hostile-audited b14 census (`44,450` canonical including zero, dump SHA256 `4d4680a87fab0c01ac8b54bcf404eecaa707cf5db782b31d5fa7357a52249d8a`) and the completed b16 descendant profiles from Stage32-18W.

18W shows b16 work through p48 is not more skewed than b14, but the audited b14 history proves that a benign p48 profile can still hide very deep exact-leaf tails. 18X therefore probes actual b16 exact leaves on the three c54 residues that were the final b14 tails: `436`, `503`, `922`.

Final pilot geometry:

- primary gate: coordinate `54`, modulus `1024`, residues `[436,503,922]`;
- secondary gate: coordinate `48`, `8` exact shards per primary;
- total logical children: `24`;
- exact traversal node cap: `18,000,000` per child;
- max Stage32 parallelism: `15`;
- Aut group order: `1536`;
- DFS symmetry breakers: `256`.

The first armed run exposed an evidence-wrapper bug rather than a mathematical failure: GNU `time` wrote an abnormal-exit line before the elapsed seconds and the wrapper tried to parse both lines as one float. The workflow was hardened without changing the exact traversal: `/usr/bin/time -q`, last-line runtime parsing, explicit node-cap/wallclock resource statuses, and an internal 50-minute wallclock cap inside a 60-minute Actions job.

Generation 3 run `33026404734` completed successfully. All `24/24` child jobs uploaded compact evidence and the summary job passed. Every child hit the exact node cap:

- primary `436`: `8/8 RESOURCE_WALL_NODE_CAP`;
- primary `503`: `8/8 RESOURCE_WALL_NODE_CAP`;
- primary `922`: `8/8 RESOURCE_WALL_NODE_CAP`.

Observed child runtimes ranged from about `996 s` to `1930 s`. No child reached an exact `COMPLETE` leaf certificate. Therefore coordinate48 split eight ways is still too coarse for b16 production.

Frozen verdict:

`B16_TAIL_GEOMETRY__C48_EIGHT_WAY_INSUFFICIENT__FINER_SECONDARY_SPLIT_REQUIRED`

Next item:

`32-18Y-D16-B16-C48X16-TAIL-PILOT`

This leaf is resource-design evidence only. No b16 numerical/global/theorem/receiver/controller credit is granted.

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
