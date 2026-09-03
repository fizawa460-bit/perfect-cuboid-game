# Actions storage and evidence safety

## Status

This is a mandatory repository-wide Research OS policy for any GitHub Actions workload that performs substantial computation, exhaustive search, proof/certificate generation, or large parallel batching.

The top-level enforcement summary lives in `AGENTS.md`. The human-facing entrypoint is `docs/README.md`. This document gives the reusable operating standard.

## Why this policy exists

Runner availability, concurrency, rerun authorization, and artifact storage are different resources. A workflow can be mathematically correct and computationally healthy while still failing operationally because intermediate artifacts accumulate faster than the storage budget permits or an unrelated PR synchronization accidentally relaunches heavy computation.

A large batch is therefore not safe merely because:

- hosted runner minutes are available;
- jobs are succeeding;
- platform concurrency would permit more jobs;
- each individual shard finishes within its timeout;
- `pull_request.paths` matched the event.

The repository operating budget for Actions artifact/storage is **500 MB** unless this policy is explicitly revised. Heavy reruns require explicit commit-range authorization; the mere continued presence of a run-key path in a PR diff is not authorization.

There is no repository-wide fixed per-Stage heavy-job concurrency ceiling. Workflow concurrency is an execution parameter and does not grant mathematical credit.

## Mandatory heavy-rerun authorization gate

`pull_request.paths` is a useful coarse trigger filter but is **not** a proof that the dedicated run key changed in the event that caused the workflow run. A heavy workflow must therefore fail closed after the event fires unless a cheap authorization job proves that this event contains a fresh explicit arm.

For every new or materially revised PR-triggered heavy workflow:

1. **Gate before heavy compute.** A cheap validation job must run first. Every heavy matrix/job must depend on it and use an `authorized` output (or equivalent) so the expensive jobs are skipped unless authorization succeeds.
2. **For `synchronize`, inspect the actual event commit range.** Use `github.event.before` as the old revision and `github.event.pull_request.head.sha` as the new revision. Fetch the old revision and require the dedicated run-key path itself to appear in `git diff --name-only "$BEFORE" "$HEAD"`. If `before` is absent, cannot be fetched, or the diff cannot be verified, authorization is false.
3. **Require semantic arming.** If the key is newly added, require a positive generation/revision and the workflow's explicit armed flag. If the key already existed, compare old and new key content and require the generation/revision to advance strictly, plus all workflow-specific source/artifact/parameter locks to validate. A whitespace-only/cosmetic edit or unrelated file change is not an arm.
4. **Non-key bookkeeping is cold.** Audit records, controller/status changes, README/docs changes, source edits, formatting, review bookkeeping, and other unrelated synchronizations must not authorize heavy reruns merely because the run key remains in the cumulative PR diff.
5. **`reopened` is cold by default.** Reopening an already-armed PR must not restart heavy computation. Require a fresh run-key generation/revision on a later `synchronize` event before heavy work can run again.
6. **Initial `opened` is restricted.** It may authorize only if the dedicated run key is newly introduced or changed relative to the PR base and passes the same semantic validation. The safer preferred pattern is to open the PR cold, finish source/workflow edits, and arm exactly once in a distinct follow-up commit.
7. **Existing heavy workflows are migration obligations.** Before an existing heavy workflow is armed for another generation, migrate it to this commit-range gate. Until the active set has been migrated or linted, do not claim repository-wide mechanical enforcement.

A representative `synchronize` gate has the following shape:

```bash
KEY='stages/<stage>/runkeys/<dedicated-key>.json'
BEFORE='${{ github.event.before }}'
HEAD='${{ github.event.pull_request.head.sha }}'
authorized=false
if [ -n "$BEFORE" ]; then
  git fetch --no-tags --depth=1 origin "$BEFORE" || true
  if git cat-file -e "$BEFORE^{commit}" 2>/dev/null \
     && git diff --name-only "$BEFORE" "$HEAD" | grep -Fxq "$KEY"; then
    authorized=true
  fi
fi
```

The shell diff check is necessary but not sufficient; the validation step must still parse the old/new key and prove the generation/revision and locked parameters are valid before emitting `authorized=true`.

## Mandatory storage preflight gate

Before launching a new high-mass batch, record or derive:

1. the number of planned jobs/shards;
2. the largest plausible artifact per shard;
3. the measured artifact size of at least one representative shard when a comparable prior run is unavailable;
4. the size of historical artifacts that must remain available until final aggregation/audit;
5. the size and retention period of final outputs;
6. the projected peak simultaneous storage against the 500 MB operating budget;
7. the cleanup point at which intermediates become disposable;
8. the planned effective heavy concurrency;
9. the dedicated run-key authorization method and the event/commit-range condition that permits a heavy rerun.

