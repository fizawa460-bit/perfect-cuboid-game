# PR1827 — current-main repair / independent re-audit handoff

Status: **FROZEN / PENDING INDEPENDENT HOSTILE RE-AUDIT / ZERO NEW CREDIT**.

User authorization: repair PR1827 until it is ready for audit. This does not authorize merging PR1827 into main or self-awarding hostile-audit PASS.

## Exact input boundaries

- Retained research head: `68e9ce5dc1453caa7d4802929b573e5fb3fdb1e0`.
- Current main incorporated: `c6cc8f12d7044eb3f3dc182850decd565a4e1752` (includes merged PR1831).
- Previous externally recorded restart PASS: `37727ad09b62c49b49cfb2e1e428b5a2d4826e88`, corrected review5258058107. It remains historical and is not inherited by this repair.

## Repair scope

1. Preserve current MAIN's startup workflow, current authority checks and local-first lifecycle. Add only the bounded MB compact checker and nine exact PR path entries; no broad MB wildcard or new automatic workflow.
2. Check the historical post-freeze research delta at its immutable retained head separately from the PR's current-main integration delta. Importing current main must not be misclassified as unauthorized new MB mathematics.
3. Add the already-retained invariant-line note to the narrow research path set and verify its SHA256.
4. Correct six stale verifier predicates: b3 quotient, anti-invariant jets and ACM are not live routes; the Z12 main observation is historical; the retained Betti cycle is blocked and its final view is parked. Retained mathematical assertions remain checked.
5. Preserve the entire retained_frontier object with canonical SHA256 `b70a41d328b28cce77e1a73df8b3b97cb0e91185c404c069f6774d50b9ceca17`. The checker rejects any mathematical frontier alteration, including fields not individually tested by the historical predicates.
6. Freeze ordinary research pending independent re-audit. Preserve the old next_obligation verbatim as resume_obligation. The latest coreless interface is the retained `nodes/MB104/MB104-000707-CORELESS-INVARIANT-LINE-WALL-20260926.md`; historical rational-core success shapes are not new live problems.

## Local verification

Run locally under docs/research-os/policies/local-first-execution.md:

```sh
PYTHONDONTWRITEBYTECODE=1 python stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_compact_audit_restart.py --self-test-fail-closed
PYTHONDONTWRITEBYTECODE=1 python scripts/local_replay_workflow.py .github/workflows/stage32-claim-frontier-integrity.yml --out <claim-record.json>
PYTHONDONTWRITEBYTECODE=1 python scripts/local_replay_workflow.py .github/workflows/stage32-main-startup-authority.yml --job startup-authority --out <startup-record.json>
```

Fail-closed regressions cover an unapproved path, early research reopening, audit-inheritance bypass, a retired route made live, an altered retained mathematical claim, note identity tampering, self-awarded merge credit, and a lost resume pointer.

Replay records bind the tested exact commit, environment, initial tree state, commands, exits and bounded output. Records committed later are evidence-only descendants of that tested boundary; they do not falsely claim to have run on their own future commit SHA. Final exact-head replay is also performed after documentation/evidence consolidation.

## Independent auditor's boundary

Confirm the exact repair head, both ancestry boundaries, bounded PR diff, retained-frontier and note hashes, corrected routing semantics, regression failures, startup/claim replay, workflow lifecycle and zero-credit flags. Local checker PASS is not hostile-audit PASS. The pre-audit rational-core result remains pre-audit; CORELESS / NO NONEMPTY CLUMP, balanced bulk, e2 and 32-03 remain open. No heavy computation, receiver discharge, effectivity, theorem, endpoint, Stage32 closure or Perfect Cuboid claim is released.
