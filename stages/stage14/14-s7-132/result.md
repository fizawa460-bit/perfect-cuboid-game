# Stage14-s7-132 — witness-dependence separability test for the conditioned second-reverse correlation

## Status

`COMPLETE_WITNESS_DEPENDENCE_SEPARABILITY_TEST_NEGATIVE`

Consumes merged `Stage14-s7-129..131` and merged `Stage14-Work-ceX43/q20` from main

```text
b75d2784850766f936c9c7e586de7005f379094a
```

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exact dependence from the reverse dictionary

For one retained first-layer witness `lambda`, merged s7-119 gives

```text
F2^-*F2^+=W2(z),
cp=(F2^++F2^-)/2,
dq=(F2^+-F2^-)/2,
```

followed by ordered factorizations

```text
cp=c*p,
dq=d*q.
```

The second reciprocal product is then

```text
W1(lambda)=4*r_ep*s_ep*epsilon_k*p*q.
```

Thus `W1` depends on the retained first-layer witness through the chosen `F2` factor pair and the induced factorizations of `cp,dq`.  It is not determined by the charged outer scalar `z` alone, and on the polynomial branch it is not determined by the charged pair `(E,m)` alone.

## 2. Separability test

A q20-style fixed-shift or fixed-form transfer would require the second-layer arithmetic object to depend only on the charged outer variable(s), up to frozen packet coefficients and `B^o(1)` labels that may be frozen without changing the support problem.

That condition fails here: two retained first-layer witnesses above the same outer point may have different `(p,q)` and hence different `W1`.  Freezing one `(p,q)` is not free at the outer-support level because existence of such a witness is exactly part of the conditioned correlation being counted.

Therefore

```text
Q20_WITNESS_DEPENDENCE_SEPARABILITY_TEST=FAIL_INTRINSIC_FIRST_WITNESS_DEPENDENCE
SECOND_REVERSE_W1_OUTER_ONLY=false
FIRST_LAYER_WITNESS_CAN_BE_SUMMED_AWAY_FOR_FREE=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
```

This is a logical nonseparability statement, not a claim that no later transformation can reorganize the joint sum.

## 3. No recharge

The already proved `B^o(1)` multiplicities of first-layer and second-layer witnesses remain multiplicity envelopes only.  They cannot be used to select one witness and infer an outer density saving.

```text
FIRST_LAYER_MULTIPLICITY_RECHARGED=false
SECOND_LAYER_MULTIPLICITY_RECHARGED=false
```

## 4. Boundary

The correct next operation is to normalize the exact second-layer divisor predicate while retaining `lambda` as an index.

```text
STAGE14_S7_132=COMPLETE_WITNESS_DEPENDENCE_SEPARABILITY_TEST_NEGATIVE
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-133
```
