# Stage33 anti-loop / route-churn guard

Purpose: allow MAIN to keep moving aggressively while preventing silent infinite research loops, especially repeated attacks on the same receiver under renamed invariants.

This guard supplements `docs/research-os/policies/cycle-exploration-safety-protocol.md`. It does not require every batch to close a milestone. It requires every continuing batch to produce a distinguishable mathematical state transition or to explicitly broaden.

## Batch state vector

At the end of every Stage33 MAIN batch, classify the mathematical state by:

```text
ACTIVE_RECEIVER
ACTIVE_MISSING_INTERFACE
LOAD_BEARING_INVARIANTS
LIVE_CANDIDATE_COUNT
UNTESTED_CANDIDATE_COUNT
NEW_EXACT_INFORMATION
ROUTES_NEWLY_BLOCKED_OR_PROVED_EQUIVALENT
```

Bookkeeping, controller edits, verifier wiring, CI green status, source-lock restatement, renamed coordinates, and a reformulation with no new theorem/adapter/invariant do **not** count as `NEW_EXACT_INFORMATION` by themselves.

A route rejection does count as exact information only when it permanently removes a mathematically distinct candidate or proves an exact equivalence/dominance relation that prevents re-entry under another name.

## Hard loop rules

### 1. Exact repeat prohibition

If the current proposal is exactly equivalent to a previously BLOCKED/EQUIVALENT/DOMINATED route, do not execute it again. Record the reduction and choose another live candidate.

### 2. Semantic route-churn detection

Different names are not different routes when they attempt to extract the same missing bit through the same mathematical functor/invariant class. Before launching a new route, compare its input object, target object, map/functor, and claimed distinguishing invariant with the candidate ledger.

Examples of a single route family rather than independent progress include repeated attempts to distinguish the same Brauer class using only Picard-discriminant symmetry signatures (Galois fixedness, automorphism fixedness, relabelled Smith coordinates) after that family has been proved non-separating.

### 3. Two-batch stagnation trigger

If two consecutive MAIN batches satisfy all of:

```text
ACTIVE_RECEIVER unchanged
ACTIVE_MISSING_INTERFACE unchanged
LIVE_CANDIDATE_COUNT unchanged
no new load-bearing invariant/theorem/adapter
no candidate permanently removed by an exact block/equivalence
```

then a third ordinary MAIN continuation on the same route is forbidden.

Automatically run `EXHAUSTIVE_VIEW_AUDIT` plus `BLIND_REDISCOVERY` before further narrowing.

### 4. Wrong-weapon trigger

Immediately broaden, without waiting for two batches, when a newly proved fact changes the mathematical species of the receiver or target. Examples: discovering that two equal-cardinality groups are different quotients; learning that the required map lives in cohomology rather than the Picard discriminant; or proving that the active symmetry group acts trivially on the target.

The breadth audit must ask explicitly whether the current tool family attacks the actual load-bearing interface, rather than merely an associated object.

### 5. Progress reset rule

The stagnation counter resets only when at least one of these occurs:

- the receiver is strictly reduced;
- a missing interface is constructed or its domain/codomain is sharpened;
- a new load-bearing invariant is proved;
- a live candidate is permanently eliminated by exact proof;
- a genuinely new mathematical route is introduced by an exhaustive/blind audit;
- a theorem/source-lock supplies a previously missing semantic adapter.

A new certificate that only records already-known facts does not reset the counter.

## Candidate ledger for Stage33-12 current receiver

Current receiver:

```text
named CV J2 class -> Br(Kc)[2] = Hom(T(Kc), Z/2)
T(Kc) ~= <4> direct_sum <8>
```

Current live/untested route families after the 2026-08-29 loop audit:

1. `BRANCH_COHOMOLOGICAL_MAP` — LIVE / preferred. Compute the branch-normalization 2-torsion to K3 `H^2(mu_2)`/Brauer map directly, then read its functional in the fixed transcendental target.
2. `SHIODA_INOSE_OR_CM_MODEL_MARKING` — UNTESTED. Identify an explicit singular-K3/CM model compatible with `T=<4,8>` and transport the named class through a proved model adapter.
3. `DIRECT_TOPOLOGICAL_OR_BFIELD_CYCLE_EVALUATION` — LIVE. Construct/evaluate on marked transcendental cycles `t1,t2` directly.
4. `GOOD_REDUCTION_ETALE_SPECIALIZATION` — UNTESTED. Use a proved specialization/Frobenius adapter if it distinguishes the named class without silently changing the receiver.

Previously rejected route families must not be resurrected under new names without a new hypothesis or adapter:

- direct HS-d2 parity as a Picard-discriminant orientation bit;
- unsupported classical Kummer `(16_6)` transfer;
- historical Smith frame alone;
- Picard-discriminant `ct`/full-Galois fixed-line signatures;
- Kc automorphism/sign/swap signatures;
- unique-isotropic discriminant-vector selection;
- any selector that identifies `(T*/T)[2]` with `Br(Kc)[2]` without the required semantic adapter.

## Required MAIN exit fields

Every future Stage33 MAIN result/controller checkpoint should keep these conceptually current:

```text
LOOP_GUARD_ACTIVE=true
LOOP_STAGNATION_COUNT=<0|1|2>
LOOP_ACTIVE_RECEIVER=<exact object>
LOOP_ACTIVE_MISSING_INTERFACE=<exact map/adapter>
LOOP_NEW_EXACT_INFORMATION=<short statement or NONE>
LOOP_CANDIDATES_REMOVED_THIS_BATCH=<count>
LOOP_EXHAUSTIVE_VIEW_AUDIT_REQUIRED=<true|false>
LOOP_BLIND_REDISCOVERY_REQUIRED=<true|false>
```

If `LOOP_STAGNATION_COUNT=2`, normal same-route MAIN continuation is prohibited until the breadth audit runs.

## Safety invariant

The objective is not to guarantee that research never revisits an idea. That is impossible in open mathematics. The objective is to guarantee that Stage33 does not unknowingly spend unbounded batches on the same mathematical interface merely because the attempted invariant has been renamed.
