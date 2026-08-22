# Cycle Exploration Safety Protocol

Purpose: keep the fast single-active-route cycle workflow while reducing the risk that optimization, Arsenal anchoring, or repeated narrowing silently discards a mathematically distinct route.

This protocol is repository-wide and is intended to be invoked by future cycle prompts with one instruction: **apply the Cycle Exploration Safety Protocol**. Human operators should not need to remember when to switch modes manually.

## 1. Default operating mode: one active route

Keep one active receiver/gate whenever possible. Do not split merely because several ideas can be named.

For each audited substage classify the result as one of:

- `PASS_NEXT_GATE_UNCHANGED`: the current route remains legal and should continue.
- `PASS_NEW_GATE_FROM_STRONGER_VIEW`: the audited route remains valid, but a strictly stronger or cleaner formulation/receiver has been proved; replace the active gate with it.
- `BLOCKED_NEW_PATTERN_ISOLATED`: the attempted route is blocked, but the failure exposes a new exact obstruction, invariant, receiver, theorem species, or legal charge candidate; freeze the block and continue from the new pattern.
- `BLOCKED_NO_NEW_INFORMATION`: the route is closed and adds no new live mathematical object; archive it and choose the best remaining live candidate.
- `SPLIT_TRIGGERED_DISTINCT_OBSTRUCTIONS`: two or more live routes are proved genuinely non-equivalent and neither depends on resolving the other. Only then open parallel branches.

A `BLOCK` is not a command to stop the research cycle. Freeze the reason, prohibit unsupported reuse, and route to the next legal candidate.

## 2. Candidate ledger

Every cycle must maintain, explicitly or in its frozen exit, a candidate ledger with statuses:

- `LIVE`: currently active or immediately actionable.
- `UNTESTED`: mathematically distinct candidate not yet audited enough to discard.
- `EQUIVALENT`: exact reduction to an already-audited route has been exhibited.
- `DOMINATED`: a proved stronger formulation subsumes it without losing hypotheses, masks, measure, or uniformity.
- `BLOCKED`: a named obstruction prevents the required receiver.

Do not erase an `UNTESTED` candidate merely because it resembles a known route. To mark `EQUIVALENT`, record an exact reduction or identity. To mark `DOMINATED`, state the implication and verify all physical filters, quantifiers, measures, and no-recharge constraints.

## 3. Anti-optimization triggers

The cycle agent must decide automatically whether to broaden. Human prompting is not required.

Run an `EXHAUSTIVE_VIEW_AUDIT` when any of the following occurs:

1. the current receiver is described as minimal, naked, unique remaining object, or equivalent language;
2. three or more materially different attempted routes since the last broad audit are `BLOCKED` without proving the target;
3. the same essential receiver survives two consecutive cycle batches despite reformulation;
4. a new exact invariant/core/lattice/height identity materially changes the geometry or counting variables;
5. the active route would otherwise be parked at an external theorem gate;
6. the agent has high uncertainty that the candidate ledger covers the natural mathematical viewpoints.

A cycle may trigger the audit earlier when the cost is small relative to the risk of premature parking.

## 4. EXHAUSTIVE_VIEW_AUDIT

This is a breadth audit, not a demand to prove every idea.

Given the exact current receiver and physical masks:

1. Enumerate materially distinct mathematical lenses that could attack, reparameterize, majorize, dualize, average, localize, or reconstruct the receiver.
2. Include, when structurally relevant, exact algebra/parametrization, divisibility and valuations, lattice/congruence geometry, Gaussian or other norm-form structure, sieve/large-sieve/dispersion, analytic first or second moments, geometry of numbers, elliptic/genus-one/descent methods, toric/universal-torsor viewpoints, incidence/energy methods, local-global or adelic formulations, and height changes. This list is suggestive, not exhaustive.
3. Compare every generated candidate against the ledger and Arsenal.
4. Classify it `LIVE`, `UNTESTED`, `EQUIVALENT`, `DOMINATED`, or `BLOCKED`.
5. Preserve every `UNTESTED` candidate in the ledger even if it is not selected as the next active route.
6. Select the next active route by expected information gain and closeness to the receiver, not by familiarity alone.

