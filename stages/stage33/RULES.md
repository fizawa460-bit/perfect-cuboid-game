# Stage33 rules

This file is the Stage33-specific rule layer. It is intentionally stable: current receivers, live routes, current progress, and batch-by-batch findings do not belong here.

## Authority layers

Use the repository in this order:

1. `docs/research-os/` and `AGENTS.md` — repo-wide research safety, evidence, credit, Actions, and cycle policies.
2. `stages/stage33/RULES.md` — stable Stage33-specific rules and routing.
3. `stages/stage33/CURRENT.md` and `stages/stage33/controller.json` — current human/machine execution state.
4. active unit state, e.g. `stages/stage33/33-05/j2-representative-repair-state.json` — detailed current mathematics for the active repair.
5. `stages/stage33/HISTORY.md`, `33-xx/result.md`, certificates, scripts, audits, and Git history — historical work and evidence.

If a historical result or roadmap status conflicts with CURRENT/controller/active authoritative state, the current authoritative state wins. Mathematical certificate claims remain limited to their declared scope; this routing rule does not upgrade credit.

## Frozen Stage33 scope

Stage33 executes the frozen Stage29 physical-open Brauer kernel `K16-C2-BRAUER-EXPLICIT-CHAIN` / `BRAUER-EXPLICIT-DAG`.

The Stage33 scope includes the Stage29-retained open-algebraic contribution, physical-boundary residue contribution, and two-primary geometric/transcendental contribution. No surviving class may be silently discarded merely because a later sub-route is two-primary.

Detailed unit acceptance criteria remain delegated to:

`stages/stage33/33-00/unit-closure-contract.md`

## Progress and release law

The Stage33 progress denominator is 11 big tasks. Repair children do not independently increment that denominator.

A big task releases dependent downstream work only when its required closure state is exact and audited according to the unit closure contract. Partial, preview, numerical, blocked, or audit-pending states do not count as closed.

Repair-child completion does not automatically close its reopened parent. The parent closes only after the required repair chain and hostile recertification succeed.

## Credit and audit firewall

Stage33 may not weaken the repo-wide Research OS promotion rules.

In particular:

- geometric, extension-field, quotient, bounded, or finite-presentation evidence stays at that scope until an explicit descent/adapter is proved;
- Galois fixedness alone does not imply Hochschild-Serre obstruction zero;
- successful CI or a materialized certificate does not by itself release theorem, receiver, endpoint, or perfect-cuboid credit;
- hostile audit may revoke or reopen prior credit;
- no perfect-cuboid existence/nonexistence claim is released without the explicit audited final endpoint required by Research OS.

## Stage33 bounded stop conditions

A Stage33 line may stop/checkpoint for one of these stable reasons:

- `EXACT_BRANCH_CLOSURE` — the declared branch is exactly discharged;
- `NEW_KERNEL_EXPOSED` — a smaller unresolved theorem/arithmetic/effectivity dependency is isolated;
- `HOSTILE_AUDIT_REQUIRED` — a promotion boundary requires independent audit;
- `EXECUTION_RESOURCE_WALL` — a finite exact computation is specified but the current backend cannot complete it.

Low prospect, an unhelpful sample, a trivial-looking local evaluation, or external pessimism is not a mathematical stop condition.

## Stage33 anti-loop rules

These rules are stable. Current route names and current receiver ledgers belong in CURRENT/HISTORY, not here.

1. **Exact repeat prohibition.** Do not rerun a mathematically equivalent blocked/dominated route without a new hypothesis, adapter, or invariant.
2. **Semantic route-churn detection.** Renaming the same input, target, functor, and distinguishing invariant is not a new route.
3. **Two-batch stagnation trigger.** If two consecutive MAIN batches leave the active receiver, missing interface, live candidate information, and exact mathematical information unchanged, a third ordinary same-route continuation is forbidden; run breadth/route audit first.
4. **Wrong-weapon trigger.** If new evidence changes the mathematical species of the missing interface, broaden immediately rather than continuing with an associated but non-load-bearing invariant.
5. **Bookkeeping is not mathematical progress.** Controller edits, CI green status, source-lock restatement, and renamed coordinates do not reset stagnation unless they add new exact mathematics or permanently eliminate a distinct route.

The reusable repo-wide cycle policy remains:

`docs/research-os/policies/cycle-exploration-safety-protocol.md`

`LOOP-GUARD.md` is retained for historical compatibility and detailed prior examples, but its old current-receiver/candidate-ledger sections are not authoritative current state.

## Compact evidence and bounded context

Stage33 should keep exact evidence reproducible without making routine MAIN load or persist giant expanded objects.

For large generated evidence, prefer a compact committed interface containing:

```text
SOURCE_LOCKS
GENERATOR / deterministic invocation
CANONICAL_SHA256 of complete regenerated output
SEMANTIC_SUMMARY
EXIT_RELEVANT_INVARIANTS
REGEN_COMMAND
```

Expanded deterministic evidence should normally remain runner-local and be regenerated for verification. Do not commit or upload giant expanded artifacts by default when a compact deterministic certificate preserves the exact downstream invariants. Any exception must name the irreducible load-bearing data that cannot be reconstructed.

Routine context is tiered:

```text
HOT  = RULES + CURRENT + controller + active state + immediate current-leaf certificates/scripts
WARM = predecessor compact handoff/result and named interface definitions
COLD = giant generated JSON, old workflow logs, full PR diffs, audited ancestor internals
```

COLD material is loaded only for a named reason such as source-lock mismatch, certificate contradiction, a missing load-bearing representative/matrix, hostile-audit mode, or deterministic replay debugging. If the same cold detail must be rediscovered repeatedly, export it once into a compact reusable interface.

These Stage33 rules operate under the stricter repo-wide Actions storage policy in Research OS.

## MAIN startup order

For a Stage33 MAIN batch, read only what is needed in this order:

1. `AGENTS.md`
2. `stages/stage33/RULES.md`
3. `stages/stage33/CURRENT.md`
4. `stages/stage33/controller.json`
5. the active unit's authoritative state and only the certificates/scripts required by the current leaf

Before Actions/artifacts/heavy compute, read the Research OS Actions safety policy. Before claim promotion, closure, or downstream release, read the Research OS credit/promotion firewall.

## File-role invariant

Do not put current receiver/status into RULES. Do not put historical route ledgers into controller. Do not put stable policy into CURRENT. Do not delete failed/revoked certificates merely to simplify navigation; HISTORY should index them and their credit status.
