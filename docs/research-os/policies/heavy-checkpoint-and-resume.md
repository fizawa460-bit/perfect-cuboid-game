# Heavy checkpoint and resume policy

This policy is mandatory when designing, materially revising, authorizing, rerunning, or recovering an artifact-producing/heavy workflow.

The default execution model is **resume-first**, not monolithic rerun. Long computations must be partitioned at the finest practical exact boundary into deterministic independently verifiable work units. A successful unit is durable work: later generations must salvage and validate it, carry it forward, and recompute only unfinished units.

## Required heavy-run design

Before arming heavy compute, record the following in the runkey, preflight, workflow, or an equivalent source-locked execution contract:

1. the exact partition key and expected coverage;
2. the certificate/artifact emitted by each completed unit;
3. the validation needed before a prior unit may be carried forward;
4. the union/coverage verifier proving no gaps, overlaps, or source-lock drift;
5. the recovery rule for timeout, cancellation, runner loss, and partial completion;
6. whether partial outputs are uploaded with `if: always()` or an equivalent fail-safe path;
7. the storage/retention bound required by the repository Actions-storage policy.

If a mathematically valid finer partition is not yet available, the workflow must fail closed to a diagnostic or bounded pilot unless the execution contract explicitly records `RESUME_NOT_FEASIBLE` with the reason. Merely increasing a job timeout is not a substitute for a resume design.

## Carry-over rules

A prior work unit may be reused only when its certificate is complete and its execution semantics match the current generation exactly. At minimum verify the work-unit identity, source/execution locks, schema, solver/search parameters that affect semantics, traversal/completeness certificate, and deterministic content digest where available.

Incomplete containers may still contain reusable completed subunits. Recovery must inspect and salvage those subunits before scheduling recomputation. The Stage32-18T pattern is the reference precedent: validate completed packet/residue/subshard artifacts, carry them into the next run, and schedule only the missing residue/subshard set.

Never infer completion from job success alone when a certificate exists. Never reuse a partial unit merely because output files exist.

### Large predecessor artifact sets

Recovery must not assume that an artifact-list/download helper returns every predecessor artifact in one page. Before relying on per-unit artifacts, determine whether the predecessor can exceed the helper/API page size; **100 or more expected artifacts is an explicit trigger for paginated retrieval or a compact carry-bundle/manifest design**.

For predecessor runs at or above that threshold:

- enumerate all artifact pages explicitly, or consume a deterministic carry bundle whose manifest names every retained unit;
- compare the predecessor's expected/completed-unit count with the number of retrieved and validated unit certificates before scheduling recovery;
- if the counts disagree and the difference is not explicitly explained by rejected/expired artifacts, fail closed instead of treating unseen artifacts as missing compute;
- never convert a retrieval truncation into recomputation work;
- keep the validated unit manifest/carry bundle below the relevant retrieval limit when chaining generations, or prove that the retrieval path itself is fully paginated.

The recovery snapshot must record both `discovered_artifact_count` and `validated_carried_unit_count` (or equivalent fields) when the predecessor may contain 100 or more artifacts, so an artifact-enumeration truncation cannot masquerade as unfinished mathematics.

## Timeout and cancellation recovery

After timeout/cancellation/resource-wall failure:

- preserve/upload all already-complete exact subunits when technically safe;
- construct a source-locked recovery snapshot describing complete, incomplete, missing, and rejected carry-over units;
- re-arm a new generation only for the remaining work;
- do not rerun the whole parent population when validated completed subunits are available;
- do not repeatedly extend the same monolithic timeout after one or more long failures without first seeking a finer exact partition.

If the current worker cannot expose a valid finer partition, add execution-only partition controls plus exact union verification before spending another long generation, provided this does not alter mathematical population or source semantics.

## Completion and credit firewall

Carry-over is an execution optimization only. It does not change the mathematical population, grant research credit, or weaken hostile-audit requirements. Aggregated completion is accepted only after exact coverage/union verification and source-lock validation. MAIN/theorem/receiver/effectivity credit remains controlled by the normal promotion firewalls.

## Operational precedent

Stage32-01 established independently resumable immutable strata. Stage32-18T then implemented the stronger production pattern used here: union successful prior runs, salvage completed residues from otherwise incomplete packets, pass them through a carry directory, and compute only unfinished residues. New heavy workflows should reuse this pattern whenever their search admits an exact subproblem partition.
