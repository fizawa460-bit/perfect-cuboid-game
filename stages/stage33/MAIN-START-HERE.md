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

This ordered list is the **sole routine startup enumeration authority**. Other
Stage33 files may point here but must not maintain a competing copy of the list.

Out-of-repo conversation notes or inherited prompt/handoff text are operational
hints, not durable Stage33 policy. In particular, branch/PR restrictions from
such notes MUST be revalidated against live GitHub state and current repository
authority when their referent may have changed; stale notes never become
permanent policy by repetition.

`MAIN-BATCH-HANDOFF.md` is a **transient delta note only**. It may contain only
useful narrowing/blockers learned after the mathematical state represented by
`MAIN-STATE.json`. It MUST NOT recap facts already exported by `MAIN-STATE.json`,
repeat old certificates, reconstruct prior conversations, or become a second
state file.

If the handoff status is `EMPTY`, consume no history from it: continue directly
from `MAIN-STATE.json`. If non-empty, read only its current unresolved delta and
immediate next action.

Do not automatically read `RULES.md`, `CURRENT.md`, the full controller,
roadmaps, HISTORY, compatibility shims, old Stage33-05 state, ancestor results,
old PR diffs, or a directory-wide certificate set. `MAIN-STATE.json` is a
machine-checked projection of the detailed controller and current exact input.

Before expanding beyond that set, inspect `resolved_investigations` and
`anti_loop_reopen_policy` in `MAIN-STATE.json`, plus any current anti-repeat item
in the transient handoff. An item marked resolved or as a prohibited shortcut
MUST NOT be reinvestigated in an ordinary MAIN batch while its listed source
lock still matches. Reopen it only under a listed reopen condition. Human memory
is never required to stop a repeated investigation.

A resolved-investigation or “do not reinvestigate” rule is therefore scoped to
the **same effective premises**: the same locked inputs, basis/conventions, and
source/target/interface meaning. A mere state promotion does not reopen it.
However, if a new proof, adapter, basis, source/target definition, or other exact
change materially alters premises on which that investigation depended, MAIN may
re-evaluate only the affected item under the new premises. That is a new
interface question, not permission to rerun the old investigation unchanged.

If the compact state is absent or fails
`python stages/stage33/sync_main_state.py --check`, stop and repair the compact
state before mathematical work. Do not compensate by broadly rereading history.

## Authority and expansion

Repo-wide policy in `AGENTS.md` always applies. Detailed Stage33 authority is:

1. `RULES.md` for stable Stage33-only policy;
2. `controller.json` for detailed machine state;
3. active unit state and exact certificates for mathematical claims;
4. results, HISTORY, roadmaps, old states, and Git history for provenance.

`MAIN-BATCH-HANDOFF.md` is operational scratch memory only. It does not promote
a claim and never overrides an exact certificate or machine authority.

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
- Before ending a MAIN batch, write only genuinely unpromoted narrowing/blockers
  to `MAIN-BATCH-HANDOFF.md`. Do not copy current mathematical state into it.

## MAIN batch completion gate

`Stage33-main-batch` is a work unit, not a single-observation or short-status
unit. After compact startup, continue the current exact leaf until one of these
conditions is reached:

- exact progress is promoted/materialized and the required state/writeback is
  complete;
- an exact blocker is materially narrowed with durable evidence and the latest
  unresolved delta/next action is committed to `MAIN-BATCH-HANDOFF.md`;
- a real permission, safety, tool, or external dependency boundary prevents
  further progress in the current turn.

Do NOT end a MAIN batch merely because an intermediate diagnostic was found, a
search target was narrowed, several tool calls elapsed, or a plausible next step
became visible. If an exploration changes the blocker or next action but is not
promoted state, that change is itself an unpromoted delta and MUST be written to
the handoff before the user-visible batch completion response.

The user must not be required to remind MAIN to continue, commit durable work,
or update/reset the handoff. Those are part of the batch completion condition.

## Mandatory handoff reset law

Whenever a batch promotes mathematical progress into exact certificates and the
detailed state, then successfully synchronizes `MAIN-STATE.json`, the handoff
MUST be reset in the same batch.

Reset means:

- remove every fact now represented by certificates/controller/`MAIN-STATE.json`;
- set the handoff to `EMPTY` if no post-promotion unresolved delta remains;
- if more work happened after the promotion, record only that new post-promotion
  delta, never the promoted material;
- never carry a previous batch narrative forward merely for convenience.

The handoff should stay tiny (target: under about 60 lines). If it starts looking
like a conversation summary, it is being used incorrectly.

## Writeback law

After a batch with repository writes:

1. update the detailed controller/result only if their state changed;
2. run `python stages/stage33/sync_main_state.py` when detailed state changed;
3. after a successful state sync, immediately reset `MAIN-BATCH-HANDOFF.md` under
   the mandatory reset law above;
4. if no mathematical state promotion occurred, overwrite the handoff with only
   the latest unresolved delta/blocker/next action;
5. run `python stages/stage33/sync_main_state.py --check` plus current-leaf
   verifier/replay and `git diff --check` as applicable;
6. commit and push the same branch unless the user forbids it.

Do not append live discoveries to this constitution. Change it only when the
startup/authority protocol itself changes. Mutable mathematical state belongs in
the generated compact state and detailed controller/evidence; the batch handoff
is disposable scratch state only.
