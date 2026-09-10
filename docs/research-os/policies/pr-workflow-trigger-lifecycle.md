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

## Why `paths` is insufficient

Do not use `pull_request.paths` as the only lifecycle control. GitHub evaluates pull-request path filters against the PR-wide changed-file set. On a long-lived PR, a historical path that was changed much earlier can continue to match when an unrelated later commit synchronizes the PR. The result is repeated re-execution of obsolete workflows.

Path filtering may still narrow an active workflow, but retirement from automatic PR execution must be explicit.

## Heavy workflows

This policy does not weaken the repository heavy-workflow authorization contract. A heavy workflow that is `ACTIVE_AUTO` must still remain behind its cheap run-key/authorization gate. Automatic trigger eligibility and heavy-compute authorization are separate gates.

## Existing-workflow repair

When this policy is introduced or repaired for a Stage, inventory the currently reachable Stage workflows and record their lifecycle class. Historical/retired/audited-consumed workflows must be changed in the repository, not merely described as manual. A policy-only change is insufficient if obsolete `pull_request` triggers remain live.
