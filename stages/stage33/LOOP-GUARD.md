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
J2_INDEPENDENT_OBSERVATIONS
ROUTES_NEWLY_BLOCKED_OR_PROVED_EQUIVALENT
```

Bookkeeping, controller edits, verifier wiring, CI green status, source-lock restatement, renamed coordinates, and a reformulation with no new theorem/adapter/invariant do **not** count as `NEW_EXACT_INFORMATION` by themselves.

A route rejection counts as exact information only when it permanently removes a mathematically distinct candidate or proves an exact equivalence/dominance relation that prevents re-entry under another name.

## Hard loop rules

### 1. Exact repeat prohibition

If the current proposal is exactly equivalent to a previously BLOCKED/EQUIVALENT/DOMINATED route, do not execute it again. Record the reduction and choose another live candidate.

### 2. Semantic route-churn detection

Different names are not different routes when they attempt to extract the same missing bit through the same mathematical functor/invariant class. Before launching a new route, compare its input object, target object, map/functor, and claimed distinguishing invariant with the candidate ledger.

Examples of a single route family rather than independent progress include repeated attempts to distinguish the same Brauer class using only Picard-discriminant symmetry signatures (Galois fixedness, automorphism fixedness, relabelled Smith coordinates) after that family has been proved non-separating.

### 3. Three-candidate relabeling rule

For the current Stage33-12 receiver, the repeated appearance of

```text
[1,0], [0,1], [1,1]
```

is expected because these are the three nonzero elements of `Br(Kc)[2] ~= F2^2`. Their reappearance is not by itself a loop.

However, a construction that merely maps these three candidates bijectively to three new labels, three new lattices, three new signatures, or three new cases **does not reset the stagnation counter** unless it also produces at least one independent datum from the named J2 side or removes at least one candidate.

Examples:

```text
3 Brauer candidates -> 3 kernel-lattice fingerprints        structural preparation only
named J2 -> observed elliptic 2-torsion / cycle value / local invariant  independent J2 datum
3 candidates -> 2 or 1 candidates                           receiver reduction
```

### 4. Two-batch stagnation trigger

If two consecutive MAIN batches satisfy all of:

```text
ACTIVE_RECEIVER unchanged
ACTIVE_MISSING_INTERFACE unchanged
LIVE_CANDIDATE_COUNT unchanged
no named-J2 independent observation acquired
no candidate permanently removed by an exact block/equivalence
```

then a third ordinary MAIN continuation on the same route is forbidden.

Automatically run `EXHAUSTIVE_VIEW_AUDIT` plus `BLIND_REDISCOVERY` before further narrowing.

### 5. Wrong-weapon trigger

Immediately broaden, without waiting for two batches, when a newly proved fact changes the mathematical species of the receiver or target. Examples: discovering that two equal-cardinality groups are different quotients; learning that the required map lives in cohomology rather than the Picard discriminant; or proving that the active symmetry group acts trivially on the target.

The breadth audit must ask explicitly whether the current tool family attacks the actual load-bearing interface, rather than merely an associated object.

### 6. Progress reset rule

For Stage33-12's current three-candidate marking problem, the stagnation counter resets only when at least one of these occurs:

- the live Brauer candidate count strictly decreases;
- a named-J2-side independent observable is computed that was not inferred by assuming one of the three Brauer candidates;
- the missing semantic interface itself is constructed;
- a theorem/source-lock supplies the actual transport adapter from a J2-side observable to the marked Brauer receiver;
- an exact route equivalence permanently removes a materially distinct live route from the ledger.

A bijective relabeling of the same three candidates does not reset the counter. A new certificate that only records already-known facts does not reset the counter.

## Candidate ledger for Stage33-12 current receiver

Current receiver:

```text
named CV J2 class -> Br(Kc)[2] = Hom(T(Kc), Z/2)
T(Kc) ~= <4> direct_sum <8>
```

Current route families:

1. `BRANCH_COHOMOLOGICAL_MAP` — EQUIVALENT / ARCHIVED. It constructs the same abstract named Brauer class but does not mark it in `Hom(T,Z/2)`.
2. `KERNEL_LATTICE_FINGERPRINT_IDENTIFICATION` — LIVE. The three Brauer candidates have pairwise non-isometric index-two kernels; this is a comparison dictionary, not by itself a J2 observation.
3. `SHIODA_INOSE_OR_CM_MODEL_MARKING` — LIVE / NATURAL NEXT TRANSPORT. Seek an explicit CM/Shioda-Inose adapter carrying an independently observed J2 elliptic-torsion datum to the K3 transcendental marking.
4. `DIRECT_TOPOLOGICAL_OR_BFIELD_CYCLE_EVALUATION` — LIVE. Construct/evaluate on marked transcendental cycles `t1,t2` directly.
5. `GOOD_REDUCTION_ETALE_SPECIALIZATION` — UNTESTED. Use a proved specialization/Frobenius adapter if it distinguishes the named class without silently changing the receiver.

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
LOOP_J2_INDEPENDENT_OBSERVATION=<short statement or NONE>
LOOP_CANDIDATES_REMOVED_THIS_BATCH=<count>
LOOP_EXHAUSTIVE_VIEW_AUDIT_REQUIRED=<true|false>
LOOP_BLIND_REDISCOVERY_REQUIRED=<true|false>
```

If `LOOP_STAGNATION_COUNT=2`, normal same-route MAIN continuation is prohibited until the breadth audit runs.

## Safety invariant

The objective is not to guarantee that research never revisits an idea. That is impossible in open mathematics. The objective is to guarantee that Stage33 does not unknowingly spend unbounded batches on the same mathematical interface merely because the attempted invariant has been renamed.
