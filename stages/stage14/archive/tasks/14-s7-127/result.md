# Stage14-s7-127 — exact pair-indexed filtered tau3 encoding on the polynomial outer-pair branch

## Status

`COMPLETE_POLYNOMIAL_PAIR_FIBERED_FILTERED_TAU3_ENCODING`

Consumes merged `Stage14-s7-125`, merged `Stage14-q18`, and batch-local `Stage14-s7-126`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Keep the charged outer pair

On the polynomial branch the charged outer variable is the pair `(E,m)`, while the internal square-class host is

```text
z=n=E*m.
```

Freeze one principal pair cell, packet coefficients and one ordered squarefree allocation. The first reverse layer is

```text
g*x*y = c_C*E*m,
R_mult(E,m;g,x,y)=1.
```

The prefilter and first-layer predicate remain pair-dependent exactly as in s7-122/s7-125.

## 2. Exact pair-indexed restricted ternary-divisor weight

Define

```text
N_mult_pair(E,m)
 := sum_{g*x*y=c_C*E*m} R_mult(E,m;g,x,y).
```

Then the first-layer support on the charged pair baseline is exactly

```text
(E,m) in S_mult_pair
iff
(E,m) in S_pre_pair and N_mult_pair(E,m)>=1.
```

Therefore q18's polynomial-pair support-moment handoff has an exact moment object without changing measure:

```text
M1_pair := sum_{(E,m) in S_pre_pair} N_mult_pair(E,m).
```

```text
Q18_POLYNOMIAL_PAIR_FIBERED_SUPPORT_MOMENT_TEST=PASS_EXACT_PAIR_INDEXED_WEIGHT
S_PAIR_FILTERED_TAU3_ENCODING_EXACT=true
```

## 3. No scalarization through n=Em

For fixed `n`, the number of factor pairs `(E,m)` with `E*m=n` is at most `d(n)=B^o(1)`, but that fact does not identify the indicators or weights because `S_pre_pair` and `R_mult(E,m;...)` depend on the charged pair.

Thus one may algebraically group the first moment by `n`,

```text
M1_pair
 = sum_n sum_{E*m=n, (E,m) in S_pre_pair} N_mult_pair(E,m),
```

but one may not replace the inner sum by a scalar support indicator or an unfiltered scalar `tau_3` weight.

```text
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
FIXED_N_PAIR_FIBER_RECHARGED=false
PAIR_CHARGED_MEASURE_PRESERVED=true
```

## 4. Uniform multiplicity envelope

Again `c_C*E*m <= B^O(1)`, hence pointwise

```text
0 <= N_mult_pair(E,m) <= d_3(c_C*E*m) <= B^o(1).
```

This is only a multiplicity envelope. It does not imply pair support.

```text
PAIR_FILTERED_TAU3_WEIGHT_UPPER_ENVELOPE=Bo1
PAIR_FILTERED_TAU3_MULTIPLICITY_RECHARGED=false
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-128
```

## Boundary

```text
STAGE14_S7_127=COMPLETE_POLYNOMIAL_PAIR_FIBERED_FILTERED_TAU3_ENCODING
Q18_POLYNOMIAL_PAIR_FIBERED_SUPPORT_MOMENT_TEST=PASS_EXACT_PAIR_INDEXED_WEIGHT
S_PAIR_FILTERED_TAU3_ENCODING_EXACT=true
PAIR_CHARGED_MEASURE_PRESERVED=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-128
```
