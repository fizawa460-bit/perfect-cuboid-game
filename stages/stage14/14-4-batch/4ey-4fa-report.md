# Stage14-4 batch report — 4ey through 4fa

## Boundary

```text
STAGE14_4_BATCH=COMPLETE
BATCH_START_MAIN_SHA=7f8b5c1f683a68ba2bcf8a9393b26d8872a5c457
BATCH_PUBLICATION_MAIN_SHA=7f8b5c1f683a68ba2bcf8a9393b26d8872a5c457
BATCH_FIRST_STAGE=Stage14-4ey
BATCH_LAST_STAGE=Stage14-4fa
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4fb
```

## Result

Starting from merged 4ex's fixed-kernel square-value receiver:

1. `4ey` uses the squarefree physical xi-agreement product `D=UV=oddpart(RJ)` to solve the squareclass identity exactly:

   ```text
   D = sf_odd(K*Z),
   Z=oddpart(Xr*Yr).
   ```

   Thus `(U,V)` is divisor-many once `(K,Z)` is fixed.

2. `4ez` defines `G=gcd(D,K)` and proves

   ```text
   D/G | rad(Z),
   G >= D/Z = B^(4phi-1/2-o(1)) >= B^(1/3-o(1)).
   ```

   Since `G|K` and the ray kernel `K` is fixed, one exact large `G` may be frozen at `B^o(1)` cost.

3. `4fa` allocates `G=G_U G_V` into the coprime primitive agreement pair and reapplies the existing common-core primitive root-line lemma **conditionally on the new large divisor**. The residual pair has product `UV/G`, so

   ```text
   #(U,V | fixed C,K,G,allocation)=B^o(1)
   ```

   because `(UV/G)/C=B^(1/4-g+o(1))` and `g>=1/3-o(1)`.

   After `(U,V)` is fixed, only the radial square scale remains, with

   ```text
   #h <= B^(1/4-phi+o(1)) <= B^(1/24+o(1)).
   ```

The heavy-ray branch is not declared closed because the concentrated exact-`C` collision ledger supplies only `M_C=B^(eta+o(1))` for an unspecified fixed `eta>0`; no merged uniform lower bound `eta>1/24` exists. The receiver nonetheless changes materially from an arbitrary fixed-kernel square-value incidence to

```text
FixedPrimitiveRayFixedAgreementPairShortRadialSquareScalePhysicalIncidence.
```

## Publication recheck

Latest main remained `7f8b5c1f683a68ba2bcf8a9393b26d8872a5c457`. The newly merged fixed-U `t118..t120` route ends at generic scalar-norm support and proves no charged-once adapter to the global heavy-ray `(K,G,h)` coordinates, so no fixed-U saving is cross-promoted.

## Other mainline branches

Unchanged pending branches remain:

```text
LOW C:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity

POLYNOMIAL C / GENUINE MOVER:
  FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion

POLYNOMIAL C / DIFFUSE POLYNOMIAL COMPLEMENTARY NORM:
  DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
```

The heavy-ray branch still has an internal successor, so the whole mainline is not H-blocked.
