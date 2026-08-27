# Stage32-18Y — b16 c48x16 tail-geometry pilot

Stage32-18X tested the three historical b14 tail primaries `436`, `503`, and `922` at bound16 using a coordinate48 eight-way secondary split. Generation 3 completed cleanly as evidence, but all `24/24` logical children hit the exact `18,000,000` node cap. Therefore x8 is too coarse.

18Y keeps every mathematical source lock and gate fixed and changes only the execution partition geometry:

- primary coordinate/modulus: `54 / 1024`;
- primary residues: `[436,503,922]`;
- secondary coordinate: `48`;
- secondary shard count: `16`;
- logical children: `48`;
- exact traversal node cap: `18,000,000` per child;
- max concurrent heavy jobs: `15`.

The prepared exact certifier remains immutable from artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`. Each child preserves exact rational branch rejection, the 256 DFS symmetry breakers, and Aut order `1536`.

Operational safety is part of the ARM gate. Before heavy jobs start, the workflow sums current nonexpired repository Actions artifacts and requires current usage plus the capped worst-case 18Y artifact peak to stay below the repository 500MB budget. Child artifacts are capped at 4,000,000 uncompressed bytes and retained for 7 days; a larger exact output is recorded as an artifact-size resource wall rather than silently exceeding the storage plan. Effective Stage32 parallelism is statically fixed at 15, below the repo ceiling of 18.

If all 16 children of every primary complete, the summary independently checks source locks, duplicate freedom, histogram equality and the exact sorted union for each primary. Any node-cap, wallclock or artifact-size wall routes to a finer partition without numerical credit.

Firewalls:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
