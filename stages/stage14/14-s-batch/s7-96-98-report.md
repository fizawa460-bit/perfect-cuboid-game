# Stage14-s-batch report — s7-96 through s7-98

```text
STAGE14_S_BATCH=COMPLETE
BATCH_START_MAIN_SHA=43c2beeda0c9c5af2154d6deca5912d5be9e3ab2
BATCH_PUBLICATION_MAIN_SHA=43c2beeda0c9c5af2154d6deca5912d5be9e3ab2
BATCH_FIRST_STAGE=Stage14-s7-96
BATCH_LAST_STAGE=Stage14-s7-98
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_S_RECEIVER=FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence_OR_PolynomialComplementaryDilationFixedPrimitiveProductCanonicalReverseOuterOccupancy_OR_PolynomialComplementaryDilationPolynomialPrimitiveProductInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-99
```

Consumes merged `s7-93..95`, merged mainline `4fk..4fm`, and merged `Work-btX32`.

`Stage14-s7-96` synchronizes the s packet with the stronger merged physical-weight description:

```text
W_unit(n,q,u)=m_E(E)*m_cpl(n,u,q/u,E),
E=n/q.
```

The factorization is only a conjunction split by proven variable dependence; no independence is assumed. It imports the merged `4fm` split `E=B^o(1)` versus polynomial `E` without recharging it.

`Stage14-s7-97` freezes exact `E=E0` on the subpolynomial branch. The local complementary mask is then constant `1` on a surviving cell. Writing `m=n/E0` gives

```text
m=uv,
gcd(u,v)=1,
u||m,
u^2/m in R_int(E0*m),
```

weighted only by

```text
c_E0(m,u)=m_cpl(E0*m,u,m/u,E0).
```

Fixed `(E0,m,u)` has only `B^o(1)` full physical reverse-completion multiplicity by the merged fixed-radial reconstruction, but existence of a completion is not automatic. Thus the canonical/reverse Boolean remains a genuine inner weight and q14/Ford bounded-distortion transfer is still unproved.

`Stage14-s7-98` treats polynomial `E` and freezes the primitive-product scale `m=B^(kappa+o(1))`.

- if `kappa=0`, exact `m` and one unitary orientation `u||m` freeze at `B^o(1)` cost, so all polynomial entropy is in `E`; the branch becomes one-dimensional canonical/reverse outer occupancy;
- if `kappa>0`, both `E` and `m` remain polynomial and the unitary selector remains coupled to the canonical/reverse Boolean, giving a genuine two-scale correlation.

This materially changes the heavy receiver to

```text
FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence
OR
PolynomialComplementaryDilationFixedPrimitiveProductCanonicalReverseOuterOccupancy
OR
PolynomialComplementaryDilationPolynomialPrimitiveProductInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation.
```

No generic divisor/unitary-divisor density, fixed-n fiber, reverse-completion multiplicity, radial-endpoint saving, or q14/Ford saving is recharged. No new `sH` is opened. `Stage14-s7-99` should open the canonical/reverse Boolean on the fixed-`E` and fixed-primitive-product branches first, because they have only one polynomial outer coordinate left.