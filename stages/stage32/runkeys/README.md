# Stage32 run keys

Files in this directory are explicit execution keys for heavy Stage32 GitHub Actions workflows.

Changing implementation code does not authorize a heavy rerun. A heavy workflow should listen only to its dedicated run-key path. After the intended implementation revision is ready, update that key's `generation` and the workflow-specific execution parameters once.

Required base fields:

- `schema`: `STAGE32_HEAVY_RUN_KEY_V1`
- `workflow`: stable workflow identifier expected by the workflow itself
- `generation`: positive integer increased for a deliberate new execution
- `heavy_execution_explicitly_armed`: `true`

Workflow-specific fields should select the smallest necessary execution set, for example only failed shard IDs or only breaker counts that still need measurement.

See `stages/stage32/HEAVY_WORKFLOW_POLICY.md` for the full policy.
