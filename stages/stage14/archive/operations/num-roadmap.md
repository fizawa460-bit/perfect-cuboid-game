# Stage14-num roadmap — independent numerical observatory

> STATUS: `STAGE14_NUM_ROADMAP=READY`
>
> PURPOSE: maintain a proof-independent, exact finite-data observatory for Stage14.  The num track does **not** prove asymptotics.  It extends exact censuses, profiles/scales the enumerator, records stable object-level fingerprints, and reports anomalies back to the proof tracks.

## 0. Mission and separation of duties

Stage14 now has several fast-moving proof tracks (`14-4`, `14-t`, `14-s`, `14-e`, literature radar, and Stage13 repair work).  The numerical observatory is deliberately orthogonal to them.

The num track owns:

- exact finite enumeration under the frozen Stage14 physical definitions;
- performance engineering and reproducibility of that enumeration;
- common-cutoff ledgers shared by proof tracks;
- moving-window finite diagnostics and anomaly detection;
- independent cross-checks between distinct generation routes.

The num track does **not** own:

- asymptotic theorems;
- extrapolated existence/nonexistence claims;
- proof of a `sqrt(B)` law;
- proof of directional limits;
- proof of perfect-cuboid existence/nonexistence;
- reinterpretation of theorem-level results from other tracks.

Permanent locks:

