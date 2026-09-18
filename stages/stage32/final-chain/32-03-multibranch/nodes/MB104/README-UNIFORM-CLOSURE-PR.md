# MB104 uniform-closure PR entrypoint

Ordinary `stage32mb-mainbatch` startup remains governed by `MAIN-START-HERE.md`. On this branch, the lane-local `STATE.json` has been advanced to `MB104` and points to this restart surface; MB103's retained result/certificate/verifier are copied locally so startup does not fall back to the archived #1791 branch.

After ordinary startup and resolution of the recorded live-MAIN authority drift, read:

1. `MB104-UNIFORM-CLOSURE-RESTART-20260917.md`
2. `MB104-UNIFORM-CLOSURE-ROUTE-UPDATE-20260917.md`
3. `MB104-U3-U4-U12-PORTFOLIO-GATE-20260917.md`
4. `MB104-U12-CONGRUENCE-CONTINUITY-GATE-20260917.md`
5. `MB104-U12-DYADIC-FRATTINI-SOURCE-WALL-20260918.md`
6. `MB104-U12-P6-VALUE-GATE-20260918.md`
7. `MB104-GLOBAL-REPLACEMENT-PORTFOLIO-EXHAUSTION-20260918.md`
8. `MB104-PR-SPLIT-MANIFEST-20260917.json`

Do not preload the archived `#1791` history. Fetch old MB104 artifacts only by the immutable exact head recorded in the restart ledger and only when a selected replacement-theorem route needs them.

Current research target: prove either an all-`l` exclusion for the exact balanced MB104 ray or a uniform `l>L` exclusion with explicit finite remainder `l<=L`.

Archive disposition: PR #1791 may be closed after this handoff, but `stage32mb-mainbatch-20260912` must remain available as the immutable historical archive. Do not merge #1791 and do not delete its archive branch under this handoff.

This PR carries no new mathematical credit and must remain small.
