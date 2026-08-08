# E-1c — cutoff scaling and directional-ratio analysis

> **STATUS:** `E_1C_COMPLETE_AT_FINITE_SCALING_DIAGNOSTIC_LEVEL`
>
> **COUNTING:** primitive canonical `0<a<b<c`, common geometric cutoff `a^2+b^2+c^2<=B^2`
>
> **SPACE DIAGONAL:** integrality not required

E-1c extends the E-1b exactly-one population profile from `B=10,000` to `B=500,000` and tests whether the apparent `2:1:1` shape persists.

## 1. Extended population table

| B | N_ab | N_ac | N_bc | ab/bc | ac/bc |
|---:|---:|---:|---:|---:|---:|
| 10,000 | 31,593,274 | 14,373,282 | 16,389,285 | 1.927679 | 0.876993 |
| 20,000 | 137,675,586 | 62,698,520 | 70,266,959 | 1.959322 | 0.892290 |
| 50,000 | 953,782,022 | 434,710,270 | 477,608,567 | 1.996995 | 0.910181 |
| 100,000 | 4,097,242,942 | 1,868,209,055 | 2,026,452,228 | 2.021880 | 0.921911 |
| 200,000 | 17,516,747,856 | 7,990,469,902 | 8,569,465,813 | 2.044089 | 0.932435 |
| 500,000 | 118,791,437,295 | 54,216,622,276 | 57,394,634,228 | 2.069731 | 0.944629 |

At the largest cutoff,

```text
N_ab:N_ac:N_bc
≈ 2.069731 : 0.944629 : 1.
```

The normalized vector is approximately

```text
(0.5155818, 0.2353124, 0.2491057).
```

## 2. The finite `2:1:1` picture bends rather than stops

The leading ratio does not approach `2` from below and then settle there. It is

```text
ab/bc = 1.996995... at B=50,000
ab/bc = 2.021880... at B=100,000
```

so it crosses `2` between these sampled cutoffs and continues upward to `2.069731...` by `B=500,000`.

The secondary ratio remains below `1` throughout the audited range,

```text
ac/bc = 0.944629... at B=500,000,
```

but it continues to increase.

Therefore E-1c rejects the naive finite interpretation that the ratios simply converge to `2:1:1` from the observed side. No monotonicity theorem is claimed.

## 3. Scale diagnostic

The quantities

```text
N_q(B) / [B^2 log B]
```

vary slowly over the high-cutoff range. At `B=10,000 -> 500,000` they move approximately as

```text
ab: 0.034302 -> 0.036210
ac: 0.015606 -> 0.016526
bc: 0.017794 -> 0.017495
```

so `B^2 log B` is a natural scale to test next. E-1c does not promote this diagnostic to an asymptotic theorem.

## 4. Comparison with the space-diagonal-side chamber vector

The already-proved Stage13 space-diagonal-side chamber ratio is

```text
2.431684750178191 : 1.115756428951881 : 1.
```

For the E-1c high-cutoff data, purely diagnostic fits in

```text
x = 1/log B
```

give the following `x -> 0` intercepts:

```text
linear fit:
  ab/bc -> 2.404489
  ac/bc -> 1.103842

quadratic fit:
  ab/bc -> 2.454947
  ac/bc -> 1.122531
```

The Stage13 chamber ratio lies between the linear and quadratic diagnostics in both coordinates.

This is strong numerical evidence that the two tracks may share the same leading canonical chamber vector despite having different space-diagonal integrality conditions. **It is not yet a proof that the Euler-side limit exists or equals the Stage13 limit.**

## 5. Decision

```text
E_1C=COMPLETE_AT_FINITE_SCALING_DIAGNOSTIC_LEVEL
CANONICAL_ORDER=0<a<b<c
SPACE_DIAGONAL_INTEGRALITY_REQUIRED=false
LARGEST_B=500000
AB_OVER_BC_CROSSES_2_IN_AUDITED_RANGE=true
AC_OVER_BC_CROSSES_1_IN_AUDITED_RANGE=false
NAIVE_LIMIT_2_1_1_SUPPORTED=false
B2_LOG_B_IS_NATURAL_NEXT_SCALE_DIAGNOSTIC=true
SAME_LIMIT_AS_STAGE13_PROVED=false
FINITE_DATA_CONSISTENT_WITH_STAGE13_CHAMBER=true
NEXT=E-1d structural explanation of the directional profile
```
