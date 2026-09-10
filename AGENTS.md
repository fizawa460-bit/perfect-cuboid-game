# Repository agent instructions

Keep this root file small. Stage-specific startup, history, and operating detail belong in the Stage entrypoint/state; reusable research-process detail belongs under `docs/research-os/`.

During ordinary Stage startup, do not preload Research OS. Follow the Stage-local startup contract and open Research OS only on the explicit triggers below.

## Repository traversal discipline

Repository discovery is search-first, not tree-first. **Never acquire a recursive/full repository tree, and never call a recursive tree endpoint (including `recursive=1`) for discovery, exhaustive enumeration, or as a fallback after any search miss. There is no Stage/task exception to this rule.** Fetch known paths directly; use GitHub search for filenames/paths and GitHub code search for terms, symbols, identifiers, or phrases; follow controller, roadmap, source-lock, certificate, index, or other authority references only to the exact targets needed for the active leaf. If exhaustive enumeration is genuinely required, use bounded/paginated targeted search, explicit non-recursive directory traversal, or a task-specific repository index instead; if those mechanisms cannot establish exhaustive coverage, stop and record that limitation rather than requesting a recursive/full tree. A search miss never proves repository-wide absence; broaden only under the active Stage/search policy.

## Context-safe file inspection

Before any whole-file read, establish byte size from metadata without reading the target contents. Unknown size is unsafe; files `>= 65536` bytes must not be whole-fetched into assistant/chat context. **Size alone is not sufficient:** generated, encoded, compressed, minified, binary-like, single-line, or opaque-payload files must be handled through compact repo-side loaders/adapters/verifiers or bounded structured output. Do not use line-range fetching to bypass this rule and never expand Base64/Base85/compressed retained payloads into context merely to inspect them.

Permanent whole-fetch denylist:
- `stages/stage33/33-07/picard_base_rows_retained.py`
- `stages/stage33/33-07/stage32_picard_marking_retained.py`

- **On-demand trigger:** open `docs/research-os/policies/context-safe-file-inspection.md` before inspecting a file when size/representation may be context-heavy, or whenever one of the denylisted files is relevant.

## Repo-wide Actions safety

- Treat GitHub Actions artifact/storage capacity as a hard execution constraint. The repository operating budget is **500 MB** unless explicitly revised.
- Before artifact-producing compute, conservatively preflight peak stored footprint. For a new high-mass workflow, measure a representative shard before scaling.
- Keep raw exhaustive evidence runner-local when possible; persist compact deterministic certificates only after verification. Use bounded waves and short retention for necessary intermediates.
- Storage risk, upload failure, or materially larger-than-estimated artifacts are stop/cancel conditions. Do not trade mathematical exactness for storage.
- **On-demand trigger:** open `docs/research-os/policies/actions-storage-and-evidence-safety.md` only when designing, materially revising, authorizing, rerunning, or diagnosing an artifact-producing/heavy workflow.

## Pull-request workflow trigger lifecycle

Stage-local or leaf workflows may be created freely for research verification, but creating a workflow does **not** grant permission to leave it on an automatic PR trigger indefinitely.

- Automatic `pull_request` / `pull_request_target` triggers are reserved for the current **ACTIVE frontier** and repository-wide safety/authority gates such as MAIN startup and claim/frontier integrity.
- `RETIRED`, `HISTORICAL`, or `AUDITED-CONSUMED` leaf workflows must default to manual execution (`workflow_dispatch`) unless the active Stage controller explicitly keeps them automatic.
- When the active frontier advances, retire the previous leaf's automatic PR trigger in the same transition, or before enabling the next leaf's automatic trigger.
- Every new or materially revised Stage-local workflow must classify its trigger lifecycle as `ACTIVE_AUTO`, `MANUAL`, or `RETIRED`; if the class or active authority is unclear, fail closed to `MANUAL`.
- Cross-Stage execution by a current `ACTIVE_AUTO` workflow on a long-lived sibling PR is permitted when its automatic trigger/path conditions match. Lifecycle replay must report total runs separately from `MANUAL`/`RETIRED` runs; the prohibited historical/manual fan-out is the latter, not all nonzero automatic execution.
- Hostile audit of workflow/lifecycle/frontier changes must independently verify the exact-head inventory and trigger classes: `MANUAL`/`RETIRED` must have no unintended automatic event, `ACTIVE_AUTO` must still map to the current frontier or a repository-wide safety/authority gate, the verifier must be current/fail-closed, and representative exact-head replay must show `MANUAL`/`RETIRED` automatic runs = 0. Prose-only retirement is not audit evidence.
- Do **not** rely on `pull_request.paths` alone as workflow-lifecycle control. On long-lived PRs GitHub evaluates path filters against the PR-wide changed-file set, so historical workflow paths may re-match on unrelated later synchronizations.
- A historical replay needed for audit, repair, or source-lock verification should be invoked explicitly rather than kept permanently auto-triggered.
- **On-demand trigger:** open `docs/research-os/policies/pr-workflow-trigger-lifecycle.md` when adding or materially revising a Stage workflow, changing the active frontier, retiring/consuming a leaf, diagnosing repeated PR-triggered Actions runs, or auditing workflow lifecycle compliance.

## Heavy workflow rerun authorization

Heavy PR workflows must not rerun merely because a PR was synchronized, reopened, or docs/controller/status/source files changed. Every heavy job must remain behind a cheap authorization gate and run only when its dedicated run key is explicitly and semantically advanced/armed in the triggering commit range. If authorization cannot be verified, fail closed and skip heavy compute.

## Research credit and claim promotion

- finite/bounded/sample evidence is not a global theorem;
- computational, numerical, receiver, theorem, effectivity/existence, and endpoint credit stay distinct;
- changes of population, measure, field, quotient, model, mask, height, multiplicity, or other semantics require an exact adapter;
- do not double-charge a restriction/saving or assume independence without proof;
- formal classes/orbits/cohomology do not by themselves prove existence of the required geometric object;
- only the active controller's required audited closure releases downstream credit, and hostile audit may revoke it;
- a blocked route or finite zero hit is not impossibility;
- never claim perfect-cuboid existence/nonexistence without an explicit audited full-endpoint certificate.

Stage-local controllers may strengthen these firewalls but must not weaken them.

- **On-demand trigger:** open `docs/research-os/policies/research-credit-and-promotion-firewalls.md` only when promoting, revoking, or auditing research credit or when an adapter/semantic-scope question is load-bearing.
- **On-demand trigger:** open `docs/research-os/policies/hostile-audit-and-freshness.md` when performing a hostile audit, promoting or revoking audit credit, when the relationship between current-main freshness and hostile-audit result is load-bearing, **or when a shared/retained research PR approaches 100 commits since its last hostile-audited exact-head checkpoint**. In the long-lived-PR case, insert the intermediate audit checkpoint defined by that policy before allowing the shared retained surface to grow materially beyond the threshold; scratch-only branches are excluded.

## Repository-wide research routing

- **Existing weapon/evidence lookup:** open `docs/research-os/policies/repository-asset-discovery.md` only when the active leaf needs an already-existing weapon or evidence asset.
- **Route broadening/parking:** open `docs/research-os/policies/cycle-exploration-safety-protocol.md` only when deciding whether to broaden, park, dominate, reopen, or declare a route exhausted.
