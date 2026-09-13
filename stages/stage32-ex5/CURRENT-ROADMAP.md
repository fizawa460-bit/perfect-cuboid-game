# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged. Merge is not authorized.

BC2-36 hostile audit **PASS** is consumed from exact head `9c63ccb48dd0e5bdeedda7739dd05e2404698465`, review `5188625406`. Its audited lower bound is `7295`, with exact remaining-41 hash `570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9`.

BC2-37 has completed and is now frozen for hostile audit:

- execution head `52dfcb0ae986dac1b27998349feb97171c30be1b`
- workflow `34728149823`
- authorizer job `103645902953`
- compute job `103645956700`
- artifact `10309795138`
- artifact ZIP sha256 `f3ab28efcbe4881f053fc5bbcaccd26fba44056d635603d6f3a05ed6a589fdc4`
- raw JSON sha256 `4dc7d7108b7edfc18a987e9f6a3574b323ce70d82b33444e4ef5c2955404b2aa`
- retained checkpoint canonical `286e40b0004b978cdbbc3829c600383c34a8bdc4e1492c54d99a2400258e37b7`
- retained checkpoint blob `6ac4592eded6be2bf80e88c33d0ac5944f13afaf`
- consumed/disarmed runkey blob `f23a9062f5211dbf0cd17dd6d9d14299551a8e51`
- retained verifier blob `744ef59e67baca75900dd25381107b35dbbf04c5`
- exact result `7 UNSAT / 34 UNKNOWN / 0 SAT`
- remaining UNKNOWN hash `b2b0d1ef7d667fc380457818aa352e770f41fcdef7ca34c9ea88372c3193f891`
- status-stream sha256 `2f1bf300c7ec7a05975c2a4be5fb8d85deb4a40980e9daa12d7aec5adedf8f66`
- candidate lower bound `7302`
- audited lower bound remains `7295` until hostile audit PASS.

BC2-37 heavy authorization/execution is retired. The active route is `HOSTILE_AUDIT_BC2_37_TARGETED_REPLAY`; BC2-38 remains blocked until exact-head hostile audit PASS. UNKNOWN remains UNKNOWN.

No whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid, heavy-scaleout, or merge credit follows automatically.

Next command: `stage32ex5-audit`.
