# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_2A=COMPLETE
STAGE14_2B=COMPLETE
STAGE14_2C=COMPLETE
FINITE_CENSUS_FROZEN=true
INDEPENDENT_GENERATION_ROUTES=2
ALL_11_ROWS_MATCH=true
MAX_VERIFIED_B=2000000
STAGE13_ANALYTIC_DEPENDENCY_USED=false
NEXT=Stage14-3 finite directional analysis
STOP_AFTER_STAGE14_3=true
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```

The canonical mathematical source is `stages/stage14/main.md`; detailed finite-census closure is recorded in

```text
stages/stage14/archive/stage14-2c-census-closure.md
```

## Counting convention

Use

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

The three exactly-two directions are

```text
ab+ac only  <-> shared edge a <-> smallest edge shared
ab+bc only  <-> shared edge b <-> middle edge shared
ac+bc only  <-> shared edge c <-> largest edge shared
```

Write

\[
N_a^{(2)}=N_{ab,ac}^{(2)},
\qquad
N_b^{(2)}=N_{ab,bc}^{(2)},
\qquad
N_c^{(2)}=N_{ac,bc}^{(2)}.
\]

Stage14 retains the raw pair-overlap vector

\[
\mathbf O=(O_{ab,ac},O_{ab,bc},O_{ac,bc})
\]

and triple population `T(B)`, with

\[
\mathbf N_2^{\rm dir}=\mathbf O-T(1,1,1).
\]

No perfect-cuboid nonexistence assumption is built into the counting convention.

## Stage14-2 — frozen finite census

The production enumerator is

```text
stages/stage14/scripts/14-2/two_face_census.py
```

and imports no Stage13 counting code. Stage14-2c adds a second generation route

```text
stages/stage14/scripts/14-2/shared_leg_crosscheck.py
```

which first joins two Pythagorean faces on a shared leg and only then tests the integer space diagonal. This is materially different from the production face-to-space-diagonal gluing route.

Both routes agree exactly at every audited cutoff:

| B | exactly-two vector `(a,b,c)` | N2 | T |
|---:|---:|---:|---:|
| 1,000 | `(2,0,0)` | 2 | 0 |
| 2,000 | `(2,2,1)` | 5 | 0 |
| 5,000 | `(6,6,3)` | 15 | 0 |
| 10,000 | `(9,11,5)` | 25 | 0 |
| 20,000 | `(16,16,10)` | 42 | 0 |
| 50,000 | `(24,24,14)` | 62 | 0 |
| 100,000 | `(33,33,23)` | 89 | 0 |
| 200,000 | `(42,50,24)` | 116 | 0 |
| 500,000 | `(70,78,40)` | 188 | 0 |
| 1,000,000 | `(98,101,56)` | 255 | 0 |
| 2,000,000 | `(142,134,80)` | 356 | 0 |

At `B=2,000,000`, the c-normalized ratio is

\[
1.775:1.675:1.
\]

The finite leader changes from `b` at 200k/500k/1m to `a` at 2m. Therefore no monotone directional convergence is assumed.

No triple object was found through `B=2,000,000`; this is a finite search statement only.

Machine-readable outputs:

```text
stages/stage14/data/14-2/historical_reproduction_report.json
stages/stage14/data/14-2/extended_census_report.json
stages/stage14/data/14-2/shared_leg_crosscheck_report.json
stages/stage14/data/14-2/final_census_audit.json
```

## Stage13 review isolation

Current Stage14 finite conclusions use neither Stage13 code nor a Stage13 asymptotic theorem. The first seven historical values now have independent Stage14 reproductions and the four extension rows are Stage14-owned results.

Any Stage13 analytic statement under external review is quarantined from Stage14-2 and Stage14-3.

## Planned sequence and stop line

```text
14-1   definition / interface / counting specification   [complete]
14-2   validated finite census through B=2,000,000       [complete]
14-3   finite directional-ratio evolution                [next]
14-4   true total growth order                           [paused]
14-5   directionwise asymptotic structure                [paused]
```

Stage14 stops after Stage14-3 for now. Stage14-4 and Stage14-5 resume only after the one-face / Stage13 proof review clarifies what structural results are reliable enough to reuse. Stage14-3 may diagnose finite behavior but must not promote an empirical fit to a theorem.
