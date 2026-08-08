# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3A=COMPLETE
FINITE_CENSUS_FROZEN=true
INDEPENDENT_GENERATION_ROUTES=2
ALL_11_ROWS_MATCH=true
MAX_VERIFIED_B=2000000
STAGE13_ANALYTIC_DEPENDENCY_USED=false
NEXT=Stage14-3b late-range finite cutoff densification
STOP_AFTER_STAGE14_3=true
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```

The canonical mathematical source is `stages/stage14/main.md`.

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

Two independent generation routes agree exactly at every audited cutoff through `B=2,000,000`:

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

No triple object was found through `B=2,000,000`; this is only a finite search statement.

Frozen census artifacts:

```text
stages/stage14/data/14-2/final_census_audit.json
stages/stage14/scripts/14-2/two_face_census.py
stages/stage14/scripts/14-2/shared_leg_crosscheck.py
stages/stage14/archive/stage14-2c-census-closure.md
```

## Stage14-3a — descriptive directional ledger

Stage14-3a derives only finite diagnostics from the frozen 11-row census. No fit, limiting vector, monotonicity claim, or Stage13 asymptotic input is used.

Late cumulative ratios are

| B | `N_a/N_c` | `N_b/N_c` | `N_a/N_b` | leader |
|---:|---:|---:|---:|---|
| 100,000 | 1.434783 | 1.434783 | 1.000000 | tie a/b |
| 200,000 | 1.750000 | 2.083333 | 0.840000 | b |
| 500,000 | 1.750000 | 1.950000 | 0.897436 | b |
| 1,000,000 | 1.750000 | 1.803571 | 0.970297 | b |
| 2,000,000 | 1.775000 | 1.675000 | 1.059701 | a |

The exact finite equality

\[
N_a/N_c=7/4
\]

occurs at the three sampled cutoffs `200k`, `500k`, and `1m`, then shifts slightly to `1.775` at `2m`. This is recorded only as a finite plateau, not as a limiting constant.

The `b -> a` cumulative leader reversal is reflected in shell composition:

```text
100k -> 200k:  delta(a,b,c)=(9,17,1)
200k -> 500k:  delta(a,b,c)=(28,28,16)
500k -> 1m:    delta(a,b,c)=(28,23,16)
1m   -> 2m:    delta(a,b,c)=(44,33,24)
```

Thus the sampled late shells change from `b`-heavy, to a/b tie, to `a`-heavy. This is why Stage14-3 does not assume a simple monotone ratio trajectory.

Artifacts:

```text
stages/stage14/scripts/14-3/directional_ledger.py
stages/stage14/data/14-3/directional_ledger.json
stages/stage14/archive/stage14-3a-directional-ledger.md
```

## Stage13 review isolation

Current Stage14 finite conclusions use neither Stage13 code nor a Stage13 asymptotic theorem. Any Stage13 analytic statement under external review remains quarantined from Stage14-2 and Stage14-3.

## Planned sequence and stop line

```text
14-1   definition / interface / counting specification   [complete]
14-2   validated finite census through B=2,000,000       [complete]
14-3a  descriptive directional ledger                    [complete]
14-3b  late-range finite cutoff densification            [next]
14-3   finite directional-ratio evolution
14-4   true total growth order                           [paused]
14-5   directionwise asymptotic structure                [paused]
```

Stage14 stops after Stage14-3 for now. Stage14-4 and Stage14-5 resume only after the one-face / Stage13 proof review clarifies what structural results are reliable enough to reuse.
