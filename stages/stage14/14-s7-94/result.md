# Stage14-s7-94 — primitive ratio pairs are prime-power orientations, and inner-ratio endpoints do not vanish geometrically

## Status

`COMPLETE_PRIMITIVE_RATIO_TO_PRIME_POWER_ORIENTATION_AND_INNER_ENDPOINT_GEOMETRY_NOGO`

Consumes batch-local `Stage14-s7-93`, merged `Stage14-s7-92`, merged mainline `Stage14-4fi/4fj`, and merged `Stage14-Work-bsX31`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Compress the primitive pair to q=uv

For every ratio candidate in s7-93 define

```text
q:=u*v.
```

Then

```text
q | n,
E=n/q,
gcd(u,v)=1,
u*v=q.
```

Write

```text
q=prod_p p^e_p.
```

Because `u` and `v` are coprime, each complete prime power `p^e_p` is assigned to exactly one side. Thus the primitive factorization is equivalent to an orientation vector

```text
epsilon_p in {+1,-1},
```

with

```text
u=prod_{epsilon_p=+1} p^e_p,
v=prod_{epsilon_p=-1} p^e_p.
```

The number of orientations is exactly

```text
2^omega(q)<=tau(q)=B^o(1)
```

on the polynomial Stage14 range. This recovers the already-charged fixed-`n` finite inner fiber; it is not a new saving.

```text
PRIMITIVE_PAIR_PRODUCT_Q_DEFINED=true
COPRIME_FACTOR_PAIR_EQUALS_FULL_PRIME_POWER_ORIENTATION=true
FIXED_Q_ORIENTATION_COUNT=Bo1
ORIENTATION_COUNT_RECHARGE_ALLOWED=false
```

## 2. The short ratio window is a signed logarithmic prime-power window

The ratio is exactly

```text
u/v
 = prod_p p^(epsilon_p*e_p),
```

so

```text
log(u/v)
 = sum_p epsilon_p*e_p*log p.
```

Therefore the multiplicatively short interval

```text
u/v in R_phys(n)
```

is an interval constraint on one signed prime-power subset sum. The complementary factor is independently reconstructed from

```text
E=n/q.
```

The s7-93 physical weight becomes

```text
1_{gcd(sqf(n/q),K_Z)=1}
* w_res(n,u,v,n/q).
```

No random-sign or independence model is introduced.

```text
RATIO_WINDOW_IS_SIGNED_PRIME_POWER_LOG_INTERVAL=true
COMPLEMENTARY_FACTOR_E=n_over_q
PRIME_POWER_ORIENTATION_RANDOMNESS_ASSUMED=false
```

## 3. Inner-ratio endpoints are not the radial endpoints already removed by 4fi

There are now two logically distinct endpoint notions:

```text
outer radial endpoint:
  n near an endpoint of the reciprocal product window;

inner ratio endpoint:
  one side u or v is small/subpolynomial inside a fixed interior n.
```

Merged 4fi discharges only the first. It does not imply that the second has fixed-power-small support.

Indeed the bare arithmetic constraints

```text
gcd(u,v)=1,
uv|n
```

permit endpoint-oriented factorizations such as

```text
u=1, v=q
```

or

```text
u=q, v=1
```

for every divisor `q|n`. Whether such an orientation lies in `R_phys(n)` is a physical-window question, not a consequence of divisor cardinality. Across polynomially many outer integers `n`, the existence of a small side therefore cannot be ruled out by the fixed-`n` `B^o(1)` fiber or by the already-used radial endpoint estimate.

So no uniform fixed-power loss may be charged merely from

```text
min(u,v)=B^o(1)
```

or from calling that configuration an endpoint.

```text
INNER_RATIO_ENDPOINT_DISTINCT_FROM_RADIAL_ENDPOINT=true
RADIAL_ENDPOINT_DISCHARGE_DOES_NOT_CLOSE_RATIO_ENDPOINT=true
SMALL_ONE_SIDE_GEOMETRY_ALONE_FIXED_POWER_SAVING=false
FIXED_N_FIBER_CANNOT_BE_REUSED_AS_OUTER_DENSITY_SAVING=true
```

## 4. Exact incidence after q-compression

The surviving physical incidence can now be written as

```text
I_ratio
 = sum_{n in N_int(theta)}
   sum_{q|n}
   sum_{epsilon on prime powers of q}
      1_{exp(sum epsilon_p e_p log p) in R_phys(n)}
      1_{gcd(sqf(n/q),K_Z)=1}
      w_res(n,u_epsilon,v_epsilon,n/q).
```

All sums are restricted to the inherited physical ranges and frozen labels. For one fixed `n`, this remains `B^o(1)` total inner candidates because it is exactly the same coordinate fiber as s7-92/4fj.

This representation exposes the arithmetic source of any possible thinning: a correlated orientation window together with a complementary-`E` physical weight.

## 5. Receiver and H decision

The receiver is not yet declared materially changed because the orientation language can be compressed one step further to the intrinsic unitary-divisor coordinate. That next step will convert the ratio interval into an ordinary short interval for a unitary divisor of `q` and freeze the exact weighted incidence to be handed to later theorem/adapter work.

No new sH is opened. Existing divisor-in-an-interval results do not automatically control a correlated full-prime-power orientation with the complementary `E` canonical weight.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_94_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_94=COMPLETE_PRIMITIVE_RATIO_TO_PRIME_POWER_ORIENTATION_AND_INNER_ENDPOINT_GEOMETRY_NOGO
PRIMITIVE_PAIR_PRODUCT_Q_DEFINED=true
COPRIME_FACTOR_PAIR_EQUALS_FULL_PRIME_POWER_ORIENTATION=true
RATIO_WINDOW_IS_SIGNED_PRIME_POWER_LOG_INTERVAL=true
INNER_RATIO_ENDPOINT_DISTINCT_FROM_RADIAL_ENDPOINT=true
SMALL_ONE_SIDE_GEOMETRY_ALONE_FIXED_POWER_SAVING=false
ORIENTATION_COUNT_RECHARGE_ALLOWED=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_94_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-95
```