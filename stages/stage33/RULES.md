# Stage33 rules

Stage33 inherits all repo-wide rules in `AGENTS.md` and `docs/research-os/`. Stage-local rules may strengthen those rules but never weaken them. Repo-wide Actions/storage, research-credit/promotion, cycle-exploration, and claim firewalls are not restated here; read the authoritative Research OS policy when its trigger applies.

This file contains only Stage33-specific scope, authority, release, and context-routing rules. Current receivers, live routes, progress, and batch findings do not belong here.

## Authority layers

Use Stage33 material in this order:

1. `AGENTS.md` and `docs/research-os/` — repo-wide policy.
2. `stages/stage33/RULES.md` — stable Stage33-specific rules.
3. `stages/stage33/MAIN-STATE.json` — compact generated projection for ordinary MAIN startup.
4. `stages/stage33/controller.json` and active unit state — detailed current machine state and mathematics.
5. `stages/stage33/CURRENT.md`, `stages/stage33/HISTORY.md`, unit results/audits/certificates/scripts, and Git history — human dashboard, historical work, and evidence.

If historical plan/status conflicts with MAIN-STATE/controller/active authoritative state, the current authoritative state wins. Certificate claims remain limited to their declared scope.

## Frozen Stage33 scope

Stage33 executes the frozen Stage29 physical-open Brauer kernel `K16-C2-BRAUER-EXPLICIT-CHAIN` / `BRAUER-EXPLICIT-DAG`.

The frozen scope includes the Stage29-retained open-algebraic contribution, physical-boundary residue contribution, and two-primary geometric/transcendental contribution. No surviving class may be silently discarded because a later sub-route is two-primary.

Detailed unit acceptance criteria live in:

`stages/stage33/33-00/unit-closure-contract.md`

## Progress and release law

Stage33 has 11 big tasks. Repair children do not independently increment that denominator.

A big task releases dependent downstream work only when the unit-closure contract marks the required state exact and audited. Partial, preview, numerical, blocked, or audit-pending states do not count as closed.

Repair-child completion does not automatically close its reopened parent; the parent closes only after the required repair chain and hostile recertification succeed.

## Stage33 bounded stop conditions

A Stage33 line may stop/checkpoint only as one of:

- `EXACT_BRANCH_CLOSURE`
- `NEW_KERNEL_EXPOSED`
- `HOSTILE_AUDIT_REQUIRED`
- `EXECUTION_RESOURCE_WALL`

The detailed meanings and generic anti-loop/parking rules are inherited from Research OS. Low prospect, an unhelpful sample, a trivial-looking local evaluation, or external pessimism is not by itself a mathematical stop condition.

## Stage33 anti-loop routing

Apply the repo-wide Cycle Exploration Safety Protocol. Stage33 adds only these routing requirements:

- current receiver/candidate/route state belongs in generated MAIN-STATE/controller/active state, not RULES;
- `LOOP-GUARD.md` is compatibility/history, not current-state authority;
- after a material receiver change, do not continue an obsolete associated route merely because its artifacts still exist;
- bookkeeping or relabeling does not change Stage33 progress or release status.

## Compact evidence and bounded context

Use the repo-wide evidence/storage policy for exact evidence. For routine Stage33 context, use:

```text
HOT  = MAIN-START-HERE + MAIN-STATE + immediate current-leaf certificates/scripts
WARM = predecessor compact handoff/result and named interface definitions
COLD = giant generated JSON, old workflow logs, full PR diffs, audited ancestor internals
```

Load COLD material only for a named reason such as source-lock mismatch, certificate contradiction, missing load-bearing data, hostile audit, or deterministic replay debugging. If the same COLD detail is repeatedly needed, export a compact reusable interface instead.

## MAIN startup order

For a routine Stage33 MAIN batch, `AGENTS.md` routes startup through
`MAIN-START-HERE.md`. Read only what is needed in this order:

1. `AGENTS.md`
2. `stages/stage33/MAIN-START-HERE.md`
3. `stages/stage33/MAIN-STATE.json`
4. only the immediate files named by `current_leaf_working_set`

Do not read RULES, CURRENT, the full controller, compatibility shims, old
Stage33-05 state, roadmaps, or HISTORY merely because they exist. The startup
constitution names the exact triggers that authorize expanding to those layers.
After writes, regenerate and verify MAIN-STATE with `sync_main_state.py`.

Read additional Research OS policy only when its trigger applies, especially before Actions/heavy compute, claim promotion, closure/release, hostile audit, or breadth/parking decisions.

## File-role invariant

- RULES: stable Stage33-specific policy only.
- MAIN-STATE: generated compact startup projection; never hand-edit it.
- controller: detailed current status, receiver, missing interface, and release state.
- CURRENT: optional human dashboard, not ordinary MAIN startup input.
- active unit state: detailed current mathematics.
- HISTORY/results/audits/certificates/Git: historical evidence and provenance.

Do not duplicate mutable state across these layers merely for convenience, and do not delete failed/revoked evidence merely to simplify navigation.
