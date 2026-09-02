# Stage33 MAIN startup

Ordinary `Stage33-main-batch` uses one compact current-state file. This file is
only the short routing contract; it is not mathematical state or history.

## Active recovery routing

The temporary `SEARCH_MODE_NAMED_J2_ORDER4_SOURCE` override is retired. It must
not be re-entered automatically.

The current recovery boundary is already saved in
`MAIN-STATE.json.work_checkpoint`. In particular, the recovered H1 coordinate
41 blocker and raw ct support `[9,11,19]` have an exact replay at:

- `stages/stage33/33-12/j2-recovered-mask6-h1-coordinate41-blocker.json`
- `stages/stage33/33-12/verify_j2_recovered_mask6_h1_coordinate41_blocker.py`

Do not search repo/PR/commit history again for those facts. The only remaining
unpromoted recovery datum is the source-first named order-4 quotient derivation
that had reached `(a,b)=(0,1)`, equivalently retained10 mask 6. That recovered
value is not source authority and does not select named J2.

Ordinary MAIN must now follow the checkpoint's narrow `next_action`: reconstruct
that source-first quotient derivation only from current locked leaf inputs. A
historical search may be reopened only if a current artifact supplies a new
exact file/commit identifier or the user explicitly requests historical
revalidation. Failure to replay the quotient derivation is a boundary to save,
not a reason to restart broad discovery.

## Startup

1. Confirm the live PR/branch/head with GitHub.
2. Read `AGENTS.md`.
3. Read `stages/stage33/MAIN-STATE.json`.
4. If `work_checkpoint.status == ACTIVE_UNPROMOTED`, follow its `next_action`
   and `anti_repeat` rules before expanding the working set.
5. Read only `current_leaf_working_set` plus any exact recovery artifact named
   by the checkpoint.

Do not routinely read the full controller, RULES, CURRENT, HISTORY, roadmaps,
old unit state, ancestor PRs, or broad certificate sets except when a source
lock/check fails, a load-bearing input is missing, authorities conflict,
audit/closure/heavy work requires it, or the user explicitly requests history.

## Durable work

`MAIN-STATE.json.work_checkpoint` is the only operational scratch checkpoint.
It is not proof authority. As soon as unpromoted work materially changes the
next action or anti-repeat boundary, save that checkpoint and commit it before
broadening further.

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
