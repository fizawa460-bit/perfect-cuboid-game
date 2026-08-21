# Stage29-num3 — exact aggregated M2 production census

```text
TRACK=Stage29-num3
POPULATION=M2
STATUS=PRODUCTION_COMPLETE_AUDITED_METHOD
ROLE=EXACT_FINITE_NUMERICAL_EVIDENCE
ALGORITHM=stage29-num3-shared-edge-mobius-v1
CUTOFF=R^2=a^2+b^2+c^2<=B^2
CANONICAL=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
EXACT_FACE_MULTIPLICITY=2
SPACE_DIAGONAL_REQUIRED=false
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact production panel

The audited aggregate counter has now been run through the common Stage29 physical cutoff `B=1,000,000,000`.

| B | M2(B) | canonical shared-edge directions `(a,b,c)` |
|---:|---:|---:|
| 1,000,000 | 13,817,725 | (4,592,536, 5,816,786, 3,408,403) |
| 5,000,000 | 97,499,562 | (33,135,250, 40,788,738, 23,575,574) |
| 10,000,000 | 224,273,087 | (76,864,512, 93,602,678, 53,805,897) |
| 50,000,000 | 1,525,891,974 | (532,039,538, 633,780,237, 360,072,199) |
| 100,000,000 | 3,462,162,225 | (1,215,113,122, 1,435,434,486, 811,614,617) |
| 200,000,000 | 7,827,445,549 | (2,764,094,851, 3,239,873,832, 1,823,476,866) |
| 500,000,000 | 22,894,939,276 | (8,145,730,486, 9,457,081,553, 5,292,127,237) |
| 1,000,000,000 | **51,379,127,865** | **(18,376,842,946, 21,192,298,114, 11,809,986,805)** |

The direction entries sum exactly to `M2(B)` at every checkpoint.

## Counting identity and exactness

For a fixed shared edge `e`, let its positive Pythagorean partners inside the physical cutoff be paired unorderedly. Counting primitive shared-edge incidences gives `G(B)`. Then

```text
G(B) = M2(B) + 3*M3(B)
M2(B) = G(B) - 3*M3(B)
```

because an exactly-two-face cuboid has one unique common edge of its two successful faces, while an Euler cuboid has three successful face pairs and contributes once at each of its three edges.

Primitivity is imposed by the exact Möbius identity

```text
1_{gcd(e,x,y)=1} = sum_{d|e,d|x,d|y} mu(d).
```

The physical cutoff is tested with integer arithmetic in `__uint128_t`. Partner ordering is removed, and strict physical canonical ordering is recovered without equality cases because equal positive edges cannot form an integral Pythagorean face.

## Independent direct regression

The aggregate method is not accepted only by internal self-consistency. A materially different direct implementation enumerates Euclid primitive triples, their scales, explicit partner pairs and explicit gcd tests. It agrees exactly with the Möbius aggregate method in total and in all three directional counts at both independent checkpoints:

```text
B=1,000,000
M2=13,817,725
M2_direction=(4,592,536,5,816,786,3,408,403)

B=10,000,000
M2=224,273,087
M2_direction=(76,864,512,93,602,678,53,805,897)
```

The one-pass lightweight audit is recorded in `stages/stage29/num3/audit.md` and is PASS.

## Production provenance

```text
DIRECT_B1M_RUN=32447838198
DIRECT_B1M_ARTIFACT=9434675731
DIRECT_B1M_ARTIFACT_SHA256=6da61a04b73e8823d81d57ce0e10e633a9f3093308323fb4e9ff3c9e303e61b4

DIRECT_B10M_RUN=32447945537
DIRECT_B10M_ARTIFACT=9434716391
DIRECT_B10M_ARTIFACT_SHA256=efdef04459d559ca010f15f0f86f340400c76567ca547895a2ca606d2de648d3

MOBIUS_CROSSCHECK_RUN=32448163579
MOBIUS_CROSSCHECK_ARTIFACT=9434775818
MOBIUS_CROSSCHECK_ARTIFACT_SHA256=c216df7ab4e07027a9b6c6eacc755ed5825e91956dac24fff969cf0909d84c8a

B100M_RUN=32448268597
B100M_ARTIFACT=9434805744
B100M_ARTIFACT_SHA256=23ca9e24f465c417c8ec3334cb8183954ffe8632e67daf1f403d1ecdeee4fd00

SCALEOUT_RUN=32448381018
B200M_ARTIFACT=9434885777
B200M_ARTIFACT_SHA256=1619b2bbc0e50eab0ca8036ebcdab752f048e8165b03548174eeeea6f98b535e
B500M_ARTIFACT=9434938636
B500M_ARTIFACT_SHA256=f058510162a3366bb2da23ff500bc714bfb6210f60087d51e93bb949e07cf58b
B1B_ARTIFACT=9435024844
B1B_ARTIFACT_SHA256=cde592d9514154add331a31fcf0cf260141b32eb5f627be75c5c8fb878185d35

MATCHED_FILL_RUN=32449142616
B5M_ARTIFACT=9435051527
B5M_ARTIFACT_SHA256=cee035b03880c12c1ef1282bbb6aee7dde5809123f78f3bb72bb0cb3102d451c
B50M_ARTIFACT=9435058936
B50M_ARTIFACT_SHA256=02107f651b5a6e2c415cb827aeeec9d72b4ff29ab2741dd5b127f10b63d57d7e
```

At `B=1e9`, the aggregate production run took about 611.9 seconds wall time on four threads with peak resident memory about 982 MB. Runtime and memory are operational facts only and are not part of the mathematical count.

## Interpretation boundary

This census supplies finite exact values for the Stage18 denominator population. In particular, `N2(B)/M2(B)` at a matched cutoff is a legal finite survival fraction for imposing the integral-space condition on exactly-two-face cuboids. By contrast, `M3(B)/M2(B)` compares adjacent but different strata and is not an objectwise survival probability.

The finite values do not prove the Stage18 asymptotic, identify a new exponent, or imply perfect-cuboid existence/nonexistence.

```text
M2_1E9=51379127865
PRODUCTION_COMPLETE_THROUGH_B=1000000000
METHOD_AUDIT=PASS
DIRECT_INDEPENDENT_REGRESSION=PASS
M2_ASYMPTOTIC_INFERRED_FROM_CENSUS=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```