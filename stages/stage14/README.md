# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3A=COMPLETE
STAGE14_3B=COMPLETE
FINITE_CENSUS_FROZEN=true
MAX_VERIFIED_B=2000000
DENSE_FINITE_GRID_STEP=50000
STAGE13_ANALYTIC_DEPENDENCY_USED=false
NEXT=Stage14-3c finite diagnostic synthesis / stop-line preparation
STOP_AFTER_STAGE14_3=true
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```

Canonical source: `stages/stage14/main.md`.

## Counting convention

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The three exactly-two directions are

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

Write

\[
N_a^{(2)}=O_{ab,ac}-T,\qquad
N_b^{(2)}=O_{ab,bc}-T,\qquad
N_c^{(2)}=O_{ac,bc}-T.
\]

No perfect-cuboid nonexistence assumption is made.

## Stage14-2 — frozen finite census

Two materially different exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`.

```text
100k   (33,33,23)
200k   (42,50,24)
500k   (70,78,40)
1m     (98,101,56)
2m     (142,134,80)
```

No triple object was found through `B=2,000,000`; this is a finite search statement only.

## Stage14-3a — coarse finite directional ledger

The coarse late samples were

```text
B=200k:  a/c=1.75   b/c=2.083333   a/b=0.84
B=500k:  a/c=1.75   b/c=1.95       a/b=0.897436
B=1m:    a/c=1.75   b/c=1.803571   a/b=0.970297
B=2m:    a/c=1.775  b/c=1.675      a/b=1.059701
```

This suggested an apparent finite `a/c=7/4` plateau and a `b -> a` leader reversal.

## Stage14-3b — dense late-range geography

Stage14-3b recomputes the same finite population on a 50k grid from `B=100k` through `B=2m` and also follows every exactly-two event by its exact integer space diagonal `d`.

Artifacts:

```text
stages/stage14/scripts/14-3/late_range_densification.py
stages/stage14/data/14-3/late_range_densification.json
stages/stage14/archive/stage14-3b-late-range-densification.md
```

The denser grid shows that the apparent `a/c=7/4` plateau is not a stable finite law. Between the coarse sample points the ratio moves substantially; e.g.

```text
150k  1.625000
200k  1.750000
250k  1.920000
300k  1.785714
400k  1.694444
500k  1.750000
550k  1.553191
1m    1.750000
```

Thus `7/4` is not promoted to an invariant or limiting value.

The `a/b` reversal can be localized exactly in the finite event stream after `1m`:

```text
d=1,083,121   a-b: -1 ->  0
 d=1,096,685  a-b:  0 -> -1
 d=1,127,185  a-b: -1 ->  0
 d=1,148,545  a-b:  0 -> +1
```

From `d=1,148,545` through the verified ceiling `B=2,000,000`, every subsequent exactly-two event state has `a>b`. This is finite only; eventual asymptotic dominance is not inferred.

## Stage13 isolation and stop line

Current Stage14 finite conclusions use neither Stage13 code nor a Stage13 asymptotic theorem.

```text
14-3c  finite diagnostic synthesis / stop-line preparation   [next]
14-4   true total growth order                               [paused]
14-5   directionwise asymptotic structure                    [paused]
```

Stage14 stops after Stage14-3 until the one-face / Stage13 proof review clarifies what proof machinery is reliable enough to reuse.
