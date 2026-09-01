# Stage33 MAIN constitution — start here

This is the stable bootstrap contract for an ordinary `Stage33-main-batch`.
Its purpose is to reserve context for the live exact computation. It is not a
proof certificate, history log, or duplicate controller.

## Ordinary startup: bounded by default

After confirming the branch head with the GitHub connector, read only:

1. `AGENTS.md`
2. this file
3. `stages/stage33/MAIN-STATE.json`
4. `stages/stage33/MAIN-BATCH-HANDOFF.md`
5. only the immediate files named by `current_leaf_working_set`

`MAIN-BATCH-HANDOFF.md` is a small mandatory continuation note. It records the
latest narrowing, failed routes, and immediate next action even when the exact
mathematical state was not promoted. Read it before expanding the working set so
that an ordinary MAIN batch does not redo the previous batch's search.

Do not automatically read `RULES.md`, `CURRENT.md`, the full controller,
roadmaps, HISTORY, compatibility shims, old Stage33-05 state, ancestor results,
old PR diffs, or a directory-wide certificate set. `MAIN-STATE.json` is a
machine-checked projection of the detailed controller and current exact input.

Before expanding beyond that set, inspect `resolved_investigations` and
`anti_loop_reopen_policy` in `MAIN-STATE.json`, plus the anti-repeat section of
`MAIN-BATCH-HANDOFF.md`. An item marked resolved or as a prohibited shortcut
MUST NOT be reinvestigated in an ordinary MAIN batch while its listed source
lock still matches. Reopen it only under a listed reopen condition. Human memory
is never required to stop a repeated investigation.

If the compact state is absent or fails
`python stages/stage33/sync_main_state.py --check`, stop and repair the compact
state before mathematical work. Do not compensate by broadly rereading history.

## Authority and expansion

Repo-wide policy in `AGENTS.md` always applies. Detailed Stage33 authority is:

1. `RULES.md` for stable Stage33-only policy;
2. `controller.json` for detailed machine state;
3. active unit state and exact certificates for mathematical claims;
4. results, HISTORY, roadmaps, old states, and Git history for provenance.

`MAIN-BATCH-HANDOFF.md` is operational memory only. It does not promote a claim
and never overrides an exact certificate or machine authority.

Expand beyond the ordinary working set only for one named reason:

- a source lock or compact-state check fails;
- the current proof needs a load-bearing matrix/representative not exported by
  the compact interface;
- two authoritative certificates contradict each other;
- hostile audit, closure/release, heavy compute, or claim promotion is actually
  being performed;
- the user explicitly asks for audit or history.

State the reason, open the smallest relevant source, and return to the compact
working set afterward. Never reload a closed ancestor merely for reassurance.

## MAIN behavior

- Advance the exact leaf in `MAIN-STATE.json`; do not spend the batch rebuilding
  the full Stage33 narrative.
- Reuse source-locked exact interfaces. If identities differ, construct an
  explicit adapter instead of silently transferring credit.
- Keep unknown data explicit. No guessed coordinate, zero column, representative,
  descent, closure, or endpoint claim.
- Compatibility files are historical shims and are never routine startup input.
- Before Actions/heavy compute, claim promotion, closure/release, or hostile
  audit, load the specific policy and detailed authority required by that trigger.
- Before ending any MAIN batch that learned a useful narrowing, failed route,
  blocker, or next action, overwrite `MAIN-BATCH-HANDOFF.md` with that result.
  This is required even when no theorem-facing state or controller field changes.

## Writeback law

After a batch with repository writes:

1. update the detailed controller/result only if their state changed;
2. update `stages/stage33/MAIN-BATCH-HANDOFF.md` with the latest compact
   continuation note, including exact known facts, routes not to repeat, and the
   immediate next action;
3. run `python stages/stage33/sync_main_state.py` when detailed state changed;
4. run `python stages/stage33/sync_main_state.py --check` plus current-leaf
   verifier/replay and `git diff --check` as applicable;
5. commit and push the same branch unless the user forbids it.

Do not append live discoveries to this constitution. Change it only when the
startup/authority protocol itself changes. Mutable mathematical state belongs in
the generated compact state and detailed controller/evidence; the batch handoff
is only the bounded operational continuation note.