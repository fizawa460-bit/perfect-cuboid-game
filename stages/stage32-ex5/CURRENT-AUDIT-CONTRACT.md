# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. Merge is not authorized.

BC2-36 hostile audit **PASS** is consumed from exact head `9c63ccb48dd0e5bdeedda7739dd05e2404698465`, review `5188625406`. Its bounded EX5 authority is `11 UNSAT / 41 UNKNOWN / 0 SAT`, audited known parent-UNSAT lower bound `7295`, remaining UNKNOWN hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`.

## Active BC2-37 hostile-audit boundary

BC2-37 executed exactly the hostile-audited BC2-36 41-UNKNOWN set at `120000 ms` per parent, one heavy runner, no scaleout.

Execution receipt:

- execution head `52dfcb0ae986dac1b27998349feb97171c30be1b`
- workflow `34728149823`
- authorize job `103645902953`: SUCCESS / fresh-runkey
- compute job `103645956700`: SUCCESS
- artifact `10309795138`
- artifact ZIP sha256 `f3ab28efcbe4881f053fc5bbcaccd26fba44056d635603d6f3a05ed6a589fdc4`
- raw JSON sha256 `4dc7d7108b7edfc18a987e9f6a3574b323ce70d82b33444e4ef5c2955404b2aa`

Retained result to audit:

- `7 UNSAT / 34 UNKNOWN / 0 SAT`
- new UNSAT IDs `[1003,1016,1066,1198,2690,3160,4549]`
- remaining UNKNOWN IDs `[1014,1048,1050,1056,1103,1133,1206,1216,1218,1243,1251,1703,1706,1717,1719,1733,1798,1910,2092,2122,2187,2407,2634,2651,2817,2819,3205,3375,3635,3885,3901,3915,3980,4200]`
- remaining UNKNOWN hash `b2b0d1ef7d667fc380457818aa352e770f41fcdef7ca34c9ea88372c3193f891`
- status-stream sha256 `2f1bf300c7ec7a05975c2a4be5fb8d85deb4a40980e9daa12d7aec5adedf8f66`
- checkpoint canonical `286e40b0004b978cdbbc3829c600383c34a8bdc4e1492c54d99a2400258e37b7`
- checkpoint blob `6ac4592eded6be2bf80e88c33d0ac5944f13afaf`
- consumed/disarmed runkey blob `f23a9062f5211dbf0cd17dd6d9d14299551a8e51`
- retained verifier blob `744ef59e67baca75900dd25381107b35dbbf04c5`
- candidate lower bound `7302`
- audited lower bound remains `7295` until BC2-37 hostile-audit PASS.

`MAIN-STATE.json` must retain `new_audit_boundary_exists=true`, `freeze_active=true`, `re_audit_required=true`, and `bc2_37_execution_authorized=false`. BC2-37 heavy execution is retired; BC2-38 remains blocked.

Hostile audit must independently verify exact target partition, artifact/raw-result identity, source-lock chain through BC2-36/BC2-32/BC2-19/BC2-18, UNKNOWN preservation, consumed runkey, heavy-path retirement, state freeze, audited/candidate separation, and broad-credit firewalls.

A future BC2-37 hostile-audit PASS may advance only the bounded EX5 audited lower bound from `7295` to `7302` and release the explicit 34 UNKNOWN set for BC2-38. It cannot automatically grant whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid, or merge credit.

Next command: `stage32ex5-audit`.
