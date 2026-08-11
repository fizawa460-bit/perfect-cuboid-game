# Stage14-s7-83 — radial square-dilate physical-support receiver

## Status

`COMPLETE_HEAVY_RAY_RADIAL_SUPPORT_TO_SQUARE_DILATE_PHYSICAL_FACTOR_ACCEPTANCE_RECEIVER`

Consumes batch-local `Stage14-s7-81/82`, merged `Stage14-4eq`, merged `Stage14-Work-boX27`, and latest merged main at batch start.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Charged-once accepted radial support

Fix the heavy primitive-ray packet

```text
C,
(x,y), gcd(x,y)=1,
N0=x^2+y^2=C*m0,
D0=x^2-y^2,
```

and one frozen raw reciprocal range/chart/orientation cell. Define

```text
H_phys(C,x,y)
```

to be the set of exact integers `h>=1` for which there exists at least one full canonical physical background producing

```text
(X,Y)=h(x,y)
```

and satisfying all original primitive, range/angular, squarefree/coprime, allocation, reciprocal and post-column masks.

Merged `4eq` gives uniformly

```text
1 <= # backgrounds above h <= B^o(1)
```

for `h in H_phys`. Therefore the charged-once heavy-ray incidence mass is exponent-equivalent to

```text
# H_phys(C,x,y).
```

```text
HEAVY_RAY_MASS_EXPONENT_EQUIVALENT_TO_ACCEPTED_RADIAL_SUPPORT=true
FIXED_H_BACKGROUND_FIBER_ALREADY_CHARGED=true
```

## 2. Exact square-dilate acceptance equation

Stage14-s7-82 gives for every accepted `h`

```text
h^2*D0
 = 4*epsilon_x*Xr*Yr*U*V.
```

Thus `h` belongs to `H_phys(C,x,y)` only if the square dilate `h^2 D0` admits a physical factor packet

```text
(Xr,Yr,U,V; finite decorations)
```

that also reconstructs a canonical background satisfying every retained mask.

Conversely, when such a complete charged-once physical factor packet exists, the exact reciprocal identities and the merged reconstruction direction recover an accepted background with only `B^o(1)` multiplicity.

Hence the heavy-ray radial branch is exponent-equivalent to the support of physical factorizations of the fixed integer `D0` under moving square dilation `h^2`.

```text
RADIAL_ACCEPTANCE_IS_SQUARE_DILATE_PHYSICAL_FACTOR_SUPPORT=true
SQUARE_DILATE_TO_BACKGROUND_FIBER=Bo1
```

## 3. Prime-valuation form of the moving outer coordinate

For every prime `ell`,

```text
v_ell(h^2*D0)=2*v_ell(h)+v_ell(D0).
```

The fixed term `v_ell(D0)` is part of the primitive-ray packet. All polynomial mobility from new radial primes enters through the even increment

```text
2*v_ell(h).
```

The right-hand physical factors distribute this valuation subject to the original masks. No assumption is made here that `Xr,Yr,U,V` are mutually coprime or squarefree beyond what the original packet actually imposes.

The fixed-h number of admissible valuation allocations remains `B^o(1)`; what may be polynomial is the set of distinct `h` whose square-dilate valuation pattern admits at least one physical allocation.

```text
RADIAL_PRIME_VALUATIONS_ENTER_AS_EVEN_MOVING_INCREMENTS=true
FIXED_H_VALUATION_ALLOCATION_FIBER=Bo1
POLYNOMIAL_OUTER_COORDINATE_IS_RADIAL_SQUARE_DILATION_SUPPORT=true
```

## 4. Material receiver change

The previous heavy-ray receiver

```text
FixedPrimitiveReciprocalRayDiffuseRadialScalePhysicalIncidence
```

still described acceptance at the level of an opaque radial parameter. After s7-81..83, every subpolynomial reverse/factor fiber has been removed and the exact arithmetic carrier is visible:

```text
FixedPrimitiveReciprocalRayPolynomialRadialSquareDilationPhysicalFactorSupport.
```

The live question is now whether polynomially many `h` can make

```text
h^2*D0
```

admit the required canonical physical factor allocation and reconstruction under the full masks.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveReciprocalRayPolynomialRadialSquareDilationPhysicalFactorSupport
RECEIVER_MATERIALLY_CHANGED=true
```

This is distinct from the existing mover H target and from the diffuse complementary-Gaussian-factor H target. Neither can be cross-promoted onto the radial square-dilate support.

## 5. H decision

No new `sH` is required at this boundary. The square-dilate receiver has just become explicit, but its mask-sensitive prime-valuation coefficient system has not yet been separated. An external theorem audit now would be premature and would risk treating the `B^o(1)` valuation-allocation fiber as an independent density source.

The next internal stage should project the retained squarefree/coprime/allocation masks onto the moving prime valuations of `h` and decide whether the radial support becomes a sieve condition, a smooth/rough support condition, or a correlated multiplicative-weight problem.

```text
S7_83_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_83=COMPLETE_HEAVY_RAY_RADIAL_SUPPORT_TO_SQUARE_DILATE_PHYSICAL_FACTOR_ACCEPTANCE_RECEIVER
HEAVY_RAY_MASS_EXPONENT_EQUIVALENT_TO_ACCEPTED_RADIAL_SUPPORT=true
RADIAL_ACCEPTANCE_IS_SQUARE_DILATE_PHYSICAL_FACTOR_SUPPORT=true
RADIAL_PRIME_VALUATIONS_ENTER_AS_EVEN_MOVING_INCREMENTS=true
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveReciprocalRayPolynomialRadialSquareDilationPhysicalFactorSupport
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_83_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-84
```
