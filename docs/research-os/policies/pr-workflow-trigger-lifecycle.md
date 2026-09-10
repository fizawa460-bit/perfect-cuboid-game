# Pull-request workflow trigger lifecycle

This policy defines lifecycle control for Stage-local and leaf GitHub Actions workflows.

## Principle

Research workflows may be created freely, but automatic pull-request triggering is a scarce repository resource. A workflow's existence does not imply that it should continue to run automatically after its leaf stops being active.

## Trigger classes

Every new or materially revised Stage-local workflow should be classified as one of:

- `ACTIVE_AUTO`: automatic PR execution is justified because the workflow guards the current active frontier or a repository-wide safety/authority boundary.
- `MANUAL`: retained and runnable through `workflow_dispatch`, but not automatically executed on ordinary PR synchronization.
- `RETIRED`: historical workflow retained for provenance or reproducibility; automatic PR execution is disabled.

If classification or active authority is unclear, use `MANUAL`.

## Frontier transition

When a Stage advances from one leaf to another, retire or demote the previous leaf's automatic PR trigger in the same retained transition, or before activating the successor's automatic trigger. Historical replay required for audit, repair, or source-lock verification should be invoked explicitly.

Repository-wide safety/authority gates, including Stage MAIN startup and claim/frontier integrity where applicable, may remain automatic independently of the active mathematical leaf.

## Cross-Stage behavior on long-lived PRs

The current repository policy prohibits automatic fan-out from `MANUAL` and `RETIRED` workflows. It does **not** require every `ACTIVE_AUTO` workflow to be branch-local.

Accordingly, a current `ACTIVE_AUTO` workflow may execute on a long-lived sibling PR when its automatic trigger and PR-wide path match apply there. This includes cross-Stage current-frontier or safety/authority workflows. Such execution is intentional under this policy and must be distinguished from the prohibited historical fan-out.

For replay evidence, always report both:

- total PR-triggered workflow runs at the exact head; and
- the subset attributable to `MANUAL` / `RETIRED` workflows.

A replay passes this lifecycle policy when the `MANUAL` / `RETIRED` automatic subset is zero. A nonzero total run count is not itself a lifecycle failure if every run is from the explicit `ACTIVE_AUTO` set.

If a future Stage requires branch-local-only execution for an `ACTIVE_AUTO` workflow, that restriction must be encoded as an additional trigger/gating rule; it is not implied by lifecycle classification alone.

## Why `paths` is insufficient

Do not use `pull_request.paths` as the only lifecycle control. GitHub evaluates pull-request path filters against the PR-wide changed-file set. On a long-lived PR, a historical path that was changed much earlier can continue to match when an unrelated later commit synchronizes the PR. The result is repeated re-execution of obsolete workflows.

Path filtering may still narrow an active workflow, but retirement from automatic PR execution must be explicit.

## Hostile-audit obligation

Workflow lifecycle compliance is part of hostile-audit scope whenever the audited PR changes workflow definitions, lifecycle policy, the active Stage frontier, or a long-lived PR's retained workflow surface. The audit must not treat a workflow as safely retired merely because prose says so.

A lifecycle audit must establish all of the following at the audited exact head:

1. the repository/branch inventory covers every reachable `.github/workflows/*.yml` and `.yaml` workflow in scope, with each classified as `ACTIVE_AUTO`, `MANUAL`, or `RETIRED`;
2. every `MANUAL` and `RETIRED` workflow is actually non-automatic — normally `workflow_dispatch`-only — and has no live `pull_request`, `pull_request_target`, schedule, push, or other unintended automatic event unless the governing policy explicitly authorizes that event;
3. every `ACTIVE_AUTO` workflow is an explicit allowlist member whose automatic role still corresponds to the current Stage frontier or a repository-wide safety/authority gate; a stale leaf may not remain automatic merely because it is present in an allowlist;
4. the lifecycle verifier/inventory is current against the exact workflow subtree and fails closed on an unclassified or stale path; and
5. representative exact-head replay evidence reports total automatic runs separately from `MANUAL`/`RETIRED` runs and shows `MANUAL`/`RETIRED` automatic runs = 0.

If any of these checks cannot be established from exact-head evidence, lifecycle audit credit fails closed. Job success/failure for an allowed `ACTIVE_AUTO` workflow remains separate from lifecycle correctness.

## Heavy workflows

This policy does not weaken the repository heavy-workflow authorization contract. A heavy workflow that is `ACTIVE_AUTO` must still remain behind its cheap run-key/authorization gate. Automatic trigger eligibility and heavy-compute authorization are separate gates.

## Existing-workflow repair

When this policy is introduced or repaired for a Stage, inventory the currently reachable Stage workflows and record their lifecycle class. Historical/retired/audited-consumed workflows must be changed in the repository, not merely described as manual. A policy-only change is insufficient if obsolete `pull_request` triggers remain live.
