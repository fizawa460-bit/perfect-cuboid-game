# Post-Stage29 research OS handoff

This file is a restart guide, not a new Stage29 task.

## Stable frontier

After final audit, future work should begin from the 13 active kernels recorded in `final-handoff.json`, not by replaying Stage29 theorem searches or reopening all 46 receivers.

The default recursion rule is:

```text
kernel
  -> dependency DAG
  -> bounded work packages
  -> leaf-level 1/2/3/4 reclassification
```

At every decomposition level:

- Class 1: execute now and archive the result;
- Class 2: split further until the concrete model/CAS/code/certificate wall is explicit;
- Class 3: state the minimum missing theorem and record exact downstream consequence;
- Class 4: park with a falsifiable reactivation trigger.

A Class-2 route may expose a new Class-3 theorem wall. A Class-3 route may drop to Class 2 if a special-structure reduction turns the general theorem into a finite exact computation. Both are expected outcomes.

## Computational track

The four initial Class-2 roots are:

1. `K16-C2-LOWGENUS-PICARD-PRODUCTION`
2. `K16-C2-MODULAR-S4-ACTION`
3. `K16-C2-BRAUER-EXPLICIT-CHAIN` — treat as a dependency DAG despite the retained compatibility name
4. `K16-C2-EXT-E-INTEGRAL-CERTIFICATION`

A future roadmap may order these by algorithmic tractability or research value, but Stage29 itself does not impose an order.

For each computational leaf, require:

```text
exact input object
exact output/certificate
software/runtime assumptions
reproducible command or manifest
independent checker or mathematical invariant
failure mode
next dependency edges
```

Do not grant mathematical closure from a numerical heuristic, approximate rank, unsourced CAS transcript or non-reproducible black-box output.

## New-theorem track

The nine Class-3 roots are retained without priority lock. They vary from narrow problem-specific statements to broad arithmetic frontiers.

`K16-C3-PESCH-EXPONENT-ONE` has the clearest audited direct nonexistence implication if its conjectural statement is proved. This does not require it to be attacked first.

`K16-C3-TERMINAL-P-OVER-M3` and `K16-C3-M3-LOCAL-TO-GLOBAL` are broad and mathematically difficult, while a successful density theorem would not automatically imply endpoint emptiness.

A theorem-forge workflow should record for every target:

```text
minimal theorem statement
nearest published theorem
hypothesis mismatch
perfect-cuboid-specific structure available
proof experiments/counterexample search
which receivers close if proved
whether endpoint existence/nonexistence follows
independent mathematical interest
```

## External AI handoff

An independent AI review (Claude or another system) may be useful after Stage29 close, especially for:

- challenging whether a Class-3 item can actually be reduced to Class 2;
- finding a missed decomposition of a large Class-2 kernel;
- proposing alternate dependency DAGs or theorem formulations;
- ranking the 13 kernels by difficulty, tractability and decision value.

Every external-AI output remains unverified input. No theorem, route, color or receiver may change without source lock, exact theorem verification, duplication check and exact endpoint/physical adapter verification.

## Anti-loop rule

Do not reopen Stage29 merely to rename the same wall.

Reentry is justified only by at least one of:

1. a new published theorem/preprint materially changes a Class-3 applicability verdict;
2. a Class-2 execution produces new exact structure that changes the dependency graph;
3. a dormant Class-4 trigger actually fires;
4. a genuinely new route with a distinct endpoint consequence is found;
5. an audited contradiction is found in a frozen Stage29 result.
