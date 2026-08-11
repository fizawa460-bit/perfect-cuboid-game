# Stage14-4eo — theorem gate for separated fixed-common-core off-diagonal projective collision energy

## Status

`COMPLETE_SEPARATED_COMMON_CORE_OFFDIAGONAL_PROJECTIVE_COLLISION_DISPERSION_H_GATE`

Consumes batch-local `Stage14-4el/4em/4en`, merged `Stage14-4ek`, and merged `Stage14-Work-bnX26`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exact surviving concentrated receiver

After 4el and 4en, a concentrated polynomial-common-core saturating branch can only survive on a frozen cell with

```text
C=B^(kappa+o(1)), kappa>0,
|X_j|~R,
|Y_j|~S,
RS/C >= B^(eta+o(1))
```

for some fixed `eta>0`, and with exponent-zero weighted mass of genuine off-diagonal pairs satisfying

```text
X1*Y2-X2*Y1 = q C,
q != 0,
|q| <= B^o(1) RS/C.
```

The exact modulus `C` is frozen; the determinant quotient `q` remains polynomial and may not be frozen at `B^o(1)` cost.

All candidate weights remain the actual canonical-allocation / reciprocal physical weights. They are not arbitrary independent box weights.

```text
CONCENTRATED_RECEIVER_FIXED_EXACT_C=true
CONCENTRATED_RECEIVER_GENUINE_OFFDIAGONAL_ONLY=true
CONCENTRATED_RECEIVER_Q_POLYNOMIAL=true
CANONICAL_PHYSICAL_WEIGHT_CORRELATION_RETAINED=true
```

## 2. Elementary reductions are exhausted on this branch

The following sources have already been removed or discharged:

```text
diagonal collisions,
exact rational proportional collisions,
near-maximal C~RS fixed-quotient collisions,
Gaussian splitting/root principal density,
finite reciprocal/allocation witness multiplicity,
second-modulus recharge.
```

For the surviving scale, the affine-line parameter `t` can range polynomially after `q` ranges polynomially. Pointwise lattice counting reproduces the ambient pair exponent and does not give a uniform fixed-power energy deficit.

Likewise treating `q` as an independent uniformly distributed variable is illegal: it is defined by the same physical pair and the same exact modulus `C`.

```text
ELEMENTARY_FIXED_Q_AFFINE_LINE_REDUCTION_EXHAUSTED=true
Q_INDEPENDENCE_ASSUMED=false
POINTWISE_LATTICE_COUNT_FIXED_POWER_SAVING_PROVED=false
```

## 3. Freeze the independent theorem target

The theorem-ready object is

```text
FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
```

with the immutable contract recorded in `reciprocal-h-target.md`.

A successful theorem/audit must prove, for some fixed `delta>0`, a bound strong enough to exclude exponent-zero off-diagonal energy uniformly on every frozen physical packet, schematically

```text
OffDiagEnergy_C
 << M_C^2 B^(-delta+o(1)),
```

or an equivalent bilinear/dispersion/incidence estimate, while retaining:

```text
exact correlated modulus C,
primitive candidate vectors,
canonical allocation background,
range/angular/chart masks,
squarefree/coprime/smooth-rough masks,
charged-once reciprocal candidate fibers,
nonzero determinant quotient with polynomial range.
```

An estimate for unrestricted box points, independent coefficient sequences, or a different modulus average is advisory only unless a mask-preserving adapter is proved.

```text
NEW_RECIPROCAL_H_NEEDED=true
NEW_RECIPROCAL_H_TARGET=FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
NEW_RECIPROCAL_H_BLOCKING_CONCENTRATED_BRANCH=true
```

## 4. Whole mainline is not blocked

The low-common-core allocation branch already has the separate merged-4ef H target

```text
CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity.
```

The diffuse polynomial-common-core branch from 4ek is also independent of the exact-modulus concentrated branch and still admits internal reduction. Therefore this new H gate blocks only the concentrated subroute; the requested batch may continue to Stage14-4ep on the diffuse branch without consuming any positive H conclusion.

```text
WHOLE_MAINLINE_BLOCKED_BY_NEW_RECIPROCAL_H=false
DIFFUSE_BRANCH_MAY_CONTINUE_INTERNAL_REDUCTION=true
```

## Boundary

```text
STAGE14_4EO=COMPLETE_SEPARATED_COMMON_CORE_OFFDIAGONAL_PROJECTIVE_COLLISION_DISPERSION_H_GATE
ELEMENTARY_FIXED_Q_AFFINE_LINE_REDUCTION_EXHAUSTED=true
CONCENTRATED_RECEIVER_Q_POLYNOMIAL=true
NEW_RECIPROCAL_H_NEEDED=true
NEW_RECIPROCAL_H_TARGET=FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
NEW_RECIPROCAL_H_BLOCKING_CONCENTRATED_BRANCH=true
WHOLE_MAINLINE_BLOCKED_BY_NEW_RECIPROCAL_H=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4ep
```
