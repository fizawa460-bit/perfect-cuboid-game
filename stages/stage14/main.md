# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_3_COMPLETE_STOP_LINE_ACTIVE_14_4_PAUSED`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and **exactly two** integral face diagonals. The finite census and finite directional reconnaissance are complete through `B=2,000,000`. Stage14 now stops before asymptotic work until the one-face / Stage13 proof review identifies reliable proof-level machinery.

## §1. Locked counting convention

For `B>=1`, count positive integers satisfying

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Let

\[
I_{ab}=\mathbf1_{a^2+b^2=\square},\quad
I_{ac}=\mathbf1_{a^2+c^2=\square},\quad
I_{bc}=\mathbf1_{b^2+c^2=\square}.
\]

The raw pair populations are

\[
O_{ab,ac}=\sum I_{ab}I_{ac},\quad
O_{ab,bc}=\sum I_{ab}I_{bc},\quad
O_{ac,bc}=\sum I_{ac}I_{bc},
\]

and the triple population is

\[
T=\sum I_{ab}I_{ac}I_{bc}.
\]

The exactly-two directional populations are

\[
N_a^{(2)}=O_{ab,ac}-T,
\qquad
N_b^{(2)}=O_{ab,bc}-T,
\qquad
N_c^{(2)}=O_{ac,bc}-T,
\]

where

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

and

\[
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}.
\]

No perfect-cuboid nonexistence assumption is made. Any `T>0` object must be preserved as an exact witness.

### §1.1 Stage13 analytic quarantine

Current Stage14 finite conclusions use no Stage13 code and no Stage13 asymptotic theorem.

```text
STAGE13_CODE_IMPORTED=false
STAGE13_ASYMPTOTIC_RESULT_USED=false
```

A previously recorded Stage13-derived analytic bound is not an input to the current Stage14 conclusions while Stage13 is under external review.

## §2. Stage14-2 — frozen finite census

