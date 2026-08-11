# Stage14-s-batch report — s7-93 through s7-95

```text
STAGE14_S_BATCH=COMPLETE
BATCH_START_MAIN_SHA=1cce848e748d6b02d7e878c6bd1b326e953bc98c
BATCH_PUBLICATION_MAIN_SHA=1cce848e748d6b02d7e878c6bd1b326e953bc98c
BATCH_FIRST_STAGE=Stage14-s7-93
BATCH_LAST_STAGE=Stage14-s7-95
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_S_RECEIVER=FixedPrimitiveRayFixedAgreementPairInteriorNormalizedRadialWeightedUnitaryDivisorShortIntervalPhysicalIncidenceWithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-96
```

This batch consumes merged `s7-90..92`, merged mainline `4fi/4fj`, merged `Work-bsX31`, and merged q14 as the existing literature-routing boundary.

`Stage14-s7-93` consumes the already-proved global/s radial endpoint discharge rather than recharging it. It pulls the merged physical `(n,L)` incidence exactly to

```text
n=E*u*v,
gcd(u,v)=1,
E=n/(uv),
L=n*u/v,
```

and defines the physical Boolean `w_ratio(n,u,v,E)`. The identity `E=sqf(E)*square` is tautological for every positive integer and supplies no density saving. The genuine deterministic complementary-factor condition exposed at this level is

```text
gcd(sqf(E),K_Z)=1,
```

while all remaining canonical/orientation/root-origin/reverse-completion conditions stay in a residual Boolean `w_res`.

`Stage14-s7-94` sets

```text
q=u*v.
```

Since `gcd(u,v)=1`, every full prime power of `q` is assigned wholly to one side. Thus `(u,v)` is exactly a prime-power orientation of `q`, with `2^omega(q)=B^o(1)` possibilities for fixed `q`, and

```text
log(u/v)=sum_p epsilon_p v_p(q) log p.
```

It also separates inner-ratio endpoints from the radial product-window endpoints already removed by 4fi. The bare constraints `gcd(u,v)=1`, `uv|n` do not make small-one-side configurations fixed-power rare across outer `n`; no second endpoint saving is charged.

`Stage14-s7-95` identifies `u` as a unitary divisor of `q`:

```text
u || q,
v=q/u.
```

If

```text
R_phys(n)=[r_-(n),r_+(n)],
```

then exactly

```text
u/v in R_phys(n)
<=>
sqrt(q*r_-(n)) <= u <= sqrt(q*r_+(n)).
```

The heavy incidence is therefore

```text
I_unit
 = sum_{n in N_int(theta)}
   sum_{q|n}
   sum_{u||q, u in U_phys(n,q)}
     W_unit(n,q,u),
```

where

```text
W_unit(n,q,u)
 = 1_{gcd(sqf(n/q),K_Z)=1}
   * w_res(n,u,q/u,n/q),
```

and a survivor requires

```text
I_unit>=B^(mu-o(1)).
```

This materially changes the heavy receiver to

```text
FixedPrimitiveRayFixedAgreementPairInteriorNormalizedRadialWeightedUnitaryDivisorShortIntervalPhysicalIncidenceWithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu.
```

Merged q14/Ford remains near geometry only. No ordinary-divisor or generic unitary-divisor density is charged because the complementary `E=n/q` physical weight remains correlated with the same candidate. No new sH is opened; `Stage14-s7-96` should open `w_res` through the merged fixed-data reverse reconstruction and determine whether it collapses to divisor-many local labels or remains a genuine canonical correlation.
