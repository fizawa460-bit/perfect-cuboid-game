# Stage14-num-α — Space-Diagonal Collision Engine

## Purpose

Stage14-num-α began as an experimental numerical side track asking whether the historical body-diagonal-first architecture could be converted into a materially faster **exact** Stage14 census engine without losing primitive two-face-or-more objects.

That validation phase is now complete. α1 through α8 established exact equivalence against the ordinary Stage14-num engine, a matched constant-factor speedup, safe primitive pruning, exact diagonal sharding, and a production-scale extension from the ordinary `B=150,000,000` frontier to exact `B=200,000,000`.

The ordinary Stage14-num results through `B=150,000,000` remain an independent regression oracle. Beyond that frontier, the validated α engine is the production extension path, with exact manifests and hash locks required at each new checkpoint.

## Frozen Stage14 target

```text
0<a<b<c
gcd(a,b,c)=1
a^2+b^2+c^2=d^2
d<=B
at least two integral face diagonals
```

Thus α's outer variable `d` is exactly the Stage14 physical cutoff. Searching `d<=B` covers the same finite height region.

## Completed validation and production phases

### α1 — exact dictionary: COMPLETE

Two ordered representations of one fixed `d^2`, together with a positive-square residual, are exactly equivalent to reconstructing a Stage14 cuboid with at least two integral face diagonals. Canonical deduplication separates exactly-two from triple witnesses.

### α2 — reference collision enumerator: COMPLETE

The deliberately simple diagonal-first implementation reproduced the ordinary exact census at the raw `(a,b,c,d,mask)` level and at the frozen B2m hashes.

### α3 — sum-of-two-squares generation audit: COMPLETE

Gaussian/Girard generation was corrected to preserve scaled representations and then matched the reference representation sets exactly.

### α4 — compressed collision engine: COMPLETE

The four ordered-role collision search was algebraically compressed to at most three positive residual candidates per unordered representation pair, with exact output preserved. Square-root calls were reduced substantially.

### α5 — primitive-safe sieve: COMPLETE

Only filters proved safe for the full primitive two-face-or-more population were admitted. In particular, primitive accepted objects force `d` to have only `1 mod 4` prime support; representation-count and pair-level common-divisor filters were proved and audited. Perfect-only historical congruence shortcuts remain disabled.

### α6 — independent equality matrix: COMPLETE

Raw-set equality against ordinary num was verified at multiple small cutoffs, and all frozen counts, graph fields and hashes matched at B2m, B5m and B10m.

### α7 — matched performance crossover: COMPLETE

On the same runner and exact-output semantics, the α engine was faster at every tested cutoff:

```text
B=200k   1.55x
B=500k   1.93x
B=1m     2.08x
B=2m     2.23x
```

This is a finite engineering speedup, not an asymptotic runtime theorem.

### α8 — production scaleout to B200m: COMPLETE

Eight disjoint body-diagonal shards extended the exact census beyond the ordinary B150m frontier. The α union restricted to B150m matched Stage14-num6 in every frozen field before the new shell was accepted.

Frozen B200m result:

```text
N_a^(2),N_b^(2),N_c^(2) = 957,967,533
N2 = 2457
T = 0
active oriented faces = 3563
raw pair edges = 2457
max degree = 11
N2/sqrt(B) = 0.17373613613753472
```

The change in `N2/sqrt(B)` from B150m to B200m is about `-3.85%`, so the large-census diagnostics are not yet declared stable.

## Post-B200m roadmap — explicit stopping rule

The numerical program no longer extends the cutoff merely because a larger number is possible. Its provisional terminal target is **B=500,000,000**. The purpose of the next checkpoints is to decide whether the principal normalized finite diagnostics have become empirically stable.

This is a deterministic exact census, not an iid random sample. The stability rule below is therefore an operational research diagnostic, **not** a confidence interval, p-value, or proof of an asymptotic law.

### Primary stability panel

At every checkpoint freeze the exact census and compute at least:

```text
R0 = N2/sqrt(B)
Ra = N_a^(2)/N2
Rb = N_b^(2)/N2
Rc = N_c^(2)/N2
Rg = active_oriented_face_vertices/N2
```

Also report, but do not use as primary stop-gate quantities:

```text
T(B)
shell counts by direction
raw pair edges
vertex repeat incidence rate
max degree
all exact object/mask/graph SHA locks
```

For a primary diagnostic `R`, define the checkpoint drift by

