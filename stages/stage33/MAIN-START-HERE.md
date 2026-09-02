# Stage33 MAIN startup

Ordinary `Stage33-main-batch` uses one compact current-state file. This file is
only the short routing contract; it is not mathematical state or history.

## Active operational override

Until explicitly cleared after the source search succeeds or is exhausted,
ordinary `Stage33-main-batch` starts in `SEARCH_MODE_NAMED_J2_ORDER4_SOURCE`.
This is an operational routing override requested by the user on 2026-09-02;
it is NOT mathematical authority and does not promote mask 6 or close Stage33-12.

Search target, in priority order:

1. a source-locked named J2 order-4 lift `t1/4` with actual `swap12/swap13`
   behavior;
2. an equivalent source-locked two-bit quotient value `(a,b)`;
3. source material sufficient to reconstruct either of those, especially the
   labeled index512 glue, marked NS-T discriminant anti-isometry, or the
   source-locked 2x14 J2 pullback adapter.

Use the saved H1 coordinate 41 mismatch and raw ct support `[9,11,19]` as search
anchors, not as proof authority. It is now permitted to expand into repo/PR/
commit history specifically to find the missing source. Do NOT redo already
closed mathematics merely because history is being searched: rows 20/67,
qPic/Smith, sign census, S3 candidate enumeration, correction/half-lift
enumeration, and the four-mask two-bit enumeration remain closed unless a
located source actually invalidates a locked input.

For this active override, the SEARCH_MODE instruction supersedes only the
`work_checkpoint.next_action` that previously prioritized the smallest H1-41
replay. All mathematical firewalls, nonclaims, and source-lock requirements in
`MAIN-STATE.json` remain authoritative. Persist meaningful search narrowing in
`MAIN-STATE.json.work_checkpoint` before the turn ends so the same search is not
repeated in a later chat.

## Startup

1. Confirm the live PR/branch/head with GitHub.
2. Read `AGENTS.md`.
3. Read `stages/stage33/MAIN-STATE.json`.
4. Apply the active operational override above before interpreting
   `work_checkpoint.next_action`.
5. Read only the files in `current_leaf_working_set`; then expand only as needed
   for the targeted source search above.

Do not routinely read the full controller, RULES, CURRENT, HISTORY, roadmaps,
old unit state, ancestor PRs, or broad certificate sets except as specifically
needed by the active targeted source search, or when a source lock/check fails,
a load-bearing input is missing, authorities conflict, audit/closure/heavy work
requires it, or the user explicitly requests history.

## Durable work

`MAIN-STATE.json.work_checkpoint` is the only operational scratch checkpoint.
It is not proof authority. As soon as unpromoted work materially changes the
next action, search boundary, or anti-repeat boundary, save that checkpoint and
commit it before broadening further. Do not keep such progress only in chat.

Exact progress belongs in certificates/controller. After exact state changes,
run `sync_main_state.py`; it preserves `work_checkpoint`. Clear the checkpoint
only after its content is fully promoted, or replace it with the corrected
narrow blocker/search state if replay or source inspection rejects it.

`MAIN-BATCH-HANDOFF.md` is retired and must not be recreated.

## Completion

A checkpoint is a durability mechanism, not a new mathematical stop condition.
Continue MAIN until exact progress is materialized, a Stage33/Research-OS stop
condition is reached, or a real tool/permission/resource boundary ends the turn.

Before completion after writes, run `python stages/stage33/sync_main_state.py --check`,
the current-leaf verifier/replay as applicable, and `git diff --check`; commit
and push the same branch unless explicitly forbidden. Never merge without
explicit authorization.
