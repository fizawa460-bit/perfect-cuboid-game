# Stage14-s7-126 — exact scalar filtered tau3 encoding of the first reverse layer

## Status

`COMPLETE_SCALAR_FILTERED_TAU3_ENCODING`

Consumes merged `Stage14-s7-125` and merged `Stage14-q18`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Frozen scalar packet

Work on one principal scalar cell of either active one-dimensional realization from s7-125: the fixed-E endpoint branch or the polynomial-E fixed-product branch. Freeze the packet coefficients and one ordered squarefree allocation from s7-124. The charged outer variable is one scalar `z` and the first reverse layer is

```text
g*x*y = c_C*z,
R_mult(z;g,x,y)=1,
```

where `R_mult` is the exact deterministic conjunction of the already-exposed first-layer positivity, parity, order, endpoint/cell and divisibility conditions. No residual second-layer or post-mask condition is inserted into `R_mult`.

## 2. Exact restricted ternary-divisor weight

Define

```text
N_mult(z)
 := sum_{g*x*y=c_C*z} R_mult(z;g,x,y).
```

Equivalently this is a restricted generalized ternary-divisor weight on the integer `c_C*z`, with the outer scalar `z` retained as a parameter of the filter. Then, by definition of `S_mult` in s7-125,

```text
z in S_mult
iff
z in S_pre and N_mult(z)>=1.
```

Thus the q18 scalar encoding test has an exact answer:

```text
Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST=PASS_EXACT_RESTRICTED_WEIGHT
S_SCALAR_FILTERED_TAU3_ENCODING_EXACT=true
```

This statement is only an encoding. It does **not** identify `N_mult` with an unfiltered classical `tau_3`, and it does not make an AP theorem applicable.

## 3. Uniform multiplicity envelope

All variables are polynomially bounded on the Stage14 packet, so `c_C*z <= B^O(1)`. Hence

```text
0 <= N_mult(z) <= d_3(c_C*z) <= B^o(1)
```

uniformly on the frozen principal cell.

The upper bound is a witness-multiplicity envelope only. It is not a density saving and does not imply `N_mult(z)>0`.

```text
SCALAR_FILTERED_TAU3_WEIGHT_UPPER_ENVELOPE=Bo1
SCALAR_FILTERED_TAU3_MULTIPLICITY_RECHARGED=false
```

## 4. Theorem-import boundary

q18 found nearby generalized-divisor/AP moment architectures but no direct theorem for the exact filtered support. The normalization here makes the missing adapter precise: a usable first-moment theorem must preserve the frozen squarefree allocation and the exact `R_mult` filter on every principal scalar cell.

No theorem is imported at this stage.

```text
S7_126_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT=Stage14-s7-127
```

## Boundary

```text
STAGE14_S7_126=COMPLETE_SCALAR_FILTERED_TAU3_ENCODING
Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST=PASS_EXACT_RESTRICTED_WEIGHT
S_SCALAR_FILTERED_TAU3_ENCODING_EXACT=true
SCALAR_FILTERED_TAU3_WEIGHT_UPPER_ENVELOPE=Bo1
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-127
```
