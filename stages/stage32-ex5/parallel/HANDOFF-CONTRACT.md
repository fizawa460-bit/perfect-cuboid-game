# Parallel lane handoff contract

Each scratch lane should leave a compact machine-readable result under `stages/stage32-ex5/parallel/results/` when it has a coherent checkpoint.

Required fields:
- `schema`
- `lane`
- `base_scaffold_commit`
- `target = BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`
- `status = PASS | BLOCKED | PARTIAL`
- `exact_inputs[]` with repository/source locators and immutable identifiers where available
- `claims[]` with explicit scope and assumptions
- `checks[]` with deterministic replay commands/procedures
- `ambiguities[]`
- `blockers[]`
- `artifacts[]`
- `authority = SCRATCH_ONLY`
- all downstream credit flags false

For a PASS candidate involving a 48-object construction, also record exact counts, uniqueness/collision checks, and the canonicalization definition. Tables may be retained as separate compact JSON artifacts; do not embed large opaque payloads.

Mainbatch may compare scratch results but must independently validate any load-bearing claim before retained consolidation.