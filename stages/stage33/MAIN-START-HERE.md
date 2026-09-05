# Stage33 MAIN startup

For ordinary `Stage33-main-batch`, read only:

1. repo-root `AGENTS.md`;
2. this file;
3. `stages/stage33/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

`MAIN-STATE.json` is the single mutable ordinary-startup authority for the current Stage33 frontier, leaf, working set, anti-loop boundary, and firewalls. This file must not duplicate a version number, current mathematical frontier, current leaf, support vector, or batch progress.

The full `controller.json`, `RULES.md`, `HISTORY.md`, old roadmaps, compatibility shims, and cold evidence are not routine startup inputs. Expand to them only for a named reason required by the active leaf, a verifier, an audit, or a source-lock.

## Repository-read discipline

Repository traversal itself follows `AGENTS.md`.

For an existing weapon/evidence lookup or named expansion, the stable navigation order is:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

For ordinary startup, do not open controller/roadmap unless a named reason requires that expansion; follow `MAIN-STATE.current_leaf_working_set` first.

V58 remains the stable operational routing rule: Arsenal first, then repeatable bounded search only when each repeat has a materially new mathematical signal. Unbounded/open-ended search is forbidden, and a search miss never proves repository-wide or mathematical absence.

Do not preload Research OS. Open `docs/research-os/policies/repository-asset-discovery.md` only when the active `current_leaf_working_set` includes it or another explicit Research OS trigger applies.

## Promotion synchronization rule

A new Stage33 exact frontier is not operationally promoted until the same change updates:

- `MAIN-STATE.json`;
- `sync_main_state.py`;
- the current-frontier alignment verifier;
- any workflow entry that designates the live frontier.

Historical frontier verifiers remain retained as evidence but must not pin the live state backward.

## Writes and verification

After Stage33 MAIN writes, run at minimum:

- the active exact-frontier verifier named by the current workflow;
- `python stages/stage33/sync_main_state.py --check`;
- `git diff --check`.

Commit and push the same branch. Do not merge without explicit authorization.
