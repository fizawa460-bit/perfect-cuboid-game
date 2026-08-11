# Stage14-s7-80 — heavy primitive ray collapses to radial signed-quotient support or fixed-data upstream reverse fiber

## Status

`COMPLETE_HEAVY_RAY_TO_RADIAL_SIGNED_QUOTIENT_SUPPORT_OR_FIXED_DATA_BACKGROUND_FIBER_SPLIT`

Consumes batch-local `Stage14-s7-78/79`, merged `Stage14-s7-70/77`, and merged mainline `Stage14-4el..4ep`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exact signed-quotient radial line

On the fixed primitive heavy ray `(x,y)` the unprimitive reciprocal coordinates satisfy

```text
X=h*x,
Y=h*y.
```

Merged s7-70 defines

```text
Q_xi+P_xi=X,
Q_xi-P_xi=Y.
```

Therefore exactly

```text
2 Q_xi = h(x+y),
2 P_xi = h(x-y).
```

Equivalently every heavy-ray reciprocal signed-quotient pair lies on the one-dimensional rational line

```text
(P_xi,Q_xi)
 = h/2 * (x-y,x+y),
```

with the physical parity condition selecting the admissible integer `h` values.

```text
HEAVY_RAY_SIGNED_QUOTIENTS_LIE_ON_ONE_RADIAL_LINE=true
RADIAL_PARAMETER_IS_EXACTLY_H=true
```

There is no independent two-dimensional polynomial `(P_xi,Q_xi)` support on a fixed primitive ray.

## 2. Fixed h freezes all reciprocal-side scalar data up to B^o(1)

Fix one exact admissible `h`. Then

```text
X,Y,P_xi,Q_xi
```

are fixed. Stage14-s7-79 shows the decompositions

```text
X=p*c,
Y=q*d
```

have only `B^o(1)` possibilities. Freezing one such factor tuple therefore costs only `B^o(1)` relative to the exact-`h` incidence mass.

Together with the already-fixed

```text
C,
(x,y),
N0=x^2+y^2,
m0=N0/C,
```

a concentrated exact-`h` heavy packet can be localized to one reciprocal-side data tuple

```text
(C,x,y,h,p,q,c,d,P_xi,Q_xi)
```

with only `B^o(1)` loss.

```text
FIXED_H_FREEZES_SIGNED_QUOTIENT_PAIR=true
FIXED_H_RECIPROCAL_DATA_DICTIONARY=Bo1
```

## 3. What is not proved by the reciprocal reconstruction

The merged finite-fiber statements are conditional on stronger upstream data such as the canonical allocation witness or the reverse-reciprocal `(U,V,M)` packet. They do not currently prove that fixing only the reciprocal-side tuple above determines the primitive slope / canonical allocation background with `B^o(1)` multiplicity.

Therefore it would be circular to declare the exact-`h` heavy branch closed by the existing completion fiber.

Define the remaining exact-data reverse fiber

```text
F_back(C,x,y,h,p,q,c,d)
 := {canonical physical backgrounds producing this fixed reciprocal tuple}.
```

Its uniform size is presently unproved.

```text
FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=UNPROVED
EXISTING_COMPLETION_FIBER_REVERSED_ILLEGALLY=false
```

## 4. Material heavy-ray receiver split

Combine the radial concentration/diffusion dichotomy of s7-79 with the exact signed-quotient line.

### Branch HR-C: radial concentration

A `B^o(1)` set of exact radial scales carries exponent-zero heavy-ray mass. Then one exact reciprocal tuple may be frozen at `B^o(1)` loss, and saturation forces

```text
|F_back(C,x,y,h,p,q,c,d)|
```

to have exponent-zero relative mass.

Receiver:

```text
FixedScaledReciprocalVectorCanonicalAllocationReverseFiberMultiplicity.
```

### Branch HR-D: radial diffusion

No `B^o(1)` set of exact `h` values carries exponent-zero mass. Then polynomially many admissible radial dilations are genuinely needed along the one-dimensional line

```text
(P_xi,Q_xi)=h/2*(x-y,x+y).
```

Receiver:

```text
FixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidence.
```

The divisor-factorization dictionary is `B^o(1)` on each radial value and is not a separate polynomial coordinate.

```text
HEAVY_RAY_SPLIT_INTO_FIXED_DATA_BACKGROUND_FIBER_OR_DIFFUSE_RADIAL_SUPPORT=true
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. Complete s-route survivor list

After consuming merged mainline `4el..4ep`, the legal s-route obstructions are now

```text
LOW C0:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity;

POLYNOMIAL C0 / HEAVY RAY / RADIAL CONCENTRATION:
  FixedScaledReciprocalVectorCanonicalAllocationReverseFiberMultiplicity;

POLYNOMIAL C0 / HEAVY RAY / RADIAL DIFFUSION:
  FixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidence;

POLYNOMIAL C0 / GENUINE MOVER:
  FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion
  (existing mover-only H gate; no result consumed);

POLYNOMIAL C0 / DIFFUSE MODULUS:
  DiffuseCanonicalAllocationPrimitiveGaussianNormFactorCorrelation.
```

No survivor has a certified new fixed-power saving.

## 6. H decision

No new sH is opened at this receiver boundary. The two heavy-ray branches have immediate internal questions:

```text
HR-C: substitute the fixed reciprocal tuple back into the canonical allocation equations and bound or expose F_back;
HR-D: determine the physical length and fibers of the radial h coordinate.
```

The diffuse norm-factor branch also still has the internal `m`-scale split from merged 4ep. The separated genuine-mover branch already has its own frozen 4eo auxiliary theorem target, but the whole s route is not blocked on that branch.

```text
S7_80_NEW_AUXILIARY_H_NEEDED=false
EXISTING_MOVER_H_GATE_PENDING=true
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_80=COMPLETE_HEAVY_RAY_TO_RADIAL_SIGNED_QUOTIENT_SUPPORT_OR_FIXED_DATA_BACKGROUND_FIBER_SPLIT
HEAVY_RAY_SIGNED_QUOTIENTS_LIE_ON_ONE_RADIAL_LINE=true
FIXED_H_RECIPROCAL_DATA_DICTIONARY=Bo1
FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=UNPROVED
HEAVY_RAY_SPLIT_INTO_FIXED_DATA_BACKGROUND_FIBER_OR_DIFFUSE_RADIAL_SUPPORT=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_80_NEW_AUXILIARY_H_NEEDED=false
EXISTING_MOVER_H_GATE_PENDING=true
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT=Stage14-s7-81
```