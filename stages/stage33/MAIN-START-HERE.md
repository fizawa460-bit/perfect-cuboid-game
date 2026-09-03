# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Synchronized post-V36 authority

`controller.json` V59 and `sync_main_state.py` are synchronized to the exact V25-V36 certificate chain. `MAIN-STATE.json` V16 is generated from that controller. V37 is a superseded operational repair receipt; V38 records completion of the synchronization and grants no mathematical credit.

V36 remains the exact stop: J2-adapted Kummer columns are `1/10`, original standard columns are `0/10`. Do not restart broad origin/history search, split standard col2/col3 from the XOR relation, or guess a remaining column. Proceed only if a V25-V36 source lock fails, a new genuine full-surface H2(mu2) lift is supplied, a newly registered positive evidence asset source-locks a remaining adapted source, or historical revalidation/audit is explicitly requested.

`MAIN-STATE.json.work_checkpoint` is operational scratch only and is currently `EMPTY`. After legitimate exact-state changes, update controller/certificates coherently and regenerate `MAIN-STATE.json`.

`MAIN-BATCH-HANDOFF.md` is retired and must not be recreated.

After writes, run the current-leaf verifier, `python stages/stage33/sync_main_state.py --check`, and `git diff --check`. Commit and push the same branch. Do not merge without explicit authorization.
