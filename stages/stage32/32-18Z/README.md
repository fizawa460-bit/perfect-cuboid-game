# Stage32-18Z — adaptive b16 c48x32 tail rescue

Stage32-18Y c48x16 completed 10 of 48 exact real-leaf children and isolated the remaining resource wall to 38 coordinate48 residue classes. This leaf preserves those 10 completed children and refines only the 38 node-cap parents.

For a fixed primary `h54 mod 1024` gate, an x16 secondary class `h48 mod 16 == s` is exactly the disjoint union of x32 classes `s` and `s+16`. Therefore each failed x16 parent is replaced by exactly two x32 children without changing the mathematical population.

Frozen 18Y source:

- workflow run `33030066426`;
- summary artifact `9631617459`;
- summary digest `sha256:3607380f62285a7c89919f0b184bceb296713b8a18fc7ae81f135e289f79c0f2`;
- COMPLETE x16 children: 10;
- node-cap x16 parents to rescue: 38;
- new x32 children: 76.

The immutable exact certifier remains prepared artifact `9626136705`, ZIP SHA256 `f706cd79cf1fc64da0a59bc5cc528ea677e3892f602d3f58d78cb1543bf8380c`. Bound remains 16, primary coordinate/modulus remains 54/1024, secondary coordinate remains 48, and the per-child node cap remains 18,000,000.

Execution safety:

- dedicated ARM-only run-key commit;
- `max-parallel: 15`, below the repository Stage ceiling 18;
- current nonexpired artifact usage plus worst-case new evidence must remain below 500MB;
- each new child artifact is capped at 1,000,000 uncompressed bytes with 7-day retention;
- node-cap, wallclock and artifact-size walls are explicit non-credit statuses.

The summary must independently reload the frozen 18Y artifacts, verify the exact 10-COMPLETE/38-wall pattern, and then reconstruct each failed x16 parent from its two x32 children. Only if all 16 logical secondaries of all three primaries are complete may the pilot declare the historical tail geometry production-ready.

Firewalls remain:

```text
D16_B16_NUMERICAL_CREDIT=false
GLOBAL_B16_AGGREGATION_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
