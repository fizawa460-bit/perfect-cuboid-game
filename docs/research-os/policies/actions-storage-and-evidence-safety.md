# Actions storage and evidence safety

## Status

This is a mandatory repository-wide Research OS policy for any GitHub Actions workload that performs substantial computation, exhaustive search, proof/certificate generation, or large parallel batching.

The top-level enforcement summary lives in `AGENTS.md`. This document gives the reusable operating standard.

## Core constraints

Runner availability, rerun authorization, and artifact storage are distinct resources. A workflow can be mathematically correct while still failing operationally because artifacts exceed the storage budget or an unrelated PR synchronization accidentally relaunches heavy computation.

The repository operating budget for Actions artifact/storage is **500 MB** unless this policy is explicitly revised. Heavy reruns require explicit commit-range authorization; the mere continued presence of a run-key path in a PR diff is not authorization.

There is no repository-wide fixed per-Stage heavy-job concurrency ceiling. Choose workflow concurrency from the actual compute topology, platform limits, storage preflight, and Stage-local requirements. Concurrency is an execution parameter, not mathematical credit.

## Mandatory heavy-rerun authorization gate

`pull_request.paths` is a coarse trigger filter, not proof that the dedicated run key changed in the event that caused the run. Every PR-triggered heavy workflow must fail closed unless a cheap authorization job proves a fresh explicit arm.

For every new or materially revised PR-triggered heavy workflow:

1. Gate before heavy compute. Every heavy job depends on a cheap authorization result.
2. For `synchronize`, inspect the actual `github.event.before..github.event.pull_request.head.sha` range and require the dedicated run-key path itself to have changed. If the range cannot be verified, authorization is false.
3. Require semantic arming: generation/revision must advance and workflow-specific locks must validate. Cosmetic edits are not authorization.
4. Audit/controller/status/docs/source bookkeeping is cold unless it explicitly and validly advances the dedicated run key.
5. `reopened` is cold by default; require a fresh later run-key advance.
6. Initial `opened` may authorize only when the dedicated key is newly introduced or changed relative to base and passes the same semantic checks.
7. Existing heavy workflows must use this commit-range gate before another credited generation is armed.

A shell diff check is necessary but not sufficient; validation must parse old/new key content and prove the semantic generation/revision and locked parameters before emitting authorization.

## Mandatory storage preflight gate

Before a new high-mass batch, record or derive:

1. planned jobs/shards;
2. largest plausible artifact per shard;
3. measured representative artifact size when comparable prior evidence is unavailable;
4. historical artifacts that must coexist until aggregation/audit;
5. final-output size and retention;
6. projected peak simultaneous storage against the 500 MB budget;
7. cleanup point for intermediates;
8. dedicated run-key authorization method and event/commit-range condition.

If available storage cannot be read reliably, redesign so correctness does not depend on assumed spare capacity.

## Preferred evidence architecture

Prefer:

```text
exact raw computation on runner
  -> full local verification
  -> deterministic compact certificate
  -> upload compact certificate only
  -> aggregate compact certificates
  -> final parent/audit manifest
```

Compaction happens only after exact validation. It must not omit unresolved branches, collapse UNKNOWN into UNSAT, weaken source locks, or discard information required by downstream audit.

A compact certificate should preserve the exact source/parameter locks, shard identity and partition/completion invariants, UNKNOWN/resource-wall counts, survivor data or auditable commitment, deterministic raw/evidence/certificate commitments, and Stage-required credit/firewall fields.

## Bounded-wave rule for unavoidable raw artifacts

If downstream verification genuinely requires raw intermediate files, use bounded waves rather than requiring every large shard artifact to coexist:

```text
wave A -> verify/aggregate -> compact -> delete raw A
wave B -> verify/aggregate -> compact -> delete raw B
...
final aggregate from compact wave certificates
```

Choose wave size from measured artifact size and the 500 MB storage budget, not convenience alone.

## Retention and cleanup

Every non-final `actions/upload-artifact` must have explicit short retention. Use one day for transient shard/intermediate evidence where practical and 1-3 days for short-lived repair/audit inputs; retain final manifests longer only when justified.

A cancelled, superseded, or non-credit production run is not operationally finished until unnecessary artifacts are removed after any unique evidence has been compacted/source-locked elsewhere.

## Runtime stop conditions

Stop or cancel before further upload/scale-out when artifact size materially exceeds preflight, projected storage approaches the 500 MB budget, quota uncertainty makes completion unsafe, uploads fail, the evidence topology needs more simultaneous raw storage than planned, or heavy compute lacks fresh valid run-key authorization.

These are execution-resource walls, not mathematical results. They grant no UNSAT, theorem, receiver, effectivity, or endpoint credit.

## Relationship to exactness and hostile audit

Storage/rerun optimization is allowed only when final persisted evidence still supports the Stage's exactness claim. Hostile audit should be able to distinguish exact execution, raw verification before deletion, deterministic compact commitments, complete shard/cell coverage, explicit UNKNOWN/resource walls, unchanged mathematical firewalls, and valid heavy-run authorization.

Operational invariant:

> Preflight storage before compute; require fresh commit-range run-key authorization for heavy reruns; verify raw before compacting; persist only what audit needs; stop before storage limits or accidental relaunches become a correctness risk.

## Incident precedents

Stage32-13 established the storage precedent: a 48-shard exact computation initially persisted very large raw shard JSONs. The run was cancelled and replaced by runner-local raw verification plus compact deterministic certificates, reducing persisted evidence dramatically without weakening exactness.

Stage32-18L established the rerun-authorization precedent: audit/controller bookkeeping synchronization re-triggered heavy production even though its run key had not changed. This showed that `pull_request.paths` is not per-synchronization authorization; later heavy workflows use an actual `before..head` run-key gate.

These precedents are operational guidance, not mathematical credit for the associated runs.
