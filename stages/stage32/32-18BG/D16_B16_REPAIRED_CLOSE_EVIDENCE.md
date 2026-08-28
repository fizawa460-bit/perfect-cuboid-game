# Stage32-18BG — repaired D16/B16 close evidence

Status: **PENDING HOSTILE AUDIT**. This record supersedes the invalidated 32-18BB closure chain for D16/B16 bounded-computation evidence only. It does not grant theorem, receiver, route-color, endpoint, or perfect-cuboid existence/nonexistence credit.

## Scope and locks

- Kernel: `K16-C2-LOWGENUS-PICARD-PRODUCTION`
- Bound: `D16 / B16`
- Frozen cut39 parent namespace, shard count 1024, split coordinate 48
- Source exact artifact: `9574308138`
- Source exact artifact SHA256: `0671a8a8637641f5cc4da36b99700b1511c923d03e5ea446317d17b35bd88fc4`
- Pairwise6 activation rule after repair: only when `last_remaining < block_cut`; it must not fire while the cut39 parent is being recorded.
- Automatic B18 or higher remains forbidden.

## Hostile-audit failure being repaired

Review `5049175475` rejected the prior 18AY/AZ/BA/BB closure chain because pairwise6 fired before the cut39 parent namespace was recorded. Independent replay found baseline `4103` parents versus pairwise6 `3893`, i.e. 210 baseline parents disappeared from the namespace. The Gram/KKT prune itself remained mathematically safe, but the old frontier IDs were not valid closure evidence for the baseline parent stream.

Therefore 18AY, 18AZ, 18BA, and 18BB retain no D16/B16 closure credit.

## Repaired evidence chain

1. **Parent-stream identity gate — 18BC/G4.** Run `33155002856` moved pairwise6 strictly below cut39 and independently compared baseline/repaired parent streams for all six remaining walls. Result: `PASSED_6_OF_6`, requiring byte-identical parent streams rather than count-only agreement.

2. **Original 172 replay in repaired namespace — 18BC/G5+G6.** G5 replayed the original 172 monster-parent selection in chunks; one environment-failed chunk was selectively recovered by G6 run `33161746999` without rerunning successful chunks. The final repaired-original-172 summary is artifact `9682227148`, SHA256 `2a5e24b16d6a4be83de7081f9f4bf009e9d2ff3bbf753fc2b0d1ec27ebfa0493`. It verifies exactly 172 distinct selected parents, `22` completed and `150` unresolved, under parent-stream identity `PASSED_6_OF_6`.

3. **Residual-150 deep replay — 18BD.** Run `33163638379` replayed only the 150 exact residual parent IDs at 2,000,000 probe nodes/state. Summary artifact `9685982339`, SHA256 `096446e8d7b5d945d5f01194363b9c476c213d01976b7d3ce3c63965eeb35670`. Result: `144/150` completed, six unresolved parents only.

4. **Residual-six child split — 18BE.** Run `33174535334` split only those six unresolved cut39 parents at coordinate39, retaining the frozen parent namespace. Summary artifact `9687893070`, SHA256 `eb1a85f4a2e7e751c6b7de9aa30235f5083d94dba20849fc1bb11295bb393233`. Result: four parents fully completed; two unresolved children remained, exactly `p436-s362 / parent 886 / z39=0` and `p922-s13 / parent 1200 / z39=0`.

5. **Final two-child deeper split — 18BF.** Run `33179349822` split only those two unresolved `z39=0` children at coordinate38, with 2,000,000 probe nodes per grandchild. Both jobs and summary succeeded. For parent 886, all 5 grandchildren completed; for parent 1200, all 6 grandchildren completed. Unresolved-grandchild total is `0`. Summary artifact `9689626245`, SHA256 `d8620591648f04b9c11e39bbcc772f483309b831ba243c1defcad2b71bae5ae1`.

## Coverage accounting

The repaired chain preserves one parent namespace throughout:

- original repaired monster parents: `172`
- 18BC completes `22`, transfers exactly `150`
- 18BD completes `144`, transfers exactly `6`
- 18BE completes `4` parents, transfers exactly `2` unresolved children
- 18BF completes those `2` children through exhaustive coordinate38 grandchildren (`5 + 6` grandchildren), leaving `0` unresolved

No already-completed repaired parent/child unit was intentionally rerun in later residual stages; each transition consumes only the explicitly recorded residual set from its immediate predecessor.

## Provisional closure statement

Within the certified D16/B16 bounded execution interface, the six previously remaining B16 walls now have zero unresolved states under the **repaired, baseline-identical cut39 parent namespace**. The bounded computational evidence needed to request a fresh hostile D16/B16 closure audit is complete.

This is not yet numerical credit. Successful Actions plus this evidence record remain provisional until the required hostile audit independently validates namespace identity, exact residual transfers, partition coverage, solver completion semantics, and artifact locks.

## Firewalls

- `D16_B16_NUMERICAL_CREDIT = false` pending hostile audit
- `FULL_D16_G0_ROW_COMPLETE = false` pending hostile audit / closure-scope determination
- `R29_LG2 = NOT_DISCHARGED`
- `R29_LG2_EFF = NOT_DISCHARGED`
- `R29_LG2_MB = NOT_DISCHARGED`
- `G10_LOWGENUS_PICARD = AMBER`
- theorem credit = false
- receiver credit = false
- route color change authorized = false
- perfect cuboid existence claim = false
- perfect cuboid nonexistence claim = false
- B18 release = forbidden

## Audit request

Fresh hostile audit should independently verify:

1. the G4 baseline/repaired cut39 stream is byte-identical on all six walls;
2. the original 172 IDs are interpreted in that repaired baseline namespace;
3. 18BC `22 + 150 = 172` with no dropped/duplicated parent IDs;
4. 18BD transfers exactly those 150 IDs and leaves exactly six;
5. 18BE consumes exactly those six parents and partitions each selected parent without omission/overlap;
6. 18BF consumes exactly the two recorded unresolved children and partitions them at coordinate38 without omission/overlap;
7. every reported `complete` is exact completion, not timeout/node-cap/UNKNOWN promotion;
8. all cited source/summary artifact IDs and SHA256 digests;
9. the bounded-computation scope remains separate from numerical-credit promotion, receiver/theorem credit, and endpoint claims;
10. controller metadata currently names `stages/stage32/GOAL_AND_STOP_CONTRACT.md`, but that path is absent on the branch; audit should determine whether this is stale metadata or a required missing contract before any downstream release.
