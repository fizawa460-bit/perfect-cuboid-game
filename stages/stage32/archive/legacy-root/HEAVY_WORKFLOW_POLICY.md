# Stage32 heavy-workflow execution policy

Stage32 can generate long CPU-bound matrices and exact-enumeration jobs. Those jobs must not be armed merely because a pull request is opened or synchronized.

## Required convention

Any Stage32 workflow that can consume substantial runner time, fan out a matrix, or execute an exact/large bounded census must be controlled by a dedicated file under `stages/stage32/runkeys/`.

A heavy workflow's `pull_request.paths` must point to its run-key file, not to its implementation, README, audit, or controller paths. Ordinary source edits therefore remain cold. Once the intended implementation revision has been reviewed, one deliberate run-key revision arms the heavy execution.

Run keys use schema `STAGE32_HEAVY_RUN_KEY_V1` and should include at least:

```json
{
  "schema": "STAGE32_HEAVY_RUN_KEY_V1",
  "workflow": "stable-workflow-id",
  "generation": 1,
  "heavy_execution_explicitly_armed": true
}
```

A workflow-specific key may also lock bounds, shard IDs, breaker counts, matrices, resource caps, or other execution parameters. The workflow must validate those fields before heavy work begins.

## Operational rules

1. Do not bump a run key for documentation, audit metadata, controller bookkeeping, comments, formatting, or unrelated repairs.
2. Source/workflow changes do not by themselves authorize a heavy rerun. Finish the intended source revision first, then change the key exactly once.
3. Prefer a key that selects only the required matrix entries rather than rerunning successful entries.
4. Heavy workflows must use a per-PR `concurrency` group with `cancel-in-progress: true` unless a documented exactness requirement makes cancellation unsafe.
5. The Stage32 stale-run sweeper cancels active Stage32 runs from older heads of the same PR branch. This is a resource-safety mechanism only; it grants no mathematical credit.
6. Existing historical workflows are not retroactively authoritative merely because they ran. Numerical, theorem, receiver, and completeness credit continue to follow the Stage32 exact/audit firewalls.

## Default for new Stage32 work

If a new workflow might plausibly run for many minutes or launch multiple runners, treat it as heavy and key-gate it from the start. Cheap lint, syntax, schema, or small deterministic checks may remain automatic.
