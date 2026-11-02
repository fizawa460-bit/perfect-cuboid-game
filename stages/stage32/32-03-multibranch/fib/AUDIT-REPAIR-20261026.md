# MB-FIB Gen30 audit repair

Retained research head: `970a42ad2aeb343911ffc3d2e06b7357ed042ae0`.
Integrated MAIN: `c6cc8f12d7044eb3f3dc182850decd565a4e1752`.

Status: frozen pending independent exact-head hostile re-audit. No heavy execution, research release, mathematical promotion or merge is authorized.

The Gen30 cold deriver now pins a shared lock helper before importing it. That helper checks all five retained transitive source blobs before any numeric dependency is imported. The normal preflight also pins and invokes it before executing the carry or cold verifiers. Six reversible mutation regressions prove that altered dependencies (including the helper itself) cannot execute their injected marker. Original bytes are restored in finally blocks.

The MB-FIB pilot is MANUAL and contains only COLD verification steps. Historical heavy-execution and auto-commit jobs were removed from the live workflow; their provenance remains in Git history. All four historical materializers remain RETIRED/workflow_dispatch-only. Inventories preserve MAIN's local-first automatic allowlist. Current effective heavy concurrency is zero; any future heavy Actions authorization is separate and subject to the repository-wide cap of two and explicit per-run user authorization. The immutable historical cold design's concurrency-eight metadata does not authorize execution.

The original Gen29 bundles, source/index/residual files and Gen30 cold certificate are unchanged. Completed111/timeout49 accounting and all49 x56 split leaves/392 intervals are retained exactly. Current routing is COLD, unarmed and frozen; older Gen28 CI/audit data is historical evidence, not current-head PASS. MAIN workflow and command-surface conflict resolution retain current MAIN authority; the bounded FIB PR paths are admitted by an exact-path startup scope case.

Reproduce locally, with PYTHONDONTWRITEBYTECODE=1:

```bash
python stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_000707_gen26_adaptive_x58_preflight.py
python stages/stage32/final-chain/32-03-multibranch/nodes/MB104/test_mb104_fib_preimport_locks.py
python scripts/local_replay_workflow.py .github/workflows/stage32-claim-frontier-integrity.yml --out /tmp/pr1829-claim.json
python scripts/local_replay_workflow.py .github/workflows/stage32-main-startup-authority.yml --job startup-authority --out /tmp/pr1829-startup.json
python scripts/local_replay_workflow.py .github/workflows/stage32-mb-fib-isotropic-shell-pilot.yml --job authorize --out /tmp/pr1829-cold.json
```

Exact-head local receipts are published in the PR body without advancing the frozen source head. PASS of these implementation checks is not an independent hostile-audit PASS.
