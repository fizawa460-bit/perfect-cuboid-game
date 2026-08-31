# Stage33 MAIN constitution — start here

This is the stable bootstrap contract for an ordinary `Stage33-main-batch`.
Its purpose is to reserve context for the live exact computation. It is not a
proof certificate, history log, or duplicate controller.

## Ordinary startup: bounded by default

After confirming the branch head with the GitHub connector, read only:

1. `AGENTS.md`
2. this file
3. `stages/stage33/MAIN-STATE.json`
4. only the immediate files named by `current_leaf_working_set`

Do not automatically read `RULES.md`, `CURRENT.md`, the full controller,
roadmaps, HISTORY, compatibility shims, old Stage33-05 state, ancestor results,
old PR diffs, or a directory-wide certificate set. `MAIN-STATE.json` is a
machine-checked projection of the detailed controller and current exact input.

If the compact state is absent or fails
`python stages/stage33/sync_main_state.py --check`, stop and repair the compact
state before mathematical work. Do not compensate by broadly rereading history.

## Authority and expansion

Repo-wide policy in `AGENTS.md` always applies. Detailed Stage33 authority is:

1. `RULES.md` for stable Stage33-only policy;
2. `controller.json` for detailed machine state;
3. active unit state and exact certificates for mathematical claims;
4. results, HISTORY, roadmaps, old states, and Git history for provenance.

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

## Writeback law

After a batch with repository writes:

1. update the detailed controller/result only if their state changed;
2. run `python stages/stage33/sync_main_state.py`;
3. run `python stages/stage33/sync_main_state.py --check` plus current-leaf
   verifier/replay and `git diff --check`;
4. commit and push the same branch unless the user forbids it.

Do not append live discoveries to this constitution. Change it only when the
startup/authority protocol itself changes. Mutable state belongs exclusively in
the generated compact state and detailed controller/evidence.
