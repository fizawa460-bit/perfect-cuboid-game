# Repository agent instructions

## CRITICAL repo-wide rule: bounded Actions storage before compute

This rule has priority over stage-local speed, convenience, or batching preferences.

Before launching any GitHub Actions workload that can create artifacts, the agent MUST treat Actions artifact/storage capacity as a hard execution constraint, separate from runner-minute or concurrency limits.

1. **Preflight the storage peak before launch.** Estimate the worst-case simultaneous stored footprint of all still-required existing artifacts, all new intermediate artifacts, and the final evidence. If the available quota cannot be verified, use a conservative design that does not depend on having large spare storage. Do not start a batch whose projected peak can plausibly exhaust the account/repository storage budget. The repository operating budget is **500 MB** unless this policy is explicitly revised.
2. **Measure one representative shard before scaling out.** For a new high-mass workflow, run or inspect a representative unit and use its actual artifact size to project the full batch. Do not extrapolate only from branch count or runtime.
3. **Raw exhaustive evidence stays runner-local whenever possible.** Validate raw branch rows/logs on the runner, then persist compact deterministic certificates: source/raw SHA, exact coverage/partition evidence, UNKNOWN count, survivor set or survivor digest as appropriate, solver-completion flags, and required firewalls. Compaction MUST be post-verification only and MUST NOT weaken mathematical exactness.
4. **Never require all large raw shards to coexist in artifact storage.** If raw intermediates are genuinely required, aggregate in bounded waves/chunks and discard superseded intermediates before proceeding to the next wave.
5. **Set explicit short retention on intermediates.** Temporary shard artifacts should normally use the minimum practical `retention-days` (typically 1-3 days). Only final audit/manifest artifacts receive longer retention when justified.
6. **Storage risk is a stop condition.** If projected peak storage becomes unsafe, artifact uploads begin failing, quota/usage is uncertain in a way that can invalidate the run, or observed shard size materially exceeds the preflight estimate, STOP/CANCEL before producing more large artifacts and redesign the evidence flow. Do not continue merely because compute jobs are succeeding.
7. **Cancelled/non-credit production runs are cleanup obligations.** Once any evidence that must be retained has been compacted/source-locked elsewhere, delete the obsolete run/artifacts rather than leaving large abandoned intermediates resident.
8. **Do not trade exactness for storage.** Any compact certificate used for theorem-facing or hostile-audit evidence must preserve enough deterministic commitments and invariants for independent verification of the claimed exact coverage/result. Storage optimization never grants theorem, receiver, effectivity, or endpoint credit by itself.

## CRITICAL repo-wide rule: heavy Actions concurrency headroom

This rule is mandatory and has the same priority as the storage rule above.

1. **A single Stage MUST NOT be designed to occupy more than 18 heavy compute runners concurrently.** This is a hard upper bound, not a target.
2. **Count effective overlap, not individual YAML values.** If multiple matrix jobs or workflows from the same Stage can run at the same time, sum their concurrently runnable heavy jobs. For example, `max-parallel: 10` plus another overlapping `max-parallel: 10` is an effective 20 and is prohibited.
3. **Do not evade the cap by splitting work across workflows/PRs.** Coordinated heavy workloads belonging to the same Stage are counted together.
4. **Other Stages must retain runner headroom.** Heavy workflow design must deliberately leave capacity for independent Stage work, reconnaissance, audits, and lightweight Actions. Stage-local speed or earlier completion does not override this requirement.
5. **Preflight before launch.** Every new or materially revised heavy workflow MUST record/verify `planned effective heavy concurrency <= 18` before it is armed. If the overlap cannot be bounded confidently, reduce `max-parallel` until the bound is guaranteed.
6. **Absolute compliance.** Never knowingly launch a heavy configuration that can exceed 18 effective concurrent jobs for one Stage. Redesign or split in time instead.

Detailed reusable policy: `docs/research-os/policies/actions-storage-and-evidence-safety.md`.
Human-facing entrypoint: `docs/README.md`.

## Stage14 automation PR contract

Every pull request created for one of the recurring Stage14 batches must include exactly one safety marker and exactly one route marker in its body:

```text
STAGE14_AUTOMATION_SAFE=true
STAGE14_ROUTE=<route>
```

Use the route corresponding to the requested batch:

- `Stage14-main-batch` -> `main`
- `Stage14-s-batch` -> `s`
- `Stage14-t-batch` -> `t`
- `Stage14-Work-toolbox-XQ` (integration batch) -> `xq`

Do not set `STAGE14_AUTOMATION_SAFE=true` for unrelated PRs. Do not use a route other than `main`, `s`, `t`, or `xq`. If a batch is blocked, unsafe to merge, has unresolved conflicts, or needs manual review, omit the safety marker and state the blocker in the PR body.
