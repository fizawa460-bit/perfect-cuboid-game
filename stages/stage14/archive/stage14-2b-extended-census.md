# Stage14-2b — independent census extension above B=100000

## Scope

Stage14-2b extends the Stage14-owned finite census beyond the inherited Stage13 range. No Stage13 counting code is imported, and no Stage13 asymptotic theorem is used in producing or interpreting these rows.

The ambient population remains

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The exactly-two directions are

```text
a = ab+ac only
b = ab+bc only
c = ac+bc only
```

with the triple population `T` retained explicitly.

## Extended census

| B | N_a^(2) | N_b^(2) | N_c^(2) | N_2 | T | c-normalized ratio |
|---:|---:|---:|---:|---:|---:|---|
| 200,000 | 42 | 50 | 24 | 116 | 0 | 1.7500 : 2.0833 : 1 |
| 500,000 | 70 | 78 | 40 | 188 | 0 | 1.7500 : 1.9500 : 1 |
| 1,000,000 | 98 | 101 | 56 | 255 | 0 | 1.7500 : 1.803571 : 1 |
| 2,000,000 | 142 | 134 | 80 | 356 | 0 | 1.7750 : 1.6750 : 1 |

Every row satisfies exactly

\[
N_a^{(2)}=O_{ab,ac}-T,
\qquad
N_b^{(2)}=O_{ab,bc}-T,
\qquad
N_c^{(2)}=O_{ac,bc}-T,
\]

and

\[
N_2=O_{ab,ac}+O_{ab,bc}+O_{ac,bc}-3T.
\]

All square tests are exact integer tests. Canonical tuples are deduplicated by `(a,b,c,d)` and all three face flags are recomputed after deduplication.

## Finite observations only

The finite directional leader is not stable over the extended range:

```text
B=200k   b-direction largest
B=500k   b-direction largest
B=1m     b-direction largest
B=2m     a-direction largest
```

Thus Stage14-2b records a finite leader reversal. It does not infer monotone convergence, a limiting ratio, an exponent, or a logarithmic power.

The a/c ratio is numerically `1.75` at 200k, 500k and 1m, then `1.775` at 2m. This is recorded only as a finite diagnostic; no exact or asymptotic identity is claimed.

No triple object was found through `B=2,000,000`. This is only a finite search statement and is not evidence of perfect-cuboid nonexistence in the theorem sense.

## Stage13 independence

This extension is intentionally usable while Stage13 analytic review is unresolved.

```text
STAGE13_CODE_IMPORTED=false
STAGE13_ASYMPTOTIC_RESULT_USED=false
```

The only historical role of Stage13 in Stage14-2 was the checksum gate already closed independently in 14-2a. The new `B>100000` rows are produced directly by the Stage14 enumerator.

## Decision

```text
STAGE14_2B=COMPLETE
EXTENSION_ABOVE_B100000_COMPLETED=true
MAX_VERIFIED_B=2000000
PERFECT_CUBOID_WITNESS_FOUND=false
FINITE_LEADER_REVERSAL_OBSERVED=true
MONOTONE_CONVERGENCE_CLAIMED=false
LIMITING_RATIO_CLAIMED=false
GROWTH_LAW_CLAIMED=false
STAGE13_ANALYTIC_DEPENDENCY_USED=false
NEXT=Stage14-2c finite-census closure / audit before Stage14-3
```
