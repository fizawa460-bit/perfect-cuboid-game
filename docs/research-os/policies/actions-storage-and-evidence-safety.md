# Actions storage and evidence safety

## Status

This is a mandatory repository-wide Research OS policy for any GitHub Actions workload that performs substantial computation, exhaustive search, proof/certificate generation, or large parallel batching.

The top-level enforcement summary lives in `AGENTS.md`. This document gives the reusable operating standard.

## Why this policy exists

Runner availability and artifact storage are different resources. A workflow can be mathematically correct and computationally healthy while still failing operationally because intermediate artifacts accumulate faster than the storage budget permits.

A large batch is therefore not safe merely because:

- hosted runner minutes are available;
- jobs are succeeding;
- concurrency is below the platform limit;
- each individual shard finishes within its timeout.

The relevant quantity is the **peak simultaneously retained evidence footprint** over the whole workflow and over all still-live historical inputs that the workflow depends on.

## Mandatory preflight gate

Before launching a new high-mass batch, record or derive:

1. the number of planned jobs/shards;
2. the largest plausible artifact per shard;
3. the measured artifact size of at least one representative shard when a comparable prior run is unavailable;
4. the size of historical artifacts that must remain available until final aggregation/audit;
5. the size and retention period of final outputs;
6. the projected peak simultaneous storage;
7. the cleanup point at which intermediates become disposable.

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

The wave size must be chosen from measured artifact size and the available storage headroom, not from convenience alone.

## Retention policy

Every `actions/upload-artifact` for non-final evidence must specify an explicit retention period.

Default guidance:

- transient shard/intermediate: `retention-days: 1` where practical;
- short-lived repair/audit input: 1-3 days;
- final parent/audit manifest: longer only when justified by the audit/reproducibility workflow.

Do not leave default long retention on dozens of large intermediate artifacts.

## Runtime stop conditions

Stop or cancel a live workflow before further uploads when any of the following occurs:

- measured artifact size materially exceeds the preflight estimate;
- projected peak storage can approach/exhaust the usable budget;
- storage/quota uncertainty makes successful completion unsafe;
- artifact upload starts failing or being rejected;
- a cancelled/failed run has already produced large non-credit intermediates that should be cleaned before retry;
- the evidence topology turns out to require more simultaneous raw artifacts than planned.

A storage stop is an **execution-resource wall**, not a mathematical result. It grants no UNSAT, theorem, receiver, effectivity, or endpoint credit.

## Cleanup obligation

A cancelled, superseded, or non-credit production run is not finished operationally until its unnecessary artifacts are removed after any required evidence has been safely compacted/source-locked elsewhere.

Before deleting a run that contains unique evidence, first preserve the deterministic commitments or compact certificate needed to reproduce/audit the result. Once the run is explicitly non-credit and no unique evidence is needed, delete it rather than carrying its storage indefinitely.

## Relationship to exactness and hostile audit

Storage optimization is allowed only when the final persisted evidence still supports the stage's exactness claim.

Hostile audit should be able to distinguish:

- computation executed exactly;
- raw output was verified before deletion;
- compact certificate commits deterministically to that verified output;
- all expected shards/cells are present exactly once;
- UNKNOWN/resource-wall states were not silently promoted;
- mathematical firewalls remain unchanged.

The operational rule is therefore:

> **Preflight storage before compute; verify raw before compacting; persist only what the audit actually needs; stop before the storage budget becomes a correctness risk.**

## Incident precedent

Stage32-13 established the motivating precedent: a 48-shard exact computation initially persisted raw shard JSONs of roughly tens of MiB each. The run was cancelled before the storage design became a failure mode. A representative raw shard was then independently compacted after full branch verification from roughly 159 MB uncompressed to roughly 2.3 KB while retaining deterministic raw/evidence commitments and exact completion invariants. The replacement workflow persists compact certificates only.

This precedent is operational guidance, not mathematical credit for that cancelled run.
