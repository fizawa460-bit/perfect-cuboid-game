# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2A=COMPLETE
HISTORICAL_REPRODUCTION_PASS=true
MAX_VERIFIED_B=100000
NEXT=Stage14-2b
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

Stage14-1 identifies the raw pair/triple objects with the earlier Stage13 overlap ledger and locks the finite enumeration contract.

Required rules include:

```text
exact integer square tests only
canonical sort and dedup by (a,b,c,d)
recompute all three face flags after dedup
retain raw pair, triple and exactly-two ledgers
reproduce all seven inherited rows exactly
produce at least one verified cutoff above B=100000
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

Stage14-2a adds a standalone Stage14 census implementation. It imports no Stage13 counting code. It independently generates the primitive canonical population by Pythagorean-triple gluing, deduplicates canonical tuples and recomputes all face-square flags exactly.

The inherited seven cutoff rows were reproduced exactly:

| B | exactly-two vector `(a,b,c)` | N2 | T |
|---:|---:|---:|---:|
| 1,000 | `(2,0,0)` | 2 | 0 |
| 2,000 | `(2,2,1)` | 5 | 0 |
| 5,000 | `(6,6,3)` | 15 | 0 |
| 10,000 | `(9,11,5)` | 25 | 0 |
| 20,000 | `(16,16,10)` | 42 | 0 |
| 50,000 | `(24,24,14)` | 62 | 0 |
| 100,000 | `(33,33,23)` | 89 | 0 |

At `B=100000`, the c-normalized exactly-two ratio is

\[
1.4347826087:1.4347826087:1.
\]

This is a finite observation only. No limiting ratio or growth law is inferred at 14-2a.

Machine-readable result:

```text
stages/stage14/data/14-2/historical_reproduction_report.json
```

Stage14-2a satisfies the historical reproduction gate but intentionally does not satisfy the Stage14-2 extension requirement above `B=100000`; that is the next task.

## Planned sequence

```text
14-1   definition / interface / counting specification   [complete]
14-2a  standalone historical reproduction                [complete]
14-2b  verified extension above B=100000                 [next]
14-2   complete finite enumeration
14-3   finite directional-ratio evolution
14-4   true total growth order
14-5   directionwise asymptotic structure
```

The difficult analytic tasks `14-4` and `14-5` may use two-letter substages beginning at `aa`.
