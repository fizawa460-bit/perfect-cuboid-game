# Stage14-s-batch report — s7-87 through s7-89

```text
STAGE14_S_BATCH=COMPLETE
BATCH_START_MAIN_SHA=c5c84d2727caad0afdc08dec69f6696716f21b38
BATCH_PUBLICATION_MAIN_SHA=c5c84d2727caad0afdc08dec69f6696716f21b38
BATCH_FIRST_STAGE=Stage14-s7-87
BATCH_LAST_STAGE=Stage14-s7-89
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_S_RECEIVER=FixedPrimitiveRayFixedAgreementPairSharedSquarefreeDilationFixedCoefficientSquareRatioRadialPhysicalOccupancy_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-90
```

This batch consumes merged `s7-84..86`, merged mainline `4fb..4fd`, and merged `Work-bqX29`.

`Stage14-s7-87` records the mainline/Work supersession of the old s7-86 mass-capacity gap.  A surviving heavy ray has

```text
0<mu<=rho(phi)=1/4-phi<=1/24,
B^(mu-o(1)) <= #H_* <= B^(rho(phi)+o(1)).
```

Using the exact s7-86 relation

```text
d0*J*a*b=c0*h,
gcd(c0,d0)=1,
```

it proves

```text
h=d0*n,
J*a*b=c0*n.
```

If `h=B^(sigma+o(1))` and `d0=B^(lambda+o(1))`, survival forces `lambda<=sigma-mu`; a near-capacity radial packet therefore forces `d0=B^o(1)`.

`Stage14-s7-88` allocates the fixed numerator `c0` prime-power by prime-power among `(J,a,b)`.  There are only `d_3(c0)=B^o(1)` allocations, so one can freeze

```text
c0=c_J*c_a*c_b,
J=c_J*J1,
a=c_a*a1,
b=c_b*b1
```

and obtain the coefficient-free exact equation

```text
n=J1*a1*b1,
h=d0*J1*a1*b1.
```

For fixed `n`, the normalized triple fiber is still `B^o(1)`.

`Stage14-s7-89` substitutes the peel back into the two physical root factors.  For fixed positive coefficients

```text
alpha=c_J*A*c_a^2,
beta=c_J*B*c_b^2,
```

every accepted normalized point has

```text
|Xr|=alpha*J1*a1^2,
|Yr|=beta*J1*b1^2,
h=d0*J1*a1*b1.
```

Hence `J1` is a shared squarefree dilation, while the projective root ratio is

```text
|Xr|/|Yr|=(alpha/beta)*(a1/b1)^2
```

and is independent of `J1`.  This materially changes the heavy-ray receiver from unstructured polynomial radial occupancy to

```text
FixedPrimitiveRayFixedAgreementPairSharedSquarefreeDilationFixedCoefficientSquareRatioRadialPhysicalOccupancy.
```

No generic square/squarefree/multiplication-table density is recharged.  No new `sH` is opened: the next internal stage must project the actual physical root-origin/range/reverse-completion masks onto the normalized `(J1,a1,b1)` coefficient system before an external theorem audit is justified.

```text
PUBLICATION_MAIN_RECHECK_COMPLETE=true
NEW_MERGED_CONSUMER_AFTER_BATCH_START=false
```