```text
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
PROOF_TRACK_INDEPENDENT=true
SQRT_B_ASYMPTOTIC_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Frozen Stage14 population contract

Every num-stage census uses the canonical primitive cuboid convention

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\]

with integer space diagonal

\[
a^2+b^2+c^2=d^2,\qquad d\le B.
\]

Write the three face-square indicators for

\[
a^2+b^2,\qquad a^2+c^2,\qquad b^2+c^2.
\]

The main exact-two directional counts are

\[
N_a^{(2)},\qquad N_b^{(2)},\qquad N_c^{(2)},
\]

where `a/b/c` denotes the shared smallest/middle/largest edge respectively, and

\[
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}.
\]

The triple count `T` is retained without assuming it vanishes.

Frozen baseline through `B=2,000,000`:

```text
(N_a^(2), N_b^(2), N_c^(2)) = (142, 134, 80)
N_2 = 356
T = 0
```

No Stage14-num implementation may advance beyond num1 until it reproduces these locks exactly using at least two logically distinct routes or one route plus an independently frozen object ledger.

## 2. Canonical object identity

Every physical cuboid object must have a stable canonical key

```text
(a,b,c,d)
```

with `0<a<b<c`.

Derived face/vertex records must point back to this key rather than relying on row order or generator-specific IDs.

For oriented first-face/fiber records, the canonical face key is

```text
(S,X,H)
```

in reduced primitive Pythagorean form, together with an explicit orientation label.  Any Selmer/Kummer/height fingerprint imported from another track must be attached by this canonical key and must retain the source stage/commit.

## 3. Data tiers

The observatory separates three data tiers.

### Tier A — exact census locks

Counts and object ledgers reproduced exactly by deterministic code.

Examples:

```text
N_a^(2), N_b^(2), N_c^(2), N_2, T
raw pair overlaps
active first-face vertices
first-hit heights
Euler-brick counts at matching cutoffs
```

### Tier B — deterministic derived diagnostics

Computed exactly from Tier A, but not mathematical theorems.

Examples:

```text
N_2/sqrt(B)
direction proportions
first-hit multiplicity distribution
canonical-height summaries
moving-window effective exponents
curve/fiber fingerprints
```

### Tier C — heuristic fits

Regression, extrapolation, changepoint, or model-selection output.

All Tier C fields must carry

```text
classification=FINITE_HEURISTIC_ONLY
```

and may never be promoted to theorem flags by the num track.

## 4. Stage14-num1 — baseline correctness and profiler

Goal: establish a trustworthy numerical kernel before extending the cutoff.

Tasks:

1. identify all currently used Stage14 exact enumerators/generation routes;
2. reproduce the full frozen `B=2,000,000` exact-two object ledger and counts;
3. cross-check duplicate suppression, primitiveness, canonical ordering, direction labels, and triple handling;
4. benchmark CPU time, peak memory, candidate generation volume, and rejection stages;
5. record deterministic hashes of the frozen baseline ledger;
6. identify the actual complexity bottleneck before optimizing anything.

Required exit locks:

```text
STAGE14_NUM1=COMPLETE_BASELINE_CROSSCHECK_AND_PROFILE
B2M_MAIN_COUNTS_REPRODUCED=true
B2M_OBJECT_LEDGER_HASH_LOCKED=true
DIRECTION_LABELS_CROSSCHECKED=true
TRIPLE_HANDLING_CROSSCHECKED=true
DUPLICATE_SUPPRESSION_CROSSCHECKED=true
NEXT=Stage14-num2 enumerator acceleration and incremental architecture
```

No performance rewrite is accepted unless it reproduces the exact baseline ledger.

## 5. Stage14-num2 — enumerator acceleration and incremental architecture

Goal: make larger exact cutoffs feasible without changing the mathematical population.

Candidate engineering directions, to be benchmarked rather than assumed:

- face-first generation with indexed shared-leg matching;
- gcd/lcm indexing from the exact `(g,u,v)` inverse;
- incremental processing by new space-diagonal shell rather than full restart;
- compact integer representations and sorted hash/merge joins;
- early modular rejection where mathematically exact;
- separate generation and canonical-dedup phases for easier auditing;
- deterministic chunking suitable for parallel execution.

Every optimization must pass bit-for-bit object-ledger equality at all existing frozen cutoffs.

Required outputs:

```text
benchmark-before.json
benchmark-after.json
baseline-ledger-hash comparison
scaling model for runtime/memory (finite engineering diagnostic only)
```

Required exit locks:

```text
STAGE14_NUM2=COMPLETE_EXACT_ENUMERATOR_ACCELERATION
BASELINE_LEDGER_UNCHANGED=true
INCREMENTAL_CUTOFF_ARCHITECTURE=true
PARALLEL_CHUNK_REPRODUCIBILITY=true
NEXT=Stage14-num3 extended exact census
```

## 6. Stage14-num3 — extended exact census

Goal: extend the exact common-cutoff Stage14 census beyond `2m`.

Preferred milestone cutoffs, subject to actual resource cost:

```text
B = 5,000,000
B = 10,000,000
B = 20,000,000
B = 50,000,000
```

These are targets, not promises.  Each completed cutoff is frozen independently; failure to reach a later cutoff does not invalidate earlier exact locks.

At every completed cutoff record at minimum:

```text
N_a^(2)
N_b^(2)
N_c^(2)
N_2
T
number of active oriented first-face vertices
number of distinct physical cuboids
first-hit / repeat-hit counts
```

Also record exact common-cutoff Euler-brick counts when the ambient enumerator can supply them without materially changing the main computation.

### Perfect-cuboid emergency protocol

If any newly enumerated primitive object has all three face diagonals integral (`T>0`):

1. mark the object `UNVERIFIED_PERFECT_CUBOID_CANDIDATE`;
2. independently recompute all seven square conditions with exact integer arithmetic;
3. reproduce the object through a second generation route;
4. verify primitiveness and canonical ordering;
5. freeze the minimal reproducer and hashes;
6. do not make a public existence claim from a single program path.

The num track may report a verified computational candidate, but theorem-level interpretation remains outside this track.

## 7. Stage14-num4 — unified cross-track fingerprint ledger

Goal: give the proof tracks one canonical finite object table instead of separate incompatible samples.

For every active first-face/fiber seen by the extended census, attach whichever deterministic fields are already available from merged stages, for example:

```text
first physical hit d
number of partners <= B
face direction
(S,X,H)
(g,u,v) / gcd-lcm fingerprint
local six-state fingerprints for selected primes
elliptic specialization coefficients
certified rank interval if already computed
2-Selmer summary if already computed
canonical height of the actual first-hit point
Kummer / square-class fingerprint
known low-degree-curve or bisection class label, if available
source stage + source commit for every imported field
```

Missing fields remain null.  The num track must not silently recompute a theorem-sensitive invariant with a different normalization.

Required exit lock:

```text
STAGE14_NUM4=COMPLETE_UNIFIED_FINITE_FINGERPRINT_LEDGER
CANONICAL_OBJECT_KEYS_STABLE=true
SOURCE_PROVENANCE_RECORDED=true
CROSS_TRACK_JOIN_REPRODUCIBLE=true
NEXT=Stage14-num5 scaling and anomaly diagnostics
```

## 8. Stage14-num5 — scaling and anomaly diagnostics

Goal: monitor finite behavior without promoting it to asymptotics.

For every sufficiently dense set of exact cutoffs, compute:

### Main exact-two scale

\[
N_2(B)/\sqrt B,
\]

plus moving-window effective power exponents for

\[
N_2(B)\approx B^{\alpha_{\rm eff}}.
\]

### Direction behavior

\[
N_a/N_2,\qquad N_b/N_2,\qquad N_c/N_2,
\]

and their finite drift.

### Active-vertex behavior

Record

```text
active vertex count
new-active-vertex arrivals per shell
first-hit d distribution
partner multiplicity distribution
```

### Height / arithmetic fingerprints

Where available, compare active vs inactive controls by

```text
canonical height
Selmer/rank diagnostics
gcd/lcm strata
local-state fingerprints
Kummer/bisection labels
```

### Model discipline

At least the following fits should be compared rather than selecting one in advance:

```text
c*sqrt(B)
c*B^alpha
c*sqrt(B)*(log B)^beta
c*B^alpha*(log B)^beta
```

Use nested cutoff windows and report parameter drift.  A fit that is not stable under moving the lower cutoff must be labeled pre-asymptotic.

Permanent result flag:

```text
FINITE_SCALING_DIAGNOSTICS_ONLY=true
```

## 9. Stage14-num6+ — rolling observatory

After num5, the track becomes rolling rather than sequential.

Whenever computation permits a materially larger exact cutoff:

1. extend the census;
2. append rather than rewrite historical cutoffs;
3. recompute derived diagnostics;
4. run anomaly detectors;
5. issue a compact handoff note only when something materially changes.

Examples of material changes:

- `N_2/sqrt(B)` leaves the historical band decisively;
- direction proportions reverse or show a new sustained trend;
- a new low-height active-fiber cluster appears;
- the first-hit height distribution develops a new component;
- a new Kummer/bisection fingerprint captures a substantial fraction of new hits;
- a triple/perfect-cuboid candidate appears;
- a proof-track conjectured finite signature is contradicted by exact data.

No-news cutoff extensions need only update the ledger and machine-readable summary.

## 10. Handoff contract to proof tracks

The observatory reports facts in the following format:

```text
OBSERVATION_ID=<stable id>
CUTOFF_RANGE=<exact B range>
EXACT_OR_HEURISTIC=<EXACT | DERIVED_EXACT | FINITE_HEURISTIC_ONLY>
OBJECT_COUNT=<n>
AFFECTED_TRACKS=<14-4 | 14-s | 14-t | 14-e | Stage13 | ...>
OBSERVATION=<short statement>
REPRODUCER=<script/path + commit>
THEOREM_CLAIM=false
```

Proof tracks are free to use the finite observation as motivation, but must independently prove any theorem they promote.

## 11. Reproducibility rules

Every num stage must satisfy:

- deterministic output ordering;
- exact-integer square tests only;
- no floating-point test for integrality;
- explicit cutoff convention (`d<=B` unless a different diagnostic is clearly named);
- canonical primitive ordering;
- machine-readable JSON/CSV/Parquet or equivalent plus a compact Markdown summary;
- source commit and script hash in every frozen large census;
- historical cutoffs are append-only unless a correctness bug is documented;
- when a bug is fixed, old incorrect artifacts remain traceable and are explicitly superseded.

## 12. Resource discipline

The num track may optimize aggressively, but it must not turn the repository into a raw-data dump.

Preferred policy:

- commit compact summaries and hashes;
- commit full object ledgers only when they are reasonably sized and scientifically useful;
- for very large ledgers, commit deterministic generation instructions, chunk hashes, aggregate summaries, and a small validation sample;
- keep profiling artifacts small and machine-readable;
- do not duplicate large data already frozen by another stage.

## 13. Current roadmap lock

```text
STAGE14_NUM_ROADMAP=READY
TRACK_ROLE=INDEPENDENT_NUMERICAL_OBSERVATORY
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
PROOF_TRACK_INDEPENDENT=true
BASELINE_B=2000000
BASELINE_NA=142
BASELINE_NB=134
BASELINE_NC=80
BASELINE_N2=356
BASELINE_T=0
NEXT=Stage14-num1 baseline correctness and profiler
```
