# Stage14-4eu — theorem gate for diffuse polynomial Gaussian-factor correlation

## Status

`COMPLETE_DIFFUSE_POLYNOMIAL_GAUSSIAN_FACTOR_CORRELATION_H_GATE`

Consumes batch-local `Stage14-4eq..4et`, merged `Stage14-4eo/4ep`, merged `Stage14-Work-bnX26`, merged `Stage14-q13`, and latest main.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

The diffuse branch has been reduced to the polynomial complementary-factor family

```text
z=epsilon*alpha*beta,
N(alpha)=C=B^(kappa+o(1)), 1/6<=kappa<=1/4,
N(beta)=m=B^(lambda+o(1)), lambda>0,
```

with `alpha` selected by the actual common-core Gaussian root orientation and with the full canonical physical weight retained. Stage14-4es has already closed the `m=B^o(1)` branch at exponent `1/4`.

The elementary reductions now exhausted on this diffuse subroute are:

```text
subpolynomial complementary quotient,
ordinary divisor multiplicity,
primitive two-square representation multiplicity,
finite Gaussian unit/orientation fibers,
standalone Gaussian split-prime support,
post-column finite reconstruction.
```

A further fixed-power saving must control the **joint physical correlation** between the selected common-core Gaussian factor, its polynomial complementary factor, and the canonical allocation background.

Freeze the theorem target

```text
DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
```

in `diffuse-h-target.md`.

A valid theorem/audit must retain the actual factor selection and all physical masks and prove some fixed `delta>0` strong enough to give

```text
DiffusePolynomialQuotientMass(B)
 << B^(1/2-delta+o(1))
```

uniformly on every frozen square-root packet, or an equivalent estimate excluding square-root-scale occupancy.

Merged q13 provides literature leads but no direct import. In particular Wright 2026 becomes relevant only if a mask-preserving convolution and the required small-modulus/Siegel-Walfisz input are proved. Unrestricted Gaussian Type-II estimates or unrelated modulus averages are advisory only.

```text
NEW_DIFFUSE_H_NEEDED=true
NEW_DIFFUSE_H_TARGET=DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
NEW_DIFFUSE_H_BLOCKING_DIFFUSE_BRANCH=true
Q13_DIRECT_DIFFUSE_THEOREM_AVAILABLE=false
```

The complete current mainline survivor list is now

```text
LOW COMMON CORE:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
  -> existing allocation H gate;

POLYNOMIAL COMMON CORE / HEAVY RAY / RADIAL DIFFUSION:
  FixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidence
  -> still internal, not H-gated;

POLYNOMIAL COMMON CORE / GENUINE MOVER:
  FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
  -> existing 4eo mover H gate;

POLYNOMIAL COMMON CORE / DIFFUSE MODULUS / POLYNOMIAL m:
  DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
  -> new 4eu diffuse H gate.
```

Therefore the whole mainline is **not** blocked by H: the heavy-ray radial-diffusion branch remains an internal route.

```text
ALL_CURRENT_MAINLINE_SURVIVORS_THEOREM_GATED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
PREFERRED_NEXT_INTERNAL_RECEIVER=FixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidence
```

```text
STAGE14_4EU=COMPLETE_DIFFUSE_POLYNOMIAL_GAUSSIAN_FACTOR_CORRELATION_H_GATE
DIFFUSE_SMALL_QUOTIENT_BRANCH_CLOSED=true
NEW_DIFFUSE_H_NEEDED=true
NEW_DIFFUSE_H_TARGET=DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
NEW_DIFFUSE_H_BLOCKING_DIFFUSE_BRANCH=true
HEAVY_RAY_RADIAL_DIFFUSION_BRANCH_RETAINED=true
ALL_CURRENT_MAINLINE_SURVIVORS_THEOREM_GATED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4ev
```