Two materially different exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`.

| B | N_a^(2) | N_b^(2) | N_c^(2) | N_2 | T |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 2 | 0 | 0 | 2 | 0 |
| 2,000 | 2 | 2 | 1 | 5 | 0 |
| 5,000 | 6 | 6 | 3 | 15 | 0 |
| 10,000 | 9 | 11 | 5 | 25 | 0 |
| 20,000 | 16 | 16 | 10 | 42 | 0 |
| 50,000 | 24 | 24 | 14 | 62 | 0 |
| 100,000 | 33 | 33 | 23 | 89 | 0 |
| 200,000 | 42 | 50 | 24 | 116 | 0 |
| 500,000 | 70 | 78 | 40 | 188 | 0 |
| 1,000,000 | 98 | 101 | 56 | 255 | 0 |
| 2,000,000 | 142 | 134 | 80 | 356 | 0 |

Canonical audit:

```text
stages/stage14/data/14-2/final_census_audit.json
```

No triple object was found through `B=2,000,000`; this is a finite search statement only.

## §3. Stage14-3 — finite directional reconnaissance

Stage14-3 studies only finite behavior of

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}.
\]

No finite fit is promoted to a theorem.

### §3.1 Stage14-3a — coarse descriptive ledger

The coarse late sample was

| B | N_a/N_c | N_b/N_c | N_a/N_b | leader |
|---:|---:|---:|---:|---|
| 200,000 | 1.750000 | 2.083333 | 0.840000 | b |
| 500,000 | 1.750000 | 1.950000 | 0.897436 | b |
| 1,000,000 | 1.750000 | 1.803571 | 0.970297 | b |
| 2,000,000 | 1.775000 | 1.675000 | 1.059701 | a |

This raised two finite questions: whether the repeated sampled equality `N_a/N_c=7/4` was meaningful, and where the cumulative `b -> a` leader reversal occurred.

Artifacts:

```text
stages/stage14/data/14-3/directional_ledger.json
stages/stage14/archive/stage14-3a-directional-ledger.md
```

### §3.2 Stage14-3b — dense late-range geography

Stage14-3b forms the cumulative grid

```text
100,000, 150,000, ..., 2,000,000
step = 50,000
39 rows
```

and follows the exact exactly-two event stream near the `a/b` crossing.

Artifacts:

```text
stages/stage14/scripts/14-3/late_range_densification.py
stages/stage14/data/14-3/late_range_densification.json
stages/stage14/archive/stage14-3b-late-range-densification.md
```

#### §3.2.1 The coarse `a/c=7/4` pattern is not stable

The 50k grid gives, for example,

```text
150k   a/c=1.625000
200k   a/c=1.750000
250k   a/c=1.920000
300k   a/c=1.785714
400k   a/c=1.694444
500k   a/c=1.750000
550k   a/c=1.553191
1m     a/c=1.750000
```

Thus the repeated equality at `200k,500k,1m` is a sparse-grid finite artifact, not a stable finite law. Stage14 does not infer `7/4` as an invariant, limit, or asymptotic constant.

#### §3.2.2 Exact localization of the finite `a/b` reversal

After `B=1m`, the relevant exact event sequence is

```text
d=1,083,121   a-b: -1 ->  0
d=1,096,685   a-b:  0 -> -1
d=1,127,185   a-b: -1 ->  0
d=1,148,545   a-b:  0 -> +1
```

Immediately after the final crossing,

```text
(N_a,N_b,N_c)=(107,106,60).
```

From

\[
\boxed{d=1,148,545}
\]

through the verified ceiling `B=2,000,000`, every subsequent exactly-two event state has `a>b`. This is only a finite-range persistence statement; eventual or asymptotic `a` dominance is not inferred.

### §3.3 Stage14-3c — final finite synthesis

Stage14-3c adds no new asymptotic model. It closes the finite reconnaissance by separating robust finite facts, discarded sparse-grid interpretations, and open analytic questions.

Canonical synthesis:

```text
stages/stage14/data/14-3/final_finite_reconnaissance.json
stages/stage14/archive/stage14-3c-final-finite-reconnaissance.md
```

#### §3.3.1 Robust finite facts

The retained finite conclusions are:

1. Two independent exact generation routes agree at all 11 locked audit cutoffs through `B=2,000,000`.
2. At the verified ceiling,
   \[
   (N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),\quad N_2=356,\quad T=0.
   \]
3. The dense `100k..2m` directional trajectory is not monotone in any simple sense.
4. The apparent coarse `a/c=7/4` plateau is not stable under densification and is rejected as a finite invariant candidate.
5. The last `a/b` crossing in the verified event stream occurs at `d=1,148,545`; finite `a>b` persistence is verified from there through `2m`.
6. No triple object is found through the verified ceiling, but no perfect-cuboid nonexistence claim follows.
7. None of these finite conclusions uses Stage13 analytic machinery.

#### §3.3.2 What remains unknown

Stage14-3 does **not** identify

```text
the true growth order of N_2(B)
a limiting directional vector or limiting proportions
a monotonicity theorem
an eventual directional leader
an asymptotic meaning for 7/4
an Euler-side two-face equality or inequality
whether T(B) ever becomes positive
```

These are precisely the phenomena a later proof must explain.

#### §3.3.3 Restart gate

Stage14 now stops deliberately. Stage14-4 is not allowed to begin merely by importing the old Stage13 proof chain.

When the one-face / Stage13 review settles which tools are reliable, the recommended restart is

```text
14-4aa  independent two-face parametrization and proof-input audit
```

Every reused Stage13 dependency must be explicitly re-audited before it becomes a Stage14 proof input.

### §3.4 Locked Stage14-3 decision

```text
STAGE14_3A=COMPLETE
STAGE14_3B=COMPLETE
STAGE14_3C=COMPLETE
STAGE14_3=COMPLETE
FINITE_RECONNAISSANCE_COMPLETE=true
DENSE_FINITE_GRID_STEP=50000
MAX_VERIFIED_B=2000000
A_OVER_C_7_4_LIMIT_SUPPORTED=false
FINAL_A_OVER_B_CROSSING_D_WITHIN_VERIFIED_RANGE=1148545
ASYMPTOTIC_FIT_PERFORMED=false
FINITE_RATIO_LIMIT_IDENTIFIED=false
MONOTONE_CONVERGENCE_SUPPORTED=false
STAGE13_ANALYTIC_DEPENDENCY_USED=false
```

## §4. Stop line — ACTIVE

Current policy is

```text
Stage14-1   COMPLETE
Stage14-2   COMPLETE
Stage14-3   COMPLETE
Stage14-4   PAUSED_PENDING_ONE_FACE_REVIEW
Stage14-5   PAUSED_PENDING_ONE_FACE_REVIEW
```

There is no `14-3d` planned. Stage14 resumes only after the one-face / Stage13 proof review provides a trustworthy proof-level starting point.

```text
STOP_LINE_ACTIVE=true
NEXT=WAIT_FOR_ONE_FACE_REVIEW_BEFORE_STAGE14_4
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```
