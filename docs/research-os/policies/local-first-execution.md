# Local-first execution policy

Status: repository-wide, effective 2026-10-16. This policy takes precedence over any Stage-local controller, runkey, workflow, or older Research OS text that assumes GitHub Actions as the default execution or evidence surface. Stage-local files may be stricter; they may not be looser.

## 0. Why

In September 2026 the repository owner's GitHub account was suspended after GitHub flagged excessive Actions usage. The root cause was volume: on long-lived research PRs, every push re-ran several automatic workflows (for example, about 45 pushes on 2026-09-25 each triggered five workflows, and one integrity gate alone accumulated about four runner-hours that day). Access has been restored. The repository now runs **local-first**: research computation and verification happen on the owner's machine, and GitHub is used for storage, review, and a minimal set of cheap automatic safety gates.

## 1. Default execution surface: local

- Run verifiers, replays, pilots, and heavy computation locally (owner's PC: Windows + WSL Ubuntu; Python, PARI/GP; other free tools may be installed locally).
- Before every push, run the verifiers that the changed boundary depends on locally and record the result (command, exit status, and the key PASS lines) in the commit message, PR body, or a retained local-replay record (§4).
- Never push merely to "see what CI says". CI is not a debugger.
- Windows checkouts must use `git config core.autocrlf false` (and a working tree checked out with LF). Many verifiers compare `git hash-object` blob hashes against source locks; a CRLF working tree makes them fail spuriously. WSL checkouts are unaffected.
- `scripts/local_replay_workflow.py` replays the `run:` steps of a workflow locally and writes an exact-head local replay record (§5). Heavy steps behind gate outputs are evaluated from the gate's `$GITHUB_OUTPUT`, and unsupported `if:` expressions fail closed (the step is not run). A step consisting only of a pinned `pip install` is checked offline: it passes iff exactly the pinned versions are installed. For CI parity use an environment with the workflow's pinned Python and packages (for example a WSL Ubuntu venv); Windows text-mode writes can break byte-exact `cmp` replays.

## 2. Automatic workflows

- `ACTIVE_AUTO` is limited to this allowlist:
  - `.github/workflows/pages.yml` (site deploy on push to `main` only);
  - `.github/workflows/stage32-main-startup-authority.yml` (cheap Stage32 startup/authority gate);
  - `.github/workflows/stage32-claim-frontier-integrity.yml` (cheap workflow-inventory / claim-frontier gate).
- Every other workflow is `MANUAL` (`workflow_dispatch` only) or `RETIRED`. Adding a workflow to `ACTIVE_AUTO` requires explicit user approval recorded in the PR, plus an update of this list and of the inventory verifiers.
- New research workflows are created `MANUAL` by default; prefer a local script over a new workflow.
- The authoritative inventory is enforced by `verify_repo_workflow_trigger_inventory.py` and `verify_stage32_pr_workflow_trigger_inventory.py` in this directory.

### Long-lived branches

`pull_request` workflows run from the PR branch's own workflow files. An open PR branch created before this migration may still carry old automatic triggers. Before pushing to such a branch, first merge or cherry-pick this migration (or otherwise manualize the branch's workflows) in a single locally verified commit. Do not push further research commits to a branch whose workflow files still contain demoted automatic triggers.

## 3. Push discipline

- Batch work locally; push at meaningful checkpoints (for example, a frozen audit boundary or the end of a work session), not after every small commit.
- Target: at most a few pushes per PR per day. A burst of many consecutive pushes is a stop condition: pause and batch.
- Do not keep many long-lived PRs that receive frequent pushes at the same time.

## 4. Heavy computation

- Heavy computation runs locally by default, under the same resume-first discipline as `heavy-checkpoint-and-resume.md` (exact partition, per-unit certificates, carry-over, union verifier). Local checkpoints replace Actions artifacts.
- A heavy GitHub Actions run is allowed only when the user explicitly authorizes **that specific run** in the conversation/PR (the run key alone is not authorization). Such runs use `workflow_dispatch`, at most **2** effective concurrent heavy jobs for the whole repository, and the storage rules of `actions-storage-and-evidence-safety.md`.
- The older "<= 18 effective concurrent heavy jobs" ceiling is superseded by this stricter limit.

## 5. Evidence and hostile audit

- An exact-head **local replay record** is acceptable exact-head evidence wherever a policy, controller, or audit contract asks for "required exact-head CI" or a workflow run. The record must state: the exact commit SHA; a clean working tree (`git status` empty) or the precise diff; the commands run; the environment (OS, Python/PARI versions); the exit status; and the output digest or key PASS lines. Store it under the relevant Stage/leaf directory (for example, `LOCAL-REPLAY-<leaf>-<shortsha>.json` or `.md`).
- A hostile auditor may re-run the same commands locally to confirm. Missing or non-reproducible local evidence fails closed exactly as missing CI evidence would.
- Workflow-lifecycle audits verify the static trigger inventory with the two verifiers above; they no longer require "representative exact-head replay" of GitHub runs.
- This changes **where** evidence is produced, not what counts as proof. All research-credit, promotion, adapter, and hostile-audit firewalls remain unchanged.

## 6. Precedence

If an older rule requires an automatic workflow, an Actions run ID, or Actions artifacts as the only acceptable evidence, apply the local equivalent in §5 instead. If no local equivalent can be produced, stop and ask the user before arming Actions.
