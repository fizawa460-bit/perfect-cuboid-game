# Stage14-s7-139 — sufficient lower-domination criterion for q17-to-s conditioned transfer

## Status

`COMPLETE_PUSHFORWARD_LOWER_DOMINATION_TRANSFER_CRITERION`

Consumes batch-local `Stage14-s7-138`.

## 1. Frozen inner predicate

Let `K(theta) in {0,1}` be the reciprocal-CRT acceptance predicate on the common q17 inner kernel. The q17 baseline and the s conditioned baseline carry weights `a_q17(theta)` and `a_s(theta)` respectively.

A q17 lower-ratio theorem has the form, on one principal q17 cell,

```text
sum_theta a_q17(theta) K(theta)
 >= B^(-o(1)) sum_theta a_q17(theta).
```

The desired s conclusion is

```text
sum_theta a_s(theta) K(theta)
 >= B^(-o(1)) sum_theta a_s(theta).
```

## 2. Sufficient adapter

A sufficient fixed-power transfer adapter is two-sided `B^o(1)` comparability on the relevant common kernel support, together with negligible s mass outside the q17 theorem domain. Concretely, if there is `eps(B)=o(1)` such that

```text
B^(-eps) a_q17(theta) <= a_s(theta) <= B^(eps) a_q17(theta)
```

for all relevant `theta`, and

```text
sum_{theta outside q17 domain} a_s(theta)
 <= B^(-delta+o(1)) sum_theta a_s(theta)
```

for some fixed `delta>0` (or the outside mass is zero), then the q17 lower ratio transfers at fixed-power precision.

The same proof works with cellwise lower domination plus a matching total-mass upper comparison; full pointwise symmetry is stronger than necessary.

```text
Q17_TO_S_LOWER_DOMINATION_CRITERION_PROVED=true
POINTWISE_TWO_SIDED_COMPARABILITY_IS_SUFFICIENT_NOT_NECESSARY=true
```

## 3. Current evidence does not establish the criterion

Existing Stage14 `B^o(1)` fiber bounds prove at most an upper multiplicity envelope. They do not give:

- support coverage of q17-good packets by the s pushforward;
- a lower bound for `a_s(theta)` relative to `a_q17(theta)`;
- negligible s mass outside the q17 theorem domain.

Therefore the sufficient adapter is not currently verified.

```text
S_PUSHFORWARD_LOWER_DOMINATION_PROVED=false
S_PUSHFORWARD_Q17_DOMAIN_COVERAGE_PROVED=false
Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false
```

## 4. Branch firewall

The scalar and polynomial `(E,m)` branches retain distinct charged outer measures. The criterion must be checked separately for both theorem species; grouping the pair branch by `n=Em` is not a proof of comparability.

```text
S_MEASURE_TRANSFER_VARIANT_COUNT=2
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-140
```
