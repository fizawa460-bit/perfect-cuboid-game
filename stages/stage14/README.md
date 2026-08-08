# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2A=COMPLETE
STAGE14_2B=COMPLETE
HISTORICAL_REPRODUCTION_PASS=true
EXTENSION_ABOVE_B100000_COMPLETED=true
MAX_VERIFIED_B=2000000
STAGE13_ANALYTIC_DEPENDENCY_USED=false
NEXT=Stage14-2c
```

The canonical mathematical source is

```text
stages/stage14/main.md
```

The active roadmap is

```text
stages/stage14/roadmap.md
```

Stage14-2 finite outputs are stored under

```text
stages/stage14/data/14-2/
```

and the standalone census code is

```text
stages/stage14/scripts/14-2/two_face_census.py
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

and the triple population `T(B)`, with

\[
\mathbf N_2^{\rm dir}=\mathbf O-T(1,1,1).
\]

No perfect-cuboid nonexistence assumption is built into the counting convention.

## Stage14-1 interface and contract

Stage14-1 locks the finite enumeration contract. Required rules include:

```text
exact integer square tests only
canonical sort and dedup by (a,b,c,d)
recompute all three face flags after dedup
retain raw pair, triple and exactly-two ledgers
reproduce all seven historical rows exactly
produce verified cutoffs above B=100000
never assume or silently discard T=0
```

If `T(B)>0`, the enumerator preserves

```text
a,b,c,d,d_ab,d_ac,d_bc
```

for independent exact verification.

Machine-readable Stage14-1 specifications:

```text
stages/stage14/data/14-1/stage13_pair_interface.json
stages/stage14/data/14-1/enumeration_output_spec.json
```

## Stage14-2a — historical reproduction

Stage14-2a added a standalone Stage14 census implementation. It imports no Stage13 counting code. It independently generates the primitive canonical population by Pythagorean-triple gluing, deduplicates canonical tuples and recomputes all face-square flags exactly.

The seven historical cutoff rows were reproduced exactly:

| B | exactly-two vector `(a,b,c)` | N2 | T |
|---:|---:|---:|---:|
| 1,000 | `(2,0,0)` | 2 | 0 |
| 2,000 | `(2,2,1)` | 5 | 0 |
| 5,000 | `(6,6,3)` | 15 | 0 |
| 10,000 | `(9,11,5)` | 25 | 0 |
| 20,000 | `(16,16,10)` | 42 | 0 |
| 50,000 | `(24,24,14)` | 62 | 0 |
| 100,000 | `(33,33,23)` | 89 | 0 |

Machine-readable result:

```text
stages/stage14/data/14-2/historical_reproduction_report.json
```

## Stage14-2b — independent extension

Using the same Stage14-owned enumerator, with no Stage13 analytic result used, the census was extended to `B=2,000,000`:

| B | exactly-two vector `(a,b,c)` | N2 | T | c-normalized ratio |
|---:|---:|---:|---:|---|
| 200,000 | `(42,50,24)` | 116 | 0 | `1.7500 : 2.0833 : 1` |
| 500,000 | `(70,78,40)` | 188 | 0 | `1.7500 : 1.9500 : 1` |
| 1,000,000 | `(98,101,56)` | 255 | 0 | `1.7500 : 1.803571 : 1` |
| 2,000,000 | `(142,134,80)` | 356 | 0 | `1.7750 : 1.6750 : 1` |

The finite leader changes from `b` at 200k/500k/1m to `a` at 2m. Therefore no monotone directional convergence is assumed.

No triple object was found through `B=2,000,000`; this is only a finite search statement.

Machine-readable result:

```text
stages/stage14/data/14-2/extended_census_report.json
```

Detailed record:

```text
stages/stage14/archive/stage14-2b-extended-census.md
```

## Stage13 review isolation

Stage14-2b deliberately uses no Stage13 asymptotic theorem. The finite rows above depend only on the Stage14 counting definition and standalone exact enumerator.

If Stage13 proof review changes an asymptotic claim, these Stage14-2 rows remain unchanged. Stage13 can be compared again only after its review state stabilizes.

## Planned sequence

```text
14-1   definition / interface / counting specification   [complete]
14-2a  standalone historical reproduction                [complete]
14-2b  verified extension through B=2,000,000            [complete]
14-2c  finite-census closure / audit                      [next]
14-3   finite directional-ratio evolution
14-4   true total growth order
14-5   directionwise asymptotic structure
```

The difficult analytic tasks `14-4` and `14-5` may use two-letter substages beginning at `aa`.
