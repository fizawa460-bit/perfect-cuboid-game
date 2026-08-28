# Stage32-18BB — provisional D16/B16 close evidence

Status: **PENDING HOSTILE AUDIT**. This file records the exact bounded-computation evidence chain only. It does not grant theorem, receiver, route-color, endpoint, or perfect-cuboid existence/nonexistence credit.

## Scope

- Kernel: `K16-C2-LOWGENUS-PICARD-PRODUCTION`
- Bound: `D16 / B16`
- Frozen parent partition: cut 39, shard count 1024, split coordinate 48
- Source exact artifact: `9574308138`
- Source artifact SHA256: `0671a8a8637641f5cc4da36b99700b1511c923d03e5ea446317d17b35bd88fc4`
- Automatic B18 or higher: forbidden

## Evidence chain

1. Six remaining B16 walls were calibrated at tier3 with 262144 nodes/state. The exact monster counts were `36,34,31,30,22,19`, total `172`.
2. Stage32-18AY compared parent-stable candidate algorithms on a 24-monster sample. Pairwise6 and pairwise12 both completed 24/24; pairwise6 used fewer than half the nodes and was selected without changing the frozen cut39 parent partition.
3. Stage32-18AZ, run `33151447281`, applied parent-stable pairwise6 to all 172 baseline monster parents at 262144 nodes/state. Result: `167/172` complete, five residual parents only. Summary artifact `9678028840`, SHA256 `9ec5ac2a6f8e520f23b96a7e029be264b451b37fdcba211bc61bc96d95f3e4c6`.
4. Residual IDs were exactly: `p436/s5: [724,728]`, `p436/s362: [1463]`, `p503/s118: [700]`, `p503/s665: [862]`; both p922 walls had no residual.
5. Stage32-18BA, run `33152432433`, replayed only those five frozen cut39 parents using the same pairwise6 semantics with a 2000000-node/state budget. All four jobs and the summary job succeeded. Result: `5/5` complete, `0` unresolved. Summary artifact `9678446245`, SHA256 `76a0f8c66c6b3b26461d58ab4d23d816e8cc51d196c9cedf4ea348a592ee58fa`.
6. 18BA exact per-wall node totals: p436/s5 `1004366`, p436/s362 `351846`, p503/s118 `362467`, p503/s665 `563424`. No residual parent requires child splitting.

## Provisional closure statement

Within the certified D16/B16 bounded execution interface, the six previously remaining B16 walls now have no unresolved cut39 parent states after the exact pairwise6 replay chain. The numerical-computation evidence needed to request D16/B16 closure audit is complete.

This statement is **provisional until hostile audit**. Per repository credit policy, successful Actions and this evidence record do not themselves authorize numerical-credit promotion or downstream release.

## Firewalls

- `D16_B16_NUMERICAL_CREDIT = false` pending audit
- `FULL_D16_G0_ROW_COMPLETE = false` pending audit/closure semantics
- `R29_LG2 = NOT_DISCHARGED`
- `R29_LG2_EFF = NOT_DISCHARGED`
- `R29_LG2_MB = NOT_DISCHARGED`
- `G10_LOWGENUS_PICARD = AMBER`
- theorem credit = false
- receiver credit = false
- route color change authorized = false
- perfect cuboid existence claim = false
- perfect cuboid nonexistence claim = false

## Audit request

Hostile audit should independently verify source locks, frozen parent-partition semantics, exact residual-ID transfer from 18AZ to 18BA, absence of dropped/duplicated states, `complete` interpretation, run/artifact digests, and the distinction between bounded numerical closure and theorem/receiver/endpoint credit.
