# Stage32-18BG — repaired D16/B16 close evidence

Status: **HOSTILE AUDIT PASS**. Audit state: `stages/stage32/audits/32-18BG.json`.

This record supersedes the invalidated 32-18BB closure chain for D16/B16 bounded-computation evidence only. It grants `D16_B16_NUMERICAL_CREDIT=true`; it does not grant full D16-row, theorem, receiver, route-color, endpoint, B18, or perfect-cuboid existence/nonexistence credit.

## Scope and locks

- Kernel: `K16-C2-LOWGENUS-PICARD-PRODUCTION`
- Bound: `D16 / B16`
- Frozen cut39 parent namespace, shard count 1024, split coordinate 48
- Source exact artifact: `9574308138`
- Source exact artifact SHA256: `0671a8a8637641f5cc4da36b99700b1511c923d03e5ea446317d17b35bd88fc4`
- Repaired pairwise6 activation: only when `last_remaining < block_cut`
- Audited functional head: `9f0cab5aa290648094cfff5da55c1e32f29381f1`

## Prior hostile-audit failure

Review `5049175475` correctly rejected the old 18AY/AZ/BA/BB chain: pairwise6 executed before the cut39 parent was recorded, producing baseline `4103` versus pairwise `3893` on p436/s5 and losing 210 parents from the namespace. The exact Gram/KKT prune itself was mathematically safe, but the old frontier IDs could not certify the original baseline parents. Those old closure claims remain invalidated.

## Repaired audited chain

1. **18BC/G4 parent-stream identity.** Run `33155002856` compares baseline and repaired streams byte-for-byte on all six walls after moving pairwise strictly below cut39. Result: `PASSED_6_OF_6`. Frontier counts are p436-s5 `4103`, p436-s362 `3897`, p503-s118 `3596`, p503-s665 `3761`, p922-s13 `4095`, p922-s38 `4203`.

2. **18BC original 172 replay.** Final recovery run `33161746999`; summary artifact `9682227148`, SHA256 `2a5e24b16d6a4be83de7081f9f4bf009e9d2ff3bbf753fc2b0d1ec27ebfa0493`. Exact accounting: `172 = 22 complete + 150 residual`, selected IDs duplicate-free, zero timeout chunks.

3. **18BD residual-150 deep replay.** Run `33163638379`; summary artifact `9685982339`, SHA256 `096446e8d7b5d945d5f01194363b9c476c213d01976b7d3ce3c63965eeb35670`. The selected sequence is asserted equal to the exact 18BC residual sequence, chunk coverage is contiguous and duplicate-free, and `150 = 144 complete + 6 residual`. All timeout-chunk counts are zero. Residual parents are p436-s362 `[886]`, p436-s5 `[1914,1919]`, p503-s665 `[846]`, p922-s13 `[1200]`, p922-s38 `[1861]`.

4. **18BE six-parent child split.** Run `33174535334`; summary artifact `9687893070`, SHA256 `eb1a85f4a2e7e751c6b7de9aa30235f5083d94dba20849fc1bb11295bb393233`. It consumes exactly the six 18BD residual parents and enumerates each selected parent's actual feasible coordinate-39 DFS children. Four parents close; exactly two capped children remain: `p436-s362 / parent 886 / z39=0` and `p922-s13 / parent 1200 / z39=0`.

5. **18BF final two-child split.** Run `33179349822`; summary artifact `9689626245`, SHA256 `d8620591648f04b9c11e39bbcc772f483309b831ba243c1defcad2b71bae5ae1`. It consumes exactly those two children and enumerates their actual feasible coordinate-38 grandchildren. Parent 886 has 5/5 complete grandchildren; parent 1200 has 6/6. Unresolved grandchild total: `0`.

## Exact completion semantics

The frontier-cost planner marks a subtree complete only when its DFS returns without reaching the local probe budget. Reaching the budget sets `planner_probe_capped_=true` and therefore `complete=0`. While planner mode is active, the global traversal node cap is not used to manufacture completion. Missing/unprocessed rows remain unresolved, and shell timeouts fail the job rather than create successful completion evidence. The successful 18BD summary reports zero timeout chunks; all 18BE and 18BF child/deeper-child jobs completed successfully.

Therefore the repaired chain closes the original 172 baseline monster parents without a namespace shift, dropped/duplicated residual transfer, or timeout/node-cap/UNKNOWN promotion.

## Goal/stop contract metadata resolution

`stages/stage32/GOAL_AND_STOP_CONTRACT.md` is absent both at PR #1450's base (`dac08863c3e29ea8c3062a4dc8ff846fb83021a6`) and at the audited functional head. The reference is therefore a pre-existing stale controller reference, not a regression introduced by this PR. Repo-wide credit policy requires the active audited closure state but does not require this named file specifically.

This stale reference is **nonblocking for the D16/B16 bounded numerical audit**, but it remains a hard blocker for post-B16 downstream release until the controller reference is removed, repaired, or backed by an explicit contract. No B18 may be armed through this audit.

## Audited closure and firewalls

- `D16_B16_NUMERICAL_CREDIT = true`
- `FULL_D16_G0_ROW_COMPLETE = false`
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
- post-B16 downstream release = blocked until goal/stop metadata is resolved
- Stage32 closed = false

Audit verdict: `PASS_REPAIRED_BYTE_IDENTICAL_CUT39_NAMESPACE_EXACT_RESIDUAL_PARTITIONS_ZERO_UNRESOLVED`.