Never claim that all mathematically possible viewpoints have been exhausted. The auditable claim is only that the generated candidate set was classified without silently discarding unresolved distinct candidates.

## 5. BLIND_REDISCOVERY

To reduce Arsenal anchoring, every `EXHAUSTIVE_VIEW_AUDIT` must contain a blind pass.

Blind pass rules:

1. Work from the exact receiver, hypotheses, masks, height, and required quantitative target.
2. Temporarily do not consult Arsenal route recommendations or prior route names while generating candidate viewpoints.
3. Generate independent candidate formulations and attacks.
4. Only after generation, compare them with Arsenal and the historical BLOCK ledger.
5. Record any candidate that is absent from the Arsenal as `UNTESTED` or `LIVE` unless an exact reduction/block is then proved.

The blind pass does not forbid using known mathematics. It forbids letting the repository's preferred historical routes determine the initial candidate list.

## 6. Parallelization rule

Default: do not parallelize.

Set `SPLIT_TRIGGERED_DISTINCT_OBSTRUCTIONS` only when all are true:

- at least two candidates remain `LIVE` or high-value `UNTESTED`;
- an exact audit shows they are not merely different coordinates for the same receiver;
- neither route requires the immediate output of the other;
- running them separately reduces wall-clock or context risk enough to justify merge/reconciliation cost.

Otherwise keep one active route and preserve the others in the ledger.

## 7. No-recharge and cross-promotion firewall

Broad exploration does not relax proof discipline. Every new route must still audit:

- whether a core/invariant has already been charged;
- whether a local/fixed-packet/fixed-height statement is being promoted to the whole family;
- whether measures and weights are interchangeable;
- whether exceptional sets have a proved adapter;
- whether physical filters and primitivity are preserved;
- whether an apparent new congruence is algebraically identical to an existing lock;
- whether an external theorem has the required uniformity window.

A novel viewpoint that fails these checks is `BLOCKED`, not a saving.

## 8. Parking rule

Do not park a receiver merely because the currently preferred route is blocked.

Before parking at a theorem gate, require:

- the current candidate ledger has no unprocessed `LIVE` candidate;
- all generated alternatives are `BLOCKED`, `EQUIVALENT`, `DOMINATED`, or explicitly retained as `UNTESTED` with a reason they cannot presently be audited;
- an `EXHAUSTIVE_VIEW_AUDIT` and `BLIND_REDISCOVERY` have been run since the last material receiver change;
- the exact missing theorem/adapter is stated with quantifiers, measure, height, masks, and required exponent;
- the exit does not claim impossibility unless impossibility was actually proved.

## 9. Required cycle exit fields

Where practical, append these fields to future frozen cycle exits:

```text
CYCLE_ROUTE_STATUS=<one of the five route statuses>
CYCLE_ACTIVE_RECEIVER=<exact current receiver>
CYCLE_LIVE_CANDIDATES=<count>
CYCLE_UNTESTED_CANDIDATES=<count>
CYCLE_EXHAUSTIVE_VIEW_AUDIT=<true|false>
CYCLE_BLIND_REDISCOVERY=<true|false>
CYCLE_SPLIT_TRIGGERED=<true|false>
CYCLE_PARKING_AUDIT_COMPLETE=<true|false>
```

If an audit generated a new route, also record:

```text
CYCLE_NEW_VIEW=<short exact description>
CYCLE_NEW_VIEW_SOURCE=<ARSENAL|BLIND|BOTH|INTERNAL_DERIVATION>
```

## 10. Human operator contract

The human operator may continue to issue a single generic cycle command. The agent is responsible for deciding whether the next action is continuation, reframing, broadening, blind rediscovery, or a justified split.

The human operator should only need to intervene for scope changes, resource limits, publication/review decisions, or genuinely ambiguous research goals.

## 11. Safety invariant

Fast narrowing is the default. Periodic deliberate de-optimization is mandatory when the triggers fire.

The protocol does **not** guarantee that every possible mathematical idea has been considered. It is designed to guarantee something narrower and auditable: generated distinct candidates are not silently discarded, historical Arsenal knowledge does not monopolize idea generation, and parking occurs only after an explicit breadth audit.