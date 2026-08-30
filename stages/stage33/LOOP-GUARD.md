# Stage33 anti-loop / route-churn guard

This file is retained as the detailed Stage33 anti-loop compatibility document. Stable policy is summarized authoritatively in `RULES.md`.

**Current receiver, live routes, candidate counts, and current missing interfaces do not belong here.** Read them from `CURRENT.md`, `controller.json`, and the active unit state. Historical route ledgers belong in `HISTORY.md`, unit results, certificates, and Git history.

This guard supplements `docs/research-os/policies/cycle-exploration-safety-protocol.md`.

## Batch state vector

At the end of a Stage33 MAIN batch, conceptually track:

```text
ACTIVE_RECEIVER
ACTIVE_MISSING_INTERFACE
LOAD_BEARING_INVARIANTS
LIVE_CANDIDATE_COUNT
UNTESTED_CANDIDATE_COUNT
NEW_EXACT_INFORMATION
INDEPENDENT_OBSERVATIONS
ROUTES_NEWLY_BLOCKED_OR_PROVED_EQUIVALENT
```

These values are **dynamic state**. Store them in controller/active state when needed, not in this rule document.

Bookkeeping, controller edits, verifier wiring, CI green status, source-lock restatement, renamed coordinates, and a reformulation with no new theorem/adapter/invariant do not count as `NEW_EXACT_INFORMATION` by themselves.

A route rejection counts as exact information only when it permanently removes a mathematically distinct candidate or proves an exact equivalence/dominance relation that prevents re-entry under another name.

## Hard loop rules

### 1. Exact repeat prohibition

If a proposal is exactly equivalent to a previously blocked/equivalent/dominated route, do not execute it again unless there is a genuinely new hypothesis, adapter, invariant, or target.

### 2. Semantic route-churn detection

Different names are not different routes when they attempt to extract the same missing bit through the same mathematical functor/invariant class. Before launching a route, compare its input object, target object, map/functor, and claimed distinguishing invariant with prior work.

### 3. Relabeling is not progress

A bijective relabeling of the same live candidates into new coordinates, lattices, signatures, or case names does not reset stagnation unless it also produces an independent observable, constructs the missing semantic interface, or permanently removes a candidate/route.

### 4. Two-batch stagnation trigger

If two consecutive MAIN batches satisfy all of:

```text
ACTIVE_RECEIVER unchanged
ACTIVE_MISSING_INTERFACE unchanged
LIVE_CANDIDATE information unchanged
no independent observation acquired
no candidate or materially distinct route permanently removed
no missing semantic interface constructed
```

then a third ordinary continuation on the same route is forbidden.

Run breadth/route audit (`EXHAUSTIVE_VIEW_AUDIT` / `BLIND_REDISCOVERY` or the current equivalent) before further narrowing.

### 5. Wrong-weapon trigger

Broaden immediately when a newly proved fact changes the mathematical species of the receiver or missing interface. Do not continue attacking an associated object after it is known not to carry the load-bearing information.

### 6. Progress reset rule

The stagnation counter resets only when at least one materially new event occurs, such as:

- a live candidate set strictly decreases;
- an independent observable is computed rather than inferred from a candidate assumption;
- the missing semantic interface/adapter itself is constructed;
- a new theorem/source-lock supplies the required transport/descent map;
- an exact route equivalence permanently removes a materially distinct live route;
- the active receiver changes because the prior receiver was exactly discharged or replaced by a smaller kernel.

A new certificate that only records already-known facts does not reset the counter.

## MAIN exit fields

When loop tracking is load-bearing, keep these conceptually current in controller/active state:

```text
LOOP_GUARD_ACTIVE=true
LOOP_STAGNATION_COUNT=<0|1|2>
LOOP_ACTIVE_RECEIVER=<exact object>
LOOP_ACTIVE_MISSING_INTERFACE=<exact map/adapter>
LOOP_NEW_EXACT_INFORMATION=<short statement or NONE>
LOOP_INDEPENDENT_OBSERVATION=<short statement or NONE>
LOOP_CANDIDATES_REMOVED_THIS_BATCH=<count>
LOOP_EXHAUSTIVE_VIEW_AUDIT_REQUIRED=<true|false>
LOOP_BLIND_REDISCOVERY_REQUIRED=<true|false>
```

If `LOOP_STAGNATION_COUNT=2`, normal same-route MAIN continuation is prohibited until the breadth audit runs.

## Historical route ledgers

Older versions of this file contained a Stage33-12-specific current receiver, the three `[1,0]`, `[0,1]`, `[1,1]` candidates, named LIVE route families, and rejected route lists. Those entries were useful at that time but became stale as the repair moved on.

They are intentionally removed from the live rule file. Recover them from Git history and use `HISTORY.md` / per-unit results as the historical index. Their removal does not revive any rejected route or revoke any valid certificate.

## Safety invariant

The objective is not to prohibit revisiting an idea when genuinely new mathematics appears. The objective is to prevent unbounded repeated attacks on the same missing interface merely because the attempted invariant or route has been renamed.
