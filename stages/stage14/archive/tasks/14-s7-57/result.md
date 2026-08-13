# Stage14-s7-57 — Bernoulli Fréchet envelope audit for dense pair covariance

## Status

`COMPLETE_BERNOULLI_FRECHET_ENVELOPE_NO_NEAR_DETERMINISM_FROM_EXPONENT_SATURATION`

Consumes merged `Stage14-s7-56`, merged `Stage14-s7-55`, merged `Stage14-4dm`, merged `Stage14-s7-52`, and merged `Stage14-X15`.

The whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

For a representative pair write

```text
X=W_i,
Y=W_j,
a=E X,
b=E Y,
p=E(XY),
Gamma=p-ab.
```

On the surviving s7-52/s7-56 interior-dense cells,

```text
a,b,p = B^(-o(1)),
1-a,1-b = B^(-o(1)).
```

For Bernoulli variables the exact Fréchet bounds are

```text
max(0,a+b-1) <= p <= min(a,b).
```

Hence the maximal positive covariance at fixed marginals is

```text
M_+(a,b)
 := min(a,b)-ab
 = min(a(1-b), b(1-a)).
```

Therefore

```text
0 <= Gamma^+ <= M_+(a,b).
```

Define the normalized positive-correlation ratio

```text
eta := Gamma^+/M_+(a,b)
```

when `M_+>0`, and `eta=0` otherwise. Then `0<=eta<=1`.

## Fixed-power small eta is already sub-square-root

If

```text
eta <= B^(-delta+o(1)),
```

then, since `M_+(a,b)<=1`, the positive pairwise contribution is

```text
<< B^(1/2-delta+o(1)).
```

Thus square-root pairwise saturation requires

```text
eta=B^(-o(1)).
```

This is consistent with the merged 4dl correlation-ratio localization.

## Crucial no-go: exponent saturation does not imply near-deterministic coupling

The condition

```text
eta=B^(-o(1))
```

only says that `eta` has no fixed-power decay. It does **not** imply

```text
eta=1-B^(-delta+o(1))
```

or any analogous near-extremal Fréchet saturation.

Indeed take fixed interior marginals

```text
a=b=1/2.
```

Then `M_+=1/4`. Choosing for example

```text
p=3/8
```

gives

```text
Gamma=1/8,
eta=1/2.
```

This has exponent-zero positive covariance and therefore can remain at square-root scale, but is bounded away from deterministic equality `X=Y` by a fixed constant.

Hence no legal fixed-power peel follows from replacing the current pairwise receiver by a "near deterministic pair coupling" receiver.

```text
PAIRWISE_SQRT_SATURATION_IMPLIES_NEAR_DETERMINISTIC_COUPLING=false
PAIRWISE_FRECHET_RATIO_FIXED_POWER_SMALL_STRICT_SUBSQRT=true
PAIRWISE_SQRT_SATURATION_REQUIRES_ETA=Bo0=true
PAIRWISE_ETA=Bo0_DOES_NOT_IMPLY_ETA_NEAR_ONE=true
```

## Consequence

The pairwise branch remains exactly the two mechanisms isolated by merged 4dm:

```text
1. positive zero-mode cofactor covariance;
2. positive masked full-conductor inverse-fraction covariance.
```

Bernoulli extremal geometry supplies no additional fixed-power saving after the existing variance/joint-density peels.

The next internal task is therefore not another probabilistic normalization. It is the q11/4dm-recommended arithmetic factorization test of the zero-mode cofactor covariance, while retaining the masked centered inverse-fraction branch separately.

No new auxiliary H is opened.

```text
STAGE14_S7_57=COMPLETE_BERNOULLI_FRECHET_ENVELOPE_NO_NEAR_DETERMINISM_FROM_EXPONENT_SATURATION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PAIRWISE_FRECHET_ENVELOPE_EXACT=true
PAIRWISE_NEAR_DETERMINISM_PROMOTION_LEGAL=false
PAIRWISE_ZERO_MODE_COFACTOR_COVARIANCE_REMAINS=true
PAIRWISE_MASKED_CENTERED_INVERSE_FRACTION_COVARIANCE_REMAINS=true
S7_57_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT=Stage14-s7-58
```
