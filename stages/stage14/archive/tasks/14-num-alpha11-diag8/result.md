# Stage14-numα11-diag8 — extended raw-face denominator census

## Result

Diag8 extends the Stage13-style complete primitive canonical raw-face census from `B=100000` to `B=1000000` and recomputes the conditional second-face survival profile at

```text
100k, 200k, 300k, 400k, 500k, 750k, 1m.
```

The enumeration is performed from the same Pythagorean-gluing construction used by Stage13, with direct recomputation of all three face-square masks. At every checkpoint, the exactly-two pair counts are independently cross-checked against the frozen Stage14 B500m object source.

## Exact locks

At `B=100000`, the Stage13 census is reproduced exactly:

```text
raw (ab,ac,bc) = (84212,43236,40760)
N1  (ab,ac,bc) = (84146,43180,40704)
pair (a,b,c)   = (33,33,23)
```

At every extended checkpoint,

```text
raw_q - exactly_one_q = exactly_two endpoint load E_q
```

and the frozen Stage14 pair counts agree exactly. No exactly-three object appears through `B=1000000`.

## Extended survival profile

Define

```text
S_ab=(a+b)/A_ab,
S_ac=(a+c)/A_ac,
S_bc=(b+c)/A_bc.
```

Relative to `S_bc=1`, the cumulative profiles are

```text
B=100k : 0.570448 : 0.942733 : 1
B=200k : 0.597980 : 0.833559 : 1
B=300k : 0.599843 : 0.827653 : 1
B=400k : 0.594434 : 0.853837 : 1
B=500k : 0.601907 : 0.869959 : 1
B=750k : 0.597434 : 0.871081 : 1
B=1m   : 0.604399 : 0.908758 : 1
```

Thus the main diag7 mechanism persists throughout the extended window:

```text
S_ab < S_ac < S_bc
```

at every checkpoint. The large `ab` raw-face population is systematically less likely to acquire a second integral face than `ac` or `bc`.

## Comparison with the Stage13 -> hypothetical 2:2:1 bridge

If the proved Stage13 limiting face vector

```text
(0.5347369332,0.2453591778,0.2199038889)
```

were combined with a hypothetical Stage14 exactly-two pair limit `2:2:1`, the required relative survival profile would be

```text
0.548317 : 0.896253 : 1.
```

The empirical profile does not move monotonically toward this target. Its normalized-shape L1 distances are

```text
100k  0.02234
200k  0.04764
300k  0.05136
400k  0.03700
500k  0.03841
750k  0.03544
1m    0.03239
```

So the structural shape remains close, but diag8 does **not** support a claim of monotone convergence to that bridge profile.

## B=1m snapshot

```text
raw                 = (1237105,636722,589898)
exactly-two pair    = (98,101,56)
endpoint load       = (199,154,157)
N2                  = 255
survival rel bc=1   = (0.604399,0.908758,1)
```

The complete B=1m enumeration audited

```text
1,980,642 integer Pythagorean triples
12,419,089 glued records before filters
2,463,470 distinct primitive canonical objects with >=1 integral face
```

## Boundary

This is a finite exact census only. The exactly-two population is still only `255` objects at B=1m, so neither an asymptotic survival profile nor an asymptotic `2:2:1` law is claimed.

```text
STAGE14_NUM_ALPHA11_DIAG8=EXTENDED_RAW_FACE_DENOMINATOR_CENSUS_COMPLETE
MATCHED_MAX_B=1000000
STAGE13_B100K_LOCK_REPRODUCED=true
FROZEN_STAGE14_PAIR_COUNTS_MATCH_ALL_CHECKPOINTS=true
RAW_MINUS_EXACT_ONE_ENDPOINT_IDENTITY_ALL_CHECKPOINTS=true
TRIPLE_COUNT_ZERO_THROUGH_B1M=true
AB_SECOND_FACE_SURVIVAL_LOWER_THAN_AC_BC_ALL_CHECKPOINTS=true
SURVIVAL_PROFILE_MONOTONE_TO_HYPOTHETICAL_BRIDGE=false
B1M_SURVIVAL_REL_BC=0.6043990674035388,0.9087577682163763,1
B1M_N2=255
ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM=false
ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM=false
NEXT=Stage14-num-alpha11-diag9 shell-wise second-face survival drift and bridge-residual decomposition
```