If the current storage quota cannot be read reliably, the workflow must be redesigned so that correctness does not depend on large spare capacity. Uncertainty is not permission to assume unlimited storage.

## Preferred evidence architecture

For exhaustive numerical/proof workloads, prefer:

```text
exact raw computation on runner
  -> full local verification
  -> deterministic compact certificate
  -> upload compact certificate only
  -> aggregate compact certificates
  -> final parent/audit manifest
```

The raw computation may be large. The persisted evidence should normally be small.

A compact certificate should preserve, as applicable:

- exact parameter/source locks;
- immutable cell/shard identity;
- exact expected and executed branch counts;
- proof that branch indices form the intended disjoint partition;
- solver completion for every branch;
- explicit node-budget/UNKNOWN count;
- survivor list or a lossless/auditable survivor commitment;
- deterministic raw-output SHA;
- canonical branch-evidence-stream SHA or equivalent commitment;
- deterministic compact-certificate SHA;
- theorem/receiver/effectivity/firewall fields required by the stage contract.

Compaction happens **after** exact validation. It is not permission to omit unresolved branches, collapse UNKNOWN into UNSAT, weaken source locks, or discard survivor information needed by downstream orbit/effectivity checks.

## Bounded-wave rule for unavoidable raw artifacts

If downstream verification genuinely needs raw intermediate files, do not design one final job that requires every large shard artifact to coexist.

Instead use bounded waves such as:

```text
wave A shards -> verify/aggregate A -> compact A -> delete raw A
wave B shards -> verify/aggregate B -> compact B -> delete raw B
...
final aggregate from compact wave certificates
```

The wave size must be chosen from measured artifact size and the 500 MB storage headroom, not from convenience alone.

## Retention policy

Every `actions/upload-artifact` for non-final evidence must specify an explicit retention period.

Default guidance:

- transient shard/intermediate: `retention-days: 1` where practical;
- short-lived repair/audit input: 1-3 days;
- final parent/audit manifest: longer only when justified by the audit/reproducibility workflow.

Do not leave default long retention on dozens of large intermediate artifacts.

## Runtime stop conditions

Stop or cancel a live workflow before further uploads or scale-out when any of the following occurs:

- measured artifact size materially exceeds the preflight estimate;
- projected peak storage can approach/exhaust the 500 MB operating budget;
- storage/quota uncertainty makes successful completion unsafe;
- artifact upload starts failing or being rejected;
- a cancelled/failed run has already produced large non-credit intermediates that should be cleaned before retry;
- the evidence topology turns out to require more simultaneous raw artifacts than planned;
- a heavy run was triggered without a fresh valid commit-range run-key authorization.

A storage/authorization stop is an **execution-resource wall**, not a mathematical result. It grants no UNSAT, theorem, receiver, effectivity, or endpoint credit.

## Cleanup obligation

A cancelled, superseded, or non-credit production run is not finished operationally until its unnecessary artifacts are removed after any required evidence has been safely compacted/source-locked elsewhere.

Before deleting a run that contains unique evidence, first preserve the deterministic commitments or compact certificate needed to reproduce/audit the result. Once the run is explicitly non-credit and no unique evidence is needed, delete it rather than carrying its storage indefinitely.

## Relationship to exactness and hostile audit

Storage/concurrency/rerun optimization is allowed only when the final persisted evidence still supports the stage's exactness claim.

Hostile audit should be able to distinguish:

- computation executed exactly;
- raw output was verified before deletion;
- compact certificate commits deterministically to that verified output;
- all expected shards/cells are present exactly once;
- UNKNOWN/resource-wall states were not silently promoted;
- mathematical firewalls remain unchanged;
- every credited heavy run had an explicit valid run-key authorization rather than an accidental PR re-trigger.

The operational rule is therefore:

> **Preflight storage before compute; require fresh commit-range run-key authorization for heavy reruns; verify raw before compacting; persist only what the audit actually needs; stop before resource limits or accidental relaunches become a correctness risk.**

## Incident precedent

Stage32-13 established the motivating storage precedent: a 48-shard exact computation initially persisted raw shard JSONs of roughly tens of MiB each. The run was cancelled before the storage design became a failure mode. A representative raw shard was then independently compacted after full branch verification from roughly 159 MB uncompressed to roughly 2.3 KB while retaining deterministic raw/evidence commitments and exact completion invariants. The replacement workflow persists compact certificates only.

The Stage32-18L audit established the rerun-authorization precedent: an audit/controller bookkeeping synchronization re-triggered the heavy production workflow even though its run-key file itself had not changed. This demonstrated that `pull_request.paths` can remain matched by the PR's cumulative changed-file set and is not a per-synchronization authorization proof. Subsequent Stage32 heavy workflows therefore use a commit-range gate that checks the actual `before..head` change before launching heavy jobs.

These precedents are operational guidance, not mathematical credit for the associated runs.
