# Stage14-numα11-diag6 — matched Stage13 exactly-one vs Stage14 exactly-two comparison

## Result

This stage compares the Stage13 finite exactly-one census and the Stage14 frozen exactly-two census under the same primitive canonical convention and the same space-diagonal cutoff `d<=B`.

Matched cutoffs:

```text
B = 1k, 2k, 5k, 10k, 20k, 50k, 100k
```

At every one of these cutoffs the Stage14 exactly-two vector reconstructed from the frozen B500m object source agrees exactly with the Stage13 overlap ledger:

```text
a = ab & ac only
b = ab & bc only
c = ac & bc only
```

There are no triples in the matched window.

## 1. The finite `2:1:1 -> 2:2:1` intuition is real, but only as shorthand

At `B=100000`, Stage13 exactly-one gives

```text
(ab,ac,bc) = (84146,43180,40704)
ratios      = (0.500780,0.256978,0.242242)
```

which is still very close to the familiar finite `2:1:1` pattern. Its L1 distance to `(1/2,1/4,1/4)` is only

```text
0.0155151.
```

The matched exactly-two population is

```text
(a,b,c) = (33,33,23)
ratios  = (0.370787,0.370787,0.258427).
```

The empirical Stage14 reference `(0.4,0.4,0.2)` is therefore already visible qualitatively, but not stably: the L1 distance at B100k is `0.116854`.

At B500m, where Stage14 has 3495 exactly-two objects, the cumulative vector becomes

```text
(a,b,c) = (1374,1371,750)
ratios  = (0.393133,0.392275,0.214592)
```

with L1 distance only `0.0291845` from `2:2:1`.

Thus

```text
finite one-face near 2:1:1
    -> finite two-face cumulative near 2:2:1
```

is a useful empirical shorthand for what originally motivated Stage14.

It is **not** a theorem-to-theorem transition. Stage13 proves the exactly-one limit

```text
(0.5347369332, 0.2453591778, 0.2199038889),
```

which is not exactly `2:1:1`, while Stage14 has not proved any limiting exactly-two direction law.

## 2. Matched cumulative panel

```text
B       exactly-one (ab,ac,bc)      exactly-two (a,b,c)
1k      (304,158,138)                (2,0,0)
2k      (698,369,367)                (2,2,1)
5k      (2288,1129,1068)             (6,6,3)
10k     (5261,2726,2643)             (9,11,5)
20k     (12375,6258,6079)            (16,16,10)
50k     (36966,19042,17867)          (24,24,14)
100k    (84146,43180,40704)          (33,33,23)
```

The `B=100k` population ratio is

```text
N2/N1 = 89/168030 = 0.0005296673.
```

So the second-face population is already a very thin subset in the finite Stage13 window.

## 3. Same shells expose a strong stability difference

Non-overlapping matched shells are

```text
(0,1k]       N1=600    N2=2
(1k,2k]      N1=834    N2=3
(2k,5k]      N1=3051   N2=10
(5k,10k]     N1=6145   N2=10
(10k,20k]    N1=14082  N2=17
(20k,50k]    N1=49163  N2=20
(50k,100k]   N1=94155  N2=27
```

The exactly-one shell proportions settle rapidly toward the finite near-`2:1:1` regime. For example:

```text
(10k,20k]  = (0.505184,0.250817,0.243999)
(20k,50k]  = (0.500193,0.260033,0.239774)
(50k,100k] = (0.501089,0.256365,0.242547)
```

The exactly-two shell vectors remain much more erratic:

```text
(5k,10k]    (3,5,2) = (0.3000,0.5000,0.2000)
(10k,20k]   (7,5,5) = (0.4118,0.2941,0.2941)
(20k,50k]   (8,8,4) = (0.4000,0.4000,0.2000)
(50k,100k]  (9,9,9) = (0.3333,0.3333,0.3333)
```

Restricting to adjacent shell transitions whose lower endpoint is at least 5k:

```text
max exactly-one adjacent L1 shift = 0.0427519
max exactly-two adjacent L1 shift = 0.4117647
```

The two-face shell counts are tiny (`10–27` here), so this is a finite descriptive comparison rather than a statistical or asymptotic conclusion. But it directly explains why a cumulative stability rule that looked harmless for the one-face population is much less reliable for the two-face population.

## 4. Interpretation

The matched comparison separates three statements that had been easy to blur together:

1. Stage13 finite data really do sit close to `2:1:1` over the accessible panel.
2. Stage14 cumulative B500m data really do sit close to `2:2:1`.
3. Neither observation implies a literal asymptotic transition `2:1:1 -> 2:2:1`.

The next natural object is therefore not another shell refinement. It is the **conditional second-face survival map**: starting from a distinguished one-face category, which additional face survives, and with what finite directional probability? That directly connects the Stage13 and Stage14 observables rather than merely juxtaposing their normalized vectors.

## Boundary

```text
STAGE14_NUM_ALPHA11_DIAG6=MATCHED_STAGE13_EXACTLY_ONE_VS_STAGE14_EXACTLY_TWO_COMPARISON_COMPLETE
MATCHED_CUTOFF_MAX=100000
STAGE13_STAGE14_EXACTLY_TWO_RECOMPOSITION_EXACT=true
B100K_N1=168030
B100K_N2=89
B100K_EXACTLY_ONE_COUNTS=84146,43180,40704
B100K_EXACTLY_TWO_COUNTS=33,33,23
B500M_EXACTLY_TWO_COUNTS=1374,1371,750
FINITE_2_1_1_TO_2_2_1_USEFUL_SHORTHAND=true
LITERAL_THEOREM_TO_THEOREM_2_1_1_TO_2_2_1=false
EXACTLY_ONE_FINITE_SHELL_VECTOR_MORE_STABLE_IN_MATCHED_WINDOW=true
EXACTLY_TWO_SMALL_SHELL_COUNTS_LIMIT_STRENGTH=true
ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM=false
NEXT=Stage14-num-alpha11-diag7 conditional second-face survival by source-face category
```