```text
relative_drift(R; B_old,B_new)
  = |R(B_new)-R(B_old)| / max(|R(B_new)|, 1e-30).
```

### Stage14-num-α9 — exact B300m extension, with B250m checkpoint

Run the validated segmented/sharded α engine through `B=300,000,000`. From the same exact object union freeze nested checkpoints at:

```text
B=250,000,000
B=300,000,000
```

Requirements:

- B200m nested regression reproduces α8 exactly;
- freeze counts, directional counts, `T`, graph fields, object SHA, object+mask SHA, vertex SHA and edge SHA at B250m and B300m;
- publish the first post-B200m stability panel;
- if `T>0`, stop the ordinary roadmap and enter the emergency independent-verification protocol before any mathematical claim.

### Stage14-num-α10 — exact B400m checkpoint

Extend to `B=400,000,000`, preserving the B200m/B250m/B300m nested manifests. Freeze the B400m exact census and update the stability matrix.

No early stopping is declared here: B400m exists to provide enough separated checkpoints for the terminal B500m decision.

### Stage14-num-α11 — exact B500m terminal checkpoint and stop gate

Extend to the provisional terminal cutoff

```text
B=500,000,000.
```

Evaluate each primary normalized diagnostic over the last three checkpoint transitions:

```text
250m -> 300m
300m -> 400m
400m -> 500m
```

The large-census program is considered **empirically stable enough to stop at B500m** if all of the following hold:

1. every exact integrity/hash/nesting gate passes;
2. `T(B)=0` through B500m;
3. every primary diagnostic `R0,Ra,Rb,Rc,Rg` has relative drift `<= 0.02` on **each** of those three transitions.

If this gate passes, set:

```text
LARGE_CENSUS_COMPLETE_AT_B500M=true
B1B_ESCALATION_REQUIRED=false
```

and park large-scale Stage14-num. Further numerical work should then be driven only by a named request from a proof lane or by a genuinely new structural diagnostic.

### Stage14-num-α12 — conditional B1B escalation only

`B=1,000,000,000` is **not automatic**. Open α12 only if the B500m stop gate fails materially while exact integrity remains sound, or if another Stage14 proof route requests a specifically defined larger-cutoff diagnostic.

If opened, α12 must declare its checkpoints and stopping test before computation starts; it must not become an indefinite "keep increasing B" loop.

### Stage14-num-αH — optional historical reproduction

Historical diagonal-interval reproduction is moved off the numbered critical path. `αH` may be used occasionally to validate old search architecture or compare historical almost-perfect data, but it never blocks α9–α11 and is never substituted for the exact Stage14 census.

## Emergency and non-goal rules

- `T>0` is an emergency verification event, not an automatic perfect-cuboid announcement. Recompute the candidate independently with ordinary/reference arithmetic and verify every edge, face diagonal, space diagonal and primitive condition exactly.
- `T=0` at any finite cutoff, including B500m or B1B, does **not** prove nonexistence.
- A 2% stability gate is a declared finite-data stopping convention, not evidence by itself for a limiting constant.
- Do not import historical perfect-only `11`/`19` or analogous pruning without a separate proof that it preserves the full Stage14 two-face-or-more population.
- Do not sacrifice exact two-face completeness for perfect-cuboid search speed.

## Locked roadmap state

```text
STAGE14_NUM_ALPHA_ROADMAP=POST_B200M_STABILITY_PLAN
ALPHA1_THROUGH_ALPHA8_COMPLETE=true
ORDINARY_NUM_B150M_REMAINS_INDEPENDENT_REGRESSION_ORACLE=true
ALPHA_PRODUCTION_EXACT_CUTOFF_B=200000000
PROVISIONAL_LARGE_CENSUS_TARGET_B=500000000
STABILITY_CHECKPOINTS_B=250000000,300000000,400000000,500000000
STABILITY_RELATIVE_DRIFT_THRESHOLD=0.02
STABILITY_REQUIRED_CONSECUTIVE_TRANSITIONS=3
STABILITY_IS_HEURISTIC_NOT_CONFIDENCE_INTERVAL=true
FINITE_CENSUS_ASYMPTOTIC_CLAIM=false
B1B_ESCALATION_AUTOMATIC=false
PERFECT_CUBOID_EMERGENCY_ON_T_POSITIVE=true
HISTORICAL_REPRODUCTION_MOVED_TO_ALPHA_H=true
NEXT=Stage14-num-alpha9 exact B300m extension with nested B250m/B300m stability checkpoints
```
