# Stage14-s-batch report — s7-90 through s7-92

```text
STAGE14_S_BATCH=COMPLETE
BATCH_START_MAIN_SHA=d519dcccee5bedb4844dbcee5cb4b5171600c0bf
BATCH_PUBLICATION_MAIN_SHA=d519dcccee5bedb4844dbcee5cb4b5171600c0bf
BATCH_FIRST_STAGE=Stage14-s7-90
BATCH_LAST_STAGE=Stage14-s7-92
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_S_RECEIVER=FixedPrimitiveRayFixedAgreementPairNormalizedRadialPrimitiveCoprimeDivisorRatioShortWindowPhysicalOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-93
```

This batch consumes merged `s7-87..89`, merged mainline `4fe..4fg`, and merged `Work-brX30` on latest merged main.

`Stage14-s7-90` peels the common gcd

```text
g=gcd(a1,b1),
a1=g*u,
b1=g*v,
gcd(u,v)=1,
```

and absorbs the squarefree/shared common magnitude into

```text
E=J1*g^2.
```

The normalized physical packet becomes exactly

```text
n=E*u*v,
|Xr|=alpha*E*u^2,
|Yr|=beta*E*v^2,
```

with `sqf(E)=J1`. Thus the moving root geometry splits into one common dilation `E` and one primitive coprime projective ratio `(u:v)`.

`Stage14-s7-91` eliminates `E=n/(uv)` and obtains

```text
|Xr|=alpha*n*(u/v),
|Yr|=beta*n*(v/u),
uv|n.
```

Hence the merged reciprocal divisor coordinate is simply

```text
L_s/n=u/v.
```

For frozen root windows `I_X=[X_-,X_+]`, `I_Y=[Y_-,Y_+]`, physical acceptance projects exactly to

```text
u/v in R_phys(n)
 = [X_-/(alpha n),X_+/(alpha n)]
   intersect
   [beta n/Y_+,beta n/Y_-],
```

plus the complementary factor `E=n/(uv)` squareclass/gcd masks and every remaining physical/canonical mask.

`Stage14-s7-92` separates the archimedean and arithmetic content. The real interval intersection is nonempty exactly when

```text
X_-Y_-/(alpha beta) <= n^2 <= X_+Y_+/(alpha beta).
```

After the legal `B^o(1)` dyadic localization, this product window has only `B^o(1)` multiplicative width but can still contain polynomially many integers; it gives no fixed-power saving by itself.

For each accepted `n`, however, the required primitive ratio lies in a multiplicatively `B^o(1)`-short interval and must satisfy

```text
gcd(u,v)=1,
uv|n,
E=n/(uv),
```

with all inherited complementary-`E` squareclass and canonical masks. Fixed-`n` candidates remain only `B^o(1)`; the polynomial obstruction is occupancy across at least `B^(mu-o(1))` distinct `n`.

This materially changes the heavy-ray receiver to

```text
FixedPrimitiveRayFixedAgreementPairNormalizedRadialPrimitiveCoprimeDivisorRatioShortWindowPhysicalOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi.
```

No generic divisor-ratio, squarefree, or dyadic-window density is charged. No new `sH` is opened. `Stage14-s7-93` should split endpoint/subpolynomial primitive ratios from genuinely interior balanced ratios and freeze the exact inherited weight on `E=n/(uv)` before any external theorem audit.

```text
PUBLICATION_MAIN_RECHECK_COMPLETE=true
NEW_MERGED_CONSUMER_AFTER_BATCH_START=false
```
