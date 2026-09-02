# Stage33 MAIN startup

Ordinary `Stage33-main-batch` uses one compact current-state file. This file is
only the short routing contract; it is not mathematical state or history.

## Startup

1. Confirm the live PR/branch/head with GitHub.
2. Read `AGENTS.md`.
3. Read `stages/stage33/MAIN-STATE.json`.
4. If `work_checkpoint.status == ACTIVE_UNPROMOTED`, execute its
   `current_action` subject to its `anti_repeat` rules.
5. Read only `current_leaf_working_set` plus any exact artifact named by the
   checkpoint.

`current_action` is the work to do now from the live remote head.

Do not routinely read the full controller, RULES, CURRENT, HISTORY, roadmaps,
old unit state, ancestor PRs, or broad certificate sets except when a source
lock/check fails, a load-bearing input is missing, authorities conflict,
audit/closure/heavy work requires it, or the user explicitly requests history.

## Durable work

`MAIN-STATE.json.work_checkpoint` is the only operational scratch checkpoint.
It is not proof authority. As soon as unpromoted work materially changes the
current action or anti-repeat boundary, save that checkpoint and commit it
before broadening further.

Exact progress belongs in certificates/controller. After exact state changes,
run `sync_main_state.py`; it preserves `work_checkpoint`. Clear the checkpoint
only after its content is fully promoted, or replace it with the corrected
narrow blocker if replay rejects it.

`MAIN-BATCH-HANDOFF.md` is retired and must not be recreated.

## Completion

A checkpoint is a durability mechanism, not a new mathematical stop condition.
Continue MAIN until exact progress is materialized, a Stage33/Research-OS stop
condition is reached, or a real tool/permission/resource boundary ends the turn.

Before completion after writes, run `python stages/stage33/sync_main_state.py --check`,
the current-leaf verifier/replay as applicable, and `git diff --check`; commit
and push the same branch unless explicitly forbidden. Never merge without
explicit authorization.
