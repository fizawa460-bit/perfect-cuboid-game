# Stage14-2a — standalone historical reproduction

## Purpose

Establish a Stage14-owned finite census implementation before extending the two-face population beyond the Stage13 historical range.

The implementation is standalone:

```text
stages/stage14/scripts/14-2/two_face_census.py
```

It imports no Stage13 counting code. The inherited Stage13 rows are used only as checksum targets.

## Method

Enumerate all positive integer Pythagorean triples up to the space-diagonal cutoff and glue

\[
x^2+y^2=p^2,
\qquad
p^2+z^2=d^2.
\]

For each generated candidate:

1. sort `(x,y,z)` to canonical `(a,b,c)`;
2. require `0<a<b<c`;
3. require `gcd(a,b,c)=1`;
4. deduplicate by `(a,b,c,d)`;
5. recheck `a^2+b^2+c^2=d^2` exactly;
6. recompute all three face-square flags using `isqrt` only;
7. count raw pairs, exactly-two classes and triples from the recomputed mask.

Any triple mask preserves the full witness

```text
a,b,c,d,d_ab,d_ac,d_bc
```

rather than being discarded.

## Historical reproduction

The Stage14 implementation reproduces all inherited rows exactly:

| B | N_a^(2) | N_b^(2) | N_c^(2) | N_2 | T |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 2 | 0 | 0 | 2 | 0 |
| 2,000 | 2 | 2 | 1 | 5 | 0 |
| 5,000 | 6 | 6 | 3 | 15 | 0 |
| 10,000 | 9 | 11 | 5 | 25 | 0 |
| 20,000 | 16 | 16 | 10 | 42 | 0 |
| 50,000 | 24 | 24 | 14 | 62 | 0 |
| 100,000 | 33 | 33 | 23 | 89 | 0 |

At `B=100000`,

\[
\mathbf N_2^{\rm dir}=(33,33,23),
\qquad
N_2=89,
\qquad
T=0,
\]

and the c-normalized finite ratio is

\[
1.4347826087:1.4347826087:1.
\]

The directional ratio is visibly unstable over the short historical range; no asymptotic model is inferred here.

## Validation

For every row,

\[
N_a^{(2)}=O_{ab,ac}-T,
\quad
N_b^{(2)}=O_{ab,bc}-T,
\quad
N_c^{(2)}=O_{ac,bc}-T,
\]

and

\[
N_2=O_{ab,ac}+O_{ab,bc}+O_{ac,bc}-3T
\]

are checked exactly.

The `B=100000` enumeration diagnostics reproduce the earlier whole-population counts as a secondary checksum:

```text
integer Pythagorean triples                   161436
glued records before filters                 721980
primitive glued records before dedup         168208
distinct primitive canonical >=1-face objs   168119
face histogram: exactly-one/exactly-two/three
                168030 / 89 / 0
```

## Boundary

Stage14-2a closes only the historical reproduction gate. It does not yet satisfy the Stage14-2 requirement to extend above `B=100000`, and it does not prove any growth law or limiting directional ratio.

```text
STAGE14_2A=COMPLETE
HISTORICAL_REPRODUCTION_PASS=true
MAX_VERIFIED_B=100000
EXTENSION_ABOVE_B100000_COMPLETED=false
PERFECT_CUBOID_WITNESS_FOUND=false
NEXT=Stage14-2b verified extension above B=100000
```
