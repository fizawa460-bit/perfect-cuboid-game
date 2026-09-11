# Research OS

Reusable repository-wide research-process policies and lightweight research-mission templates. Do not preload this directory during ordinary Stage startup; follow the Stage-local startup contract first and open only the policy or template required by the active trigger.

## Trigger router

- Context-heavy repository file inspection, unknown file size, encoded/compressed/minified/opaque payload, or permanent denylist hit -> `policies/context-safe-file-inspection.md`
- Artifact-producing/heavy workflow design, revision, authorization, rerun, or diagnosis -> `policies/actions-storage-and-evidence-safety.md`
- Research-credit promotion, revocation, hostile audit, or load-bearing semantic/adapter question -> `policies/research-credit-and-promotion-firewalls.md`
- Existing weapon/evidence lookup or catalog maintenance -> `policies/repository-asset-discovery.md`
- Route broadening, parking, domination, reopening, or exhaustion decision -> `policies/cycle-exploration-safety-protocol.md`
- Self-contained final mathematical review artifact -> `policies/self-contained-review-standard.md`
- Bounded Codex task scope/stop decision -> `policies/codex-task-scope-stop-policy.md`

Read one matching policy first. Do not recursively load the other policies unless that policy or the active Stage contract makes another trigger load-bearing.

## Reusable mission template

For a new Stage32EX-style research program with dependency-DAG decomposition, search-before-create reuse, blocked-route memory, derived open frontier, and bounded multi-agent parallelism, use:

`templates/mission-dag/`

The human-facing interface is intentionally small:

- `research-start <mission>: <target>` — instantiate and lock the first mission target;
- `<mission>-mainbatch` — continue from the derived READY frontier while avoiding duplicate nodes and unchanged blocked routes;
- `<mission>-audit` — separate exact-head hostile audit at a retained checkpoint.

The template does not duplicate all Research OS policy text. It invokes the existing policies only when their trigger becomes load-bearing.
