# Stage32-18Y — b16 c48x16 tail-geometry pilot

Stage32-18X tested the three historical b14 tail primaries `436`, `503`, and `922` at bound16 using a coordinate48 eight-way secondary split. Generation 3 completed cleanly as evidence, but all `24/24` logical children hit the exact `18,000,000` node cap. Therefore x8 was too coarse.

18Y kept every mathematical source lock and gate fixed and changed only the execution partition geometry:

- primary coordinate/modulus: `54 / 1024`;
- primary residues: `[436,503,922]`;
- secondary coordinate: `48`;
- secondary shard count: `16`;
- logical children: `48`;
- exact traversal node cap: `18,000,000` per child;
- max concurrent heavy jobs: `15`.

The prepared exact certifier remained immutable from artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`. Each child preserves exact rational branch rejection, the 256 DFS symmetry breakers, and Aut order `1536`.

Operational safety was enforced by the ARM gate: repository artifact usage plus the capped worst-case 18Y peak had to remain below 500MB; child artifacts were capped at 4,000,000 uncompressed bytes; effective Stage32 parallelism was fixed at 15.

## Frozen result

Generation 1 run `33030066426` completed GREEN as evidence. Summary artifact `9631617459` has digest `sha256:3607380f62285a7c89919f0b184bceb296713b8a18fc7ae81f135e289f79c0f2`.

The x16 refinement partially closes the historical tails:

- primary `436`: COMPLETE secondaries `{2,4,13}` = `3/16`;
- primary `503`: COMPLETE secondaries `{1,7,14}` = `3/16`;
- primary `922`: COMPLETE secondaries `{4,5,8,9}` = `4/16`;
- total COMPLETE = `10/48`;
- remaining `38/48` children hit `RESOURCE_WALL_NODE_CAP`;
- wallclock walls = `0`;
- artifact-size walls = `0`.

Verdict:

`B16_TAIL_GEOMETRY__C48_SIXTEEN_WAY_INSUFFICIENT__FINER_SECONDARY_SPLIT_REQUIRED`

Next item:

`32-18Z-D16-B16-C48X32-TAIL-PILOT`

The next pilot should not recompute all 96 c48x32 children. The 10 exact COMPLETE x16 children are immutable reusable evidence. Only the 38 node-cap x16 parents need refinement; each parent is the disjoint union of its two c48 mod32 children `s` and `s+16`, giving 76 new heavy jobs.

Firewalls remain:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
