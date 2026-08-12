# Stage14-s7-129 — exact conditioned second-reverse extension weight

## Status

`COMPLETE_CONDITIONED_SECOND_REVERSE_EXACT_WEIGHT_ENCODING`

Consumes merged `Stage14-s7-128`, merged `Stage14-Work-cdX42`, and merged `Stage14-q19` from main `238642b4140a7320f4b2f5e9c601b87f02b217f8`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Charged first-layer baseline is retained

On either scalar branch let a charged first-layer object be

```text
lambda=(z;g,x,y)
```

with

```text
g*x*y=c_C*z,
R_mult(lambda)=1.
```

On the polynomial branch retain the charged outer pair and write

```text
lambda=(E,m;g,x,y),
z=E*m,
g*x*y=c_C*E*m,
R_mult(lambda)=1.
```

No grouping by `z=Em` changes the charged pair measure.

## 2. Exact extension multiplicity

For a fixed first-layer witness `lambda`, all quantities entering the next reciprocal reconstruction are deterministic polynomial-height integers. Let `W1(lambda)` be the exact second reciprocal product from the already merged reverse dictionary. Define

```text
N_rev2(lambda)
 := #{ admissible positive second-layer factor pairs
       (F1^-,F1^+) :
       F1^-*F1^+=W1(lambda),
       inherited cp=c*p and dq=d*q reconstruction holds,
       all second-layer positivity/parity/order/divisibility filters hold }.
```

The residual root/canonical/post-column mask is deliberately excluded.

Equivalently, writing `f=F1^-` and `F1^+=W1/f`, the factor-pair equations together with the reciprocal reconstruction can be tested by the exact divisibility predicates inherited from the frozen reverse dictionary. This is one divisor variable `f|W1(lambda)` plus deterministic filters; no new free polynomial-dimensional witness is introduced.

By definition,

```text
lambda extends through the second reverse layer
iff
N_rev2(lambda)>=1.
```

Therefore q19's primary handoff passes exactly:

```text
Q19_SECOND_REVERSE_EXACT_WEIGHT_ENCODING_TEST=PASS
S_SECOND_REVERSE_EXACT_EXTENSION_WEIGHT_DEFINED=true
POST_MASK_INSERTED_IN_N_REV2=false
PAIR_CHARGED_MEASURE_PRESERVED=true
```

## 3. Uniform multiplicity envelope

All relevant integers are polynomially bounded in `B`. For fixed `lambda`, the possible `f` are divisors of `W1(lambda)`, hence

```text
0 <= N_rev2(lambda) <= tau(W1(lambda)) = B^o(1)
```

uniformly on every frozen principal cell. Any bounded parity/orientation decoration is absorbed into the same `B^o(1)` envelope.

This is only a witness multiplicity bound. It gives no positive extension density by itself.

```text
SECOND_REVERSE_EXTENSION_MULTIPLICITY_UPPER_ENVELOPE=Bo1
SECOND_REVERSE_MULTIPLICITY_RECHARGED_AS_SAVING=false
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-130
```

## Boundary

```text
STAGE14_S7_129=COMPLETE_CONDITIONED_SECOND_REVERSE_EXACT_WEIGHT_ENCODING
Q19_SECOND_REVERSE_EXACT_WEIGHT_ENCODING_TEST=PASS
S_SECOND_REVERSE_EXACT_EXTENSION_WEIGHT_DEFINED=true
SECOND_REVERSE_EXTENSION_MULTIPLICITY_UPPER_ENVELOPE=Bo1
POST_MASK_INSERTED_IN_N_REV2=false
PAIR_CHARGED_MEASURE_PRESERVED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-130
```
