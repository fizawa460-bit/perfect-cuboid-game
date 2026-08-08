# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_3A_3B_COMPLETE_14_3C_NEXT_14_4_PAUSED`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and **exactly two** integral face diagonals. The finite census is independently audited through `B=2,000,000`. Current work is restricted to finite directional diagnostics; asymptotic stages remain paused pending the one-face / Stage13 proof review.

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

## §3. Stage14-3 — finite directional diagnostics

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

This produced two finite questions:

1. is the repeated sampled equality `N_a/N_c=7/4` meaningful or only a sparse-grid artifact?;
2. where exactly does the cumulative `b -> a` leader reversal occur?

Artifacts:

```text
stages/stage14/data/14-3/directional_ledger.json
stages/stage14/archive/stage14-3a-directional-ledger.md
```

### §3.2 Stage14-3b — dense late-range finite geography

Stage14-3b enumerates the production Stage14 route once through `B=2,000,000`, retains every exactly-two object by its exact space diagonal `d`, and forms the cumulative grid

```text
100,000, 150,000, ..., 2,000,000
step = 50,000
39 rows
```

The anchor values `100k,200k,500k,1m,2m` reproduce the frozen Stage14-2 population exactly.

Artifacts:

```text
stages/stage14/scripts/14-3/late_range_densification.py
stages/stage14/data/14-3/late_range_densification.json
stages/stage14/archive/stage14-3b-late-range-densification.md
```

#### §3.2.1 The apparent `a/c=7/4` plateau is not stable

The 50k grid gives, for example,

```text
B=150k   a/c=1.625000
B=200k   a/c=1.750000
B=250k   a/c=1.920000
B=300k   a/c=1.785714
B=350k   a/c=1.866667
B=400k   a/c=1.694444
B=500k   a/c=1.750000
B=550k   a/c=1.553191
B=1m     a/c=1.750000
```

Thus the repeated coarse equality at `200k,500k,1m` is not a stable finite trajectory.

Since the cumulative counts are step functions, exact equality

\[
4N_a^{(2)}=7N_c^{(2)}
\]

holds on several disjoint integer cutoff intervals in `100k<=B<=2m`:

```text
172057..207280
364285..365548
499525..501684
984113..1006560
1123357..1127184
1212625..1218028
1384837..1421728
```

The equality is therefore intermittent. Stage14 does **not** infer `7/4` as an invariant, limit, or asymptotic constant.

#### §3.2.2 Exact localization of the finite `a/b` reversal

At `B=1m`,

```text
(N_a,N_b,N_c)=(98,101,56),
a-b=-3.
```

Following the exact event stream after `1m` gives the relevant tie/crossing events:

```text
d=1,083,121:  a-b -1 ->  0, counts=(105,105,59)
d=1,096,685:  a-b  0 -> -1, counts=(105,106,59)
d=1,127,185:  a-b -1 ->  0, counts=(106,106,60)
d=1,148,545:  a-b  0 -> +1, counts=(107,106,60)
```

After the event at

\[
\boxed{d=1,148,545}
\]

`a>b` at every subsequent exactly-two event state through the verified ceiling `B=2,000,000`.

This is only a finite-range statement. It does not prove eventual or asymptotic dominance of the `a` direction.

#### §3.2.3 Selected dense trajectory

```text
100k   (33,33,23)    a-b=  0
150k   (39,37,24)    a-b= +2
200k   (42,50,24)    a-b= -8
500k   (70,78,40)    a-b= -8
900k   (95,99,54)    a-b= -4
1m     (98,101,56)   a-b= -3
1.10m  (105,106,59)  a-b= -1
1.15m  (107,106,60)  a-b= +1
1.50m  (123,120,70)  a-b= +3
2m     (142,134,80)  a-b= +8
```

The finite leader itself changes more than once over the wider range, so neither cumulative leader nor ratio motion should be treated as monotone evidence.

#### §3.2.4 Stage14-3b decision

```text
STAGE14_3A=COMPLETE
STAGE14_3B=COMPLETE
DENSE_FINITE_GRID_STEP=50000
A_OVER_C_7_4_LIMIT_SUPPORTED=false
A_B_CROSSING_LOCALIZED=true
FINAL_A_OVER_B_CROSSING_D_WITHIN_VERIFIED_RANGE=1148545
FINITE_RATIO_LIMIT_IDENTIFIED=false
ASYMPTOTIC_FIT_PERFORMED=false
MONOTONE_CONVERGENCE_SUPPORTED=false
STAGE13_ANALYTIC_DEPENDENCY_USED=false
```

### §3.3 Next — Stage14-3c finite diagnostic synthesis

Stage14-3c should not search for an asymptotic law. Its purpose is to close the finite reconnaissance cleanly:

```text
separate robust finite observations from sparse-grid artifacts
summarize the shell/event geography any later proof must explain
record all currently open directional questions
close Stage14-3
activate the agreed stop line before Stage14-4
```

## §4. Stop line

Current policy:

```text
Stage14-3c  finite diagnostic synthesis / closure     NEXT / ALLOWED
Stage14-4   true total growth order                   PAUSED
Stage14-5   directionwise asymptotic structure        PAUSED
```

Stage14 stops after Stage14-3. Stage14-4 and Stage14-5 resume only after the one-face / Stage13 proof review clarifies what structural machinery is reliable enough to serve as a proof-level map.

```text
NEXT=Stage14-3c finite diagnostic synthesis / stop-line preparation
STOP_AFTER_STAGE14_3=true
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```
