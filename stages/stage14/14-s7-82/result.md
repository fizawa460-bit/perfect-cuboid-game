# Stage14-s7-82 — exact radial square-dilation equation in the second reciprocal packet

## Status

`COMPLETE_HEAVY_RAY_RADIAL_SCALE_TO_EXACT_SQUARE_DILATE_SECOND_RECIPROCAL_PACKET`

Consumes batch-local `Stage14-s7-81`, merged `Stage14-s7-80`, merged `Stage14-4eq`, and merged `Stage14-Work-boX27`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Fixed primitive-ray data and moving radius

On the surviving heavy-ray branch freeze

```text
C,
(x,y), gcd(x,y)=1,
N0=x^2+y^2=C*m0,
```

and let the raw reciprocal vector vary only through

```text
X=h*x,
Y=h*y.
```

The signed quotient coordinates remain exactly

```text
Q_xi+P_xi=h*x,
Q_xi-P_xi=h*y,
```

so

```text
P_xi=h*(x-y)/2,
Q_xi=h*(x+y)/2.
```

Parity only imposes the fixed O(1) condition needed for these to be integral; it cannot supply a fixed-power density loss.

```text
RADIAL_SIGNED_QUOTIENT_LINE_EXACT=true
RADIAL_PARITY_COST=O1
```

## 2. Insert the radius into the exact second reciprocal identity

Merged `4eq` uses the exact identity

```text
X^2-Y^2
 = 4*Xr*Yr*epsilon_x*U*V.
```

Substituting `X=h*x`, `Y=h*y` gives

```text
h^2*(x^2-y^2)
 = 4*Xr*Yr*epsilon_x*U*V.
```

Define the fixed primitive-ray determinant factor

```text
D0 := x^2-y^2.
```

Then every accepted radial scale satisfies the exact physical factor equation

```text
h^2*D0
 = 4*epsilon_x*Xr*Yr*U*V.
```

The only polynomially moving arithmetic on the left is now the square dilation `h^2`; `D0` is fixed on the heavy primitive ray.

```text
HEAVY_RAY_SECOND_RECIPROCAL_SQUARE_DILATE_IDENTITY_EXACT=true
FIXED_PRIMITIVE_RAY_FACTOR_D0_DEFINED=true
RADIAL_POLYNOMIAL_MOBILITY_ENTERS_AS_H_SQUARED=true
```

## 3. Fixed-h fibers stay subpolynomial

For any exact `h`, the integer `h^2 D0` is fixed. The possible tuples

```text
(Xr,Yr,U,V)
```

compatible with the product identity are a subset of the ordered divisor factorizations of `|h^2D0|/4`, together with frozen finite 2-primary/sign data. Hence their multiplicity is `B^o(1)` on the Stage14 polynomial height range.

This recovers the fixed-h part of merged 4eq in a form adapted to the moving radial support. It is not a fresh saving and cannot be recharged.

```text
FIXED_H_SQUARE_DILATE_FACTOR_PACKET_MULTIPLICITY=Bo1
FIXED_H_FACTOR_PACKET_RECHARGE_ALLOWED=false
```

## 4. Common-core overlap with the radius is not a new power source

The primitive root reduction already peeled any fixed-power overlap between the common-core modulus and the common gcd used to define the primitive ray. Thus on the surviving packet the `C`-supported part of `h` is at most subpolynomial in the charged-once sense.

Write schematically

```text
h=h_C*h_perp,
prime support of h_C contained in C,
gcd(h_perp,C)=1,
h_C=B^o(1)
```

on any possible saturation sequence after the existing overlap exceptional support is removed.

The factor `h_C` therefore belongs to the already-charged inner fiber. Polynomial radial mobility, if present, must persist in the `C`-coprime outer part `h_perp` up to `B^o(1)` distortion.

```text
RADIAL_COMMON_CORE_OVERLAP_FIBER=Bo1
POLYNOMIAL_RADIAL_MOBILITY_MUST_PERSIST_OUTSIDE_COMMON_CORE_SUPPORT=true
COMMON_CORE_RADIAL_OVERLAP_RECHARGE_ALLOWED=false
```

No density saving is inferred from coprimality with `C`: for the split-supported polynomial modulus this local condition need not have a uniform fixed-power density deficit.

## 5. Receiver and next

The heavy-ray problem has been rewritten exactly as a moving square-dilate factor packet, but the physical acceptance masks on the right have not yet been projected onto the prime valuations of `h`. This is still an internal reduction of the same radial-support receiver.

The next stage should define the charged-once radial square-dilate acceptance set and isolate the polynomial outer support after all fixed-h divisor fibers are removed.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_82_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_82=COMPLETE_HEAVY_RAY_RADIAL_SCALE_TO_EXACT_SQUARE_DILATE_SECOND_RECIPROCAL_PACKET
HEAVY_RAY_SECOND_RECIPROCAL_SQUARE_DILATE_IDENTITY_EXACT=true
RADIAL_POLYNOMIAL_MOBILITY_ENTERS_AS_H_SQUARED=true
FIXED_H_SQUARE_DILATE_FACTOR_PACKET_MULTIPLICITY=Bo1
RADIAL_COMMON_CORE_OVERLAP_FIBER=Bo1
POLYNOMIAL_RADIAL_MOBILITY_MUST_PERSIST_OUTSIDE_COMMON_CORE_SUPPORT=true
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_82_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-83
```
