# Stage14-s7-95 — primitive coprime ratio windows are weighted unitary-divisor short intervals

## Status

`COMPLETE_PRIMITIVE_RATIO_WINDOW_TO_WEIGHTED_UNITARY_DIVISOR_SHORT_INTERVAL_RECEIVER`

Consumes batch-local `Stage14-s7-93/94`, merged mainline `Stage14-4fi/4fj`, merged `Stage14-Work-bsX31`, and merged q14 as the existing divisor-window literature boundary.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Unitary-divisor form of the primitive pair

Stage14-s7-94 writes

```text
q=u*v,
gcd(u,v)=1.
```

Thus `u` is a unitary divisor of `q`:

```text
u | q,
gcd(u,q/u)=1.
```

Write this as

```text
u || q.
```

Conversely every unitary divisor `u||q` determines exactly

```text
v=q/u,
gcd(u,v)=1.
```

Hence the primitive pair and the unitary divisor are exactly equivalent coordinates.

```text
PRIMITIVE_COPRIME_PAIR_EQUIVALENT_TO_UNITARY_DIVISOR=true
UNITARY_DIVISOR_COORDINATE=u_double_bar_q
```

## 2. The ratio interval becomes an ordinary short interval for u

Let the exact positive primitive-ratio window at one accepted outer integer be

```text
R_phys(n)=[r_-(n),r_+(n)].
```

Since

```text
u/v=u^2/q,
```

the condition

```text
u/v in R_phys(n)
```

is exactly

```text
boxed:
sqrt(q*r_-(n)) <= u <= sqrt(q*r_+(n)).
```

Define

```text
U_phys(n,q)
 := [sqrt(q*r_-(n)), sqrt(q*r_+(n))].
```

The multiplicative width satisfies

```text
width_mult(U_phys(n,q))
 = sqrt(r_+(n)/r_-(n)).
```

After the legal dyadic localization this is `B^o(1)`. On the merged 4fi interior packet, the reciprocal `L` window has logarithmic width at least `B^(-theta+o(1))`; because `L/n=u/v`, the corresponding `u` interval has logarithmic width at least

```text
(1/2) B^(-theta+o(1))
 = B^(-theta+o(1)).
```

Thus the heavy packet is supported on genuine interior short unitary-divisor intervals, not on a vanishing radial endpoint strip.

```text
RATIO_WINDOW_TO_UNITARY_DIVISOR_INTERVAL_EXACT=true
UNITARY_DIVISOR_INTERVAL_MULTIPLICATIVE_WIDTH=Bo1
INTERIOR_UNITARY_INTERVAL_LOG_WIDTH_LOWER_BOUND=B^(-theta+o(1))
```

## 3. Freeze the exact complementary physical weight

Because

```text
q|n,
E=n/q,
v=q/u,
```

all normalized moving coordinates are determined by `(n,q,u)`. Define

```text
W_unit(n,q,u)
 := 1_{gcd(sqf(n/q),K_Z)=1}
    * w_res(n,u,q/u,n/q).
```

Then

```text
0<=W_unit(n,q,u)<=1,
```

and the full surviving heavy incidence is exactly

```text
I_unit
 := sum_{n in N_int(theta)}
    sum_{q|n}
    sum_{
      u || q,
      u in U_phys(n,q)
    }
      W_unit(n,q,u).
```

The coordinate changes in s7-93..95 are bijective on accepted candidates, so

```text
I_unit=I_ratio=I_int
```

up to only the already-frozen finite labels. Therefore

```text
I_unit>=B^(mu-o(1)).
```

For one fixed `n`, the full `(q,u)` candidate set is still `B^o(1)`; this is the already-charged fixed-outer fiber and cannot be used again as a density gain.

```text
WEIGHTED_UNITARY_DIVISOR_INCIDENCE_DEFINED=true
WEIGHTED_UNITARY_INCIDENCE_REQUIRED_EXPONENT=mu
FIXED_N_UNITARY_CANDIDATE_FIBER=Bo1
FIXED_N_UNITARY_FIBER_RECHARGED=false
```

## 4. Relation to q14 / Ford and exact current no-go

Merged q14 identifies Ford-type divisor-in-an-interval estimates as the closest architecture for the global/s reciprocal-window problem, but finds no theorem directly preserving the charged squareclass/physical measure.

The present reduction sharpens the mismatch. The inner arithmetic object is not merely

```text
a divisor d of one integer lying in a short interval.
```

It is

```text
q|n,
u||q,
u in U_phys(n,q),
```

weighted by the correlated complementary cofactor

```text
E=n/q
```

through `W_unit`, including the kernel coprimality and unresolved canonical/reverse-completion Boolean.

Therefore neither ordinary-divisor short-interval density nor generic unitary-divisor density may be multiplied into the Stage14 ledger without a weight-preserving transfer theorem.

```text
Q14_FORD_GEOMETRY_RETAINED_AS_NEAR_ARCHITECTURE=true
FORD_DIRECTLY_APPLICABLE_TO_WEIGHTED_UNITARY_INCIDENCE=false
GENERIC_UNITARY_DIVISOR_DENSITY_RECHARGE_ALLOWED=false
PHYSICAL_WEIGHT_PRESERVING_TRANSFER_PROVED=false
```

## 5. Material receiver change

The s-route heavy branch is now a fully explicit three-coordinate weighted arithmetic incidence:

```text
outer normalized radial n,
divisor q|n,
unitary divisor u||q in a short physical interval,
complement E=n/q carrying the physical weight.
```

The minimal receiver becomes

```text
FixedPrimitiveRayFixedAgreementPairInteriorNormalizedRadialWeightedUnitaryDivisorShortIntervalPhysicalIncidenceWithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu.
```

This is materially sharper than the primitive ratio formulation and triggers the batch stop.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairInteriorNormalizedRadialWeightedUnitaryDivisorShortIntervalPhysicalIncidenceWithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu
RECEIVER_MATERIALLY_CHANGED=true
```

## 6. H decision

No new sH is opened in this batch. q14 has already supplied the relevant literature boundary and explicitly found no direct full-obstruction theorem. The remaining internal task is to open `w_res` through the merged fixed-data reverse reconstruction and determine whether the canonical/reverse Boolean reduces to divisor-many local labels or remains a genuinely correlated weight.

Only after that decomposition can a new Ford-transfer / weighted-unitary-divisor theorem target be frozen without losing the physical measure.

```text
S7_95_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_95=COMPLETE_PRIMITIVE_RATIO_WINDOW_TO_WEIGHTED_UNITARY_DIVISOR_SHORT_INTERVAL_RECEIVER
PRIMITIVE_COPRIME_PAIR_EQUIVALENT_TO_UNITARY_DIVISOR=true
RATIO_WINDOW_TO_UNITARY_DIVISOR_INTERVAL_EXACT=true
WEIGHTED_UNITARY_DIVISOR_INCIDENCE_DEFINED=true
WEIGHTED_UNITARY_INCIDENCE_REQUIRED_EXPONENT=mu
FORD_DIRECTLY_APPLICABLE_TO_WEIGHTED_UNITARY_INCIDENCE=false
PHYSICAL_WEIGHT_PRESERVING_TRANSFER_PROVED=false
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairInteriorNormalizedRadialWeightedUnitaryDivisorShortIntervalPhysicalIncidenceWithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_95_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-96
```