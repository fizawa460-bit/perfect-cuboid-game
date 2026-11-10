# Stage32 MAIN startup

This is the sole ordinary Stage32 startup and dispatch contract.

## Read order

For `stage32mainbatch`, read only:

1. repository-root `AGENTS.md`;
2. this file;
3. `stages/stage32/CURRENT.json`;
4. the `LIVE.json` of the selected unit;
5. only the detailed state/evidence explicitly named by that live pointer and needed for the current leaf.

Do **not** ordinarily preload `MAIN-STATE.json`, full `ROADMAP.md`, claim/lane registries, cross-lane demands, historical controllers, audit receipts, parked lanes, or Research OS policies.

Open the formal `ROADMAP.md` section for the selected unit only when its mathematical scope, close criterion, residual classification, or synthesis/audit transition is load-bearing.

## Dispatch

`CURRENT.json` owns only the compact current-status projection. This file owns dispatch policy.

- 32-01 is complete and retained.
- 32-02 is primary.
- 32-03 is parallel.
- 32-04 waits for both.
- 32-05 is external hostile audit.

Default to 32-02. Use 32-03 when 32-02 is blocked or resumable 32-03 work is the better immediate path.

EX5, MB, and MB-FIB are internal execution surfaces, not operator entrypoints. 178, CUT, and BRIDGE are parked/reopen-only.

When dispatching to 32-03, read its LIVE-named STATE and honor `next_obligation.operational_next`
and `route_register.routes.E` before interpreting a historical `active_leaf` label. The old
MB104 active-leaf identifier is retained for audit-verifier compatibility; it does not by
itself authorize blind repetition of E2 work or promotion of the post-E12 route.

## Authority

`ROADMAP.md` is the sole formal owner of mathematical unit definitions and close criteria.

`CURRENT.json` and unit `LIVE.json` files are compact routing/resume projections, not proof certificates and not alternate mathematical specifications.

If a mathematical claim, credit transition, source identity, historical receipt, or audit boundary becomes load-bearing, open the exact detailed authority named by the live pointer.

Never promote bounded/sample/timeout evidence into theorem, effectivity, receiver, endpoint, closure, or Perfect-Cuboid credit without the required audited boundary.

## Audit standard (owner decision, 2026-11-06)

This section applies to `stage32mainbatch` and to `stage32audit`.

- **Purpose of an audit.** The audit checks that nothing is wrong. A reading (paper) audit is sufficient. It checks the
  mathematics and the logic, and what each computation decides. Under this standard, a reading audit with PASS and no
  open must-fix counts as **PASS**.
- **Re-execution is optional.** The auditor need not rerun the computations. "Not re-executed" alone does not make a
  PASS conditional, and does not keep a result unsettled.
- **Compute only when needed.** Run or rerun computations only when an argument requires them, or when an audit
  finding concerns what a computation decides.
- **Reproducibility is kept.** Scripts, commands, outputs and caveats stay recorded, so that anyone can check the
  computations.
- **Unchanged.** This standard does not change:
  - the repository-wide rules in `docs/research-os/policies/hostile-audit-and-freshness.md` and
    `research-credit-and-promotion-firewalls.md`;
  - credit flags;
  - the requirement of the owner's OK for any STATE, credit or merge change.

  A mathematical gap remains open outside the exact audited scope. For example, the d = 16 all-classes leaf
  (including multibranch-only classes) does not supply a uniform degree bound for all multibranch genus <= 1
  curves and does not close 32-03. Do not mistake a fixed-degree reading-audit PASS for Stage32 closure.

## Stop

Stop on the smallest precise residual/tool/theorem wall, at the 32-04 synthesis boundary, or before 32-05 external audit.

Do not merge without explicit user authorization.
