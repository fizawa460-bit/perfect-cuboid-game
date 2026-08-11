# Stage14-4eo — theorem gate for separated fixed-common-core genuine-mover dispersion

## Status

`COMPLETE_SEPARATED_COMMON_CORE_GENUINE_MOVER_DISPERSION_H_GATE`

Consumes corrected batch-local `Stage14-4el/4em/4en`, merged `Stage14-s7-75..77`, merged `Stage14-4ek`, and merged `Stage14-Work-bnX26`.

This stage applies only to the **genuine determinant-mover** alternative. The merged s7-77 heavy primitive-ray alternative remains an independent live receiver.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
HEAVY_RAY_BRANCH_UNCHANGED=true
```

## 1. Exact surviving mover receiver

After 4em/4en, the genuine-mover alternative can survive only on a frozen cell with

```text
C=B^(kappa+o(1)), kappa>0,
|X_j|~R,
|Y_j|~S,
RS/C >= B^(eta+o(1)), eta>0,
```

and exponent-zero mover pair mass satisfying

```text
X1*Y2-X2*Y1=qC,
q!=0,
|q| <= B^o(1) RS/C.
```

The exact modulus `C` is frozen; `q` has polynomial range and may not be frozen at `B^o(1)` cost. Candidate weights remain the actual canonical-allocation / reciprocal physical weights.

```text
MOVER_RECEIVER_FIXED_EXACT_C=true
MOVER_RECEIVER_GENUINE_NONZERO_DETERMINANT_ONLY=true
MOVER_RECEIVER_Q_POLYNOMIAL=true
CANONICAL_PHYSICAL_WEIGHT_CORRELATION_RETAINED=true
```

## 2. Elementary mover reductions are exhausted

On this subbranch the following have already been discharged:

```text
diagonal self-pairs,
zero-determinant pairs by routing them to the separate heavy-ray branch,
near-maximal C~RS genuine movers,
Gaussian splitting/root principal density,
finite per-candidate reconstruction fibers,
second-modulus recharge.
```

Importantly, zero-determinant repeated rays are **not** claimed to have finite global multiplicity. They survive separately as

```text
ConcentratedExactCommonCoreHeavyPrimitiveReciprocalRayIncidence.
```

For the separated mover scale, pointwise affine-line counting reproduces the ambient exponent after polynomial `q` summation. Treating `q` as independent is illegal.

```text
ELEMENTARY_MOVER_AFFINE_LINE_REDUCTION_EXHAUSTED=true
Q_INDEPENDENCE_ASSUMED=false
POINTWISE_MOVER_LATTICE_COUNT_FIXED_POWER_SAVING_PROVED=false
```

## 3. Freeze the mover theorem target

The theorem-ready object is

```text
FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
```

with the immutable contract recorded in `reciprocal-h-target.md`. Here “off-diagonal projective collision” is restricted to the genuine nonzero-determinant mover component.

A successful audit must prove, for some fixed `delta>0`, a bound such as

```text
MoverEnergy_C << M_C^2 B^(-delta+o(1)),
```

or an equivalent bilinear/dispersion/incidence estimate, retaining:

```text
exact correlated modulus C,
primitive distinct projective rays,
canonical allocation background,
range/angular/chart masks,
squarefree/coprime/smooth-rough masks,
charged-once reciprocal candidate fibers,
nonzero determinant quotient with polynomial range.
```

An unrestricted-box estimate or unrelated modulus average is advisory unless a mask-preserving adapter is proved.

```text
NEW_RECIPROCAL_MOVER_H_NEEDED=true
NEW_RECIPROCAL_MOVER_H_TARGET=FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
NEW_RECIPROCAL_MOVER_H_BLOCKING_MOVER_BRANCH=true
```

For compatibility with the Stage14 H ledger:

```text
NEW_RECIPROCAL_H_NEEDED=true
NEW_RECIPROCAL_H_TARGET=FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
```

## 4. Whole mainline remains open

Three other routes remain independent:

```text
low C0 allocation correlation,
concentrated heavy primitive-ray reverse incidence,
diffuse polynomial-C norm-divisor graph.
```

Therefore this H gate blocks only the separated genuine-mover subbranch. Stage14-4ep may continue on the diffuse branch without consuming any positive H conclusion; the heavy-ray branch also remains available for internal work.

```text
WHOLE_MAINLINE_BLOCKED_BY_NEW_RECIPROCAL_H=false
HEAVY_RAY_BRANCH_MAY_CONTINUE_INTERNAL_REDUCTION=true
DIFFUSE_BRANCH_MAY_CONTINUE_INTERNAL_REDUCTION=true
```

## Boundary

```text
STAGE14_4EO=COMPLETE_SEPARATED_COMMON_CORE_GENUINE_MOVER_DISPERSION_H_GATE
ELEMENTARY_MOVER_AFFINE_LINE_REDUCTION_EXHAUSTED=true
MOVER_RECEIVER_Q_POLYNOMIAL=true
HEAVY_RAY_BRANCH_UNCHANGED=true
NEW_RECIPROCAL_MOVER_H_NEEDED=true
NEW_RECIPROCAL_MOVER_H_TARGET=FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
NEW_RECIPROCAL_MOVER_H_BLOCKING_MOVER_BRANCH=true
NEW_RECIPROCAL_H_NEEDED=true
NEW_RECIPROCAL_H_TARGET=FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
WHOLE_MAINLINE_BLOCKED_BY_NEW_RECIPROCAL_H=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4ep
```
