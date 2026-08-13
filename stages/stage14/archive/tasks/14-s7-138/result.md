# Stage14-s7-138 — exact pushforward disintegration over the q17 reciprocal-CRT kernel

## Status

`COMPLETE_Q17_KERNEL_PUSHFORWARD_MEASURE_DISINTEGRATION`

Consumes merged `Stage14-s7-137` and merged `Stage14-Work-cgX45` from main `fa189bcb7cac4eb29d8a277130a3fa261f4691d8`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Retain the charged s witness measure

Let `Lambda_s` denote one frozen principal-cell family of retained first-layer filtered-tau3 witnesses. It is scalar-indexed on the two one-dimensional branches and `(E,m)`-indexed on the polynomial pair branch. No scalarization of the latter is allowed.

Merged cfX44/s7-135 identify the second-reverse inner arithmetic with the q17 reciprocal-CRT kernel. For each `lambda in Lambda_s`, let

```text
pi(lambda)=theta(lambda)
```

be the complete inner-kernel packet needed to evaluate the q17 reciprocal-CRT predicate: frozen `(U,V)`, the exact product `W1(lambda)`, inherited sign/two-primary labels, and every already-exposed local filter that belongs to the inner reciprocal-CRT layer.

This map is bookkeeping only; it does not change the charged outer measure.

## 2. Exact pushforward weights

For a kernel packet `theta`, define

```text
a_s(theta) := #{ lambda in Lambda_s : pi(lambda)=theta }.
```

Let `a_q17(theta)` denote the multiplicity/weight with which the corresponding kernel packet occurs in the q17 fixed-E primitive-pair baseline, when that packet belongs to the q17 theorem domain, and zero otherwise.

Then any nonnegative inner-kernel test function `K(theta)` satisfies the exact identity

```text
sum_{lambda in Lambda_s} K(pi(lambda))
 = sum_theta a_s(theta) K(theta).
```

Thus the conditioned q17-to-s transfer problem is exactly a pushforward-weight comparison problem, not a new inner arithmetic problem.

```text
S_Q17_KERNEL_PUSHFORWARD_DISINTEGRATION_PROVED=true
S_CONDITIONED_MEASURE_TRANSFER_REDUCED_TO_PUSHFORWARD_WEIGHT_COMPARISON=true
```

## 3. Why kernel equality is insufficient

A lower-ratio theorem on the q17 baseline controls a weighted sum with `a_q17(theta)`. The s receiver needs the same kernel predicate against `a_s(theta)`. Equality of kernel equations does not compare these weights.

The `B^o(1)` witness-fiber bounds proved earlier give only pointwise upper multiplicity information for preimages of `pi`; they do not imply that q17-good packets carry positive s weight, nor that the s mass avoids q17-sparse packets.

```text
IDENTICAL_KERNEL_DOES_NOT_COMPARE_PUSHFORWARD_WEIGHTS=true
BO1_FIBER_DOES_NOT_IMPLY_LOWER_DOMINATION=true
Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false
```

## 4. Next test

The next stage freezes a sufficient transfer criterion in terms of lower domination / coverage of q17-good kernel mass by `a_s`, with separate scalar and polynomial-pair charged measures.

```text
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-139
```
