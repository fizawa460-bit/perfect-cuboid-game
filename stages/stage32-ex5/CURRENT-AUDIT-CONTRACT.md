# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. Merge is not authorized.

BC2-37 hostile audit **PASS** is consumed from exact head `9852fcec959962607da3290100291a60185e7104`, review `5189412496`. Its bounded EX5 authority is `7 UNSAT / 34 UNKNOWN / 0 SAT`, audited known parent-UNSAT lower bound `7302`, remaining UNKNOWN hash `b2b0d1ef7d667fc380457818aa352e770f41fcdef7ca34c9ea88372c3193f891`.

## Active BC2-38 hostile-audit boundary

BC2-38 executed exactly the hostile-audited BC2-37 34-UNKNOWN set at `140000 ms` per parent, one heavy runner, no scaleout.

Execution receipt:

- execution head `d26a27e8564458f3d575ec58601b2226fc23944f`
- workflow `34742297972`
- authorize job `103683927278`: SUCCESS / fresh-runkey
- compute job `103683975497`: SUCCESS
- artifact `10313851431`
- artifact ZIP sha256 `674c4deb7c2e13f654738278ad2108d40d3c4c463ae9f158a6cc438f10f65f01`
- raw JSON sha256 `2ac56238dd57989beebfd36a346074acd6ab57d497e692b16934203306a2b0e7`

Retained result to audit:

- `4 UNSAT / 30 UNKNOWN / 0 SAT`
- new UNSAT IDs `[1014,1133,1910,2817]`
- remaining UNKNOWN IDs `[1048,1050,1056,1103,1206,1216,1218,1243,1251,1703,1706,1717,1719,1733,1798,2092,2122,2187,2407,2634,2651,2819,3205,3375,3635,3885,3901,3915,3980,4200]`
- remaining UNKNOWN hash `d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7`
- status-stream sha256 `839233bb8552e4da7589616439cb614c07ceb018643f4f6d9bf3bf3f175fdeb5`
- checkpoint canonical `88b41680df6bb78f8b7f8ca00cde121d909a39e7b3c29eef765edb77b2c022ba`
- checkpoint blob `91eca02054cd2dbf702dd4a7635398ef76ee832f`
- consumed/disarmed runkey blob `87855350c6240cd524069490f85858b11099da60`
- retained verifier blob `934f19363549d652c18b02934c1f963a19204664`
- candidate lower bound `7306`
- audited lower bound remains `7302` until BC2-38 hostile-audit PASS.

`MAIN-STATE.json` must retain `new_audit_boundary_exists=true`, `freeze_active=true`, `re_audit_required=true`, and `bc2_38_execution_authorized=false`. BC2-38 heavy execution is retired; BC2-39 remains blocked.

Hostile audit must independently verify exact target partition, artifact/raw-result identity, source-lock chain through BC2-37/BC2-32/BC2-19/BC2-18, UNKNOWN preservation, consumed runkey, heavy-path retirement, state freeze, audited/candidate separation, and broad-credit firewalls.

A future BC2-38 hostile-audit PASS may advance only the bounded EX5 audited lower bound from `7302` to `7306` and release the explicit 30 UNKNOWN set for BC2-39. It cannot automatically grant whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid, or merge credit.

Next command: `stage32ex5-audit`.
